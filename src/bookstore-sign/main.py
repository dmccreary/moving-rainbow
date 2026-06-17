# Bookstore Sign
# Filename: main.py - copy of pattern-mode-test.py
#
# Press BUTTON_1 to move to the next mode, BUTTON_2 to go to the previous one.
# The mode change uses the same interrupt + 200ms debounce technique as
# 01-test-buttons.py so a single press counts as a single press.
#
# Modes:
#   0 - AUTO-CYCLE: automatically steps through every pattern below,
#       spending 60 seconds on each one before moving to the next.
#   1 - Color Letters: each letter of BOOKSTORE a different rainbow color
#       (this is the same idea as 06-color-letter-test.py).
#   2 - Rainbow Flow: the full rainbow spectrum scrolls across the sign
#       (from tiki-bar-sign/06-rainbow-wipe.py).
#   3 - Rainbow Solid: the whole sign glows one color, slowly cycling
#       through the rainbow (from jason-sign/main.py mode 2).
#   4 - Color Sparkle: every pixel drifts through random colors
#       (from jason-sign/main.py mode 3).
#   5 - Color Wipe: the whole sign holds one bright color, then wipes to
#       the next (from tiki-bar-sign/04-named-colors.py).
#   6 - Comet: a bright dot races across leaving a fading tail
#       (from tiki-bar-sign/01-move-red.py).
#
# The pattern functions are written one "frame" at a time so the main loop
# stays responsive - that way a button press changes the mode almost instantly
# instead of waiting for a long animation to finish.

import machine
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms, ticks_diff
import random

import config

# ---------------------------------------------------------------------------
# Hardware setup
# ---------------------------------------------------------------------------
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# The on-board LED toggles on each mode change for visual feedback
builtin_led = machine.Pin(config.BUILT_IN_LED_PIN, Pin.OUT)

# Both buttons connect the pin to ground when pressed, so use PULL_UP
button_up = machine.Pin(config.BUTTON_PIN_1, machine.Pin.IN, machine.Pin.PULL_UP)
button_down = machine.Pin(config.BUTTON_PIN_2, machine.Pin.IN, machine.Pin.PULL_UP)

# How long to show each pattern when in auto-cycle mode (mode 0)
AUTO_CYCLE_MS = 60 * 1000   # 60 seconds per pattern

# ---------------------------------------------------------------------------
# Color helpers
# ---------------------------------------------------------------------------

def wheel(pos):
    """Map a value 0-255 to a rainbow color (red -> green -> blue -> red)."""
    pos = pos & 255
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def clear_strip():
    """Turn off all pixels."""
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()


# (letter, start, end, color) - end is inclusive, color is (R, G, B).
# Same left-to-right rainbow layout used in 06-color-letter-test.py.
LETTER_LAYOUT = [
    ('B',   0,  19, (255,   0,   0)),  # Red
    ('O',  20,  33, (255, 128,   0)),  # Orange
    ('O',  34,  47, (255, 255,   0)),  # Yellow
    ('K',  48,  61, (  0, 255,   0)),  # Green
    ('S',  62,  77, (  0, 255, 255)),  # Cyan
    ('T',  78,  87, (  0,   0, 255)),  # Blue
    ('O',  88, 101, (255,   0, 255)),  # Purple
    ('R', 102, 115, (255,  50,  50)),  # Pink
    ('E', 116, 133, (255, 255, 255)),  # White
]

# Bright colors the Color Wipe pattern steps through
WIPE_COLORS = [
    (255,   0,   0),  # Red
    (255,  80,   0),  # Orange
    (255, 255,   0),  # Yellow
    (  0, 255,   0),  # Green
    (  0, 255, 255),  # Cyan
    (  0,   0, 255),  # Blue
    (160,   0, 255),  # Purple
    (255,   0, 160),  # Pink
]

# ---------------------------------------------------------------------------
# Animation state (reset between mode changes by reset_pattern_state)
# ---------------------------------------------------------------------------
rainbow_offset = 0                                   # Rainbow Flow / Rainbow Solid
pixel_values = [0] * config.NUMBER_PIXELS            # Color Sparkle
wipe_index = 0                                       # Color Wipe - which color
wipe_frame = 0                                       # Color Wipe - frames held
comet_pos = 0                                        # Comet - dot position
comet_hue = 0                                        # Comet - dot color

WIPE_HOLD_FRAMES = 16   # at 0.05s/frame -> hold each wipe color ~0.8 seconds


def reset_pattern_state():
    """Reset all animation variables so each mode starts cleanly."""
    global rainbow_offset, wipe_index, wipe_frame, comet_pos, comet_hue
    rainbow_offset = 0
    wipe_index = 0
    wipe_frame = 0
    comet_pos = 0
    comet_hue = 0
    # Give the sparkle pattern a fresh random start
    for i in range(config.NUMBER_PIXELS):
        pixel_values[i] = random.randint(0, 255)


# ---------------------------------------------------------------------------
# Pattern step functions - each draws exactly ONE frame
# ---------------------------------------------------------------------------

def pattern_color_letters():
    """Each letter of BOOKSTORE shows its own color (static)."""
    for letter, start, end, color in LETTER_LAYOUT:
        for i in range(start, end + 1):
            strip[i] = color
    strip.write()


