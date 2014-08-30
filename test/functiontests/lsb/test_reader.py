import os

from nose.tools import assert_equal, assert_true

from watermarks.core.readers.lsb import Lsb
from .. import (
    run_reader_and_assert, IM_PREFIX, DATA_DIR, in_tmp,
    create_data_dir,
)
from . import WM1_1, WM1_255, WM1_255_JPG


def run_and_assert(*args, **kwargs):
    bands = kwargs.pop('bands', None)
    return run_reader_and_assert(Lsb, bands=bands,
        bands_are_filtered=bool(bands), *args, **kwargs)


def test_g_gif():
    run_and_assert('shape1-g.gif', WM1_255, ext='png')


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


# comment out due to Pillow 2.4.0
#def test_gen_l_gif():
#    run_and_assert('gen-%s-g.gif' % IM_PREFIX, WM1_255)


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

    lsb = Lsb(destination=dst_dir, format_='png')
    generated_filepaths = lsb.run([data_dir_path, filepath])
    generated_filenames = set([os.path.basename(f) for f in generated_filepaths])

    assert_true('gen-%s-rgb_R.png' % IM_PREFIX in generated_filenames)
    assert_true('gen-%s-rgb_G.png' % IM_PREFIX in generated_filenames)
    assert_true('gen-%s-rgb_B.png' % IM_PREFIX in generated_filenames)
    assert_true('gen-%s-g_L.png' % IM_PREFIX in generated_filenames)
    assert_true('shape1-g-l0_L.png' in generated_filenames)
    assert_equal(len(generated_filenames), 5)


def test_bands_rgb():
    run_and_assert('shape1-rgb-l0.png', [WM1_255], bands=['r', 'c'])


def test_bands_g():
    run_and_assert('shape1-g-l0.png', [WM1_255], bands=['l'])
