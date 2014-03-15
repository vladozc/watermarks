#!/usr/bin/python
'''
PYTHONPATH=../src ./reader.py -d ../res -m lsb ../data/
'''
import argparse
import logging
import os
import sys

from watermarker.core import setup_logger
from watermarker.core.loader import Loader


logger = logging.getLogger()


def run():
    parser = setup_parser()
    args = parser.parse_args()
    setup_logger()
    logger.debug(args)
    r = Loader('readers')
    try:
        r.run(args)
        return 0
    except ImportError:
        logger.critical('Cannot find method "%s". Please make sure you '
                        'spelled it correctly and check your PYTHONPATH.',
                        args.method)
        return 1


def setup_parser():
    description = 'Utility for reading watermarks from images.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        'sources', metavar='PTH', nargs='+',
        help='List of files/directories that will be processed. Directories '
             'will be listed (but not recursive).'
    )
    parser.add_argument(
        '-m', '--method', required=True,
        help='Watermark method to be applied.'
    )
    parser.add_argument(
        '-d', '--dest-dir', required=True,
        help='Directory where the extracted watermarks will be stored.'
    )
    parser.add_argument(
        '--format', default='png',
        help='Format for generated images.'
    )
    return parser


if __name__ == '__main__':
    exit(run())
