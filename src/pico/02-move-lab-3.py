from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Create a varuabke to store the delay 
delay = .01
while True:
    # move down
    for i in range(0, NUMBER_PIXELS - 1):
        strip[i] = (255,0,0)
        strip.write()
        sleep(delay)
        strip[i] = (0,0,0)
    
    # move back
    for i in range(NUMBER_PIXELS - 1, 0, -1):
        # turn index red pixel on for and delay
        strip[i] = (255,0,0)
        strip.write()
        sleep(delay)
        strip[i] = (0,0,0)