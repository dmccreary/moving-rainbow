# Module: Kit Helpers (shared by program 13 and the programs it loads)
# Filename: kit.py
# Version: 1.1.0
#
# Sets up the matrix, the accelerometer and the two mode buttons one time,
# and gives every mode the same helpers: xy(), clear(), fade_pixels(),
# read_tilt(), draw_text(), wait() and a list of colors.
#
# wait() is how a mode sleeps. It also watches the two mode buttons. When
# program 13 has turned the buttons on (mode_buttons_on) and one is pressed,
# wait() raises ModeChange and program 13 loads the next or previous mode.
# When a mode runs on its own (programs 11 and 12) the buttons are off.
#
# wait() also blinks the LED on the Pico board. If the LED stops blinking,
# the program has stopped. read_tilt() never stops the program: if the
# sensor does not answer, it uses the last good reading and restarts the
# sensor (see read_accel()).
# Not yet tested on hardware.

from machine import Pin, I2C
from neopixel import NeoPixel
from utime import sleep_ms, sleep_us, ticks_ms, ticks_diff
import ustruct
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
MATRIX_WIDTH = config.MATRIX_WIDTH
MATRIX_HEIGHT = config.MATRIX_HEIGHT
SERPENTINE = config.SERPENTINE
BUTTON_PIN_1 = config.BUTTON_PIN_1
BUTTON_PIN_2 = config.BUTTON_PIN_2
ACCEL_I2C_ID = config.ACCEL_I2C_ID
ACCEL_SDA_PIN = config.ACCEL_SDA_PIN
ACCEL_SCL_PIN = config.ACCEL_SCL_PIN
ACCEL_ADDRESS = config.ACCEL_ADDRESS

# LIS3DH registers
CTRL_REG1 = 0x20
CTRL_REG4 = 0x23
ACCEL_DATA_REGISTER = 0x28 | 0x80   # the 0x80 bit makes the chip step through x, y, z
COUNTS_PER_G = 16384
CTRL_REG1_VALUE = 0x57      # 100 readings a second, x y z on
CTRL_REG4_VALUE = 0x88      # high resolution, +/- 2 g

# keeping the sensor working
I2C_FREQ = 100000           # a slower clock is less bothered by noise from the matrix wires
MAX_BAD_READINGS = 5        # this many failed readings in a row restarts the sensor
MAX_SAME_READINGS = 100     # a working sensor always wiggles a little, so this many
                            # exactly equal readings in a row means it is stuck
CHECK_MS = 1000             # how often to check on the sensor

# the LED on the Pico board blinks while the program runs
HEARTBEAT_MS = 250

# how the sensor is mounted relative to the matrix (same as programs 10, 11 and 12)
FLIP_X = False
FLIP_Y = True
SWAP_XY = False

# a button press counts once, then is ignored for this many milliseconds
DEBOUNCE_MS = 200

WIDTH = MATRIX_WIDTH
HEIGHT = MATRIX_HEIGHT

# colors. A single pixel can be bright, so the biggest number is 48.
# Modes that light many pixels at once use these dimmed down.
OFF = (0, 0, 0)
RED = (48, 0, 0)
ORANGE = (48, 14, 0)
YELLOW = (40, 32, 0)
GREEN = (0, 48, 0)
BLUE = (0, 0, 48)
INDIGO = (12, 0, 48)
VIOLET = (30, 0, 40)
PINK = (48, 8, 24)
WHITE = (28, 28, 28)
TEAL = (0, 40, 30)
LIME = (20, 48, 0)
SKY = (0, 24, 48)
RAINBOW = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]
PALETTE = RAINBOW + [PINK, WHITE, TEAL, LIME, SKY]
TEXT_COLOR = (16, 16, 4)

# the digits 0 to 9 and the letter L, 3 pixels wide and 5 tall
LETTERS = {
    "L": ("X..", "X..", "X..", "X..", "XXX"),
    "0": ("XXX", "X.X", "X.X", "X.X", "XXX"),
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

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# the buttons connect the pin to GND, so a press reads 0
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

led = Pin("LED", Pin.OUT)     # "LED" works on the Pico, Pico W and Pico 2
last_blink = ticks_ms()

def heartbeat():
    # flip the LED on the Pico board every HEARTBEAT_MS
    global last_blink
    now = ticks_ms()
    if ticks_diff(now, last_blink) >= HEARTBEAT_MS:
        led.toggle()
        last_blink = now

def free_bus():
    # If a program stops in the middle of a reading, the sensor can be left
    # holding the SDA wire low, and every reading after that fails. Nine
    # clock pulses let it finish sending its byte, then a stop signal
    # (SDA going high while SCL is high) frees the bus.
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
    # free the bus, set up I2C and give the sensor its settings
    global i2c
    free_bus()
    i2c = I2C(ACCEL_I2C_ID, sda=Pin(ACCEL_SDA_PIN), scl=Pin(ACCEL_SCL_PIN), freq=I2C_FREQ)
    try:
        i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG1, bytes([CTRL_REG1_VALUE]))
        i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG4, bytes([CTRL_REG4_VALUE]))
        return True
    except OSError:
        print("Accelerometer did not answer at address", hex(ACCEL_ADDRESS))
        return False

