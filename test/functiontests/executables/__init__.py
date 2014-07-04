import subprocess

from nose import SkipTest


WM_WRITER = 'wm_writer'
WM_READER = 'wm_reader'


def run_command(command):
    try:
        sp = subprocess.Popen(
            command,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
    except OSError:
        raise SkipTest('executables are not present (hint: run tests via tox)')
    sp.communicate()
    return sp.returncode
