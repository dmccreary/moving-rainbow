# Lab 02: Hardware Probe
# Filename: 02-probe.py
# Version: 1.0.0
#
# A detailed check of the Pico, the button and the 60-pixel strip. It
# prints board info, checks config.py, checks the pin levels, lights the
# first, middle and last pixels, waits for you to press the button and ends
# with TEST PASS or TEST FAIL.
# Run it in Thonny, or from your computer with ./run-probe.sh
# Not yet tested on hardware.
#
# Wiring under test:
#   Strip DIN -> GPIO0
#   Strip +5V -> VBUS (pin 40)
#   Strip GND -> GND
#   Button    -> GPIO15 (pin 20) to GND (pin 18)
#
# Pull-ups: the pin level checks turn on the RP2040's internal weak pull-up
# (about 50-80 kOhm), so a pin that reads 0 while nothing is pressed is
# shorted to GND or wired to the wrong place.

import sys
import os
import gc
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, sleep_ms, ticks_ms, ticks_diff
import config

print("Lab 02: Hardware Probe (version 1.0.0)")

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BUTTON_PIN = config.BUTTON_PIN
BRIGHTNESS = config.BRIGHTNESS

EXPECTED_PIXELS = 60
MAX_SAFE_BRIGHTNESS = 0.3     # above this a USB battery pack may shut down
MILLIAMPS_PER_CHANNEL = 20    # one red, green or blue LED at full brightness
PRESS_TIMEOUT_MS = 10000      # how long we wait for you to press the button

problems = []

print("=" * 50)
print("Board / system info")
print("=" * 50)
u = os.uname()
print("release :", u.release)
print("machine :", u.machine)
print("platform:", sys.platform)
gc.collect()
free = gc.mem_free()
alloc = gc.mem_alloc()
print("RAM free : {} bytes ({:.1f} KB)".format(free, free / 1024))
print("RAM total: {} bytes ({:.1f} KB)".format(free + alloc, (free + alloc) / 1024))
try:
    fs = os.statvfs("/")
    print("Flash free: {:.1f} KB of {:.1f} KB".format(fs[0] * fs[3] / 1024, fs[0] * fs[2] / 1024))
except OSError as e:
    print("Flash info unavailable:", e)

print()
print("=" * 50)
print("config.py check")
print("=" * 50)
print("NEOPIXEL_PIN :", NEOPIXEL_PIN)
print("NUMBER_PIXELS:", NUMBER_PIXELS)
print("BUTTON_PIN   :", BUTTON_PIN)
print("BRIGHTNESS   :", BRIGHTNESS)
if NUMBER_PIXELS != EXPECTED_PIXELS:
    print("NOTE: this kit uses a {}-pixel strip, but NUMBER_PIXELS is {}.".format(EXPECTED_PIXELS, NUMBER_PIXELS))
    print("That is fine if you cut your strip to a different length.")
if not 0 < BRIGHTNESS <= MAX_SAFE_BRIGHTNESS:
    print("WARNING: BRIGHTNESS should be more than 0 and no more than {}.".format(MAX_SAFE_BRIGHTNESS))
    problems.append("BRIGHTNESS in config.py is outside the safe range")
# the worst case is every pixel showing full white (all three LEDs on)
worst_ma = NUMBER_PIXELS * 3 * MILLIAMPS_PER_CHANNEL * BRIGHTNESS
print("Worst-case strip current: about {:.0f} mA (every pixel white)".format(worst_ma))
print("Full brightness would be: about {:.0f} mA".format(NUMBER_PIXELS * 3 * MILLIAMPS_PER_CHANNEL))

print()
print("=" * 50)
print("Pin level check (internal pull-ups enabled)")
print("=" * 50)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
data_pin = Pin(NEOPIXEL_PIN, Pin.IN, Pin.PULL_UP)
sleep_ms(10)
button_level = button.value()
data_level = data_pin.value()
print("Button (GPIO{}) idle level: {} ({})".format(
    BUTTON_PIN, button_level,
    "1 = not pressed, as expected" if button_level == 1 else "0 = held down, or the wire is shorted to GND"))
print("Strip data (GPIO{}) idle level: {} ({})".format(
    NEOPIXEL_PIN, data_level,
    "1 = not shorted, as expected" if data_level == 1 else "0 = the data wire is touching GND"))
if button_level == 0:
    problems.append("the button reads pressed before you touched it")
if data_level == 0:
    problems.append("the strip data pin is shorted to GND")

print()
print("=" * 50)
print("Strip check (look at the strip now)")
print("=" * 50)
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
level = int(255 * BRIGHTNESS)
strip.fill((0, 0, 0))
strip[0] = (level, 0, 0)                        # first pixel red
strip[NUMBER_PIXELS // 2] = (0, level, 0)       # middle pixel green
strip[NUMBER_PIXELS - 1] = (0, 0, level)        # last pixel blue
strip.write()
print("Pixel 0 should be RED, pixel {} GREEN and pixel {} BLUE.".format(NUMBER_PIXELS // 2, NUMBER_PIXELS - 1))
print("If nothing lights, check the arrow on the strip: data must go IN at DIN.")
print("If only the first part lights, a solder joint or cut point is broken there.")

print()
print("=" * 50)
print("Button press check")
print("=" * 50)
print("Press the button now (you have {} seconds)...".format(PRESS_TIMEOUT_MS // 1000))
start = ticks_ms()
pressed = False
while ticks_diff(ticks_ms(), start) < PRESS_TIMEOUT_MS:
    if button.value() == 0:
        pressed = True
        break
    sleep_ms(10)
if pressed:
    print("Button press seen after {:.1f} seconds.".format(ticks_diff(ticks_ms(), start) / 1000))
    # flash the whole strip orange to say thank you
    strip.fill((level, level // 3, 0))
    strip.write()
    sleep(0.5)
else:
    print("No press seen. Check that the button goes from GPIO{} to a GND pin.".format(BUTTON_PIN))
    problems.append("no button press was seen")

strip.fill((0, 0, 0))
strip.write()

print()
if problems:
    print("TEST FAIL - fix these and run the probe again:")
    for problem in problems:
        print("  -", problem)
else:
    print("TEST PASS - config.py, the button and the strip pins look right")
    print("(check with your eyes that the three test pixels lit up)")
