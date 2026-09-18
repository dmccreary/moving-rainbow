# Lab 28: Button Test
# Filename: 28-button-test.py
# Version: 1.0.0
#
# Print the value of Button 1 in the Shell: 1 when it is released and 0
# when it is pressed.

from machine import Pin
import time
import config

# hardware settings from config.py
BUTTON_PIN_1 = config.BUTTON_PIN_1

# input on the lower left of the Pico
# the other side of the button goes to ground
# if the switch is open the value is pulled up to 3.3 volts
button = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)

while True:
    print(button.value())
    time.sleep(0.1) # wait 1/10th of a second
