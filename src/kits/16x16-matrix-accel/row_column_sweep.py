# Module: Row and Column Sweep (the demo version of program 08, used by program 14)
# Filename: row_column_sweep.py
# Version: 1.0.0
#
# A bar of light sweeps down the rows and then across the columns, like
# program 08. It sleeps with kit.wait() in place of sleep(), so a press of
# a mode button in program 14 stops it right away. It does not use the tilt.

import config
import kit

LEVEL = config.LEVEL
STEP_MS = 120
ROW_COLOR = (0, LEVEL, 0)       # green
COLUMN_COLOR = (0, 0, LEVEL)    # blue

def run(settings=None):
    while True:
        for y in range(kit.HEIGHT):
            kit.clear()
            for x in range(kit.WIDTH):
                kit.strip[kit.xy(x, y)] = ROW_COLOR
            kit.strip.write()
            kit.wait(STEP_MS)
        for x in range(kit.WIDTH):
            kit.clear()
            for y in range(kit.HEIGHT):
                kit.strip[kit.xy(x, y)] = COLUMN_COLOR
            kit.strip.write()
            kit.wait(STEP_MS)
