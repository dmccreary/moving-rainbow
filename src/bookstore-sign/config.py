# Moving Rainbow Configuration file
# Filename: config.py
# This file contains the hardware configuration for the BOOKSTORE sign
# This file can be imported by each program

# The pin that we connect the NeoPixel data pin
NEOPIXEL_PIN = 0

# The total number of pixels in the sign
NUMBER_PIXELS = 134

# pins to change the sign mode
BUTTON_PIN_1 = 15
BUTTON_PIN_2 = 14

# The pin we connect the centerpoint of the voltage divider to the photoresistor.
# The positive end is ADC_VREF and the negative is AGND.
ADC_PIN_0 = 26

# The on-board LED can be used for status indication
BUILT_IN_LED_PIN = 25

# Pixel range for each letter as (letter, start, end) - end is inclusive.
# NOTE: We use a LIST of tuples instead of a dictionary because the word
# "BOOKSTORE" contains the letter 'O' three times.  Dictionary keys must be
# unique, so a dict keyed by letter would lose two of the three O's.  A list
# keeps every letter in left-to-right order, duplicates and all.
LETTERS = [
    ('B', 0, 19),     # 20 pixels
    ('O', 20, 33),    # 14 pixels
    ('O', 34, 47),    # 14 pixels
    ('K', 48, 61),    # 14 pixels
    ('S', 62, 77),    # 16 pixels
    ('T', 78, 87),    # 10 pixels
    ('O', 88, 101),   # 14 pixels
    ('R', 102, 115),  # 14 pixels
    ('E', 116, 133),  # 18 pixels
]
