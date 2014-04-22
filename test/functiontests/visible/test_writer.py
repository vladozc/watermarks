from watermarks.core.writers.visible import Visible
from .. import run_writer_and_assert
from . import WM_SMALL_TL, WM_BIG_TL


def run_visible_and_assert(*args, **kwargs):
    return run_writer_and_assert(Visible, *args, **kwargs)


def test_small_tl():
    run_visible_and_assert(
        'gen-wmode-wm-rgb.png', 'shape1-rgb-l0.png', WM_SMALL_TL,
         width=10, height=5,
    )


def test_big_tl():
    run_visible_and_assert('shape1-rgb-l0.png', 'gen-wmode-wm-rgb.png', WM_BIG_TL)
