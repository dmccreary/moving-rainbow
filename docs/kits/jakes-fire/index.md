# Jakes Fire

<iframe width="560" height="315" src="https://www.youtube.com/embed/NRp6oRsooYY?si=jy_51_P1w6Z3De7N" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Requirements

    Hey, Dan!

    I'm starting a project, and would love your help with it, if you have the time. 

    I'm in need of a small, color-changing campfire that I can set on top of a wooden table- I was thinking about doing something with programmable RGB LEDs. Probably some actual wooden sticks, semi-transparent cellophane, and a bunch of hot glue to make the structure. 

    What I really need help with is getting the lighting controls settled and potentially incorporating some flickering effects.

    Let me know what you think, and if you can help! 

    Thanks! - Jake

In further discussions, we found it would be useful to change the patterns
for different versions of the game.

## Design

I used two NeoPixel rings.  The outer one had 24 pixels and the inner ring had 12 pixels.

## Sample Code

```py
# Simple Fire Effect for Pattern Integration
# Can be easily added to your main-demo-cycle.py
from machine import Pin, ADC
from neopixel import NeoPixel
from utime import sleep
from urandom import randint

import dual_ring_config

pot = ADC(dual_ring_config.POT_PIN)

NUMBER_PIXELS0 = dual_ring_config.NUMBER_PIXELS0
NUMBER_PIXELS1 = dual_ring_config.NUMBER_PIXELS1

# 24 pixels
strip0 = NeoPixel(Pin(dual_ring_config.NEOPIXEL_PIN0), NUMBER_PIXELS0)
# 12 pixels
strip1 = NeoPixel(Pin(dual_ring_config.NEOPIXEL_PIN1), NUMBER_PIXELS1)

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

def standard_fire(delay):
    for i in range(0, NUMBER_PIXELS0):
         green = 50 + randint(0,155)
         red = green + randint(25,50)
         strip0[randint(0,NUMBER_PIXELS0 - 1)] = (red, green, 0)
    strip0.write()
    for i in range(0, NUMBER_PIXELS1):
         green = 50 + randint(0,155)
         red = green + randint(25,50)
         strip1[randint(0,NUMBER_PIXELS1 - 1)] = (red, green, 0)
    strip1.write()
    sleep(delay)

def simulate_fire_pattern(pattern_number, delay):
    
    # TODO: Check that the pattern number is in the range of 0 to 7
    
    if (pattern_number == 0):
        standard_fire(delay)
    else:
        color_1 = (wheel(pattern_number * 16 + randint(0,16) % 255))
        color_2 = wheel((pattern_number * 16 + 128 + randint(0,16) % 256))
        for i in range(NUMBER_PIXELS0):
            strip0[i] = (color_1)
        strip0.write()
        for i in range(NUMBER_PIXELS1):
            strip1[i] = (color_2)
        strip1.write()
        sleep(delay)

# Erase all the pixels
def clear():
    for i in range(NUMBER_PIXELS0):
        strip0[i] = (0, 0, 0)
    strip0.write()
    for i in range(NUMBER_PIXELS1):
        strip1[i] = (0, 0, 0)
    strip1.write()

# Run the effect
try:
    print("Fire effect running - Press Ctrl+C to stop")
    while True:
        # shift over 13 bits to get a value from 0 to 7
        pattern = pot.read_u16() >> 13
        print(pattern, end=" ")
        simulate_fire_pattern(pattern, 0.1)
except KeyboardInterrupt:
    print("\nStopping fire effect")
    clear()
```

You can find the full source code and some unit tests here:


