import os

from nose.tools import assert_equal
from PIL import Image

from watermarks.core.watermark import create_watermark


DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
DST_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'tmp')


def run_reader_and_assert(reader_class, filename, wm_data, ext=None):
    base, f_ext = os.path.splitext(filename)
    ext = ext or f_ext
    filepath = os.path.join(DATA_DIR, filename)
    reader = reader_class(DST_DIR, ext.lstrip('.'))
    results = list(reader.run([filepath]))
    src_img = Image.open(filepath)
    assert_equal(len(results), len(src_img.getbands()))
    for res_filepath in results:
        res_img = Image.open(res_filepath)
        res_img.load()
        assert_equal(list(res_img.getdata()), wm_data)


def run_writer_and_assert(writer_class, filename, wm_filename, wm_data, 
                          ext=None, width=None, height=None):
    base, f_ext = os.path.splitext(filename)
    ext = ext or f_ext
    filepath = os.path.join(DATA_DIR, filename)
    wm_filepath = os.path.join(DATA_DIR, wm_filename)
    suffix = '_watermarked_test'
    if not width or not height:
        img = Image.open(filepath)
        width, height = img.size
    wm = create_watermark(wm_filepath, width=width, height=height)
    writer = writer_class(DST_DIR, ext.lstrip('.'), wm, suffix)
    results = list(writer.run([filepath]))
    assert_equal(len(results), 1)
    res_filepath = results[0]
    res_img = Image.open(res_filepath)
    res_img.load()
    for band in res_img.split():
        assert_equal(list(band.getdata()), wm_data)
