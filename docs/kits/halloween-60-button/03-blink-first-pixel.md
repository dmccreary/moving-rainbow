# Lab 3: Blink the First Pixel

Now we talk to the LED strip! This program blinks the very first pixel orange, on and off.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Hi! I'm a pixel too, so this lab is my favorite. You are about to light up your very first NeoPixel. Let's light this up!

**Program file:** [`03-blink-first-pixel.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/03-blink-first-pixel.py)

## What You'll Learn

- Make a **NeoPixel** object for the strip
- Set one pixel's color with a **tuple** (a group of three numbers)
- Send colors to the strip with `strip.write()`
- Use `BRIGHTNESS` to keep colors safe

## What You'll Need

- Your costume with the strip connected
- `config.py` saved on the Pico

## The Program

This program blinks pixel 0 orange.

```python
--8<-- "src/kits/halloween-60-button/03-blink-first-pixel.py"
```

You should see the pixel closest to the Pico blink orange once every second.

## How It Works

A color is three numbers: red, green and blue. Each one goes from 0 (off) to 255 (full). Orange is a lot of red, a little green and no blue: `(255, 80, 0)`.

We multiply each number by `BRIGHTNESS`. With 0.25, orange becomes about `(63, 20, 0)`. It still looks orange, just dimmer.

`strip[0] = orange` only changes the color in the Pico's memory. Nothing changes on the strip until `strip.write()` sends the colors out.

## Try It Yourself

1. Make the pixel purple. Try `(140, 0, 255)`.
2. Blink pixel 59, the last pixel, instead of pixel 0.

## Check Your Understanding

1. What are the three numbers in a color?
2. What does `strip.write()` do?
3. Why is the first pixel number 0 and not 1?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 4: Move a Pixel](04-move-pixel.md).
