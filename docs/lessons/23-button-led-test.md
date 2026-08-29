# Button + Built-in LED

Reading a button is only half the story. In this lesson, the button
controls something you can see: the small LED built right onto your Pico
board.

!!! tip "Pixel says..."
    This is the moment your code stops just *watching* and starts
    *reacting*. Press the button, and something in the real world
    changes. That's the whole idea behind every interactive project!

## What you'll learn

- How to turn an output on and off based on an input
- How to use `if` / `else` to react to a button press
- Why we only print when a value changes, instead of printing every time

## What you'll need

- Your Pico and button from [Testing a Button](22-button-test.md)
- The kit's `config.py` file

## Wiring

No new wiring is needed. The onboard LED is already built into the Pico at
pin 25, so your button is the only part you need to wire — the same way
you wired it in the last lesson.

## Button-Controlled LED

Remember: with a pull-up button, pressed reads as `0`. This program checks
that value and turns the LED on when the button is down.

```python
# Turn the onboard LED on while the button is held down.
from machine import Pin
from utime import sleep
import config

button = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)

BUILT_IN_LED_PIN = 25
led = Pin(BUILT_IN_LED_PIN, Pin.OUT)

button_value = 0
old_value = 0
while True:
    button_value = button.value()

    # the LED turns on when the button reads 0 (pressed)
    if button_value == 1:
        led.off()
    else:
        led.on()

    # only print when the value changes, not on every loop
    if button_value != old_value:
        print(button_value)
        old_value = button_value
```

Run it and hold the button. The little LED next to the USB port should
light up while you're pressing, and turn off when you let go.

!!! info "Pixel thinks..."
    See the `if button_value != old_value:` check? Without it, the Shell
    would print hundreds of lines a second, since the loop runs so fast.
    Comparing to `old_value` means we only print the moment something
    actually changes.

## Try It Yourself

- Flip the logic so the LED is normally **on** and turns **off** while
  you hold the button.
- Add a second `print()` that shows the word `"ON"` or `"OFF"` instead of
  `1` or `0`.

## Check Your Understanding

1. What pin number is the Pico's built-in LED connected to?
2. Why does the code check `if button_value != old_value` before printing?
3. What would happen if you swapped `led.on()` and `led.off()` in the `if` statement?
4. How is this program similar to the one from the last lesson? How is it different?

!!! success "You've got this!"
    You just built your first input-to-output reaction. Buttons and LEDs
    are the building blocks — next you'll use two buttons at once.

**What's next:** in [Two Buttons and Interrupts](24-two-button-counter.md),
you'll add a second button and meet a faster way to catch a press:
interrupts.
