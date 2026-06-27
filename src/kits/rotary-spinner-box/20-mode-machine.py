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
#       Mode 0  Knob Dot       -> knob moves a single pixel along the strip
#       Mode 1  Solid Color    -> knob changes the color
#       Mode 2  Scanner        -> knob changes the speed
#       Mode 3  Comet          -> knob changes the tail length
#       Mode 4  Moving Rainbow -> knob changes the speed
#
# Mode 0 (Knob Dot) is the default you see at power-up: turn the knob and a
# single bright pixel moves up and down the strip, following the knob directly.
#
# This is a straight 12-pixel strip (not a ring), so the moving patterns
# (Scanner and Comet) bounce back and forth between the two ends instead of
# wrapping around.
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
# Boot-safe startup window
# ---------------------------------------------------------------------------
# When this program runs as main.py it starts automatically on power-up. This
# short countdown gives you a few seconds to STOP the program (press Ctrl-C, or
# the Stop button in Thonny) before it takes over the buttons and knob - handy
# when you want to upload new code or run a different lab.  The strip lights one
# dim white pixel per remaining second as a visual cue on the box itself.
BOOT_DELAY_SECONDS = 3
for remaining in range(BOOT_DELAY_SECONDS, 0, -1):
    print('Starting mode machine in', remaining, '... (press Ctrl-C to stop)')
    for i in range(N):
        strip[i] = (3, 3, 3) if i < remaining else (0, 0, 0)
    strip.write()
    utime.sleep(1)

# clear the countdown pixels before the program begins
for i in range(N):
    strip[i] = (0, 0, 0)
strip.write()

# ---------------------------------------------------------------------------
# Modes and their parameters
# ---------------------------------------------------------------------------
MODE_NAMES = ['Knob Dot', 'Solid Color', 'Scanner', 'Comet', 'Moving Rainbow']
NUM_MODES = len(MODE_NAMES)

mode = 0          # which mode is showing now (0 = Knob Dot, the default)
mode_changed = True   # set True so we draw and announce the first mode

# Each mode stores one parameter value in this list
#         Knob pos, Solid hue, Scanner speed, Comet tail, Rainbow speed
params = [N // 2,   0,         10,            5,          10]

# The smallest and largest each parameter is allowed to be
PARAM_MIN = [0,     0,   1,  1,     1]
PARAM_MAX = [N - 1, 255, 20, N - 1, 20]

# How much one click of the knob changes each parameter
PARAM_STEP = [1,    8,   1,  1,     1]


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


# Turn a forever-growing step counter into a position that bounces back and
# forth along the strip (0, 1, ... N-1, N-2, ... 1, 0, 1, ...).  This is how
# the moving patterns travel on a strip instead of wrapping like a ring.
# Returns (position, direction) where direction is +1 going up, -1 coming back.
def bounce(step):
    period = 2 * (N - 1)        # one full there-and-back trip
    phase = step % period
    if phase < N:
        return phase, 1
    else:
        return period - phase, -1


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
        # Knob Dot: the knob moves a single bright pixel along the strip.
        # params[0] IS the pixel position, so there is no animation - the dot
        # only moves when you turn the knob.  This is the default mode.
        for i in range(N):
            strip[i] = (0, 0, 0)
        strip[params[0]] = (0, 90, 110)

    elif mode == 1:
        # Solid Color: the whole strip is one color from the wheel
        color = color_wheel(params[1])
        for i in range(N):
            strip[i] = color

    elif mode == 2:
        # Scanner: one bright dot bounces back and forth along the strip
        position, _ = bounce(step)
        for i in range(N):
            strip[i] = (0, 0, 0)
        strip[position] = (0, 60, 80)

    elif mode == 3:
        # Comet: a head with a fading tail; params[3] is the tail length.
        # The tail trails behind the head in whichever direction it is moving.
        head, direction = bounce(step)
        tail = params[3]
        for i in range(N):
            behind = (head - i) * direction
            if 0 <= behind < tail:
                fade = (tail - behind) / tail
                strip[i] = (0, int(80 * fade), int(120 * fade))
            else:
                strip[i] = (0, 0, 0)

    elif mode == 4:
        # Moving Rainbow: a rainbow that scrolls along the strip like a marquee
        offset = (step * 4) % 256
        for i in range(N):
            strip[i] = color_wheel(int(i * 256 / N) + offset)

    strip.write()


# How fast each mode animates (milliseconds between steps).
# For Scanner and Rainbow the speed parameter makes this smaller (faster).
def frame_delay():
    if mode == 2:
        return 320 - params[2] * 15
    elif mode == 4:
        return 130 - params[4] * 5
    else:
        return 80   # Knob Dot, Solid, and Comet animate at a steady rate


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
        if mode == 1:
            # Solid Color: the hue wraps around the color wheel
            params[mode] = new_value % 256
        else:
            # every other parameter - including the Knob Dot position - stops
            # at its limits instead of wrapping
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
