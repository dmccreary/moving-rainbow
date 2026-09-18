# Reaction Duel! Wait for the strip to flash green, then be the first
# to press your button. Press too early and you lose!
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)


def fill_strip(color):
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()


def wait_for_release():
    # make sure both buttons are up before starting a new round
    while button1.value() == 0 or button2.value() == 0:
        sleep(0.01)


while True:
    wait_for_release()
    fill_strip((200, 0, 0))   # red = get ready
    print("Get ready...")

    wait_ms = randint(2000, 5000)   # random 2-5 second delay
    start_wait = ticks_ms()

    false_start = False
    while ticks_ms() - start_wait < wait_ms:
        if button1.value() == 0:
            print("Player 1 jumped early - Player 2 wins!")
            false_start = True
            break
        if button2.value() == 0:
            print("Player 2 jumped early - Player 1 wins!")
            false_start = True
            break
        sleep(0.005)

    if false_start:
        fill_strip((200, 0, 0))
        sleep(2)
        continue

    fill_strip((0, 200, 0))   # green = go!
    go_time = ticks_ms()
    print("GO!")

    winner = None
    while winner is None:
        if button1.value() == 0:
            winner = "Player 1"
        elif button2.value() == 0:
            winner = "Player 2"

    reaction_ms = ticks_ms() - go_time
    print(winner, "wins! Reaction time:", reaction_ms, "ms")
    fill_strip((0, 0, 200))
    sleep(2)
