import importlib.util
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location('ember_fleet_agent', HERE / 'payload/ember-fleet-agent.py')
agent = importlib.util.module_from_spec(spec)
spec.loader.exec_module(agent)


class FleetAgentTests(unittest.TestCase):
    def test_report_sends_id_and_git_source_without_access_secrets(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = root / 'device.json'
            config.write_text(json.dumps({'repository': 'https://github.com/NateyKim/Baymax.git',
                                          'branch': 'refs/pull/3/head', 'auto_update': True}))
            current = root / 'current'
            release = root / ('a' * 40)
            release.mkdir()
            current.symlink_to(release, target_is_directory=True)
            anydesk = root / 'anydesk-id'
            anydesk.write_text('123456789\n')
            uptime = root / 'uptime'
            uptime.write_text('1234.5 0\n')
            with patch.object(agent, 'CONFIG', config), patch.object(agent, 'CURRENT', current), \
                 patch.object(agent, 'ANYDESK_ID', anydesk), \
                 patch.object(agent, 'UPTIME', uptime), \
                 patch.object(agent.os, 'statvfs', create=True, return_value=SimpleNamespace(f_bavail=100, f_blocks=200, f_frsize=4096)), \
                 patch.object(agent.subprocess, 'run') as service:
                service.return_value.stdout = 'active\n'
                result = agent.report()
            self.assertEqual(result['anydesk_id'], '123456789')
            self.assertEqual(result['git_ref'], 'refs/pull/3/head')
            self.assertEqual(result['revision'], 'a' * 40)
            self.assertNotIn('password', json.dumps(result))
            self.assertNotIn('key', json.dumps(result))


if __name__ == '__main__':
    unittest.main()
