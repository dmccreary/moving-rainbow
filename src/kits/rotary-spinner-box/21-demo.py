# Rotary Spinner Box - Capability Demo
# Filename: 21-demo.py
#
# A "show everything" demo built for science fairs, STEM nights, and teacher
# training tables.  Someone picks up the box, spins the knob, and INSTANTLY
# sees something change - that is the hook.
#
#   * The BUTTONS choose which pattern (mode) is showing.
#       BUTTON 1 (pin 14) = next pattern
#       BUTTON 2 (pin 15) = previous pattern
#
#   * The ROTARY KNOB changes one thing in EVERY pattern, so spinning it always
#     does something you can see:
#       Mode 0  Knob Dot        -> moves a single pixel along the strip
#       Mode 1  Bar / Level      -> how many pixels are lit (like a volume knob)
#       Mode 2  Solid Color      -> the color of the whole strip
#       Mode 3  Larson Scanner   -> the color of the sweeping eye
#       Mode 4  Comet            -> the length of the glowing tail
#       Mode 5  Theater Chase    -> the spacing between the lit "bulbs"
#       Mode 6  Sparkle          -> how many sparkles twinkle at once
#       Mode 7  Candle Flicker   -> how bright the flame is
#       Mode 8  Rainbow          -> rotates the whole rainbow
#
# This is a straight 12-pixel strip (not a ring), so moving patterns bounce
# back and forth between the ends instead of wrapping around.
#
# Two big ideas make this work:
#   1. The buttons use INTERRUPTS, so a press is noticed instantly.
#   2. The animation uses a TIMER (ticks_ms) instead of sleep(), so the main
#      loop can keep checking the knob while the pattern keeps moving.

from neopixel import NeoPixel
import utime
import machine
import random
from machine import Pin

import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
N = config.NUMBER_PIXELS

# ---------------------------------------------------------------------------
# Boot-safe startup window
# ---------------------------------------------------------------------------
# Gives you a few seconds to STOP the program (Ctrl-C, or the Stop button in
# Thonny) before it takes over the buttons and knob.  The strip lights one dim
# white pixel per remaining second as a visual cue on the box itself.
BOOT_DELAY_SECONDS = 3
for remaining in range(BOOT_DELAY_SECONDS, 0, -1):
    print('Starting demo in', remaining, '... (press Ctrl-C to stop)')
    for i in range(N):
        strip[i] = (3, 3, 3) if i < remaining else (0, 0, 0)
    strip.write()
    utime.sleep(1)

for i in range(N):
    strip[i] = (0, 0, 0)
strip.write()

# ---------------------------------------------------------------------------
# Modes and their parameters
# ---------------------------------------------------------------------------
MODE_NAMES = ['Knob Dot', 'Bar / Level', 'Solid Color', 'Larson Scanner',
              'Comet', 'Theater Chase', 'Sparkle', 'Candle Flicker', 'Rainbow']
NUM_MODES = len(MODE_NAMES)

mode = 0          # which mode is showing now (0 = Knob Dot, the default)
mode_changed = True   # set True so we draw and announce the first mode

