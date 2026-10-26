# Lab 03: Blink the First Pixel
# Filename: 03-blink-first-pixel.py
# Version: 1.0.0
#
# Blink the first pixel on the strip orange, on and off. This is the
# smallest program that talks to the LED strip.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

BLINK_DELAY = 0.5        # seconds the pixel stays on or off - change me!

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# pumpkin orange, made dimmer by BRIGHTNESS so it is safe on battery power
orange = (int(255 * BRIGHTNESS), int(80 * BRIGHTNESS), 0)
off = (0, 0, 0)

while True:
    strip[0] = orange     # pixel 0 is the first pixel on the strip
    strip.write()         # send the colors to the strip
    sleep(BLINK_DELAY)
    strip[0] = off
    strip.write()
    sleep(BLINK_DELAY)
