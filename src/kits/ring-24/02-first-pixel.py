# Lab 02: First Pixel
# Filename: 02-first-pixel.py
# Version: 1.0.0
#
# Pixel 0 blinks red and pixel 1 stays green. A ring has no first end you
# can point to, so this shows where the numbers start and which way they
# go around.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.5              # seconds between blinks - change me!

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
green = (0, 255, 0)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

strip[1] = fade(green, 1)
pixel_on = True
while True:
    if pixel_on:
        strip[0] = fade(red, 1)
    else:
        strip[0] = (0, 0, 0)
    strip.write()
    sleep(DELAY)
    pixel_on = not pixel_on
