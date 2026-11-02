# Lab 07: Two Comets
# Filename: 07-two-comets.py
# Version: 1.0.0
#
# Two comets chase each other, always on opposite sides of the ring.
# Adding half the ring to a position gives the spot directly across from it.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.05             # seconds between steps - smaller is faster
TAIL_LENGTH = 8          # how many pixels long each comet is

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

blue = (0, 0, 255)
orange = (255, 60, 0)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

HALF = NUMBER_PIXELS // 2

position = 0
while True:
    strip.fill((0, 0, 0))
    for t in range(TAIL_LENGTH):
        amount = (1 - t / TAIL_LENGTH) ** 2
        strip[(position - t) % NUMBER_PIXELS] = fade(blue, amount)
        strip[(position + HALF - t) % NUMBER_PIXELS] = fade(orange, amount)
    strip.write()
    sleep(DELAY)
    position = (position + 1) % NUMBER_PIXELS
