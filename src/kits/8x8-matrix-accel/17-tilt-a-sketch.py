# Lab 17: Tilt-a-Sketch
# Filename: 17-tilt-a-sketch.py
# Version: 1.1.0
#
# Draw your own picture by tilting the kit. A blinking dot is your pen.
# Tilt the board and the pen rolls toward the low side, leaving a line of
# color behind it.
#   Button 1 (GPIO 14): change the pen color
#   Button 2 (GPIO 15): lift the pen up, or put it back down
#   Shake the kit hard: erase the whole picture
# The code lives in the module tilt_a_sketch.py (with the shared helpers in
# kit.py) so that program 19 can load it as a mode too. Upload all the .py
# files with ./upload-code.sh before you run this.
# Not yet tried by hand: the tilt and buttons need a person to draw with them.

import tilt_a_sketch

print("Lab 17: Tilt-a-Sketch (version 1.1.0)")

tilt_a_sketch.run()
