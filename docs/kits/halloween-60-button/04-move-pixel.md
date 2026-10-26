# Lab 4: Move a Pixel

One orange pixel runs down all 60 pixels of the strip and then starts again. This is how every moving pattern begins.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Lights that move look alive. Let's make one pixel take a trip down your costume!

**Program file:** [`04-move-pixel.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/04-move-pixel.py)

## What You'll Learn

- Use a `for` loop to visit every pixel
- Turn a pixel on, then off, to make it move
- Change the speed with a `DELAY` variable

## What You'll Need

- Your costume with the strip connected

## The Program

This program moves one orange pixel down the strip.

```python
--8<-- "src/kits/halloween-60-button/04-move-pixel.py"
```

You should see an orange dot zoom from pixel 0 to pixel 59, over and over.

## How It Works

`for i in range(NUMBER_PIXELS)` counts from 0 to 59. Each time, `i` is the pixel we light.

After the wait, we set the pixel back to `off` in memory. We do not call `strip.write()` again right away. The next step's `write()` shows the change. This keeps the strip from missing a frame.

## Try It Yourself

1. Make the dot move twice as fast.
2. Make the dot move backward. Hint: `range(NUMBER_PIXELS - 1, -1, -1)` counts down.

## Check Your Understanding

1. What numbers does `range(60)` count?
2. What happens if you never turn the pixel off?
3. Which variable changes the speed?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 5: Button Test](05-button-test.md).
