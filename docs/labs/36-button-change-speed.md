# Lab 36: Button Change Speed

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Speed is a number in disguise! Change that number, and a pixel zips or crawls. Let's make the two buttons our speed dial.

**Program file:** [`36-button-change-speed.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/36-button-change-speed.py)

## What you'll learn

- How a `delay` variable sets the speed of an animation
- How `max()` and `min()` keep a number between a lower and an upper limit
- How a handler can change a variable that the main loop reads
- How `% NUMBER_PIXELS` makes a moving pixel wrap around the strip

## What you'll need

- Your base kit: a Pico, a breadboard, the 30-pixel LED strip, and both push buttons. Wire them as in the [Kit User's Guide](../kits/moving-rainbow-base/index.md) and [The Two Buttons](../kits/moving-rainbow-base/index.md#the-two-buttons).
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

This lab uses interrupts, debouncing, and `global` from [Lab 34: Two Buttons](34-two-button-print.md). It also uses `%` from [Lab 35: Button Change Color](35-button-change-color.md).

## The program

This program moves one blue pixel around the strip forever. Button 1 speeds it up, and Button 2 slows it down.

```python title="36-button-change-speed.py"
--8<-- "src/kits/moving-rainbow-base/36-button-change-speed.py"
```

Run it. A bright blue pixel runs along the strip and wraps back to the start. At first it takes about three seconds to go all the way around. Press Button 1 and it speeds up. Press Button 2 and it slows down. The Shell prints the new `delay` each time.

!!! warning "Heads up"
    This program erases only the pixel it leaves. If an earlier program left pixels lit, they stay lit until the blue pixel reaches them. After one full lap, the strip is clear.

## How it works

### Speed is a delay

These three lines set the speed and its limits.

```python
delay = 0.1          # seconds between moves - this is our "speed"
MIN_DELAY = 0.01     # fastest we will allow (too fast looks like a blur)
MAX_DELAY = 0.5      # slowest we will allow
```

The `delay` is how many seconds the pixel waits before it moves one step. A **smaller** delay means less waiting, so the pixel looks faster. Names in ALL CAPS, like `MIN_DELAY`, are values that stay fixed while the program runs.

| `delay` | Moves per second | One trip around the strip |
|---------|------------------|---------------------------|
| `0.01` | 100 | about 0.3 seconds |
| `0.1` | 10 | about 3 seconds |
| `0.5` | 2 | about 15 seconds |

### Speed up and slow down, within limits

This part of the handler changes `delay`.

```python
    if pin == button1:
        delay = max(MIN_DELAY, delay - 0.02)   # speed up, but not too fast
    else:
        delay = min(MAX_DELAY, delay + 0.02)   # slow down, but not too slow
```

The `max()` function picks the bigger of two numbers. Button 1 subtracts `0.02` from `delay`. If the answer falls below `MIN_DELAY`, `max()` picks `MIN_DELAY` instead. For example, `max(0.01, 0.00)` is `0.01`.

The `min()` function picks the smaller of two numbers. Button 2 adds `0.02`. If the answer rises above `MAX_DELAY`, `min()` picks `MAX_DELAY`. For example, `min(0.5, 0.52)` is `0.5`.

Using both functions together is called a **clamp**. It holds a number between two limits. Starting from `0.1`, five presses of Button 1 reach the fastest speed. About twenty presses of Button 2 reach the slowest.

Decimal numbers are stored as close approximations, so the Shell may show a value like `0.06000001` instead of `0.06`.

### The handler changes only a number

```python
def button_handler(pin):
    global delay, last_press
    now = ticks_ms()
    if now - last_press < DEBOUNCE_MS:
        return   # too soon - probably the same press bouncing, ignore it
    last_press = now
```

This is the same debounce plan you met in Labs 34 and 35. The handler ignores any press that comes within `DEBOUNCE_MS` (200 milliseconds) of the last one.

!!! info "Key idea"
    The line `global delay, last_press` lets the handler change the real `delay`. Without `global`, the handler would change a private copy, and the speed would stay the same. The loop reads `delay` fresh every time it calls `sleep(delay)`.

The handler leaves the strip alone. Only the main loop draws, so only one piece of code writes to the strip at a time. A pixel that is already waiting finishes its wait with the old delay. The new delay starts with the next step.

### The moving pixel

The main loop erases the old spot, moves on, and lights the new spot.

```python
position = 0
while True:
    strip[position] = (0, 0, 0)                    # erase the old spot
    position = (position + 1) % NUMBER_PIXELS
    strip[position] = (0, 120, 255)                 # light the new spot
    strip.write()
    sleep(delay)   # delay can change any time a button interrupt fires
```

Setting a pixel to `(0, 0, 0)` turns it off. The `position` variable holds the index of the lit pixel. Adding one moves it forward. The `% NUMBER_PIXELS` part wraps it: when `position` is 29, `29 + 1` is `30`, and `30 % 30` is `0`, so the pixel jumps back to the start of the strip.

Both changes happen in the Pico's memory. Then `strip.write()` sends them to the strip once, so the old spot goes dark and the new spot lights at the same moment. Only one pixel is lit, so this program needs very little power.

## Try it yourself

1. Change `MIN_DELAY = 0.01` to `MIN_DELAY = 0.002`. Press Button 1 until the pixel stops getting faster. At what point does it start to look like a blur?
2. Change both `0.02` values in the handler to `0.05`. Starting from `0.1`, how many presses of Button 1 does it take to reach the fastest speed?

## Check your understanding

1. What does a smaller `delay` do to the pixel's speed?
2. The `delay` is `0.02` and you press Button 1. What does `delay` become? Why?
3. Why does `button_handler` need the line `global delay`?
4. What does `% NUMBER_PIXELS` do when `position` is 29?
5. Why does the program call `strip.write()` once for each step, and not once after the erase and once after the light?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built a speed dial! One number, two buttons, and a pair of guard rails made it work.

**What's next:** In [Lab 37: Modes Auto Cycle](37-modes-auto-cycle.md), a timer, not a button, switches the strip between three colors.
