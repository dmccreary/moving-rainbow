# Fire Simulation

You've already built a [Candle Flicker](16-candle.md). This lesson goes
much further: a true heat simulation, where every pixel has its own
"temperature" that cools down, drifts, and occasionally sparks — just
like a real flame.

!!! tip "Pixel says..."
    This is one of the most-loved effects in the whole LED hobby world.
    It looks complicated, but it's really just four simple steps,
    repeated really fast.

## What you'll learn

- How to simulate heat with a list of numbers instead of colors
- How to turn a "heat" value into a realistic fire color
- How cooling, drifting, and sparking combine into one convincing effect

## What you'll need

- Your Pico and NeoPixel strip
- The kit's `config.py` file
- No buttons are needed for this lesson

## Heat Instead of Color

Instead of storing a color for each pixel, this program stores a **heat**
value from 0 (cold) to 255 (white-hot) in a list called `heat`. A helper
function turns each heat value into a fire color only at the very end:

```python
def heat_to_color(h):
    if h < 85:
        return (h * 3, 0, 0)          # black to red
    elif h < 170:
        return (255, (h - 85) * 3, 0) # red to yellow
    else:
        return (255, 255, (h - 170) * 3)  # yellow to white
```

## Four Steps, Every Frame

1. **Cool down** — every pixel loses a little heat, by a random amount.
2. **Drift upward** — heat spreads from each pixel to the ones above it,
   just like real heat rises.
3. **Spark** — every so often, a random pixel near the bottom gets a big
   burst of new heat.
4. **Draw** — turn every heat value into a color and update the strip.

## The Full Program

```python
# A flickering fire effect using a simple heat simulation. Heat cools
# down over time, drifts upward, and new sparks appear near the bottom.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

COOLING = 55      # how fast each pixel cools down (higher = shorter flames)
SPARKING = 120    # chance (0-255) of a new spark appearing each frame
heat = [0] * config.NUMBER_PIXELS


def heat_to_color(h):
    # turn a heat value (0-255) into a fire color: black -> red -> yellow -> white
    if h < 85:
        return (h * 3, 0, 0)
    elif h < 170:
        return (255, (h - 85) * 3, 0)
    else:
        return (255, 255, (h - 170) * 3)


while True:
    # Step 1: cool down every pixel a little
    for i in range(config.NUMBER_PIXELS):
        cooldown = randint(0, (COOLING * 10) // config.NUMBER_PIXELS + 2)
        heat[i] = max(0, heat[i] - cooldown)

    # Step 2: heat drifts upward and mixes with its neighbors
    for i in range(config.NUMBER_PIXELS - 1, 1, -1):
        heat[i] = (heat[i - 1] + heat[i - 2] + heat[i - 2]) // 3

    # Step 3: randomly spark a new flame near the bottom of the strip
    if randint(0, 255) < SPARKING:
        spark_pixel = randint(0, 2)
        heat[spark_pixel] = min(255, heat[spark_pixel] + randint(160, 255))

    # Step 4: draw the heat values as fire colors
    for i in range(config.NUMBER_PIXELS):
        strip[i] = heat_to_color(heat[i])
    strip.write()

    sleep(0.03)
```

Run it and stand your strip up on one end if you can. Flames should
flicker upward from the bottom, with realistic-looking random variation.

!!! info "Pixel thinks..."
    Notice `heat_to_color` never touches randomness at all — every flicker
    you see comes from the heat values changing underneath it. Separating
    "what number is this" from "what color does that number look like" is
    a pattern you'll see in professional graphics code too.

## Try It Yourself

- Raise `COOLING` to `100` for short, nervous flames. Lower it to `20` for
  tall, lazy ones.
- Change `SPARKING` to `255` to make every single frame spark.

## Check Your Understanding

1. What does the `heat` list store, if not colors?
2. What are the four steps this program repeats every frame?
3. What does raising `COOLING` do to the flames, and why?
4. Why is `heat_to_color` written as three separate ranges instead of one formula?

!!! success "You've got this!"
    That's a real simulation, not just a pattern — you modeled how heat
    actually behaves and let the visuals emerge on their own.

**What's next:** in [Cellular Automaton](47-cellular-automaton.md), you'll
build a pattern that isn't simulating anything physical at all — just a
simple rule, repeated.
