# Bounce a ball around a NeoPixel Matrix
from neopixel import NeoPixel
from utime import sleep
from urandom import randint

NEOPIXEL_PIN = 6
ROWS = 8
COLS = 8
NUMBER_PIXELS = ROWS * COLS
strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# matrix = [[0 for _ in range(cols)] for _ in range(rows)]
def clear():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,0)
    strip.write()

def write_pixel(x, y, value):
    if y >= 0 and y < ROWS and x >=0 and x < COLS:
        # odd count rows 1, 3, 5 the wire goes from bottup
        if x % 2: 
            strip[(x+1)*ROWS - y - 1] = value             
        else: # even count rows, 0, 2, 4 the wire goes from the top down up
            strip[x*ROWS + y] = value

def show():
    strip.write()

brightness=1
x=0
y=4
dx = 1
dy = 2
counter = 0
while True:
    if x <= 0:
        dx = 1
    if y <= 0:
        dy = 1
    if x >= COLS-1:
        dx = -1
    if y >= ROWS-1:
        dy = -1
    print(x,y)
    if counter < 100:
        write_pixel(x, y, (randint(0,25),randint(0,25),randint(0,25))) # random
    elif counter < 200:
        write_pixel(x, y, (0,brightness,0)) # blue
    elif counter < 300:
        write_pixel(x, y, (0,0,brightness)) # blue
    show()
    x += dx + randint(0,1)
    y += dy
    counter += 1
    if counter > 300:
        counter = 0
    if not counter % 150:
        x += 1
    sleep(.1)
