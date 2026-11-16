"""Send non-secret OP4 health to the admin fleet console once per timer run."""
import json
import os
from pathlib import Path
import re
import socket
import subprocess
import urllib.error
import urllib.request


KEY = Path('/home/ember/.config/ember/fleet-key')
CONFIG = Path('/home/ember/.config/ember/device.json')
CURRENT = Path('/home/ember/ember-deployment/current')
ANYDESK_ID = Path('/var/lib/ember/anydesk-id')
ENDPOINT = 'https://tadashirobotics.com/api/device/checkin'


def report():
    config = json.loads(CONFIG.read_text())
    revision = CURRENT.resolve().name
    if not re.fullmatch(r'[0-9a-f]{40}', revision):
        revision = None
    desk_id = ANYDESK_ID.read_text().strip() if ANYDESK_ID.exists() else ''
    stat = os.statvfs('/home/ember')
    state = subprocess.run(['systemctl', '--user', 'is-active', 'ember.service'],
                           capture_output=True, text=True, timeout=5)
    return {
        'agent_version': 'opi4-status/1', 'runtime': 'venv', 'hostname': socket.gethostname(),
        'revision': revision, 'git_repository': config['repository'], 'git_ref': config['branch'],
        'anydesk_id': desk_id if re.fullmatch(r'[0-9]{5,20}', desk_id) else None,
        'ember': 'running' if state.stdout.strip() == 'active' else ('starting' if not CURRENT.exists() else 'stopped'),
        'disk': {'free': stat.f_bavail * stat.f_frsize, 'total': stat.f_blocks * stat.f_frsize},
        'uptime': int(float(Path('/proc/uptime').read_text().split()[0])),
    }


def main():
    key = KEY.read_text().strip()
    if not re.fullmatch(r'[a-z0-9-]{1,32}\.[0-9a-f]{64}', key):
        raise SystemExit('Invalid fleet key file')
    request = urllib.request.Request(ENDPOINT, data=json.dumps(report()).encode(),
                                     headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + key},
                                     method='POST')
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            if response.status != 200:
                raise SystemExit(f'Fleet check-in returned HTTP {response.status}')
    except urllib.error.HTTPError as exc:
        raise SystemExit(f'Fleet check-in returned HTTP {exc.code}') from None
    except urllib.error.URLError:
        raise SystemExit('Fleet check-in network unavailable') from None


if __name__ == '__main__':
    main()
