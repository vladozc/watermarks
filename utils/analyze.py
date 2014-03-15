import os
import sys

from PIL import Image


def main():
    verbose = 1 if sys.argv[1] == '-v' else 0
    for i in xrange(1 + verbose, len(sys.argv)):
        analyze(sys.argv[i], verbose)


def analyze(filepath, verbose):
    img = Image.open(filepath)
    print 'Name:\t', os.path.basename(filepath)
    print 'Mode:\t', img.mode
    print 'Bands:\t', img.getbands()
    if verbose:
        img.load()
        for i, band in enumerate(img.split()):
            print 'Band %d:\t' % i, list(band.getdata())


if __name__ == '__main__':
    main()

