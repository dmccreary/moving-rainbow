# Lab 12: Blood Drip

Red drops form at the top, then fall faster and faster, just like real drops. They land in a pool that fills up, then drains away.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    This one is extra spooky, and it uses real science! Gravity makes things speed up as they fall.

**Program file:** [`12-blood-drip.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/12-blood-drip.py)

## What You'll Learn

- Use a **float** (a number with a decimal point) for position and speed
- Add gravity to make a drop speed up
- Build a pattern from three parts: grow, fall and pool

## What You'll Need

- Your costume with the strip connected

## The Program

This program grows a drop, drops it with gravity, and adds it to the pool.

```python
--8<-- "src/kits/halloween-60-button/12-blood-drip.py"
```

You should see a red drop form at pixel 0, fall, and land in a dark red pool at the far end.

## How It Works

Each step, `speed += GRAVITY` makes the drop a little faster. Then `position += speed` moves it. This is how real falling works!

`int(position)` turns the float into a pixel number, because pixels only come in whole numbers.

The pool grows by one pixel per drop. When it is deeper than `POOL_MAX`, it drains away one pixel at a time.

## Try It Yourself

1. Change `GRAVITY` to `0.01`. Is the drop slower?
2. Make the drops green for alien slime.

## Check Your Understanding

1. What does `GRAVITY` change?
2. Why do we need `int()`?
3. What happens when the pool gets too deep?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 13: Bat Swarm](13-bat-swarm.md).
