# Lab 22: Button Dial
# Filename: 22-button-dial.py
# Version: 1.0.0
#
# The two buttons turn the ring like a dial. Button 1 moves the dot one
# step clockwise and Button 2 moves it one step counter-clockwise. The dim
# marks show 12, 3, 6 and 9 o'clock.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms, ticks_diff
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BUTTON_PIN_1 = config.BUTTON_PIN_1
BUTTON_PIN_2 = config.BUTTON_PIN_2
BRIGHTNESS = config.BRIGHTNESS
TOP_PIXEL = config.TOP_PIXEL

DEBOUNCE_MS = 150        # ignore extra presses closer together than this

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

red = (255, 0, 0)
white = (255, 255, 255)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# turn a position counted clockwise from the top into a pixel number
def pixel_at(position):
    return (TOP_PIXEL + position) % NUMBER_PIXELS

position = 0
last_press = 0

# this function runs by itself the moment Button 1 is pressed
def button1_pressed(pin):
    global position, last_press
    now = ticks_ms()
    # a button "bounces" and can look like many presses, so we ignore
    # any press that comes too soon after the last one
    if ticks_diff(now, last_press) > DEBOUNCE_MS:
        position = (position + 1) % NUMBER_PIXELS
        last_press = now

# this function runs by itself the moment Button 2 is pressed
def button2_pressed(pin):
    global position, last_press
    now = ticks_ms()
    if ticks_diff(now, last_press) > DEBOUNCE_MS:
        position = (position - 1) % NUMBER_PIXELS
        last_press = now

# call the function when the pin falls from 1 (released) to 0 (pressed)
button1.irq(trigger=Pin.IRQ_FALLING, handler=button1_pressed)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button2_pressed)

QUARTER = NUMBER_PIXELS // 4

last_position = -1
while True:
    if position != last_position:
        print('position', position, 'angle', position * 360 // NUMBER_PIXELS)
        last_position = position
    strip.fill((0, 0, 0))
    for mark in range(4):
        strip[pixel_at(mark * QUARTER)] = fade(white, 0.1)
    strip[pixel_at(position)] = fade(red, 1)
    strip.write()
    sleep(0.03)
