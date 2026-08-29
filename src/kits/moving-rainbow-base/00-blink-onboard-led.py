# Use this program to test that your Pico is connected to Thonny and
# running MicroPython. No wiring needed - this uses the LED already
# built onto the Pico board.
from machine import Pin
from utime import sleep

BUILT_IN_LED_PIN = 25    # every Pico has an LED wired to this pin
BLINK_DELAY = 0.25       # seconds the LED stays on or off - change me!

led = Pin(BUILT_IN_LED_PIN, Pin.OUT)

while True:
    led.toggle()          # switch the LED on if it's off, or off if it's on
    sleep(BLINK_DELAY)
