# moving rainbow
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30
# time between a patten step
BASE_DELAY = 0.005
REPEAT_COUNT = 3
RAINBOW_LENGTH = 7
PERCENT_SMALL_COLOR_WHEEL = round(255/RAINBOW_LENGTH)
PERCENT_COLOR_WHEEL = round(255/NUMBER_PIXELS)

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

BUTTON_PIN_1 = 15
BUTTON_PIN_2 = 14

button_presses = 0 # the count of times the button has been pressed
last_time = 0 # the last time we pressed the button

builtin_led = machine.Pin(25, Pin.OUT)
# The lower left corner of the Pico has a wire that goes through the buttons upper left and the lower right goes to the 3.3 rail

button1 = machine.Pin(BUTTON_PIN_1, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(BUTTON_PIN_2, machine.Pin.IN, machine.Pin.PULL_DOWN)

red = (255, 0, 0)
pink = (255, 128, 128)
orange = (140, 60, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
purple = (255, 0, 255)
white = (128, 128, 128)
colors = (red, orange, yellow, green, blue, cyan, indigo, violet)
color_count = len(colors)
levels = [255, 128, 64, 32, 16, 8, 4, 2, 1]
level_count = len(levels)

mode_list = ['moving rainbow',
             'moving red dot', 'moving blue dot', 'moving green dot',
             'red comet', 'blue comet', 'green comet',
             'candle flicker', 'random dots',
             'bounce yellow', 'bounce cyan', 'bounce purple',
             'running lights red', 'running lights green', 'running lights blue',
             'rainbow cycle',
             'restart']
mode_count = len(mode_list) -1

# This function gets called every time the button is pressed.  The parameter "pin" is used to tell
# which pin is used
def button_pressed_handler(pin):
    global mode, last_time
    new_time = ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
        # print(pin)
        # this is a hack but I can't get the pin ID parameter without vars() or attr()
        pin_num = int(str(pin)[4:6])
        # this works as long as one of the buttons is this one
        if pin_num == BUTTON_PIN_1:
            mode +=1
        else:
            mode -=1
        # wrap around if we get too high
        mode = mode % mode_count
        last_time = new_time

# now we register the handler function when the button is pressed
button1.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)
button2.irq(trigger=machine.Pin.IRQ_FALLING, handler = button_pressed_handler)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)    

# erase the entire strip
def erase():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,0)
        strip.write()

def move_dot(counter, color, delay):
    strip[counter] = color
    strip.write()
    sleep(delay)
    strip[counter] = (0,0,0)

def comet_tail(counter, color, delay):
    for i in range(0, color_count):
        # we start to draw at the head of the commet N levels away from the counter
        target = ((level_count - i - 1) + counter) % NUMBER_PIXELS
        # number to scale by
        scale = (levels[i] / 255)
        strip[target] = (int(color[0]*scale), int(color[1]*scale), int(color[2]*scale))
        # erase the tail
        if counter > 0:
            strip[counter-1] = (0,0,0)
        if counter == NUMBER_PIXELS-1:
            strip[counter] = (0,0,0)
        strip.write()
        sleep(delay)
        
def moving_rainbow(counter, delay):
    for i in range(0, RAINBOW_LENGTH-1):
        color_index = round(i*PERCENT_SMALL_COLOR_WHEEL)
        color = wheel(color_index)
        # print(color_index, color)
        # start at the end and subtract to go backwards and add the counter for offset
        index = RAINBOW_LENGTH-1 - i  + counter
        # print(index)
        if index < NUMBER_PIXELS:
            strip[index] = color    
        strip.write()
    # erase the tail if we are not at the start
    if counter > 0:
        strip[counter-1] = (0,0,0)
        strip.write()
    # turn off the last pixel at the top
    if counter == NUMBER_PIXELS-1:
        strip[counter] = (0,0,0)
    sleep(delay)

def candle(delay):
     green = 50 + randint(0,155)
     red = green + randint(0,50)
     strip[randint(0,NUMBER_PIXELS - 1)] = (red, green, 0)
     strip.write()
     sleep(delay)

def random_color(delay):
    random_offset = randint(0, NUMBER_PIXELS-1)
    random_color = randint(0, 255)
    strip[random_offset] = wheel(random_color)
    strip.write()
    sleep(delay)

HALF_LENGTH = round(NUMBER_PIXELS/2)
def bounce(counter, color, delay):
    if counter < HALF_LENGTH:
        strip[counter] = color
        strip[NUMBER_PIXELS-1 - counter] = color
        strip.write()
        strip[counter] = (0,0,0)
        strip[NUMBER_PIXELS-1 - counter] = (0,0,0)
        sleep(delay)
    else:
        half_counter = counter - HALF_LENGTH
        strip[HALF_LENGTH - half_counter] = color
        strip[HALF_LENGTH + half_counter] = color
        strip.write()
        strip[HALF_LENGTH - half_counter] = (0,0,0)
        strip[HALF_LENGTH + half_counter] = (0,0,0)
        sleep(delay)

def running_lights(counter, color, spacing, delay):
    # how many times to repeat the run
    if counter < 3:
        for c in range(0, spacing):
            for i in range(0, NUMBER_PIXELS-spacing, spacing):
                strip[i+c] = color
                for j in range(1, spacing):
                    strip[c+i+j] = (0,0,0)          
            strip.write()
            sleep(delay)
    else: return

def rainbow_cycle(counter, wait):
    for i in range(0, NUMBER_PIXELS):
        color_index = round(i*PERCENT_COLOR_WHEEL)
        color = wheel(color_index)
        # print(color_index, color)
        strip[(i + counter) % NUMBER_PIXELS] = color
        strip.write()
    sleep(wait)

# Global variables
mode = 0
repeat_count = 0
counter = 0
last_mode = 1
bd = BASE_DELAY
bd2 = bd*2
bd5 = bd*5
while True:
    # print only on change
    if mode != last_mode:
        print('mode=', mode, 'running program', mode_list[mode])
        last_mode = mode
    if mode == 0:
        moving_rainbow(counter, bd)
        
    elif mode == 1:
        move_dot(counter, red, bd5)
    elif mode == 2:
        move_dot(counter, green, bd5)
    elif mode == 3:
        move_dot(counter, blue, bd5)
        
    elif mode == 4:  
        comet_tail(counter, red, bd/5)
    elif mode == 5:  
        comet_tail(counter, green, bd/5)
    elif mode == 6:  
        comet_tail(counter, blue, bd/5)
        
    elif mode == 7:  
        candle(bd5)
    elif mode == 8:  
        random_color(bd5)
        
    elif mode == 9:  
        bounce(counter, yellow, bd5)
    elif mode == 10:  
        bounce(counter, cyan, bd5)
    elif mode == 11:  
        bounce(counter, purple, bd5)

    elif mode == 12: 
        running_lights(counter, red, 4, .2)
    elif mode == 13: 
        running_lights(counter, green, 4, .2)
    elif mode == 14: 
        running_lights(counter, blue, 4, .2)
    
    elif mode == 15: 
        rainbow_cycle(counter, bd2)
    else:
        print('mode', mode, 'not configured')

    # wrap the counter using modulo
    if (counter+1) % (NUMBER_PIXELS):
        counter += 1;
    else:
        # reset the counter to 0
        counter = 0
        # reset the mode to 0
        if mode == mode_count:
            print('mode 0')
            mode = 0
        else:      
            repeat_count += 1
            if repeat_count >= REPEAT_COUNT:
                print('incrementing mode', mode)
                mode += 1
                repeat_count = 0