# Test 11: Sloshing Water
# Filename: 11-sloshing-water.py
# Version: 1.0.0
#
# The matrix is a square pan seen from the side, half full of blue water.
# Stand the board upright and the bottom half fills with water. Rock or
# tilt the board and the water sloshes back and forth, then settles with a
# level surface. The amount of water never changes: always 128 pixels.
# If the water falls toward the wrong side, change FLIP_X, FLIP_Y or
# SWAP_XY (they are the same settings as in program 10).
# Not yet tested on hardware.

from machine import Pin, I2C
from neopixel import NeoPixel
from utime import sleep_ms, ticks_ms, ticks_diff
import ustruct
import config

print("Test 11: Sloshing Water (version 1.0.0)")

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

# the water: half the pixels. Only half the pixels are lit and only in blue,
# so these numbers draw about 300 mA, well under what USB supplies.
WATER_PIXELS = NUMBER_PIXELS // 2
WATER_COLOR = (0, 0, 24)
SURFACE_COLOR = (0, 10, 48)     # a brighter line along the top of the water
SURFACE_THICKNESS = 1.0         # in pixels

# the water follows the pull of gravity like a weight on a spring,
# so it overshoots and rings back and forth when you rock the board
SPRING = 90         # bigger = faster sloshing (90 is about 1.5 slosh a second)
DAMPING = 2.5       # bigger = the sloshing dies out sooner
MIN_TILT = 0.2      # pull along the board below this (nearly flat): water stays put
MAX_PULL = 1.5      # ignore the extra push of hard shakes

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
i2c = I2C(ACCEL_I2C_ID, sda=Pin(ACCEL_SDA_PIN), scl=Pin(ACCEL_SCL_PIN), freq=400000)
i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG1, b'\x57')   # 100 readings a second, x y z on
i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG4, b'\x88')   # high resolution, +/- 2 g

def xy(x, y):
    if SERPENTINE and y % 2 == 1:
        return y * MATRIX_WIDTH + (MATRIX_WIDTH - 1 - x)
    return y * MATRIX_WIDTH + x

# For every pixel, work out once: its strip number, how far it is from the
# center of the pan (across and down), and a tiny nudge so no two pixels
# are ever exactly the same depth.
center_x = (MATRIX_WIDTH - 1) / 2
center_y = (MATRIX_HEIGHT - 1) / 2
pixel_index = []
across = []
down = []
nudge = []
for row in range(MATRIX_HEIGHT):
    for col in range(MATRIX_WIDTH):
        pixel_index.append(xy(col, row))
        across.append(col - center_x)
        down.append(row - center_y)
        nudge.append(0.0007 * col + 0.0011 * row)

def read_pull():
    # which way is downhill along the board, and how strong is the pull
    ax, ay, az = ustruct.unpack('<hhh', i2c.readfrom_mem(ACCEL_ADDRESS, ACCEL_DATA_REGISTER, 6))
    gx = ax / COUNTS_PER_G
    gy = ay / COUNTS_PER_G
    if SWAP_XY:
        gx, gy = gy, gx
    if FLIP_X:
        gx = -gx
    if FLIP_Y:
        gy = -gy
    size = (gx * gx + gy * gy) ** 0.5
    if size > MAX_PULL:
        gx = gx * MAX_PULL / size
        gy = gy * MAX_PULL / size
        size = MAX_PULL
    return gx, gy, size

def draw_water(nx, ny):
    # nx, ny is the downhill direction. A pixel's depth is how far it sits
    # downhill. The deepest half of the pixels are water, so the surface
    # always lands where exactly half the pan is full.
    depth = [across[i] * nx + down[i] * ny + nudge[i] for i in range(NUMBER_PIXELS)]
    cutoff = sorted(depth)[NUMBER_PIXELS - WATER_PIXELS]
    for i in range(NUMBER_PIXELS):
        below_surface = depth[i] - cutoff
        if below_surface < 0:
            strip[pixel_index[i]] = (0, 0, 0)
        elif below_surface < SURFACE_THICKNESS:
            strip[pixel_index[i]] = SURFACE_COLOR
        else:
            strip[pixel_index[i]] = WATER_COLOR
    strip.write()

# the spring: sx, sy is where the water thinks "down" is, vx, vy is how fast
# that is changing, and target is where gravity says it should be
sx = 0.0
sy = 1.0
vx = 0.0
vy = 0.0
target_x = 0.0
target_y = 1.0
nx = 0.0
ny = 1.0
last_time = ticks_ms()

while True:
    gx, gy, size = read_pull()
    if size >= MIN_TILT:
        target_x = gx
        target_y = gy

    now = ticks_ms()
    dt = ticks_diff(now, last_time) / 1000
    last_time = now
    if dt > 0.05:
        dt = 0.05

    vx += (SPRING * (target_x - sx) - DAMPING * vx) * dt
    vy += (SPRING * (target_y - sy) - DAMPING * vy) * dt
    sx += vx * dt
    sy += vy * dt

    length = (sx * sx + sy * sy) ** 0.5
    if length > 0.05:
        nx = sx / length
        ny = sy / length

    draw_water(nx, ny)
    sleep_ms(5)
