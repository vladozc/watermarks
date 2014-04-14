import os

import generate_test_cases


WM1_1 = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]

WM1_255 = [255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255]

WM1_255_JPG = [0, 255, 255, 255, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255]

WM1_WM = [254, 255, 255, 255, 1, 0, 255, 255, 255, 255,  1, 0, 1, 1, 1, 1, 0, 1, 1, 1,   255, 255, 254, 255, 1, 1, 255, 254, 255, 255,   1, 1, 1, 0, 1, 1, 1, 1, 0, 1,    255, 255, 255, 255, 0, 1, 255, 255, 255, 254]


# TODO: check that this is correct
WM1_WM_JPG = [250, 255, 239, 246, 13, 0, 255, 245, 255, 255, 3, 0, 0, 20, 0, 8, 14, 0, 0, 0, 255, 255, 254, 245, 4, 0, 254, 252, 254, 254, 0, 0, 3, 16, 7, 26, 4, 3, 3, 3, 255, 252, 255, 251, 0, 0, 255, 252, 249, 249]


WM2 = [254]*64 + [0]*64 + [255]*64 + [1]*64

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
DST_DIR = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'tmp')

IM_PREFIX = 'imode'
WM_PREFIX = 'wmode'


def setup_module():
    clean()
    if not os.path.exists(DST_DIR):
        os.mkdir(DST_DIR)
    generate_test_cases.main(DATA_DIR, IM_PREFIX, WM_PREFIX)


def teardown_module():
    clean()


def clean():
    if os.path.isdir(DST_DIR):
        for filename in os.listdir(DST_DIR):
            os.unlink(os.path.join(DST_DIR, filename))
