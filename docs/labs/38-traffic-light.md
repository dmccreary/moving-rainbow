# Lab 38: Traffic Light

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    A real traffic light tells a story in three colors: stop, go, and get ready. We'll build one with three pixels. Let's light this up!

**Program file:** [`38-traffic-light.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/38-traffic-light.py)

## What you'll learn

- How to use three pixels as the red, yellow, and green lights of a traffic light
- How one function can switch several lights on and off with a single call
- How to give each color its own amount of time
- How a **state machine** moves from one state to the next

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

This lab does not use the buttons.

## The program

This program uses the first three pixels of the strip as a traffic light. Red stays on for 4 seconds, green for 4 seconds, and yellow for 1 second, over and over.

```python title="38-traffic-light.py"
--8<-- "src/kits/moving-rainbow-base/38-traffic-light.py"
```

Run it. Pixel 0 glows red, then pixel 2 glows green, then pixel 1 glows yellow, and only one light is on at a time.

## How it works

### Name the pixels

This code gives each light a name, and it makes a color that means "off."

```python
RED_PIXEL, YELLOW_PIXEL, GREEN_PIXEL = 0, 1, 2
OFF = (0, 0, 0)
```

The first line hands out three values to three names at once. `RED_PIXEL` gets 0, `YELLOW_PIXEL` gets 1, and `GREEN_PIXEL` gets 2. Python calls this **tuple unpacking**. A **tuple** is a group of values, like the color `(0, 0, 0)`, and unpacking gives them to names in order.

Names in CAPITAL letters are **constants** (values the program keeps the same). A name like `RED_PIXEL` is clearer to read than the number 0.

### Clear the strip

This function turns every pixel off in the Pico's memory.

```python
def clear_strip():
    for i in range(NUMBER_PIXELS):
        strip[i] = OFF
```

A **function** is a named block of code that you can run whenever you like. `clear_strip()` uses a `for` loop to set all 30 pixels to `OFF`. Nothing changes on the strip yet, because `strip.write()` has not run.

### Turn lights on and off

This function takes three yes-or-no answers and lights the matching pixels.

```python
def show(red_on, yellow_on, green_on):
    clear_strip()
    strip[RED_PIXEL] = (200, 0, 0) if red_on else OFF
    strip[YELLOW_PIXEL] = (200, 160, 0) if yellow_on else OFF
    strip[GREEN_PIXEL] = (0, 200, 0) if green_on else OFF
    strip.write()
```

Each input is `True` or `False`. Values like these are called **booleans**. Each `strip[...]` line uses a **conditional expression**, which is a one-line if/else that picks a value. Read `(200, 0, 0) if red_on else OFF` as "use red if `red_on` is `True`, otherwise use `OFF`."

Notice that `strip.write()` runs only once, at the end. The function clears the strip in memory, sets all three pixels, and then sends everything together. If it wrote after clearing, the lights would blink dark for a moment.

The yellow color `(200, 160, 0)` mixes a lot of red with a good amount of green. You can explore mixing light in the [Additive and Subtractive Mixing](../sims/additive-subtractive-mixing/index.md) MicroSim.

### The main loop

This loop calls `show()` three times, and each call is followed by a wait.

```python
while True:
    show(True, False, False)    # red - stop
    sleep(4)
    show(False, False, True)    # green - go
    sleep(4)
    show(False, True, False)    # yellow - slow down
    sleep(1)
```

The three inputs to `show()` always come in the same order: red, yellow, green. One trip through the loop takes 4 + 4 + 1 = 9 seconds. Red is on for 4 of those 9 seconds, and yellow is on for only 1.

!!! info "Key idea"
    A **state machine** is a system that is always in exactly one **state** (a situation, like "red"). It follows rules to move to the next state. Your traffic light has three states, and a timer decides when to move on. The [State Machine Diagram](../sims/state-machine-diagram/index.md) shows the same idea with button presses in place of timers.

## Try it yourself

1. Change the last `sleep(1)` in the loop to `sleep(2)`. Yellow now lasts twice as long. Is that better for drivers?
2. Change the first `sleep(4)` to `sleep(8)`. How long is red now, and how many seconds does one full cycle take?

## Check your understanding

1. Which pixel is the red light, and which pixel is the green light?
2. What does `show(False, True, False)` do?
3. Why does `show()` call `strip.write()` only once?
4. How many seconds does one full red, green, yellow cycle take?
5. In a state machine, what has to happen before the program moves to the next state?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built a machine that keeps track of its own state! Crosswalk signals, elevators, and vending machines all work on this same idea.

**What's next:** In [Lab 39: Binary Counter](39-binary-counter.md), pixels show numbers instead of traffic lights.
