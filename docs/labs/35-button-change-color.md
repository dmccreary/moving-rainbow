# Lab 35: Button Change Color

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Buttons and lights finally meet! One button walks forward through a list of colors, and the other walks back. Let's light this up!

**Program file:** [`35-button-change-color.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/35-button-change-color.py)

## What you'll learn

- How to keep colors in a list and pick one with an index
- How the `%` operator wraps the index from the end of the list back to the start
- How `fill_strip()` lights every pixel with one color
- How an interrupt handler changes the strip the instant a button is pressed

## What you'll need

- Your base kit: a Pico, a breadboard, the 30-pixel LED strip, and both push buttons. Wire them as in the [Kit User's Guide](../kits/moving-rainbow-base/index.md) and [The Two Buttons](../kits/moving-rainbow-base/index.md#the-two-buttons).
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

This lab uses interrupts, debouncing, and `global` from [Lab 34: Two Buttons](34-two-button-print.md). Read that lab first if those words are new.

## The program

This program fills the whole strip with one color from a list. Button 1 moves forward through the list, and Button 2 moves backward.

```python title="35-button-change-color.py"
--8<-- "src/kits/moving-rainbow-base/35-button-change-color.py"
```

Run it. The strip glows red. Press Button 1 and it steps through orange, yellow, green, blue, and purple, then wraps back to red. Press Button 2 to go the other way. The Shell prints the current color index each time.

!!! warning "Power check"
    Every color in this list lights all 30 pixels at a high level. Yellow, `(255, 255, 0)`, is the hungriest at about 1,200 mA. Orange is about 789 mA, purple is about 777 mA, and red, green, and blue are about 600 mA each. A USB port supplies about 500 mA. Divide every number in the `colors` list by 4 to stay under that limit. For example, `(255, 255, 0)` becomes `(64, 64, 0)`, about 302 mA. Read more in [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go)

## How it works

### A list of colors

This part builds the list of colors and a number that points at one of them.

```python
colors = [
    (255, 0, 0),     # red
    (255, 80, 0),    # orange
    (255, 255, 0),   # yellow
    (0, 255, 0),     # green
    (0, 0, 255),     # blue
    (130, 0, 200),   # purple
]
color_index = 0
```

A **list** holds many values in order, inside square brackets. Each color is three numbers: red, green, and blue. The `color_index` variable is the **index** (the position) of the color we are showing now. Positions start at 0, so `colors[0]` is red and `colors[5]` is purple.

### Fill the strip

The `fill_strip()` function gives every pixel the same color.

```python
def fill_strip(color):
    for i in range(NUMBER_PIXELS):
        strip[i] = color
    strip.write()
```

A **function** is a named chunk of code that you can run whenever you like. This one takes a `color` and sets pixels `0` through `29` to it. Then it calls `strip.write()` one time, so all 30 pixels change together.

### Step through the list

When Button 1 is pressed, the index moves up by one. When Button 2 is pressed, it moves down by one.

```python
    if pin == button1:
        color_index = (color_index + 1) % len(colors)
    else:
        color_index = (color_index - 1) % len(colors)
```

The `%` sign is the **modulo** operator. It gives the remainder left over after a division. Here `len(colors)` is 6, so the index can only be 0 through 5.

- Going up from the last color: 5 + 1 is 6, and 6 % 6 is 0. That is red again.
- Going down from the first color: 0 - 1 is -1, and -1 % 6 is 5. That is purple.

Python's `%` gives an answer from 0 to 5 here, even after a subtraction. That is why Button 2 wraps around correctly. Try it in the [Modulo Wrap Simulation](../sims/modulo-wrap-simulation/index.md).

### The handler

The handler follows the same plan as Lab 34. It ignores presses that come within 200 milliseconds of the last one.

```python
DEBOUNCE_MS = 200   # ignore extra presses for 200 ms after each one
last_press = 0
```

```python
def button_handler(pin):
    # this runs the instant a button is pressed, even while the
    # rest of the program is doing something else
    global color_index, last_press
    now = ticks_ms()
    if now - last_press < DEBOUNCE_MS:
        return   # too soon - probably the same press bouncing, ignore it
    last_press = now
```

The `return` line ends the function early. A press that comes too soon is treated as bounce, and nothing else happens.

After the time check, the handler picks the new index (shown above). Then it does the real work. It lights the strip and prints the index:

```python
    fill_strip(colors[color_index])
    print("color index:", color_index)
```

Filling 30 pixels takes only a moment, so this handler still gets in and out quickly.

### Hook up the buttons, then wait

```python
button1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
```

These two lines connect both buttons to the same handler, as in Lab 34. Before the main loop starts, the program calls `fill_strip(colors[color_index])` to show the first color right away.

```python
while True:
    # the buttons do all the work through interrupts, so the main
    # loop just needs to stay alive
    sleep(1)
```

The buttons do all the work through interrupts. The main loop has nothing left to do, so it only sleeps.

## Try it yourself

1. Make the list safe for USB power. Replace the `colors` list with this version, where every number is divided by about 4:

```python title="Your change"
colors = [
    (64, 0, 0),      # red
    (64, 20, 0),     # orange
    (64, 64, 0),     # yellow
    (0, 64, 0),      # green
    (0, 0, 64),      # blue
    (32, 0, 50),     # purple
]
```

2. Light only the first half of the strip. In `fill_strip`, change `range(NUMBER_PIXELS)` to `range(NUMBER_PIXELS // 2)`. The `//` sign divides and drops any leftover.

## Check your understanding

1. What does `color_index` keep track of?
2. What is `(0 - 1) % 6`? Which color does that pick?
3. Why does `strip.write()` come after the loop in `fill_strip()` and not inside it?
4. Why does the main loop only call `sleep(1)`?
5. You add a seventh color to the `colors` list. What else must you change? Why?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built a color picker with two buttons! A list, an index, and a modulo all worked together to make it happen.

**What's next:** In [Lab 36: Button Change Speed](36-button-change-speed.md), the buttons change how fast a pixel moves instead of its color.
