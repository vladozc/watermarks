Usage
=====

There are few different ways to run WaterMarker:

- executable binary from ``bin`` folder
- using ``watermarker.core.loader.Loader`` to load and run method
- using method's init function, e.g. ``watermarker.core.writers.lsb.init``
- make method instance (e.g. ``watermarker.core.writers.lsb.Lsb``) by yourself

Examples
--------

Binary::

  $ PYTHONPATH=src python bin/reader.py -m lsb -d tmp test/data/shape1-rgb-l0.png

Loader::

  from watermarker.core.loader import Loader
  r = Loader('readers')
  r.run(args)

Init::

  from watermarker.core.readers.lsb import init
  lsb = init(args)
  lsb.run()

Directly::

  from watermarker.core.readers.lsb import Lsb
  lsb = Lsb(paths=['test/data/shape1-rgb-l0.png'], destination='tmp', format='png')
  lsb.run()

