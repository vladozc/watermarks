'''
python ~/bin/gprof2dot.py -f pstats reader_lsb.profile | dot -Tpng -o output.png
'''
import cProfile
import logging
import os

from watermarker.core import setup_logger
import watermarker.core.readers.lsb
import watermarker.core.writers.lsb


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
    dest_dir = os.path.join(os.path.dirname(__file__), '..', 'test', 'tmp')
    reader = watermarker.core.readers.lsb.Lsb([filepath], dest_dir, 'png')
    reader.run()


def run_writer_lsb():
    filepath = os.path.join(os.path.dirname(__file__), '..', 'test', 'data', 'shape1-rgb-l9.png')
    wm_filepath = os.path.join(os.path.dirname(__file__), '..', 'test', 'data', 'shape1-rgb-l9.png')
    dest_dir = os.path.join(os.path.dirname(__file__), '..', 'test', 'tmp')
    writer = watermarker.core.writers.lsb.Lsb([filepath], dest_dir, 'png', wm_filepath)
    writer.run()


if __name__ == '__main__':
    profile_all()

