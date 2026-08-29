# Button-Controlled Speed

Colors aren't the only thing buttons can change. In this lesson, Button 1
speeds up a moving pixel, and Button 2 slows it back down.

!!! tip "Pixel says..."
    Speed is just a number hiding inside a `sleep()` call. Once you can
    see that, you can control almost anything about an animation with a
    button — speed, brightness, even how many pixels light up.

## What you'll learn

- How a `delay` variable controls animation speed
- How to raise or lower a variable within a minimum and maximum limit
- Why `max()` and `min()` are useful for keeping a value in a safe range

## What you'll need

- Your Pico, NeoPixel strip, and two buttons from the earlier lessons
- The kit's `config.py` file

## Speed Is Just a Delay

Every moving pattern you've written pauses for a moment between steps
using `sleep(delay)`. A **smaller** delay means less waiting, so the
pattern looks faster. A **larger** delay means the pattern looks slower.
This lesson lets the buttons change that one number while the program runs.

## Keeping Speed in a Safe Range

If a delay gets too close to `0`, the pattern moves faster than the strip
can keep up with. If it gets too large, the strip looks like it's frozen.
`max()` and `min()` keep `delay` inside safe limits:

```python
delay = max(MIN_DELAY, delay - 0.02)   # speed up, but not too fast
```

`max()` picks whichever value is bigger — so if subtracting `0.02` would
push `delay` below `MIN_DELAY`, this line keeps it at `MIN_DELAY` instead.

## The Full Program

```python
# Button 1 speeds up a moving pixel. Button 2 slows it down.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

delay = 0.1          # seconds between moves - this is our "speed"
MIN_DELAY = 0.01     # fastest we will allow
MAX_DELAY = 0.5      # slowest we will allow

DEBOUNCE_MS = 200
last_press = 0


def button_handler(pin):
    global delay, last_press
    now = ticks_ms()
    if now - last_press < DEBOUNCE_MS:
        return

    if pin == button1:
        delay = max(MIN_DELAY, delay - 0.02)   # speed up, but not too fast
    else:
        delay = min(MAX_DELAY, delay + 0.02)   # slow down, but not too slow

    print("delay:", delay)


button1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

position = 0
while True:
    strip[position] = (0, 0, 0)                    # erase the old spot
    position = (position + 1) % config.NUMBER_PIXELS
    strip[position] = (0, 120, 255)                 # light the new spot
    strip.write()
    sleep(delay)   # delay can change any time a button interrupt fires
```

Watch the blue pixel move around the strip. Press Button 1 a few times —
it should speed up. Press Button 2 — it should slow back down. Watch the
Shell to see the exact delay value printed each time.

!!! warning "Watch out!"
    Notice that `sleep(delay)` reads the `delay` variable fresh every
    time through the loop. If the buttons changed a *copy* of `delay`
    instead of the real variable, the speed would never actually change —
    that's why `button_handler` uses `global delay`.

## Try It Yourself

- Change `MIN_DELAY` to `0.002`. How fast can the pixel go before it
  starts to look like a blur?
- Add a `print()` that shows the delay as a speed rating, like `"slow"`,
  `"medium"`, or `"fast"`.

## Check Your Understanding

1. What does a smaller `delay` value do to the animation's speed?
2. What job do `max()` and `min()` do in this program?
3. Why does `button_handler` need the line `global delay`?
4. What would happen if `MIN_DELAY` were set to `0`?

!!! success "You've got this!"
    You now control both color and speed with buttons. Next, you'll use
    the buttons to control position itself.

**What's next:** in [Buttons Move a Pixel](27-buttons-move-pixel.md),
each button press will move a lit pixel one step at a time.
