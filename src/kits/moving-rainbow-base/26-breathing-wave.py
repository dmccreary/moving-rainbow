# Lab 26: Breathing Wave
# Filename: 26-breathing-wave.py
# Version: 1.0.0
#
# A wave of blue light rolls along the strip. Every pixel breathes in and
# out smoothly, using a sine wave. Each pixel is a little behind its
# neighbor, which makes the wave travel.

import math
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

MAX_BRIGHTNESS = 60   # the brightest a pixel gets
WAVE_SPEED = 0.06     # how far the wave moves each frame
WAVE_SPACING = 0.3    # how far behind each pixel is its neighbor (0 = all breathe together)
FRAME_DELAY = 0.03    # seconds per frame

phase = 0
while True:
    for i in range(NUMBER_PIXELS):
        # sin() gives a number from -1 to 1. Add 1 and divide by 2 to get 0 to 1.
        wave = (math.sin(phase + i * WAVE_SPACING) + 1) / 2
        level = int(wave * MAX_BRIGHTNESS)
        strip[i] = (0, level // 2, level)
    strip.write()
    # move the wave forward, and start over after one full circle (2 x pi)
    phase = (phase + WAVE_SPEED) % (2 * math.pi)
    sleep(FRAME_DELAY)
