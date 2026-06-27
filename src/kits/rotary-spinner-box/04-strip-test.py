# Rotary Spinner Box - LED Strip Test
# Filename: 04-strip-test.py
#
# This program checks that all 12 NeoPixels work and are in the right order.
# It lights every pixel red, then green, then blue, then white, then turns
# them all off.  Watch the ring to make sure no pixels are dark or stuck.
#
#   NEOPIXEL strip is on GPIO pin 0 (config.NEOPIXEL_PIN)
#   The ring has 12 pixels      (config.NUMBER_PIXELS)

from neopixel import NeoPixel
import machine
from utime import sleep

import config

# Create the strip object
strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)


# Helper: set every pixel to the same color and show it
def fill(color):
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()


print('LED Strip Test ready. Watch all', config.NUMBER_PIXELS, 'pixels.')

while True:
    print('Red')
    fill((50, 0, 0))
    sleep(1)

    print('Green')
    fill((0, 50, 0))
    sleep(1)

    print('Blue')
    fill((0, 0, 50))
    sleep(1)

    print('White')
    fill((50, 50, 50))
    sleep(1)

    print('Off')
    fill((0, 0, 0))
    sleep(1)
