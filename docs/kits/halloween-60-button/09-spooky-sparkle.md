# Lab 9: Spooky Sparkle

Random pixels flash orange or purple, then slowly fade away, like sparks from a witch's wand.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Time for a little magic! Random numbers make every sparkle a surprise.

**Program file:** [`09-spooky-sparkle.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/09-spooky-sparkle.py)

## What You'll Learn

- Pick random numbers with `randint()`
- Read a pixel's color back with `strip[i]`
- Fade every pixel a little each step

## What You'll Need

- Your costume with the strip connected

## The Program

This program fades all pixels a little, then lights two new random sparks.

```python
--8<-- "src/kits/halloween-60-button/09-spooky-sparkle.py"
```

You should see orange and purple sparks pop up all over the strip and fade out.

## How It Works

`randint(0, NUMBER_PIXELS - 1)` picks a random pixel. `randint(0, 1)` is like flipping a coin to pick the color.

`r, g, b = strip[i]` reads the color a pixel has now. We multiply each part by `FADE_SPEED` (0.85), so the pixel keeps 85% of its color each step.

We never clear the strip. Old sparks fade a little at a time, which makes the trails.

## Try It Yourself

1. Change `NEW_SPARKS` to `5` for a busy sparkle.
2. Change `FADE_SPEED` to `0.95`. What happens to the trails?

## Check Your Understanding

1. What does `randint(0, 1)` give you?
2. Why do the sparks fade instead of turning off?
3. What would `FADE_SPEED = 1` do?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 10: Ghost Drift](10-ghost-drift.md).
