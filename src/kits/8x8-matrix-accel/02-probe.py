# Lab 02: Hardware Probe
# Filename: 02-probe.py
# Version: 1.0.0
#
# A detailed check of the Pico, the two buttons and the LIS3DH accelerometer.
# It prints board info, checks every pin level, scans the I2C bus, confirms
# the chip with its WHO_AM_I register, takes a few readings and ends with
# TEST PASS or TEST FAIL. Lay the kit flat and keep it still while it runs.
# Run it from your computer with ./run-probe.sh
# Tested on the kit's Pico: TEST PASS.
#
# Wiring under test:
#   Matrix data -> GPIO0  (the matrix is checked by programs 04 to 08)
#   Accel SDA   -> GPIO16 (I2C0 SDA)
#   Accel SCL   -> GPIO17 (I2C0 SCL)
#   Button 1    -> GPIO14 to GND
#   Button 2    -> GPIO15 to GND
#
# GPIO16 and GPIO17 are a valid I2C0 pair on the RP2040: GPIO16 can only be
# SDA and GPIO17 can only be SCL. machine.I2C(0, ...) raises "bad SCL pin"
# if the roles are reversed.
#
# Pull-ups: the raw pin level check always turns on the RP2040's internal
# weak pull-up (about 50-80 kOhm) so a stuck-low reading means something (a
# short or a miswired pin). The I2C scan does NOT turn it on, so it tests the
# pull-ups on the accelerometer board itself.

import sys
import os
import gc
import machine
import ustruct
from utime import sleep_ms
import config

print("Lab 02: Hardware Probe (version 1.0.0)")

# hardware settings from config.py
ACCEL_I2C_ID = config.ACCEL_I2C_ID
ACCEL_SDA_PIN = config.ACCEL_SDA_PIN
ACCEL_SCL_PIN = config.ACCEL_SCL_PIN
ACCEL_ADDRESS = config.ACCEL_ADDRESS
BUTTON_PIN_1 = config.BUTTON_PIN_1
BUTTON_PIN_2 = config.BUTTON_PIN_2

# LIS3DH facts
LIS3DH_ADDRESS_LOW = 0x18    # SDO tied low
LIS3DH_ADDRESS_HIGH = 0x19   # SDO tied high (the usual breakout default)
WHO_AM_I_REG = 0x0F
WHO_AM_I_EXPECTED = 0x33     # a LIS3DH always reports 0x33 here
CTRL_REG1 = 0x20
CTRL_REG4 = 0x23
STATUS_REG = 0x27
DATA_READY_BIT = 0x08        # new x, y and z readings are waiting
DATA_REG = 0x28 | 0x80       # the 0x80 bit makes the chip step through x, y, z
COUNTS_PER_G = 16384         # the 16-bit reading at the +/- 2 g range
SAMPLES = 10

# other sensors that could be on the bus instead, to help name what we find
OTHER_PARTS = {
    0x68: "MPU-6050 (GY-521)",
    0x69: "MPU-6050 (AD0 high)",
    0x53: "ADXL345",
    0x1E: "HMC5883L compass (GY-273)",
}

print("=" * 50)
print("Board / system info")
print("=" * 50)
u = os.uname()
print("sysname :", u.sysname)
print("nodename:", u.nodename)
print("release :", u.release)
print("version :", u.version)
print("machine :", u.machine)
print("platform:", sys.platform)

gc.collect()
free = gc.mem_free()
alloc = gc.mem_alloc()
print()
print("RAM free : {} bytes ({:.1f} KB)".format(free, free / 1024))
print("RAM used : {} bytes ({:.1f} KB)".format(alloc, alloc / 1024))
print("RAM total: {} bytes ({:.1f} KB)".format(free + alloc, (free + alloc) / 1024))

try:
    fs = os.statvfs("/")
    block_size = fs[0]
    total_blocks = fs[2]
    free_blocks = fs[3]
    flash_total = block_size * total_blocks
    flash_free = block_size * free_blocks
    print()
    print("Flash total: {} bytes ({:.1f} KB)".format(flash_total, flash_total / 1024))
    print("Flash free : {} bytes ({:.1f} KB)".format(flash_free, flash_free / 1024))
    print("Flash used : {} bytes ({:.1f} KB)".format(flash_total - flash_free, (flash_total - flash_free) / 1024))
except OSError as e:
    print("Flash info unavailable:", e)

