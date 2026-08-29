# Automatically cycle through three light patterns, staying on each one
# for a few seconds before moving to the next. No buttons yet - this is
# the "mode variable" pattern that the button-driven modes lesson builds on.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

SECONDS_PER_MODE = 4   # how long to stay on each mode before switching
NUM_MODES = 3


def fill_strip(color):
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()


def run_mode(mode):
    if mode == 0:
        fill_strip((200, 0, 0))    # mode 0: solid red
    elif mode == 1:
        fill_strip((0, 200, 0))    # mode 1: solid green
    else:
        fill_strip((0, 0, 200))    # mode 2: solid blue


mode = 0
run_mode(mode)
mode_start_time = ticks_ms()

while True:
    elapsed_seconds = (ticks_ms() - mode_start_time) / 1000

    if elapsed_seconds >= SECONDS_PER_MODE:
        mode = (mode + 1) % NUM_MODES   # advance to the next mode, then wrap
        run_mode(mode)
        mode_start_time = ticks_ms()
        print("mode:", mode)

    sleep(0.1)
