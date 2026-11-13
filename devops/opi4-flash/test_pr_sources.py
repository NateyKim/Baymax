import unittest
from unittest.mock import patch

import pr_sources


class SourceTests(unittest.TestCase):
    def test_lists_only_open_orange_pi_prs(self):
        pulls = [
            {'number': 2, 'title': 'AnyDesk display', 'head': {'ref': 'feature/opi4-display'}},
            {'number': 3, 'title': 'Flash app', 'head': {'ref': 'feature/flash-app'}},
            {'number': 1, 'title': 'Other feature', 'head': {'ref': 'feature/other'}},
        ]
        def get(url):
            if '/pulls?' in url:
                return pulls
            if '/pulls/1/files?' in url:
                return [{'filename': 'Baymax-main/other.py'}]
            raise AssertionError(url)
        with patch.object(pr_sources, '_get', side_effect=get):
            self.assertEqual(pr_sources.list_opi4_prs(),
                             [(3, 'Flash app'), (2, 'AnyDesk display')])
