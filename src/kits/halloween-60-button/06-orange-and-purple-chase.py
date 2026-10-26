# Lab 06: Orange and Purple Chase
# Filename: 06-orange-and-purple-chase.py
# Version: 1.0.0
#
# An orange comet runs down the strip while a purple comet runs back up.
# Each comet has a tail that fades out behind it, and they pass right
# through each other in the middle.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.03             # seconds between steps - smaller is faster
TAIL_LENGTH = 6          # how many pixels long each comet is

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

orange = (255, 80, 0)
purple = (140, 0, 255)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the strip is safe on battery power
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# add two colors together where comets overlap, keeping each part at 255 or less
def mix(color1, color2):
    return (min(color1[0] + color2[0], 255),
            min(color1[1] + color2[1], 255),
            min(color1[2] + color2[2], 255))

position = 0
while True:
    strip.fill((0, 0, 0))    # start each step with a dark strip in memory
    for t in range(TAIL_LENGTH):
        amount = 1 - t / TAIL_LENGTH     # the head is brightest, the tail fades out
        # the orange comet moves forward, so its tail is behind it (lower numbers)
        orange_index = (position - t) % NUMBER_PIXELS
        # the purple comet moves backward, so its tail is above it (higher numbers)
        purple_index = (NUMBER_PIXELS - 1 - position + t) % NUMBER_PIXELS
        strip[orange_index] = mix(strip[orange_index], fade(orange, amount))
        strip[purple_index] = mix(strip[purple_index], fade(purple, amount))
    strip.write()            # one write per step
    sleep(DELAY)
    # % wraps the position back to 0 at the end of the strip
    position = (position + 1) % NUMBER_PIXELS
