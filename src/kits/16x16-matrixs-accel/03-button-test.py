# Test 03: Button Test
# Filename: 03-button-test.py
# Version: 1.0.0
#
# Prints a message when each button is pressed or released, and lights
# a corner pixel while the button is held.
# Not yet tested on hardware.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

print("Test 03: Button Test (version 1.0.0)")

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
MATRIX_WIDTH = config.MATRIX_WIDTH
BUTTON_PIN_1 = config.BUTTON_PIN_1
BUTTON_PIN_2 = config.BUTTON_PIN_2

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# the buttons connect the pin to GND, so a press reads 0
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

# button 1 lights the first pixel, button 2 lights the last pixel of the first row
PIXEL_1 = 0
PIXEL_2 = MATRIX_WIDTH - 1

last1 = 1
last2 = 1
print("Press each button. Press Ctrl-C to stop.")
while True:
    now1 = button1.value()
    now2 = button2.value()
    if now1 != last1:
        print("Button 1 (GP%d):" % BUTTON_PIN_1, "pressed" if now1 == 0 else "released")
        last1 = now1
    if now2 != last2:
        print("Button 2 (GP%d):" % BUTTON_PIN_2, "pressed" if now2 == 0 else "released")
        last2 = now2
    strip[PIXEL_1] = (0, 20, 0) if now1 == 0 else (0, 0, 0)
    strip[PIXEL_2] = (0, 0, 20) if now2 == 0 else (0, 0, 0)
    strip.write()
    sleep(0.02)
