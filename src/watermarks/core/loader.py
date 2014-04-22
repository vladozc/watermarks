import logging


logger = logging.getLogger()


class Loader(object):
    '''Class responsible for loading and running watermark method.
    Method will first be searched in local modules and if it will not be
    found, Loader will try to find it in global scope (so you can use
    your own methods).
    '''
    def __init__(self, type_=''):
        '''
        :param str type_:
            readers/writers This parameter is used only for local methods
            and it is part of import path.
        '''
        self.type = type_

    def run(self, args):
        '''Runs desired watermark method with `args`.'''
        module = self._load_method(args.method)
        x = module.init(args)
        return x.run()

    def _load_method(self, method):
        local_method = self.__module__.rsplit('.', 1)[0] + '.' + self.type + '.' + method
        try:
            logger.debug('Trying to load method from local modules.')
            module = __import__(local_method, fromlist=('init',))
        except ImportError:
            logger.debug('Loading method from local modules failed, trying '
                         'to load from global scope.')
            module = __import__(method, fromlist=('init',))
        return module
