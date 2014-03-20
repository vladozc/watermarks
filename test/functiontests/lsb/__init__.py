import os

import generate_test_cases


WM1_1 = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]

WM1_255 = [255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255]

WM1_WM = [254, 255, 255, 255, 1, 0, 255, 255, 255, 255,  1, 0, 1, 1, 1, 1, 0, 1, 1, 1,   255, 255, 254, 255, 1, 1, 255, 254, 255, 255,   1, 1, 1, 0, 1, 1, 1, 1, 0, 1,    255, 255, 255, 255, 0, 1, 255, 255, 255, 254]

WM2 = [254]*64 + [0]*64 + [255]*64 + [1]*64

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
DST_DIR = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'tmp')

IM_PREFIX = 'imode'
WM_PREFIX = 'wmode'


def setup_module():
    if not os.path.exists(DST_DIR):
        os.mkdir(DST_DIR)
    generate_test_cases.main(DATA_DIR, IM_PREFIX, WM_PREFIX)

