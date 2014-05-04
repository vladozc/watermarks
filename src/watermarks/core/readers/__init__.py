import abc
import logging
import os

from PIL import Image


logger = logging.getLogger()


class BaseReader(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, destination, format_):
        '''
        :param str destination:
            Destination where extracted watermarks will be stored.

        :param str format_:
            Watermark format.
        '''
        self.destination = destination
        self.format = format_

    def run(self, paths):
        '''Runs the process.

        :param list paths:
            Filepaths/folders to be processed.

        :return:
            List of generated files.
        :rtype: list
        '''
        processed = []
        if not os.path.exists(self.destination):
            os.makedirs(self.destination)
        for path in paths:
            if not os.path.exists(path):
                logger.error('Path "%s" does not exist! (skip)', path)
            elif os.path.isdir(path):
                processed.extend(self._process_dir(path))
            elif os.path.isfile(path):
                processed.extend(self._process_file(path))
            else:
                raise NotImplementedError('Cannot determine type of %s', path)
        return filter(None, processed)

    def _process_dir(self, dirpath):
        processed = []
        for filename in os.listdir(dirpath):
            full_filepath = os.path.join(dirpath, filename)
            if os.path.isfile(full_filepath):
                res = self._process_file(full_filepath)
                processed.extend(res)
        return processed

    def _process_file(self, filepath):
        src_img = Image.open(filepath)
        if src_img.format not in self.allowed_formats:
            logger.warning('File "%s" is in not allowed format. (skip)', filepath)
            return []

        if src_img.mode in self.allowed_modes:
            generated_filepaths = []
            base_name, _ = os.path.splitext(os.path.basename(filepath))
            logger.info('Processing file "%s"', filepath)
            dst_imgs = self._create_watermarked(src_img)
            for band_name, dst_img in zip(src_img.getbands(), dst_imgs):
                dst_filepath = os.path.join(self.destination, '%s_%s.%s' % (base_name, band_name, self.format))
                dst_img.save(dst_filepath)
                logger.info('Generated file "%s".', dst_filepath)
                generated_filepaths.append(dst_filepath)
            return generated_filepaths
        else:
            logger.warning('File "%s" is in unsupported mode "%s". (skip)', filepath, src_img.mode)
            return []

    @abc.abstractproperty
    def _create_watermarked(self, src_img):
        '''Method responsible for reading wm from single image.'''

    @abc.abstractproperty
    def allowed_formats(self):
        '''List of allowed image formats for particular method.'''

    @abc.abstractproperty
    def allowed_modes(self):
        '''List of allowed image modes for particular method.'''
