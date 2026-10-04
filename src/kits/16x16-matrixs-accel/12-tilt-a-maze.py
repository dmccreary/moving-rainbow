# Test 12: Tilt-a-Maze
# Filename: 12-tilt-a-maze.py
# Version: 1.0.0
#
# Tilt the board to roll the red ball through a light blue maze and into
# the green hole in the opposite corner. Each level is a little harder:
# the early mazes have shortcuts, and level 9 has only one way through.
# Before each level the matrix shows its number (L1 to L9). Finish level 9
# and a rainbow appears, then the game starts over.
# The ball rolls toward the low side. If it rolls the wrong way, change
# FLIP_X, FLIP_Y or SWAP_XY (the same settings as programs 10 and 11).
# Not yet tested on hardware.

from machine import Pin, I2C
from neopixel import NeoPixel
from utime import sleep_ms, ticks_ms, ticks_diff
import ustruct
import config

print("Test 12: Tilt-a-Maze (version 1.0.0)")

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
MATRIX_WIDTH = config.MATRIX_WIDTH
MATRIX_HEIGHT = config.MATRIX_HEIGHT
SERPENTINE = config.SERPENTINE
ACCEL_I2C_ID = config.ACCEL_I2C_ID
ACCEL_SDA_PIN = config.ACCEL_SDA_PIN
ACCEL_SCL_PIN = config.ACCEL_SCL_PIN
ACCEL_ADDRESS = config.ACCEL_ADDRESS

# LIS3DH registers
CTRL_REG1 = 0x20
CTRL_REG4 = 0x23
ACCEL_DATA_REGISTER = 0x28 | 0x80   # the 0x80 bit makes the chip step through x, y, z
COUNTS_PER_G = 16384

# how the sensor is mounted relative to the matrix (same as program 10)
FLIP_X = False
FLIP_Y = True
SWAP_XY = False

# colors. About half the pixels are walls, so the wall color stays dim:
# the whole maze draws about 300 mA, well under what USB supplies.
WALL_COLOR = (3, 10, 18)        # light blue
BALL_COLOR = (40, 0, 0)         # red
HOLE_COLOR = (0, 40, 0)         # green
TEXT_COLOR = (16, 16, 4)
OFF = (0, 0, 0)

# the rolling ball
TILT_MIN = 0.25         # tilts smaller than this (in g) do nothing
TILT_FULL = 0.8         # tipping this far rolls the ball at full speed
STEP_SLOW_MS = 260      # time per pixel at the gentlest tilt
STEP_FAST_MS = 90       # time per pixel when tipped all the way

# the levels. Level 1 is the first item in each list.
LAST_LEVEL = 9
# walls knocked out of the finished maze to make shortcuts: fewer each level
EXTRA_OPENINGS = [40, 30, 22, 16, 11, 7, 4, 2, 0]
# starting numbers for the maze builder, one per level, so every level is the
# same each time you play. Each one was picked so the way through is longer.
MAZE_SEEDS = [1, 87, 194, 108, 499, 236, 7, 701, 95]

# The maze is made of 8 x 8 cells. A cell is one pixel, with a wall pixel
# between it and the next cell, so cell (cx, cy) is pixel (2 * cx, 2 * cy).
# The last column and row are the maze's right and bottom walls.
CELLS_ACROSS = MATRIX_WIDTH // 2
CELLS_DOWN = MATRIX_HEIGHT // 2
# the ball starts in a different corner each level; the hole is the opposite one
# (level 1: ball in the upper left corner, hole in the lower right)
CORNERS = [(0, 0), (CELLS_ACROSS - 1, 0), (CELLS_ACROSS - 1, CELLS_DOWN - 1), (0, CELLS_DOWN - 1)]

# the rainbow arch
RAINBOW_COLORS = [
    (16, 0, 0),     # red
    (16, 5, 0),     # orange
    (14, 12, 0),    # yellow
    (0, 16, 0),     # green
    (0, 6, 16),     # blue
    (3, 0, 16),     # indigo
    (9, 0, 14),     # violet
]
RAINBOW_CENTER_X = (MATRIX_WIDTH - 1) / 2
RAINBOW_CENTER_Y = MATRIX_HEIGHT - 1
RAINBOW_INNER_RADIUS = 4
RAINBOW_BAND_WIDTH = 1.6
RAINBOW_FRAMES = 70
FRAME_MS = 130

