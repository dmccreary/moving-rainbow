# Lab 14: Accelerometer Bubble
# Filename: 14-accel-bubble.py
# Version: 1.1.0
#
# A 2x2 dot on the matrix acts like a bubble in a level: tilt the kit
# and the dot slides toward the low side. If it slides the wrong way,
# change FLIP_X or FLIP_Y. If left-right and up-down are swapped,
# change SWAP_XY.
# The LED on the Pico board blinks while the program runs. If a reading
# fails, the dot stays where it was and the program keeps going.
# Not yet tried by hand: the tilt needs a person to tip the kit.

from machine import Pin, I2C
from neopixel import NeoPixel
from utime import sleep, sleep_us, ticks_ms, ticks_diff
import ustruct
import config

print("Lab 14: Accelerometer Bubble (version 1.1.0)")

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

# keeping the sensor working
I2C_FREQ = 100000       # a slower clock is less bothered by noise from the matrix wires
MAX_BAD_READINGS = 5    # this many failed readings in a row restarts the sensor
CHECK_MS = 1000         # how often to check on the sensor
HEARTBEAT_MS = 250      # how often the LED on the Pico board blinks

# how the sensor is mounted relative to the matrix
FLIP_X = False
FLIP_Y = True
SWAP_XY = False

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
led = Pin("LED", Pin.OUT)   # the LED on the Pico board

def free_bus():
    # If a program stops in the middle of a reading, the sensor can be left
    # holding the SDA wire low. Nine clock pulses let it finish sending its
    # byte, then a stop signal (SDA going high while SCL is high) frees the bus.
    scl = Pin(ACCEL_SCL_PIN, Pin.OUT, value=1)
    sda = Pin(ACCEL_SDA_PIN, Pin.IN, Pin.PULL_UP)
    for i in range(9):
        scl.value(0)
        sleep_us(5)
        scl.value(1)
        sleep_us(5)
    scl.value(0)
    sda.init(Pin.OUT, value=0)
    sleep_us(5)
    scl.value(1)
    sleep_us(5)
    sda.init(Pin.IN, Pin.PULL_UP)
    sleep_us(5)

def start_sensor():
    global i2c
    free_bus()
    i2c = I2C(ACCEL_I2C_ID, sda=Pin(ACCEL_SDA_PIN), scl=Pin(ACCEL_SCL_PIN), freq=I2C_FREQ)
    try:
        i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG1, b'\x57')   # 100 readings a second, x y z on
        i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG4, b'\x88')   # high resolution, +/- 2 g
    except OSError:
        print("Accelerometer did not answer at address", hex(ACCEL_ADDRESS))

def sensor_has_settings():
    # a dip in the power can reset the chip, which puts it back to sleep
    try:
        return i2c.readfrom_mem(ACCEL_ADDRESS, CTRL_REG1, 1)[0] == 0x57
    except OSError:
        return False

start_sensor()

def xy(x, y):
    if SERPENTINE and y % 2 == 1:
        return y * MATRIX_WIDTH + (MATRIX_WIDTH - 1 - x)
    return y * MATRIX_WIDTH + x

def to_column(g, size):
    # -1 g -> 0, 0 g -> middle, +1 g -> size - 2 (leaves room for the 2x2 dot)
    position = round((g + 1) / 2 * (size - 2))
    return max(0, min(size - 2, position))

ax, ay = 0, 0         # the last good reading: level until the first one
bad_readings = 0
last_check = ticks_ms()
last_blink = ticks_ms()
while True:
    if ticks_diff(ticks_ms(), last_blink) >= HEARTBEAT_MS:
        led.toggle()    # blinks while the program runs
        last_blink = ticks_ms()

    try:
        raw = i2c.readfrom_mem(ACCEL_ADDRESS, ACCEL_DATA_REGISTER, 6)
        ax, ay, az = ustruct.unpack('<hhh', raw)
        bad_readings = 0
    except OSError:
        bad_readings += 1   # keep the last good ax and ay
    # once a second, restart the sensor if it stopped answering or lost its settings
    if ticks_diff(ticks_ms(), last_check) >= CHECK_MS:
        last_check = ticks_ms()
        if bad_readings >= MAX_BAD_READINGS or not sensor_has_settings():
            print("Accelerometer not working - restarting it")
            start_sensor()
            bad_readings = 0

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
