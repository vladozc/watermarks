import os
import sys

from PIL import Image


def main(dst_path, img_modes_prefix, wm_modes_prefix):
    generate_img_modes_types(dst_path, img_modes_prefix)
    generate_wm_modes(dst_path, wm_modes_prefix)
    return 0


def generate_img_modes_types(dst_path, prefix):
    band_data = [255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 255, 255, 255, 255]
    band_wm = Image.new('L', (10, 5))
    band_wm.putdata(band_data)

    for format_ in ('png', 'gif', 'bmp'):
        img = Image.merge('L', [band_wm])
        img.save(os.path.join(dst_path, 'gen-%s-g.%s' % (prefix, format_)))

    for format_ in ('png', 'bmp', 'jpg'):
        img = Image.merge('RGB', [band_wm]*3)
        img.save(os.path.join(dst_path, 'gen-%s-rgb.%s' % (prefix, format_)))


def generate_wm_modes(dst_path, prefix):
    band_1 = Image.new('1', (16, 16))
    band_1.putdata([0] * 128 + [1] * 128)
    band_8 = Image.new('L', (16, 16))
    band_8.putdata(range(256))
    band_a = Image.new('L', (16, 16))
    band_a.putdata([255]*256)

    wm_1 = Image.merge('1', [band_1])
    wm_1.save(os.path.join(dst_path, 'gen-%s-wm-1.png' % prefix))

    wm_l = Image.merge('L', [band_8])
    wm_l.save(os.path.join(dst_path, 'gen-%s-wm-l.png' % prefix))

    wm_rgb = Image.merge('RGB', [band_8, band_8, band_8])
    wm_rgb.save(os.path.join(dst_path, 'gen-%s-wm-rgb.png' % prefix))

    wm_rgba = Image.merge('RGBA', [band_8, band_8, band_8, band_a])
    wm_rgba.save(os.path.join(dst_path, 'gen-%s-wm-rgba.png' % prefix))

    #wm_cmyk = Image.merge('CMYK', [band_8, band_8, band_8, band_8])
    #wm_cmyk.save(os.path.join(dst_path, 'gen-%s-wm-cmyk.jpg' % prefix))

    band_img = Image.new('L', (16, 16))
    band_img.putdata([255]*64 + [0]*64 + [255]*64 + [0]*64)
    img = Image.merge('L', [band_img])
    img.save(os.path.join(dst_path, 'gen-%s-img.png' % prefix))


if __name__ == '__main__':
    exit(main(*sys.argv[1:]))

