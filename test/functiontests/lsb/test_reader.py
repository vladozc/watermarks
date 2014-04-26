import os
import shutil

from nose.tools import assert_equal
from PIL import Image

from watermarks.core.readers.lsb import Lsb
from .. import run_reader_and_assert
from . import WM1_1, WM1_255, WM1_255_JPG, DATA_DIR, DST_DIR, IM_PREFIX


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


def test_unknown_extension():
    shutil.copyfile(
        os.path.join(DATA_DIR, 'gen-%s-rgb.png' % IM_PREFIX),
        os.path.join(DATA_DIR, 'gen-%s-rgb.unknownextension' % IM_PREFIX),
    )
    run_and_assert('gen-%s-rgb.unknownextension' % IM_PREFIX, WM1_255, ext='.png')


def test_unsupported_format():
    run_and_assert('unsupported_format.tiff')


def test_unsupported_mode():
    run_and_assert('unsupported_mode.png')
