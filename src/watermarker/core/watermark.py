import logging

from PIL import Image


ALLOWED_FORMATS = ('bmp', 'jpg', 'jpeg', 'png')
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
        self.init()

    def init(self):
        '''Initializes watermark - load, set width/height, ...'''
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


class WatermarkFile(Watermark):
    '''Watermark image specified by filepath.'''
    def __init__(self, filepath, *args, **kwargs):
        self.filepath = filepath
        img = Image.open(filepath)
        super(WatermarkFile, self).__init__(img=img, *args, **kwargs)


class WatermarkImg(Watermark):
    '''Watermark image with specified size.'''
    def __init__(self, img, width, height, *args, **kwargs):
        sized_img = Image.new('1', (width, height), 'white')
        # todo: merge img to sized_img (center)
        super(WatermarkFile, self).__init__(img=sized_img, *args, **kwargs)

