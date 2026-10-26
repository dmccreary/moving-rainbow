# Lab 10: Ghost Drift

A pale ghost with a fading tail floats down your costume, turns around at the end and floats back.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Boo! This ghost knows which way it is going because of one little variable.

**Program file:** [`10-ghost-drift.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/10-ghost-drift.py)

## What You'll Learn

- Use a `direction` variable of 1 or -1
- Bounce at both ends of the strip
- Make a tail that fades faster with `**` (power)

## What You'll Need

- Your costume with the strip connected

## The Program

This program draws the ghost and its tail, then moves the ghost one pixel in its direction.

```python
--8<-- "src/kits/halloween-60-button/10-ghost-drift.py"
```

You should see a pale blue-white ghost float slowly to the end of the strip and back.

## How It Works

`position += direction` moves the ghost. When `direction` is 1 it goes down. When it is -1 it comes back.

When the ghost reaches pixel 0 or pixel 59, `direction = -direction` flips it around.

The tail is drawn behind the ghost, on the other side of its direction. `(1 - t / TAIL_LENGTH) ** 2` squares the amount, so the tail fades quickly.

## Try It Yourself

1. Make the ghost green `(0, 255, 60)` for a slime ghost.
2. Add a second ghost that starts at the other end.

## Check Your Understanding

1. What does `direction = -direction` do?
2. What is `0.5 ** 2`?
3. Why do we check `0 <= index < NUMBER_PIXELS`?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 11: Monster Eyes](11-monster-eyes.md).
