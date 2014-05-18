import os
import shutil
import subprocess

from nose.tools import assert_equal, assert_true

from watermarks.core.watermark import create_watermark
from watermarks.core.writers.lsb import Lsb
from .. import (
    run_writer_and_assert, DATA_DIR, in_tmp, IM_PREFIX, WM_PREFIX,
    create_data_dir,
)
from . import (
    WM1_WM, WM1_WM_JPG, WM2,
    WM_SMALL_TL, WM_SMALL_T, WM_SMALL_TR,
    WM_SMALL_L, WM_SMALL_C, WM_SMALL_R,
    WM_SMALL_BL, WM_SMALL_B, WM_SMALL_BR,
    WM_BIG_TL, WM_BIG_T, WM_BIG_TR,
    WM_BIG_L, WM_BIG_C, WM_BIG_R,
    WM_BIG_BL, WM_BIG_B, WM_BIG_BR,
)


def run_lsb_and_assert(*args, **kwargs):
    return run_writer_and_assert(Lsb, *args, **kwargs)


def small(wm, pos):
    run_lsb_and_assert(
        'gen-%s-wm-rgb.png' % WM_PREFIX, 'rgb-24-16b.png', wm,
         width=10, height=5, position=pos,
    )


def big(wm, pos):
    run_lsb_and_assert(
        'gen2-%s-rgb.png' % IM_PREFIX, 'rgb-24-16b.png', wm,
         width=5, height=3, position=pos,
    )


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


def test_wm_mode_1():
    run_lsb_and_assert('gen-%s-img.png' % WM_PREFIX, 'gen-%s-wm-1.png' % WM_PREFIX, WM2)


def test_wm_mode_l():
    run_lsb_and_assert('gen-%s-img.png' % WM_PREFIX, 'gen-%s-wm-l.png' % WM_PREFIX, WM2)


def test_wm_mode_rgb():
    run_lsb_and_assert('gen-%s-img.png' % WM_PREFIX, 'gen-%s-wm-rgb.png' % WM_PREFIX, WM2)


def test_wm_mode_rgba():
    run_lsb_and_assert('gen-%s-img.png' % WM_PREFIX, 'gen-%s-wm-rgba.png' % WM_PREFIX, WM2)


def test_small_wm_tl():
    small(WM_SMALL_TL, 'tl')


def test_small_wm_t():
    small(WM_SMALL_T, 't')


def test_small_wm_tr():
    small(WM_SMALL_TR, 'tr')


def test_small_wm_l():
    small(WM_SMALL_L, 'l')


def test_small_wm_c():
    small(WM_SMALL_C, 'c')


def test_small_wm_r():
    small(WM_SMALL_R, 'r')


def test_small_wm_bl():
    small(WM_SMALL_BL, 'bl')


def test_small_wm_b():
    small(WM_SMALL_B, 'b')


def test_small_wm_br():
    small(WM_SMALL_BR, 'br')


def test_big_wm_tl():
    big(WM_BIG_TL, 'tl')


def test_big_wm_t():
    big(WM_BIG_T, 't')


def test_big_wm_tr():
    big(WM_BIG_TR, 'tr')


def test_big_wm_l():
    big(WM_BIG_L, 'l')


def test_big_wm_c():
    big(WM_BIG_C, 'c')


def test_big_wm_r():
    big(WM_BIG_R, 'r')


def test_big_wm_bl():
    big(WM_BIG_BL, 'bl')


def test_big_wm_b():
    big(WM_BIG_B, 'b')


def test_big_wm_br():
    big(WM_BIG_BR, 'br')


def test_unsupported_format():
    run_lsb_and_assert('unsupported_format.tiff', 'rgb-24-16b.png')


def test_unsupported_mode():
    run_lsb_and_assert('unsupported_mode.png', 'rgb-24-16b.png')


def test_not_exists():
    run_lsb_and_assert('this_file_does_not_exist.png', 'rgb-24-16b.png', width=1, height=1)


@in_tmp
def test_dir(dst_dir):
    filenames = ['gen-%s-rgb.png' % IM_PREFIX, 'gen-%s-g.png' % IM_PREFIX]
    data_dir_path = create_data_dir(os.path.join(dst_dir, 'writer_dir'), filenames)
    filepath = os.path.join(DATA_DIR, 'shape1-g-l0.png')
    suffix = '_watermarked_test'

    wm = create_watermark(os.path.join(DATA_DIR, 'shape1-g-l0.png'))
    lsb = Lsb(dst_dir, 'png', wm, suffix)
    generated_filepaths = lsb.run([data_dir_path, filepath])
    generated_filenames = set([os.path.basename(f) for f in generated_filepaths])

    assert_true('gen-%s-rgb%s.png' % (IM_PREFIX, suffix) in generated_filenames)
    assert_true('gen-%s-g%s.png' % (IM_PREFIX, suffix) in generated_filenames)
    assert_true('shape1-g-l0%s.png' % suffix in generated_filenames)
    assert_equal(len(generated_filenames), 3)


@in_tmp
def test_bin(dst_dir):
    filepath = os.path.join(DATA_DIR, 'gen-%s-g.png' % IM_PREFIX)
    generated_filepath = os.path.join(dst_dir, 'gen-%s-g_watermarked_test.png' % IM_PREFIX)
    if os.path.exists(generated_filepath):
        os.unlink(generated_filepath)

    sp = subprocess.Popen(
        ['wm_writer', '-m', 'lsb', '-q', '-d', dst_dir, '-s',
         '_watermarked_test', '-w', filepath, filepath],
    )
    stdout, stderr = sp.communicate()

    assert_equal(sp.returncode, 0)
    assert_true(os.path.isfile(generated_filepath))
