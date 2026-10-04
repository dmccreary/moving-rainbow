# Module: Sloshing Water (program 11, and mode 9 of program 13)
# Filename: sloshing_water.py
# Version: 1.0.0
#
# The matrix is a square pan seen from the side, half full of blue water.
# Stand the board upright and the bottom half fills with water. Rock or
# tilt the board and the water sloshes back and forth, then settles with a
# level surface. The amount of water never changes: always 128 pixels.
# Run it on its own with 11-sloshing-water.py.
# If the water falls toward the wrong side, change FLIP_X, FLIP_Y or
# SWAP_XY in kit.py.
# Not yet tested on hardware.

import kit

# the water: half the pixels. Only half the pixels are lit and only in blue,
# so these numbers draw about 300 mA, well under what USB supplies.
NUMBER_PIXELS = kit.NUMBER_PIXELS
WATER_PIXELS = NUMBER_PIXELS // 2
WATER_COLOR = (0, 0, 24)
SURFACE_COLOR = (0, 10, 48)     # a brighter line along the top of the water
SURFACE_THICKNESS = 1.0         # in pixels

# the water follows the pull of gravity like a weight on a spring,
# so it overshoots and rings back and forth when you rock the board
SPRING = 90         # bigger = faster sloshing (90 is about 1.5 slosh a second)
DAMPING = 2.5       # bigger = the sloshing dies out sooner
MIN_TILT = 0.2      # pull along the board below this (nearly flat): water stays put
MAX_PULL = 1.5      # ignore the extra push of hard shakes

# For every pixel, work out once: its strip number, how far it is from the
# center of the pan (across and down), and a tiny nudge so no two pixels
# are ever exactly the same depth.
center_x = (kit.WIDTH - 1) / 2
center_y = (kit.HEIGHT - 1) / 2
pixel_index = []
across = []
down = []
nudge = []
for row in range(kit.HEIGHT):
    for col in range(kit.WIDTH):
        pixel_index.append(kit.xy(col, row))
        across.append(col - center_x)
        down.append(row - center_y)
        nudge.append(0.0007 * col + 0.0011 * row)

def read_pull():
    # which way is downhill along the board, and how strong is the pull
    gx, gy = kit.read_tilt()
    size = (gx * gx + gy * gy) ** 0.5
    if size > MAX_PULL:
        gx = gx * MAX_PULL / size
        gy = gy * MAX_PULL / size
        size = MAX_PULL
    return gx, gy, size

def draw_water(nx, ny):
    # nx, ny is the downhill direction. A pixel's depth is how far it sits
    # downhill. The deepest half of the pixels are water, so the surface
    # always lands where exactly half the pan is full.
    depth = [across[i] * nx + down[i] * ny + nudge[i] for i in range(NUMBER_PIXELS)]
    cutoff = sorted(depth)[NUMBER_PIXELS - WATER_PIXELS]
    for i in range(NUMBER_PIXELS):
        below_surface = depth[i] - cutoff
        if below_surface < 0:
            kit.strip[pixel_index[i]] = kit.OFF
        elif below_surface < SURFACE_THICKNESS:
            kit.strip[pixel_index[i]] = SURFACE_COLOR
        else:
            kit.strip[pixel_index[i]] = WATER_COLOR
    kit.strip.write()

def run(settings=None):
    from utime import ticks_ms, ticks_diff

    # the spring: sx, sy is where the water thinks "down" is, vx, vy is how
    # fast that is changing, and target is where gravity says it should be
    sx = 0.0
    sy = 1.0
    vx = 0.0
    vy = 0.0
    target_x = 0.0
    target_y = 1.0
    nx = 0.0
    ny = 1.0
    last_time = ticks_ms()

    while True:
        gx, gy, size = read_pull()
        if size >= MIN_TILT:
            target_x = gx
            target_y = gy

        now = ticks_ms()
        dt = ticks_diff(now, last_time) / 1000
        last_time = now
        if dt > 0.05:
            dt = 0.05

        vx += (SPRING * (target_x - sx) - DAMPING * vx) * dt
        vy += (SPRING * (target_y - sy) - DAMPING * vy) * dt
        sx += vx * dt
        sy += vy * dt

        length = (sx * sx + sy * sy) ** 0.5
        if length > 0.05:
            nx = sx / length
            ny = sy / length

        draw_water(nx, ny)
        kit.wait(5)
