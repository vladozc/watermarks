import logging
import os
import math

import six
from PIL import Image


ALLOWED_FORMATS = ('BMP', 'JPEG', 'PNG')
# mode color depth, http://effbot.org/imagingbook/concepts.htm
MODE_DEPTHS = {
    '1': 1,
    'L': 8,
    'RGB': 8,
    'RGBA': 8,
    'CMYK': 8,
    #'I': 32,
    #'F': 32,
}
logger = logging.getLogger()


class Watermark(object):
    '''Basic class for image that will be put to other image as watermark.
    As input, it works with image object.
    '''
    def __init__(self, img):
        self.img = img

    def init(self):
        '''Initializes watermark - load, set width/height, ...'''
        if self.img.format not in ALLOWED_FORMATS:
            logger.warning('Watermark format "%s" is not allowed. (skip)', self.img.format)
            raise ValueError()
        self.img.load()
        self.width, self.height = self.img.size
        self.band = self.img.split()[0]
        self.threshold = self.get_px_max_value() / 2

    def get_px_max_value(self):
        '''Determines maximum pixel value according to used mode.'''
        try:
            return 2 ** MODE_DEPTHS[self.img.mode] - 1
        except KeyError:
            logger.critical('Watermark mode "%s" is not supported!', 
                            self.img.mode)
            raise


def create_watermark(wm, width=None, height=None, position=None, *args, **kwargs):
    if isinstance(wm, six.string_types):
        if not os.path.isfile(wm):
            logger.critical('Watermark file "%s" does not exist!' % wm)
            exit(1)
        wm = Image.open(wm)

    if width and height:
        img_w, img_h = wm.size
        if img_w != width or img_h != height:
            right = width - img_w
            bottom = height - img_h
            center_w = math.floor(right / 2) if right > 0 else math.ceil(right / 2)
            center_h = math.floor(bottom / 2) if bottom > 0 else math.ceil(bottom / 2)
            sized_img = Image.new(wm.mode, (width, height), 'white')
            position = position.upper()
            if position == 'TL':
                sized_img.paste(wm, (0, 0))
            elif position == 'T':
                sized_img.paste(wm, (center_w, 0))
            elif position == 'TR':
                sized_img.paste(wm, (right, 0))
            elif position == 'L':
                sized_img.paste(wm, (0, center_h))
            elif position == 'R':
                sized_img.paste(wm, (right, center_h))
            elif position == 'BL':
                sized_img.paste(wm, (0, bottom))
            elif position == 'B':
                sized_img.paste(wm, (center_w, bottom))
            elif position == 'BR':
                sized_img.paste(wm, (right, bottom))
            else:
                sized_img.paste(wm, (center_w, center_h))
            sized_img.format = wm.format
            wm = sized_img

    wm_instance = Watermark(wm, *args, **kwargs)
    wm_instance.init()
    return wm_instance
