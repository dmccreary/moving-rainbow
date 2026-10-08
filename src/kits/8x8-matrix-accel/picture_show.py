# Module: Picture Show (used by mode 6 of program 18)
# Filename: picture_show.py
# Version: 1.0.0
#
# Shows the pictures in the gallery file pictures.py, one after another.
# Each new picture slides in from the right and pushes the old one out.
# It does not use the tilt.

import kit
import pictures

HOLD_MS = 2200          # how long each picture stays still
SLIDE_MS = 45           # time for each step of the slide

def draw(old, new, shift):
    # shift 0 shows the old picture. Each step moves everything one column
    # to the left, so at shift 8 the new picture has taken its place.
    for y in range(kit.HEIGHT):
        row = old[y] + new[y]           # the two pictures side by side
        for x in range(kit.WIDTH):
            kit.strip[kit.xy(x, y)] = pictures.COLORS[row[x + shift]]
    kit.strip.write()

def run(settings=None):
    count = len(pictures.GALLERY)
    number = 0
    blank = ["." * kit.WIDTH] * kit.HEIGHT
    old = blank
    while True:
        new = pictures.GALLERY[number][1]
        for shift in range(1, kit.WIDTH + 1):
            draw(old, new, shift)
            kit.wait(SLIDE_MS)
        kit.wait(HOLD_MS)
        old = new
        number = (number + 1) % count
