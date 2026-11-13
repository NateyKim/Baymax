"""Open Orange Pi 4 Pro pull requests for the image builder's source picker."""
import json
import re
from urllib.request import Request, urlopen

API = 'https://api.github.com/repos/NateyKim/Baymax'


def _get(url):
    request = Request(url, headers={'Accept': 'application/vnd.github+json',
                                    'User-Agent': 'Ember-Image-Builder'})
    with urlopen(request, timeout=10) as response:
        return json.load(response)


def list_opi4_prs():
    pulls = _get(API + '/pulls?state=open&per_page=100')
    found = []
    for pull in pulls:
        label = pull['title'] + ' ' + pull['head']['ref']
        relevant = re.search(r'opi4|orange[ -]?pi[ -]?4|flash', label, re.I)
        if not relevant:
            files = _get(API + f"/pulls/{pull['number']}/files?per_page=100")
            relevant = any(file['filename'].startswith('devops/opi4-flash/') for file in files)
        if relevant:
            found.append((pull['number'], pull['title']))
    return sorted(found, reverse=True)
