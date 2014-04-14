import os
import shutil

from nose.tools import assert_equal
from PIL import Image

from watermarker.core.writers.lsb import Lsb
from . import WM1_WM, WM1_WM_JPG, WM2, DATA_DIR, DST_DIR, IM_PREFIX, WM_PREFIX


def run_and_assert(filename, wm_filename, wm_data, ext=None):
    base, f_ext = os.path.splitext(filename)
    ext = ext or f_ext
    filepath = os.path.join(DATA_DIR, filename)
    wm_filepath = os.path.join(DATA_DIR, wm_filename)
    suffix = '_watermarked_test'
    writer = Lsb([filepath], DST_DIR, ext.lstrip('.'), wm_filepath, suffix)
    writer.run()
    src_img = Image.open(filepath)
    res_filename = '%s%s%s' % (base, suffix, ext)
    res_filepath = os.path.join(DST_DIR, res_filename)
    res_img = Image.open(res_filepath)
    res_img.load()
    for band in res_img.split():
        assert_equal(list(band.getdata()), wm_data)


def test_g_gif():
    run_and_assert('shape1-g.gif', 'wm-png-24-16b.png', WM1_WM)


def test_g_l0_png():
    run_and_assert('shape1-g-l0.png', 'wm-png-24-16b.png', WM1_WM)


def test_g_l9_png():
    run_and_assert('shape1-g-l9.png', 'wm-png-24-16b.png', WM1_WM)


#def test_rgb_16_1555_bmp():
#    run_and_assert('shape1-rgb-16-1555.bmp', 'wm-png-24-16b.png', WM1_WM)


def test_rgb_l0_png():
    run_and_assert('shape1-rgb-l0.png', 'wm-png-24-16b.png', WM1_WM)


def test_rgb_l9_png():
    run_and_assert('shape1-rgb-l9.png', 'wm-png-24-16b.png', WM1_WM)


def test_gen_l_bmp():
    run_and_assert('gen-%s-g.bmp' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM)


def test_gen_l_gif():
    run_and_assert('gen-%s-g.gif' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM)


def test_gen_l_png():
    run_and_assert('gen-%s-g.png' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM)


def test_gen_rgb_bmp():
    run_and_assert('gen-%s-rgb.bmp' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM)


def test_gen_rgb_jpg():
    run_and_assert('gen-%s-rgb.jpg' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM_JPG)


def test_gen_rgb_png():
    run_and_assert('gen-%s-rgb.png' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM)


def test_unknown_extension():
    shutil.copyfile(
        os.path.join(DATA_DIR, 'gen-%s-rgb.png' % IM_PREFIX),
        os.path.join(DATA_DIR, 'gen-%s-rgb.unknownextension' % IM_PREFIX),
    )
    run_and_assert('gen-%s-rgb.unknownextension' % IM_PREFIX, 'wm-png-24-16b.png', WM1_WM, ext='.png')


def test_wm_mode_1():
    run_and_assert('gen-%s-img.png' % WM_PREFIX, 'gen-%s-wm-1.png' % WM_PREFIX, WM2)


def test_wm_mode_l():
    run_and_assert('gen-%s-img.png' % WM_PREFIX, 'gen-%s-wm-l.png' % WM_PREFIX, WM2)


def test_wm_mode_rgb():
    run_and_assert('gen-%s-img.png' % WM_PREFIX, 'gen-%s-wm-rgb.png' % WM_PREFIX, WM2)


def test_wm_mode_rgba():
    run_and_assert('gen-%s-img.png' % WM_PREFIX, 'gen-%s-wm-rgba.png' % WM_PREFIX, WM2)

