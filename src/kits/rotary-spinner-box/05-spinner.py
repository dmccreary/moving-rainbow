# Rotary Spinner Box - Scanner
# Filename: 05-spinner.py
#
# This is the signature moving pattern of the box: a single bright dot that
# travels back and forth along the 12-pixel strip, like the scanner light on
# a robot.
#
# Because this is a straight strip (not a ring), the dot cannot wrap around
# from the last pixel to the first without "jumping".  Instead, when the dot
# reaches an end of the strip it turns around and heads back the other way.
#
# We track two things:
#   position  - which pixel the dot is on
#   direction - +1 means moving toward the end, -1 means moving back

from neopixel import NeoPixel
import machine
from utime import sleep

import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# The color of the moving dot
DOT_COLOR = (0, 60, 80)

# How long the dot stays on each pixel, in seconds
DELAY = 0.06

# Start the dot at pixel 0, moving toward the far end
position = 0
direction = 1

print('Scanner running. Watch the dot travel back and forth along the strip.')

while True:
    # turn every pixel off, then light only the current one
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip[position] = DOT_COLOR
    strip.write()
    sleep(DELAY)

    # if we are at either end, turn around
    if position == 0:
        direction = 1
    elif position == config.NUMBER_PIXELS - 1:
        direction = -1

    # take one step in the current direction
    position = position + direction
