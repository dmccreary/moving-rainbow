from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint


NEOPIXEL_PIN = 0
ROWS = 16
COLS = 16
NUMBER_PIXELS = ROWS * COLS
# Allocate memory for the NeoPixel matrix
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def write_pixel(x, y, value):
    if y >= 0 and y < ROWS and x >=0 and x < COLS:
        # odd count rows 1, 3, 5 the wire goes from bottup
        if x % 2: 
            strip[(x+1)*ROWS - y - 1] = value             
        else: # even count rows, 0, 2, 4 the wire goes from the top down up
            strip[x*ROWS + y] = value    

# Create a varuabke to store the delay 
delay = .002

# position
x=randint(0, 16)
y=randint(0, 16)
# directions
dx = randint(-1,3)
dy = randint(-1,3)

counter = 0
while True:
    print(x,y)
    write_pixel(x, y, (1, 0, 0))
    x = x + dx
    y = y + dy
    # randomly change directions every 50 times
    if counter % 50 == 0:
        dx = randint(0,3) - 1
        dy = randint(0,3) - 1
    if dx == 0 and dy == 0:
        dx = 1
        dy = 1
    if x < 0:
        x = 0
        dx = -dx
    if x > 15:
        x = 15
        dx = -dx
    if y < 0:
        y = 0
        dy = -dy
    if y > 15:
        y = 15
        dy = -dy
    write_pixel(x, y, (0, 0, 10))
    strip.write()
    sleep(.1)
    counter += 1
    
    
