# Lab 12: Loading Spinner

This is the busy spinner you see on a phone or computer while something loads. An arc of light grows longer and shorter as it races around the ring.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Loading... loading... ready! Let's build the spinner that keeps people company while they wait.

**Program file:** [`12-loading-spinner.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/ring-24/12-loading-spinner.py)

![A long green arc that covers most of the ring, with a bright head and a fading tail](img/12-loading-spinner.png){ width="260" }

*Drawn by a ring simulator on a computer, so your real ring may look a little different. On the real ring it moves.*

## What You'll Learn

- Describe an **arc** (a curved piece of the ring) with a tail and a length
- Use a **Boolean** variable (one that can only be `True` or `False`) to remember if the arc is growing or shrinking
- Move the two ends of the arc at different speeds
- Make a **gradient** (a smooth change from dim to bright) along the arc

## What You'll Need

- Your ring kit with the ring on GPIO 0
- `config.py` saved on the Pico

## The Program

This program draws an arc that grows, shrinks and changes color.

```python
--8<-- "src/kits/ring-24/12-loading-spinner.py"
```

You should see a red arc race clockwise, stretching out and then squeezing back down. Each time it gets short again, it switches to a new color.

## How It Works

The arc has two numbers. `tail` is the pixel where it starts, and `length` is how many pixels long it is. The **head** is the far end of the arc, the end that leads the way.

The `for t in range(length)` loop lights each pixel of the arc. `amount = (t + 1) / length` is small at the tail and 1.0 at the head. So the tail is dim and the head is bright.

`growing` is a Boolean variable. While it is `True`, the tail moves 1 pixel and the length grows by 1. That means the head moves 2 pixels, so it runs ahead. When the length reaches `LONGEST` (20), `growing` turns `False`.

While shrinking, the tail moves 2 pixels and the length drops by 1. Now the head moves only 1 pixel, and the tail catches up. When the length gets down to `SHORTEST` (2), the arc starts growing again, and `hue` moves `COLOR_STEP` (40) steps along the color wheel. The `%` in `(tail + t) % NUMBER_PIXELS` wraps any pixel past 23 back to 0.

## Try It Yourself

1. Change `LONGEST` to `23`. How much of the ring does the arc fill now?
2. Change `COLOR_STEP` to `128`. How many colors does the spinner take turns with now?

## Check Your Understanding

1. How many pixels does the head move each step while the arc is growing?
2. What does the `growing` variable remember?
3. Why is the head of the arc brighter than its tail?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    Loading complete! Your spinner is ready to roll.

## What's Next

Go on to [Lab 13: Breathing Halo](13-breathing-halo.md).
