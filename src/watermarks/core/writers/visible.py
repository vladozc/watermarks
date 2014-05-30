import logging
import math

from watermarks.core.watermark import create_watermark 
from watermarks.core.writers import BaseWriter

logger = logging.getLogger()


def update_parser(parser):
    pass


def init(args):
    '''Returns initialized Visible (writer) object from arguments passed from
    command line.
    '''
    wm = create_watermark(args.watermark)
    return Visible(args.dest_dir, args.format, wm, args.suffix)


class Visible(BaseWriter):
    '''Visible method inserts visible watermark to top left corner of
    original image.

    '''
    allowed_formats = ('BMP', 'PNG', 'GIF', 'JPEG')
    allowed_modes = ('CMYK', 'L', 'RGB')

    def _create_watermarked(self, src_img):
        dst_img = src_img.copy()
        dst_w, dst_h = dst_img.size
        wm_w, wm_h = self.wm.img.size
        right = dst_w - wm_w
        bottom = dst_h - wm_h
        center_w = int(math.floor(right / 2.0) if right > 0 else math.ceil(right / 2.0))
        center_h = int(math.floor(bottom / 2.0) if bottom > 0 else math.ceil(bottom / 2.0))
        if self.position == 'TL':
            dst_img.paste(self.wm.img, (0, 0))
        elif self.position == 'T':
            dst_img.paste(self.wm.img, (center_w, 0))
        elif self.position == 'TR':
            dst_img.paste(self.wm.img, (right, 0))
        elif self.position == 'L':
            dst_img.paste(self.wm.img, (0, center_h))
        elif self.position == 'R':
            dst_img.paste(self.wm.img, (right, center_h))
        elif self.position == 'BL':
            dst_img.paste(self.wm.img, (0, bottom))
        elif self.position == 'B':
            dst_img.paste(self.wm.img, (center_w, bottom))
        elif self.position == 'BR':
            dst_img.paste(self.wm.img, (right, bottom))
        else:
            dst_img.paste(self.wm.img, (center_w, center_h))
        return dst_img
