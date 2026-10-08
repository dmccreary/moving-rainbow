# Lab 12: Scrolling Message
# Filename: 12-scrolling-message.py
# Version: 1.0.0
#
# Scrolls a message across the matrix, like a sign in a shop window.
# The matrix is only 8 pixels wide, so the program builds one long strip
# of columns and shows 8 of them at a time, sliding along one column per step.
# The letter shapes come from font.py. Save font.py on the Pico before you
# run this. Change MESSAGE to your own words.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config
import font

print("Lab 12: Scrolling Message (version 1.0.0)")

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
MATRIX_WIDTH = config.MATRIX_WIDTH
MATRIX_HEIGHT = config.MATRIX_HEIGHT
SERPENTINE = config.SERPENTINE

MESSAGE = "HELLO WORLD!"    # change me!
COLOR = (0, 30, 30)         # the color of the letters
SCROLL_DELAY = 0.12         # seconds between steps: a smaller number is faster
LETTER_HEIGHT = 5           # every letter in font.py is 5 pixels tall
TOP_ROW = 1                 # the letters sit in rows 1 to 5
EMPTY_COLUMN = "....."

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def xy(x, y):
    if SERPENTINE and y % 2 == 1:
        return y * MATRIX_WIDTH + (MATRIX_WIDTH - 1 - x)
    return y * MATRIX_WIDTH + x

def build_columns(message):
    # Turn the message into one long list of columns. A column is 5 letters,
    # read from top to bottom: "X" is a lit pixel and "." is a dark one.
    columns = [EMPTY_COLUMN] * MATRIX_WIDTH         # start with an empty matrix
    for letter in message.upper():
        rows = font.LETTERS.get(letter, font.LETTERS["?"])
        for col in range(len(rows[0])):
            column = ""
            for row in range(LETTER_HEIGHT):
                column = column + rows[row][col]
            columns.append(column)
        columns.append(EMPTY_COLUMN)                # a gap between letters
    columns = columns + [EMPTY_COLUMN] * MATRIX_WIDTH   # end with an empty matrix
    return columns

def draw_window(columns, start):
    # show 8 columns of the long strip, beginning at column number start
    for x in range(MATRIX_WIDTH):
        column = columns[start + x]
        for row in range(LETTER_HEIGHT):
            if column[row] == "X":
                strip[xy(x, TOP_ROW + row)] = COLOR
            else:
                strip[xy(x, TOP_ROW + row)] = (0, 0, 0)
    strip.write()

columns = build_columns(MESSAGE)
print("The message is", len(columns), "columns long")

while True:
    # slide the 8-column window along the strip, one column at a time
    for start in range(len(columns) - MATRIX_WIDTH + 1):
        draw_window(columns, start)
        sleep(SCROLL_DELAY)
