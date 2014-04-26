from nose.tools import assert_true

from watermarks.selftest import selftest


def test_selftest():
    assert_true(selftest())