# Each mode stores one parameter value that the knob changes.
#         KnobDot Bar  Solid Scanner Comet Theater Sparkle Candle Rainbow
params =   [N // 2, N // 2, 0,    0,      5,    3,      5,      20,    0]
PARAM_MIN = [0,     0,      0,    0,      1,    2,      1,      3,     0]
PARAM_MAX = [N - 1, N,      255,  255,    N - 1, 6,     N,      40,    255]
PARAM_STEP = [1,    1,      8,    8,      1,    1,      1,      2,     8]
# Wrapping parameters roll over (colors); the rest stop at their limits.
WRAP =      [False, False,  True, True,   False, False, False,  False, True]

# How many milliseconds between animation frames in each mode
FRAME_MS = [80, 80, 80, 60, 60, 90, 60, 70, 80]


# ---------------------------------------------------------------------------
# Color helpers
# ---------------------------------------------------------------------------
# The color wheel: position 0-255 in, an (r,g,b) color out.
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


# Multiply an (r,g,b) color by a fraction (0.0 - 1.0) to dim it.
def scale(color, frac):
    return (int(color[0] * frac), int(color[1] * frac), int(color[2] * frac))


# A random color that is VIVID and easy to tell apart from other random colors.
# Trick: pick a random HUE and run it through the color wheel.  Random RGB
# (three random channels) makes muddy, similar-looking colors instead.
def random_vivid_hue():
    return random.randint(0, 255)


def clear():
    for i in range(N):
        strip[i] = (0, 0, 0)


# Turn a forever-growing step counter into a position that bounces back and
# forth along the strip (0, 1, ... N-1, N-2, ... 1, 0, 1, ...).
# Returns (position, direction): direction is +1 going up, -1 coming back.
def bounce(step):
    period = 2 * (N - 1)
    phase = step % period
    if phase < N:
        return phase, 1
    else:
        return period - phase, -1


# ---------------------------------------------------------------------------
# State for the random patterns (Sparkle), kept between frames
# ---------------------------------------------------------------------------
sparkle_hue = [0] * N    # the hue of each pixel's sparkle
sparkle_life = [0] * N   # how much life (0-100) each sparkle has left


def reset_sparkles():
    for i in range(N):
        sparkle_life[i] = 0


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
        for i in range(N):
            strip[i] = (0, 0, 0)
        strip[params[0]] = (0, 90, 110)

    elif mode == 1:
        # Bar / Level: params[1] pixels are lit from one end, like a volume
        # meter, colored green at the bottom fading to red at the top.
        level = params[1]
        for i in range(N):
            if i < level:
                ratio = i / (N - 1)
                strip[i] = (int(80 * ratio), int(80 * (1 - ratio)), 0)
            else:
                strip[i] = (0, 0, 0)

    elif mode == 2:
        # Solid Color: the whole strip is one color from the wheel.
        color = color_wheel(params[2])
        for i in range(N):
            strip[i] = color

    elif mode == 3:
        # Larson Scanner: a glowing "eye" sweeps back and forth.  The knob sets
        # the eye color.  Pixels near the eye are bright and fade with distance.
        position, _ = bounce(step)
        eye = scale(color_wheel(params[3]), 0.8)
        width = 3
        for i in range(N):
            distance = abs(i - position)
            if distance < width:
                strip[i] = scale(eye, 1 - distance / width)
            else:
                strip[i] = (0, 0, 0)

    elif mode == 4:
        # Comet: a head with a fading tail; params[4] is the tail length.
        head, direction = bounce(step)
        tail = params[4]
        for i in range(N):
            behind = (head - i) * direction
            if 0 <= behind < tail:
                fade = (tail - behind) / tail
                strip[i] = (0, int(80 * fade), int(120 * fade))
            else:
                strip[i] = (0, 0, 0)

    elif mode == 5:
        # Theater Chase: every params[5]-th pixel is lit, and the pattern
        # marches one pixel each frame, like a marquee sign.
        spacing = params[5]
        phase = step % spacing
        for i in range(N):
            if (i - phase) % spacing == 0:
                strip[i] = (60, 50, 25)   # warm white "bulb"
            else:
                strip[i] = (0, 0, 0)

    elif mode == 6:
        # Sparkle: random pixels twinkle in vivid, distinct colors.  params[6]
        # sets how many sparkles are alive at once.
        density = params[6]
        # fade every active sparkle a little
        for i in range(N):
            if sparkle_life[i] > 0:
                sparkle_life[i] = max(0, sparkle_life[i] - 12)
        # spawn new sparkles on dark pixels until we reach the density
        active = 0
        for i in range(N):
            if sparkle_life[i] > 0:
                active += 1
        attempts = 0
        while active < density and attempts < 2 * N:
            p = random.randint(0, N - 1)
            if sparkle_life[p] == 0:
                sparkle_hue[p] = random_vivid_hue()
                sparkle_life[p] = 100
                active += 1
            attempts += 1
        # draw
        for i in range(N):
            if sparkle_life[i] > 0:
                strip[i] = scale(color_wheel(sparkle_hue[i]), sparkle_life[i] / 100)
            else:
                strip[i] = (0, 0, 0)

    elif mode == 7:
        # Candle Flicker: a warm amber glow that flickers like a real flame.
        # params[7] sets the base brightness.
        base = params[7]
        for i in range(N):
            flick = random.randint(0, 8)
            level = base + flick
            strip[i] = (level, int(level * 0.4), 0)   # warm orange

    elif mode == 8:
        # Rainbow: a full rainbow across the strip.  The knob (params[8])
        # rotates it - spin to slide the colors along.
        offset = params[8]
        for i in range(N):
            strip[i] = color_wheel(int(i * 256 / N) + offset)

    strip.write()


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
step = 0
last_frame = utime.ticks_ms()

print('Capability Demo ready.  Spin the knob - something changes in every mode!')
print('BUTTON 1 = next pattern, BUTTON 2 = previous pattern.')

while True:
    # 1. Announce and reset when the mode changes
    if mode_changed:
        mode_changed = False
        step = 0
        clear()
        reset_sparkles()
        print('Mode', mode, '-', MODE_NAMES[mode], '| knob value =', params[mode])
        draw(step)
        last_frame = utime.ticks_ms()

    # 2. Check the knob every loop so we never miss a click
    turn = read_knob()
    if turn != 0:
        if WRAP[mode]:
            params[mode] = (params[mode] + turn * PARAM_STEP[mode]) % 256
        else:
            new_value = params[mode] + turn * PARAM_STEP[mode]
            if new_value < PARAM_MIN[mode]:
                new_value = PARAM_MIN[mode]
            if new_value > PARAM_MAX[mode]:
                new_value = PARAM_MAX[mode]
            params[mode] = new_value
        print(MODE_NAMES[mode], 'knob value =', params[mode])
        draw(step)   # show the change right away

    # 3. Advance the animation when enough time has passed
    now = utime.ticks_ms()
    if utime.ticks_diff(now, last_frame) >= FRAME_MS[mode]:
        step += 1
        draw(step)
        last_frame = now
