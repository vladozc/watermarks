'''Test if format passed from command line was processed correctly.

LSB watermark should use default format PNG.
Visible watermark should use default format same as original file.
If format was specified with --format argument, use that format.

'''

import os

from nose.tools import assert_equal, assert_true

from .. import DATA_DIR, IM_PREFIX, in_tmp
from . import WM_WRITER, WM_READER, run_command


@in_tmp
def writer(dst_dir, src_filename, gen_filename, method, format_=None):
    filepath = os.path.join(DATA_DIR, src_filename)
    generated_filepath = os.path.join(dst_dir, gen_filename)
    if os.path.exists(generated_filepath):
        os.unlink(generated_filepath)

    command_args = [WM_WRITER, method, '-d', dst_dir, '-s',
                   '_watermarked_test', '-w', filepath, filepath]

    if format_:
        command_args.insert(-1, '--format')
        command_args.insert(-1, format_)

    rc = run_command(command_args)

    assert_equal(rc, 0)
    assert_true(os.path.isfile(generated_filepath))


@in_tmp
def reader(dst_dir, src_filename, gen_filenames, method, format_=None):
    filepath = os.path.join(DATA_DIR, src_filename)
    generated_filepaths = [os.path.join(dst_dir, f) for f in gen_filenames]
    for generated_filepath in generated_filepaths:
        if os.path.exists(generated_filepath):
            os.unlink(generated_filepath)

    command_args = [WM_READER, method, '-d', dst_dir, '-s',
                   '_watermarked_test', filepath]

    if format_:
        command_args.insert(-1, '--format')
        command_args.insert(-1, format_)

    rc = run_command(command_args)

    assert_equal(rc, 0)
    for generated_filepath in generated_filepaths:
        assert_true(os.path.isfile(generated_filepath))


def test_reader_lsb():
    src_filename = 'gen-%s-g.png' % IM_PREFIX
    gen_filenames = ['gen-%s-g_L_watermarked_test.jpg' % IM_PREFIX]
    reader(src_filename, gen_filenames, 'lsb', format_='jpg')


def test_reader_lsb_default_format():
    src_filename = 'gen-%s-g.bmp' % IM_PREFIX
    gen_filenames = ['gen-%s-g_L_watermarked_test.png' % IM_PREFIX]
    reader(src_filename, gen_filenames, 'lsb')


def test_writer_lsb():
    src_filename = 'gen-%s-g.png' % IM_PREFIX
    gen_filename = 'gen-%s-g_watermarked_test.jpg' % IM_PREFIX
    writer(src_filename, gen_filename, 'lsb', format_='jpg')


def test_writer_lsb_default_format():
    src_filename = 'gen-%s-g.bmp' % IM_PREFIX
    gen_filename = 'gen-%s-g_watermarked_test.png' % IM_PREFIX
    writer(src_filename, gen_filename, 'lsb')


def test_writer_visible():
    src_filename = 'gen-%s-g.png' % IM_PREFIX
    gen_filename = 'gen-%s-g_watermarked_test.jpg' % IM_PREFIX
    writer(src_filename, gen_filename, 'visible', format_='jpg')


def test_writer_visible_default_format():
    src_filename = 'gen-%s-g.bmp' % IM_PREFIX
    gen_filename = 'gen-%s-g_watermarked_test.bmp' % IM_PREFIX
    writer(src_filename, gen_filename, 'visible')

