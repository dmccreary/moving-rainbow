# Test 09: Accelerometer Print
# Filename: 09-accel-print.py
# Version: 1.1.0
#
# Reads a LIS3DH accelerometer and prints x, y and z in g.
# Lay the kit flat: z should be about 1.0 and x and y close to 0.
# Tilt it and watch the numbers change.
# The LED on the Pico board blinks while the program runs. If a reading
# fails, the program prints a message and keeps going instead of stopping.
# Not yet tested on hardware.

from machine import Pin, I2C
from utime import sleep, sleep_us, ticks_ms, ticks_diff
import ustruct
import config

print("Test 09: Accelerometer Print (version 1.1.0)")

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

# keeping the sensor working
I2C_FREQ = 100000       # a slower clock is less bothered by electrical noise
MAX_BAD_READINGS = 5    # this many failed readings in a row restarts the sensor
CHECK_MS = 1000         # how often to check on the sensor

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
        # the chip starts powered down; 0x57 = 100 readings a second with x, y and z on
        i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG1, b'\x57')
        # 0x88 = high resolution, +/- 2 g, and hold each reading steady while we read it
        i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG4, b'\x88')
    except OSError:
        print("Accelerometer did not answer at address", hex(ACCEL_ADDRESS))

def sensor_has_settings():
    # a dip in the power can reset the chip, which puts it back to sleep
    try:
        return i2c.readfrom_mem(ACCEL_ADDRESS, CTRL_REG1, 1)[0] == 0x57
    except OSError:
        return False

start_sensor()
try:
    print("WHO_AM_I:", hex(i2c.readfrom_mem(ACCEL_ADDRESS, WHO_AM_I_REGISTER, 1)[0]), "(0x33 is a LIS3DH)")
except OSError:
    print("WHO_AM_I: no answer. Check the wiring and run 02-probe.py")

bad_readings = 0
last_check = ticks_ms()
while True:
    led.toggle()    # blinks while the program runs
    try:
        raw = i2c.readfrom_mem(ACCEL_ADDRESS, ACCEL_DATA_REGISTER, 6)
    except OSError:
        raw = None
    if raw is None:
        bad_readings += 1
        print("no reading (", bad_readings, "in a row )")
    else:
        bad_readings = 0
        x, y, z = ustruct.unpack('<hhh', raw)
        print("x: %5.2f  y: %5.2f  z: %5.2f" % (x / COUNTS_PER_G, y / COUNTS_PER_G, z / COUNTS_PER_G))

    # once a second, restart the sensor if it stopped answering or lost its settings
    if ticks_diff(ticks_ms(), last_check) >= CHECK_MS:
        last_check = ticks_ms()
        if bad_readings >= MAX_BAD_READINGS or not sensor_has_settings():
            print("Accelerometer not working - restarting it")
            start_sensor()
            bad_readings = 0
    sleep(0.2)
