# Lab 25: Bouncing Ball
# Filename: 25-bouncing-ball.py
# Version: 1.0.0
#
# A ball drops from the top of the strip, speeds up as it falls, and
# bounces on pixel 0. Each bounce is lower than the one before, until the
# ball comes to rest. Then it drops again.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

BALL_COLOR = (140, 60, 0)   # orange
GRAVITY = 0.2               # how much faster the ball falls each frame
BOUNCE = 0.8                # the ball keeps 80% of its speed after a bounce
MIN_SPEED = 0.6             # slower than this and the ball stops bouncing
FRAME_DELAY = 0.03          # seconds per frame

old_pixel = 0
while True:
    # drop the ball from the top of the strip. Pixel 0 is the floor.
    position = NUMBER_PIXELS - 1
    velocity = 0            # pixels per frame: up is positive, down is negative
    bouncing = True

    while bouncing:
        # gravity changes the speed, and then the speed moves the ball
        velocity = velocity - GRAVITY
        position = position + velocity

        # the ball hit the floor: bounce back up, but slower
        if position <= 0:
            position = 0
            velocity = -velocity * BOUNCE
            if velocity < MIN_SPEED:
                bouncing = False

        # keep the ball on the strip, even if BOUNCE is set very high
        if position > NUMBER_PIXELS - 1:
            position = NUMBER_PIXELS - 1

        # erase the old spot in memory, light the new spot, and write once
        strip[old_pixel] = (0, 0, 0)
        pixel = round(position)
        strip[pixel] = BALL_COLOR
        strip.write()
        old_pixel = pixel
        sleep(FRAME_DELAY)

    sleep(1)    # the ball rests for a moment, then drops again
