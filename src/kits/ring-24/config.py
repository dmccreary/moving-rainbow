# Ring 24 Kit Configuration file
# Filename: config.py
# Version: 1.0.0
#
# This file contains the hardware configuration for your kit.
# It is imported by each program.
#
# The kit has a 24-pixel NeoPixel ring on GPIO 0 and two push buttons
# wired from GPIO 15 and GPIO 14 to GND.
NEOPIXEL_PIN = 0
NUMBER_PIXELS = 24
BUTTON_PIN_1 = 15
BUTTON_PIN_2 = 14

# The pixel numbers run clockwise. Pixel 0 sits at about 1:30 on a clock
# dial, so the pixel at 12 o'clock is number 21. If you mount your ring a
# different way, run Lab 03 and change this number until red is at the top.
TOP_PIXEL = 21

# 24 pixels at full brightness can pull more than 1 amp, which is too much
# for a USB port. Every program multiplies its colors by this number.
# 0.25 means one quarter brightness.
BRIGHTNESS = 0.25
