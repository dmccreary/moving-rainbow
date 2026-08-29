# Button 1 speeds up a moving pixel. Button 2 slows it down.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

delay = 0.1          # seconds between moves - this is our "speed"
MIN_DELAY = 0.01     # fastest we will allow (too fast looks like a blur)
MAX_DELAY = 0.5      # slowest we will allow

DEBOUNCE_MS = 200
last_press = 0


def button_handler(pin):
    global delay, last_press
    now = ticks_ms()
    if now - last_press < DEBOUNCE_MS:
        return   # too soon - probably the same press bouncing, ignore it
    last_press = now

    if pin == button1:
        delay = max(MIN_DELAY, delay - 0.02)   # speed up, but not too fast
    else:
        delay = min(MAX_DELAY, delay + 0.02)   # slow down, but not too slow

    print("delay:", delay)


button1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

position = 0
while True:
    strip[position] = (0, 0, 0)                    # erase the old spot
    position = (position + 1) % config.NUMBER_PIXELS
    strip[position] = (0, 120, 255)                 # light the new spot
    strip.write()
    sleep(delay)   # delay can change any time a button interrupt fires
