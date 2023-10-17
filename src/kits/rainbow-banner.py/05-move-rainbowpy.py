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

def draw_colors(start, bandLength):
    wheel_step = int(255/bandLength)
    for i in range(start, start+bandLength):
        set(i, wheel(int(i*wheel_step % 255)))
            
BAND_LENGTH = 10

while True:
    for i in range(0, NUMBER_PIXELS - BAND_LENGTH):
        draw_colors(i, BAND_LENGTH)
        write()
        sleep(.03)
        for j in range(0, BAND_LENGTH):
            set(i+j, off)
          
    led.toggle() # toggle the LED

