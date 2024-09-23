from machine import Pin
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 6
ROWS = 8
COLS = 8
NUMBER_PIXELS = ROWS * COLS

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
# Allocate memory for the NeoPixel matrix
matrix = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# (0,0) is at the lower left
def write_pixel(x, y, value):
    if y >= 0 and y < ROWS and x >=0 and x < COLS:
        # odd count rows 1, 3, 5 the wire goes from bottum
        if y % 2: 
            strip[(y+1)*ROWS - x - 1] = value             
        else: # even count rows, 0, 2, 4 the wire goes from the top down up
            strip[y*ROWS + x] = value

# draw four colors at each corner of the matrix
write_pixel(0, 0, (255, 0, 0)) # draw a red pixel at the top left corner
write_pixel(7, 0, (0, 255, 0)) # draw a green pixel at the lower right
write_pixel(0, 7, (0, 0, 255)) # draw a blue pixel at the top left corner
write_pixel(7, 7, (255, 255, 255)) # draw a white pixel at the upper right corner
strip.write()
