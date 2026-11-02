# Lab 14: Sine Wave
# Filename: 14-sine-wave.py
# Version: 1.0.0
#
# Waves of light roll around the ring. A sine wave repeats every full
# circle, and a ring IS a full circle, so the wave joins up with itself
# perfectly. Change CRESTS to 1, 3 or 4 to fit more or fewer waves.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from math import sin, pi
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.03             # seconds between steps - smaller is faster
CRESTS = 2               # how many bright waves fit around the ring - a whole number
SPEED = 0.15             # how far the waves move each step

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

FULL_CIRCLE = 2 * pi     # a full circle in radians

phase = 0
hue = 0
while True:
    color = wheel(hue)
    for i in range(NUMBER_PIXELS):
        angle = FULL_CIRCLE * CRESTS * i / NUMBER_PIXELS
        # sin() gives -1 to 1, so this changes it to 0 to 1
        wave = (sin(angle - phase) + 1) / 2
        strip[i] = fade(color, wave * wave)
    strip.write()
    sleep(DELAY)
    phase = (phase + SPEED) % FULL_CIRCLE
    hue = (hue + 1) % 256
