# Module: Rainbow Rain (used by mode 4 of program 13)
# Filename: rain.py
# Version: 1.0.0
#
# Colored drops fall down the matrix, each at its own speed, leaving a fading
# trail. A drop that reaches the bottom starts again at the top. It does not
# use the tilt.
# Not yet tested on hardware.

from utime import ticks_ms, ticks_diff
from urandom import randint
import kit

FRAME_MS = 20
DROPS = 10
KEEP = 195              # how much of each pixel's color stays every frame
MIN_SPEED = 5           # pixels per second
MAX_SPEED = 14

def new_drop(drop):
    # [column, row, speed, color]. A negative row means the drop waits above
    # the top edge for a moment before it appears.
    drop[0] = randint(0, kit.WIDTH - 1)
    drop[1] = -randint(0, 12)
    drop[2] = randint(MIN_SPEED, MAX_SPEED)
    drop[3] = kit.RAINBOW[randint(0, len(kit.RAINBOW) - 1)]

def run(settings=None):
    drops = []
    for i in range(DROPS):
        drop = [0, 0, 0, kit.RED]
        new_drop(drop)
        drops.append(drop)

    last_time = ticks_ms()
    while True:
        now = ticks_ms()
        dt = ticks_diff(now, last_time) / 1000
        last_time = now
        if dt > 0.1:
            dt = 0.1

        kit.fade_pixels(KEEP)
        for drop in drops:
            drop[1] += drop[2] * dt
            row = round(drop[1])
            if row >= kit.HEIGHT:
                new_drop(drop)
            elif row >= 0:
                kit.strip[kit.xy(drop[0], row)] = drop[3]

        kit.strip.write()
        kit.wait(FRAME_MS)
