# Rotary Spinner Box - Blink the Onboard LED
# Filename: 01-blink-internal-led.py
#
# The classic "hello world" of microcontrollers.  This blinks the tiny LED
# built into the Raspberry Pi Pico itself - no wiring and no NeoPixel strip
# needed.  It is the very first proof that your code is running on the board.
#
# The onboard LED is wired to GPIO pin 25 on the Pico.

import machine
from utime import sleep

# Set up the onboard LED pin as an output we can turn on and off
led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.value(1)    # turn the LED on
    sleep(0.5)      # wait half a second

    led.value(0)    # turn the LED off
    sleep(0.5)      # wait half a second
