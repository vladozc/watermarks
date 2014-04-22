import logging

from watermarks.core.watermark import create_watermark 
from watermarks.core.writers import BaseWriter

logger = logging.getLogger()


def init(args):
    '''Returns initialized Visible (writer) object from arguments passed from
    command line.
    '''
    wm = create_watermark(args.watermark)
    return Visible(args.dest_dir, args.format, wm)


class Visible(BaseWriter):
    '''Visible method inserts visible watermark to top left corner of
    original image.

    '''
    allowed_formats = ('BMP', 'PNG', 'GIF', 'JPEG')
    allowed_modes = ('CMYK', 'L', 'RGB')

    def _create_watermarked(self, src_img):
        dst_img = src_img.copy()
        dst_img.paste(self.wm.img, (0, 0))
        return dst_img
