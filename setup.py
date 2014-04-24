from distutils.core import setup
from setuptools import find_packages


setup(
    name='watermarks',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    version='0.1',
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
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics",
        ],
    install_requires=[
        'Pillow==2.3.0',
        'six==1.6.1',
    ],
)
