# Lab 25: Prize Wheel
# Filename: 25-prize-wheel.py
# Version: 1.0.0
#
# Press either button to spin the wheel. The white pointer starts fast,
# friction slows it down and it stops on a colored wedge, which flashes.
# Every step the speed is multiplied by a number just below 1, which is
# what makes the pointer slow down so gently. The program can be "waiting",
# "spinning" or "won". That word is called its state.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms, ticks_diff
from urandom import randint
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BUTTON_PIN_1 = config.BUTTON_PIN_1
BUTTON_PIN_2 = config.BUTTON_PIN_2
BRIGHTNESS = config.BRIGHTNESS
TOP_PIXEL = config.TOP_PIXEL

DELAY = 0.03             # seconds between steps
DEBOUNCE_MS = 250        # ignore extra presses closer together than this
FRICTION = 0.985         # each step the pointer keeps this much of its speed
STOP_SPEED = 0.04        # the pointer stops when it is slower than this
WIN_STEPS = 70           # how many steps the winning wedge flashes
WEDGE_DIM = 0.12         # how bright the wedges are while waiting

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

white = (255, 255, 255)
# each wedge is a name and a color. 24 pixels share out evenly to 6 wedges.
wedges = (('red', (255, 0, 0)),
          ('orange', (255, 60, 0)),
          ('yellow', (255, 150, 0)),
          ('green', (0, 255, 0)),
          ('blue', (0, 0, 255)),
          ('violet', (138, 43, 226)))
WEDGE_SIZE = NUMBER_PIXELS // len(wedges)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# turn a position counted clockwise from the top into a pixel number
def pixel_at(position):
    return (TOP_PIXEL + position) % NUMBER_PIXELS

def draw_wedges():
    for position in range(NUMBER_PIXELS):
        name, color = wedges[position // WEDGE_SIZE]
        strip[pixel_at(position)] = fade(color, WEDGE_DIM)

spin_requested = False
last_press = 0

# this function runs by itself the moment either button is pressed
def button_pressed(pin):
    global spin_requested, last_press
    now = ticks_ms()
    # a button "bounces" and can look like many presses, so we ignore
    # any press that comes too soon after the last one
    if ticks_diff(now, last_press) > DEBOUNCE_MS:
        spin_requested = True
        last_press = now

# call button_pressed when a pin falls from 1 (released) to 0 (pressed)
button1.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)

print('Press a button to spin the wheel!')
state = 'waiting'
pointer = 0.0            # the pointer's position, counted from the top
speed = 0.0              # how many pixels the pointer moves each step
win_step = 0
while True:
    if state == 'waiting':
        draw_wedges()
        strip[pixel_at(int(pointer))] = fade(white, 1)
        if spin_requested:
            spin_requested = False
            # a random speed means a random stopping place
            speed = randint(70, 130) / 100
            state = 'spinning'
    elif state == 'spinning':
        draw_wedges()
        strip[pixel_at(int(pointer))] = fade(white, 1)
        pointer = (pointer + speed) % NUMBER_PIXELS
        speed = speed * FRICTION
        if speed < STOP_SPEED:
            name, color = wedges[int(pointer) // WEDGE_SIZE]
            print('You won', name)
            win_step = 0
            state = 'won'
    elif state == 'won':
        winner = int(pointer) // WEDGE_SIZE
        name, color = wedges[winner]
        strip.fill((0, 0, 0))
        # flash the winning wedge: 8 steps on, 8 steps off
        if (win_step // 8) % 2 == 0:
            for position in range(winner * WEDGE_SIZE, (winner + 1) * WEDGE_SIZE):
                strip[pixel_at(position)] = fade(color, 1)
        strip[pixel_at(int(pointer))] = fade(white, 1)
        win_step += 1
        if win_step >= WIN_STEPS:
            spin_requested = False   # ignore any presses during the flashing
            state = 'waiting'
    strip.write()
    sleep(DELAY)
