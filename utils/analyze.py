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
    print 'Name:\t', os.path.basename(filepath)
    print 'Mode:\t', img.mode
    print 'Size:\t', img.size
    print 'Bands:\t', img.getbands()
    if verbose:
        img.load()
        for band_name, band in zip(img.getbands(), img.split()):
            print 'Band %s:\t' % band_name, list(band.getdata())


if __name__ == '__main__':
    exit(main())

