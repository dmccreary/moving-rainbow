# Lab 12: Rainbow Cycle

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    What if the whole rainbow could spin around the strip? We'll shift every color over by one pixel, again and again. This rainbow is going places!

**Program file:** [`12-rainbow-cycle.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/12-rainbow-cycle.py)

## What you'll learn

- How an `offset` slides the rainbow one pixel at a time
- How the **modulo** operator `%` wraps a pixel number back to the start of the strip
- Why the rainbow needs no erasing when the loop repaints every pixel
- How the `sleep()` value sets the speed of the spin

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- The rainbow from [Lab 11: Rainbow](11-rainbow.md), because this lab builds on it

## The program

This program draws the rainbow over and over, and it starts each new drawing one pixel further along the strip.

```python title="12-rainbow-cycle.py"
--8<-- "src/kits/moving-rainbow-base/12-rainbow-cycle.py"
```

Run it. The whole rainbow rotates around the strip, and the red end moves toward the higher pixel numbers, away from the end where your wires connect. This program keeps going until you press **Stop**.

## How it works

### What stays the same

The `wheel()` function and the step size are the same as in [Lab 11](11-rainbow.md). Each pixel in the rainbow sits 8 positions further around the wheel than the pixel before it.

### Two counters

These two lines set up the numbers that change as the program runs.

```python
current_color = 0
offset = 0
```

`current_color` is the wheel position for the next pixel, as in Lab 11. `offset` is new. It tells the program how many pixels to slide the rainbow along the strip. It starts at 0, so the first rainbow looks like the one in Lab 11.

### Paint the strip again and again

This loop paints all 30 pixels, and then it makes one small change and paints them again.

```python
while True:
    for i in range(0,NUMBER_PIXELS):
        strip[(i+offset) % NUMBER_PIXELS] = wheel(current_color)
        current_color = current_color + color_wheel_step
        strip.write()
        sleep(.001)
    current_color = 0
    offset += 1
```

The `for` loop makes one **pass**, painting each of the 30 colors once. When the pass ends, two lines get ready for the next one. `current_color = 0` sends the wheel position back to red. `offset += 1` adds 1 to `offset`, so the next pass starts one pixel further along.

Every pass repaints all 30 pixels. Each pixel gets a new color on top of its old one, so nothing needs to be erased.

### Wrap around with modulo

The strip has pixels 0 to 29. What happens when `i + offset` reaches 30 or more? That is a pixel that does not exist. The **modulo** operator `%` fixes it. It gives the remainder after dividing. So `30 % 30` is 0, `31 % 30` is 1, and `5 % 30` is 5.

The expression `(i+offset) % NUMBER_PIXELS` therefore always lands between 0 and 29. A color that slides off the end of the strip comes back in at pixel 0.

| `offset` | Where the red pixel goes | Where the last color goes (`i` is 29) |
|----------|--------------------------|---------------------------------------|
| 0 | pixel 0 | pixel 29 |
| 1 | pixel 1 | pixel 0 |
| 2 | pixel 2 | pixel 1 |

See it in action in the [Modulo Wrap-Around MicroSim](../sims/modulo-wrap-simulation/index.md). Each pass moves the rainbow by one pixel, so 30 passes bring it all the way around.

### How fast is it?

Each pass paints 30 pixels, and each one waits `sleep(.001)`. So the waiting alone takes 30 × .001 = .03 seconds per pass. Each `strip.write()` also takes a little time. A full trip around the strip needs 30 passes, so it takes at least 30 × .03 = .9 seconds.

!!! warning "Power check"
    This program keeps all 30 pixels lit. Every wheel color adds up to 255, so each pixel draws about 20 mA. That makes about 600 mA for the strip, and a USB port supplies about 500 mA. See [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go) for the details. To cut the total to about 150 mA, divide each color number by 4.

Replace the line that starts with `strip[(i+offset) % NUMBER_PIXELS] =` with these two lines to dim the rainbow.

```python title="Your change"
red, green, blue = wheel(current_color)
strip[(i+offset) % NUMBER_PIXELS] = (red // 4, green // 4, blue // 4)
```

The first line splits the three numbers from `wheel()` into `red`, `green`, and `blue`. The `//` sign divides and drops any leftover decimal.

## Try it yourself

1. Change `offset += 1` to `offset -= 1`. Which way does the rainbow spin now?
2. Change `sleep(.001)` to `sleep(.01)`. How much slower is the spin? Work out the new minimum time for one trip around the strip.

## Check your understanding

1. What is `31 % 30`? What is `29 % 30`?
2. What does `offset` change about the picture on the strip?
3. Why does the program set `current_color = 0` after every pass?
4. How many passes does the rainbow need to travel once around a 30-pixel strip?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    Your rainbow is on the move! The `%` trick lets colors wrap around the strip like a loop, and you'll meet it again in later labs.

**What's next:** In [Lab 13: Moving Rainbow with the Color Wheel](13-moving-rainbow.md), a short rainbow slides along the strip and leaves the rest dark.
