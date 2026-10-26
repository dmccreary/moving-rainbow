# Lab 09: Spooky Sparkle
# Filename: 09-spooky-sparkle.py
# Version: 1.0.0
# Not yet tested on hardware.
#
# Random pixels flash orange or purple and then slowly fade away, like
# sparks from a witch's wand.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
from urandom import randint

DELAY = 0.04             # seconds between steps
NEW_SPARKS = 2           # how many new sparks appear each step
FADE_SPEED = 0.85        # each step a pixel keeps 85% of its color

orange = (255, 80, 0)
purple = (140, 0, 255)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the strip is safe on battery power
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

while True:
    # step 1: fade every pixel a little
    for i in range(NUMBER_PIXELS):
        r, g, b = strip[i]
        strip[i] = (int(r * FADE_SPEED), int(g * FADE_SPEED), int(b * FADE_SPEED))
    # step 2: light a few new sparks in random places
    for n in range(NEW_SPARKS):
        place = randint(0, NUMBER_PIXELS - 1)
        if randint(0, 1) == 0:      # flip a coin to pick the color
            strip[place] = fade(orange, 1)
        else:
            strip[place] = fade(purple, 1)
    strip.write()
    sleep(DELAY)
