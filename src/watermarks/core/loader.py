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
        self.modules = None

    def run(self, args, chaining=False):
        '''Runs desired watermark methods with `args`.'''
        new_files = []
        if not self.modules:
            self.load_methods(args.methods)
        for module in self.modules:
            x = module.init(args)
            if chaining:
                new_files = x.run(args.sources)
                args.sources = new_files
                args.suffix = ''
            else:
                new_files.extend(x.run(args.sources))
        return new_files

    def load_methods(self, methods):
        self.modules = []
        for method in methods.split(','):
            local_method = self.__module__.rsplit('.', 1)[0] + '.' + self.type \
                + '.' + method
            try:
                logger.debug('Trying to load method from local modules.')
                module = __import__(local_method, fromlist=('init', 'update_args'))
            except ImportError:
                logger.debug('Loading method from local modules failed, trying '
                             'to load from global scope.')
                module = __import__(method, fromlist=('init', 'update_args'))
            self.modules.append(module)
