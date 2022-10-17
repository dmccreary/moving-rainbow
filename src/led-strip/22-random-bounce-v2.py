# random bounce
# pixels appear to bounce around on the LED strip as they move back-and-forth
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
red_med = (32, 0, 0)
red_light = (8, 0, 0)
off = (0, 0, 0)
orange = (140, 60, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
purple = (255, 0, 255)
white = (128, 128, 128)
colors = (red, orange, yellow, green, blue, cyan, indigo, violet, purple)
color_count = len(colors)
levels = [255, 128, 64, 32, 16, 8, 4, 2, 1]
level_count = len(levels)

# location and color are stored in a list
pixel_list = [
  [10, 1, (255, 0, 0)],
  [20, -1, (0, 255, 0)],
  [30, 1, (0, 0, 255)],
]

def add_pixel(my_list, delay, color):
    random_index = randint(0, NUMBER_PIXELS-1)
    # random dir is 1 or -1
    dir = randint(-1,1)
    if dir == 0:
        dir = -1
    print('adding pixel at', random_index, 'moving', dir)
    # must be a list since tuple is non-mutable
    my_list.append(list((random_index, dir, color)))

def display_pixel(id):
    strip[id[0]] = id[2]
    strip.write()

def display_pixels(pixel_list):
    for i in range(0, len(pixel_list)):
        print('displaying', pixel_list[i])
        display_pixel(pixel_list[i])

def update_pixel(id):
    strip[id[0]] = id[2]
    if id[1] == 1:
       strip[ id[0]-1 ] = (0,0,0)
    strip.write()

def clear():
    for i in range(0, NUMBER_PIXELS-1):
        strip[i] = (0,0,0)
        strip.write()    

add_pixel(pixel_list, 1, yellow)
add_pixel(pixel_list, 1, cyan)
add_pixel(pixel_list, 1, purple)
print('found ', len(pixel_list), 'items in pixel list')
print(pixel_list)
counter = 0
clear()
# drop in N pixels
while True:
    # for each pixel
    display_pixels(pixel_list)
    # update positions
    for i in range(0, len(pixel_list)):
        print('current pixel', pixel_list[i])
        if pixel_list[i][1] == 1:
            new_index = pixel_list[i][0] + 1
            if new_index > NUMBER_PIXELS - 1:
                new_index = NUMBER_PIXELS - 1
                # reverse direction
                pixel_list[i][1] = -1
            pixel_list[i][0] = new_index
        else:
            new_index = pixel_list[i][0] - 1
            if new_index < 0:
                pixel_list[i][0] = 0
                pixel_list[i][1] = 1
            pixel_list[i][0] = pixel_list[i][0] - 1
    sleep(.1)
    