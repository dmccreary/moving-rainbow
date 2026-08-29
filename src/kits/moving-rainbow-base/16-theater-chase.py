from machine import Pin
from neopixel import NeoPixel
from utime import sleep, sleep_ms
import config

NUMBER_PIXELS = config.NUMBER_PIXELS
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), NUMBER_PIXELS)

# Color RGB values
red = (255, 0, 0)
orange = (255, 60, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
color_names = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
num_colors = len(color_names)
colors = (red, orange, yellow, green, blue, indigo, violet)

def theater_chase(strip, color, wait_ms, iterations):
    for j in range(iterations):
        for q in range(4):
            # turn every nth one on
            for i in range(0, NUMBER_PIXELS-1, 4):
                if i+q < NUMBER_PIXELS:
                    strip[i+q] = color
            strip.write()
            sleep_ms(wait_ms)
            # erase
            for i in range(0, NUMBER_PIXELS-1, 4):
                strip[(i+q) % NUMBER_PIXELS] = (0,0,0)

while True:
    # iterate through all the colors
    for c in range(0, num_colors):
        theater_chase(strip, colors[c], 200, 8)
