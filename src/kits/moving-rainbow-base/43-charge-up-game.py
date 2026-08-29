# Hold Button 1 to fill the strip. Try to release exactly when the bar
# reaches the target zone (marked in blue) to win!
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms, ticks_diff
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)

FILL_SECONDS = 3.0     # time it takes to fill the whole strip
TARGET_START = config.NUMBER_PIXELS - 10
TARGET_END = config.NUMBER_PIXELS - 6


def draw_bar(lit_count):
    for i in range(config.NUMBER_PIXELS):
        in_target = TARGET_START <= i <= TARGET_END
        if i < lit_count:
            strip[i] = (255, 255, 0) if in_target else (0, 120, 0)
        else:
            strip[i] = (0, 0, 150) if in_target else (0, 0, 0)
    strip.write()


def flash(color, times=3):
    for _ in range(times):
        for i in range(config.NUMBER_PIXELS):
            strip[i] = color
        strip.write()
        sleep(0.15)
        for i in range(config.NUMBER_PIXELS):
            strip[i] = (0, 0, 0)
        strip.write()
        sleep(0.15)


draw_bar(0)

while True:
    # wait here until the button is pressed
    while button1.value() == 1:
        sleep(0.01)
    press_time = ticks_ms()

    # while the button stays down, grow the bar
    lit_count = 0
    while button1.value() == 0:
        held_seconds = ticks_diff(ticks_ms(), press_time) / 1000
        lit_count = min(config.NUMBER_PIXELS,
                         int((held_seconds / FILL_SECONDS) * config.NUMBER_PIXELS))
        draw_bar(lit_count)
        sleep(0.02)

    # the button was released - check the result
    if TARGET_START <= lit_count <= TARGET_END:
        print("You win! Released at pixel", lit_count)
        flash((0, 200, 0))
    else:
        print("Try again! Released at pixel", lit_count)
        flash((200, 0, 0))

    draw_bar(0)
    sleep(0.5)
