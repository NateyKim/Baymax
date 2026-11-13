"""Exercise HDMI changes without touching the host display."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


@unittest.skipUnless(os.name == 'posix' and shutil.which('bash'), 'requires Linux bash and symlinks')
class DisplayTests(unittest.TestCase):
    def test_hdmi_and_virtual_display_switch_once_per_change(self):
        source = (Path(__file__).parent / 'payload/ember-select-display').read_text()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            conf = root / '20-ember-virtual.conf'
            virtual = root / 'ember-virtual.conf'
            virtual.write_text('virtual Xorg config')
            conf.symlink_to(virtual)
            connector = root / 'card0-HDMI-A-1'
            connector.mkdir()
            status = connector / 'status'
            log = root / 'restarts'
            systemctl = root / 'systemctl'
            systemctl.write_text('#!/bin/sh\n[ "$1" = is-active ] || echo "$1" >> "$EMBER_RESTART_LOG"\n')
            systemctl.chmod(0o755)
            script = root / 'select-display'
            script.write_text(source.replace('/etc/X11/xorg.conf.d/20-ember-virtual.conf', str(conf))
                              .replace('/etc/X11/ember-virtual.conf', str(virtual))
                              .replace('/sys/class/drm/*HDMI*/status', str(root / '*HDMI*/status'))
                              .replace('systemctl', str(systemctl)))
            env = {**os.environ, 'EMBER_RESTART_LOG': str(log)}

            status.write_text('connected\n')
            subprocess.run(['bash', str(script), '--no-restart'], check=True, env=env)
            self.assertFalse(conf.exists())
            self.assertFalse(log.exists())
            status.write_text('disconnected\n')
            subprocess.run(['bash', str(script)], check=True, env=env)
            subprocess.run(['bash', str(script)], check=True, env=env)
            self.assertEqual(conf.resolve(), virtual)
            self.assertEqual(log.read_text().splitlines(), ['restart'])
            status.write_text('connected\n')
            subprocess.run(['bash', str(script)], check=True, env=env)
            self.assertFalse(conf.exists())
            self.assertEqual(log.read_text().splitlines(), ['restart', 'restart'])
