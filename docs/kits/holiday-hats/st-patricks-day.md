# St. Patrick's Day Hat

This hat celebrates St. Patrick's Day with green, gold, and white.
The program below has 8 lucky patterns. Press the two buttons on your
kit to move forward and backward through them.

!!! tip "Pixel says..."
    Top o' the morning! Green is made from pure G in our (R, G, B)
    colors. Gold mixes a lot of red with some green. Let's find a
    pot of color at the end of your rainbow!

## What you'll need

- A Moving Rainbow base kit with a 30-pixel LED strip
- The two-button hat wiring (buttons on pins 15 and 14)
- A foam-core hat to mount the strip on

## How to Use the Buttons

- **Button 1** moves forward to the next pattern.
- **Button 2** moves backward to the previous pattern.

When you reach the last pattern, the next press wraps back to the first one.

## The Patterns

This program cycles through 8 patterns:

1. Green color wipe (green fills the strip one pixel at a time)
2. Gold comet (a gold dot with a fading tail)
3. Green comet (a green dot with a fading tail)
4. Shamrock chase (green and white moving stripes)
5. Gold sparkle (random gold dots, like coins)
6. Green and gold running lights
7. Rainbow (because every St. Patrick's Day needs a rainbow!)
8. Lucky blink (the whole strip flips between green and gold)

## The Code

Copy this code into a file named `main.py` on your Pico. It runs all
8 patterns and lets you switch between them with the two buttons.

```python
# St. Patrick's Day Hat - green, gold, and white patterns
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint

NEOPIXEL_PIN = 0       # the data pin for the LED strip
NUMBER_PIXELS = 30     # how many LEDs are on the hat
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

BUTTON_PIN_1 = 15      # next pattern
BUTTON_PIN_2 = 14      # previous pattern

# St. Patrick's Day color palette (red, green, blue) values from 0 to 255
green = (0, 255, 0)
gold = (200, 140, 0)
white = (120, 120, 120)
off = (0, 0, 0)

# Brightness levels used to draw a fading comet tail
levels = [255, 128, 64, 32, 16, 8]

mode = 0               # which pattern is playing
mode_count = 8         # how many patterns we have
counter = 0            # steps the animation forward
last_time = 0          # the last time a button was pressed

# A color wheel turns a number from 0 to 255 into a rainbow color.
def wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

# This runs every time a button is pressed.
def button_pressed_handler(pin):
    global mode, last_time
    new_time = ticks_ms()
    # ignore presses closer than 1/5 of a second apart (debounce)
    if (new_time - last_time) > 200:
        pin_num = int(str(pin)[4:6])
        if pin_num == BUTTON_PIN_1:
            mode += 1      # button 1 goes forward
        else:
            mode -= 1      # button 2 goes backward
        mode = mode % mode_count   # wrap around at the ends
        last_time = new_time

button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_DOWN)
button1.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed_handler)

# Turn every pixel off.
def erase():
    for i in range(NUMBER_PIXELS):
        strip[i] = off
    strip.write()

# Pattern 0: fill the strip one pixel at a time with green.
def color_wipe(counter, color, delay):
    strip[counter] = color
    strip.write()
    sleep(delay)
    if counter == NUMBER_PIXELS - 1:
        erase()

# Patterns 1 and 2: a bright dot with a fading tail.
def comet(counter, color, delay):
    erase()
    for i in range(len(levels)):
        pos = (counter - i) % NUMBER_PIXELS
        scale = levels[i] / 255
        strip[pos] = (int(color[0] * scale),
                      int(color[1] * scale),
                      int(color[2] * scale))
    strip.write()
    sleep(delay)

# Pattern 3: moving green and white stripes.
def shamrock_chase(counter, delay):
    for i in range(NUMBER_PIXELS):
        if ((i + counter) // 3) % 2 == 0:
            strip[i] = green
        else:
            strip[i] = white
    strip.write()
    sleep(delay)

# Pattern 4: random gold sparkles, like scattered coins.
def gold_sparkle(delay):
    erase()
    for i in range(8):
        strip[randint(0, NUMBER_PIXELS - 1)] = gold
    strip.write()
    sleep(delay)

# Pattern 5: green and gold lights spaced evenly that march along.
def running_lights(counter, delay):
    for i in range(NUMBER_PIXELS):
        if (counter + i) % 4 == 0:
            strip[i] = green
        elif (counter + i) % 4 == 2:
            strip[i] = gold
        else:
            strip[i] = off
    strip.write()
    sleep(delay)

# Pattern 6: a full moving rainbow.
def rainbow(counter, delay):
    for i in range(NUMBER_PIXELS):
        color_index = (i * 256 // NUMBER_PIXELS + counter * 8) % 256
        strip[i] = wheel(color_index)
    strip.write()
    sleep(delay)

# Pattern 7: flip the whole strip between green and gold.
def lucky_blink(counter, delay):
    color = green if counter % 2 == 0 else gold
    for i in range(NUMBER_PIXELS):
        strip[i] = color
    strip.write()
    sleep(delay * 6)

# The main loop picks the right pattern for the current mode.
while True:
    if mode == 0:
        color_wipe(counter, green, 0.05)
    elif mode == 1:
        comet(counter, gold, 0.04)
    elif mode == 2:
        comet(counter, green, 0.04)
    elif mode == 3:
        shamrock_chase(counter, 0.08)
    elif mode == 4:
        gold_sparkle(0.1)
    elif mode == 5:
        running_lights(counter, 0.1)
    elif mode == 6:
        rainbow(counter, 0.05)
    elif mode == 7:
        lucky_blink(counter, 0.08)

    counter += 1
    if counter >= NUMBER_PIXELS:
        counter = 0
```

You should see the strip glow in green and gold, with a surprise
rainbow pattern in the middle of the cycle.

!!! tip "Pixel's tip"
    Green is the "luckiest" color to make on a NeoPixel. It uses only
    the green part of each pixel, so it draws less power than white.
    That means your battery lasts longer!

## Try It Yourself

- Change the `gold` values to make a brighter or deeper gold.
- Add a "lucky number" pattern that lights up exactly 7 green pixels.
- Make the rainbow move faster by changing `counter * 8` to `counter * 16`.
