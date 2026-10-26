# Lab 16: Lightning Storm

A haunted thunderstorm rolls across your costume. Every few seconds lightning flashes and leaves a purple glow.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    This is the biggest pattern yet! It uses a **state machine**, the same idea games use to know what to do next.

**Program file:** [`16-lightning-storm.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/16-lightning-storm.py)

## What You'll Learn

- Build a **state machine** (a program that is always in one of a few named states)
- Use `sin()` to make soft, rolling clouds
- Time each part of the lightning with `ticks_ms()`

## What You'll Need

- Your costume with the strip connected

## The Program

This program draws the clouds each step, then does the job of the current state.

```python
--8<-- "src/kits/halloween-60-button/16-lightning-storm.py"
```

You should see dark purple clouds roll by. Every 2 to 6 seconds, part of the strip flashes white two or three times and fades out.

## How It Works

The `state` variable is `"calm"`, `"flash"`, `"dark"` or `"glow"`. Each state does its own job and decides when to switch to the next one.

`sin()` makes a smooth wave that goes up and down. Adding `cloud_time` slides the wave, so the clouds roll.

Real lightning flickers. The `"dark"` state makes a short gap between flashes to copy that.

## Try It Yourself

1. Make lightning strike more often. Hint: change the `randint(2000, 6000)` numbers.
2. Make the lightning green for a spooky storm.

## Check Your Understanding

1. What are the four states?
2. What does `sin()` help us draw?
3. Why is there a `"dark"` state?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 20: Main Template](20-main-template.md).
