# Module: Kit Helpers (shared by programs 15 to 18 and the modes they load)
# Filename: kit.py
# Version: 1.0.0
#
# Sets up the matrix, the accelerometer and the two mode buttons one time,
# and gives every mode the same helpers: xy(), clear(), fade_pixels(),
# read_tilt(), draw_text(), wait() and a list of colors.
#
# wait() is how a mode sleeps. It also watches the two mode buttons. When
# program 18 has turned the buttons on (mode_buttons_on) and one is pressed,
# wait() raises ModeChange and program 18 loads the next or previous mode.
# When a mode runs on its own (programs 15 and 16) the buttons are off.

from machine import Pin, I2C
from neopixel import NeoPixel
from utime import sleep_ms, ticks_ms, ticks_diff
import ustruct
import config
from font import LETTERS

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

# how the sensor is mounted relative to the matrix (same as program 14)
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

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# the buttons connect the pin to GND, so a press reads 0
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

i2c = I2C(ACCEL_I2C_ID, sda=Pin(ACCEL_SDA_PIN), scl=Pin(ACCEL_SCL_PIN), freq=400000)
i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG1, b'\x57')   # 100 readings a second, x y z on
i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG4, b'\x88')   # high resolution, +/- 2 g


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
    check()
    while ms > 0:
        step = min(ms, 10)
        sleep_ms(step)
        ms -= step
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
    ax, ay, az = ustruct.unpack('<hhh', i2c.readfrom_mem(ACCEL_ADDRESS, ACCEL_DATA_REGISTER, 6))
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
    # draw the letters in the middle of the matrix and show them.
    # The letter shapes come from font.py. Two letters fit: "L1" or "12".
    width = len(text) - 1                   # one dark column between letters
    for letter in text:
        width += len(LETTERS[letter][0])
    left = (MATRIX_WIDTH - width) // 2
    top = (MATRIX_HEIGHT - 5) // 2
    clear()
    for letter in text:
        rows = LETTERS[letter]
        for row in range(5):
            for col in range(len(rows[row])):
                x = left + col
                if rows[row][col] == "X" and 0 <= x < MATRIX_WIDTH:
                    strip[xy(x, top + row)] = color
        left += len(rows[0]) + 1
    strip.write()
