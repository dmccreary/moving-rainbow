# Rotary Spinner Box - Rainbow
# Filename: 07-rainbow.py
#
# This program spreads a full rainbow across the 12 pixels of the strip and
# holds it still.  It introduces the color wheel: a helper that turns a single
# number (0-255) into a color somewhere in the rainbow.
#
# By giving each pixel an evenly spaced spot on the color wheel, the whole
# strip shows one smooth rainbow from end to end.

from neopixel import NeoPixel
import machine
from utime import sleep

import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)


# The color wheel: give it a position from 0 to 255 and it returns an (r,g,b)
# color.  As the position grows, the color moves through red, green, and blue
# and back to red.
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


print('Rainbow displayed. The strip shows one full rainbow.')

# Set each pixel to an evenly spaced color around the wheel, just once
for i in range(config.NUMBER_PIXELS):
    position = int(i * 256 / config.NUMBER_PIXELS)
    strip[i] = color_wheel(position)
strip.write()

# Nothing changes after this, so the main loop just waits
while True:
    sleep(1)
