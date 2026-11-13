"""Build an Orange Pi image in a local Multipass VM on Windows or macOS."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime
import secrets

from configure_image import save_private
from image_settings import validate

HERE = (Path(sys._MEIPASS) / 'builder' if getattr(sys, 'frozen', False)
        else Path(__file__).resolve().parent)
VM = 'ember-opi4-builder'
VM_HOME = '/home/ubuntu'
MIN_FREE_BYTES = 35 * 1024**3


def multipass_path():
    candidates = [shutil.which('multipass')]
    if os.name == 'nt':
        candidates.append(str(Path(os.environ.get('ProgramFiles', 'C:/Program Files')) /
                              'Multipass/bin/multipass.exe'))
    else:
        candidates.extend(['/usr/local/bin/multipass', '/opt/homebrew/bin/multipass'])
    return next((str(path) for path in candidates if path and Path(path).is_file()), None)


def run(argv, log, *, cwd=None):
    """Stream progress while keeping all secrets in transferred files."""
    log('$ ' + ' '.join(str(part) for part in argv))
    with subprocess.Popen(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          text=True, errors='replace', bufsize=1) as process:
        for line in process.stdout:
            log(line.rstrip())
        if process.wait():
            raise RuntimeError(f'Command failed (exit {process.returncode}): {argv[1]}')


def instance_state(multipass):
    result = subprocess.run([multipass, 'list', '--format', 'json'], capture_output=True,
                            text=True, check=True)
    info = json.loads(result.stdout).get('info', [])
    if isinstance(info, dict):
        info = [dict(name=name, **details) for name, details in info.items()]
    return next((item.get('state', '') for item in info if item.get('name') == VM), None)


def prepare_vm(multipass, log):
    state = instance_state(multipass)
    if state is None:
        run([multipass, 'launch', '24.04', '--name', VM, '--cpus', '4',
             '--memory', '4G', '--disk', '50G'], log)
    elif state.lower() != 'running':
        run([multipass, 'start', VM], log)
    marker = f'{VM_HOME}/.ember-opi4-builder-ready'
    ready = subprocess.run([multipass, 'exec', VM, '--', 'test', '-f', marker],
                           capture_output=True).returncode == 0
    if not ready:
        log('Installing Linux image-building tools in the VM (first run only).')
        setup = ('sudo apt-get update && '
                 'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y '
                 'curl python3 git xz-utils util-linux e2fsprogs openssl ca-certificates && '
                 'if [ "$(uname -m)" != aarch64 ]; then '
                 'sudo DEBIAN_FRONTEND=noninteractive apt-get install -y qemu-user-static binfmt-support; fi && '
                 f'touch {marker}')
        run([multipass, 'exec', VM, '--', 'bash', '-lc', setup], log)


def make_builder_archive(path):
    """Copy only builder source, never local images, caches or private settings."""
    files = [file for file in HERE.iterdir() if file.is_file() and
             file.name not in {'settings.private.json', 'flash_app.py', 'flash_vm.py',
                               'package_app.py', 'test_flash_vm.py'} and
             file.suffix in {'.py', '.sh', '.json'}]
    private_names = {'credentials.json', 'image-settings.private.json', 'bundle-source.json',
                     'ember.bundle'}
    files += [file for file in (HERE / 'payload').rglob('*') if file.is_file() and
              file.name not in private_names and file.suffix not in {'.deb', '.whl'}]
    with tarfile.open(path, 'w:gz') as archive:
        for file in files:
            archive.add(file, arcname=file.relative_to(HERE))


def verify_image(output):
    manifest = json.loads((output / 'ready-image.json').read_text())
    image = output / manifest['image']
    if image.name != manifest['image'] or image.stat().st_size != manifest['length']:
        raise ValueError('Transferred image size does not match the build manifest.')
    with image.open('rb') as stream:
        digest = hashlib.file_digest(stream, 'sha256').hexdigest()
    if digest != manifest['sha256']:
        raise ValueError('Transferred image checksum does not match the build manifest.')
    return manifest


def build_image(settings, output_parent, log):
    settings = validate(settings)
    multipass = multipass_path()
    if not multipass:
        raise RuntimeError('Install Multipass from canonical.com/multipass, then reopen this app.')
    parent = Path(output_parent).expanduser().resolve()
    if not parent.is_dir():
        raise ValueError('Choose an existing output folder.')
    if shutil.disk_usage(parent).free < MIN_FREE_BYTES:
        raise RuntimeError('At least 35 GiB of free disk space is needed for the VM and image.')

    job_id = datetime.now().strftime('%Y%m%d-%H%M%S-') + secrets.token_hex(3)
    remote = f'{VM_HOME}/ember-jobs/{job_id}'
    output = parent / f'ember-opi4-{job_id}'
    prepare_vm(multipass, log)
    output.mkdir(mode=0o700)
    if os.name == 'nt':
        owner = subprocess.check_output(['whoami'], text=True).strip()
        subprocess.run(['icacls.exe', str(output), '/inheritance:r', '/grant:r',
                        owner + ':(OI)(CI)(F)', 'SYSTEM:(OI)(CI)(F)'],
                       check=True, stdout=subprocess.DEVNULL)
    with tempfile.TemporaryDirectory(prefix='ember-flash-') as temporary:
        staging = Path(temporary)
        make_builder_archive(staging / 'builder.tar.gz')
        save_private(staging / 'settings.private.json', settings)
        run([multipass, 'exec', VM, '--', 'mkdir', '-p', f'{remote}/src'], log)
        for name in ('builder.tar.gz', 'settings.private.json'):
            run([multipass, 'transfer', name, f'{VM}:{remote}/{name}'], log, cwd=staging)
        run([multipass, 'exec', VM, '--', 'tar', '-xzf', f'{remote}/builder.tar.gz',
             '-C', f'{remote}/src'], log)
        run([multipass, 'exec', VM, '--', 'sudo', 'python3', f'{remote}/src/build.py',
             '--settings', f'{remote}/settings.private.json',
             '--cache', f'{VM_HOME}/ember-cache', '--output', f'{remote}/output'], log)
        run([multipass, 'exec', VM, '--', 'sudo', 'chown', '-R', 'ubuntu:ubuntu',
             f'{remote}/output'], log)
        for name in ('ember-opi4.img', 'device-access.private.json', 'ready-image.json'):
            run([multipass, 'transfer', f'{VM}:{remote}/output/{name}', name], log, cwd=output)
        manifest = verify_image(output)
        run([multipass, 'exec', VM, '--', 'sudo', 'rm', '-rf', remote], log)
    log('Image verified and ready to write with an SD card image writer.')
    return output, manifest
