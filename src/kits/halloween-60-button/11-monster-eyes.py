# Lab 11: Monster Eyes
# Filename: 11-monster-eyes.py
# Version: 1.0.0
# Not yet tested on hardware.
#
# Pairs of glowing eyes hide along the strip. Each pair blinks at its own
# random time, so it looks like monsters are watching you from the dark.
# A list remembers when each pair should blink next.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
from utime import ticks_ms, ticks_diff
from urandom import randint

DELAY = 0.02             # seconds between steps
EYE_SPACING = 10         # pixels from one pair of eyes to the next
BLINK_TIME = 150         # milliseconds the eyes stay shut

eye_colors = [(255, 0, 0), (0, 255, 0), (255, 80, 0), (140, 0, 255)]

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the strip is safe on battery power
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# make one pair of eyes every EYE_SPACING pixels
eyes = []                # each pair is a list: [first pixel, color, next blink time]
for start in range(2, NUMBER_PIXELS - 1, EYE_SPACING):
    color = eye_colors[randint(0, len(eye_colors) - 1)]
    eyes.append([start, color, ticks_ms() + randint(500, 4000)])

while True:
    now = ticks_ms()
    strip.fill((0, 0, 0))
    for pair in eyes:
        start, color, blink_at = pair
        time_left = ticks_diff(blink_at, now)
        if time_left > 0:
            # not time to blink yet: eyes open
            strip[start] = fade(color, 1)
            strip[start + 1] = fade(color, 1)
        elif time_left < -BLINK_TIME:
            # the blink is over: pick a new random time for the next blink
            pair[2] = now + randint(1000, 5000)
        # otherwise the eyes are shut, so we leave them dark
    strip.write()
    sleep(DELAY)