print()
print("=" * 50)
print("Button pin check (GPIO{} and GPIO{}, internal pull-ups enabled)".format(BUTTON_PIN_1, BUTTON_PIN_2))
print("=" * 50)
button1 = machine.Pin(BUTTON_PIN_1, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(BUTTON_PIN_2, machine.Pin.IN, machine.Pin.PULL_UP)
buttons_ok = True
for number, button, pin in ((1, button1, BUTTON_PIN_1), (2, button2, BUTTON_PIN_2)):
    level = button.value()
    print("Button {} (GPIO{}) idle level: {} ({})".format(
        number, pin, level,
        "1 = not pressed, as expected" if level == 1 else "0 = held down, or the wire is shorted to GND"))
    if level == 0:
        buttons_ok = False
if not buttons_ok:
    print("WARNING: a button reads pressed. Let go of the buttons and run the probe again.")
    print("If it still reads 0, that pin is shorted to GND or the button is wired wrong.")

print()
print("=" * 50)
print("Raw pin level check (SCL=GPIO{}, SDA=GPIO{}, internal pull-ups enabled)".format(ACCEL_SCL_PIN, ACCEL_SDA_PIN))
print("=" * 50)
scl_raw = machine.Pin(ACCEL_SCL_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
sda_raw = machine.Pin(ACCEL_SDA_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
sleep_ms(10)
print("SCL idle level:", scl_raw.value(), "(1 = pulled high as expected, 0 = stuck low / shorted / no pull-up reaching this net)")
print("SDA idle level:", sda_raw.value(), "(1 = pulled high as expected, 0 = stuck low / shorted / no pull-up reaching this net)")
lines_ok = scl_raw.value() == 1 and sda_raw.value() == 1
if not lines_ok:
    print("WARNING: a line is stuck low. With only the Pico's internal pull-up")
    print("in the circuit, this points to a short, a reversed/miswired pin,")
    print("or a dead/backwards module pulling the line down - not a missing")
    print("external pull-up.")

def find_lis3dh(devices):
    if ACCEL_ADDRESS in devices:
        return ACCEL_ADDRESS
    if LIS3DH_ADDRESS_HIGH in devices:
        return LIS3DH_ADDRESS_HIGH
    if LIS3DH_ADDRESS_LOW in devices:
        return LIS3DH_ADDRESS_LOW
    return None


def report_devices(devices):
    print("Found {} device(s):".format(len(devices)))
    for addr in devices:
        marker = ""
        if addr == LIS3DH_ADDRESS_LOW:
            marker = "  <-- LIS3DH (SDO low)"
        elif addr == LIS3DH_ADDRESS_HIGH:
            marker = "  <-- LIS3DH (SDO high)"
        elif addr in OTHER_PARTS:
            marker = "  <-- " + OTHER_PARTS[addr] + " (not a LIS3DH)"
        print("  decimal {:3d}  hex 0x{:02X}{}".format(addr, addr, marker))


def check_who_am_i(i2c, found_address):
    print()
    print("=" * 50)
    print("WHO_AM_I check (register 0x{:02X} at device 0x{:02X})".format(WHO_AM_I_REG, found_address))
    print("=" * 50)
    if found_address != ACCEL_ADDRESS:
        print("NOTE: config.py ACCEL_ADDRESS is 0x{:02X} but the chip is at 0x{:02X}.".format(ACCEL_ADDRESS, found_address))
        print("Set ACCEL_ADDRESS = 0x{:02X} in config.py.".format(found_address))
    try:
        who_am_i = i2c.readfrom_mem(found_address, WHO_AM_I_REG, 1)[0]
    except OSError as e:
        print("WHO_AM_I read failed:", e)
        print()
        print("TEST FAIL - device acked its address but did not respond to a register read")
        return
    print("WHO_AM_I returned: 0x{:02X}".format(who_am_i))
    if who_am_i != WHO_AM_I_EXPECTED:
        print()
        print("TEST FAIL - device answered at 0x{:02X} but WHO_AM_I was 0x{:02X}, not 0x33".format(found_address, who_am_i))
        print("(programs 13 and 14 are written for a LIS3DH)")
        return
    check_readings(i2c, found_address)


def check_readings(i2c, found_address):
    print()
    print("=" * 50)
    print("Readings ({} samples, keep the kit still)".format(SAMPLES))
    print("=" * 50)
    i2c.writeto_mem(found_address, CTRL_REG1, b'\x57')   # 100 readings a second, x y z on
    i2c.writeto_mem(found_address, CTRL_REG4, b'\x88')   # high resolution, +/- 2 g
    reg1 = i2c.readfrom_mem(found_address, CTRL_REG1, 1)[0]
    reg4 = i2c.readfrom_mem(found_address, CTRL_REG4, 1)[0]
    print("CTRL_REG1 read back: 0x{:02X} (wrote 0x57)".format(reg1))
    print("CTRL_REG4 read back: 0x{:02X} (wrote 0x88)".format(reg4))
    registers_ok = reg1 == 0x57 and reg4 == 0x88

    sleep_ms(50)
    status = i2c.readfrom_mem(found_address, STATUS_REG, 1)[0]
    print("STATUS_REG: 0x{:02X} ({})".format(status, "new data ready" if status & DATA_READY_BIT else "no new data"))
    data_ready = (status & DATA_READY_BIT) != 0

    xs = []
    ys = []
    zs = []
    for i in range(SAMPLES):
        x, y, z = ustruct.unpack('<hhh', i2c.readfrom_mem(found_address, DATA_REG, 6))
        xs.append(x / COUNTS_PER_G)
        ys.append(y / COUNTS_PER_G)
        zs.append(z / COUNTS_PER_G)
        sleep_ms(50)
    avg_x = sum(xs) / SAMPLES
    avg_y = sum(ys) / SAMPLES
    avg_z = sum(zs) / SAMPLES
    strength = (avg_x * avg_x + avg_y * avg_y + avg_z * avg_z) ** 0.5
    spread = max(max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs))
    print("average x: {:5.2f} g   y: {:5.2f} g   z: {:5.2f} g".format(avg_x, avg_y, avg_z))
    print("total pull: {:.2f} g (about 1.00 when still)".format(strength))
    print("spread    : {:.3f} g (small when still)".format(spread))
    axes = [("x", avg_x), ("y", avg_y), ("z", avg_z)]
    name, value = max(axes, key=lambda a: abs(a[1]))
    print("The {} axis points {} ({:.2f} g).".format(name, "down" if value > 0 else "up", value))

    gravity_ok = 0.8 < strength < 1.2
    steady_ok = spread < 0.1
    print()
    if registers_ok and data_ready and gravity_ok and steady_ok:
        if buttons_ok and lines_ok:
            print("TEST PASS - LIS3DH found at 0x{:02X}, WHO_AM_I confirms 0x33, readings look right".format(found_address))
        else:
            print("TEST FAIL - the accelerometer works, but a button or I2C pin reading above was wrong")
    else:
        print("TEST FAIL - LIS3DH found, but:")
        if not registers_ok:
            print("  - a control register did not read back what was written")
        if not data_ready:
            print("  - the chip never reported new data")
        if not gravity_ok:
            print("  - the total pull is not about 1 g (is the kit moving?)")
        if not steady_ok:
            print("  - the readings jump around (is the kit moving, or the wires loose?)")


print()
print("=" * 50)
print("I2C{} scan (SDA=GPIO{}, SCL=GPIO{}, no internal pull-ups - testing board's own pull-ups)".format(ACCEL_I2C_ID, ACCEL_SDA_PIN, ACCEL_SCL_PIN))
print("=" * 50)
scl = machine.Pin(ACCEL_SCL_PIN, machine.Pin.IN)
sda = machine.Pin(ACCEL_SDA_PIN, machine.Pin.IN)
i2c = machine.I2C(ACCEL_I2C_ID, sda=sda, scl=scl, freq=400000)

devices = i2c.scan()

if devices:
    report_devices(devices)
    found_address = find_lis3dh(devices)
    if found_address is None:
        print()
        print("TEST FAIL - no device at 0x18 or 0x19 (the LIS3DH's possible addresses)")
    else:
        check_who_am_i(i2c, found_address)
else:
    print("No I2C devices found on the hardware I2C{} pins as wired.".format(ACCEL_I2C_ID))
    print()
    print("=" * 50)
    print("Fallback: bit-banged scan with SDA/SCL swapped (GPIO{}=SCL, GPIO{}=SDA)".format(ACCEL_SDA_PIN, ACCEL_SCL_PIN))
    print("=" * 50)
    print("This checks for the accelerometer's SCL/SDA wires landing on the opposite")
    print("pins from what the RP2040's I2C{} hardware block requires.".format(ACCEL_I2C_ID))
    swapped_i2c = machine.SoftI2C(
        scl=machine.Pin(ACCEL_SDA_PIN, machine.Pin.IN),
        sda=machine.Pin(ACCEL_SCL_PIN, machine.Pin.IN),
        freq=100000,
    )
    swapped_devices = swapped_i2c.scan()
    if not swapped_devices:
        print("No I2C devices found either way.")
        print("Check wiring: VCC->3.3V OUT, GND->GND, and SDA/SCL to GPIO{}/GPIO{} (either order)".format(ACCEL_SDA_PIN, ACCEL_SCL_PIN))
        print("TEST FAIL")
    else:
        report_devices(swapped_devices)
        found_address = find_lis3dh(swapped_devices)
        if found_address is None:
            print()
            print("TEST FAIL - a device responded, but not at 0x18 or 0x19")
        else:
            print()
            print("DIAGNOSIS: the accelerometer IS present and wired correctly point-to-point,")
            print("but its SCL wire lands on GPIO{} and its SDA wire lands on GPIO{} -".format(ACCEL_SDA_PIN, ACCEL_SCL_PIN))
            print("the opposite of what the RP2040's I2C{} hardware block requires".format(ACCEL_I2C_ID))
            print("(GPIO{}=SDA, GPIO{}=SCL). Swap the two wires on the breadboard.".format(ACCEL_SDA_PIN, ACCEL_SCL_PIN))
            check_who_am_i(swapped_i2c, found_address)
