# Lab 07: Pumpkin Glow
# Filename: 07-pumpkin-glow.py
# Version: 1.0.0
# Not yet tested on hardware.
#
# The whole strip glows orange and slowly gets brighter and dimmer, like
# a jack-o'-lantern breathing in the dark.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

DELAY = 0.02             # seconds between steps - smaller is a faster glow
LOWEST = 10              # the dimmest step (out of 100) so the pumpkin never goes dark

orange = (255, 80, 0)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the strip is safe on battery power
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

while True:
    # get brighter: count up from LOWEST to 100
    for level in range(LOWEST, 101, 2):
        strip.fill(fade(orange, level / 100))
        strip.write()
        sleep(DELAY)
    # get dimmer: count back down from 100 to LOWEST
    for level in range(100, LOWEST - 1, -2):
        strip.fill(fade(orange, level / 100))
        strip.write()
        sleep(DELAY)
