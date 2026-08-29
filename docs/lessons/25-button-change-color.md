# Button-Controlled Color

Now let's connect your two buttons to the LED strip. Button 1 will move
forward through a list of colors, and Button 2 will move backward.

!!! tip "Pixel says..."
    This is where buttons and light finally meet! You've read buttons and
    you've lit up strips — now you get to control one with the other.

## What you'll learn

- How to store a list of colors and step through it with an index
- How to use the modulo operator (`%`) to wrap around from the last color back to the first
- How to fill an entire strip with one color

## What you'll need

- Your Pico, NeoPixel strip, and two buttons from the earlier lessons
- The kit's `config.py` file

## Stepping Through a List

A **list index** is a number that points at one item in a list. Here, the
index starts at `0` (red) and moves up by one each time Button 1 is
pressed:

```python
color_index = (color_index + 1) % len(colors)
```

The `% len(colors)` part is the **modulo operator**. It divides by the
length of the list and keeps only the remainder, which wraps the index
back to `0` once it goes past the last color. Button 2 does the same
thing in reverse, subtracting one instead of adding.

## The Full Program

```python
# Press Button 1 to move forward through a list of colors.
# Press Button 2 to move backward through the list.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

# A small list of colors to cycle through.
colors = [
    (255, 0, 0),     # red
    (255, 80, 0),    # orange
    (255, 255, 0),   # yellow
    (0, 255, 0),     # green
    (0, 0, 255),     # blue
    (130, 0, 200),   # purple
]
color_index = 0

DEBOUNCE_MS = 200
last_press = 0


def fill_strip(color):
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()


def button_handler(pin):
    global color_index, last_press
    now = ticks_ms()
    if now - last_press < DEBOUNCE_MS:
        return

    if pin == button1:
        color_index = (color_index + 1) % len(colors)
    else:
        color_index = (color_index - 1) % len(colors)

    fill_strip(colors[color_index])
    print("color index:", color_index)


button1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

fill_strip(colors[color_index])   # show the first color right away

while True:
    sleep(1)
```

Press Button 1 a few times and watch the strip step through red, orange,
yellow, green, blue, and purple. Press Button 2 to step back the other
way. Keep pressing Button 2 past red — the strip wraps around to purple.

!!! info "Pixel thinks..."
    That wraparound is the modulo operator at work again. `-1 % 6` in
    Python gives `5`, not a negative number — which is exactly why the
    index lands back on the last color in the list instead of breaking.

## Try It Yourself

- Add two more colors to the `colors` list.
- Change `fill_strip` so it only lights up the first half of the strip.

## Check Your Understanding

1. What does `color_index` keep track of?
2. What happens when `color_index` would go below `0`? Why?
3. What does `fill_strip` do to every pixel in the strip?
4. What would you change to add a seventh color to the list?

!!! success "You've got this!"
    You just built a color picker with two buttons. Next, you'll control
    something you can't see directly: speed.

**What's next:** in [Button-Controlled Speed](26-button-change-speed.md),
your buttons will speed up and slow down a moving pixel.
