# Moving Rainbow Configuration file
# Filename: config.py
# Version: 1.0.0
#
# This file contains the hardware configuration for the Tilt-a-Rainbow
# kit. It is imported by each program.

# 16x16 NeoPixel matrix (256 pixels)
NEOPIXEL_PIN = 0
MATRIX_WIDTH = 16
MATRIX_HEIGHT = 16
NUMBER_PIXELS = MATRIX_WIDTH * MATRIX_HEIGHT
# Many 16x16 panels are wired in a zig-zag: row 0 runs left to right,
# row 1 runs right to left, and so on. This panel is NOT: every row runs
# left to right. (Test 10 showed it: with True, the two rows of the dot
# moved in opposite directions.) Run 06-walk-pixels.py to see the pixel order.
SERPENTINE = False

# Largest color number that is safe when ALL 256 pixels are lit at once.
# 256 pixels at (8, 8, 8) draw about 480 mA, close to what a USB port supplies.
# Programs that light only a few pixels can use bigger numbers.
LEVEL = 8

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
