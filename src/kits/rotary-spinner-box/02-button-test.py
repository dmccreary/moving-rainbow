# Rotary Spinner Box - Two Button Test
# Filename: 02-button-test.py
#
# This program tests the two momentary push buttons on the rotary spinner box.
# Each time you press a button, a message is printed to the MicroPython console.
#
#   BUTTON 1 is on GPIO pin 14 (config.PUSH_BUTTON_PIN_1)
#   BUTTON 2 is on GPIO pin 15 (config.PUSH_BUTTON_PIN_2)
#
# Both buttons connect their pin to ground when pressed, so we turn on the
# internal PULL_UP resistor.  The pin reads 1 (HIGH) when the button is up and
# 0 (LOW) when the button is pressed down.
#
# A 200ms debounce in the interrupt handler keeps a single press from
# registering as several presses.

import utime
import machine
from machine import Pin

import config

# Count how many times each button has been pressed
button_1_count = 0
button_2_count = 0

# The last time we handled a button event (used for debounce)
last_time = 0

# Toggle the built-in LED for visual feedback on each press
builtin_led = machine.Pin(25, Pin.OUT)

# Set up both buttons as inputs with internal pull-up resistors
button_1 = machine.Pin(config.PUSH_BUTTON_PIN_1, machine.Pin.IN, machine.Pin.PULL_UP)
button_2 = machine.Pin(config.PUSH_BUTTON_PIN_2, machine.Pin.IN, machine.Pin.PULL_UP)


# The interrupt callback - get in and out quickly
def button_callback(pin):
    global button_1_count, button_2_count, last_time
    new_time = utime.ticks_ms()
    # only act if it has been more than 200ms since the last event
    if utime.ticks_diff(new_time, last_time) > 200:
        if pin is button_1:
            button_1_count += 1
            print('BUTTON 1 pressed (pin', config.PUSH_BUTTON_PIN_1,
                  ') - count:', button_1_count)
        else:
            button_2_count += 1
            print('BUTTON 2 pressed (pin', config.PUSH_BUTTON_PIN_2,
                  ') - count:', button_2_count)
        builtin_led.toggle()
        last_time = new_time


# Register the handler for the falling edge (button press) of each button
button_1.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)
button_2.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)

print('Two Button Test ready.')
print('Press BUTTON 1 (pin', config.PUSH_BUTTON_PIN_1,
      ') or BUTTON 2 (pin', config.PUSH_BUTTON_PIN_2, ').')

# The interrupt handlers do all the work, so the main loop just waits
while True:
    utime.sleep(1)
