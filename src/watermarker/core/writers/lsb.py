from itertools import izip
import logging
import os

from PIL import Image

from watermarker.core.watermark import Watermark, WatermarkFile, WatermarkImg

ALLOWED_FORMATS = ('bmp', 'png', 'gif')
logger = logging.getLogger()


def init(args):
    return Lsb(args.sources, args.dest_dir, args.format, args.watermark)


class Lsb(object):

    allowed_modes = ('CMYK', 'L', 'RGB')

    def __init__(self, paths, destination, format, wm_filepath):
        self.paths = paths
        self.destination = destination
        self.format = format
        self.wm = WatermarkFile(wm_filepath)

    def run(self):
        for path in self.paths:
            if not os.path.exists(path):
                logger.error('Path "%s" does not exist! (skip)', path)
            elif os.path.isdir(path):
                self._process_dir(path)
            elif os.path.isfile(path):
                self._process_file(path)
            else:
                raise NotImplementedError('Cannot determine type of %s', path)
        return 0

    def _process_dir(self, dirpath):
        for filename in os.listdir(dirpath):
            full_filepath = os.path.join(dirpath, filename)
            if os.path.isfile(full_filepath):
                self._process_file(full_filepath)

    def _process_file(self, filepath):
        base_name, src_format = os.path.splitext(os.path.basename(filepath))
        if src_format[1:].lower() not in ALLOWED_FORMATS:
            logger.warning('File "%s" is in not allowed format. (skip)', filepath)
            return

        src_img = Image.open(filepath)
        if src_img.mode in self.allowed_modes:
            logger.info('Processing file "%s"', filepath)
            src_img.load()
            bands = src_img.split()
            dst_filepath = os.path.join(self.destination, '%s_watermarked.%s' % (base_name, self.format))
            bands_wm = []
            for band in bands:
                band_wm = Image.new('L', src_img.size)
                band_wm.putdata([convert(orig_px, wm_px) for orig_px, wm_px in izip(band.getdata(), self.wm.band.getdata())])
                bands_wm.append(band_wm)
            dst_img = Image.merge(src_img.mode, bands_wm)
            dst_img.save(dst_filepath)
            logger.info('Generated file "%s".', dst_filepath)
        else:
            logger.warning('File "%s" is in unsupported mode "%s". (skip)', filepath, src_img.mode)


def convert(orig_px, wm_px):
    if wm_px == 0:
        return orig_px & 254
    return orig_px | 1
