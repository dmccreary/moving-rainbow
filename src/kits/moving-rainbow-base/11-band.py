from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint
import config

NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
orange = (140, 60, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)

def draw_band(start, end, color):
    # draw the band from start to end
    for i in range(start, end+1):
    # use the modulo to round to within the range of the strip
        strip[i % NUMBER_PIXELS] = color
    strip.write()

# this is designed to work on a 30-pixel strp
draw_band(0, 4, red)
draw_band(5, 9, orange)
draw_band(10, 14, yellow)
draw_band(15, 19, green)
draw_band(20, 24, blue)
draw_band(25, 29, purple)
