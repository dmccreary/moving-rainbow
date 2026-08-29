from machine import Pin
from neopixel import NeoPixel
from utime import sleep, localtime
# get the configuration information
import config

np = config.NUMBER_PIXELS
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), np)

sec_bits = [0,0,0,0,0,0]
min_bits = [0,0,0,0,0,0]
hr_bits = [0,0,0,0,0,0]

def decimal_to_binary(n, a):
    global sec_bits
    for i in range(0,6):
        if n % 2:
            a[i] = 1
        else:
            a[i] = 0
        ## n halfed
        n //= 2

def display_binary(binary, index, color):
    for i in range(0, 6):
        # print(i, ' ', end='')
        if binary[i] == 1:
            strip[index+i] = color
        else:
            strip[index+i] = (0,0,0)
    strip.write()

# light mark and write
def display_mark(loc):
    strip[loc] = (5,5,5)
    strip.write()

# update from the first time
# sec
display_mark(0)
display_mark(7)

# min
display_mark(9)
display_mark(16)

# min
display_mark(19)
display_mark(26)

now = localtime()
hour = now[3]
# use AM/PM 12 hour time
if hour > 12:
    hour = hour - 12
minute = now[4]

# this is not working
decimal_to_binary(minute, min_bits)
print('initial min:', minute, min_bits)
display_binary(min_bits, 10, (0,10,0))

decimal_to_binary(hour, hr_bits)
print('initial hour:', hour, hr_bits)
display_binary(hr_bits, 20, (0,0,10))

while True:
    now = localtime()
    hour = now[3]
    # use AM/PM 12 hour time
    if hour > 12:
        hour = hour - 12
    minute = now[4]
    sec = now[5]
    print(hour, ':', minute, ' ', sec, sep='')
    strip.write()
    decimal_to_binary(sec, sec_bits)
    print('sec:', sec, sec_bits)
    display_binary(sec_bits, 1, (10,0,0))
    if sec == 60:
        minute = minute + 1
        sec = 0
        decimal_to_binary(minute, min_bits)
        print('min:', minute, min_bits)
        display_binary(min_bits, 10, (0,10,0))
        if minute == 60:
            decimal_to_binary(hour, hr_bits)
            print('hour:', hour, hr_bits)
            display_binary(hr_bits, 20, (0,0,10))
            hour = hour + 1
            minute = 0
            if hour == 24:
                hour = 0
    sleep(1)