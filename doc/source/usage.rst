Usage
=====

There are few different ways to run Watermarks:

- executables ``wm_reader`` and ``wm_writer``
- using ``watermarks.core.loader.Loader`` to load and run method
- using method's init function, e.g. ``watermarks.core.writers.lsb.init``
- make method instance (e.g. ``watermarks.core.writers.lsb.Lsb``) by yourself

Examples
--------

Executable::

  (e) $ wm_reader lsb -d tmp test/data/shape1-rgb-l0.png

Loader::

  from watermarks.core.loader import Loader
  r = Loader('readers')
  r.run(args)

Init::

  from watermarks.core.readers.lsb import init
  lsb = init(args)
  lsb.run(['test/data/shape1-rgb-l0.png'])

Directly::

  from watermarks.core.readers.lsb import Lsb
  lsb = Lsb(destination='tmp', format='png')
  lsb.run(['test/data/shape1-rgb-l0.png'])

