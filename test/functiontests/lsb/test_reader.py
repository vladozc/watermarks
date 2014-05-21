import os
import subprocess

from nose import SkipTest
from nose.tools import assert_equal, assert_true
from PIL import Image

from watermarks.core.readers.lsb import Lsb
from .. import (
    run_reader_and_assert, IM_PREFIX, DATA_DIR, in_tmp,
    create_data_dir,
)
from . import WM1_1, WM1_255, WM1_255_JPG


def run_and_assert(*args, **kwargs):
    run_reader_and_assert(Lsb, *args, **kwargs)


def test_g_gif():
    run_and_assert('shape1-g.gif', WM1_255)


def test_g_l0_png():
    run_and_assert('shape1-g-l0.png', WM1_255)


def test_g_l9_png():
    run_and_assert('shape1-g-l9.png', WM1_255)


#def test_rgb_16_1555_bmp():
#    run_and_assert('shape1-rgb-16-1555.bmp', WM1_255)


def test_rgb_l0_png():
    run_and_assert('shape1-rgb-l0.png', WM1_255)


def test_rgb_l9_png():
    run_and_assert('shape1-rgb-l9.png', WM1_255)


def test_gen_l_bmp():
    run_and_assert('gen-%s-g.bmp' % IM_PREFIX, WM1_255)


def test_gen_l_gif():
    run_and_assert('gen-%s-g.gif' % IM_PREFIX, WM1_255)


def test_gen_l_png():
    run_and_assert('gen-%s-g.png' % IM_PREFIX, WM1_255)


def test_gen_rgb_bmp():
    run_and_assert('gen-%s-rgb.bmp' % IM_PREFIX, WM1_255)


def test_gen_rgb_jpg():
    run_and_assert('gen-%s-rgb.jpg' % IM_PREFIX, WM1_255_JPG, ext='.png')


def test_gen_rgb_png():
    run_and_assert('gen-%s-rgb.png' % IM_PREFIX, WM1_255)


def test_unsupported_format():
    run_and_assert('unsupported_format.tiff')


def test_unsupported_mode():
    run_and_assert('unsupported_mode.png')


def test_not_exists():
    run_and_assert('this_file_does_not_exist.png')


@in_tmp
def test_dir(dst_dir):
    filenames = ['gen-%s-rgb.png' % IM_PREFIX, 'gen-%s-g.png' % IM_PREFIX]
    data_dir_path = create_data_dir(os.path.join(dst_dir, 'reader_dir'), filenames)
    filepath = os.path.join(DATA_DIR, 'shape1-g-l0.png')

    lsb = Lsb(dst_dir, 'png')
    generated_filepaths = lsb.run([data_dir_path, filepath])
    generated_filenames = set([os.path.basename(f) for f in generated_filepaths])

    assert_true('gen-%s-rgb_R.png' % IM_PREFIX in generated_filenames)
    assert_true('gen-%s-rgb_G.png' % IM_PREFIX in generated_filenames)
    assert_true('gen-%s-rgb_B.png' % IM_PREFIX in generated_filenames)
    assert_true('gen-%s-g_L.png' % IM_PREFIX in generated_filenames)
    assert_true('shape1-g-l0_L.png' in generated_filenames)
    assert_equal(len(generated_filenames), 5)


@in_tmp
def test_bin(dst_dir):
    filepath = os.path.join(DATA_DIR, 'gen-%s-g.png' % IM_PREFIX)
    suffix = '_test'
    generated_filepath = os.path.join(dst_dir, 'gen-%s-g_L%s.png' % (IM_PREFIX, suffix))
    if os.path.exists(generated_filepath):
        os.unlink(generated_filepath)

    try:
        sp = subprocess.Popen(
            ['wm_reader', 'lsb', '-q', '-d', dst_dir, '-s', suffix, filepath],
        )
    except FileNotFoundError:
        raise SkipTest('binaries are not present (hint: run tests via tox)')
    sp.communicate()

    assert_equal(sp.returncode, 0)
    assert_true(os.path.isfile(generated_filepath))
