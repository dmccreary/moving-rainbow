# Lab 29: Button and Built-in LED
# Filename: 29-button-led-test.py
# Version: 1.0.0
#
# The Pico's built-in LED turns on while Button 1 is pressed.

from machine import Pin
import time
import config

# hardware settings from config.py
BUTTON_PIN_1 = config.BUTTON_PIN_1
# the LED built onto the Pico board (not set in config.py)
BUILT_IN_LED_PIN = 25

# input on the lower left of the Pico
# the other side of the button goes to ground
# if the switch is open the value is pulled up to 3.3 volts

# Create a button object on the pin
button = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)

# create an LED object
led = Pin(BUILT_IN_LED_PIN, Pin.OUT)

button_value = 0
old_value = 0
while True:
    # get the new value
    button_value = button.value()
    
    # change the LED to on when the button is pressed
    if button_value == 1:
        led.off()
    else:
        led.on()
        
    # only print on if there is a change
    if button_value != old_value:
        print(button_value)
        old_value = button_value
