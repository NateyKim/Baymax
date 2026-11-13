import hashlib
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch

import flash_vm
import package_app


class FlashVmTests(unittest.TestCase):
    def test_archive_never_includes_private_settings_or_old_images(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'payload').mkdir()
            (root / 'build.py').write_text('builder')
            (root / 'assets.json').write_text('{}')
            (root / 'payload/ember-provision').write_text('provision')
            (root / 'settings.private.json').write_text('SECRET')
            (root / 'output').mkdir()
            (root / 'output/old.img').write_text('OLD IMAGE')
            archive = root / 'builder.tar.gz'
            with patch.object(flash_vm, 'HERE', root):
                flash_vm.make_builder_archive(archive)
            with tarfile.open(archive) as stream:
                self.assertEqual(set(stream.getnames()),
                                 {'build.py', 'assets.json', 'payload/ember-provision'})

    def test_verified_image_must_match_size_and_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            image = output / 'ember-opi4.img'
            image.write_bytes(b'image')
            manifest = {'image': image.name, 'length': 5,
                        'sha256': hashlib.sha256(b'image').hexdigest()}
            (output / 'ready-image.json').write_text(json.dumps(manifest))
            self.assertEqual(flash_vm.verify_image(output), manifest)
            image.write_bytes(b'wrong')
            with self.assertRaisesRegex(ValueError, 'checksum'):
                flash_vm.verify_image(output)

    def test_package_stages_only_builder_files(self):
        with tempfile.TemporaryDirectory() as directory:
            staged = Path(directory) / 'builder'
            package_app.stage_builder(staged)
            self.assertTrue((staged / 'build.py').is_file())
            self.assertTrue((staged / 'payload/ember-provision').is_file())
            self.assertFalse((staged / 'settings.private.json').exists())
            self.assertFalse((staged / 'flash_app.py').exists())
