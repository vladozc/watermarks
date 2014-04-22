import os

from nose.tools import assert_equal
from PIL import Image

from watermarks.core.watermark import create_watermark


DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
DST_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'tmp')


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
    writer = writer_class([filepath], DST_DIR, ext.lstrip('.'), wm, suffix)
    results = writer.run()
    assert_equal(len(results), 1)
    res_filepath = results[0]
    res_img = Image.open(res_filepath)
    res_img.load()
    for band in res_img.split():
        assert_equal(list(band.getdata()), wm_data)

