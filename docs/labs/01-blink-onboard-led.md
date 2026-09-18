# Lab 01: Blink the Onboard LED

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Before we wire anything, let's say hello to your Pico. If its little light blinks,
    your Pico is alive and listening. Let's light this up!

**Program file:** [`01-blink-onboard-led.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/01-blink-onboard-led.py)

## What you'll learn

- How to run a program on your Pico from Thonny
- How to switch a pin on and off with `led.toggle()`
- How a named setting like `BLINK_DELAY` changes what a program does
- Why a blink program needs `while True:`

## What you'll need

- A Raspberry Pi Pico plugged into your computer with a USB data cable
- Thonny open and connected to your Pico (see [Desktop Setup](../getting-started/desktop-setup.md) if you are still installing Thonny or MicroPython)

This lab needs no breadboard, no LED strip, and no `config.py`. It is the "Is my Pico alive?" test.

## The program

This program flips the Pico's own LED on and off every quarter of a second, forever.

```python title="01-blink-onboard-led.py"
--8<-- "src/kits/moving-rainbow-base/01-blink-onboard-led.py"
```

Open the program in Thonny and press the green **Run** button. The small LED near the USB connector blinks about twice every second. Press **Stop** when you are ready to end it.

## How it works

### Bring in two tools

```python
from machine import Pin
from utime import sleep
```

An **import** brings in code that other people already wrote. `Pin` lets us control the Pico's **pins** (metal contacts that can switch on and off). `sleep` pauses the program for a number of seconds.

### Name your settings

```python
BUILT_IN_LED_PIN = 25    # every Pico has an LED wired to this pin
BLINK_DELAY = 0.25       # seconds the LED stays on or off - change me!
```

A **variable** is a name that holds a value. Capital letters tell us these two are settings we may want to change. Keeping them at the top means you can find them fast. Change one number here, and the whole program changes.

### Why this lab skips `config.py`

Every other program in this book uses `import config`. The `config.py` file holds your kit's pin numbers and pixel count. This lab is the one exception. It only uses the Pico's built-in LED, so it needs nothing from `config.py`. You can run it the moment Thonny sees your Pico, before any other file is on the board.

### Make the LED an output

```python
led = Pin(BUILT_IN_LED_PIN, Pin.OUT)
```

This line builds an object named `led` that controls pin 25. `Pin.OUT` tells the Pico that this pin sends a signal **out**, to the LED. An **object** is a bundle of code and data with a name, so we can say what to do with it.

### Toggle, wait, repeat

```python
while True:
    led.toggle()          # switch the LED on if it's off, or off if it's on
    sleep(BLINK_DELAY)
```

`while True:` starts a **loop** (code that repeats). Because `True` is always true, the loop keeps going until you press **Stop**. Each time around, `led.toggle()` flips the LED to the opposite state. Then `sleep(BLINK_DELAY)` waits 0.25 seconds.

The LED stays on for 0.25 seconds and off for 0.25 seconds. So one full blink takes 0.5 seconds, and you see two blinks every second.

### If you have a Pico W

On a Pico W (the version with Wi-Fi), the built-in LED is wired through the wireless chip. Pin 25 does not control it. The LED has a name instead of a number. Replace the `led = ...` line with this one, and keep everything else the same:

```python title="Your change"
led = Pin("LED", Pin.OUT)
```

!!! warning "Heads up"
    If nothing blinks, look at the bottom-right corner of Thonny. It should say *MicroPython (Raspberry Pi Pico)*. If it does not, try a different USB cable. Some cables only charge and cannot carry data. The [When Something Doesn't Work](../kits/moving-rainbow-base/index.md#when-something-doesnt-work) table has more ideas.

## Try it yourself

1. Change `BLINK_DELAY` to `1.0`, then to `0.02`. What do you see at each speed? Find the smallest delay where you can still tell the LED is blinking.
2. Make a "two quick blinks, then a pause" pattern. Try it on your own first. The hint: `led.on()` and `led.off()` let you choose exactly when the LED is lit, so replace the two lines inside `while True:`.

Here is one sketch to compare with your version:

```python title="Your change"
while True:
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.6)
```

## Check your understanding

1. Which pin number controls the built-in LED on a standard Pico? What do you use on a Pico W?
2. What does `led.toggle()` do each time it runs?
3. With `BLINK_DELAY = 0.25`, how long does one full blink (on, then off) take?
4. Why can this program run before `config.py` is on your Pico?
5. Why does the program use `while True:` instead of running once?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    Your Pico is alive and listening! That little blink means your cable, Thonny, and MicroPython are all working together.

**What's next:** In [Lab 02: Blink](02-blink.md), you'll move from the Pico's own light to a pixel on your LED strip.
