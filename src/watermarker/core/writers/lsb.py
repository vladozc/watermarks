import logging
import os

from PIL import Image

from watermarker.core.watermark import Watermark, WatermarkFile, WatermarkImg

ALLOWED_FORMATS = ('BMP', 'PNG', 'GIF', 'JPEG')
logger = logging.getLogger()


def init(args):
    return Lsb(args.sources, args.dest_dir, args.format, args.watermark)


class Lsb(object):

    allowed_modes = ('CMYK', 'L', 'RGB')

    def __init__(self, paths, destination, format, wm_filepath, suffix='_watermarked'):
        self.paths = paths
        self.destination = destination
        self.format = format
        self.wm = WatermarkFile(wm_filepath)
        self.suffix = suffix

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
        src_img = Image.open(filepath)
        if src_img.format not in ALLOWED_FORMATS:
            logger.warning('File "%s" is in not allowed format. (skip)', filepath)
            return

        if src_img.mode in self.allowed_modes:
            base_name, _ = os.path.splitext(os.path.basename(filepath))
            logger.info('Processing file "%s"', filepath)
            src_img.load()
            bands = src_img.split()
            dst_filepath = os.path.join(self.destination, '%s%s.%s' % (base_name, self.suffix, self.format))
            bands_wm = []
            for band in bands:
                band_wm = Image.new('L', src_img.size)
                band_wm.putdata([convert(orig_px, wm_px, self.wm.threshold) 
                                 for orig_px, wm_px 
                                 in zip(band.getdata(), self.wm.band.getdata())
                                ])
                bands_wm.append(band_wm)
            dst_img = Image.merge(src_img.mode, bands_wm)
            dst_img.save(dst_filepath)
            logger.info('Generated file "%s".', dst_filepath)
        else:
            logger.warning('File "%s" is in unsupported mode "%s". (skip)', filepath, src_img.mode)


def convert(orig_px, wm_px, threshold):
    if wm_px <= threshold:
        return orig_px & 254
    return orig_px | 1
