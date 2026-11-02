# Lab 23: Speed and Direction

A rainbow comet circles the ring. Button 1 changes its speed and Button 2 makes it turn around.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Faster, slower, turn around! You are the driver of this comet.

**Program file:** [`23-speed-and-direction.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/ring-24/23-speed-and-direction.py)

![A comet with a green head and a rainbow tail moving around the ring](img/23-speed-and-direction.png){ width="260" }

*Drawn by a ring simulator on a computer, so your real ring may look a little different. On the real ring it moves.*

## What You'll Learn

- Store a **direction** as a number: `1` for clockwise and `-1` for counter-clockwise
- Pick a speed from a **tuple** (a list of values that never changes)
- Use an interrupt with a debounce for each button
- Keep a comet's tail behind its head, whichever way it goes

## What You'll Need

- Your Ring 24 kit with Button 1 on GPIO 15 and Button 2 on GPIO 14

## The Program

This program draws a rainbow comet and lets the two buttons change its speed and its direction.

```python
--8<-- "src/kits/ring-24/23-speed-and-direction.py"
```

You should see a 12-pixel rainbow comet going clockwise. Press Button 1 to go faster, and press Button 2 to flip it around.

## How It Works

`delays` holds five sleep times, from slow (0.16 seconds) to fast (0.01 seconds). `speed_index` picks one. It starts at 1, the second speed. Each press of Button 1 adds 1, and `% len(delays)` wraps from the fastest speed back to the slowest.

`direction` is `1` or `-1`. Button 2 does `direction = -direction`, which flips the sign. The line `position = (position + direction) % NUMBER_PIXELS` moves the head one step clockwise or one step counter-clockwise.

The tail pixels sit at `position - t * direction`. When `direction` is `-1`, the minus signs cancel, so the tail moves to the other side. The tail stays behind the head either way.

Both buttons use interrupts. Each one ignores presses less than `DEBOUNCE_MS` (200 ms) after the last one, because buttons bounce.

## Try It Yourself

1. Add a sixth speed of `0.3` to the start of `delays` for a very slow comet.
2. Change `TAIL_LENGTH` to `6` for a short comet.

## Check Your Understanding

1. What does `direction = -direction` do?
2. What happens when you press Button 1 at the fastest speed?
3. Why is the tail drawn at `position - t * direction`?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    Way to go, in both directions! You steered a comet with two buttons.

## What's Next

Go on to [Lab 24: Ring Clock](24-ring-clock.md).
