# Lab 05: Button Test
# Filename: 05-button-test.py
# Version: 1.0.0
#
# Print the value of the button in the Shell: 1 when it is released and 0
# when it is pressed. The onboard LED also lights while you hold the button.

from machine import Pin
from utime import sleep
import config

# hardware settings from config.py
BUTTON_PIN = config.BUTTON_PIN
# the LED built onto the Pico board (not set in config.py)
BUILT_IN_LED_PIN = 25

# the button connects GPIO 15 to GND
# PULL_UP holds the pin at 3.3 volts (a 1) until the button pulls it to GND (a 0)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
led = Pin(BUILT_IN_LED_PIN, Pin.OUT)

while True:
    value = button.value()
    print(value)
    if value == 0:       # 0 means the button is pressed
        led.on()
    else:
        led.off()
    sleep(0.1)           # wait 1/10th of a second
