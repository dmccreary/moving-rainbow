# Setup - run once
from machine import Pin # Get the Pin function from the machine module.
from time import sleep # Get the sleep library from the time module.
from neopixel import NeoPixel

# read the hardware config file
import config
NUMBER_PIXELS = config.NUMBER_PIXELS
STRIP0_PIN = config.STRIP0_PIN
STRIP1_PIN = config.STRIP1_PIN
STRIP2_PIN = config.STRIP2_PIN

# This is the built-in green LED on the Pico.
BUILT_IN_LED_PIN = 25
# change this to the following named pin on the "W"
# BUILT_IN_LED_PIN = Pin("LED", Pin.OUT)

# The line below indicates we are configuring this as an output (not input)
led = machine.Pin(BUILT_IN_LED_PIN, machine.Pin.OUT)
strip0 =  NeoPixel(machine.Pin(STRIP0_PIN), NUMBER_PIXELS)
strip1 =  NeoPixel(machine.Pin(STRIP1_PIN), NUMBER_PIXELS)
strip2 =  NeoPixel(machine.Pin(STRIP2_PIN), NUMBER_PIXELS)

brightness = 255
red = (brightness, 0, 0)
green = (0, brightness, 0)
blue = (0, 0, brightness)
off = (0,0,0)

def set(i, color):
    strip0[i] = color
    strip1[i] = color
    strip2[i] = color

def write():
    strip0.write()
    strip1.write()
    strip2.write()

while True:
    set(0, red)
    write()
    sleep(.5)
    set(0, off)
    write()
    sleep(.5)
    led.toggle() # toggle the LED

