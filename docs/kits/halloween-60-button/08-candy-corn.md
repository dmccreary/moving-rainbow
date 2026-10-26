# Lab 8: Candy Corn

Stripes of yellow, orange and white, like candy corn, slide along your costume.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Who wants a treat? These stripes look good enough to eat!

**Program file:** [`08-candy-corn.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/08-candy-corn.py)

## What You'll Learn

- Make repeating stripes with `//` (whole-number division) and `%`
- Keep colors in a **list** (an ordered group of values)
- Slide a pattern by adding an offset

## What You'll Need

- Your costume with the strip connected

## The Program

This program colors every pixel by its stripe, then shifts the stripes one pixel.

```python
--8<-- "src/kits/halloween-60-button/08-candy-corn.py"
```

You should see yellow, orange and white stripes, each 4 pixels wide, slide down the strip.

## How It Works

`(i + offset) // STRIPE_WIDTH` tells us which stripe a pixel is in. Pixels 0 to 3 are stripe 0, pixels 4 to 7 are stripe 1, and so on.

`% len(stripes)` wraps the stripe number to 0, 1 or 2, so the three colors repeat forever.

Adding 1 to `offset` each step moves every stripe one pixel.

## Try It Yourself

1. Change `STRIPE_WIDTH` to `2` or `8`.
2. Add a fourth color to the `stripes` list. Try green.

## Check Your Understanding

1. What is `7 // 4`? What is `7 % 4`?
2. What makes the stripes move?
3. Why does adding a color to the list just work?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 9: Spooky Sparkle](09-spooky-sparkle.md).
