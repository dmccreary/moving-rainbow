# Lab 08: Candy Corn
# Filename: 08-candy-corn.py
# Version: 1.0.0
# Not yet tested on hardware.
#
# Stripes of yellow, orange and white, like a piece of candy corn, slide
# along the strip. The % (modulo) operator repeats the stripes forever.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

DELAY = 0.08             # seconds between steps - smaller is faster
STRIPE_WIDTH = 4         # how many pixels wide each stripe is

yellow = (255, 180, 0)
orange = (255, 60, 0)
white = (180, 180, 180)
stripes = [yellow, orange, white]

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the strip is safe on battery power
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

offset = 0
while True:
    for i in range(NUMBER_PIXELS):
        # which stripe is pixel i in? divide by the width, then wrap with %
        stripe = ((i + offset) // STRIPE_WIDTH) % len(stripes)
        strip[i] = fade(stripes[stripe], 1)
    strip.write()
    sleep(DELAY)
    offset += 1          # move every stripe one pixel for the next step
