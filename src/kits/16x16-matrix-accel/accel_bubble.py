# Module: Accelerometer Bubble (the demo version of program 10, used by program 14)
# Filename: accel_bubble.py
# Version: 1.0.0
#
# A 2x2 dot acts like a bubble in a level: tilt the kit and the dot slides
# toward the low side, like program 10. The sensor is read by kit.py, so a
# fix to FLIP_X, FLIP_Y or SWAP_XY goes there. It sleeps with kit.wait(),
# so a press of a mode button in program 14 stops it right away.

import kit

FRAME_MS = 30
BUBBLE_COLOR = (0, 40, 40)

def to_column(g, size):
    # -1 g -> 0, 0 g -> middle, +1 g -> size - 2 (leaves room for the 2x2 dot)
    position = round((g + 1) / 2 * (size - 2))
    return max(0, min(size - 2, position))

def run(settings=None):
    while True:
        gx, gy = kit.read_tilt()
        col = to_column(gx, kit.WIDTH)
        row = to_column(gy, kit.HEIGHT)
        kit.clear()
        for dx in range(2):
            for dy in range(2):
                kit.strip[kit.xy(col + dx, row + dy)] = BUBBLE_COLOR
        kit.strip.write()
        kit.wait(FRAME_MS)
