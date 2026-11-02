# Lab 13: Breathing Halo
# Filename: 13-breathing-halo.py
# Version: 1.0.0
#
# The whole ring glows and fades like slow breathing. The color changes
# while the ring is at its darkest, so you never see it jump.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.02             # seconds between steps - smaller is faster breathing
HALF_BREATH = 100        # steps from brightest to darkest

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
orange = (255, 60, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
violet = (138, 43, 226)
colors = (red, orange, green, cyan, blue, violet)
color_count = len(colors)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

step = 0
color_index = 0
while True:
    # level counts 1.0 down to 0.0 and back up to 1.0
    level = abs(step - HALF_BREATH) / HALF_BREATH
    # squaring the level makes the fade look smoother to our eyes
    strip.fill(fade(colors[color_index], 0.02 + 0.98 * level * level))
    strip.write()
    sleep(DELAY)
    step = (step + 1) % (HALF_BREATH * 2)
    if step == HALF_BREATH:
        # we are at the darkest point, so it is safe to change color
        color_index = (color_index + 1) % color_count
