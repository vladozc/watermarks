from watermarks.core.writers.visible import Visible
from .. import run_writer_and_assert
from . import (
    WM_SMALL_TL, WM_SMALL_T, WM_SMALL_TR,
    WM_SMALL_L, WM_SMALL_C, WM_SMALL_R,
    WM_SMALL_BL, WM_SMALL_B, WM_SMALL_BR,
    WM_BIG_TL, WM_BIG_T, WM_BIG_TR,
    WM_BIG_L, WM_BIG_C, WM_BIG_R,
    WM_BIG_BL, WM_BIG_B, WM_BIG_BR,
)


def run_visible_and_assert(*args, **kwargs):
    return run_writer_and_assert(Visible, *args, **kwargs)


def small(wm, pos):
    run_visible_and_assert(
        'gen-wmode-wm-rgb.png', 'shape1-rgb-l0.png', wm,
         width=10, height=5, position=pos,
    )


def big(wm, pos):
    run_visible_and_assert(
        'shape1-rgb-l0.png', 'gen-wmode-wm-rgb.png', wm, position=pos)


def test_small_tl():
    small(WM_SMALL_TL, 'TL')


def test_small_t():
    small(WM_SMALL_T, 'T')


def test_small_tr():
    small(WM_SMALL_TR, 'TR')


def test_small_l():
    small(WM_SMALL_L, 'L')


def test_small_c():
    small(WM_SMALL_C, 'C')


def test_small_r():
    small(WM_SMALL_R, 'R')


def test_small_bl():
    small(WM_SMALL_BL, 'BL')


def test_small_b():
    small(WM_SMALL_B, 'B')


def test_small_br():
    small(WM_SMALL_BR, 'BR')


def test_big_tl():
    big(WM_BIG_TL, 'TL')


def test_big_t():
    big(WM_BIG_T, 'T')


def test_big_tr():
    big(WM_BIG_TR, 'TR')


def test_big_l():
    big(WM_BIG_L, 'L')


def test_big_c():
    big(WM_BIG_C, 'C')


def test_big_r():
    big(WM_BIG_R, 'R')

def test_big_bl():
    big(WM_BIG_BL, 'BL')


def test_big_b():
    big(WM_BIG_B, 'B')


def test_big_br():
    big(WM_BIG_BR, 'BR')

