# Rotary Spinner Box - Moving Rainbow
# Filename: 08-moving-rainbow.py
#
# This program takes the rainbow from lab 07 and makes it spin around the ring.
# The trick is a number called "offset" that grows a little each step.  Adding
# the offset to every pixel's wheel position slides the whole rainbow forward.

from neopixel import NeoPixel
import machine
from utime import sleep

import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)


# The color wheel: position 0-255 in, an (r,g,b) color out
def color_wheel(pos):
    pos = pos % 256
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)


# How long to wait between steps, in seconds
DELAY = 0.03

# This grows each step to make the rainbow move
offset = 0

print('Moving Rainbow running. The rainbow spins around the ring.')

while True:
    for i in range(config.NUMBER_PIXELS):
        # spread the rainbow around the ring, then shift it by the offset
        position = int(i * 256 / config.NUMBER_PIXELS) + offset
        strip[i] = color_wheel(position)
    strip.write()
    sleep(DELAY)

    # grow the offset so the rainbow moves next time (wrap at 255)
    offset = (offset + 2) % 256
