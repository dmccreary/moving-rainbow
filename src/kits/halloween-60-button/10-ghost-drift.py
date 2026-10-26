# Lab 10: Ghost Drift
# Filename: 10-ghost-drift.py
# Version: 1.0.0
# Not yet tested on hardware.
#
# A pale ghost with a fading tail floats slowly down the strip, turns
# around at the end and floats back. A direction variable of 1 or -1
# tells the ghost which way to go.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

DELAY = 0.06             # seconds between steps - ghosts are slow
TAIL_LENGTH = 8          # how long the ghost's tail is

ghost = (160, 170, 255)  # a cold, pale blue-white

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the strip is safe on battery power
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

position = 0
direction = 1            # 1 means down the strip, -1 means back up
while True:
    strip.fill((0, 0, 0))
    for t in range(TAIL_LENGTH):
        # the tail trails behind, so it is on the other side of the direction
        index = position - t * direction
        if 0 <= index < NUMBER_PIXELS:
            amount = (1 - t / TAIL_LENGTH) ** 2   # squaring makes the tail fade faster
            strip[index] = fade(ghost, amount)
    strip.write()
    sleep(DELAY)
    position += direction
    # turn around when the ghost reaches either end
    if position == NUMBER_PIXELS - 1 or position == 0:
        direction = -direction
