# 08-color-wheel
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
# get the configuration information
import config

np = config.NUMBER_PIXELS
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), np)
color_wheel_step = int(256 / np)

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
for i in range(0,np):
    strip[i] = wheel(current_color)
    current_color = current_color + color_wheel_step
    strip.write()
    sleep(.03)
