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
NUMBER_PIXELS = 135

BUILT_IN_LED_PIN = 25 
led = machine.Pin(BUILT_IN_LED_PIN, machine.Pin.OUT)

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions"""
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)
    
# Create a variable to store the delay 
delay = .001
while True:
    for color in range(0, 255):
        # turn index red pixel on for a short delay
        for i in range(0, NUMBER_PIXELS-1):
            strip[i] = (wheel(color))
        strip.write()
    print('.', end='')
    sleep(.01)
    led.toggle()