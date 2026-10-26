# Lab 13: Bat Swarm

A swarm of purple bats flutters along your costume under the moonlight. Every bat flies at its own speed.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Bats! Each one has its own speed, so we use two lists to keep track of them all.

**Program file:** [`13-bat-swarm.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/13-bat-swarm.py)

## What You'll Learn

- Keep two lists that go together: positions and speeds
- Use a negative speed to fly backward
- Use `%` to wrap a bat from one end to the other

## What You'll Need

- Your costume with the strip connected

## The Program

This program moves every bat by its speed and draws it with a wing.

```python
--8<-- "src/kits/halloween-60-button/13-bat-swarm.py"
```

You should see six purple bats flying both ways on a dim yellow sky. They flap as they fly.

## How It Works

`positions[b]` and `speeds[b]` belong to the same bat number `b`. Lists that line up like this are called **parallel lists**.

A speed like 0.25 means the bat moves one pixel every four steps. A negative speed flies backward.

`% NUMBER_PIXELS` wraps a bat that flies off one end back in at the other end.

## Try It Yourself

1. Change `NUMBER_OF_BATS` to `12`.
2. Make the moon brighter by changing `moon_color`.

## Check Your Understanding

1. What is a parallel list?
2. What does a negative speed do?
3. How does a bat flap its wings?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 14: Cauldron Bubbles](14-cauldron-bubbles.md).
