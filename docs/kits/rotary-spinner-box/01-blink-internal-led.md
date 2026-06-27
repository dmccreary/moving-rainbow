# Lab 1: Blink the Onboard LED

This is your first program. It blinks the tiny light built right into the
Raspberry Pi Pico — the small computer chip in your box. You don't need to
wire up anything. If this light blinks, your code is running!

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Every coder's first win is making a light blink. It's our way of saying
    "hello!" to a new computer. Once you see that little light flash, you'll
    know your code made it all the way to the chip. Let's light this up!

## What You'll Learn

By the end of this lab, you'll be able to:

- Run a MicroPython program on the Raspberry Pi Pico
- Turn the onboard LED **on** and **off** in code
- Use a **loop** (code that repeats) to blink forever
- Explain what **sequencing** means in a program

## What You'll Need

- Your Rotary Spinner Box with the Pico inside
- A USB cable to connect the box to your computer
- The Thonny program open on your computer

You do **not** need the LED strip, the knob, or the buttons for this lab.

## A First Look at the Code

The **onboard LED** (the light built into the Pico) lives on pin 25. A **pin**
is one of the metal connection points on the chip. Our program turns that pin
on, waits, turns it off, waits, and repeats.

Here is the full program. It is the file `01-blink-internal-led.py`.

```python
import machine
from utime import sleep

# Set up the onboard LED pin as an output we can turn on and off
led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.value(1)    # turn the LED on
    sleep(0.5)      # wait half a second

    led.value(0)    # turn the LED off
    sleep(0.5)      # wait half a second
```

When you run it, the small green light on the Pico blinks on and off once
every second.

## How It Works, Line by Line

Let's read the code the way the Pico does — from top to bottom. Doing steps in
order like this is called **sequencing**.

- `import machine` brings in the tools for talking to the chip's pins.
- `from utime import sleep` gives us `sleep`, which **pauses** the program.
- `led = machine.Pin(25, machine.Pin.OUT)` makes a **variable** named `led`. A
  variable is a name that holds something. Here it holds our LED pin. `OUT`
  means we will send power *out* to the light.
- `while True:` starts a **loop**. A loop is code that repeats. `True` is
  always true, so this loop never stops.
- `led.value(1)` turns the light **on**. `1` means "on."
- `sleep(0.5)` waits half a second so we can see the light.
- `led.value(0)` turns the light **off**. `0` means "off."

!!! info "Pixel thinks..."
    <img src="../../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    Why do we need the `sleep` lines? The chip is *fast* — millions of steps a
    second. Without a pause, the light would flip on and off so fast it would
    just look dim. The `sleep` gives your eyes time to catch up.

## Why the Loop Matters

Without the `while True:` loop, the light would blink **once** and stop. The
loop is what makes it blink again and again. This idea — repeating steps — is
called **iteration**, and you'll use it in almost every program you write.

!!! warning "Watch out!"
    <img src="../../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    The lines inside the loop are **indented** (pushed in with spaces).
    MicroPython uses that spacing to know what belongs to the loop. If your
    code doesn't run, check that the indented lines all line up.

## From the Onboard LED to a Real Pixel

The onboard LED can only do one thing: on or off. The 12-pixel strip in your
box can show any color. The next file, `01-blink.py`, blinks the **first
pixel** of the strip in red:

```python
from neopixel import NeoPixel
from utime import sleep
import config

# Make a strip object so we can control the NeoPixels
strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

while True:
    strip[0] = (255, 0, 0)   # set the first pixel to red
    strip.write()            # send the colors to the strip
    sleep(0.5)

    strip[0] = (0, 0, 0)     # set the first pixel to off (black)
    strip.write()
    sleep(0.5)
```

It uses the same blink idea, but now a color. `(255, 0, 0)` means full red, no
green, no blue. `strip.write()` is the line that actually sends the colors to
the lights.

## Try It Yourself

1. **Blink faster.** Change both `sleep(0.5)` lines to `sleep(0.1)`. What is the
   smallest number where you can still see the light blink?
2. **Blink a slow heartbeat.** Use a short on-time and a long off-time, like
   `sleep(0.1)` on and `sleep(0.9)` off.
3. **Change the pixel color.** In `01-blink.py`, change `(255, 0, 0)` to
   `(0, 255, 0)`. What color do you get?

## Check Your Understanding

1. What does the onboard LED tell you when it blinks?
2. What does the `while True:` loop do?
3. Why do we need the `sleep` lines?
4. In `(255, 0, 0)`, which number controls the red light?
5. What is the name for doing steps in order, top to bottom?

!!! success "Chapter complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You did it — your very first program is running on a real computer chip!
    Every light show in this kit is built on what you just learned: do steps in
    order, and repeat them in a loop. You're already glowing!

## What's Next

In [Lab 2: Test the Buttons](02-button-test.md), you'll make your code react
when *you* press a button.
