# Lab 06: Comet
# Filename: 06-comet.py
# Version: 1.0.0
#
# A bright head with a fading tail circles the ring, and the comet changes
# color after every lap. The tail wraps across pixel 0 with no break.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.04             # seconds between steps - smaller is faster
TAIL_LENGTH = 10         # how many pixels long the comet is

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
orange = (255, 60, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
violet = (138, 43, 226)
colors = (red, orange, yellow, green, cyan, blue, violet)
color_count = len(colors)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

position = 0
color_index = 0
while True:
    strip.fill((0, 0, 0))    # start each step with a dark ring in memory
    for t in range(TAIL_LENGTH):
        # squaring the amount makes the tail fade away faster
        amount = (1 - t / TAIL_LENGTH) ** 2
        # the tail is behind the head, and % wraps it across pixel 0
        strip[(position - t) % NUMBER_PIXELS] = fade(colors[color_index], amount)
    strip.write()            # one write per step
    sleep(DELAY)
    position = (position + 1) % NUMBER_PIXELS
    if position == 0:
        # one full lap is done, so use the next color
        color_index = (color_index + 1) % color_count
