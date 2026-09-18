# Lab 27: Sunrise
# Filename: 27-sunrise.py
# Version: 1.0.0
#
# The whole strip glows like the sky. The colors blend from night to dawn to
# sunrise to day. After a pause the sun sets and the colors blend backward.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

night = (0, 0, 8)
dawn = (30, 0, 30)
sunrise = (80, 20, 0)
day = (80, 60, 20)
sky_colors = [night, dawn, sunrise, day]

STEPS = 60          # how many small steps to blend from one color to the next
STEP_DELAY = 0.1    # seconds per step

def blend(color1, color2, fraction):
    # fraction 0.0 gives color1, 1.0 gives color2, and 0.5 is halfway between
    red = int(color1[0] + (color2[0] - color1[0]) * fraction)
    green = int(color1[1] + (color2[1] - color1[1]) * fraction)
    blue = int(color1[2] + (color2[2] - color1[2]) * fraction)
    return (red, green, blue)

def fade(color1, color2):
    for step in range(STEPS + 1):
        color = blend(color1, color2, step / STEPS)
        for i in range(NUMBER_PIXELS):
            strip[i] = color
        strip.write()
        sleep(STEP_DELAY)

while True:
    # sunrise: blend through the colors in order
    for i in range(len(sky_colors) - 1):
        fade(sky_colors[i], sky_colors[i + 1])
    sleep(3)

    # sunset: blend back through the colors in reverse order
    for i in range(len(sky_colors) - 1, 0, -1):
        fade(sky_colors[i], sky_colors[i - 1])
    sleep(3)
