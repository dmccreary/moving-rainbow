# Lab 23: Speed and Direction
# Filename: 23-speed-and-direction.py
# Version: 1.0.0
#
# A rainbow comet circles the ring. Button 1 steps through five speeds and
# Button 2 makes the comet turn around. The direction is just a number:
# +1 goes clockwise and -1 goes counter-clockwise.

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

DEBOUNCE_MS = 200        # ignore extra presses closer together than this
TAIL_LENGTH = 12         # how many pixels long the comet is
delays = (0.16, 0.08, 0.04, 0.02, 0.01)   # seconds between steps, slow to fast

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

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

speed_index = 1
direction = 1
last_press = 0

# this function runs by itself the moment Button 1 is pressed
def button1_pressed(pin):
    global speed_index, last_press
    now = ticks_ms()
    # a button "bounces" and can look like many presses, so we ignore
    # any press that comes too soon after the last one
    if ticks_diff(now, last_press) > DEBOUNCE_MS:
        speed_index = (speed_index + 1) % len(delays)
        last_press = now

# this function runs by itself the moment Button 2 is pressed
def button2_pressed(pin):
    global direction, last_press
    now = ticks_ms()
    if ticks_diff(now, last_press) > DEBOUNCE_MS:
        direction = -direction
        last_press = now

# call the function when the pin falls from 1 (released) to 0 (pressed)
button1.irq(trigger=Pin.IRQ_FALLING, handler=button1_pressed)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button2_pressed)

position = 0
hue = 0
while True:
    strip.fill((0, 0, 0))
    for t in range(TAIL_LENGTH):
        amount = (1 - t / TAIL_LENGTH) ** 2
        color = wheel((hue + t * 12) % 256)
        # the tail is always behind the head, whichever way it goes
        strip[(position - t * direction) % NUMBER_PIXELS] = fade(color, amount)
    strip.write()
    sleep(delays[speed_index])
    position = (position + direction) % NUMBER_PIXELS
    hue = (hue + 2) % 256
