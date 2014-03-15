import logging


logger = logging.getLogger()


class Loader(object):

    def __init__(self, type_, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.type = type_

    def run(self, args):
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
                         'to load from global space.')
            module = __import__(method, fromlist=('init',))
        return module
