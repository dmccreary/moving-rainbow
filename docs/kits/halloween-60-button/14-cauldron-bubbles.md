# Lab 14: Cauldron Bubbles

A witch's potion bubbles on your costume. Green and purple bubbles rise up, get brighter and pop in a white flash.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Double, double, toil and trouble! This potion uses a list that grows and shrinks.

**Program file:** [`14-cauldron-bubbles.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/14-cauldron-bubbles.py)

## What You'll Learn

- Add items to a list with `append()`
- Remove items with `remove()`
- Loop over a copy of a list with `[:]`

## What You'll Need

- Your costume with the strip connected

## The Program

This program sometimes adds a bubble, moves each bubble up, and pops the ones that reach their height.

```python
--8<-- "src/kits/halloween-60-button/14-cauldron-bubbles.py"
```

You should see green and purple bubbles rise from pixel 0 on a dark green potion and pop in white flashes.

## How It Works

Each bubble is a list: `[position, color, pop height]`. A new bubble is added with `bubbles.append()`.

When a bubble reaches its pop height, `bubbles.remove(bubble)` takes it out of the list.

We loop over `bubbles[:]`, which is a copy. Changing a list while you loop over it can skip items, so the copy keeps us safe.

## Try It Yourself

1. Change `NEW_BUBBLE_CHANCE` to `40` for a wild potion.
2. Make the potion purple and the bubbles orange.

## Check Your Understanding

1. What does `append()` do?
2. Why do we loop over `bubbles[:]`?
3. Why do bubbles get brighter as they rise?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 15: Jack-o'-Lantern Fire](15-jack-o-lantern-fire.md).
