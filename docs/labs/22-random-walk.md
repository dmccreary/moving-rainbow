# Lab 22: Random Walk

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Meet the wandering pixel! It can't decide where to go, so it flips a coin at every step.
    Heads, go left. Tails, go right!

**Program file:** [`22-random-walk.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/22-random-walk.py)

## What you'll learn

- What a random walk is
- How `randint(0,1)` works like a coin flip
- How `loc % NUMBER_PIXELS` wraps a pixel around both ends of the strip
- How `+=` and `-=` move a number up or down

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

## The program

This program moves one dim white pixel a step left or right, chosen at random, about ten times each second.

```python title="22-random-walk.py"
--8<-- "src/kits/moving-rainbow-base/22-random-walk.py"
```

Run it. A dim white dot starts in the middle of the strip and wanders. When it walks off one end, it appears at the other end.

## How it works

### Start in the middle

```python
loc = int(NUMBER_PIXELS/2)
```

The name `loc` is short for *location*. It is a **variable** (a name that holds a value that can change). It holds the pixel number where the dot is now.

The `/` symbol divides and gives a decimal answer, so `30/2` is 15.0. The `int()` function drops the decimal part, so `loc` starts as the whole number 15.

### Show the pixel, then erase it

```python
strip[loc % NUMBER_PIXELS] = (10,10,10)
strip.write()
sleep(.1)
strip[loc % NUMBER_PIXELS] = (0,0,0)
```

The first line lights the pixel. Equal amounts of red, green, and blue make white, and the small number 10 keeps it dim. Then `strip.write()` shows it, and `sleep(.1)` holds it for a tenth of a second.

The last line turns the pixel off in the Pico's memory. The next `strip.write()` sends the erase and the new pixel together.

### Flip a coin

```python
move_dir = randint(0,1)
if move_dir == 0:
    loc -= 1
else:
    loc += 1
```

The call `randint(0,1)` gives 0 or 1, each about half the time. That's like a coin flip. The name `move_dir` is short for *move direction*.

The `if` line checks the coin. On 0, `loc -= 1` subtracts 1 from `loc`, so the dot moves to a lower pixel number. On 1, `loc += 1` adds 1, so the dot moves to a higher pixel number.

A path made of random steps is called a **random walk**. Scientists use random walks to study things like drifting smoke and wandering animals. [Chapter 13](../chapters/13-intermediate-animations/index.md) shows a random walk that stops at the ends of the strip instead of wrapping.

### Wrap around with modulo

The variable `loc` has no limit. It can grow past 29 or shrink below 0. But the strip only has pixels 0 to 29. The **modulo** operator `%` gives the remainder after a division, and it fixes this puzzle. In every line that touches the strip, the code uses `loc % NUMBER_PIXELS`.

- `30 % 30` is 0, so walking past the last pixel lands on the first.
- `31 % 30` is 1, so the walk keeps going from the start.
- `-1 % 30` is 29, so walking left from pixel 0 lands on the last pixel.

When you divide by 30, Python's `%` always gives an answer from 0 to 29. That's why the dot can leave either end and come back on the other side. You can watch this in the [Modulo Wrap-Around Animation](../sims/modulo-wrap-simulation/index.md) MicroSim.

## Try it yourself

1. Change the color on the first `strip[loc % NUMBER_PIXELS]` line from `(10,10,10)` to `(0,0,40)`. What color is the wanderer now? The erase line keeps `(0,0,0)`.
2. Make the walk lopsided. Change `move_dir = randint(0,1)` to `move_dir = randint(0,3)`. Only 0 sends the dot left. What happens over time?

## Check your understanding

1. Which pixel does the dot start on?
2. What two values can `randint(0,1)` give? What does each one do to `loc`?
3. What are `31 % 30` and `-1 % 30`?
4. Why does the dot stay on the strip?
5. Why does the code use `int()` in `int(NUMBER_PIXELS/2)`?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You made a pixel that wanders on its own! A coin flip and a bit of modulo can make surprising motion.

**What's next:** In [Lab 23: Heartbeat](23-heartbeat.md), one pixel beats like a heart: a strong pulse, a softer pulse, and a rest.
