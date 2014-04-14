import logging
import os

from PIL import Image


ALLOWED_FORMATS = ('BMP', 'GIF', 'JPEG', 'PNG')
logger = logging.getLogger()


def init(args):
    '''Returns initialized Lsb (reader) object from arguments passed from
    command line.
    '''
    return Lsb(args.sources, args.dest_dir, args.format)


class Lsb(object):
    '''Class wraps the LSB functionality. It allows to extract watermark
    from more images at once. To do so, just pass list of images (folders)
    to constructor (argument `paths`). If the path is folder, it is scanned
    for images inside (not recursive). `destination` is path where extracted
    watermarks will be stored and `format` is their format (e.g. png).

    Class will generate watermark for each band separately. Generated
    watermark filepath is:
    "<destination>/<original filename>_<band shortcut>.<format>"
    '''
    allowed_modes = ('CMYK', 'L', 'RGB')

    def __init__(self, paths, destination, format):
        '''
        :param list paths:
            Filepaths/folders to be processed.

        :param str destination:
            Destination where extracted watermarks will be stored.

        :param str format:
            Watermark format.
        '''
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
            for band_name, band in zip(src_img.getbands(), bands):
                dst_filepath = os.path.join(self.destination, '%s_%s.%s' % (base_name, band_name, self.format))
                bw = band.point(convert)
                dst_band = 'P' if src_img.mode == 'P' else 'L'
                dst_img = Image.merge(dst_band, (bw, ))
                dst_img.save(dst_filepath)
                logger.info('Generated file "%s".', dst_filepath)
        else:
            logger.warning('File "%s" is in unsupported mode "%s". (skip)', filepath, src_img.mode)


def convert(x):
    '''Converts subpixel value to 0 or 255 depending on least significant
    bit.
    '''
    return 255 if (x & 1) else 0
