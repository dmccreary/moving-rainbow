from machine import Pin
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60
strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
orange = (140, 60, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
light_green = (30, 255, 30)
blue = (0, 0, 255)
cyan = (0, 255, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
white = (128, 128, 128)
colors = (red, orange, yellow, green, light_green, blue, cyan, indigo, violet, white)
color_count = len(colors)
levels = [255, 128, 64, 32, 16, 8, 4, 2, 1]
level_count = len(levels)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

# offset should be incremented by one for motion
def draw_comet_tail(offset, color, delay):
    offset = offset % NUMBER_PIXELS
    for i in range(0, color_count-1):
        target = ((level_count - i - 1) + offset) % NUMBER_PIXELS
        # number to scale by
        scale = (levels[i] / 255)
        strip[target] = (int(color[0]*scale), int(color[1]*scale), int(color[2]*scale))      
        if offset > 0:
            strip[offset-1] = (0,0,0)
        if offset == NUMBER_PIXELS-1:
            strip[offset] = (0,0,0)
        strip.write()
        sleep(delay)

def clear():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,0)
    strip.write()

# setup
counter = 0
clear()

# main loop
while True:
    for color_index in range(0, color_count):
        for i in range(0, NUMBER_PIXELS):
            draw_comet_tail(counter, colors[color_index], .005)
            counter += 1
            print(counter)
