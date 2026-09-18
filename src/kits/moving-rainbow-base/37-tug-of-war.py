# Two-player tug of war! Button 1 pulls the marker toward the high end.
# Button 2 pulls it toward the low end. First to reach their end wins!
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

LAST_PIXEL = config.NUMBER_PIXELS - 1
position = config.NUMBER_PIXELS // 2   # marker starts in the middle

DEBOUNCE_MS = 120
last_press = 0
game_over = False


def draw_marker():
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip[position] = (200, 0, 200)
    strip.write()


def button_handler(pin):
    global position, last_press, game_over
    if game_over:
        return
    now = ticks_ms()
    if now - last_press < DEBOUNCE_MS:
        return
    last_press = now

    if pin == button1:
        position += 1   # Player 1 pulls toward the high end
    else:
        position -= 1   # Player 2 pulls toward the low end

    draw_marker()

    if position >= LAST_PIXEL:
        print("Player 1 wins!")
        game_over = True
    elif position <= 0:
        print("Player 2 wins!")
        game_over = True


button1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

draw_marker()

while True:
    if game_over:
        # flash the winning end of the strip
        winner_pixel = LAST_PIXEL if position >= LAST_PIXEL else 0
        strip[winner_pixel] = (255, 255, 0)
        strip.write()
        sleep(0.2)
        strip[winner_pixel] = (0, 0, 0)
        strip.write()
        sleep(0.2)
    else:
        sleep(0.05)
