# Module: Tilt-a-Sketch (a mode of program 14)
# Filename: tilt_a_sketch.py
# Version: 1.0.0
#
# Draw your own picture by tilting the kit. A blinking dot is your pen.
# Tilt the board and the pen rolls toward the low side, leaving a line of
# color behind it.
#   Button 1 (GPIO 14): change the pen color
#   Button 2 (GPIO 15): lift the pen up, or put it back down
#   Shake the kit hard: erase the whole picture
# Copied from the 8x8 kit. In program 14 the two buttons change modes, so
# the sketch leaves them alone. run() takes this setting:
#   auto_color - True to move to the next pen color with every step, so the
#                line comes out in many colors without pressing a button

from utime import ticks_ms, ticks_diff
import kit

# the pen colors, in the order button 1 steps through them. The picture can
# fill all 256 pixels, so these numbers stay small (half the 8x8 kit's).
PEN_COLORS = [
    ("red", (12, 0, 0)),
    ("orange", (12, 4, 0)),
    ("yellow", (10, 8, 0)),
    ("green", (0, 12, 0)),
    ("blue", (0, 0, 12)),
    ("violet", (7, 0, 11)),
    ("white", (7, 7, 7)),
]
PEN_UP_COLOR = (30, 30, 30)     # the pen blinks white while it is lifted

# the rolling pen
TILT_MIN = 0.25         # tilts smaller than this (in g) do nothing
TILT_FULL = 0.8         # tipping this far rolls the pen at full speed
STEP_SLOW_MS = 260      # time per pixel at the gentlest tilt (the matrix is twice as wide as the 8x8)
STEP_FAST_MS = 90       # time per pixel when tipped all the way

SHAKE_G = 1.7           # a pull along the board stronger than this is a shake
BLINK_MS = 250          # how long the pen stays on, then off
LOOP_MS = 10            # the program looks at the tilt 100 times a second

# the picture so far: one color for every spot, in (x, y) order
canvas = [kit.OFF] * kit.NUMBER_PIXELS

pen_x = kit.WIDTH // 2
pen_y = kit.HEIGHT // 2
pen_down = True
color_number = 0

def spot(x, y):
    # where the color for column x, row y is kept in the canvas list
    return y * kit.WIDTH + x

def bright(color):
    # the pen shows a brighter copy of its color, so you can find it
    return (color[0] * 2, color[1] * 2, color[2] * 2)

def show(pen_lit):
    # draw the picture, then the pen on top of it
    for y in range(kit.HEIGHT):
        for x in range(kit.WIDTH):
            kit.strip[kit.xy(x, y)] = canvas[spot(x, y)]
    if pen_down:
        if pen_lit:
            kit.strip[kit.xy(pen_x, pen_y)] = bright(PEN_COLORS[color_number][1])
        else:
            kit.strip[kit.xy(pen_x, pen_y)] = kit.OFF
    elif pen_lit:
        kit.strip[kit.xy(pen_x, pen_y)] = PEN_UP_COLOR
    kit.strip.write()

def tilt_direction(g):
    # -1, 0 or 1: which way a tilt pushes, or 0 if it is too small
    if g >= TILT_MIN:
        return 1
    if g <= -TILT_MIN:
        return -1
    return 0

def run(settings=None):
    # run() changes the pen's state, so it says these are the variables
    # at the top of the file, not new ones of its own
    global pen_x, pen_y, pen_down, color_number
    auto_color = settings is not None and settings["auto_color"]
    # in program 14 the buttons belong to the mode changer
    use_buttons = not kit.mode_buttons_on

    canvas[spot(pen_x, pen_y)] = PEN_COLORS[color_number][1]
    if use_buttons:
        print("Button 1: next color. Button 2: pen up or down. Shake: erase.")
    else:
        print("Tilt to draw. Shake: erase.")
    print("Pen color:", PEN_COLORS[color_number][0])

    last1 = 1
    last2 = 1
    last_step = ticks_ms()
    last_blink = ticks_ms()
    pen_lit = True
    show(pen_lit)

    while True:
        changed = False

        # the buttons: a press is a change from 1 to 0
        if use_buttons:
            now1 = kit.button1.value()
            now2 = kit.button2.value()
            if now1 == 0 and last1 == 1:
                color_number = (color_number + 1) % len(PEN_COLORS)
                print("Pen color:", PEN_COLORS[color_number][0])
                if pen_down:
                    canvas[spot(pen_x, pen_y)] = PEN_COLORS[color_number][1]
                changed = True
            if now2 == 0 and last2 == 1:
                pen_down = not pen_down
                print("Pen down" if pen_down else "Pen up")
                if pen_down:
                    canvas[spot(pen_x, pen_y)] = PEN_COLORS[color_number][1]
                changed = True
            last1 = now1
            last2 = now2

        gx, gy = kit.read_tilt()
        now = ticks_ms()

        # a hard shake erases the picture
        if (gx * gx + gy * gy) ** 0.5 > SHAKE_G:
            print("Shake! The picture is erased.")
            for i in range(kit.NUMBER_PIXELS):
                canvas[i] = kit.OFF
            if pen_down:
                canvas[spot(pen_x, pen_y)] = PEN_COLORS[color_number][1]
            last_step = now + 500       # hold the pen still for half a second
            changed = True

        # the tilt rolls the pen, faster when you tip farther
        size = max(abs(gx), abs(gy))
        if size >= TILT_MIN:
            speed = min(1, (size - TILT_MIN) / (TILT_FULL - TILT_MIN))
            interval = STEP_SLOW_MS - (STEP_SLOW_MS - STEP_FAST_MS) * speed
            if ticks_diff(now, last_step) >= interval:
                # move one pixel along the direction tipped hardest
                if abs(gx) >= abs(gy):
                    new_x = pen_x + tilt_direction(gx)
                    new_y = pen_y
                else:
                    new_x = pen_x
                    new_y = pen_y + tilt_direction(gy)
                # the pen stops at the edges of the matrix
                if 0 <= new_x < kit.WIDTH and 0 <= new_y < kit.HEIGHT:
                    pen_x = new_x
                    pen_y = new_y
                    if auto_color:
                        color_number = (color_number + 1) % len(PEN_COLORS)
                    if pen_down:
                        canvas[spot(pen_x, pen_y)] = PEN_COLORS[color_number][1]
                    last_step = now
                    changed = True

        # blink the pen
        if ticks_diff(now, last_blink) >= BLINK_MS:
            pen_lit = not pen_lit
            last_blink = now
            changed = True

        if changed:
            show(pen_lit)
        kit.wait(LOOP_MS)
