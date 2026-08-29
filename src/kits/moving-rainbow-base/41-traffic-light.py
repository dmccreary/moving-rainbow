# Simulate a traffic light using the first three pixels of the strip.
# Each color stays on for a different amount of time, just like a real
# traffic light.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

RED_PIXEL, YELLOW_PIXEL, GREEN_PIXEL = 0, 1, 2
OFF = (0, 0, 0)


def clear_strip():
    for i in range(config.NUMBER_PIXELS):
        strip[i] = OFF


def show(red_on, yellow_on, green_on):
    clear_strip()
    strip[RED_PIXEL] = (200, 0, 0) if red_on else OFF
    strip[YELLOW_PIXEL] = (200, 160, 0) if yellow_on else OFF
    strip[GREEN_PIXEL] = (0, 200, 0) if green_on else OFF
    strip.write()


while True:
    show(True, False, False)    # red - stop
    sleep(4)
    show(False, False, True)    # green - go
    sleep(4)
    show(False, True, False)    # yellow - slow down
    sleep(1)
