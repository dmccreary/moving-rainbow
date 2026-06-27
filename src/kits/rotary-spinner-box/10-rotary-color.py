# Rotary Spinner Box - Rotary Color
# Filename: 10-rotary-color.py
#
# This time the knob controls a different parameter: COLOR.  Spinning the knob
# moves a position around the color wheel, so the whole ring slowly changes
# from red to orange to yellow to green to blue to purple and back.
#
# Same pattern as the brightness lab, but the parameter is a color-wheel
# position (0-255) instead of a brightness.

from neopixel import NeoPixel
import machine
from utime import sleep

import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# Encoder pins
clk = machine.Pin(config.ROTARY_ENCODER_PIN_A, machine.Pin.IN, machine.Pin.PULL_UP)
dt = machine.Pin(config.ROTARY_ENCODER_PIN_B, machine.Pin.IN, machine.Pin.PULL_UP)
last_clk = clk.value()


# The color wheel: position 0-255 in, an (r,g,b) color out
def color_wheel(pos):
    pos = pos % 256
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)


# The color parameter: a position on the color wheel (0-255)
hue = 0

# How many wheel steps each click of the knob moves
STEP = 8


# Fill the whole ring with the current color
def show_color():
    color = color_wheel(hue)
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()


print('Rotary Color ready. Spin the knob to change the color.')
show_color()

while True:
    current_clk = clk.value()
    if current_clk != last_clk and current_clk == 0:
        if dt.value() != current_clk:
            hue = (hue + STEP) % 256   # clockwise
        else:
            hue = (hue - STEP) % 256   # counterclockwise
        print('hue:', hue)
        show_color()
    last_clk = current_clk
