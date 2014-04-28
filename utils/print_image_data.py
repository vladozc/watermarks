import os
import sys

from PIL import Image


def print_image_data(filepath):
    img = Image.open(filepath)
    img.load()
    bands = img.split()
    for band in bands:
        print(list(band.getdata()))


def main():
    for filepath in sys.argv[1:]:
        print_image_data(filepath)
    return 0


if __name__ == '__main__':
    exit(main())
