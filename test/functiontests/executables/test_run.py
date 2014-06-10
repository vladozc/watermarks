import os
import subprocess

from nose import SkipTest
from nose.tools import assert_equal, assert_true

from .. import DATA_DIR, IM_PREFIX, in_tmp


@in_tmp
def test_writer(dst_dir):
    filepath = os.path.join(DATA_DIR, 'gen-%s-g.png' % IM_PREFIX)
    generated_filepath = os.path.join(dst_dir, 'gen-%s-g_watermarked_test.png' % IM_PREFIX)
    if os.path.exists(generated_filepath):
        os.unlink(generated_filepath)

    try:
        sp = subprocess.Popen(
            ['wm_writer', 'lsb', '-q', '-d', dst_dir, '-s',
             '_watermarked_test', '-w', filepath, filepath],
        )
    except OSError:
        raise SkipTest('executables are not present (hint: run tests via tox)')
    stdout, stderr = sp.communicate()

    assert_equal(sp.returncode, 0)
    assert_true(os.path.isfile(generated_filepath))


@in_tmp
def test_reader(dst_dir):
    filepath = os.path.join(DATA_DIR, 'gen-%s-g.png' % IM_PREFIX)
    suffix = '_test'
    generated_filepath = os.path.join(dst_dir, 'gen-%s-g_L%s.png' % (IM_PREFIX, suffix))
    if os.path.exists(generated_filepath):
        os.unlink(generated_filepath)

    try:
        sp = subprocess.Popen(
            ['wm_reader', 'lsb', '-q', '-d', dst_dir, '-s', suffix, filepath],
        )
    except OSError:
        raise SkipTest('executables are not present (hint: run tests via tox)')
    sp.communicate()

    assert_equal(sp.returncode, 0)
    assert_true(os.path.isfile(generated_filepath))