# the numbers 1 to 9 and the letter L, 3 pixels wide and 5 tall
LETTERS = {
    "L": ("X..", "X..", "X..", "X..", "XXX"),
    "1": (".X.", "XX.", ".X.", ".X.", "XXX"),
    "2": ("XXX", "..X", "XXX", "X..", "XXX"),
    "3": ("XXX", "..X", "XXX", "..X", "XXX"),
    "4": ("X.X", "X.X", "XXX", "..X", "..X"),
    "5": ("XXX", "X..", "XXX", "..X", "XXX"),
    "6": ("XXX", "X..", "XXX", "X.X", "XXX"),
    "7": ("XXX", "..X", "..X", "..X", "..X"),
    "8": ("XXX", "X.X", "XXX", "X.X", "XXX"),
    "9": ("XXX", "X.X", "XXX", "..X", "XXX"),
}
TEXT_SCALE = 2          # each letter pixel is drawn as a 2 x 2 block
TITLE_MS = 1500

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
i2c = I2C(ACCEL_I2C_ID, sda=Pin(ACCEL_SDA_PIN), scl=Pin(ACCEL_SCL_PIN), freq=400000)
i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG1, b'\x57')   # 100 readings a second, x y z on
i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG4, b'\x88')   # high resolution, +/- 2 g

def xy(x, y):
    if SERPENTINE and y % 2 == 1:
        return y * MATRIX_WIDTH + (MATRIX_WIDTH - 1 - x)
    return y * MATRIX_WIDTH + x

def read_tilt():
    # the pull of gravity along the board, pointing toward the low side
    ax, ay, az = ustruct.unpack('<hhh', i2c.readfrom_mem(ACCEL_ADDRESS, ACCEL_DATA_REGISTER, 6))
    gx = ax / COUNTS_PER_G
    gy = ay / COUNTS_PER_G
    if SWAP_XY:
        gx, gy = gy, gx
    if FLIP_X:
        gx = -gx
    if FLIP_Y:
        gy = -gy
    return gx, gy

def clear():
    for i in range(NUMBER_PIXELS):
        strip[i] = OFF

# A small random number maker. Starting from the same seed it always makes
# the same numbers, so a level's maze is the same every time.
random_state = 1

def random_number(limit):
    global random_state
    random_state = (random_state * 75 + 74) % 65537
    return random_state % limit

def build_maze(level):
    # returns a list with one True (wall) or False (open) for every pixel
    global random_state
    random_state = MAZE_SEEDS[level - 1]
    walls = [True] * NUMBER_PIXELS
    seen = [False] * (CELLS_ACROSS * CELLS_DOWN)

    # Start in the upper left cell, wander to a cell we have not seen, and
    # knock out the wall between them. When stuck, back up. This visits every
    # cell and leaves exactly one way between any two of them.
    walls[0] = False
    seen[0] = True
    path = [(0, 0)]
    while len(path) > 0:
        cx, cy = path[-1]
        options = []
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < CELLS_ACROSS and 0 <= ny < CELLS_DOWN and not seen[ny * CELLS_ACROSS + nx]:
                options.append((dx, dy))
        if len(options) > 0:
            dx, dy = options[random_number(len(options))]
            nx = cx + dx
            ny = cy + dy
            walls[(2 * cy + dy) * MATRIX_WIDTH + 2 * cx + dx] = False   # the gap between the cells
            walls[2 * ny * MATRIX_WIDTH + 2 * nx] = False               # the new cell
            seen[ny * CELLS_ACROSS + nx] = True
            path.append((nx, ny))
        else:
            path.pop()

    # shortcuts: knock out some more of the walls that are still standing
    closed = []
    for y in range(MATRIX_HEIGHT - 1):
        for x in range(MATRIX_WIDTH - 1):
            if (x % 2) + (y % 2) == 1 and walls[y * MATRIX_WIDTH + x]:
                closed.append((x, y))
    shortcuts = EXTRA_OPENINGS[level - 1]
    if shortcuts > len(closed):
        shortcuts = len(closed)
    for i in range(shortcuts):
        x, y = closed.pop(random_number(len(closed)))
        walls[y * MATRIX_WIDTH + x] = False
    return walls

def draw_text(text):
    # draw the letters in the middle of the matrix
    width = (len(text) * 3 + (len(text) - 1)) * TEXT_SCALE
    left = (MATRIX_WIDTH - width) // 2
    top = (MATRIX_HEIGHT - 5 * TEXT_SCALE) // 2
    clear()
    for n in range(len(text)):
        rows = LETTERS[text[n]]
        for row in range(5):
            for col in range(3):
                if rows[row][col] == "X":
                    for sy in range(TEXT_SCALE):
                        for sx in range(TEXT_SCALE):
                            x = left + (n * 4 + col) * TEXT_SCALE + sx
                            y = top + row * TEXT_SCALE + sy
                            strip[xy(x, y)] = TEXT_COLOR
    strip.write()

