import os
import shutil

from watermarks.core.writers.lsb import Lsb
from .. import run_writer_and_assert, DATA_DIR
from . import (
    WM1_WM, WM1_WM_JPG, WM2, IM_PREFIX, WM_PREFIX,
    WM_BIG, WM_SMALL,
)


def run_lsb_and_assert(*args, **kwargs):
    return run_writer_and_assert(Lsb, *args, **kwargs)


def test_g_gif():
    run_lsb_and_assert('shape1-g.gif', 'wm-png-24-16b.png', WM1_WM)


def test_g_l0_png():
    run_lsb_and_assert('shape1-g-l0.png', 'wm-png-24-16b.png', WM1_WM)


def test_g_l9_png():
    run_lsb_and_assert('shape1-g-l9.png', 'wm-png-24-16b.png', WM1_WM)


#def test_rgb_16_1555_bmp():
#    run_lsb_and_assert('shape1-rgb-16-1555.bmp', 'wm-png-24-16b.png', WM1_WM)


def test_rgb_l0_png():
    run_lsb_and_assert('shape1-rgb-l0.png', 'wm-png-24-16b.png', WM1_WM)


def test_rgb_l9_png():
    run_lsb_and_assert('shape1-rgb-l9.png', 'wm-png-24-16b.png', WM1_WM)


def test_gen_l_bmp():
    run_lsb_and_assert('gen-%s-g.bmp' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM)


def test_gen_l_gif():
    run_lsb_and_assert('gen-%s-g.gif' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM)


def test_gen_l_png():
    run_lsb_and_assert('gen-%s-g.png' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM)


def test_gen_rgb_bmp():
    run_lsb_and_assert('gen-%s-rgb.bmp' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM)


def test_gen_rgb_jpg():
    run_lsb_and_assert('gen-%s-rgb.jpg' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM_JPG)


def test_gen_rgb_png():
    run_lsb_and_assert('gen-%s-rgb.png' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM)


def test_unknown_extension():
    shutil.copyfile(
        os.path.join(DATA_DIR, 'gen-%s-rgb.png' % IM_PREFIX),
        os.path.join(DATA_DIR, 'gen-%s-rgb.unknownextension' % IM_PREFIX),
    )
    run_lsb_and_assert('gen-%s-rgb.unknownextension' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM, ext='.png')


def test_wm_mode_1():
    run_lsb_and_assert('gen-%s-img.png' % WM_PREFIX, 'gen-%s-wm-1.png' % WM_PREFIX, WM2)


def test_wm_mode_l():
    run_lsb_and_assert('gen-%s-img.png' % WM_PREFIX, 'gen-%s-wm-l.png' % WM_PREFIX, WM2)


def test_wm_mode_rgb():
    run_lsb_and_assert('gen-%s-img.png' % WM_PREFIX, 'gen-%s-wm-rgb.png' % WM_PREFIX, WM2)


def test_wm_mode_rgba():
    run_lsb_and_assert('gen-%s-img.png' % WM_PREFIX, 'gen-%s-wm-rgba.png' % WM_PREFIX, WM2)

def test_big_wm():
    run_lsb_and_assert('rgb-24-16b.png', 'gen-%s-wm-rgb.png' % WM_PREFIX, WM_BIG)


def test_small_wm():
    run_lsb_and_assert('gen-%s-wm-rgb.png' % WM_PREFIX, 'rgb-24-16b.png', WM_SMALL)


def test_unsupported_format():
    run_lsb_and_assert('unsupported_format.tiff', 'rgb-24-16b.png')


def test_unsupported_mode():
    run_lsb_and_assert('unsupported_mode.png', 'rgb-24-16b.png')


def test_not_exists():
    run_lsb_and_assert('this_file_does_not_exist.png', 'rgb-24-16b.png', width=1, height=1)
