import abc
import logging
import os

from PIL import Image

from watermarks.core.method import BaseMethod


logger = logging.getLogger()


class BaseWriter(BaseMethod):
    '''Base class for writers. It is responsible for selecting files to
    be processed, checking them and calling watermark method on them.    

    '''
    __metaclass__ = abc.ABCMeta

    def __init__(self, destination, format, wm, suffix='_watermarked'):
        '''
        :param str destination:
            Destination where watermarked images will be stored.

        :param str format:
            Output format.

        :param watermarks.core.watermark wm:
            Watermark instance.

        :param str suffix:
            Suffix added to generated files. If set to empty string,
            generated image will overwrite original image.
        '''
        self.destination = destination
        self.format = format
        self.wm = wm
        self.suffix = suffix

    def _generate_files(self, filepath, src_img):
        base_name, _ = os.path.splitext(os.path.basename(filepath))
        logger.info('Processing file "%s"', filepath)
        dst_filepath = os.path.join(self.destination, '%s%s.%s' % (base_name, self.suffix, self.format))
        dst_img = self._create_watermarked(src_img)
        dst_img.save(dst_filepath)
        logger.info('Generated file "%s".', dst_filepath)
        return [dst_filepath]
