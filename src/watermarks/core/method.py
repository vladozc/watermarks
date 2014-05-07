import abc
import logging
import os

from PIL import Image


logger = logging.getLogger()


class BaseMethod(object):

    def run(self, paths):
        '''Runs the process.

        :param list paths:
            Filepaths/folders to be processed.

        :return:
            List of generated files.
        :rtype: list
        '''
        processed = []
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
            return self._generate_files(filepath, src_img)
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

