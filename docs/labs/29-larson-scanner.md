# Lab 29: Larson Scanner

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Meet the scanning eye! A red glow sweeps back and forth, and it feels like something is watching. Let's light this up!

**Program file:** [`29-larson-scanner.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/29-larson-scanner.py)

## What you'll learn

- How five pixels with different brightness make one glowing eye
- How `range()` counts down when you give it a step of `-1`
- How to erase only the trailing pixel instead of the whole strip
- Where the scanning eye came from

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- The counting-down `range` from [Lab 06: Up and Down](06-up-and-down.md)

## The program

This program sweeps a red five-pixel eye along the strip and back again, forever.

```python title="29-larson-scanner.py"
--8<-- "src/kits/moving-rainbow-base/29-larson-scanner.py"
```

Run it. A bright red pixel with dim red pixels on both sides glides to the far end. Then it turns around and glides back.

## How it works

### Three levels of red

```python
red = (255, 0, 0)
red_med = (32, 0, 0)
red_light = (8, 0, 0)
off = (0,0,0)
```

The eye has a bright center and dim edges. These four colors give us those levels. The numbers drop fast: 255, then 32, then 8.

Our eyes are very sensitive to dim light, so these steep steps still look like a smooth glow. You can explore this idea in the [Perceived vs. Linear Brightness](../sims/perceived-vs-linear-brightness/index.md) MicroSim.

### Draw the eye

```python
strip[i-2] = red_light
strip[i-1] = red_med
strip[i] = red
strip[i+1] = red_med
strip[i+2] = red_light
```

The variable `i` is the position of the eye's center. These five lines paint the five pixels around it, dim to bright to dim:

```text
pixel:   i-2     i-1    i    i+1     i+2
color:   light   med    RED  med     light
```

### Sweep forward

```python
for i in range(2, NUMBER_PIXELS-2):
```

Here `NUMBER_PIXELS` is 30, so this is `range(2, 28)`. The counter `i` runs from 2 to 27, and the stop value 28 is not included. That is 26 steps.

Why start at 2? At `i = 2`, the eye covers pixels 0 to 4. A start of 0 would make `i-2` negative, and negative positions count from the end of the strip.

Why stop at 27? At `i = 27`, the eye covers pixels 25 to 29, the last pixel. At `i = 28`, the value `i+2` would be 30, and there is no pixel 30.

### Erase the trailing pixel

```python
# erase the trailing pixel
if i > 0:
    strip[i-3] = off
strip.write()
sleep(delay)
```

When the eye moves one step forward, one pixel is left behind. That pixel is `i-3`. The program turns it off, so no red trail stays on the strip.

Only one pixel needs erasing, because the other four are repainted in their new places. The program changes all six pixels in memory first. Then one `strip.write()` shows the whole eye at once, and `sleep(delay)` holds it for 0.05 seconds.

Here is what the loops do at a few steps:

| Loop | `i` | Eye covers | Pixel turned off |
|------|-----|------------|------------------|
| Forward | 2 | 0 to 4 | `strip[-1]`, the last pixel |
| Forward | 3 | 1 to 5 | 0 |
| Forward | 27 | 25 to 29 | 24 |
| Backward | 26 | 24 to 28 | 29 |
| Backward | 25 | 23 to 27 | 28 |
| Backward | 2 | 0 to 4 | 5 |

!!! info "Key idea"
    On the first forward step, `i-3` is -1. Python counts negative positions from the end, so `strip[-1]` is the last pixel. That pixel is already off, so nothing changes.

### Sweep backward

```python
for i in range(NUMBER_PIXELS-4, 1, -1):
    # erase the trailing pixel
    if i < NUMBER_PIXELS-2:
        strip[i+3] = off
```

The `range` now has three numbers: start, stop, and step. It is `range(26, 1, -1)`, so `i` counts 26, 25, and so on down to 2. That is 25 steps.

The eye now moves toward pixel 0, so the pixel left behind is on the high side. That is why the erase line uses `i+3` instead of `i-3`. The five draw lines are the same as before.

A trip forward takes 26 steps and a trip back takes 25. At 0.05 seconds per step, a round trip takes about 2.5 seconds. Then `while True:` starts it all again.

Look closely at the ends. The last backward step and the first forward step both draw the eye at `i = 2`. So the eye rests at the pixel-0 end for two steps, but only one step at the far end. Can you spot the tiny pause?

## Where the scanner comes from

The scanning eye is named after Glen A. Larson, a TV producer. He created the shows Battlestar Galactica (1978) and Knight Rider (1982). In Battlestar Galactica, the Cylon robots have a red light that sweeps from side to side. In Knight Rider, a talking car named KITT has a red scanner on its nose.

The sweeping light made each machine seem alive and watching. Makers still copy it today. You might hear it called a Larson scanner, a Cylon eye, or a KITT scanner. Read the whole tale in the graphic novel [The Scanning Eye](../stories/larson-scanner/index.md).

## Try it yourself

### Challenge 1: Change the color

Change the three color lines near the top so the eye glows green. The names still say red, and that is fine for now.

```python title="Your change"
red = (0, 255, 0)
red_med = (0, 32, 0)
red_light = (0, 8, 0)
```

Can you make a blue eye too?

### Challenge 2: Change the speed

Change `delay = .05` to `delay = .02`. Then try `.1`. What is the smallest delay that still looks like a smooth glow?

## Check your understanding

1. Which pixel is the brightest, and where is it compared with `i`?
2. Why does the forward loop start at 2 and stop before `NUMBER_PIXELS-2`?
3. What does the `-1` in `range(NUMBER_PIXELS-4, 1, -1)` do?
4. Why does the forward loop erase `strip[i-3]`, but the backward loop erases `strip[i+3]`?
5. Why does each step call `strip.write()` only once?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built a glowing eye out of five pixels and two loops! Drawing a shape, moving it, and erasing the tail is a trick you can use in many patterns.

**What's next:** In [Lab 30: Random Bounce](30-random-bounce.md), several colored dots move on their own and turn around at the ends.
