# Binary Search: think of a pixel number from 0 to NUMBER_PIXELS-1 in
# your head. Press Button 1 if your number is HIGHER than the lit pixel.
# Press Button 2 if it's LOWER than or equal to the lit pixel. Watch how
# few guesses it takes to find your number!
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

n = config.NUMBER_PIXELS


def draw_range(low, high, guess):
    for i in range(n):
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
    print("Think of a pixel number from 0 to", n - 1)
    sleep(2)

    low, high = 0, n - 1
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
