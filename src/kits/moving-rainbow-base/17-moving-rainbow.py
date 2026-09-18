from machine import Pin
from neopixel import NeoPixel
from utime import sleep
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

while True:
    for i in range(0, NUMBER_PIXELS - num_colors + 1):
        index = 0
        # draw the rainbow
        for color in colors:
            strip[index + i] = colors[index]
            index += 1
        strip.write()
        sleep(.05)
        # erase the current pixel
        strip[i] = (0,0,0)
        # erase the last draw
        if i == NUMBER_PIXELS - num_colors:
            strip[i+1] = (0,0,0)
            strip[i+2] = (0,0,0)
            strip[i+3] = (0,0,0)
            strip[i+4] = (0,0,0)
            strip[i+5] = (0,0,0)
            strip[i+6] = (0,0,0)
            strip.write()
