"""Edit the private first-boot choices (branch, Wi-Fi, Gemini key, time zone) without echoing passwords or keys."""
import argparse
import getpass
import json
import os
from pathlib import Path
import subprocess
import tempfile
from image_settings import DEFAULT_TIMEZONE, REPOSITORY, load, timezone, valid_timezone, validate, wifi_networks


def save_private(path, settings):
    settings = validate(settings)
    path = Path(path)
    descriptor, temporary = tempfile.mkstemp(prefix='.image-settings-', dir=path.parent)
    try:
        with os.fdopen(descriptor, 'w', encoding='utf-8') as stream:
            json.dump(settings, stream, indent=2, ensure_ascii=False)
            stream.write('\n')
        if os.name == 'nt':
            owner = subprocess.check_output(['whoami'], text=True).strip()
            subprocess.run(['icacls.exe', temporary, '/inheritance:r', '/grant:r', owner + ':(F)', 'SYSTEM:(F)'],
                           check=True, stdout=subprocess.DEVNULL)
        else:
            os.chmod(temporary, 0o600)
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--settings', type=Path, default=Path(__file__).parent / 'settings.private.json')
    args = parser.parse_args()
    old = load(args.settings) if args.settings.exists() else {'branch': 'deploy', 'wifi': {'ssid': '', 'password': ''}, 'gemini_api_key': ''}
    if 'pr' in old:
        print(f'These settings followed pull request #{old["pr"]}; images now follow a branch of {REPOSITORY}.')
    current = old.get('branch', 'deploy')
    branch = input(f'Branch to follow [{current}]: ').strip() or current
    primary_wifi = wifi_networks(old)[0]
    ssid = input(f'Wi-Fi name [{primary_wifi["ssid"]}]: ').strip() or primary_wifi['ssid']
    password = getpass.getpass('Wi-Fi password (Enter keeps existing; - means open Wi-Fi): ')
    password = '' if password == '-' else password or (primary_wifi['password'] if ssid == primary_wifi['ssid'] else '')
    key = getpass.getpass('Gemini key (Enter keeps existing; - leaves manual Setup): ')
    key = '' if key == '-' else key or old['gemini_api_key']
    zone = input(f'Time zone, e.g. America/New_York [{timezone(old)}]: ').strip() or timezone(old)
    while not valid_timezone(zone):
        zone = input(f'Not a time zone name. Time zone [{DEFAULT_TIMEZONE}]: ').strip() or DEFAULT_TIMEZONE
    kept = {name: old[name] for name in ('access_password', 'linux_password', 'anydesk_password') if name in old}
    networks = [{'ssid': ssid, 'password': password}] + wifi_networks(old)[1:]
    save_private(args.settings, {'branch': branch, 'wifi_networks': networks,
                                 'gemini_api_key': key, 'timezone': zone} | kept)
    print(f'Saved branch {branch!r}, Wi-Fi {ssid!r}, Gemini key {"configured" if key else "blank"} '
          f'and time zone {zone}. Rebuild the image to apply.')


if __name__ == '__main__':
    main()
