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
    version=watermarks.__version__,
    description='Library for adding/reading watermarks from images.',
    author='Vladimir Chovanec',
    author_email='vladimir.chovanec.zc@gmail.com',
    keywords=['watermark', 'watermarks', 'watermarker', 'watermarking', 'lsb'],
    url='https://pypi.python.org/pypi/watermarks/',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GPL",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Image Processing",
        ],
)
