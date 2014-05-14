from distutils.core import setup
from setuptools import find_packages

import os
import sys
src_dir = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_dir)
import watermarks


setup(
    name='watermarks',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    scripts=['bin/wm_reader', 'bin/wm_writer'],
    version=watermarks.__version__,
    description='Library for adding/reading watermarks from images. Currently visible and LSB watermark methods are supported.',
    author='Vladimir Chovanec',
    author_email='vladimir.chovanec.zc@gmail.com',
    maintainer_email='watermarks.py@gmail.com',
    keywords=['watermark', 'watermarks', 'watermarker', 'watermarking', 'lsb'],
    url='https://github.com/vladozc/watermarks',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics",
        ],
    install_requires=[
        'Pillow==2.3.0',
        'six==1.6.1',
        'argparse==1.2.1',
    ],
)
