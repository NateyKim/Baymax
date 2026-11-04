"""The three private choices baked into an Ember SD image."""
import hashlib
import json
import re
import shlex
from pathlib import Path

# The repository every image follows. Its name is the owner's choice: keep this,
# payload/ember-device-config.py (DEFAULTS) and payload/ember-update (DEFAULT_REPOSITORY)
# in step if it changes.
REPOSITORY = 'https://github.com/JoeKojima/Ember-OrangePi.git'


def valid_branch(branch):
    """The same branch rule as payload/ember-device-config.py, which the board applies."""
    return (isinstance(branch, str) and re.fullmatch(r'[A-Za-z0-9_][A-Za-z0-9_./-]*', branch) is not None
            and '..' not in branch and not branch.endswith(('/', '.', '.lock')) and '//' not in branch
            and not any(part.startswith('.') for part in branch.split('/')))


def validate(value):
    follow = set(value) & {'branch', 'pr'} if isinstance(value, dict) else set()
    if len(follow) != 1 or set(value) - {'access_password'} - follow != {'wifi', 'gemini_api_key'}:
        raise ValueError('Choose branch (or the older pr), wifi and gemini_api_key (access_password is optional).')
    access = value.get('access_password')
    if access is not None and (not isinstance(access, str) or not 8 <= len(access) <= 64
                               or any(c.isspace() or ord(c) < 32 for c in access)):
        raise ValueError('access_password must be 8-64 characters without spaces.')
    if 'branch' in value and not valid_branch(value['branch']):
        raise ValueError('branch must be a valid Git branch name, such as release.')
    # Older private settings name a pull request instead of a branch.
    if 'pr' in value and (type(value['pr']) is not int or value['pr'] < 1):
        raise ValueError('pr must be a positive pull-request number.')
    wifi = value['wifi']
    if not isinstance(wifi, dict) or set(wifi) != {'ssid', 'password'}:
        raise ValueError('wifi needs ssid and password; use an empty password for open Wi-Fi.')
    ssid, password = wifi['ssid'], wifi['password']
    if not isinstance(ssid, str) or not 1 <= len(ssid.encode('utf-8')) <= 32 or any(ord(c) < 32 for c in ssid):
        raise ValueError('Wi-Fi SSID must contain 1-32 UTF-8 bytes without control characters.')
    if not isinstance(password, str) or any(ord(c) < 32 for c in password):
        raise ValueError('Wi-Fi password must be text without control characters.')
    if password and not (8 <= len(password.encode('utf-8')) <= 63 or re.fullmatch(r'[0-9a-fA-F]{64}', password)):
        raise ValueError('Use an 8-63 byte Wi-Fi password, a 64-digit hex PSK, or blank for open Wi-Fi.')
    key = value['gemini_api_key']
    if not isinstance(key, str) or len(key) > 4096 or any(c.isspace() or ord(c) < 32 for c in key):
        raise ValueError('Gemini key must contain no whitespace; blank waits for Setup.')
    return value


def load(path):
    return validate(json.loads(Path(path).read_text(encoding='utf-8-sig')))


def source(settings):
    branch = settings['branch'] if 'branch' in settings else f'refs/pull/{settings["pr"]}/head'
    return {'repository': REPOSITORY, 'branch': branch, 'auto_update': True}


def supplicant(wifi):
    lines = ['country=US', 'ctrl_interface=DIR=/run/wpa_supplicant GROUP=netdev',
             'update_config=1', 'network={', '    ssid=' + wifi['ssid'].encode('utf-8').hex(),
             '    priority=100']
    if wifi['password']:
        password = wifi['password']
        psk = password.lower() if re.fullmatch(r'[0-9a-fA-F]{64}', password) else hashlib.pbkdf2_hmac(
            'sha1', password.encode('utf-8'), wifi['ssid'].encode('utf-8'), 4096, 32).hex()
        lines += ['    key_mgmt=WPA-PSK', '    psk=' + psk]
    else:
        lines += ['    key_mgmt=NONE']
    return '\n'.join(lines + ['}', ''])


def dietpi_wifi(text, wifi):
    for name, value in (('aWIFI_SSID', wifi['ssid']), ('aWIFI_KEY', wifi['password'])):
        text, count = re.subn(r'^' + name + r'\[0\]=.*$', lambda _: name + '[0]=' + shlex.quote(value), text, flags=re.M)
        if count != 1:
            raise ValueError('Missing or duplicate DietPi Wi-Fi setting: ' + name)
    return text
