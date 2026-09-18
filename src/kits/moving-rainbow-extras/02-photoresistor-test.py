# Extras Lab 02: Photoresistor Test
# Filename: 02-photoresistor-test.py
# Version: 1.0.0
#
# Read the light level from a photoresistor and print it in the Shell.
# Needs a photoresistor (an extra part) and the extras config.py.
# Not yet tested on hardware: adapt for your setup.

from machine import ADC
from utime import sleep
import config

# hardware settings from config.py
PHOTORESISTOR_PIN = config.PHOTORESISTOR_PIN

photo = ADC(PHOTORESISTOR_PIN)

while True:
    light_value = photo.read_u16()   # a number from 0 to 65535
    print(light_value)               # show it in the Shell
    sleep(0.2)                       # wait a fifth of a second
