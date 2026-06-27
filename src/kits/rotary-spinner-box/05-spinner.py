# Rotary Spinner Box - Spinner
# Filename: 05-spinner.py
#
# This is the signature pattern of the spinner box: a single bright dot that
# travels around the ring, one pixel at a time, forever.
#
# We use a loop to move the dot.  Each time through the loop we:
#   1. turn ON the current pixel
#   2. wait a short time
#   3. turn OFF the current pixel
#   4. move to the next pixel (wrapping back to 0 at the end)

from neopixel import NeoPixel
import machine
from utime import sleep

import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# The color of the spinning dot
DOT_COLOR = (0, 60, 80)

# How long the dot stays on each pixel, in seconds
DELAY = 0.06

# Start the dot at pixel 0
position = 0

print('Spinner running. Watch the dot travel around the ring.')

while True:
    # turn ON the current pixel
    strip[position] = DOT_COLOR
    strip.write()
    sleep(DELAY)

    # turn OFF the current pixel
    strip[position] = (0, 0, 0)
    strip.write()

    # move to the next pixel, wrapping back to 0 at the end
    position = (position + 1) % config.NUMBER_PIXELS
