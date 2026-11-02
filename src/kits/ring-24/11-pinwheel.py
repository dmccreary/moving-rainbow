# Lab 11: Pinwheel
# Filename: 11-pinwheel.py
# Version: 1.0.0
#
# Colored blades spin like a pinwheel, and the number of blades changes
# every few seconds. A blade and the gap after it must fit evenly around
# the ring. 24 divides evenly by 2 x 2, 2 x 3, 2 x 4, 2 x 6 and 2 x 12,
# so all of these blade counts work.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.09             # seconds between steps - smaller is faster
STEPS_PER_COUNT = 60     # steps before the number of blades changes

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
blade_colors = (red, yellow, green, blue)
blade_counts = (2, 3, 4, 6, 12)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

step = 0
while True:
    blades = blade_counts[(step // STEPS_PER_COUNT) % len(blade_counts)]
    # each blade and each gap has the same width
    width = NUMBER_PIXELS // (blades * 2)
    for i in range(NUMBER_PIXELS):
        section = ((i + step) // width) % (blades * 2)
        if section % 2 == 0:
            # even sections are blades, odd sections are gaps
            strip[i] = fade(blade_colors[(section // 2) % len(blade_colors)], 1)
        else:
            strip[i] = (0, 0, 0)
    strip.write()
    sleep(DELAY)
    step += 1
