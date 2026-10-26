# Lab 15: Jack-o'-Lantern Fire

A flickering fire, like the candle inside a jack-o'-lantern. This is a real **simulation** (a program that copies how something works in the real world).

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Fire is one of the coolest effects there is. We will copy how heat really moves!

**Program file:** [`15-jack-o-lantern-fire.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/15-jack-o-lantern-fire.py)

## What You'll Learn

- Keep a heat number for every pixel in a list
- Cool, rise and spark the heat each step
- Turn a number into a color with a function

## What You'll Need

- Your costume with the strip connected

## The Program

This program updates the heat of every pixel in four steps, then turns each heat number into a color.

```python
--8<-- "src/kits/halloween-60-button/15-jack-o-lantern-fire.py"
```

You should see flames flicker up from pixel 0 in red, orange and yellow.

## How It Works

Step 1: every pixel cools a little. Step 2: heat moves up and mixes with the pixels below. Step 3: sometimes a new spark lights near the bottom.

Step 4: `heat_to_color()` turns heat into color. Low heat is dark red, middle heat is orange and high heat is yellow.

Turn your strip so pixel 0 is at the bottom, and the flames rise up your costume.

## Try It Yourself

1. Change `COOLING` to `90` for short flames, or `20` for tall ones.
2. Change `SPARKING` to `200` for a roaring fire.

## Check Your Understanding

1. What are the four steps of the fire?
2. What color is the hottest heat?
3. What does `COOLING` change?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 16: Lightning Storm](16-lightning-storm.md).
