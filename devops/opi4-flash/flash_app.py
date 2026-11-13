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
from image_settings import validate


class FlashApp:
    def __init__(self, root):
        self.root = root
        self.events = queue.Queue()
        self.running = False
        self.last_output = None
        self.branch = tk.StringVar(value='deploy')
        self.ssid = tk.StringVar()
        self.wifi_password = tk.StringVar()
        self.gemini_key = tk.StringVar()
        self.timezone = tk.StringVar(value='America/Los_Angeles')
        desktop = Path.home() / 'Desktop'
        self.output_parent = tk.StringVar(value=str(desktop if desktop.is_dir() else Path.home()))
        self.status = tk.StringVar(value='Ready to build an Orange Pi 4 Pro image.')
        self._layout()
        root.after(100, self._poll)
        root.protocol('WM_DELETE_WINDOW', self._close)

    def _layout(self):
        self.root.title('Ember Image Builder')
        self.root.minsize(660, 620)
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill='both', expand=True)
        ttk.Label(frame, text='Ember · Orange Pi 4 Pro', font=('TkDefaultFont', 17, 'bold')).grid(
            row=0, column=0, columnspan=3, sticky='w', pady=(0, 5))
        ttk.Label(frame, text='Build a private SD image on this laptop using a local Linux VM.').grid(
            row=1, column=0, columnspan=3, sticky='w', pady=(0, 18))
        fields = [
            ('Wi-Fi name', self.ssid, None),
            ('Wi-Fi password', self.wifi_password, '*'),
            ('Ember branch', self.branch, None),
            ('Time zone', self.timezone, None),
            ('Gemini key (optional)', self.gemini_key, '*'),
        ]
        for row, (label, value, mask) in enumerate(fields, start=2):
            ttk.Label(frame, text=label).grid(row=row, column=0, sticky='w', pady=5)
            entry = ttk.Entry(frame, textvariable=value, show=mask or '')
            entry.grid(row=row, column=1, columnspan=2, sticky='ew', padx=(12, 0), pady=5)
        ttk.Label(frame, text='Save image in').grid(row=7, column=0, sticky='w', pady=5)
        ttk.Entry(frame, textvariable=self.output_parent).grid(
            row=7, column=1, sticky='ew', padx=(12, 8), pady=5)
        ttk.Button(frame, text='Browse…', command=self._browse).grid(row=7, column=2, sticky='ew')
        ttk.Label(frame, text='Needs Multipass and about 35 GiB free. First build may take an hour.').grid(
            row=8, column=0, columnspan=3, sticky='w', pady=(6, 12))
        actions = ttk.Frame(frame)
        actions.grid(row=9, column=0, columnspan=3, sticky='w')
        self.build_button = ttk.Button(actions, text='Build image', command=self._start)
        self.build_button.pack(side='left')
        ttk.Button(actions, text='Install Multipass', command=lambda: webbrowser.open(
            'https://canonical.com/multipass/docs/latest/how-to-guides/install-multipass/')).pack(
                side='left', padx=8)
        self.open_button = ttk.Button(actions, text='Open finished folder', command=self._open_output,
                                      state='disabled')
        self.open_button.pack(side='left')
        ttk.Label(frame, textvariable=self.status, wraplength=620).grid(
            row=10, column=0, columnspan=3, sticky='w', pady=(18, 6))
        self.progress = ttk.Progressbar(frame, mode='indeterminate')
        self.progress.grid(row=11, column=0, columnspan=3, sticky='ew', pady=(0, 12))
        self.log = tk.Text(frame, height=12, wrap='word', state='disabled')
        self.log.grid(row=12, column=0, columnspan=3, sticky='nsew')
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(12, weight=1)

    def _browse(self):
        chosen = filedialog.askdirectory(initialdir=self.output_parent.get())
        if chosen:
            self.output_parent.set(chosen)

    def _start(self):
        settings = {'branch': self.branch.get().strip(),
                    'wifi': {'ssid': self.ssid.get(), 'password': self.wifi_password.get()},
                    'gemini_api_key': self.gemini_key.get().strip(),
                    'timezone': self.timezone.get().strip()}
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
                if kind == 'log':
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
