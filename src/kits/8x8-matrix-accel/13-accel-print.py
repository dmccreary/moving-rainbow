# Lab 13: Accelerometer Print
# Filename: 13-accel-print.py
# Version: 1.0.0
#
# Reads a LIS3DH accelerometer and prints x, y and z in g.
# Lay the kit flat: z should be about 1.0 and x and y close to 0.
# Tilt it and watch the numbers change.

from machine import Pin, I2C
from utime import sleep
import ustruct
import config

print("Lab 13: Accelerometer Print (version 1.0.0)")

# hardware settings from config.py
ACCEL_I2C_ID = config.ACCEL_I2C_ID
ACCEL_SDA_PIN = config.ACCEL_SDA_PIN
ACCEL_SCL_PIN = config.ACCEL_SCL_PIN
ACCEL_ADDRESS = config.ACCEL_ADDRESS

# LIS3DH registers
WHO_AM_I_REGISTER = 0x0F
CTRL_REG1 = 0x20
CTRL_REG4 = 0x23
ACCEL_DATA_REGISTER = 0x28 | 0x80   # the 0x80 bit makes the chip step through x, y, z
COUNTS_PER_G = 16384    # the 16-bit reading at the +/- 2 g range

i2c = I2C(ACCEL_I2C_ID, sda=Pin(ACCEL_SDA_PIN), scl=Pin(ACCEL_SCL_PIN), freq=400000)

# the chip starts powered down; 0x57 = 100 readings a second with x, y and z on
i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG1, b'\x57')
# 0x88 = high resolution, +/- 2 g, and hold each reading steady while we read it
i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG4, b'\x88')
print("WHO_AM_I:", hex(i2c.readfrom_mem(ACCEL_ADDRESS, WHO_AM_I_REGISTER, 1)[0]), "(0x33 is a LIS3DH)")

while True:
    raw = i2c.readfrom_mem(ACCEL_ADDRESS, ACCEL_DATA_REGISTER, 6)
    x, y, z = ustruct.unpack('<hhh', raw)
    print("x: %5.2f  y: %5.2f  z: %5.2f" % (x / COUNTS_PER_G, y / COUNTS_PER_G, z / COUNTS_PER_G))
    sleep(0.2)
