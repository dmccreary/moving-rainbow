# Christmas Hat

This hat uses the classic Christmas colors: red, green, and white.
The program below has 10 festive patterns. Press the two buttons on
your kit to move forward and backward through the patterns.

!!! tip "Pixel says..."
    Let's light this up! Red and green are opposite colors, so they
    really pop next to each other. Try the candy-cane chase first —
    it's my favorite!

## What you'll need

- A Moving Rainbow base kit with a 30-pixel LED strip
- The two-button hat wiring (buttons on pins 15 and 14)
- A foam-core hat to mount the strip on

## How to Use the Buttons

- **Button 1** moves forward to the next pattern.
- **Button 2** moves backward to the previous pattern.

When you reach the last pattern, the next press wraps back to the first one.

## The Patterns

This program cycles through 10 patterns:

1. Candy-cane chase (red and white moving stripes)
2. Red and green blink (the whole strip flips colors)
3. Falling snow (white pixels twinkle on and off)
4. Green color wipe (green fills the strip one pixel at a time)
5. Red color wipe (red fills the strip one pixel at a time)
6. Red comet (a red dot with a fading tail)
7. Green comet (a green dot with a fading tail)
8. Running lights (red and green spaced evenly)
9. Sparkle (random red, green, and white dots)
10. Gold theater chase (gold lights march along the strip)

## The Code

Copy this code into a file named `main.py` on your Pico. It runs all
10 patterns and lets you switch between them with the two buttons.

```python
# Christmas Hat - 10 red, green, and white patterns
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint

NEOPIXEL_PIN = 0       # the data pin for the LED strip
NUMBER_PIXELS = 30     # how many LEDs are on the hat
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

BUTTON_PIN_1 = 15      # next pattern
BUTTON_PIN_2 = 14      # previous pattern

# Christmas color palette (red, green, blue) values from 0 to 255
red = (255, 0, 0)
green = (0, 255, 0)
white = (120, 120, 120)
gold = (180, 120, 0)
off = (0, 0, 0)

# Brightness levels used to draw a fading comet tail
levels = [255, 128, 64, 32, 16, 8]

mode = 0               # which pattern is playing
mode_count = 10        # how many patterns we have
counter = 0            # steps the animation forward
last_time = 0          # the last time a button was pressed

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

# Pattern 0: moving red and white stripes, like a candy cane.
def candy_cane(counter, delay):
    for i in range(NUMBER_PIXELS):
        if ((i + counter) // 3) % 2 == 0:
            strip[i] = red
        else:
            strip[i] = white
    strip.write()
    sleep(delay)

# Pattern 1: flip the whole strip between red and green.
def red_green_blink(counter, delay):
    color = red if counter % 2 == 0 else green
    for i in range(NUMBER_PIXELS):
        strip[i] = color
    strip.write()
    sleep(delay * 6)

# Pattern 2: random white pixels twinkle like falling snow.
def snow(delay):
    erase()
    for i in range(6):
        strip[randint(0, NUMBER_PIXELS - 1)] = white
    strip.write()
    sleep(delay * 2)

# Pattern 3 and 4: fill the strip one pixel at a time with one color.
def color_wipe(counter, color, delay):
    strip[counter] = color
    strip.write()
    sleep(delay)
    if counter == NUMBER_PIXELS - 1:
        erase()

# Patterns 5 and 6: a bright dot with a fading tail.
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

# Pattern 7: red and green lights spaced evenly that march along.
def running_lights(counter, delay):
    for i in range(NUMBER_PIXELS):
        if (counter + i) % 4 == 0:
            strip[i] = red
        elif (counter + i) % 4 == 2:
            strip[i] = green
        else:
            strip[i] = off
    strip.write()
    sleep(delay)

# Pattern 8: random red, green, and white sparkles.
def sparkle(delay):
    erase()
    palette = (red, green, white)
    for i in range(8):
        strip[randint(0, NUMBER_PIXELS - 1)] = palette[randint(0, 2)]
    strip.write()
    sleep(delay)

# Pattern 9: gold lights that step forward, like a theater marquee.
def theater_chase(counter, delay):
    for i in range(NUMBER_PIXELS):
        if (i + counter) % 3 == 0:
            strip[i] = gold
        else:
            strip[i] = off
    strip.write()
    sleep(delay * 2)

# The main loop picks the right pattern for the current mode.
while True:
    if mode == 0:
        candy_cane(counter, 0.08)
    elif mode == 1:
        red_green_blink(counter, 0.08)
    elif mode == 2:
        snow(0.08)
    elif mode == 3:
        color_wipe(counter, green, 0.05)
    elif mode == 4:
        color_wipe(counter, red, 0.05)
    elif mode == 5:
        comet(counter, red, 0.04)
    elif mode == 6:
        comet(counter, green, 0.04)
    elif mode == 7:
        running_lights(counter, 0.1)
    elif mode == 8:
        sparkle(0.1)
    elif mode == 9:
        theater_chase(counter, 0.08)

    counter += 1
    if counter >= NUMBER_PIXELS:
        counter = 0
```

You should see the strip light up in red, green, and white. Each
button press jumps to a new festive pattern.

!!! tip "Pixel's tip"
    If your strip has more or fewer than 30 LEDs, just change the
    `NUMBER_PIXELS` number near the top. Everything else still works!

## Try It Yourself

- Change the `gold` color values to make a warmer or cooler gold.
- Add a new pattern that uses only white pixels for a "winter" look.
- Make the candy-cane stripes wider by changing the `// 3` to `// 5`.
