# Lab 12: Rainbow Cycle
# Filename: 12-rainbow-cycle.py
# Version: 1.0.0
#
# The rainbow rotates around the strip.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
# we have each pixel step through the color wheel
color_wheel_step = int(256 / NUMBER_PIXELS)

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

current_color = 0
offset = 0
print('Drawing rainbow in', NUMBER_PIXELS, 'steps with step size of: ', color_wheel_step)
while True:
    for i in range(0,NUMBER_PIXELS):
        strip[(i+offset) % NUMBER_PIXELS] = wheel(current_color)
        current_color = current_color + color_wheel_step
        strip.write()
        sleep(.001)
    current_color = 0
    offset += 1
