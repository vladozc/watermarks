import os

from PIL import Image


def main():
    dst_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'test',
        'data',
    )
    band_data = [255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255]
    band_wm = Image.new('L', (10, 5))
    band_wm.putdata(band_data)

    for format_ in ('png', 'gif', 'bmp'):
        img = Image.merge('L', [band_wm])
        img.save(os.path.join(dst_path, 'gen-g.%s' % format_))

    for format_ in ('png', 'bmp'):
        img = Image.merge('RGB', [band_wm]*3)
        img.save(os.path.join(dst_path, 'gen-rgb.%s' % format_))


if __name__ == '__main__':
    main()

