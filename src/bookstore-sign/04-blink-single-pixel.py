from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
# B 0-19 (20)
# O 20- (14)
# O (14)
# K (14)
# S (16)
# T 95 (10)
# O (14)
# R
# E
# total number of pixels
NUMBER_PIXELS = 134

BUILT_IN_LED_PIN = 25 
led = machine.Pin(BUILT_IN_LED_PIN, machine.Pin.OUT)

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

i = NUMBER_PIXELS - 1

# Create a variable to store the delay 
delay = .25
while True:
    # turn it one
    strip[i] = (25,25,25)
    strip.write()
    sleep(delay)

    # turn off
    strip[i] = (0,0,0)
    strip.write()
    sleep(delay)
    
    print('.', end='')
    
    led.toggle()