import logging

from PIL import Image

from watermarks.core.watermark import create_watermark
from watermarks.core.writers import BaseWriter

logger = logging.getLogger()


def update_parser(parser):
    pass


def init(args):
    '''Returns initialized Lsb (writer) object from arguments passed from
    command line.
    '''
    wm = create_watermark(args.watermark)
    return Lsb(args.dest_dir, args.format, wm, args.suffix)


class Lsb(BaseWriter):
    '''Lsb (least significant bit) is method that changes least significant
    (last) bit for every subpixel in image according to reference image.
    With this approach you can generate new image almost identical to
    original image but with your hidden watermark.
    '''
    allowed_formats = ('BMP', 'PNG', 'GIF', 'JPEG')
    allowed_modes = ('CMYK', 'L', 'RGB')

    def _create_watermarked(self, src_img):
        src_img.load()
        bands = src_img.split()
        bands_wm = []
        src_width, src_height = src_img.size
        wm_width, wm_height = self.wm.img.size
        if src_width == wm_width and src_height == wm_height:
            wm = self.wm
        else:
            wm = create_watermark(self.wm.img, width=src_width,
                                  height=src_height, position=self.position)
        for band in bands:
            band_wm = Image.new('L', src_img.size)
            band_wm.putdata([convert(orig_px, wm_px, wm.threshold)
                             for orig_px, wm_px
                             in zip(band.getdata(), wm.band.getdata())
                             ])
            bands_wm.append(band_wm)
        dst_img = Image.merge(src_img.mode, bands_wm)
        return dst_img


def convert(orig_px, wm_px, threshold):
    '''Returns modified (last bit) value for subpixel.

    :param int orig_px:
        Current image subpixel value.
    :param int wm_px:
        Watermark subpixel value.
    :param int threshold:
        If `wm_px` is less or equal than this value, `orig_px` will
        change it's last bit value to 0 and to 1 if greater.
    :return:
        New subpixel value.
    :rtype: int
    '''
    if wm_px <= threshold:
        return orig_px & 254
    return orig_px | 1
