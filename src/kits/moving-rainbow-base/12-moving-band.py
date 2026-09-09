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
i=0
while True:
    draw_band(0+i, 4+i, red)
    draw_band(5+i, 9+i, orange)
    draw_band(10+i, 14+i, yellow)
    draw_band(15+i, 19+i, green)
    draw_band(20+i, 24+i, blue)
    draw_band(25+i, 29+i, purple)
    i += 1
    sleep(.03)
