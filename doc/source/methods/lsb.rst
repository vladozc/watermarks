LSB
---

Lsb (least significant bit) is method that extracts least significat
(last) bit from every subpixel and generates image - black pixel for
subpixels ending with 0 (even) and white pixel for subpixels ending
with 1 (odd). For writing LSB watermark into image, Watermarks
modifies least significant bit of every subpixel in image.

For more information use Google :)

Example
^^^^^^^
+---------------------------------+---------------------------------------------+
| original image                  | watermarked image                           |
+=================================+=============================================+
| .. image:: _static/sample.png   | .. image:: _static/sample_watermarked.png   |
+---------------------------------+---------------------------------------------+

Can you see the difference? No? So let's use Waterm`arks to extract last bit and
generate image:

+---------------------------------+---------------------------------------------+
| red band (last bit)             | red band (last bit)                         |
+=================================+=============================================+
| .. image:: _static/sample_R.png | .. image:: _static/sample_watermarked_R.png |
+---------------------------------+---------------------------------------------+

