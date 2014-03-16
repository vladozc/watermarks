WaterMarker
===========

Library for adding/reading watermarks from images.

**IMPORTANT: this project is in early stage and it might change a lot.**

Installation
============
Library requires Python 2.6/2.7. It uses `pillow` and `nose`. You can install these dependencies with command:

`pip install -r requirements.txt`

However, `pillow` might need some other libraries to work properly. If you meet error message like `IOError: decoder zip not available`, please install following libs:

CentOS:
`yum install freetype freetype-devel libpng libpng-devel libjpeg libjpeg-devel`

Ubuntu:
`apt-get install python-dev python-setuptools`
`apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk`

Then reinstall your `pillow`.

Testing
=======
PYTHONPATH=src:utils nosetests test/functiontests/

