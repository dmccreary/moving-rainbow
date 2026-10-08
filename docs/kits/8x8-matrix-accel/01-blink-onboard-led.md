# Lab 1: Blink the Onboard LED

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Every big light show starts with one little blink! I'm an LED (a light-emitting diode) too, so this one is close to my heart.
    Let's light this up!

**Program file:** [`01-blink-onboard-led.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/8x8-matrix-accel/01-blink-onboard-led.py)

## What you'll learn

- How a Python program loads tools with `import`
- How a **variable** (a name stuck on a number) makes code easier to change
- How to turn a pin on and off to blink the LED
- How `while True` repeats code forever
- How the `sleep` time sets the speed

## What you'll need

- Your Raspberry Pi Pico and a USB data cable
- Thonny open and connected to your Pico (see the [Desktop Setup](../../getting-started/desktop-setup.md) page)
- No wires and no `config.py` for this lab. This program uses the small LED that is already built onto the Pico board

## The program

This program blinks the Pico's own LED over and over. It checks that your Pico is connected to Thonny and running Python.

```python title="01-blink-onboard-led.py"
--8<-- "src/kits/8x8-matrix-accel/01-blink-onboard-led.py"
```

Open the file in Thonny and click the green **Run** button. The small LED near the USB connector blinks twice every second. The **Shell** at the bottom of Thonny shows the name and version of the program.

Click the red **Stop** button when you want it to end.

## How it works

### Load the tools

```python
from machine import Pin
from utime import sleep
```

Python comes with a toolbox of ready-made code. The `import` word brings tools into your program. The `machine` toolbox has tools that talk to the Pico's pins. `Pin` is the tool for one pin. The `utime` toolbox has `sleep`, which makes the Pico wait.

### Give your numbers names

```python
BUILT_IN_LED_PIN = 25    # every Pico has an LED wired to this pin
BLINK_DELAY = 0.25       # seconds the LED stays on or off - change me!
```

A **variable** is a name stuck on a value. `BUILT_IN_LED_PIN` is a name for the number 25. `BLINK_DELAY` is a name for 0.25, a number with a decimal point. Names written in capital letters are a habit programmers use for settings. When you want a slower blink, you change one number at the top and nothing else.

### Make the LED object

```python
led = Pin(BUILT_IN_LED_PIN, Pin.OUT)
```

This line creates a `Pin` that controls pin 25. The word `Pin.OUT` means the pin sends a signal *out*, so it can turn a light on. We keep the result in a variable named `led`.

### Repeat forever

```python
while True:
    led.toggle()          # switch the LED on if it's off, or off if it's on
    sleep(BLINK_DELAY)
```

The `while True:` line starts a **loop**, which is code that repeats. Because `True` is always true, this loop never ends. The two indented lines belong to the loop. The spaces at the start of a line tell Python which lines are inside it.

`led.toggle()` flips the LED. If it was off, it turns on. If it was on, it turns off. Then `sleep(BLINK_DELAY)` waits a quarter of a second. One trip through the loop changes the LED once, so the LED needs two trips to finish one blink.

!!! info "Key idea"
    A program on a microcontroller usually never ends. It checks, changes, and waits, again and again, for as long as the power stays on.

## Try it yourself

1. Change the speed. Set `BLINK_DELAY = 0.1`, then `BLINK_DELAY = 1`. Predict what each one does before you run it.
2. Make a double blink. Replace the two lines inside the loop with the lines below. Run it and watch for two quick blinks and then a long pause.

    ```python
    while True:
        led.on()           # turn the LED on
        sleep(0.1)
        led.off()          # turn the LED off
        sleep(0.1)
        led.on()
        sleep(0.1)
        led.off()
        sleep(1)           # a long pause before the next double blink
    ```

3. Find the pause. How many seconds is one full blink (on, then off) when `BLINK_DELAY` is 0.25?

## Check your understanding

1. What does the `import` word do?
2. What is a variable? Name one variable in this program.
3. Why does the `while True:` loop never stop on its own?
4. What does `led.toggle()` do each time it runs?
5. How could you make the LED blink four times every second?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    Your Pico runs Python and your LED obeys! That's the first step in every project.

**What's next:** In [Lab 2: Hardware Probe](02-probe.md), your Pico tests all of your wiring and tells you what it finds.
