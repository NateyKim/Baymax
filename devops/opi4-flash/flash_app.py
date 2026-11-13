"""Clickable image builder for Orange Pi 4 Pro on Windows and macOS."""
import os
from pathlib import Path
import queue
import subprocess
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import webbrowser

from flash_vm import build_image
from image_settings import MAX_WIFI_NETWORKS, validate
from pr_sources import list_opi4_prs


class FlashApp:
    def __init__(self, root):
        self.root = root
        self.events = queue.Queue()
        self.running = False
        self.last_output = None
        self.networks = []
        self.source_options = {'Stable · deploy': {'branch': 'deploy'}}
        self.source = tk.StringVar(value='Stable · deploy')
        self.gemini_key = tk.StringVar()
        self.linux_password = tk.StringVar()
        self.anydesk_password = tk.StringVar()
        self.show_passwords = tk.BooleanVar(value=False)
        self.timezone = tk.StringVar(value='America/Los_Angeles')
        self.hostname = tk.StringVar()
        desktop = Path.home() / 'Desktop'
        self.output_parent = tk.StringVar(value=str(desktop if desktop.is_dir() else Path.home()))
        self.status = tk.StringVar(value='Add at least one Wi-Fi network, then build an image.')
        self._layout()
        self._refresh_sources()
        root.after(100, self._poll)
        root.protocol('WM_DELETE_WINDOW', self._close)

    def _layout(self):
        self.root.title('Ember Image Builder')
        self.root.minsize(700, 680)
        frame = ttk.Frame(self.root, padding=16)
        frame.pack(fill='both', expand=True)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(12, weight=1)
        ttk.Label(frame, text='Ember · Orange Pi 4 Pro', font=('TkDefaultFont', 17, 'bold')).grid(
            row=0, column=0, columnspan=3, sticky='w')
        ttk.Label(frame, text='Build a private SD image on this laptop using a local Linux VM.').grid(
            row=1, column=0, columnspan=3, sticky='w', pady=(3, 12))

        wifi = ttk.LabelFrame(frame, text='Wi-Fi networks (up to five)', padding=8)
        wifi.grid(row=2, column=0, columnspan=3, sticky='ew', pady=(0, 10))
        wifi.columnconfigure(0, weight=1)
        self.wifi_list = tk.Listbox(wifi, height=4, exportselection=False)
        self.wifi_list.grid(row=0, column=0, rowspan=5, sticky='ew', padx=(0, 8))
        for row, (label, action) in enumerate((
                ('Add Wi-Fi', lambda: self._edit_wifi()),
                ('Edit', lambda: self._edit_wifi(self._selected_wifi())),
                ('Remove', self._remove_wifi),
                ('Move up', lambda: self._move_wifi(-1)),
                ('Move down', lambda: self._move_wifi(1)))):
            ttk.Button(wifi, text=label, command=action).grid(row=row, column=1, sticky='ew', pady=1)

        ttk.Label(frame, text='Ember source').grid(row=3, column=0, sticky='w', pady=3)
        self.source_combo = ttk.Combobox(frame, textvariable=self.source, state='readonly',
                                         values=list(self.source_options))
        self.source_combo.grid(row=3, column=1, sticky='ew', padx=(12, 8), pady=3)
        ttk.Button(frame, text='Refresh PRs', command=self._refresh_sources).grid(
            row=3, column=2, sticky='ew')
        ttk.Label(frame, text='Board name (blank = random)').grid(row=4, column=0, sticky='w', pady=3)
        ttk.Entry(frame, textvariable=self.hostname).grid(
            row=4, column=1, columnspan=2, sticky='ew', padx=(12, 0), pady=3)
        ttk.Label(frame, text='Board time zone (reminders)').grid(row=5, column=0, sticky='w', pady=3)
        ttk.Combobox(frame, textvariable=self.timezone, values=(
            'America/Los_Angeles', 'America/Denver', 'America/Chicago',
            'America/New_York', 'UTC')).grid(row=5, column=1, columnspan=2,
                                           sticky='ew', padx=(12, 0), pady=3)
        self.password_entries = []
        for row, label, value in (
                (6, 'Gemini key (optional)', self.gemini_key),
                (7, 'SSH/sudo password (blank = random)', self.linux_password),
                (8, 'AnyDesk password (blank = random)', self.anydesk_password)):
            ttk.Label(frame, text=label).grid(row=row, column=0, sticky='w', pady=3)
            entry = ttk.Entry(frame, textvariable=value, show='*')
            entry.grid(row=row, column=1, columnspan=2, sticky='ew', padx=(12, 0), pady=3)
            self.password_entries.append(entry)
        ttk.Label(frame, text='Save image in').grid(row=9, column=0, sticky='w', pady=3)
        ttk.Entry(frame, textvariable=self.output_parent).grid(
            row=9, column=1, sticky='ew', padx=(12, 8), pady=3)
        ttk.Button(frame, text='Browse…', command=self._browse).grid(row=9, column=2, sticky='ew')
        ttk.Label(frame, text='Needs Multipass and about 35 GiB free. First build may take an hour.').grid(
            row=10, column=0, columnspan=3, sticky='w', pady=(8, 7))
        actions = ttk.Frame(frame)
        actions.grid(row=11, column=0, columnspan=3, sticky='w')
        self.build_button = ttk.Button(actions, text='Build image', command=self._start)
        self.build_button.pack(side='left')
        ttk.Button(actions, text='Install Multipass', command=lambda: webbrowser.open(
            'https://canonical.com/multipass/docs/latest/how-to-guides/install-multipass/')).pack(
                side='left', padx=8)
        self.open_button = ttk.Button(actions, text='Open finished folder', command=self._open_output,
                                      state='disabled')
        self.open_button.pack(side='left')
        ttk.Checkbutton(actions, text='Show passwords', variable=self.show_passwords,
                        command=self._toggle_passwords).pack(side='left', padx=8)
        progress_area = ttk.Frame(frame)
        progress_area.grid(row=12, column=0, columnspan=3, sticky='nsew', pady=(12, 0))
        progress_area.columnconfigure(0, weight=1)
        progress_area.rowconfigure(2, weight=1)
        ttk.Label(progress_area, textvariable=self.status, wraplength=650).grid(row=0, sticky='w')
        self.progress = ttk.Progressbar(progress_area, mode='indeterminate')
        self.progress.grid(row=1, sticky='ew', pady=(5, 8))
        self.log = tk.Text(progress_area, height=8, wrap='word', state='disabled')
        self.log.grid(row=2, sticky='nsew')

    def _selected_wifi(self):
        chosen = self.wifi_list.curselection()
        return chosen[0] if chosen else None

    def _toggle_passwords(self):
        for entry in self.password_entries:
            entry.configure(show='' if self.show_passwords.get() else '*')

    def _show_wifi(self, selected=None):
        self.wifi_list.delete(0, 'end')
        for index, network in enumerate(self.networks, start=1):
            kind = 'Secured' if network['password'] else 'Open'
            self.wifi_list.insert('end', f"{index}. {network['ssid']}  ·  {kind}")
        if selected is not None:
            self.wifi_list.selection_set(selected)

    def _edit_wifi(self, index=None):
        if index is None and len(self.networks) >= MAX_WIFI_NETWORKS:
            messagebox.showerror('Wi-Fi limit', f'Add up to {MAX_WIFI_NETWORKS} networks.')
            return
        existing = self.networks[index] if index is not None else {'ssid': '', 'password': ''}
        dialog = tk.Toplevel(self.root)
        dialog.title('Wi-Fi network')
        dialog.transient(self.root)
        dialog.resizable(False, False)
        dialog.grab_set()
        fields = ttk.Frame(dialog, padding=16)
        fields.pack(fill='both', expand=True)
        name = tk.StringVar(value=existing['ssid'])
        password = tk.StringVar(value=existing['password'])
        is_open = tk.BooleanVar(value=not existing['password'])
        ttk.Label(fields, text='Network name (SSID)').grid(row=0, column=0, sticky='w', pady=5)
        name_entry = ttk.Entry(fields, textvariable=name, width=36)
        name_entry.grid(row=0, column=1, pady=5)
        ttk.Label(fields, text='Password').grid(row=1, column=0, sticky='w', pady=5)
        password_entry = ttk.Entry(fields, textvariable=password, show='*', width=36)
        password_entry.grid(row=1, column=1, pady=5)
        def toggle_password():
            password_entry.configure(state='disabled' if is_open.get() else 'normal')
        ttk.Checkbutton(fields, text='Open network (no password)', variable=is_open,
                        command=toggle_password).grid(row=2, column=1, sticky='w', pady=5)
        show_wifi_password = tk.BooleanVar(value=False)
        ttk.Checkbutton(fields, text='Show password', variable=show_wifi_password,
                        command=lambda: password_entry.configure(
                            show='' if show_wifi_password.get() else '*')).grid(
                                row=3, column=1, sticky='w', pady=5)
        toggle_password()

        def save():
            network = {'ssid': name.get().strip(),
                       'password': '' if is_open.get() else password.get()}
            candidate = list(self.networks)
            if index is None:
                candidate.append(network)
            else:
                candidate[index] = network
            try:
                validate({'branch': 'deploy', 'wifi_networks': candidate, 'gemini_api_key': ''})
            except ValueError as error:
                messagebox.showerror('Check Wi-Fi', str(error), parent=dialog)
                return
            self.networks = candidate
            self._show_wifi(index if index is not None else len(candidate) - 1)
            dialog.destroy()
        ttk.Button(fields, text='Save network', command=save).grid(row=4, column=1, sticky='e', pady=(9, 0))
        name_entry.focus_set()

    def _remove_wifi(self):
        index = self._selected_wifi()
        if index is not None:
            del self.networks[index]
            self._show_wifi(min(index, len(self.networks) - 1) if self.networks else None)

    def _move_wifi(self, direction):
        index = self._selected_wifi()
        if index is not None and 0 <= index + direction < len(self.networks):
            self.networks[index], self.networks[index + direction] = (
                self.networks[index + direction], self.networks[index])
            self._show_wifi(index + direction)

    def _refresh_sources(self):
        self.status.set('Loading open Orange Pi PRs…')
        def load():
            try:
                self.events.put(('sources', list_opi4_prs()))
            except Exception as error:
                self.events.put(('sources_error', str(error)))
        threading.Thread(target=load, daemon=True).start()

    def _browse(self):
        chosen = filedialog.askdirectory(initialdir=self.output_parent.get())
        if chosen:
            self.output_parent.set(chosen)

    def _start(self):
        settings = {**self.source_options[self.source.get()],
                    'wifi_networks': list(self.networks),
                    'gemini_api_key': self.gemini_key.get().strip(),
                    'timezone': self.timezone.get().strip()}
        if self.hostname.get().strip():
            settings['hostname'] = self.hostname.get().strip()
        if self.linux_password.get():
            settings['linux_password'] = self.linux_password.get()
        if self.anydesk_password.get():
            settings['anydesk_password'] = self.anydesk_password.get()
        try:
            validate(settings)
        except ValueError as error:
            messagebox.showerror('Check image settings', str(error))
            return
        self.running = True
        self.build_button.configure(state='disabled')
        self.progress.start(12)
        self.status.set('Preparing the Linux VM and building your image…')
        threading.Thread(target=self._worker, args=(settings, self.output_parent.get()),
                         daemon=True).start()

    def _worker(self, settings, output_parent):
        try:
            output, manifest = build_image(settings, output_parent,
                                           lambda line: self.events.put(('log', line)))
            self.events.put(('done', (output, manifest)))
        except Exception as error:
            self.events.put(('error', str(error)))

    def _poll(self):
        try:
            while True:
                kind, value = self.events.get_nowait()
                if kind == 'sources':
                    current = self.source.get()
                    self.source_options = {'Stable · deploy': {'branch': 'deploy'}}
                    for number, title in value:
                        label = f"PR #{number} · {title[:65]}"
                        self.source_options[label] = {'pr': number}
                    self.source_combo.configure(values=list(self.source_options))
                    self.source.set(current if current in self.source_options else 'Stable · deploy')
                    if not self.running and not self.last_output:
                        self.status.set(f'{len(value)} open Orange Pi PR(s) found. Add Wi-Fi to build.')
                elif kind == 'sources_error':
                    if not self.running and not self.last_output:
                        self.status.set('Could not load PRs; stable deploy remains available.')
                elif kind == 'log':
                    self.log.configure(state='normal')
                    self.log.insert('end', value + '\n')
                    self.log.see('end')
                    self.log.configure(state='disabled')
                else:
                    self.running = False
                    self.progress.stop()
                    self.build_button.configure(state='normal')
                    if kind == 'done':
                        self.last_output, manifest = value
                        self.open_button.configure(state='normal')
                        self.status.set(f"Ready: {manifest['hostname']} · {self.last_output}")
                        messagebox.showinfo('Image ready', 'The image checksum passed. Open the folder '
                                            'and write ember-opi4.img to the microSD card with an image writer.')
                    else:
                        self.status.set('Build stopped. See the log below.')
                        messagebox.showerror('Image build stopped', value)
        except queue.Empty:
            pass
        self.root.after(100, self._poll)

    def _open_output(self):
        if sys.platform == 'win32':
            os.startfile(self.last_output)
        else:
            subprocess.Popen(['open', str(self.last_output)])

    def _close(self):
        if self.running:
            messagebox.showinfo('Build in progress', 'Wait for this build to finish before closing the app.')
        else:
            self.root.destroy()


if __name__ == '__main__':
    window = tk.Tk()
    FlashApp(window)
    window.mainloop()
