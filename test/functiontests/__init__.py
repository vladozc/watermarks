import os
import shutil
import tempfile

from nose.tools import assert_equal, make_decorator
from PIL import Image

from watermarks.core.watermark import create_watermark
from . import generate_test_cases


ROOT_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_DIR = os.path.join(ROOT_DIR, 'test', 'data')

IM_PREFIX = 'imode'
WM_PREFIX = 'wmode'


def setup_module():
    clean()
    generate_test_cases.main(DATA_DIR, IM_PREFIX, WM_PREFIX)


def teardown_module():
    clean()


def clean():
    pass


def in_tmp(func):
    def wrapper(*args, **kwargs):
        tmp_path = tempfile.mkdtemp()
        try:
            rv = func(tmp_path, *args, **kwargs)
            shutil.rmtree(tmp_path)
            return rv
        except Exception:
            shutil.rmtree(tmp_path)
            raise
    wrapper = make_decorator(func)(wrapper)
    return wrapper


def create_data_dir(dir_path, filenames):
    os.makedirs(dir_path)
    for filename in filenames:
        shutil.copyfile(
            os.path.join(DATA_DIR, filename),
            os.path.join(dir_path, filename),
        )
    return dir_path


@in_tmp
def run_reader_and_assert(dst_dir, reader_class, filename, wm_data=None, ext=None, bands_are_filtered=False, **kwargs):
    base, f_ext = os.path.splitext(filename)
    ext = ext or f_ext
    filepath = os.path.join(DATA_DIR, filename)
    reader = reader_class(destination=dst_dir, format_=ext.lstrip('.'), **kwargs)
    results = list(reader.run([filepath]))
    if wm_data is None:
        assert_equal(len(results), 0)
        return
    src_img = Image.open(filepath)
    if bands_are_filtered:
        assert_equal(len(results), len(wm_data))
    else:
        assert_equal(len(results), len(src_img.getbands()))
    for i, res_filepath in enumerate(results):
        res_img = Image.open(res_filepath)
        res_img.load()
        expected_data = wm_data[i] if bands_are_filtered else wm_data
        assert_equal(list(res_img.getdata()), expected_data)


@in_tmp
def run_writer_and_assert(dst_dir, writer_class, filename, wm_filename,
                          wm_data=None, ext=None, width=None, height=None,
                          position='', bands_are_filtered=False, **kwargs):
    base, f_ext = os.path.splitext(filename)
    ext = ext or f_ext
    filepath = os.path.join(DATA_DIR, filename)
    wm_filepath = os.path.join(DATA_DIR, wm_filename)
    suffix = '_watermarked_test'
    if not width or not height:
        img = Image.open(filepath)
        width, height = img.size
    wm = create_watermark(wm_filepath, width=width, height=height, position=position)
    writer = writer_class(destination=dst_dir, format_=ext.lstrip('.'),
        wm=wm, suffix=suffix, position=position, **kwargs)
    results = list(writer.run([filepath]))
    if wm_data is None:
        assert_equal(len(results), 0)
        return
    assert_equal(len(results), 1)
    res_filepath = results[0]
    res_img = Image.open(res_filepath)
    res_img.load()
    for i, band in enumerate(res_img.split()):
        expected_data = wm_data[i] if bands_are_filtered else wm_data
        assert_equal(list(band.getdata()), expected_data)
