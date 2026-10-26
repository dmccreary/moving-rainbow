# Lab 6: Orange and Purple Chase

Two comets race along your costume. An orange one runs down and a purple one runs back up. They pass right through each other in the middle.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Halloween colors, here we come! This is your first real costume pattern.

**Program file:** [`06-orange-and-purple-chase.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/06-orange-and-purple-chase.py)

## What You'll Learn

- Draw a **comet** with a fading tail
- Use `%` (**modulo**, the remainder after dividing) to wrap around the strip
- Mix two colors where comets overlap
- Write a **function** (a named block of code you can reuse)

## What You'll Need

- Your costume with the strip connected

## The Program

This program draws two comets each step, then moves them one pixel.

```python
--8<-- "src/kits/halloween-60-button/06-orange-and-purple-chase.py"
```

You should see an orange comet and a purple comet chase each other in opposite directions.

## How It Works

Each step starts with `strip.fill((0, 0, 0))`, which makes every pixel dark in memory. Then we draw both comets fresh.

The `fade()` function takes a color and an amount from 0.0 to 1.0. The head of the comet gets 1.0. Each tail pixel gets a little less.

`position = (position + 1) % NUMBER_PIXELS` adds one and wraps back to 0 after pixel 59. That is what modulo is for!

## Try It Yourself

1. Change `TAIL_LENGTH` to `12` for long comets.
2. Change the purple comet to green `(0, 255, 0)` for a zombie look.

## Check Your Understanding

1. What does `% NUMBER_PIXELS` do?
2. Why does each tail pixel use a smaller amount?
3. What does the `mix()` function do?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 7: Pumpkin Glow](07-pumpkin-glow.md).
