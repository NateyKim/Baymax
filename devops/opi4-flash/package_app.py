"""Package the desktop app with only public builder source and payload files."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
BUILDER_FILES = ('assets.json', 'build.py', 'build_linux.sh', 'configure_image.py', 'image_settings.py',
                 'inject_image.py', 'validate_image.py')


def stage_builder(destination):
    destination.mkdir()
    for name in BUILDER_FILES:
        shutil.copy2(HERE / name, destination / name)
    for test in HERE.glob('test_*.py'):
        if test.name == 'test_flash_vm.py':
            continue
        shutil.copy2(test, destination / test.name)
    shutil.copytree(HERE / 'payload', destination / 'payload',
                    ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '*.deb', '*.whl',
                                                  'credentials.json', 'image-settings.private.json',
                                                  'bundle-source.json', 'ember.bundle'))


def main():
    with tempfile.TemporaryDirectory(prefix='ember-package-') as directory:
        staged = Path(directory) / 'builder'
        stage_builder(staged)
        subprocess.run([sys.executable, '-m', 'PyInstaller', '--noconfirm', '--clean',
                        '--windowed', '--onefile', '--name', 'Ember-Image-Builder',
                        '--add-data', f'{staged}:builder', str(HERE / 'flash_app.py')],
                       cwd=HERE, check=True)


if __name__ == '__main__':
    main()
