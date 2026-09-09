# Press Button 1 to move forward through a list of colors.
# Press Button 2 to move backward through the list.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

# A small list of colors to cycle through.
colors = [
    (255, 0, 0),     # red
    (255, 80, 0),    # orange
    (255, 255, 0),   # yellow
    (0, 255, 0),     # green
    (0, 0, 255),     # blue
    (130, 0, 200),   # purple
]
color_index = 0

DEBOUNCE_MS = 200   # ignore extra presses for 200 ms after each one
last_press = 0


def fill_strip(color):
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()


def button_handler(pin):
    # this runs the instant a button is pressed, even while the
    # rest of the program is doing something else
    global color_index, last_press
    now = ticks_ms()
    if now - last_press < DEBOUNCE_MS:
        return   # too soon - probably the same press bouncing, ignore it
    last_press = now

    # pin tells us which button object triggered the interrupt
    if pin == button1:
        color_index = (color_index + 1) % len(colors)
    else:
        color_index = (color_index - 1) % len(colors)

    fill_strip(colors[color_index])
    print("color index:", color_index)


button1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

fill_strip(colors[color_index])   # show the first color right away

while True:
    # the buttons do all the work through interrupts, so the main
    # loop just needs to stay alive
    sleep(1)
