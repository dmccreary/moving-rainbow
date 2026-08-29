# Blink the Onboard LED

Welcome to your very first program! Before you wire anything at all, let's
make sure your Pico and Thonny are talking to each other. Every Pico has a
small LED already built onto the board — no breadboard needed.

!!! tip "Pixel says..."
    You're already glowing — now let's make your LEDs glow too! This tiny
    test is how every Moving Rainbow builder gets started. Let's light
    this up!

## What you'll learn

- How to connect your Pico to Thonny and run a program
- How to turn an output pin on and off in a loop
- How changing one number changes what your program does

## What you'll need

- A Raspberry Pi Pico connected to your computer with a USB cable
- Thonny, with the Pico selected as the run target

No breadboard, wires, or LED strip are needed for this lesson.

## Your First Program

Every Pico has a small LED built onto the board at pin 25. This program
turns it on, waits, turns it off, waits, and repeats forever.

```python
# Use this program to test that your Pico is connected to Thonny and
# running MicroPython. No wiring needed - this uses the LED already
# built onto the Pico board.
from machine import Pin
from utime import sleep

BUILT_IN_LED_PIN = 25    # every Pico has an LED wired to this pin
BLINK_DELAY = 0.25       # seconds the LED stays on or off - change me!

led = Pin(BUILT_IN_LED_PIN, Pin.OUT)

while True:
    led.toggle()          # switch the LED on if it's off, or off if it's on
    sleep(BLINK_DELAY)
```

Save this file to your Pico and run it. You should see the small LED next
to the USB port blink on and off.

!!! info "Pixel thinks..."
    If nothing happens, that's a puzzle to solve, not a failure! Check
    that Thonny shows your Pico's name in the bottom-right corner, and
    that you saved the file **to the Pico**, not to your computer.

## Try It Yourself

- Change `BLINK_DELAY` to `1.0`. How does the blink speed change?
- Change `BLINK_DELAY` to `0.02`. Can you still see it blink, or does it
  look like it's just on all the time?
- Find the slowest and fastest `BLINK_DELAY` you can still call a "blink."

## Check Your Understanding

1. What pin number is the Pico's built-in LED connected to?
2. What does `led.toggle()` do?
3. What does the `BLINK_DELAY` variable control?
4. Why does this program need `while True:` instead of just running once?

!!! success "You've got this!"
    That's your very first working program. Every project in this book —
    from a single blinking pixel to a full two-player game — builds on
    this same idea: change something, wait, change it back.

**What's next:** in [Blink](01-blink.md), you'll wire up your NeoPixel
strip and blink your first full-color pixel.