def can_roll(walls, x, y):
    return 0 <= x < MATRIX_WIDTH and 0 <= y < MATRIX_HEIGHT and not walls[y * MATRIX_WIDTH + x]

def tilt_direction(g):
    # -1, 0 or 1: which way a tilt pushes, or 0 if it is too small
    if g >= TILT_MIN:
        return 1
    if g <= -TILT_MIN:
        return -1
    return 0

def play_level(level):
    walls = build_maze(level)
    start_x, start_y = CORNERS[(level - 1) % 4]
    hole_x, hole_y = CORNERS[(level + 1) % 4]
    ball_x = start_x * 2
    ball_y = start_y * 2
    hole_x = hole_x * 2
    hole_y = hole_y * 2

    for y in range(MATRIX_HEIGHT):
        for x in range(MATRIX_WIDTH):
            strip[xy(x, y)] = WALL_COLOR if walls[y * MATRIX_WIDTH + x] else OFF
    strip[xy(hole_x, hole_y)] = HOLE_COLOR
    strip[xy(ball_x, ball_y)] = BALL_COLOR
    strip.write()

    moves = 0
    last_step = ticks_ms()
    while ball_x != hole_x or ball_y != hole_y:
        gx, gy = read_tilt()
        size = max(abs(gx), abs(gy))
        now = ticks_ms()
        if size >= TILT_MIN:
            # the harder you tip, the faster the ball rolls
            speed = min(1, (size - TILT_MIN) / (TILT_FULL - TILT_MIN))
            interval = STEP_SLOW_MS - (STEP_SLOW_MS - STEP_FAST_MS) * speed
            if ticks_diff(now, last_step) >= interval:
                # try the direction tipped hardest, then the other one, so the
                # ball slides along a wall instead of sticking to it
                if abs(gx) >= abs(gy):
                    tries = ((tilt_direction(gx), 0), (0, tilt_direction(gy)))
                else:
                    tries = ((0, tilt_direction(gy)), (tilt_direction(gx), 0))
                for dx, dy in tries:
                    if (dx != 0 or dy != 0) and can_roll(walls, ball_x + dx, ball_y + dy):
                        strip[xy(ball_x, ball_y)] = OFF
                        ball_x += dx
                        ball_y += dy
                        strip[xy(ball_x, ball_y)] = BALL_COLOR
                        strip.write()
                        moves += 1
                        last_step = now
                        break
        sleep_ms(10)

    print("Level", level, "solved in", moves, "moves")
    # the ball falls in the hole: flash green
    for i in range(3):
        strip[xy(hole_x, hole_y)] = OFF
        strip.write()
        sleep_ms(150)
        strip[xy(hole_x, hole_y)] = HOLE_COLOR
        strip.write()
        sleep_ms(150)

def show_rainbow():
    # an arch of seven colored bands that, after a moment, flow outward
    band_of = []
    for y in range(MATRIX_HEIGHT):
        for x in range(MATRIX_WIDTH):
            dx = x - RAINBOW_CENTER_X
            dy = y - RAINBOW_CENTER_Y
            distance = (dx * dx + dy * dy) ** 0.5
            band = int((distance - RAINBOW_INNER_RADIUS) / RAINBOW_BAND_WIDTH)
            if distance < RAINBOW_INNER_RADIUS or band >= len(RAINBOW_COLORS):
                band = -1
            band_of.append(band)
    for frame in range(RAINBOW_FRAMES):
        shift = 0
        if frame > 15:
            shift = (frame - 15) // 2
        for y in range(MATRIX_HEIGHT):
            for x in range(MATRIX_WIDTH):
                band = band_of[y * MATRIX_WIDTH + x]
                if band < 0:
                    strip[xy(x, y)] = OFF
                else:
                    strip[xy(x, y)] = RAINBOW_COLORS[(band + shift) % len(RAINBOW_COLORS)]
        strip.write()
        sleep_ms(FRAME_MS)

def play_game():
    for level in range(1, LAST_LEVEL + 1):
        print("Level", level)
        draw_text("L" + str(level))
        sleep_ms(TITLE_MS)
        play_level(level)
    print("You finished all", LAST_LEVEL, "levels!")
    show_rainbow()

while True:
    play_game()
