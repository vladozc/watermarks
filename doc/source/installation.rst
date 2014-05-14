Installation
============

pip
---

Just type command::

  pip install watermarks

From source code
----------------

Download/clone repository from `GitHub <https://github.com/vladozc/watermarks>`_.

Library requires Python 2.6/2.7/3.x. It uses some third party libs. You can install them with command::

  pip install -r requirements.txt

You can test Watermarks by calling selftest() function::

  >>> from watermarks.selftest import selftest
  >>> selftest()
  True

However, the ``pillow`` dependency might need some other libraries to work properly. If you meet error message like ``IOError: decoder zip not available``, please install following libs::

  CentOS:
      yum install freetype freetype-devel libpng libpng-devel libjpeg libjpeg-devel

  Ubuntu:
      apt-get install python-dev
    or:
      apt-get install python-dev3

    and:
      apt-get install python-setuptools libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk

Then reinstall the ``pillow`` dependency::

  pip uninstall pillow
  pip install -r requirements.txt

If it is still not running, please visit `pillow's documentation <http://pillow.readthedocs.org/en/latest/installation.html>`_ for more installation help.
