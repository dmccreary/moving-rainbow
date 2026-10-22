# Module: Walk the Pixels (the demo version of program 06, used by program 19)
# Filename: walk_pixels.py
# Version: 1.0.0
#
# Lights one pixel at a time in strip order, from pixel 0 to pixel 63, like
# program 06. It sleeps with kit.wait() in place of sleep(), so a press of
# a mode button in program 19 stops it right away. It does not use the tilt.

import kit

STEP_MS = 100
WALK_COLOR = (40, 0, 40)

def run(settings=None):
    kit.clear()         # wipe out the mode number program 19 just showed
    while True:
        for i in range(kit.NUMBER_PIXELS):
            kit.strip[i] = WALK_COLOR
            kit.strip.write()
            kit.strip[i] = kit.OFF      # erased by the next write()
            kit.wait(STEP_MS)
