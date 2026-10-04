# Test 13: Modes
# Filename: 13-modes.py
# Version: 1.0.0
#
# Ten light shows in one program. Press button 1 (GPIO 14) for the next
# mode and button 2 (GPIO 15) for the previous one. The matrix shows the
# mode number for a moment, then the mode starts.
#
#   1  three slow bouncing dots (red, green, blue)
#   2  seven faster bouncing dots, one for each color of the rainbow
#   3  twelve colors that leave small trails
#   4  rainbow rain
#   5  ripple rings
#   6  a blue dot you roll by tilting the board
#   7  three dots that roll around as you tilt
#   8  seven dots that roll around as you tilt
#   9  sloshing water (program 11)
#   10 tilt-a-maze (program 12)
#
# Each mode is a separate module that is loaded only when you switch to it
# and thrown away when you leave, so the Pico never holds more than one
# mode in memory. Add a mode by writing a module with a run(settings)
# function and adding a line to MODES.
# Not yet tested on hardware.

import sys
import gc
import kit

print("Test 13: Modes (version 1.0.0)")

MODE_NUMBER_MS = 700    # how long the mode number shows before the mode starts

# (name, module to load, settings handed to the module's run() function)
MODES = [
    ("Three dots", "bounce_dots",
     {"colors": [kit.RED, kit.GREEN, kit.BLUE], "speed": 4, "fade": 0}),
    ("Seven dots", "bounce_dots",
     {"colors": kit.RAINBOW, "speed": 7, "fade": 0}),
    ("Colors with trails", "bounce_dots",
     {"colors": kit.PALETTE, "speed": 9, "fade": 215}),
    ("Rainbow rain", "rain", None),
    ("Ripple rings", "rings", None),
    ("Tilt one dot", "tilt_balls",
     {"colors": [kit.BLUE]}),
    ("Tilt three dots", "tilt_balls",
     {"colors": [kit.RED, kit.GREEN, kit.BLUE]}),
    ("Tilt seven dots", "tilt_balls",
     {"colors": kit.RAINBOW}),
    ("Sloshing water", "sloshing_water", None),
    ("Tilt-a-maze", "tilt_a_maze", None),
]

def unload(module_name):
    # forget the module so its memory can be reused by the next mode
    if module_name in sys.modules:
        del sys.modules[module_name]
    gc.collect()

kit.mode_buttons_on = True
mode = 0
while True:
    name, module_name, settings = MODES[mode]
    print("Mode", mode + 1, "-", name, "(module " + module_name + ")")
    step = 1
    module = None
    try:
        # a button press during any wait() raises kit.ModeChange
        kit.draw_text(str(mode + 1))
        kit.wait(MODE_NUMBER_MS)
        module = __import__(module_name)
        print("  RAM free:", gc.mem_free(), "bytes")
        module.run(settings)
    except kit.ModeChange as change:
        step = change.args[0]
    module = None       # let go of the module, then forget it
    kit.clear()
    kit.strip.write()
    unload(module_name)
    mode = (mode + step) % len(MODES)
