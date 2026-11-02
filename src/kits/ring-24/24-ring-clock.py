# Lab 24: Ring Clock
# Filename: 24-ring-clock.py
# Version: 1.0.0
#
# The ring becomes a clock face. The hour hand is red, the minute hand is
# green and the second hand is blue. Where hands overlap, their colors mix.
# Button 1 adds one hour and Button 2 adds one minute, so you can set the
# time. (Thonny sets the Pico's clock when it connects. On battery power
# the clock starts from a fixed time and you set it with the buttons.)

from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms, ticks_diff, time
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BUTTON_PIN_1 = config.BUTTON_PIN_1
BUTTON_PIN_2 = config.BUTTON_PIN_2
BRIGHTNESS = config.BRIGHTNESS
TOP_PIXEL = config.TOP_PIXEL

DEBOUNCE_MS = 200        # ignore extra presses closer together than this

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# add two colors together, keeping each part at 255 or less
def mix(color1, color2):
    return (min(color1[0] + color2[0], 255),
            min(color1[1] + color2[1], 255),
            min(color1[2] + color2[2], 255))

# turn a position counted clockwise from the top into a pixel number
def pixel_at(position):
    return (TOP_PIXEL + position) % NUMBER_PIXELS

# add a color to whatever is already at this position
def draw_hand(position, color):
    pixel = pixel_at(position)
    strip[pixel] = mix(strip[pixel], fade(color, 1))

offset_seconds = 0       # the seconds the buttons have added to the Pico's clock
last_press = 0

# this function runs by itself the moment Button 1 is pressed
def button1_pressed(pin):
    global offset_seconds, last_press
    now = ticks_ms()
    # a button "bounces" and can look like many presses, so we ignore
    # any press that comes too soon after the last one
    if ticks_diff(now, last_press) > DEBOUNCE_MS:
        offset_seconds += 3600   # one hour
        last_press = now

# this function runs by itself the moment Button 2 is pressed
def button2_pressed(pin):
    global offset_seconds, last_press
    now = ticks_ms()
    if ticks_diff(now, last_press) > DEBOUNCE_MS:
        offset_seconds += 60     # one minute
        last_press = now

# call the function when the pin falls from 1 (released) to 0 (pressed)
button1.irq(trigger=Pin.IRQ_FALLING, handler=button1_pressed)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button2_pressed)

QUARTER = NUMBER_PIXELS // 4

last_minute = -1
while True:
    total = time() + offset_seconds
    second = total % 60
    minute = (total // 60) % 60
    hour = (total // 3600) % 12      # 12 hours once around the clock face

    if minute != last_minute:
        print('The time is', 12 if hour == 0 else hour, ':', minute)
        last_minute = minute

    strip.fill((0, 0, 0))
    # dim marks at 12, 3, 6 and 9 o'clock
    for mark in range(4):
        strip[pixel_at(mark * QUARTER)] = fade(white, 0.05)
    # the fraction of the way around the dial, times the number of pixels
    draw_hand(second * NUMBER_PIXELS // 60, blue)
    draw_hand(minute * NUMBER_PIXELS // 60, green)
    # the hour hand also creeps along during the hour
    draw_hand((hour * 60 + minute) * NUMBER_PIXELS // 720, red)
    strip.write()
    sleep(0.1)
