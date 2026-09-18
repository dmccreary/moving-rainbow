# Lab 24: Fading Stars
# Filename: 24-fading-stars.py
# Version: 1.0.0
#
# Stars flare up at random places and then fade away smoothly. A list keeps
# one brightness number for every pixel.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

STAR_CHANCE = 20        # percent chance that a new star appears each frame
STAR_BRIGHTNESS = 120   # how bright a new star starts out (0 to 255)
FRAME_DELAY = 0.05      # seconds per frame

# one brightness number for each pixel, and 0 means dark
brightness = [0] * NUMBER_PIXELS

while True:
    # sometimes start a new star at a random pixel
    if randint(1, 100) <= STAR_CHANCE:
        brightness[randint(0, NUMBER_PIXELS - 1)] = STAR_BRIGHTNESS

    # show every pixel, then fade its brightness a little
    for i in range(NUMBER_PIXELS):
        level = brightness[i]
        strip[i] = (level, level, level)
        brightness[i] = level * 3 // 4   # keep three quarters of the brightness
    strip.write()
    sleep(FRAME_DELAY)
