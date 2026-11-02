# Lab 05: Spin a Dot
# Filename: 05-spin-dot.py
# Version: 1.0.0
#
# A single red dot goes around and around the ring. On a straight strip
# a moving dot has to stop at the end. On a ring, the % (modulo) operator
# sends pixel 23 straight on to pixel 0, so the dot never stops.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.06             # seconds between steps - smaller is faster

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

position = 0
while True:
    strip[position] = fade(red, 1)
    strip.write()
    sleep(DELAY)
    strip[position] = (0, 0, 0)   # erase in memory - the next write shows it
    position = (position + 1) % NUMBER_PIXELS
