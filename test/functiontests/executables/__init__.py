import subprocess

from nose import SkipTest


WM_WRITER = 'wm-writer'
WM_READER = 'wm-reader'


def run_command(command, debug=False):
    try:
        sp = subprocess.Popen(
            command,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
    except OSError:
        raise SkipTest('executables are not present (hint: run tests via tox)')
    stdout, stderr = sp.communicate()
    if debug:
        print(subprocess.list2cmdline(command))
        print(stdout)
        print(stderr)
    return sp.returncode
