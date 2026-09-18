# Lab 43: Fire Simulation

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Fire is one of my favorite lights to make. It looks tricky, but it's four small steps repeated over and over. Let's light this up!

**Program file:** [`43-fire-simulation.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/43-fire-simulation.py)

## What you'll learn

- How to keep a list of **heat** numbers instead of a list of colors
- How to turn a heat number into a fire color
- How cooling, drifting, and sparking combine into one flame
- How `COOLING` and `SPARKING` change the way the fire looks

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

This lab does not use the buttons. You made a simpler flame in [Lab 18: Candle Flicker](18-candle-flicker.md), and the [Jake's Fire](../kits/jakes-fire/index.md) kit turns flickering pixels into a small campfire.

## The program

This program simulates a fire. Each pixel has a heat number that cools down, drifts upward, and gets new sparks near the bottom.

```python title="43-fire-simulation.py"
--8<-- "src/kits/moving-rainbow-base/43-fire-simulation.py"
```

Run it, and stand the strip on one end if you can. Pixel 0 is the bottom of the flame. Expect pale yellow near the base, orange in the middle, and dim red toward the top, all flickering.

!!! warning "Power check"
    We added up the colors this program makes. We estimate the strip draws about 900 mA on average and reaches about 1,200 mA at its brightest moments. A USB port supplies about 500 mA. Read [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go) to learn why. To stay safe, divide each color number by 4 in Step 4 of the loop, as shown below.

To make that change, replace the `strip[i] = heat_to_color(heat[i])` line in Step 4 with these lines. They use about a quarter of the power.

```python title="Your change"
for i in range(NUMBER_PIXELS):
    r, g, b = heat_to_color(heat[i])
    strip[i] = (r // 4, g // 4, b // 4)
```

## How it works

### Heat, not color

These lines set up the fire's settings and its list of heat numbers.

```python
COOLING = 55      # how fast each pixel cools down (higher = shorter flames)
SPARKING = 120    # chance (0-255) of a new spark appearing each frame
heat = [0] * NUMBER_PIXELS
```

A **list** is an ordered group of values, and `heat[3]` is the fourth one. The expression `[0] * NUMBER_PIXELS` makes a list of 30 zeros, one for each pixel. A heat number runs from 0 (cold) to 255 (white-hot). The program stores heat and works out the colors at the very end.

### Turn heat into color

This function changes a heat number into a color, using three ranges.

```python
def heat_to_color(h):
    # turn a heat value (0-255) into a fire color: black -> red -> yellow -> white
    if h < 85:
        return (h * 3, 0, 0)
    elif h < 170:
        return (255, (h - 85) * 3, 0)
    else:
        return (255, 255, (h - 170) * 3)
```

The word `elif` means "else if." A low heat adds only red. A middle heat keeps red at full and adds green, which makes orange and yellow. A high heat keeps red and green at full and adds blue, which makes white.

| Heat | Color it makes | Looks like |
|------|----------------|------------|
| 0 | `(0, 0, 0)` | Dark |
| 60 | `(180, 0, 0)` | Red |
| 127 | `(255, 126, 0)` | Orange |
| 200 | `(255, 255, 90)` | Pale yellow |
| 255 | `(255, 255, 255)` | White |

### Step 1: cool down

This step takes a random amount of heat away from every pixel.

```python
# Step 1: cool down every pixel a little
for i in range(NUMBER_PIXELS):
    cooldown = randint(0, (COOLING * 10) // NUMBER_PIXELS + 2)
    heat[i] = max(0, heat[i] - cooldown)
```

With the starting numbers, `(55 * 10) // 30 + 2` is 20. So each pixel loses a random amount from 0 to 20 every frame, about 10 on average. A **frame** is one picture of the fire. `max(0, ...)` keeps heat from dropping below 0.

A bigger `COOLING` number means a bigger cooldown, so the flames stay shorter.

### Step 2: heat drifts upward

This step slides heat up the strip and blends it with its neighbors.

```python
# Step 2: heat drifts upward and mixes with its neighbors
for i in range(NUMBER_PIXELS - 1, 1, -1):
    heat[i] = (heat[i - 1] + heat[i - 2] + heat[i - 2]) // 3
```

The loop counts down from pixel 29 to pixel 2. Each pixel takes an average of the two pixels below it, and the one two steps below counts twice. For example, if the pixel below has 90 and the one below that has 150, the new value is (90 + 150 + 150) // 3 = 130.

Working from the top down matters. The pixels below have not changed yet, so each pixel blends the old values. Pixels 0 and 1 are skipped, because nothing sits below them.

### Step 3: add a spark

This step sometimes drops a burst of new heat near the bottom.

```python
# Step 3: randomly spark a new flame near the bottom of the strip
if randint(0, 255) < SPARKING:
    spark_pixel = randint(0, 2)
    heat[spark_pixel] = min(255, heat[spark_pixel] + randint(160, 255))
```

`randint(0, 255)` picks one of 256 numbers. With `SPARKING` at 120, the test is true for 120 of them. That is a little less than half of all frames. A spark lands on pixel 0, 1, or 2 and adds 160 to 255 heat. `min(255, ...)` caps the total at 255.

### Step 4: draw

This step turns every heat number into a color and sends it to the strip.

```python
# Step 4: draw the heat values as fire colors
for i in range(NUMBER_PIXELS):
    strip[i] = heat_to_color(heat[i])
strip.write()

sleep(0.03)
```

The `sleep(0.03)` pause makes about 30 new frames every second. Watch the strip and you can see all four steps at work: sparks appear at the bottom, heat climbs, and the top fades away.

## Try it yourself

1. Change `COOLING = 55` to `COOLING = 100`, then to `COOLING = 20`. Which value gives short, nervous flames? Which gives tall, lazy ones? A low `COOLING` also lights the strip brighter, so try the Power check change first.
2. Change `SPARKING = 120` to `SPARKING = 30`, then to `SPARKING = 255`. What happens to the flicker?

## Check your understanding

1. What does the `heat` list hold, if it does not hold colors?
2. What are the four steps the program repeats every frame?
3. What happens to the flames when you raise `COOLING`, and why?
4. Why does Step 1 use `max(0, ...)` and Step 3 use `min(255, ...)`?
5. Which pixel is the bottom of the flame?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    That's a real simulation! You modeled how heat behaves, and the flicker appears all on its own.

**What's next:** In [Lab 44: Cellular Automaton](44-cellular-automaton.md), a single simple rule builds a whole pattern.
