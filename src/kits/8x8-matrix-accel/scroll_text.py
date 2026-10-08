# Module: Scrolling Message (used by mode 7 of program 18)
# Filename: scroll_text.py
# Version: 1.0.0
#
# Scrolls a message across the matrix, with each letter in the next color
# of the rainbow. It does not use the tilt. run() takes these settings:
#   text  - the message to show (capital letters, numbers and ! ? . -)
#   speed - how many columns the message moves every second

import kit
from font import LETTERS

LETTER_HEIGHT = 5
TOP_ROW = (kit.HEIGHT - LETTER_HEIGHT) // 2

def run(settings):
    text = settings["text"]
    step_ms = 1000 // settings["speed"]

    # one long strip of columns: each is (5 letters top to bottom, color)
    empty = (".....", kit.OFF)
    columns = [empty] * kit.WIDTH
    letter_number = 0
    for letter in text:
        rows = LETTERS.get(letter, LETTERS["?"])
        color = kit.RAINBOW[letter_number % len(kit.RAINBOW)]
        if letter != " ":
            letter_number += 1
        for col in range(len(rows[0])):
            column = ""
            for row in range(LETTER_HEIGHT):
                column = column + rows[row][col]
            columns.append((column, color))
        columns.append(empty)
    columns = columns + [empty] * kit.WIDTH

    while True:
        # slide an 8-column window along the strip
        for start in range(len(columns) - kit.WIDTH + 1):
            for x in range(kit.WIDTH):
                column, color = columns[start + x]
                for row in range(LETTER_HEIGHT):
                    if column[row] == "X":
                        kit.strip[kit.xy(x, TOP_ROW + row)] = color
                    else:
                        kit.strip[kit.xy(x, TOP_ROW + row)] = kit.OFF
            kit.strip.write()
            kit.wait(step_ms)
