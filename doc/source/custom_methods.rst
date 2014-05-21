Custom methods
==============

You are allowed to use custom watermark methods. When running from
binary, just pass your custom watermark method via -m argument. (If WM
does not find method in it's built-in methods then it will try to find it
in ``$PYTHONPATH``.)

Module with custom method must have functions ``init(args)``,
``update_parser(parser)`` and method implementation class with
function ``run()``. Please see some existing method (in
``watermarks.core.[readers|writers]``) for example.

