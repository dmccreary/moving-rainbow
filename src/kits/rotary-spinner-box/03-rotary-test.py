# Rotary Spinner Box - Rotary Encoder Test
# Filename: 03-rotary-test.py
#
# This program tests the rotary encoder (the knob you can spin).
# Turning the knob one "click" prints a message to the console and changes
# a counter.  Turning clockwise (CW) adds 1, counterclockwise (CCW) subtracts 1.
#
#   ENCODER PIN A (CLK) is on GPIO pin 12 (config.ROTARY_ENCODER_PIN_A)
#   ENCODER PIN B (DT)  is on GPIO pin 13 (config.ROTARY_ENCODER_PIN_B)
#
# A rotary encoder has two switches that turn on and off in a known order as
# you spin it.  By watching which one changes first, we can tell the direction.

import utime
import machine
from machine import Pin

import config

# Set up the two encoder pins as inputs with internal pull-up resistors
clk = machine.Pin(config.ROTARY_ENCODER_PIN_A, machine.Pin.IN, machine.Pin.PULL_UP)
dt = machine.Pin(config.ROTARY_ENCODER_PIN_B, machine.Pin.IN, machine.Pin.PULL_UP)

# Remember the last value of CLK so we can see when it changes
last_clk = clk.value()

# The running counter
counter = 0

print('Rotary Encoder Test ready.')
print('Spin the knob clockwise (CW) or counterclockwise (CCW).')

while True:
    current_clk = clk.value()
    # We act only on the falling edge of CLK (when it changes from 1 to 0)
    if current_clk != last_clk and current_clk == 0:
        if dt.value() != current_clk:
            counter += 1
            print('CW  -> count:', counter)
        else:
            counter -= 1
            print('CCW -> count:', counter)
    last_clk = current_clk
