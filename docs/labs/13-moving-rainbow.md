# Lab 13: Moving Rainbow with the Color Wheel

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    A tiny rainbow is about to go for a walk! We'll make it slide from one end of the strip to the other. This one is a colorful trip, so let's trace it together.

**Program file:** [`13-moving-rainbow.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/13-moving-rainbow.py)

## What you'll learn

- How to space a few colors evenly around the wheel with `round()`
- How `index` puts red at the front and the other colors behind it
- How `if index < NUMBER_PIXELS` keeps the code inside the strip
- How to erase the pixel behind a moving pattern
- How to **trace** a program (follow it step by step and track each value)

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico, with the Shell visible at the bottom
- The `wheel()` function from [Lab 09](09-color-wheel.md) and the `%` operator from [Lab 12](12-rainbow-cycle.md)

## The program

This program draws a short rainbow at the start of the strip. Then it moves the rainbow one pixel at a time, until it slides off the far end.

```python title="13-moving-rainbow.py"
--8<-- "src/kits/moving-rainbow-base/13-moving-rainbow.py"
```

Run it. A small rainbow with red at the front slides along the strip, about one pixel every twentieth of a second. It slides off the end, and then a new one starts at the beginning. This program keeps going until you press **Stop**.

!!! warning "Heads up"
    If the strip still glows from an earlier lab, those old colors stay lit ahead of the rainbow on its first trip. They disappear as the rainbow passes over them. Unplug the USB cable and plug it in again for a dark start.

## How it works

### Choose the rainbow length

These two lines set how long the rainbow is and how far apart its colors sit on the wheel.

```python
RAINBOW_LENGTH = 7
PERCENT_COLOR_WHEEL = round(255/RAINBOW_LENGTH)
```

`RAINBOW_LENGTH` is a **constant** (a value we set once and keep the same). Programmers write constants in capital letters. The `round()` function gives the nearest whole number, so 255 / 7 = 36.43 becomes 36.

The name `PERCENT_COLOR_WHEEL` is a bit misleading. It is not a percent. It is the gap, in wheel positions, between one color and the next.

### Pick a color for each pixel

This loop picks one wheel color for each pixel in the rainbow.

```python
for i in range(0, RAINBOW_LENGTH-1):
    color_index = round(i*PERCENT_COLOR_WHEEL)
    color = wheel(color_index)
```

Trace it. The loop runs `range(0, RAINBOW_LENGTH-1)`, which is `range(0, 6)`. That counts 0 to 5, so the loop makes six colors. The wheel positions are 0, 36, 72, 108, 144, and 180.

### Place the colors with the head in front

This code decides which pixel gets each color.

```python
# start at the end and subtract to go backwards and add the counter for offset
index = RAINBOW_LENGTH-1 - i  + counter
print(index)
if index < NUMBER_PIXELS:
    strip[index] = color
```

The variable `counter` says how far the rainbow has moved. With `RAINBOW_LENGTH` at 7, `index` is 6 - `i` + `counter`. Red is `i = 0`, so it lands furthest along the strip, at `counter + 6`. It is the **head** (the front). Each later color lands one pixel behind, and the last color forms the **tail** (the back).

| `i` | Wheel position | Color returned | Pixel |
|-----|----------------|----------------|-------|
| 0 | 0 | `(255, 0, 0)` | `counter + 6` |
| 1 | 36 | `(147, 108, 0)` | `counter + 5` |
| 2 | 72 | `(39, 216, 0)` | `counter + 4` |
| 3 | 108 | `(0, 186, 69)` | `counter + 3` |
| 4 | 144 | `(0, 78, 177)` | `counter + 2` |
| 5 | 180 | `(30, 0, 225)` | `counter + 1` |

The `if index < NUMBER_PIXELS:` line is a guard. Near the end of the strip, `index` grows past 29, and pixel 30 does not exist. The guard skips those colors, so the head slides off the end first.

### Erase behind the rainbow

After drawing the colors, the program turns off a pixel behind the rainbow. Without this step, every pixel the rainbow visits would stay lit.

```python
if counter > 0:
    print('off:', counter-1)
    strip[counter-1] = (0,0,0)
    strip.write()
```

The rainbow moves one pixel per step. So the pixel at `counter-1` is the one it left behind, and the program switches it off. The file also defines a function called `erase()`. This program does not call it, so you can skip it.

### Move on, then wrap

These lines pause, move the rainbow along by one pixel, and start over at the end of the strip.

```python
sleep(.05)
counter += 1
# wrap the counter using modulo
counter = counter % NUMBER_PIXELS
```

`sleep(.05)` holds each step for a twentieth of a second. After `counter` reaches 29, the modulo line, `counter % NUMBER_PIXELS`, turns 30 into 0. This wrap only restarts the counter. The rainbow does not curve around to the start of the strip. It slides off the end, and a new one appears at the beginning. A full trip takes 30 steps, so it lasts at least 30 × .05 = 1.5 seconds.

## What you see

Trace the glowing pixels after each step. Here are a few steps:

| `counter` | Pixels that glow after the step |
|-----------|---------------------------------|
| 0 | 1 to 6 |
| 1 | 1 to 7 |
| 2 | 2 to 8 |
| 10 | 10 to 16 |
| 24 | 24 to 29 |
| 28 | 28 and 29 |

Two things stand out. First, after the first step the rainbow is seven pixels wide, even though the loop draws six colors. Second, pixel 0 stays dark the whole time.

The seven pixels come from the erase step. It removes the pixel at `counter-1`. So the pixel at `counter` still glows from the last step, and it holds the same deep blue as the tail. The last color shows twice.

!!! bug "Known issue"
    `RAINBOW_LENGTH` is 7, but `range(0, RAINBOW_LENGTH-1)` draws only six colors. The seventh glowing pixel is a leftover copy of the tail, so the deep blue shows twice. Item 2 in Try it yourself draws all seven colors.

At the very end of the strip, the line `if counter == NUMBER_PIXELS-1:` turns off pixel 29. That way nothing stays lit when the next trip begins.

!!! tip "Tip"
    This program prints `index` on every step, so the Shell scrolls fast. Each trip prints more than 200 lines. Put a `#` at the start of the two `print` lines to quiet the Shell.

Want to see more animation patterns like this one? Read [Chapter 12: Basic Animation Patterns](../chapters/12-basic-animation-patterns/index.md).

## Try it yourself

1. Change `RAINBOW_LENGTH = 7` to `RAINBOW_LENGTH = 12`. Work out the new gap between colors and how many colors get drawn. Then run it and count.
2. Change `range(0, RAINBOW_LENGTH-1)` to `range(0, RAINBOW_LENGTH)`. Count the colors again. What happens to the tail?

## Check your understanding

1. How many colors does `range(0, RAINBOW_LENGTH-1)` draw when `RAINBOW_LENGTH` is 7? Which numbers does `i` take?
2. Which color is at the head of the rainbow? Which pixel does it light when `counter` is 10?
3. What does the line `if index < NUMBER_PIXELS:` protect against?
4. What does `counter % NUMBER_PIXELS` do when `counter` is 30?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You traced a whole program by hand, and that skill helps in every lab! Your little rainbow slides along like a pro.

**What's next:** In [Lab 14: Band](14-band.md), we draw solid bands of color with a function.
