import os

from nose.tools import assert_equal, assert_true
from PIL import Image

from .. import DATA_DIR, IM_PREFIX, in_tmp
from . import WM_WRITER, run_command


def compare_results(generated_fp, expected_fp):
    generated_img = Image.open(generated_fp)
    expected_img = Image.open(expected_fp)
    generated_bands = generated_img.split()
    expected_bands = expected_img.split()
    assert_equal(len(generated_bands), len(expected_bands))
    assert_true(len(generated_bands) > 0)
    for b1, b2 in zip(generated_bands, expected_bands):
        assert_equal(list(b1.getdata()), list(b2.getdata()))


@in_tmp
def run_and_assert(dst_dir, position=None):
    wm = os.path.join(DATA_DIR, 'white.png')
    img = os.path.join(DATA_DIR, 'black.png')
    position_arg = ['-p%s' % position] if position else []
    rc = run_command([WM_WRITER, 'visible'] + position_arg + ['-w', wm, '-d', dst_dir, img])
    assert_equal(rc, 0)
    generated_fp = os.path.join(dst_dir, 'black.png')
    expected_fp = os.path.join(DATA_DIR, 'black-%s.png' % (position or 'default', ))
    compare_results(generated_fp, expected_fp)


def test_default():
    run_and_assert()


def test_tl():
    run_and_assert(position='TL')


def test_t():
    run_and_assert(position='T')


def test_tr():
    run_and_assert(position='TR')


def test_l():
    run_and_assert(position='L')


def test_c():
    run_and_assert(position='C')


def test_r():
    run_and_assert(position='R')


def test_bl():
    run_and_assert(position='BL')


def test_b():
    run_and_assert(position='B')


def test_br():
    run_and_assert(position='BR')
