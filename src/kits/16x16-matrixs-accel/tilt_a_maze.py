# Module: Tilt-a-Maze (program 12, and mode 10 of program 13)
# Filename: tilt_a_maze.py
# Version: 1.0.0
#
# Tilt the board to roll the red ball through a light blue maze and into
# the green hole in the opposite corner. Each level is a little harder:
# the early mazes have shortcuts, and level 9 has only one way through.
# Before each level the matrix shows its number (L1 to L9). Finish level 9
# and a rainbow appears, then the game starts over.
# Run it on its own with 12-tilt-a-maze.py.
# The ball rolls toward the low side. If it rolls the wrong way, change
# FLIP_X, FLIP_Y or SWAP_XY in kit.py.
# Not yet tested on hardware.

from utime import ticks_ms, ticks_diff
import kit

# the matrix, from kit.py
NUMBER_PIXELS = kit.NUMBER_PIXELS
MATRIX_WIDTH = kit.WIDTH
MATRIX_HEIGHT = kit.HEIGHT
strip = kit.strip
xy = kit.xy
clear = kit.clear

# colors. About half the pixels are walls, so the wall color stays dim:
# the whole maze draws about 300 mA, well under what USB supplies.
WALL_COLOR = (3, 10, 18)        # light blue
BALL_COLOR = (40, 0, 0)         # red
HOLE_COLOR = (0, 40, 0)         # green
OFF = kit.OFF

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

TITLE_MS = 1500

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
        gx, gy = kit.read_tilt()
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
        kit.wait(10)

    print("Level", level, "solved in", moves, "moves")
    # the ball falls in the hole: flash green
    for i in range(3):
        strip[xy(hole_x, hole_y)] = OFF
        strip.write()
        kit.wait(150)
        strip[xy(hole_x, hole_y)] = HOLE_COLOR
        strip.write()
        kit.wait(150)

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
        kit.wait(FRAME_MS)

def play_game():
    for level in range(1, LAST_LEVEL + 1):
        print("Level", level)
        kit.draw_text("L" + str(level))
        kit.wait(TITLE_MS)
        play_level(level)
    print("You finished all", LAST_LEVEL, "levels!")
    show_rainbow()

def run(settings=None):
    while True:
        play_game()
