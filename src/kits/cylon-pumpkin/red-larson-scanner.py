# Simplified Red Larson Scanner (Cylon / KITT eye)
#
# A single bright red dot sweeps back and forth across the strip,
# leaving a fading red tail behind it - just like the eye of a
# Cylon from Battlestar Galactica or KITT from Knight Rider.
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

# How long to pause between each step (smaller = faster eye)
delay = 0.05

# How many pixels long the fading tail is
TAIL = 4


def draw_eye(position):
    """Light the eye at 'position' with a fading red tail and clear the rest."""
    for i in range(NUMBER_PIXELS):
        # How far is this pixel from the center of the eye?
        distance = abs(i - position)
        if distance <= TAIL:
            # Halve the brightness for every pixel away from the center
            brightness = int(255 / pow(2, distance))
            strip[i] = (brightness, 0, 0)
        else:
            # Too far from the eye - turn this pixel off
            strip[i] = (0, 0, 0)
    strip.write()
    sleep(delay)


while True:
    # Sweep the eye from the left end to the right end
    for position in range(NUMBER_PIXELS):
        draw_eye(position)
    # Sweep the eye back from the right end to the left end
    for position in range(NUMBER_PIXELS - 2, 0, -1):
        draw_eye(position)
