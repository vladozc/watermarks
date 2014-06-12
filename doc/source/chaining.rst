Methods chaining
================

There is possibility to read/write multiple watermarks in one go. To do so, pass more methods separated with comma. In `wm_writer` you must also pass appropriate number of watermarks. Example::

  wm_writer lsb,visible -w test/data/gen-wmode-wm-rgb.png -w test/data/gen-wmode-wm-l.png -d tmp test/data/shape1-rgb-l0.png

Methods will be applied in order they were specified.
