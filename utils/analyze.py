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
        for band_name, band in zip(img.getbands(), img.split()):
            print ('Band {0}:\t{1}'.format(band_name, list(band.getdata())))


if __name__ == '__main__':
    exit(main())

