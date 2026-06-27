# Rotary Spinner Box - Button Speed
# Filename: 11-button-speed.py
#
# This lab runs the spinner from lab 05, but now the BUTTONS control a
# parameter: the speed.
#
#   BUTTON 1 (pin 14) makes the spinner faster
#   BUTTON 2 (pin 15) makes the spinner slower
#
# The buttons use interrupts (like lab 02) so the spinner never has to stop
# and wait for a button.  The animation keeps running in the main loop while
# the interrupt quietly changes the speed parameter in the background.

from neopixel import NeoPixel
import utime
import machine
from machine import Pin

import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

DOT_COLOR = (0, 60, 80)

# The speed parameter is the delay between steps, in seconds.
# A SMALLER delay means a FASTER spinner.
delay = 0.08
MIN_DELAY = 0.01
MAX_DELAY = 0.30

last_time = 0

# Buttons with internal pull-up resistors
button_faster = machine.Pin(config.PUSH_BUTTON_PIN_1, machine.Pin.IN, machine.Pin.PULL_UP)
button_slower = machine.Pin(config.PUSH_BUTTON_PIN_2, machine.Pin.IN, machine.Pin.PULL_UP)


def button_callback(pin):
    global delay, last_time
    new_time = utime.ticks_ms()
    if utime.ticks_diff(new_time, last_time) > 200:
        if pin is button_faster:
            # faster means a smaller delay
            delay = max(delay - 0.01, MIN_DELAY)
        else:
            # slower means a bigger delay
            delay = min(delay + 0.01, MAX_DELAY)
        print('delay:', round(delay, 3), 'seconds')
        last_time = new_time


button_faster.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)
button_slower.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)

position = 0

print('Button Speed ready.')
print('BUTTON 1 (pin', config.PUSH_BUTTON_PIN_1, ') = faster,',
      'BUTTON 2 (pin', config.PUSH_BUTTON_PIN_2, ') = slower.')

while True:
    strip[position] = DOT_COLOR
    strip.write()
    utime.sleep(delay)

    strip[position] = (0, 0, 0)
    strip.write()

    position = (position + 1) % config.NUMBER_PIXELS
