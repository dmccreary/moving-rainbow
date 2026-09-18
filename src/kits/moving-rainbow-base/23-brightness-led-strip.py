# Lab 23: Brightness Control
# Filename: 23-brightness-led-strip.py
# Version: 1.0.0
#
# Turn a potentiometer to change the brightness of the whole strip.

from machine import ADC, Pin, PWM
from utime import sleep
from neopixel import NeoPixel
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Pins
POT_PIN = 26

pot = ADC(POT_PIN)

POLL_DELAY = .1 # poll the pot after this delay in seconds

# repeat forever
while True:
    pot_value = pot.read_u16() # read the value from the pot
    # shift the 16-bit value (0 to 65535) right 8 bits to get 0 to 255
    scaled_value = pot_value >> 8
    print("scaled value:", scaled_value)
    for i in range(NUMBER_PIXELS):
        strip[i] = (scaled_value, scaled_value, scaled_value)
    # one write per update, after every pixel is set
    strip.write()
    sleep(POLL_DELAY)
