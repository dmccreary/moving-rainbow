# Buttons Move a Pixel

In earlier lessons, pixels moved on their own, one step per loop. In this
lesson, a pixel only moves when you tell it to — Button 1 moves it forward,
Button 2 moves it backward.

!!! tip "Pixel says..."
    This one feels different the moment you try it. You're not just
    watching an animation anymore — you're driving it!

## What you'll learn

- How to store a pixel's position in a variable instead of a loop counter
- How to move that position forward or backward from a button interrupt
- How to erase the old pixel before drawing the new one

## What you'll need

- Your Pico, NeoPixel strip, and two buttons from the earlier lessons
- The kit's `config.py` file

## Position as a Variable

Every moving-pixel lesson so far used a loop counter that always went up.
Here, `position` is a regular variable that the button handler changes
directly — up for Button 1, down for Button 2. The main loop's only job is
to draw whatever `position` currently is.

```python
# Use the buttons on the controller to move a light up and down the strip.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

position = config.NUMBER_PIXELS // 2   # start in the middle of the strip
DEBOUNCE_MS = 200
last_press = 0


def button_handler(pin):
    global position, last_press
    now = ticks_ms()
    if now - last_press < DEBOUNCE_MS:
        return

    if pin == button1:
        position += 1
    else:
        position -= 1

    position = position % config.NUMBER_PIXELS   # wrap around the ends
    last_press = now


button1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

last_position = position
strip[position] = (25, 0, 0)
strip.write()

while True:
    if position != last_position:
        strip[last_position] = (0, 0, 0)   # erase the old spot
        strip[position] = (25, 0, 0)       # light the new spot
        strip.write()
        last_position = position
    sleep(0.02)
```

Press Button 1 a few times — the red pixel steps forward. Press Button 2 —
it steps back. Keep pressing past either end of the strip, and it wraps
around to the other side.

!!! info "Pixel thinks..."
    Notice the main loop checks `if position != last_position` before
    doing anything. Redrawing the same pixel over and over would waste
    time — we only need to update the strip when something actually moved.

You'll find this same idea saved in your kit as
[`50-buttons-move-light.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/led-strip-two-buttons/50-buttons-move-light.py).

## Try It Yourself

- Change the starting color from red to a color of your choice.
- Make the pixel leave a short trail behind it instead of disappearing
  completely.

## Check Your Understanding

1. What does the `position` variable represent?
2. Why does the code erase `last_position` before lighting up `position`?
3. What does `position % config.NUMBER_PIXELS` do when `position` goes past the end of the strip?
4. What is different about how this program tracks position compared to the very first Moving Pixel lesson?

!!! success "You've got this!"
    You just built direct, physical control over a pixel's position.
    That's the same core idea behind game controllers and robot arms.

**What's next:** in [Modes](28-modes.md), you'll learn how one program can
hold several different patterns and switch between them.
