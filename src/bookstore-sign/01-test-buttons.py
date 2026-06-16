# Bookstore Sign - Button Mode Test
# Filename: test-buttons.py
#
# Press BUTTON_1 to increment the mode, BUTTON_2 to decrement the mode.
# The mode cycles through 7 values (0-6) and wraps around at both ends.
# The current mode is printed to the MicroPython console whenever it changes.
#
# A 200ms debounce in the interrupt handler keeps a single press from
# registering as several presses.

import utime
import machine
from machine import Pin

import config

# Number of modes to cycle through (0 through 6)
NUMBER_MODES = 7

mode = 0          # the current mode
last_time = 0     # the last time a button event was handled (for debounce)

# Toggle the built-in LED for visual feedback on each press
builtin_led = machine.Pin(config.BUILT_IN_LED_PIN, Pin.OUT)

# Both buttons connect the pin to ground when pressed, so use PULL_UP
button_up = machine.Pin(config.BUTTON_PIN_1, machine.Pin.IN, machine.Pin.PULL_UP)
button_down = machine.Pin(config.BUTTON_PIN_2, machine.Pin.IN, machine.Pin.PULL_UP)


# Interrupt callback - get in and out quickly
def button_callback(pin):
    global mode, last_time
    new_time = utime.ticks_ms()
    # only act if it has been more than 200ms since the last event
    if utime.ticks_diff(new_time, last_time) > 200:
        if pin is button_up:
            mode = (mode + 1) % NUMBER_MODES
        else:
            mode = (mode - 1) % NUMBER_MODES
        last_time = new_time


# Register the handler for the falling edge (button press) of each button
button_up.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)
button_down.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)

# Only print when the mode value actually changes
old_mode = -1

print('Press BUTTON_1 (pin', config.BUTTON_PIN_1, ') to go up,',
      'BUTTON_2 (pin', config.BUTTON_PIN_2, ') to go down.')
print('Mode:', mode)

while True:
    if mode != old_mode:
        print('Mode:', mode)
        builtin_led.toggle()
        old_mode = mode
