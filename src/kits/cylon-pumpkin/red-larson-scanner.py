# Simplified Red Larson Scanner (Cylon / KITT eye)
#
# A single bright red dot sweeps back and forth across the strip,
# leaving a fading red tail behind it - just like the eye of a
# Cylon from Battlestar Galactica or KITT from Knight Rider.
#
# We are using https://github.com/blaz-r/pi_pico_neopixel
from utime import sleep
from neopixel import Neopixel

NUMBER_PIXELS = 25
STATE_MACHINE = 0
LED_PIN = 0

# The Neopixels on the Maker Pi RP2040 are the GRB variety, not RGB
strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, LED_PIN, "GRB")

# set to be 1 to 100 for percent brightness
strip.brightness(100)

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
            strip.set_pixel(i, (brightness, 0, 0))
        else:
            # Too far from the eye - turn this pixel off
            strip.set_pixel(i, (0, 0, 0))
    strip.show()
    sleep(delay)


while True:
    # Sweep the eye from the left end to the right end
    for position in range(NUMBER_PIXELS):
        draw_eye(position)
    # Sweep the eye back from the right end to the left end
    for position in range(NUMBER_PIXELS - 2, 0, -1):
        draw_eye(position)
