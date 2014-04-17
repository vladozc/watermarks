import logging
import os

from PIL import Image

from watermarker.core.watermark import Watermark, WatermarkFile, WatermarkImg

ALLOWED_FORMATS = ('BMP', 'PNG', 'GIF', 'JPEG')
logger = logging.getLogger()


def init(args):
    '''Returns initialized Lsb (reader) object from arguments passed from
    command line.
    '''
    wm = WatermarkFile(args.watermark)
    return Lsb(args.sources, args.dest_dir, args.format, wm)


class Lsb(object):
    '''Lsb (least significant bit) is method that changes least significant
    (last) bit for every subpixel in image according to reference image.
    With this approach you can generate new image almost identical to
    original image but with your hidden watermark.
    '''
    allowed_modes = ('CMYK', 'L', 'RGB')

    def __init__(self, paths, destination, format, wm, suffix='_watermarked'):
        '''
        :param list paths:
            Filepaths/folders to be processed.

        :param str destination:
            Destination where watermarked images will be stored.

        :param str format:
            Output format.

        :param watermarker.core.watermark wm:
            Watermark instance.

        :param str suffix:
            Suffix added to generated files. If set to empty string,
            generated image will overwrite original image.
        '''
        self.paths = paths
        self.destination = destination
        self.format = format
        self.wm = wm
        self.suffix = suffix

    def run(self):
        '''Runs the process.

        :return:
            List of generated files.
        :rtype: list
        '''
        processed = []
        for path in self.paths:
            if not os.path.exists(path):
                logger.error('Path "%s" does not exist! (skip)', path)
            elif os.path.isdir(path):
                processed.extend(self._process_dir(path))
            elif os.path.isfile(path):
                processed.append(self._process_file(path))
            else:
                raise NotImplementedError('Cannot determine type of %s', path)
        return filter(None, processed)

    def _process_dir(self, dirpath):
        processed = []
        for filename in os.listdir(dirpath):
            full_filepath = os.path.join(dirpath, filename)
            if os.path.isfile(full_filepath):
                res = self._process_file(full_filepath)
                processed.append(res)
        return processed

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
            return dst_filepath
        else:
            logger.warning('File "%s" is in unsupported mode "%s". (skip)', filepath, src_img.mode)


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
