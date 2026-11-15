"""The board Wi-Fi helper preserves existing profiles and hides passphrases."""
import importlib.machinery
import importlib.util
from pathlib import Path
import unittest


path = Path(__file__).parent / 'payload/ember-wifi'
loader = importlib.machinery.SourceFileLoader('ember_wifi', str(path))
spec = importlib.util.spec_from_loader(loader.name, loader)
ember_wifi = importlib.util.module_from_spec(spec)
loader.exec_module(ember_wifi)


class WifiTests(unittest.TestCase):
    def fake(self):
        calls = []

        def call(*args):
            calls.append(args)
            if args == ('list_networks',):
                return 'network id / ssid / bssid / flags\n0\tnatey\tany\t[CURRENT]\n1\t5G EvoPhilly\tany\t'
            if args[:1] == ('get_network',):
                return {'0': '100', '1': '99'}[args[1]]
            if args == ('add_network',):
                return '2'
            return 'OK'

        return call, calls

    def test_secured_fallback_keeps_existing_profiles_and_hides_password(self):
        call, calls = self.fake()
        self.assertEqual(ember_wifi.add('iPhone Hotspot', 'secret123', False, call), ('2', 98))
        self.assertIn(('set_network', '2', 'ssid', 'iPhone Hotspot'.encode().hex()), calls)
        self.assertIn(('set_network', '2', 'priority', '98'), calls)
        self.assertIn(('save_config',), calls)
        self.assertFalse(any('secret123' in str(args) for args in calls))
        self.assertFalse(any(args[0] == 'remove_network' for args in calls))

    def test_open_preferred_network(self):
        call, calls = self.fake()
        self.assertEqual(ember_wifi.add('Guest', '', True, call), ('2', 101))
        self.assertIn(('set_network', '2', 'key_mgmt', 'NONE'), calls)
        self.assertFalse(any(args[:3] == ('set_network', '2', 'psk') for args in calls))

    def test_failure_removes_new_runtime_profile(self):
        call, calls = self.fake()

        def fail_save(*args):
            if args == ('save_config',):
                raise RuntimeError('FAIL')
            return call(*args)

        with self.assertRaisesRegex(RuntimeError, 'FAIL'):
            ember_wifi.add('Guest', '', False, fail_save)
        self.assertIn(('remove_network', '2'), calls)

    def test_bad_password_changes_no_network(self):
        call, calls = self.fake()
        with self.assertRaisesRegex(ValueError, 'Password'):
            ember_wifi.add('Guest', 'short', False, call)
        self.assertEqual(calls, [])


if __name__ == '__main__':
    unittest.main()
