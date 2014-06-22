import argparse
import logging
import sys


class WMParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


def get_log_level(args):
    if args.verbose:
        ll = logging.DEBUG
    elif args.quiet:
        ll = logging.ERROR
    else:
        ll = None
    return ll


def add_vq_args(parser):
    parser.add_argument(
        '-q', '--quiet', action='store_true', help='Be quiet.'
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true', help='Be verbose.'
    )


def add_common_args(parser):
    parser.add_argument(
        'sources', metavar='PTH', nargs='+',
        help='List of files/directories that will be processed. Directories '
             'will be listed (but not recursive).'
    )
    parser.add_argument(
        '-d', '--dest-dir', required=True,
        help='Directory where the extracted watermarks will be stored.'
    )
    parser.add_argument(
        '--format', default='png',
        help='Format of generated images.'
    )
    parser.add_argument(
        '-s', '--suffix', default='',
        help='Suffix of watermarked files (default: %(default)s).'
    )
