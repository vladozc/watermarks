import logging

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
    As input, it works with raw image data.
    '''
    def __init__(self, img):
        self.img = img

    def init(self):
        '''Initializes watermark - load, set width/height, ...'''
        if self.img.format not in ALLOWED_FORMATS:
            logger.warning('Watermark is in not allowed format. (skip)')
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
            logger.critical('Watermark band "%s" is not supported!', 
                            self.img.mode)
            raise


def create_watermark(wm, width=None, height=None, *args, **kwargs):
    if isinstance(wm, basestring):
        wm = Image.open(wm)

    if width and height:
        img_w, img_h = img.size
        if img_w != width or img_h != height:
            # TODO
            pass

    wm_instance = Watermark(wm, *args, **kwargs)
    wm_instance.init()
    return wm_instance
