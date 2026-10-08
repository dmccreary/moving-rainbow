# Lab 10: Picture Show
# Filename: 10-picture-show.py
# Version: 1.0.0
#
# Shows the eight pictures in the gallery file pictures.py, one at a time.
# Press button 1 for the next picture and button 2 for the one before.
# If you press nothing, the show moves on by itself.
# Save pictures.py on the Pico before you run this.
# Not yet tried by hand: the buttons need a person to press them.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep_ms, ticks_ms, ticks_diff
import config
import pictures

print("Lab 10: Picture Show (version 1.0.0)")

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
MATRIX_WIDTH = config.MATRIX_WIDTH
MATRIX_HEIGHT = config.MATRIX_HEIGHT
SERPENTINE = config.SERPENTINE
BUTTON_PIN_1 = config.BUTTON_PIN_1
BUTTON_PIN_2 = config.BUTTON_PIN_2

HOLD_MS = 3000      # how long a picture stays if you press nothing - change me!

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# the buttons connect the pin to GND, so a press reads 0
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

def xy(x, y):
    if SERPENTINE and y % 2 == 1:
        return y * MATRIX_WIDTH + (MATRIX_WIDTH - 1 - x)
    return y * MATRIX_WIDTH + x

def draw(picture):
    # look at every letter and give the pixel in the same spot its color
    for y in range(MATRIX_HEIGHT):
        for x in range(MATRIX_WIDTH):
            letter = picture[y][x]
            strip[xy(x, y)] = pictures.COLORS[letter]
    strip.write()

def show(number):
    # draw one picture from the gallery and print its name
    name, picture = pictures.GALLERY[number]
    print("Picture", number + 1, "-", name)
    draw(picture)

count = len(pictures.GALLERY)
number = 0
show(number)
shown_at = ticks_ms()
last1 = 1
last2 = 1
print("Button 1 is next. Button 2 is back. Press Ctrl-C to stop.")
while True:
    now1 = button1.value()
    now2 = button2.value()
    step = 0
    if now1 == 0 and last1 == 1:        # button 1 was just pressed
        step = 1
    if now2 == 0 and last2 == 1:        # button 2 was just pressed
        step = -1
    last1 = now1
    last2 = now2
    if step == 0 and ticks_diff(ticks_ms(), shown_at) >= HOLD_MS:
        step = 1                        # nobody pressed, so move on
    if step != 0:
        number = (number + step) % count
        show(number)
        shown_at = ticks_ms()
    sleep_ms(20)
