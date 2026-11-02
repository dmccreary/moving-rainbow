# Lab 09: Color Wheel
# Filename: 09-color-wheel.py
# Version: 1.0.0
#
# Paints a real color wheel on the ring. The color of each pixel depends
# only on its angle around the circle, so red meets red again at the top
# with no seam. The program draws the wheel once and then stops.

from machine import Pin
from neopixel import NeoPixel
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS
TOP_PIXEL = config.TOP_PIXEL

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# turn a position counted clockwise from the top into a pixel number
def pixel_at(position):
    return (TOP_PIXEL + position) % NUMBER_PIXELS

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

for position in range(NUMBER_PIXELS):
    # 360 degrees / 24 pixels = 15 degrees between neighbors
    angle = position * 360 // NUMBER_PIXELS
    color = wheel(position * 256 // NUMBER_PIXELS)
    print('position', position, 'angle', angle, 'color', color)
    strip[pixel_at(position)] = fade(color, 1)
strip.write()
