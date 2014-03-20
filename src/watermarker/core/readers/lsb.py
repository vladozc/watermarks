from itertools import izip
import logging
import os

from PIL import Image


ALLOWED_FORMATS = ('BMP', 'GIF', 'JPEG', 'PNG')
logger = logging.getLogger()


def init(args):
    return Lsb(args.sources, args.dest_dir, args.format)


class Lsb(object):

    allowed_modes = ('CMYK', 'L', 'RGB')

    def __init__(self, paths, destination, format):
        self.paths = paths
        self.destination = destination
        self.format = format

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
            for band_name, band in izip(src_img.getbands(), bands):
                dst_filepath = os.path.join(self.destination, '%s_%s.%s' % (base_name, band_name, self.format))
                bw = band.point(convert)
                dst_band = 'P' if src_img.mode == 'P' else 'L'
                dst_img = Image.merge(dst_band, (bw, ))
                dst_img.save(dst_filepath)
                logger.info('Generated file "%s".', dst_filepath)
        else:
            logger.warning('File "%s" is in unsupported mode "%s". (skip)', filepath, src_img.mode)


def convert(x):
    return 255 if (x & 1) else 0
