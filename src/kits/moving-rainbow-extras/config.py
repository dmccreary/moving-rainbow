# Moving Rainbow Extras Configuration file
# Filename: config.py
# Version: 1.0.0
#
# This file contains the hardware configuration for the base kit PLUS the
# extra sensor parts. It has every setting from the base kit's config.py,
# so save this file on your Pico in place of the base kit's config.py.
NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30
BUTTON_PIN_1 = 15
BUTTON_PIN_2 = 14

# extra parts that are not in the base kit
POT_PIN = 26             # potentiometer middle leg (GP26, an ADC pin)
PHOTORESISTOR_PIN = 28   # photoresistor voltage divider (GP28, an ADC pin)
