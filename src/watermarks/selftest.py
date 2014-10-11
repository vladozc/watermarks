import os

from PIL import Image


def selftest(tmp='/tmp'):
    filepath = os.path.join(tmp, 'watermarks_test.png')
    _clean(filepath)
    try:
        _do_test(filepath)
        _clean(filepath)
        return True
    except Exception as edata:
        print('Error: {0}'.format(edata))
        return False


def _do_test(filepath):
    sample_data = [1, 2, 3, 4]
    band = Image.new('L', (2, 2))
    band.putdata(sample_data)

    img = Image.merge('L', [band])
    img.save(filepath)

    if not os.path.exists(filepath):
        raise Exception('file was not created')

    img = Image.open(filepath)
    img.load()
    img_data = list(img.split()[0].getdata())

    if sample_data != img_data:
        raise Exception('image has invalid data')


def _clean(filepath):
    if os.path.exists(filepath):
        os.unlink(filepath)
