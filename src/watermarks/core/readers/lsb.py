import logging
import os

from PIL import Image

from watermarks.core.readers import BaseReader


logger = logging.getLogger()


def init(args):
    '''Returns initialized Lsb (reader) object from arguments passed from
    command line.
    '''
    return Lsb(args.dest_dir, args.format, args.suffix)


class Lsb(BaseReader):
    '''Class wraps the LSB functionality. It allows to extract watermark
    from more images at once. To do so, just pass list of images (folders)
    to run() (argument `paths`). If the path is folder, it is scanned
    for images inside (not recursive). `destination` is path where extracted
    watermarks will be stored and `format` is their format (e.g. png).

    Class will generate watermark for each band separately. Generated
    watermark filepath is:
    "<destination>/<original filename>_<band shortcut>.<format>"
    '''
    allowed_formats = ('BMP', 'GIF', 'JPEG', 'PNG')
    allowed_modes = ('CMYK', 'L', 'RGB')

    def _create_watermarked(self, src_img):
        dst_imgs = []
        src_img.load()
        bands = src_img.split()
        for band_name, band in zip(src_img.getbands(), bands):
            bw = band.point(convert)
            dst_band = 'P' if src_img.mode == 'P' else 'L'
            dst_img = Image.merge(dst_band, (bw, ))
            dst_imgs.append(dst_img)
        return dst_imgs


def convert(x):
    '''Converts subpixel value to 0 or 255 depending on least significant
    bit.

    :param int x:
        Current subpixel value.
    :return:
        New subpixel value.
    :rtype: int
    '''
    return 255 if (x & 1) else 0
