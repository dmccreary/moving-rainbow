# Lab 46: Binary Search Visualizer
# Filename: 46-binary-search-visualizer.py
# Version: 1.0.0
#
# Think of a pixel number from 0 to NUMBER_PIXELS-1 in your head. Press
# Button 1 if your number is HIGHER than the lit pixel. Press Button 2
# if it is LOWER than or equal to the lit pixel. Watch how few guesses
# it takes to find your number!

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BUTTON_PIN_1 = config.BUTTON_PIN_1
BUTTON_PIN_2 = config.BUTTON_PIN_2

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)



def draw_range(low, high, guess):
    for i in range(NUMBER_PIXELS):
        if i == guess:
            strip[i] = (255, 255, 255)   # current guess: white
        elif low <= i <= high:
            strip[i] = (0, 0, 80)        # still in range: dim blue
        else:
            strip[i] = (0, 0, 0)         # ruled out: off
    strip.write()


def wait_for_button():
    while True:
        if button1.value() == 0:
            return "higher"
        if button2.value() == 0:
            return "lower"
        sleep(0.01)


def wait_for_release():
    while button1.value() == 0 or button2.value() == 0:
        sleep(0.01)


while True:
    print("Think of a pixel number from 0 to", NUMBER_PIXELS - 1)
    sleep(2)

    low, high = 0, NUMBER_PIXELS - 1
    guesses = 0

    while low < high:
        guess = (low + high) // 2
        draw_range(low, high, guess)
        guesses += 1
        print("Guess", guesses, "-> pixel", guess)

        answer = wait_for_button()
        wait_for_release()

        if answer == "higher":
            low = guess + 1
        else:
            high = guess

    draw_range(low, high, low)
    print("Found it! Your number was", low, "in", guesses, "guesses")

    for _ in range(4):
        strip[low] = (0, 255, 0)
        strip.write()
        sleep(0.2)
        strip[low] = (0, 0, 0)
        strip.write()
        sleep(0.2)

    sleep(1)
