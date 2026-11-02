# Lab 04: Button Test
# Filename: 04-button-test.py
# Version: 1.0.0
#
# Hold Button 1 to light the right half of the ring blue. Hold Button 2
# to light the left half yellow. Each change also prints in the Shell.
# A pin reads 1 when its button is released and 0 when it is pressed.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BUTTON_PIN_1 = config.BUTTON_PIN_1
BUTTON_PIN_2 = config.BUTTON_PIN_2
BRIGHTNESS = config.BRIGHTNESS
TOP_PIXEL = config.TOP_PIXEL

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# the other side of each button goes to ground
# if the switch is open the value is pulled up to 3.3 volts
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

blue = (0, 0, 255)
yellow = (255, 150, 0)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# turn a position counted clockwise from the top into a pixel number
def pixel_at(position):
    return (TOP_PIXEL + position) % NUMBER_PIXELS

last_value1 = 1
last_value2 = 1
while True:
    value1 = button1.value()
    value2 = button2.value()
    # print only on change
    if value1 != last_value1 or value2 != last_value2:
        print('Button 1:', value1, ' Button 2:', value2)
        last_value1 = value1
        last_value2 = value2
    for position in range(NUMBER_PIXELS):
        if position < NUMBER_PIXELS // 2:
            # the right half of the ring
            strip[pixel_at(position)] = fade(blue, 1 - value1)
        else:
            # the left half of the ring
            strip[pixel_at(position)] = fade(yellow, 1 - value2)
    strip.write()
    sleep(0.05)
