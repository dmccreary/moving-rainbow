# Halloween Costume Kit Configuration file
# Filename: config.py
# Version: 1.0.0
#
# This file contains the hardware configuration for the Halloween costume kit.
# It is imported by each program.
#
# The kit has a 60-pixel NeoPixel strip on GPIO 0 and one push button
# wired from GPIO 15 to GND.
NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60
BUTTON_PIN = 15

# 60 pixels at full brightness can pull more than 3 amps, which is too much
# for a USB battery pack. Every program multiplies its colors by this number.
# 0.25 means one quarter brightness. Keep it at 0.3 or lower on battery power.
BRIGHTNESS = 0.25
