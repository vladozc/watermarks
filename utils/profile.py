'''Generate profile statistics.

Something similar can be done with commands:
PYTHONPATH=src python -m cProfile -o reader_lsb.profile bin/reader.py -m lsb -d tmp/ test/data/shape1-rgb-l9.png
PYTHONPATH=src python -m cProfile -o writer_lsb.profile bin/writer.py -m lsb -d tmp/ -w test/data/shape1-rgb-l9.png test/data/shape1-rgb-l9.png

However, the runner overheat is very high for small pictures.

Command to generate image from the profile result:
python ~/bin/gprof2dot.py -f pstats reader_lsb.profile | dot -Tpng -o output.png
(you need to download gprof2dot.py first - http://gprof2dot.jrfonseca.googlecode.com/git/gprof2dot.py)
'''
import cProfile
import logging
import os

from watermarks.core import setup_logger
import watermarks.core.readers.lsb
import watermarks.core.writers.lsb


logger = logging.getLogger()


def profile_all():
    setup_logger()
    profile_reader_lsb()
    profile_writer_lsb()


def profile_reader_lsb():
    profiler = cProfile.Profile()
    try:
        return profiler.runcall(run_reader_lsb)
    finally:
        profiler.dump_stats('reader_lsb.profile')


def profile_writer_lsb():
    profiler = cProfile.Profile()
    try:
        return profiler.runcall(run_writer_lsb)
    finally:
        profiler.dump_stats('writer_lsb.profile')


def run_reader_lsb():
    filepath = os.path.join(os.path.dirname(__file__), '..', 'test', 'data', 'shape1-rgb-l9.png')
    dest_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')
    reader = watermarks.core.readers.lsb.Lsb([filepath], dest_dir, 'png')
    reader.run()


def run_writer_lsb():
    filepath = os.path.join(os.path.dirname(__file__), '..', 'test', 'data', 'shape1-rgb-l9.png')
    wm_filepath = os.path.join(os.path.dirname(__file__), '..', 'test', 'data', 'shape1-rgb-l9.png')
    dest_dir = os.path.join(os.path.dirname(__file__), '..', 'tmp')
    writer = watermarks.core.writers.lsb.Lsb([filepath], dest_dir, 'png', wm_filepath)
    writer.run()


if __name__ == '__main__':
    profile_all()

