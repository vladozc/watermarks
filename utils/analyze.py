import os
import sys

from PIL import Image


def main():
    verbose = 1 if sys.argv[1] == '-v' else 0
    for i in range(1 + verbose, len(sys.argv)):
        analyze(sys.argv[i], verbose)
    return 0


def analyze(filepath, verbose):
    img = Image.open(filepath)
    print ('Name:\t{0}'.format(os.path.basename(filepath)))
    print ('Mode:\t{0}'.format(img.mode))
    print ('Size:\t{0}'.format(img.size))
    print ('Bands:\t{0}'.format(img.getbands()))
    if verbose:
        img.load()
        width = img.size[0]
        for band_name, band in zip(img.getbands(), img.split()):
            band_data = list(band.getdata())
            print('\nBand {0}:'.format(band_name))
            start_index = 0
            while start_index < len(band_data):
                end_index = start_index + width
                part = str(band_data[start_index:end_index])
                print('{0},'.format(part.strip('[').strip(']')))
                start_index = end_index


if __name__ == '__main__':
    exit(main())

