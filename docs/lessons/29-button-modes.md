# Button Modes

This is the lesson that ties everything together. Button 1 advances to the
next mode, Button 2 goes back, and the strip runs whichever pattern the
mode variable points to. This is the exact pattern behind the "mode
machine" projects you've seen throughout this kit.

!!! tip "Pixel says..."
    You've built every piece of this already — buttons, interrupts,
    debouncing, and mode variables. Now you get to put them all together
    into one real project. Let's light this up!

## What you'll learn

- How to combine buttons, interrupts, and a mode variable into one program
- How to give each mode a name for clearer print statements
- How a **state machine** uses the current mode to decide what happens next

## What you'll need

- Your Pico, NeoPixel strip, and two buttons from the earlier lessons
- The kit's `config.py` file

## A State Machine, in Plain Words

A **state machine** is a program built around one idea: at any moment, it
is in exactly one **state** (here, one mode), and an event — a button
press — moves it to the next state. You already built the two halves of
this in earlier lessons:

- [Two Buttons and Interrupts](24-two-button-counter.md) — reacting to a button press
- [Modes](28-modes.md) — running a different pattern for each mode value

This lesson just connects the button press directly to the mode change,
instead of using a timer.

<iframe src="../sims/state-machine-diagram/main.html" width="100%" height="442px" scrolling="no"></iframe>
[Run State Machine Diagram Fullscreen](../sims/state-machine-diagram/main.html)

## The Full Program

```python
# Two buttons cycle forward and backward through a list of light modes.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

mode_names = ["solid red", "solid blue", "moving pixel", "off"]
NUM_MODES = len(mode_names)
mode = 0

DEBOUNCE_MS = 200
last_press = 0
position = 0


def fill_strip(color):
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()


def button_handler(pin):
    global mode, last_press
    now = ticks_ms()
    if now - last_press < DEBOUNCE_MS:
        return

    if pin == button1:
        mode = (mode + 1) % NUM_MODES
    else:
        mode = (mode - 1) % NUM_MODES

    last_press = now
    print("mode:", mode_names[mode])


button1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

while True:
    if mode == 0:
        fill_strip((200, 0, 0))
    elif mode == 1:
        fill_strip((0, 0, 200))
    elif mode == 2:
        strip[position] = (0, 0, 0)                    # erase old spot
        position = (position + 1) % config.NUMBER_PIXELS
        strip[position] = (0, 200, 0)                   # light new spot
        strip.write()
    else:
        fill_strip((0, 0, 0))   # mode 3: off

    sleep(0.05)
```

Press Button 1 to step forward through solid red, solid blue, a moving
green pixel, and off. Press Button 2 to step back the other way. Watch the
Shell — it prints the name of every mode as you switch to it.

!!! info "Pixel thinks..."
    Notice `mode_names` is just a list of words lined up with the numbers
    in the `if` / `elif` chain below. Keeping a name for each mode makes
    the `print()` output easy to read, even though the strip only ever
    sees the number.

Your kit includes a bigger version of this same idea with twelve modes —
comets, candles, rainbows, and more — saved as
[`60-pixel-demo.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/led-strip-two-buttons/60-pixel-demo.py).
Open it in Thonny and see how many modes you recognize from earlier lessons.

## Try It Yourself

- Add a fifth mode using a pattern from an earlier lesson, like the color
  wheel or the comet tail.
- Change `mode_names` and the `if` chain so Button 1 and Button 2 jump
  straight to your two favorite modes instead of cycling through all of them.

## Check Your Understanding

1. What is a state, in the context of this program?
2. What event causes the state machine to move to its next state?
3. Why does `mode_names[mode]` work as a way to print a mode's name?
4. How many modes could this program hold before you'd need to redesign
   the `if` / `elif` chain into something shorter?

!!! success "You've got this!"
    You just built a complete interactive light controller from scratch —
    buttons, interrupts, debouncing, and modes, all working together.
    That's a real engineering project, and you built it yourself!

**What's next:** you've completed the button and modes progression. From
here, try combining button modes with a sensor from
[Photoresistor](21-photo-resistor.md), or design a mode list that's
entirely your own.
