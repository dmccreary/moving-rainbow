from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 38

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
white = (128,128,128)
blue = (0, 0, 255)

colors = (red, white, blue)


def color_wipe():
    for color in colors:
        for i in range(NUMBER_PIXELS):
            strip[i] = color
            strip.write()
            sleep(0.04)

while True:
    color_wipe() 