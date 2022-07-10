from machine import ADC, Pin, PWM
from utime import sleep
from neopixel import NeoPixel

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Pins
POT_PIN = 26

pot = ADC(POT_PIN)

POLL_DELAY = .1 # poll the pot after this delay in seconds

# repeat forever
while True:
    pot_value = pot.read_u16() # read the value from the pot
    # this shifts the data right 8 bits and subtracts 1
    scaled_value = (pot_value >> 8) - 1
    # same as shift right 8 bits
    print("scaled value:", scaled_value)
    for i in range(NUMBER_PIXELS):
        strip[i] = (scaled_value, scaled_value, scaled_value)
        strip.write()
    sleep(POLL_DELAY)
