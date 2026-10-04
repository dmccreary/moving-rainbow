# Test 10: Accelerometer Bubble
# Filename: 10-accel-bubble.py
# Version: 1.0.0
#
# A 2x2 dot on the matrix acts like a bubble in a level: tilt the kit
# and the dot slides toward the low side. If it slides the wrong way,
# change FLIP_X or FLIP_Y. If left-right and up-down are swapped,
# change SWAP_XY.
# Not yet tested on hardware.

from machine import Pin, I2C
from neopixel import NeoPixel
from utime import sleep
import ustruct
import config

print("Test 10: Accelerometer Bubble (version 1.0.0)")

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

# how the sensor is mounted relative to the matrix
FLIP_X = False
FLIP_Y = True
SWAP_XY = False

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
i2c = I2C(ACCEL_I2C_ID, sda=Pin(ACCEL_SDA_PIN), scl=Pin(ACCEL_SCL_PIN), freq=400000)
i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG1, b'\x57')   # 100 readings a second, x y z on
i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG4, b'\x88')   # high resolution, +/- 2 g

def xy(x, y):
    if SERPENTINE and y % 2 == 1:
        return y * MATRIX_WIDTH + (MATRIX_WIDTH - 1 - x)
    return y * MATRIX_WIDTH + x

def to_column(g, size):
    # -1 g -> 0, 0 g -> middle, +1 g -> size - 2 (leaves room for the 2x2 dot)
    position = round((g + 1) / 2 * (size - 2))
    return max(0, min(size - 2, position))

while True:
    raw = i2c.readfrom_mem(ACCEL_ADDRESS, ACCEL_DATA_REGISTER, 6)
    ax, ay, az = ustruct.unpack('<hhh', raw)
    gx = ax / COUNTS_PER_G
    gy = ay / COUNTS_PER_G
    if SWAP_XY:
        gx, gy = gy, gx
    if FLIP_X:
        gx = -gx
    if FLIP_Y:
        gy = -gy
    col = to_column(gx, MATRIX_WIDTH)
    row = to_column(gy, MATRIX_HEIGHT)

    for i in range(NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    for dx in range(2):
        for dy in range(2):
            strip[xy(col + dx, row + dy)] = (0, 40, 40)
    strip.write()
    sleep(0.03)
