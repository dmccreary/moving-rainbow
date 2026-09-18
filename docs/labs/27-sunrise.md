# Lab 27: Sunrise

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Today your strip becomes a sky! We'll blend the colors slowly, from a quiet night to a bright morning. It's going to be a glow-rious sunrise!

**Program file:** [`27-sunrise.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/27-sunrise.py)

## What you'll learn

- How to **blend** two colors to find every color in between
- How a **list** can hold a set of colors in order
- How a function hands back a new color with `return`
- How `range` can count backward to play the sunrise in reverse

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- The fade from [Lab 04: Dimmer](04-dimmer.md), because this lab fades between two colors instead of only changing brightness

## The program

This program fades the whole strip from a dark night color to a bright daytime color, waits, and then fades back again.

```python title="27-sunrise.py"
--8<-- "src/kits/moving-rainbow-base/27-sunrise.py"
```

Run it. All 30 pixels glow the same color. The strip starts a very dim blue, turns purple, then orange, and ends as a warm yellow. That sunrise takes about 18 seconds. After a 3-second pause, the colors run backward for a sunset. This program keeps going until you press **Stop**.

This is how a wake-up light works. It brightens slowly, so waking up feels gentle. Yours does it in seconds.

## How it works

### Name the colors

These lines give each color of the sky a name and put them in order.

```python
night = (0, 0, 8)
dawn = (30, 0, 30)
sunrise = (80, 20, 0)
day = (80, 60, 20)
sky_colors = [night, dawn, sunrise, day]
```

Each color is a tuple of red, green, and blue amounts, as in [Lab 03](03-red-green-blue.md). The last line makes a **list**, which is an ordered group of values inside square brackets. Positions start at 0, so `sky_colors[0]` is `night` and `sky_colors[3]` is `day`.

!!! info "Key idea"
    The color numbers stay small on purpose, because all 30 pixels are lit at once. The brightest color is `day`. Its numbers add up to 160, and 30 pixels showing it draw about 377 mA. A USB port supplies about 500 mA. Full white would need about 1,800 mA. Read more in [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go)

### Two settings

These two settings control how smooth and how slow the sunrise is.

```python
STEPS = 60          # how many small steps to blend from one color to the next
STEP_DELAY = 0.1    # seconds per step
```

Each change from one sky color to the next is cut into 60 small steps. The program waits 0.1 seconds after each step.

### Blend two colors

**Blending** means finding a color that is part of the way from one color to another. Programmers also call it **linear interpolation** (moving in a straight line from one value to another). This function does the blending.

```python
def blend(color1, color2, fraction):
    # fraction 0.0 gives color1, 1.0 gives color2, and 0.5 is halfway between
    red = int(color1[0] + (color2[0] - color1[0]) * fraction)
    green = int(color1[1] + (color2[1] - color1[1]) * fraction)
    blue = int(color1[2] + (color2[2] - color1[2]) * fraction)
    return (red, green, blue)
```

A **function** is a named block of code you can run again and again, like `wheel()` in [Lab 09](09-color-wheel.md). This one has three **parameters** (named slots for values you hand in). It hands back a new color with `return`. The `fraction` is a decimal from 0.0 to 1.0.

Square brackets pick one item by its position, the same way `strip[0]` picks a pixel. So `color1[0]` is the first number of `color1`, which is its red amount.

Look at the red line. It starts at the red of `color1`. Then it adds a `fraction` of the distance from `color1` to `color2`. At 0.0, it adds nothing, so you get `color1`. At 1.0, it adds the whole distance, so you get `color2`. At 0.5, it adds half.

Here is `blend(night, dawn, fraction)` for three fractions. Green stays at 0 for both colors.

| `fraction` | Red | Green | Blue | Color |
|------------|-----|-------|------|-------|
| 0.0 | 0 | 0 | 8 | `night` |
| 0.5 | 15 | 0 | 19 | halfway between |
| 1.0 | 30 | 0 | 30 | `dawn` |

The `int()` function cuts off the decimals. A strip needs whole numbers, so a red of 7.5 becomes 7. You can explore the same idea in the [Math Functions in Animation](../sims/animation-math-explorer/index.md) MicroSim. Open its Linear Interpolation tab.

### Fade from one color to the next

This function shows every step of a blend on the strip.

```python
def fade(color1, color2):
    for step in range(STEPS + 1):
        color = blend(color1, color2, step / STEPS)
        for i in range(NUMBER_PIXELS):
            strip[i] = color
        strip.write()
        sleep(STEP_DELAY)
```

The `range` function stops one number before its stop value, as you saw in [Lab 04](04-dimmer.md). So `range(STEPS + 1)` counts 0 through 60. That is 61 steps. The fraction is `step / STEPS`. In MicroPython, the `/` sign gives a decimal number, so the fraction climbs from 0/60, which is 0.0, up to 60/60, which is 1.0. The last step lands exactly on `color2`.

Each step does four things. It blends a color, sets all 30 pixels to it, calls `strip.write()` one time, and sleeps for 0.1 seconds. One fade takes 61 × 0.1 = 6.1 seconds.

### Walk through the list

The main loop plays the sunrise by fading between each pair of neighbors in the list.

```python
while True:
    # sunrise: blend through the colors in order
    for i in range(len(sky_colors) - 1):
        fade(sky_colors[i], sky_colors[i + 1])
    sleep(3)
    ...
```

The `len()` function counts the items in a list, so `len(sky_colors)` is 4. Subtract 1 and the loop counts 0, 1, and 2. That gives three fades: `night` to `dawn`, `dawn` to `sunrise`, and `sunrise` to `day`.

Why subtract 1? Four colors have only three gaps between them, like four fence posts have three gaps. A fourth trip would ask for `sky_colors[4]`, which does not exist.

### Play it backward

The sunset uses the same `fade` function, but it walks the list from the end.

```python
# sunset: blend back through the colors in reverse order
for i in range(len(sky_colors) - 1, 0, -1):
    fade(sky_colors[i], sky_colors[i - 1])
sleep(3)
```

This `range` has three parts: start at 3, stop before 0, and step by -1. It counts 3, 2, and 1, like the backward count in Lab 04. The three fades are `day` to `sunrise`, `sunrise` to `dawn`, and `dawn` to `night`.

### How long is one whole day?

Each fade takes 61 steps of 0.1 seconds. Here is the whole timeline.

| Part | Time |
|------|------|
| Sunrise: 3 fades × 61 steps × 0.1 s | 18.3 s |
| Pause | 3 s |
| Sunset: 3 fades × 61 steps × 0.1 s | 18.3 s |
| Pause | 3 s |
| One full day | 42.6 s |

Writing to the strip adds a tiny bit more time to each step.

## Try it yourself

1. Make a quick demo. Change `STEP_DELAY = 0.1` to `STEP_DELAY = 0.02`. How long does a sunrise take now? Work it out with 3 × 61 × 0.02. You should get 3.66 seconds.
2. Add a color. Put a pink between `dawn` and `sunrise`, and keep the numbers small. How many fades are in the sunrise now, and how long does it take?
3. Advanced: light only a few pixels near one end, as if they were the sun. In `fade`, change `range(NUMBER_PIXELS)` to `range(5)`.

Here are the two lines for challenge 2. The loops use `len(sky_colors)`, so they adjust to the longer list by themselves.

```python title="Your change"
pink = (60, 10, 30)
sky_colors = [night, dawn, pink, sunrise, day]
```

Here is the inner loop for challenge 3. Only pixels 0 to 4 get the color, and the other 25 pixels stay dark.

```python title="Your change"
for i in range(5):
    strip[i] = color
```

## Check your understanding

1. What color does `blend(night, dawn, 0.0)` give back? What about `blend(night, dawn, 1.0)`?
2. Why does `fade` use `range(STEPS + 1)` instead of `range(STEPS)`?
3. Why does the sunrise loop use `len(sky_colors) - 1`?
4. What numbers does `range(len(sky_colors) - 1, 0, -1)` count through?
5. About how many seconds does one sunrise take? Show your math.

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You blended colors into a sunrise! Blending is how programs make smooth color changes, from glowing skies to game effects.

**What's next:** In [Lab 28: Binary Clock](28-clock.md), the strip turns into a clock that tells time in 1s and 0s.