def sensor_has_settings():
    # A dip in the power can reset the sensor. A reset sensor goes to sleep
    # and keeps sending its last reading, so tilting seems to do nothing.
    try:
        return i2c.readfrom_mem(ACCEL_ADDRESS, CTRL_REG1, 1)[0] == CTRL_REG1_VALUE
    except OSError:
        return False

start_sensor()
last_good = (0, 0, COUNTS_PER_G)    # until the first reading: lying flat
last_raw = None
bad_readings = 0
same_readings = 0
last_check = ticks_ms()

def read_accel():
    # Returns the raw x, y and z counts. If the sensor does not answer or
    # sends nonsense, this returns the last good reading instead of stopping
    # the program. Once a second it checks on the sensor and restarts it if
    # the readings failed, got stuck, or the sensor lost its settings.
    global last_good, last_raw, bad_readings, same_readings, last_check
    try:
        raw = i2c.readfrom_mem(ACCEL_ADDRESS, ACCEL_DATA_REGISTER, 6)
    except OSError:
        raw = None
    # all zeros or all ones is what a missing or sleeping sensor sends
    if raw is None or raw == b'\x00' * 6 or raw == b'\xff' * 6:
        bad_readings += 1
    else:
        bad_readings = 0
        if raw == last_raw:
            same_readings += 1
        else:
            same_readings = 0
        last_raw = raw
        last_good = ustruct.unpack('<hhh', raw)

    now = ticks_ms()
    if ticks_diff(now, last_check) >= CHECK_MS:
        last_check = now
        problem = None
        if bad_readings >= MAX_BAD_READINGS:
            problem = "stopped answering"
        elif same_readings >= MAX_SAME_READINGS:
            problem = "got stuck"
        elif not sensor_has_settings():
            problem = "lost its settings"
        if problem:
            print("Accelerometer", problem, "- restarting it")
            start_sensor()
            bad_readings = 0
            same_readings = 0
    return last_good


class ModeChange(Exception):
    # raised by wait() when a mode button is pressed: args[0] is 1 for the
    # next mode (button 1) or -1 for the previous mode (button 2)
    pass


mode_buttons_on = False
button1_was_down = False
button2_was_down = False
last_press = ticks_ms()

def check():
    # Look at the two buttons. If one was just pressed and the mode buttons
    # are on, raise ModeChange.
    global button1_was_down, button2_was_down, last_press
    if not mode_buttons_on:
        return
    down1 = button1.value() == 0
    down2 = button2.value() == 0
    pressed1 = down1 and not button1_was_down
    pressed2 = down2 and not button2_was_down
    button1_was_down = down1
    button2_was_down = down2
    now = ticks_ms()
    if (pressed1 or pressed2) and ticks_diff(now, last_press) > DEBOUNCE_MS:
        last_press = now
        if pressed1:
            raise ModeChange(1)
        raise ModeChange(-1)

def wait(ms):
    # sleep for ms milliseconds, but notice a button press right away
    heartbeat()
    check()
    while ms > 0:
        step = min(ms, 10)
        sleep_ms(step)
        ms -= step
        heartbeat()
        check()

def xy(x, y):
    if SERPENTINE and y % 2 == 1:
        return y * MATRIX_WIDTH + (MATRIX_WIDTH - 1 - x)
    return y * MATRIX_WIDTH + x

def clear():
    for i in range(NUMBER_PIXELS):
        strip[i] = OFF

def fade_pixels(keep):
    # keep is 0 to 255: how much of each pixel's color stays. Called every
    # frame, it leaves a fading trail behind anything that moves.
    for i in range(NUMBER_PIXELS):
        r, g, b = strip[i]
        if r or g or b:
            strip[i] = (r * keep // 256, g * keep // 256, b * keep // 256)

def dim(color, brightness):
    # brightness is 0.0 to 1.0
    return (int(color[0] * brightness), int(color[1] * brightness), int(color[2] * brightness))

def read_tilt():
    # the pull of gravity along the board, as (gx, gy) in g, pointing
    # toward the low side. When the board stands upright the pull is about 1.
    ax, ay, az = read_accel()
    gx = ax / COUNTS_PER_G
    gy = ay / COUNTS_PER_G
    if SWAP_XY:
        gx, gy = gy, gx
    if FLIP_X:
        gx = -gx
    if FLIP_Y:
        gy = -gy
    return gx, gy

def draw_text(text, color=TEXT_COLOR):
    # draw the letters in the middle of the matrix and show them
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
                            strip[xy(x, y)] = color
    strip.write()
