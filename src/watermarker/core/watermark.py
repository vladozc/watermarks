import logging

from PIL import Image


ALLOWED_FORMATS = ('bmp', 'jpg', 'jpeg', 'png')
logger = logging.getLogger()


class Watermark(object):

    def __init__(self, img):
        self.img = img
        self.init()

    def init(self):
        if self.img.mode != '1':
            logger.info('Converting watermark image to correct color model.')
            self.img = self.img.convert('1')
        self.img.load()
        self.width, self.height = self.img.size
        self.band = self.img.split()[0]


class WatermarkFile(Watermark):

    def __init__(self, filepath, *args, **kwargs):
        self.filepath = filepath
        img = Image.open(filepath)
        super(WatermarkFile, self).__init__(img=img, *args, **kwargs)


class WatermarkImg(Watermark):

    def __init__(self, img, width, height, *args, **kwargs):
        sized_img = Image.new('1', (width, height), 'white')
        # todo: merge img to sized_img
        super(WatermarkFile, self).__init__(img=sized_img, *args, **kwargs)

