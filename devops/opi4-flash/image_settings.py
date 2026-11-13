"""The three private choices baked into an Ember SD image, plus optional ones."""
import hashlib
import json
import re
import shlex
from pathlib import Path

# The repository every image follows. Its name is the owner's choice: keep this,
# payload/ember-device-config.py (DEFAULTS) and payload/ember-update (DEFAULT_REPOSITORY)
# in step if it changes.
REPOSITORY = 'https://github.com/NateyKim/Baymax.git'
# The board's clock unless the private settings name another time zone. Daily
# check-ins, reminders and the greeting's time of day follow it.
DEFAULT_TIMEZONE = 'America/Los_Angeles'
OPTIONAL = {'access_password', 'linux_password', 'anydesk_password', 'timezone', 'hostname'}
MAX_WIFI_NETWORKS = 5


def valid_branch(branch):
    """The same branch rule as payload/ember-device-config.py, which the board applies."""
    return (isinstance(branch, str) and re.fullmatch(r'[A-Za-z0-9_][A-Za-z0-9_./-]*', branch) is not None
            and '..' not in branch and not branch.endswith(('/', '.', '.lock')) and '//' not in branch
            and not any(part.startswith('.') for part in branch.split('/')))


def valid_timezone(name):
    """An IANA time zone name such as America/New_York or UTC. The build also checks
    that the image's own /usr/share/zoneinfo has it."""
    return (isinstance(name, str) and len(name) <= 64
            and re.fullmatch(r'[A-Za-z][A-Za-z0-9_+-]*(/[A-Za-z0-9_+-]+)*', name) is not None)


def timezone(settings):
    return settings.get('timezone', DEFAULT_TIMEZONE)


def wifi_networks(settings):
    return settings['wifi_networks'] if 'wifi_networks' in settings else [settings['wifi']]


def validate(value):
    follow = set(value) & {'branch', 'pr'} if isinstance(value, dict) else set()
    wifi_field = set(value) & {'wifi', 'wifi_networks'} if isinstance(value, dict) else set()
    if (len(follow) != 1 or len(wifi_field) != 1 or
            set(value) - OPTIONAL - follow - wifi_field != {'gemini_api_key'}):
        raise ValueError('Choose one branch or PR, one or more Wi-Fi networks, and gemini_api_key.')
    if 'access_password' in value and ({'linux_password', 'anydesk_password'} & set(value)):
        raise ValueError('Use either the legacy shared access_password or separate passwords.')
    for name in ('access_password', 'linux_password', 'anydesk_password'):
        password = value.get(name)
        if password is not None and (not isinstance(password, str) or not 8 <= len(password) <= 64
                                     or any(c.isspace() or ord(c) < 32 for c in password)):
            raise ValueError(name + ' must be 8-64 characters without spaces.')
    if 'timezone' in value and not valid_timezone(value['timezone']):
        raise ValueError('timezone must be a time zone name such as America/New_York or UTC.')
    if 'hostname' in value and (not isinstance(value['hostname'], str) or
                                re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?', value['hostname']) is None):
        raise ValueError('hostname must use lowercase letters, digits and hyphens (1-63 characters).')
    if 'branch' in value and not valid_branch(value['branch']):
        raise ValueError('branch must be a valid Git branch name, such as release.')
    # Older private settings name a pull request instead of a branch.
    if 'pr' in value and (type(value['pr']) is not int or value['pr'] < 1):
        raise ValueError('pr must be a positive pull-request number.')
    networks = wifi_networks(value)
    if not isinstance(networks, list) or not 1 <= len(networks) <= MAX_WIFI_NETWORKS:
        raise ValueError(f'Add 1-{MAX_WIFI_NETWORKS} Wi-Fi networks.')
    names = set()
    for wifi in networks:
        if not isinstance(wifi, dict) or set(wifi) != {'ssid', 'password'}:
            raise ValueError('Each Wi-Fi network needs ssid and password; blank means open.')
        ssid, password = wifi['ssid'], wifi['password']
        if not isinstance(ssid, str) or not 1 <= len(ssid.encode('utf-8')) <= 32 or any(ord(c) < 32 for c in ssid):
            raise ValueError('Wi-Fi SSID must contain 1-32 UTF-8 bytes without control characters.')
        if ssid in names:
            raise ValueError('Add each Wi-Fi name only once.')
        names.add(ssid)
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


def supplicant(networks):
    networks = [networks] if isinstance(networks, dict) else networks
    lines = ['country=US', 'ctrl_interface=DIR=/run/wpa_supplicant GROUP=netdev',
             'update_config=1']
    for index, wifi in enumerate(networks):
        lines += ['network={', '    ssid=' + wifi['ssid'].encode('utf-8').hex(),
                  f'    priority={100-index}']
        if wifi['password']:
            password = wifi['password']
            psk = password.lower() if re.fullmatch(r'[0-9a-fA-F]{64}', password) else hashlib.pbkdf2_hmac(
                'sha1', password.encode('utf-8'), wifi['ssid'].encode('utf-8'), 4096, 32).hex()
            lines += ['    key_mgmt=WPA-PSK', '    psk=' + psk]
        else:
            lines += ['    key_mgmt=NONE']
        lines.append('}')
    return '\n'.join(lines + [''])


def dietpi_wifi(text, networks):
    networks = [networks] if isinstance(networks, dict) else networks
    for index in range(MAX_WIFI_NETWORKS):
        wifi = networks[index] if index < len(networks) else {'ssid': '', 'password': ''}
        for name, value in (('aWIFI_SSID', wifi['ssid']), ('aWIFI_KEY', wifi['password']),
                            ('aWIFI_KEYMGR', 'WPA-PSK' if wifi['password'] else 'NONE')):
            pattern = rf'^{name}\[{index}\]=.*$'
            line = f'{name}[{index}]={shlex.quote(value)}'
            text, count = re.subn(pattern, lambda _: line, text, flags=re.M)
            if count > 1 or (index == 0 and name != 'aWIFI_KEYMGR' and count != 1):
                raise ValueError('Missing or duplicate DietPi Wi-Fi setting: ' + name)
            if count == 0:
                text = text.rstrip('\n') + '\n' + line + '\n'
    return text
