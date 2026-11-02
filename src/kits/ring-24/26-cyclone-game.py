# Lab 26: Cyclone Game
# Filename: 26-cyclone-game.py
# Version: 1.0.0
#
# A game like the Cyclone arcade machine. A yellow dot races around the
# ring. Press either button at the moment the dot is on the green target.
# Each hit moves the target and speeds up the dot. After 5 hits the target
# shrinks to one pixel. A miss shows your score as yellow pixels counted
# clockwise from the top, and then a new game starts.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms, ticks_diff
from urandom import randint
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BUTTON_PIN_1 = config.BUTTON_PIN_1
BUTTON_PIN_2 = config.BUTTON_PIN_2
BRIGHTNESS = config.BRIGHTNESS
TOP_PIXEL = config.TOP_PIXEL

DEBOUNCE_MS = 150        # ignore extra presses closer together than this
START_DELAY = 0.08       # seconds between steps when a game starts
FASTEST_DELAY = 0.015    # the dot never goes faster than this
SPEED_UP = 0.88          # each hit multiplies the delay by this
SMALL_TARGET_SCORE = 5   # the score where the target shrinks

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 150, 0)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# turn a position counted clockwise from the top into a pixel number
def pixel_at(position):
    return (TOP_PIXEL + position) % NUMBER_PIXELS

# the shortest number of steps between two pixels, going either way around
def ring_distance(a, b):
    forward = (a - b) % NUMBER_PIXELS
    backward = (b - a) % NUMBER_PIXELS
    return min(forward, backward)

button_was_pressed = False
last_press = 0

# this function runs by itself the moment either button is pressed
def button_pressed(pin):
    global button_was_pressed, last_press
    now = ticks_ms()
    # a button "bounces" and can look like many presses, so we ignore
    # any press that comes too soon after the last one
    if ticks_diff(now, last_press) > DEBOUNCE_MS:
        button_was_pressed = True
        last_press = now

# call button_pressed when a pin falls from 1 (released) to 0 (pressed)
button1.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)

def flash(color, times):
    for n in range(times):
        strip.fill(fade(color, 1))
        strip.write()
        sleep(0.12)
        strip.fill((0, 0, 0))
        strip.write()
        sleep(0.12)

def show_score(score):
    strip.fill((0, 0, 0))
    for position in range(min(score, NUMBER_PIXELS)):
        strip[pixel_at(position)] = fade(yellow, 1)
    strip.write()
    sleep(2)

print('Press a button when the yellow dot is on the green target!')
position = 0
target = NUMBER_PIXELS // 2
score = 0
delay = START_DELAY
while True:
    # the target is 3 pixels wide at first, and then just 1
    if score < SMALL_TARGET_SCORE:
        reach = 1
    else:
        reach = 0

    if button_was_pressed:
        if ring_distance(position, target) <= reach:
            score += 1
            print('Hit! Score:', score)
            flash(green, 1)
            target = randint(0, NUMBER_PIXELS - 1)
            delay = max(delay * SPEED_UP, FASTEST_DELAY)
        else:
            print('Missed! Final score:', score)
            flash(red, 3)
            show_score(score)
            score = 0
            delay = START_DELAY
            target = NUMBER_PIXELS // 2
        button_was_pressed = False   # ignore any presses during the flashing

    strip.fill((0, 0, 0))
    for offset in range(-reach, reach + 1):
        strip[pixel_at(target + offset)] = fade(green, 0.5)
    strip[pixel_at(position)] = fade(yellow, 1)
    strip.write()
    sleep(delay)
    position = (position + 1) % NUMBER_PIXELS
