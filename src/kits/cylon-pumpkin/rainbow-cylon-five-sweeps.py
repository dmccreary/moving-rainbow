# Cylon Eye Scanner - Five Sweeps Per Color
#
# For each color, the eye sweeps back and forth across the strip five times.
# After every color has had its turn, the rainbow band sweeps back and forth
# once, and then the whole show repeats.
#
# Uses the built-in MicroPython "neopixel" library with array index syntax:
#   strip[i] = (r, g, b)   sets the color of pixel i
#   strip.write()          sends the colors out to the strip
from utime import sleep
from machine import Pin
from neopixel import NeoPixel

NUMBER_PIXELS = 25
LED_PIN = 0

# Create the strip on the given pin (built-in library handles GRB order)
strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

# How long to pause between each step (smaller = faster)
delay = .06

# How many pixels long the fading tail is behind the eye
TAIL = 6

# How many back-and-forth trips the eye makes for each color
SWEEPS = 5

off = (0, 0, 0)

# The colors the eye cycles through, in order
eye_colors = [
    (255, 0, 0),      # red
    (255, 60, 0),     # orange
    (255, 255, 0),    # yellow
    (0, 255, 0),      # green
    (0, 0, 255),      # blue
    (0, 255, 255),    # cyan
    (75, 30, 130),    # indigo
    (255, 0, 255),    # magenta
    (255, 255, 255),  # white
]

# The 7-color band used by the rainbow sweep (left to right)
rainbow_band = (
    (138, 43, 226),   # violet
    (75, 0, 130),     # indigo
    (0, 0, 255),      # blue
    (0, 255, 0),      # green
    (255, 150, 0),    # yellow
    (255, 60, 0),     # orange
    (255, 0, 0),      # red
)


def draw_eye(position, direction, r, g, b):
    """Draw the eye at 'position' with a fading tail trailing behind it.

    'direction' is +1 when the eye is moving right and -1 when moving left,
    so the tail always trails behind the direction of motion.
    """
    for i in range(NUMBER_PIXELS):
        # How many pixels is this one *behind* the eye along the travel path?
        distance = (position - i) * direction
        if 0 <= distance <= TAIL:
            # Halve the brightness for every pixel back along the tail
            strip[i] = (int(r / pow(2, distance)),
                        int(g / pow(2, distance)),
                        int(b / pow(2, distance)))
        else:
            # Not part of the eye or its tail - turn this pixel off
            strip[i] = off
    strip.write()
    sleep(delay)


def sweep_eye(r, g, b):
    """One back-and-forth trip of the eye in the given color."""
    # Sweep the eye from the left end to the right end
    for position in range(NUMBER_PIXELS):
        draw_eye(position, 1, r, g, b)
    # Sweep the eye back from the right end to the left end
    for position in range(NUMBER_PIXELS - 2, 0, -1):
        draw_eye(position, -1, r, g, b)


def sweep_rainbow():
    """One back-and-forth trip of the 7-color rainbow band."""
    # Slide the rainbow band from the left end to the right end
    for start in range(0, NUMBER_PIXELS - 6):
        for i in range(NUMBER_PIXELS):
            strip[i] = off
        for k in range(7):
            strip[start + k] = rainbow_band[k]
        strip.write()
        sleep(delay)
    # Slide the rainbow band back from the right end to the left end
    for start in range(NUMBER_PIXELS - 7, -1, -1):
        for i in range(NUMBER_PIXELS):
            strip[i] = off
        for k in range(7):
            strip[start + k] = rainbow_band[6 - k]
        strip.write()
        sleep(delay)


while True:
    # Each color sweeps back and forth SWEEPS times before the next color
    for color in eye_colors:
        for trip in range(SWEEPS):
            sweep_eye(color[0], color[1], color[2])
    # Then the rainbow band sweeps back and forth once
    sweep_rainbow()
