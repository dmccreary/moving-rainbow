# Larson Scanner - five pixels
from machine import Pin
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 12
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
red_med = (32, 0, 0)
red_light = (8, 0, 0)
off = (0,0,0)

delay = .05
while True:
    # forward loop
    for i in range(2, NUMBER_PIXELS-2):
        strip[i-2] = red_light
        strip[i-1] = red_med
        strip[i] = red
        strip[i+1] = red_med
        strip[i+2] = red_light
        # erase the trailing pixel
        if i > 0:
            strip[i-3] = off
        strip.write()
        sleep(delay)
    # backward loop
    for i in range(NUMBER_PIXELS-4, 1, -1):
        # erase the trailing pixel
        if i < NUMBER_PIXELS-2:
            strip[i+3] = off
        strip[i-2] = red_light
        strip[i-1] = red_med
        strip[i] = red
        strip[i+1] = red_med
        strip[i+2] = red_light
        strip.write()
        sleep(delay)