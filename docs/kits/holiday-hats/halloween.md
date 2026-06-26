# Halloween Hat

This hat glows with spooky Halloween colors: orange, purple, and a
ghostly green. The program below has 8 patterns. Press the two buttons
on your kit to move forward and backward through them.

!!! tip "Pixel says..."
    Boo! Orange and purple are the classic Halloween pair. Mix a lot
    of red with a little green to get orange. Mix red and blue to get
    purple. Let's make something spooky!

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

1. Pumpkin glow (the whole strip pulses orange)
2. Orange and purple stripes that move
3. Ghost fade (white pixels fade in and out)
4. Orange comet (a bright dot with a fading tail)
5. Purple comet (a bright dot with a fading tail)
6. Spooky sparkle (random orange, purple, and green dots)
7. Candy corn wave (orange, then white, then yellow stripes)
8. Creeping shadows (a dark gap moves along a glowing strip)

## The Code

Copy this code into a file named `main.py` on your Pico. It runs all
8 patterns and lets you switch between them with the two buttons.

```python
# Halloween Hat - orange, purple, and ghostly green patterns
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint

NEOPIXEL_PIN = 0       # the data pin for the LED strip
NUMBER_PIXELS = 30     # how many LEDs are on the hat
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

BUTTON_PIN_1 = 15      # next pattern
BUTTON_PIN_2 = 14      # previous pattern

# Halloween color palette (red, green, blue) values from 0 to 255
orange = (255, 80, 0)
purple = (128, 0, 255)
green = (0, 120, 0)
yellow = (200, 160, 0)
white = (120, 120, 120)
off = (0, 0, 0)

# Brightness levels used to draw a fading comet tail
levels = [255, 128, 64, 32, 16, 8]

mode = 0               # which pattern is playing
mode_count = 8         # how many patterns we have
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

# Pattern 0: the whole strip slowly pulses orange, like a pumpkin.
def pumpkin_glow(counter, delay):
    # use a triangle wave to fade brightness up and down
    step = counter % 20
    level = step if step < 10 else 20 - step
    scale = level / 10
    color = (int(orange[0] * scale), int(orange[1] * scale), 0)
    for i in range(NUMBER_PIXELS):
        strip[i] = color
    strip.write()
    sleep(delay)

# Pattern 1: moving orange and purple stripes.
def orange_purple_stripes(counter, delay):
    for i in range(NUMBER_PIXELS):
        if ((i + counter) // 3) % 2 == 0:
            strip[i] = orange
        else:
            strip[i] = purple
    strip.write()
    sleep(delay)

# Pattern 2: white pixels fade in and out like passing ghosts.
def ghost_fade(counter, delay):
    step = counter % 20
    level = step if step < 10 else 20 - step
    scale = level / 10
    color = (int(white[0] * scale), int(white[1] * scale), int(white[2] * scale))
    erase()
    for i in range(0, NUMBER_PIXELS, 5):
        strip[i] = color
    strip.write()
    sleep(delay)

# Patterns 3 and 4: a bright dot with a fading tail.
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

# Pattern 5: random orange, purple, and green sparkles.
def spooky_sparkle(delay):
    erase()
    palette = (orange, purple, green)
    for i in range(8):
        strip[randint(0, NUMBER_PIXELS - 1)] = palette[randint(0, 2)]
    strip.write()
    sleep(delay)

# Pattern 6: orange, white, and yellow stripes, like candy corn.
def candy_corn(counter, delay):
    candy = (orange, white, yellow)
    for i in range(NUMBER_PIXELS):
        strip[i] = candy[((i + counter) // 2) % 3]
    strip.write()
    sleep(delay)

# Pattern 7: a dark gap creeps along a glowing orange strip.
def creeping_shadows(counter, delay):
    for i in range(NUMBER_PIXELS):
        strip[i] = orange
    # turn off a moving group of pixels to make a shadow
    for i in range(4):
        strip[(counter + i) % NUMBER_PIXELS] = off
    strip.write()
    sleep(delay)

# The main loop picks the right pattern for the current mode.
while True:
    if mode == 0:
        pumpkin_glow(counter, 0.06)
    elif mode == 1:
        orange_purple_stripes(counter, 0.08)
    elif mode == 2:
        ghost_fade(counter, 0.06)
    elif mode == 3:
        comet(counter, orange, 0.04)
    elif mode == 4:
        comet(counter, purple, 0.04)
    elif mode == 5:
        spooky_sparkle(0.1)
    elif mode == 6:
        candy_corn(counter, 0.1)
    elif mode == 7:
        creeping_shadows(counter, 0.08)

    counter += 1
    if counter >= NUMBER_PIXELS:
        counter = 0
```

You should see the strip glow orange and purple, with ghostly white
pixels and a creepy moving shadow.

!!! tip "Pixel's tip"
    Bright orange and purple use a lot of power. If your hat runs on
    batteries, the pulsing patterns (like Pumpkin Glow) will last
    longer than the patterns that light every pixel at full brightness.

## More Halloween Patterns

Want even more spooky effects? The full Halloween kit has a power-saving
version with patterns like witch chase, monster eyes, and potion bubbles.

[See the full Halloween Patterns kit](../halloween/index.md)

## Try It Yourself

- Change the `purple` color to a deeper "midnight" purple.
- Add a "lightning" pattern that flashes the whole strip white for one frame.
- Make the creeping shadow wider by lighting off 6 pixels instead of 4.
