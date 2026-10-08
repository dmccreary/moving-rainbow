# Module: Bouncing Dots (used by modes 1, 2 and 3 of program 18)
# Filename: bounce_dots.py
# Version: 1.0.0
#
# Dots drift across the matrix and bounce off the edges. They do not use
# the tilt. run() takes these settings:
#   colors - a list of colors, one for each dot
#   speed  - the fastest a dot moves, in pixels per second
#   fade   - 0 for no trails, or 1 to 255: how much of each pixel's color
#            stays after every frame (a bigger number leaves a longer trail)

from utime import ticks_ms, ticks_diff
from urandom import randint
import kit

FRAME_MS = 20

def run(settings):
    colors = settings["colors"]
    speed = settings["speed"]
    fade = settings["fade"]
    count = len(colors)
    last_x = kit.WIDTH - 1
    last_y = kit.HEIGHT - 1

    # every dot starts somewhere random, heading in a random direction
    xs = []
    ys = []
    vxs = []
    vys = []
    for i in range(count):
        xs.append(randint(0, last_x))
        ys.append(randint(0, last_y))
        # each speed is between 40% and 100% of the top speed
        vx = speed * randint(40, 100) / 100
        vy = speed * randint(40, 100) / 100
        if randint(0, 1) == 0:
            vx = -vx
        if randint(0, 1) == 0:
            vy = -vy
        vxs.append(vx)
        vys.append(vy)

    last_time = ticks_ms()
    while True:
        now = ticks_ms()
        dt = ticks_diff(now, last_time) / 1000
        last_time = now
        if dt > 0.1:
            dt = 0.1

        if fade > 0:
            kit.fade_pixels(fade)
        else:
            kit.clear()

        for i in range(count):
            xs[i] += vxs[i] * dt
            ys[i] += vys[i] * dt
            # turn around at an edge
            if xs[i] < 0:
                xs[i] = -xs[i]
                vxs[i] = -vxs[i]
            elif xs[i] > last_x:
                xs[i] = 2 * last_x - xs[i]
                vxs[i] = -vxs[i]
            if ys[i] < 0:
                ys[i] = -ys[i]
                vys[i] = -vys[i]
            elif ys[i] > last_y:
                ys[i] = 2 * last_y - ys[i]
                vys[i] = -vys[i]
            kit.strip[kit.xy(round(xs[i]), round(ys[i]))] = colors[i]

        kit.strip.write()
        kit.wait(FRAME_MS)
