# Lab 19: Theater Chase

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Old movie theaters had signs where the lights seemed to run around the edge. We'll make
    that with your strip. Ready to chase some light?

**Program file:** [`19-theater-chase.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/19-theater-chase.py)

## What you'll learn

- How `range(start, stop, step)` skips through the pixels
- How three loops inside each other build one pattern
- How a function with parameters runs the same pattern in any color
- How `sleep_ms` sets the speed in milliseconds

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

## The program

This program runs a **theater chase** (the moving light pattern from old movie theater signs) once for each of seven colors. One pixel in every four is lit, and the lit pixels step along the strip.

```python title="19-theater-chase.py"
--8<-- "src/kits/moving-rainbow-base/19-theater-chase.py"
```

Run it. Every fourth pixel glows, and the pattern marches toward the far end of the strip. Each color lasts about six and a half seconds. Then the next color starts.

## How it works

### A function with four parameters

```python
def theater_chase(strip, color, wait_ms, iterations):
    for j in range(iterations):
        for q in range(4):
```

A **function** is a named block of code you can run again and again. A **parameter** is a named slot for a value you hand to the function. This one has four:

- `strip` is the strip to light.
- `color` is the color to use.
- `wait_ms` is how long each step lasts, in milliseconds. One **millisecond** is a thousandth of a second.
- `iterations` is how many times to repeat the whole pattern.

The function has three loops inside each other. The `j` loop repeats the pattern. The `q` loop shifts the pattern by 0, 1, 2, and then 3 pixels. The third loop, called `i`, lights the pixels.

### Every fourth pixel

```python
for i in range(0, NUMBER_PIXELS-1, 4):
    if i+q < NUMBER_PIXELS:
        strip[i+q] = color
```

The `range` function can take three numbers: where to start, where to stop, and the **step** (how much to add each time). Here `NUMBER_PIXELS-1` is 29, so the loop counts 0, 4, 8, and so on up to 28. It stops before 29.

The `i+q` part shifts every lit pixel by `q`. Here is what each step lights:

| Step `q` | Pixels lit | How many |
|---|---|---|
| 0 | 0, 4, 8, ... 28 | 8 |
| 1 | 1, 5, 9, ... 29 | 8 |
| 2 | 2, 6, 10, ... 26 | 7 |
| 3 | 3, 7, 11, ... 27 | 7 |

The `if` line guards the edge. At `q` equal to 2, the last `i` of 28 would give pixel 30. The strip has no pixel 30, so the `if` skips it. Since 30 is not a multiple of 4, two of the four steps light seven pixels instead of eight.

### Show, wait, and erase

```python
strip.write()
sleep_ms(wait_ms)
# erase
for i in range(0, NUMBER_PIXELS-1, 4):
    strip[(i+q) % NUMBER_PIXELS] = (0,0,0)
```

The first line shows the lit pixels. The `sleep_ms` line holds them on for `wait_ms` milliseconds. Then the loop turns the same pixels off. This only changes the Pico's memory. The next `strip.write()` sends the erase and the new pixels together.

The `%` keeps the pixel number on the strip. At `q` equal to 2, the last pixel is 30 % 30, which is 0. Pixel 0 is already dark, so nothing changes.

Each step moves the lit pixels one place along. That makes the pattern seem to travel. A step takes 0.2 seconds, so the pattern moves five pixels each second.

### The main loop

```python
while True:
    # iterate through all the colors
    for c in range(0, num_colors):
        theater_chase(strip, colors[c], 200, 8)
```

The `c` loop goes through the seven colors. Each color runs `theater_chase` with a wait of 200 milliseconds and 8 repeats. Here is the timing:

- One repeat has four steps of 0.2 seconds, which is 0.8 seconds.
- Eight repeats take 6.4 seconds for each color.
- Seven colors take about 44.8 seconds before the whole show starts again.

## Try it yourself

1. Change `200` in `theater_chase(strip, colors[c], 200, 8)` to `50`, and change `8` to `30`. The chase gets faster. How long does each color last now?
2. Space the lights out. Change `4` to `6` in three places: `range(4)` and both `range(0, NUMBER_PIXELS-1, 4)` lines. What do you see? Then try changing only one of the three to see why they must match.

## Check your understanding

1. Which numbers does `range(0, 29, 4)` count through?
2. What does the loop variable `q` do?
3. Why do two of the four steps light only seven pixels?
4. How long does one color last?
5. What would you see if the erase loop were missing?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You made lights that chase each other! Three loops working together can build a pattern that looks far bigger than the code.

**What's next:** In [Lab 20: Ripple](20-ripple.md), a ripple spreads out from a random spot like a drop in a pond.
