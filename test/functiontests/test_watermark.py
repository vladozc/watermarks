import os

from nose.tools import raises

from watermarks.core.watermark import create_watermark
from . import DATA_DIR


@raises(ValueError)
def test_unsupported_format():
    create_watermark(os.path.join(DATA_DIR, 'unsupported_format.tiff'))