def pattern_rainbow_flow():
    """The full rainbow spectrum scrolls across the whole sign."""
    global rainbow_offset
    for i in range(config.NUMBER_PIXELS):
        wheel_pos = (i * 256 // config.NUMBER_PIXELS + rainbow_offset) & 255
        strip[i] = wheel(wheel_pos)
    strip.write()
    rainbow_offset = (rainbow_offset + 1) & 255


def pattern_rainbow_solid():
    """The whole sign glows one color, slowly cycling the rainbow."""
    global rainbow_offset
    color = wheel(rainbow_offset)
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()
    rainbow_offset = (rainbow_offset + 1) & 255


def pattern_color_sparkle():
    """Every pixel slowly drifts through random rainbow colors."""
    for i in range(config.NUMBER_PIXELS):
        pixel_values[i] = (pixel_values[i] + random.randint(1, 3)) & 255
        strip[i] = wheel(pixel_values[i])
    strip.write()


def pattern_color_wipe():
    """Hold one bright color across the sign, then wipe to the next."""
    global wipe_index, wipe_frame
    color = WIPE_COLORS[wipe_index]
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()
    wipe_frame += 1
    if wipe_frame >= WIPE_HOLD_FRAMES:
        wipe_frame = 0
        wipe_index = (wipe_index + 1) % len(WIPE_COLORS)


def pattern_comet():
    """A bright dot races across the sign leaving a fading tail."""
    global comet_pos, comet_hue
    # Dim every pixel a little so the tail fades out
    for i in range(config.NUMBER_PIXELS):
        r, g, b = strip[i]
        strip[i] = (r * 3 // 4, g * 3 // 4, b * 3 // 4)
    # Draw the bright head of the comet
    strip[comet_pos] = wheel(comet_hue)
    strip.write()
    comet_pos = (comet_pos + 1) % config.NUMBER_PIXELS
    comet_hue = (comet_hue + 2) & 255


# ---------------------------------------------------------------------------
# Pattern table: (name, step function, seconds to sleep between frames)
# Mode 1 maps to PATTERNS[0], mode 2 to PATTERNS[1], and so on.
# ---------------------------------------------------------------------------
PATTERNS = [
    ('Color Letters', pattern_color_letters, 0.10),
    ('Rainbow Flow',  pattern_rainbow_flow,  0.02),
    ('Rainbow Solid', pattern_rainbow_solid, 0.02),
    ('Color Sparkle', pattern_color_sparkle, 0.05),
    ('Color Wipe',    pattern_color_wipe,    0.05),
    ('Comet',         pattern_comet,         0.02),
]

# Mode 0 is the auto-cycle, then one mode per pattern
NUMBER_MODES = len(PATTERNS) + 1

# ---------------------------------------------------------------------------
# Button handling (interrupt driven, same approach as 01-test-buttons.py)
# ---------------------------------------------------------------------------
mode = 0          # the current mode
last_time = 0     # last time a button event was handled (for debounce)


def button_callback(pin):
    """Interrupt handler - get in and out quickly."""
    global mode, last_time
    new_time = ticks_ms()
    # only act if it has been more than 200ms since the last event
    if ticks_diff(new_time, last_time) > 200:
        if pin is button_up:
            mode = (mode + 1) % NUMBER_MODES
        else:
            mode = (mode - 1) % NUMBER_MODES
        last_time = new_time


# Fire the handler on the falling edge (the moment each button is pressed)
button_up.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)
button_down.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
old_mode = -1            # forces a clean setup on the first pass
auto_index = 0           # which pattern auto-cycle is showing
auto_start = ticks_ms()  # when the current auto-cycle pattern started

print('Bookstore Sign - Pattern Mode Test')
print('BUTTON_1 (pin', config.BUTTON_PIN_1, ') = next mode,',
      'BUTTON_2 (pin', config.BUTTON_PIN_2, ') = previous mode')
print('There are', NUMBER_MODES, 'modes (0 =', NUMBER_MODES - 1, ').')

while True:
    # Handle a mode change with a clean transition
    if mode != old_mode:
        old_mode = mode
        builtin_led.toggle()
        clear_strip()
        reset_pattern_state()
        if mode == 0:
            auto_index = 0
            auto_start = ticks_ms()
            print('Mode 0: AUTO-CYCLE - 60 seconds per pattern')
            print('  Now showing:', PATTERNS[auto_index][0])
        else:
            print('Mode', mode, '-', PATTERNS[mode - 1][0])

    # Pick which pattern to draw this pass
    if mode == 0:
        # Auto-cycle: advance to the next pattern every 60 seconds
        now = ticks_ms()
        if ticks_diff(now, auto_start) >= AUTO_CYCLE_MS:
            auto_start = now
            auto_index = (auto_index + 1) % len(PATTERNS)
            clear_strip()
            reset_pattern_state()
            print('  Now showing:', PATTERNS[auto_index][0])
        name, step, delay = PATTERNS[auto_index]
    else:
        name, step, delay = PATTERNS[mode - 1]

    # Draw one frame of the current pattern, then pause briefly
    step()
    sleep(delay)
