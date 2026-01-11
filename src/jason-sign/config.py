# Moving Rainbow Configuration file
# Filename: config.py
# This file contains the hardware configuration for your kit
# This file can be imported by each program

# The pin that we connect the NeoPixel data pin
NEOPIXEL_PIN = 0

# The number of pixels in the sign
NUMBER_PIXELS = 65

# pins to change the sign mode
BUTTON_PIN_1 = 15
BUTTON_PIN_2 = 14

# The pin we connect the centerpoint of the voltage divider to the photoresitor
# The positive end is ADC_VREF and the negate is AGND
ADC_PIN_0 = 26

# Define pixel ranges for each letter (start, end) - end is inclusive
LETTERS = {
    'J': (0, 7),
    'A': (8, 20),
    'S': (21, 33),
    'O': (34, 47),
    'N': (48, 64)
}