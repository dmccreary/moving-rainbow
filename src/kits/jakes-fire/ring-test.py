# Simple Fire Effect for Pattern Integration
# Can be easily added to your main-demo-cycle.py
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint

import dual_ring_config

NUMBER_PIXELS0 = dual_ring_config.NUMBER_PIXELS0
NUMBER_PIXELS1 = dual_ring_config.NUMBER_PIXELS1

# 24 pixels
strip0 = NeoPixel(Pin(dual_ring_config.NEOPIXEL_PIN0), NUMBER_PIXELS0)
# 12 pixels
strip1 = NeoPixel(Pin(dual_ring_config.NEOPIXEL_PIN1), NUMBER_PIXELS1)

def main_test(delay):
    # main outer ring
    for i in range(NUMBER_PIXELS0):
        strip0[i] = (50, 50, 50)
    strip0.write()
    for i in range(NUMBER_PIXELS1):
        strip1[i] = (50, 50, 50)
    strip1.write()
    sleep(1)
    clear()
    sleep(1)
    
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
        main_test(0.02)
except KeyboardInterrupt:
    print("\nStopping fire effect")
    clear()
