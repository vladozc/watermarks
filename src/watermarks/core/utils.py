def get_correct_wm(args, method_name):
    methods = args.methods.split(',')
    i = methods.index(method_name)
    # TODO: except KeyError: raise InvalidArgumentsError
    return args.watermark[i]
