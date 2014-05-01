Running tests
=============

\.. is as easy as::

  $ PYTHONPATH=utils tox

or::

  $ PYTHONPATH=src:utils nosetests --with-coverage --cover-erase --cover-package=watermarks.core test/functiontests/

