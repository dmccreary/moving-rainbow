# Rotary Spinner Box - Mode Machine (Capstone)
# Filename: 20-mode-machine.py
#
# This program brings everything together into one "mode machine":
#
#   * The BUTTONS choose which pattern (mode) is showing.
#       BUTTON 1 (pin 14) = next mode
#       BUTTON 2 (pin 15) = previous mode
#
#   * The ROTARY KNOB adjusts a parameter for whichever mode is showing.
#       Mode 0  Solid Color    -> knob changes the color
#       Mode 1  Spinner        -> knob changes the speed
#       Mode 2  Comet          -> knob changes the tail length
#       Mode 3  Moving Rainbow -> knob changes the speed
#
# Each mode remembers its own parameter, so when you come back to a mode it
# looks the way you left it.
#
# Two big ideas make this work:
#   1. The buttons use INTERRUPTS, so a press is noticed instantly.
#   2. The animation uses a TIMER (ticks_ms) instead of sleep(), so the main
#      loop can keep checking the knob while the pattern keeps moving.

from neopixel import NeoPixel
import utime
import machine
from machine import Pin

import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
N = config.NUMBER_PIXELS

# ---------------------------------------------------------------------------
# Modes and their parameters
# ---------------------------------------------------------------------------
MODE_NAMES = ['Solid Color', 'Spinner', 'Comet', 'Moving Rainbow']
NUM_MODES = len(MODE_NAMES)

mode = 0          # which mode is showing now
mode_changed = True   # set True so we draw and announce the first mode

# Each mode stores one parameter value in this list
#         Solid hue, Spinner speed, Comet tail, Rainbow speed
params = [0,         10,            5,          10]

# The smallest and largest each parameter is allowed to be
PARAM_MIN = [0,   1,  1,  1]
PARAM_MAX = [255, 20, N - 1, 20]

# How much one click of the knob changes each parameter
PARAM_STEP = [8, 1, 1, 1]


# ---------------------------------------------------------------------------
# The color wheel: position 0-255 in, an (r,g,b) color out
# ---------------------------------------------------------------------------
def color_wheel(pos):
    pos = pos % 256
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)


def clear():
    for i in range(N):
        strip[i] = (0, 0, 0)


# ---------------------------------------------------------------------------
# Buttons (interrupt driven) choose the mode
# ---------------------------------------------------------------------------
last_button_time = 0
button_next = machine.Pin(config.PUSH_BUTTON_PIN_1, machine.Pin.IN, machine.Pin.PULL_UP)
button_prev = machine.Pin(config.PUSH_BUTTON_PIN_2, machine.Pin.IN, machine.Pin.PULL_UP)


def button_callback(pin):
    global mode, mode_changed, last_button_time
    new_time = utime.ticks_ms()
    if utime.ticks_diff(new_time, last_button_time) > 200:
        if pin is button_next:
            mode = (mode + 1) % NUM_MODES
        else:
            mode = (mode - 1) % NUM_MODES
        mode_changed = True
        last_button_time = new_time


button_next.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)
button_prev.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)

# ---------------------------------------------------------------------------
# Rotary encoder adjusts the current mode's parameter
# ---------------------------------------------------------------------------
clk = machine.Pin(config.ROTARY_ENCODER_PIN_A, machine.Pin.IN, machine.Pin.PULL_UP)
dt = machine.Pin(config.ROTARY_ENCODER_PIN_B, machine.Pin.IN, machine.Pin.PULL_UP)
last_clk = clk.value()


def read_knob():
    # Returns +1 for clockwise, -1 for counterclockwise, 0 for no change
    global last_clk
    current = clk.value()
    turn = 0
    if current != last_clk and current == 0:
        if dt.value() != current:
            turn = 1
        else:
            turn = -1
    last_clk = current
    return turn


# ---------------------------------------------------------------------------
# Drawing each mode.  "step" is a counter that grows as the animation runs.
# ---------------------------------------------------------------------------
def draw(step):
    if mode == 0:
        # Solid Color: the whole ring is one color from the wheel
        color = color_wheel(params[0])
        for i in range(N):
            strip[i] = color

    elif mode == 1:
        # Spinner: one bright dot travels around the ring
        position = step % N
        for i in range(N):
            strip[i] = (0, 0, 0)
        strip[position] = (0, 60, 80)

    elif mode == 2:
        # Comet: a head with a fading tail; params[2] is the tail length
        head = step % N
        tail = params[2]
        for i in range(N):
            distance = (head - i) % N
            if distance < tail:
                fade = (tail - distance) / tail
                strip[i] = (0, int(80 * fade), int(120 * fade))
            else:
                strip[i] = (0, 0, 0)

    elif mode == 3:
        # Moving Rainbow: a rainbow that slides around the ring
        offset = (step * 4) % 256
        for i in range(N):
            strip[i] = color_wheel(int(i * 256 / N) + offset)

    strip.write()


# How fast each mode animates (milliseconds between steps).
# For Spinner and Rainbow the speed parameter makes this smaller (faster).
def frame_delay():
    if mode == 1:
        return 320 - params[1] * 15
    elif mode == 3:
        return 130 - params[3] * 5
    else:
        return 80   # Solid and Comet animate at a steady rate


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
step = 0
last_frame = utime.ticks_ms()

print('Mode Machine ready.')
print('BUTTON 1 = next mode, BUTTON 2 = previous mode, knob = adjust parameter.')

while True:
    # 1. Announce and reset when the mode changes
    if mode_changed:
        mode_changed = False
        step = 0
        clear()
        print('Mode', mode, '-', MODE_NAMES[mode],
              '| parameter =', params[mode])
        draw(step)
        last_frame = utime.ticks_ms()

    # 2. Check the knob every loop so we never miss a click
    turn = read_knob()
    if turn != 0:
        new_value = params[mode] + turn * PARAM_STEP[mode]
        if mode == 0:
            # color wraps around the wheel
            params[mode] = new_value % 256
        else:
            # other parameters stop at their limits
            if new_value < PARAM_MIN[mode]:
                new_value = PARAM_MIN[mode]
            if new_value > PARAM_MAX[mode]:
                new_value = PARAM_MAX[mode]
            params[mode] = new_value
        print(MODE_NAMES[mode], 'parameter =', params[mode])
        draw(step)   # show the change right away

    # 3. Advance the animation when enough time has passed
    now = utime.ticks_ms()
    if utime.ticks_diff(now, last_frame) >= frame_delay():
        step += 1
        draw(step)
        last_frame = now
