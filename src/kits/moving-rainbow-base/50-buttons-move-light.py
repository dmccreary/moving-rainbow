# Use the buttons on the controller to "move a light up and down the strip
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint
import config

NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

BUTTON_PIN_1 = 15 #Button 1 uses pin 15 on the Raspberry Pi circuit board (closer to board)
BUTTON_PIN_2 = 14 #Button 2 uses pin 14 on the Raspberry Pi circuit board (closer to edge)

button1_presses = 0 # the count of times the button has been pressed
button2_presses = 0
last_time = 0 # the last time we pressed the button

builtin_led = machine.Pin(25, Pin.OUT)
# The lower left corner of the Pico has a wire that goes through the buttons upper left and the lower right goes to the 3.3 rail

button1 = machine.Pin(BUTTON_PIN_1, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(BUTTON_PIN_2, machine.Pin.IN, machine.Pin.PULL_UP)

#Most of these color definitions are not needed here, but they came with the "copy/paste" of code I used
red = (255, 0, 0)
red_med = (32, 0, 0)
red_light = (8, 0, 0)
off = (0, 0, 0)
orange = (140, 60, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
white = (128, 128, 128)
colors = (red, orange, yellow, green, blue, cyan, indigo, violet)
color_count = len(colors)

HALF_LENGTH = round(NUMBER_PIXELS/2)
position = HALF_LENGTH


# This function gets called every time the button is pressed.  The parameter "pin" is used to tell
# which pin is used
def button_pressed_handler(pin):
#    global mode, last_time
    global position, last_time, button1_presses, button2_presses
    new_time = ticks_ms()
    # if it has been more than 1/5 of a second since the last event, we have a new event

    if (new_time - last_time) > 200:
        # this is a hack but I can't get the pin ID parameter without vars() or attr()
        #pin_num = int(str(pin)[4:6])
        pin_num = int(str(pin)[8:10])
        # this works as long as one of the buttons is this one
        if pin_num == BUTTON_PIN_1:
            position +=1
            button1_presses +=1
        else: #we know that a button has been pressed, and it's not button 1, so it must be button 2
            position -=1
            button2_presses +=1

        # wrap around if we get too high
        position = position % NUMBER_PIXELS
        last_time = new_time
        print('button 1 pressed ', button1_presses, 'times; button 2 pressed', button2_presses, 'times')

# now we register the handler function when the button is pressed
button1.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
button2.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)


# erase the entire strip
def erase():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,0)

def move_dot(lp, counter, color, delay):
    strip[lp] = (0,0,0)
    strip[counter] = color
    strip.write()
    sleep(delay)

erase()
last_position = 0

while True:
    if position != last_position:
        move_dot(last_position, position, red_med, .1)
        last_position = position
