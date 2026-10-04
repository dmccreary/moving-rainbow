# Module: Tilt Balls (used by modes 6, 7 and 8 of program 13)
# Filename: tilt_balls.py
# Version: 1.0.0
#
# One or more colored dots roll around the matrix like balls in a tray. Tilt
# the board and they roll toward the low side, bounce off the edges and
# bounce off each other. run() takes these settings:
#   colors - a list of colors, one for each ball
# Not yet tested on hardware.

import math
from utime import ticks_ms, ticks_diff
import kit

FRAME_MS = 15
ACCEL = 45          # how fast a ball speeds up, in pixels per second per second, for 1 g of tilt
FRICTION = 0.8      # the fraction of its speed a ball loses every second
BOUNCE = 0.6        # the fraction of its speed a ball keeps after a bounce
DEADZONE = 0.05     # tilts smaller than this (in g) are ignored
BALL_SIZE = 1.05    # balls are pushed apart when closer than this (in pixels)

def run(settings):
    colors = settings["colors"]
    count = len(colors)
    last_x = kit.WIDTH - 1
    last_y = kit.HEIGHT - 1

    # start the balls in a ring around the middle, sitting still
    xs = []
    ys = []
    vxs = []
    vys = []
    for i in range(count):
        angle = 2 * math.pi * i / count
        spread = 0
        if count > 1:
            spread = 4
        xs.append(last_x / 2 + spread * math.cos(angle))
        ys.append(last_y / 2 + spread * math.sin(angle))
        vxs.append(0.0)
        vys.append(0.0)

    last_time = ticks_ms()
    while True:
        now = ticks_ms()
        dt = ticks_diff(now, last_time) / 1000
        last_time = now
        if dt > 0.05:
            dt = 0.05

        gx, gy = kit.read_tilt()
        if abs(gx) < DEADZONE:
            gx = 0
        if abs(gy) < DEADZONE:
            gy = 0

        for i in range(count):
            vxs[i] += gx * ACCEL * dt
            vys[i] += gy * ACCEL * dt
            vxs[i] -= vxs[i] * FRICTION * dt
            vys[i] -= vys[i] * FRICTION * dt
            xs[i] += vxs[i] * dt
            ys[i] += vys[i] * dt
            # bounce off the edges
            if xs[i] < 0:
                xs[i] = 0
                vxs[i] = abs(vxs[i]) * BOUNCE
            elif xs[i] > last_x:
                xs[i] = last_x
                vxs[i] = -abs(vxs[i]) * BOUNCE
            if ys[i] < 0:
                ys[i] = 0
                vys[i] = abs(vys[i]) * BOUNCE
            elif ys[i] > last_y:
                ys[i] = last_y
                vys[i] = -abs(vys[i]) * BOUNCE

        # balls that overlap push each other apart and trade speed
        for turn in range(2):
            for i in range(count):
                for j in range(i + 1, count):
                    dx = xs[j] - xs[i]
                    dy = ys[j] - ys[i]
                    distance = (dx * dx + dy * dy) ** 0.5
                    if distance < BALL_SIZE:
                        if distance < 0.001:
                            dx = 1.0
                            dy = 0.0
                            distance = 1.0
                        nx = dx / distance
                        ny = dy / distance
                        push = (BALL_SIZE - distance) / 2
                        xs[i] -= nx * push
                        ys[i] -= ny * push
                        xs[j] += nx * push
                        ys[j] += ny * push
                        closing = (vxs[j] - vxs[i]) * nx + (vys[j] - vys[i]) * ny
                        if closing < 0:
                            share = closing * (1 + BOUNCE) / 2
                            vxs[i] += nx * share
                            vys[i] += ny * share
                            vxs[j] -= nx * share
                            vys[j] -= ny * share
            # pushing must not shove a ball through the edge
            for i in range(count):
                xs[i] = min(max(xs[i], 0), last_x)
                ys[i] = min(max(ys[i], 0), last_y)

        kit.clear()
        for i in range(count):
            kit.strip[kit.xy(round(xs[i]), round(ys[i]))] = colors[i]
        kit.strip.write()
        kit.wait(FRAME_MS)
