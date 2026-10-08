# Moving Rainbow Configuration file
# Filename: config.py
# Version: 1.0.0
#
# This file contains the hardware configuration for the Tilt-a-Rainbow
# Mini kit. It is imported by each program.

# 8x8 NeoPixel matrix (64 pixels)
NEOPIXEL_PIN = 0
MATRIX_WIDTH = 8
MATRIX_HEIGHT = 8
NUMBER_PIXELS = MATRIX_WIDTH * MATRIX_HEIGHT
# Some 8x8 panels are wired in a zig-zag: row 0 runs left to right,
# row 1 runs right to left, and so on. This panel is NOT: every row runs
# left to right. (Checked on the real panel: pixel 8 sits right below
# pixel 0.) Run 06-walk-pixels.py to see the pixel order.
SERPENTINE = False

# The color number the programs use when ALL 64 pixels are lit at once.
# 64 pixels at (20, 20, 20) draw about 300 mA, safely under the 500 mA a
# USB port supplies. Programs that light only a few pixels can use bigger
# numbers.
LEVEL = 20

# Two mode buttons, each wired from its GPIO pin to GND
BUTTON_PIN_1 = 14
BUTTON_PIN_2 = 15

# Accelerometer on I2C bus 0 (GP16 is SDA, GP17 is SCL)
# LIS3DH accelerometer. 0x19 is the usual address (0x18 if SDO is tied to GND).
# Run 02-probe.py to check.
ACCEL_I2C_ID = 0
ACCEL_SDA_PIN = 16
ACCEL_SCL_PIN = 17
ACCEL_ADDRESS = 0x19
