# Rotary Spinner Box - Rotary Brightness
# Filename: 09-rotary-brightness.py
#
# Now the knob does something useful: it controls a PARAMETER.  Here the
# parameter is brightness.  Spin clockwise to make the ring brighter, spin
# counterclockwise to make it dimmer.
#
# This is the key idea for the rest of the labs: a value we store in a variable
# (the parameter) changes what the LEDs do, and an input device (the knob)
# changes the parameter.

from neopixel import NeoPixel
import machine
from utime import sleep

import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# Encoder pins
clk = machine.Pin(config.ROTARY_ENCODER_PIN_A, machine.Pin.IN, machine.Pin.PULL_UP)
dt = machine.Pin(config.ROTARY_ENCODER_PIN_B, machine.Pin.IN, machine.Pin.PULL_UP)
last_clk = clk.value()

# The base color of the ring before brightness is applied
BASE_COLOR = (255, 120, 0)

# The brightness parameter: a value from 0 (off) to 20 (full)
brightness = 10
MAX_BRIGHTNESS = 20


# Draw the whole ring at the current brightness
def show_brightness():
    fade = brightness / MAX_BRIGHTNESS
    color = (int(BASE_COLOR[0] * fade),
             int(BASE_COLOR[1] * fade),
             int(BASE_COLOR[2] * fade))
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()


print('Rotary Brightness ready. Spin the knob to change brightness.')
show_brightness()

while True:
    current_clk = clk.value()
    if current_clk != last_clk and current_clk == 0:
        if dt.value() != current_clk:
            # clockwise: brighter (but not past the maximum)
            brightness = min(brightness + 1, MAX_BRIGHTNESS)
        else:
            # counterclockwise: dimmer (but not below zero)
            brightness = max(brightness - 1, 0)
        print('brightness:', brightness)
        show_brightness()
    last_clk = current_clk
