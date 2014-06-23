import os
import subprocess

from nose import SkipTest
from nose.tools import assert_equal, assert_true

from .. import DATA_DIR, IM_PREFIX, in_tmp


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


@in_tmp
def test_writer(dst_dir):
    filepath = os.path.join(DATA_DIR, 'gen-%s-g.png' % IM_PREFIX)
    generated_filepath = os.path.join(dst_dir, 'gen-%s-g_watermarked_test.png' % IM_PREFIX)
    if os.path.exists(generated_filepath):
        os.unlink(generated_filepath)

    rc = run_command([WM_WRITER, 'lsb', '-q', '-d', dst_dir, '-s',
                     '_watermarked_test', '-w', filepath, filepath])

    assert_equal(rc, 0)
    assert_true(os.path.isfile(generated_filepath))


@in_tmp
def test_writer_chain(dst_dir):
    filepath = os.path.join(DATA_DIR, 'gen-%s-g.png' % IM_PREFIX)
    generated_filepath = os.path.join(dst_dir, 'gen-%s-g_watermarked_test.png' % IM_PREFIX)
    if os.path.exists(generated_filepath):
        os.unlink(generated_filepath)

    rc = run_command([WM_WRITER, 'lsb,visible', '-q', '-d', dst_dir, '-s',
                     '_watermarked_test', '-w', filepath, '-w', filepath,
                     filepath])

    assert_equal(rc, 0)
    assert_true(os.path.isfile(generated_filepath))
    # TODO: check content of generated file


@in_tmp
def test_reader(dst_dir):
    filepath = os.path.join(DATA_DIR, 'gen-%s-g.png' % IM_PREFIX)
    suffix = '_test'
    generated_filepath = os.path.join(dst_dir, 'gen-%s-g_L%s.png' % (IM_PREFIX, suffix))
    if os.path.exists(generated_filepath):
        os.unlink(generated_filepath)

    rc = run_command([WM_READER, 'lsb', '-q', '-d', dst_dir, '-s', suffix, filepath])

    assert_equal(rc, 0)
    assert_true(os.path.isfile(generated_filepath))


@in_tmp
def test_reader_chain(dst_dir):
    filepath = os.path.join(DATA_DIR, 'gen-%s-g.png' % IM_PREFIX)
    suffix = '_test'
    # TODO: use different methods. Since WM currently does not support
    # more readers methods, I cannot do it now.
    methods = ['lsb', 'lsb']
    for method in methods:
        generated_filepath = os.path.join(dst_dir, 'gen-%s-g_L_%s%s.png' % (IM_PREFIX, method, suffix))
        if os.path.exists(generated_filepath):
            os.unlink(generated_filepath)

    rc = run_command([WM_READER, ','.join(methods), '-q', '-d', dst_dir, '-s', suffix, filepath])

    assert_equal(rc, 0)
    for method in methods:
        generated_filepath = os.path.join(dst_dir, 'gen-%s-g_L_%s%s.png' % (IM_PREFIX, method, suffix))
        assert_true(os.path.isfile(generated_filepath))
    assert_true(len(methods) > 1)


def test_writer_help():
    rc = run_command([WM_WRITER, '--help'])
    assert_equal(rc, 0)


def test_reader_help():
    rc = run_command([WM_READER, '--help'])
    assert_equal(rc, 0)


def test_writer_method_help():
    rc = run_command([WM_WRITER, 'lsb', '--help'])
    assert_equal(rc, 0)


def test_reader_method_help():
    rc = run_command([WM_READER, 'lsb', '--help'])
    assert_equal(rc, 0)


def test_writer_version():
    rc = run_command([WM_WRITER, '--version'])
    assert_equal(rc, 0)


def test_reader_version():
    rc = run_command([WM_READER, '--version'])
    assert_equal(rc, 0)


def test_writer_no_args():
    rc = run_command([WM_WRITER])
    assert_equal(rc, 2)


def test_reader_no_args():
    rc = run_command([WM_READER])
    assert_equal(rc, 2)


def test_writer_invalid_method():
    rc = run_command([WM_WRITER, 'not_existing_method'])
    assert_equal(rc, 1)


def test_reader_invalid_method():
    rc = run_command([WM_READER, 'not_existing_method'])
    assert_equal(rc, 1)


def test_writer_few_args1():
    rc = run_command([WM_WRITER, 'lsb'])
    assert_equal(rc, 2)


def test_writer_few_args2():
    rc = run_command([WM_WRITER, 'lsb', '-d'])
    assert_equal(rc, 2)


def test_writer_few_args3():
    rc = run_command([WM_WRITER, 'lsb', '-d', 'tmp'])
    assert_equal(rc, 2)


def test_writer_few_args4():
    rc = run_command([WM_WRITER, '-w'])
    assert_equal(rc, 2)


def test_writer_few_args5():
    rc = run_command([WM_WRITER, 'lsb', '-w', 'image.png'])
    assert_equal(rc, 2)


def test_writer_few_args6():
    rc = run_command([WM_WRITER, 'lsb', 'image.png'])
    assert_equal(rc, 2)


def test_reader_few_args1():
    rc = run_command([WM_READER, 'lsb'])
    assert_equal(rc, 2)


def test_reader_few_args2():
    rc = run_command([WM_READER, 'lsb', '-d'])
    assert_equal(rc, 2)


def test_reader_few_args3():
    rc = run_command([WM_READER, 'lsb', '-d', 'tmp'])
    assert_equal(rc, 2)


def test_reader_few_args4():
    rc = run_command([WM_READER, 'lsb', 'image.png'])
    assert_equal(rc, 2)

