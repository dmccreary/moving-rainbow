# Lab 19: Demo Mode
# Filename: 19-template-main.py
# Version: 1.1.0
#
# Every show and game in the kit in one program, for showing the kit off.
# Press button 1 (GPIO 14) for the next mode and button 2 (GPIO 15) for the
# previous one. The matrix shows the mode number for a moment, then the
# mode starts.
#
#   Mode  Show                                   From program
#   1     fill colors                            05
#   2     walk the pixels                        06
#   3     row and column sweep                   08
#   4     winking face                           09 and 11
#   5     picture show                           10
#   6     scrolling message                      12
#   7     three slow bouncing dots               18
#   8     seven faster bouncing dots             18
#   9     twelve colors that leave small trails  18
#   10    rainbow rain                           18
#   11    ripple rings                           18
#   12    a bubble that slides as you tilt       14
#   13    one dot that rolls as you tilt         18
#   14    three dots that roll as you tilt       18
#   15    seven dots that roll as you tilt       18
#   16    sloshing water                         15
#   17    tilt-a-maze                            16
#   18    tilt-a-sketch: tilt to draw            17
#
# Modes 1 to 11 do not use the tilt, and modes 12 to 18 do. Programs 01 to
# 04 and 07 are wiring checks and 13 only prints numbers, so they are left
# out. The buttons change modes here, so the sketch in mode 18 cannot use
# them: its pen changes color by itself, and a shake still erases.
#
# This program is a template for main.py. The Pico runs main.py by itself
# when it powers up, so save a copy on the Pico as main.py and the demo
# starts with no computer. Use a wall charger: many power banks switch off
# when the kit draws only a little current. Thonny's Stop button stops it.
#
# It works like program 18: each mode is a module that is loaded only when
# you switch to it and thrown away when you leave. Add a mode by writing a
# module with a run(settings) function and adding a line to MODES.
# Tried by hand on 2026-10-22: the buttons change modes, and it starts as main.py.

import sys
import gc
import kit

print("Lab 19: Demo Mode (version 1.1.0)")

MODE_NUMBER_MS = 700    # how long the mode number shows before the mode starts

# (name, module to load, settings handed to the module's run() function)
MODES = [
    # shows that do not use the tilt
    ("Fill colors", "fill_colors", None),
    ("Walk the pixels", "walk_pixels", None),
    ("Row and column sweep", "row_column_sweep", None),
    ("Winking face", "winking_face", None),
    ("Picture show", "picture_show", None),
    ("Scrolling message", "scroll_text",
     {"text": "MOVING RAINBOW!", "speed": 9}),
    ("Three dots", "bounce_dots",
     {"colors": [kit.RED, kit.GREEN, kit.BLUE], "speed": 2.5, "fade": 0}),
    ("Seven dots", "bounce_dots",
     {"colors": kit.RAINBOW, "speed": 4, "fade": 0}),
    ("Colors with trails", "bounce_dots",
     {"colors": kit.PALETTE, "speed": 5, "fade": 215}),
    ("Rainbow rain", "rain", None),
    ("Ripple rings", "rings", None),
    # shows and games that use the tilt
    ("Accelerometer bubble", "accel_bubble", None),
    ("Tilt one dot", "tilt_balls",
     {"colors": [kit.BLUE]}),
    ("Tilt three dots", "tilt_balls",
     {"colors": [kit.RED, kit.GREEN, kit.BLUE]}),
    ("Tilt seven dots", "tilt_balls",
     {"colors": kit.RAINBOW}),
    ("Sloshing water", "sloshing_water", None),
    ("Tilt-a-maze", "tilt_a_maze", None),
    ("Tilt-a-sketch", "tilt_a_sketch",
     {"auto_color": True}),
]

def unload(module_name):
    # forget the module so its memory can be reused by the next mode.
    # The picture gallery is big, so forget it too if a mode loaded it.
    for name in (module_name, "pictures"):
        if name in sys.modules:
            del sys.modules[name]
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
    except Exception as error:
        # any other problem: print it, then start the same mode again
        print("  Mode", mode + 1, "stopped with an error:")
        sys.print_exception(error)
        step = 0
    module = None       # let go of the module, then forget it
    kit.clear()
    kit.strip.write()
    unload(module_name)
    mode = (mode + step) % len(MODES)
