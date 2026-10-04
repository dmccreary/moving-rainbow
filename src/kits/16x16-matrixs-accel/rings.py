# Module: Ripple Rings (used by mode 5 of program 13)
# Filename: rings.py
# Version: 1.0.0
#
# Colored rings start at random spots, spread out and fade away, like drops
# landing in a pond. It does not use the tilt.
# Not yet tested on hardware.

import math
from utime import ticks_ms, ticks_diff
from urandom import randint
import kit

FRAME_MS = 20
MAX_RINGS = 4
NEW_RING_MS = 600       # time between new rings
RING_SPEED = 5          # pixels per second the ring grows
MAX_RADIUS = 11         # the ring has faded out completely by this size

def draw_ring(cx, cy, radius, color):
    # the ring dims as it grows
    shown = kit.dim(color, 1 - radius / MAX_RADIUS)
    # enough points around the circle that no pixel is skipped
    points = max(8, int(radius * 7))
    for k in range(points):
        angle = 2 * math.pi * k / points
        x = round(cx + radius * math.cos(angle))
        y = round(cy + radius * math.sin(angle))
        if 0 <= x < kit.WIDTH and 0 <= y < kit.HEIGHT:
            kit.strip[kit.xy(x, y)] = shown

def run(settings=None):
    rings = []              # each ring is [center x, center y, radius, color]
    last_time = ticks_ms()
    last_ring = ticks_ms() - NEW_RING_MS
    while True:
        now = ticks_ms()
        dt = ticks_diff(now, last_time) / 1000
        last_time = now
        if dt > 0.1:
            dt = 0.1

        if ticks_diff(now, last_ring) >= NEW_RING_MS and len(rings) < MAX_RINGS:
            last_ring = now
            color = kit.PALETTE[randint(0, len(kit.PALETTE) - 1)]
            rings.append([randint(0, kit.WIDTH - 1), randint(0, kit.HEIGHT - 1), 0.0, color])

        kit.clear()
        for ring in rings:
            ring[2] += RING_SPEED * dt
            draw_ring(ring[0], ring[1], ring[2], ring[3])
        rings = [ring for ring in rings if ring[2] < MAX_RADIUS]

        kit.strip.write()
        kit.wait(FRAME_MS)
