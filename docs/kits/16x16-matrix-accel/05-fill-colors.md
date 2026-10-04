# Lab 5: Fill Colors

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    One pixel is cute. 256 pixels is a party! But a big party needs big power, so we'll do some math first.
    Let's light this up!

**Program file:** [`05-fill-colors.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/16x16-matrix-accel/05-fill-colors.py)

## What you'll learn

- How a `for` loop with `range` visits every pixel
- How to fill the whole matrix with one color
- How much power lit pixels use
- Why the kit has a `LEVEL` setting
- How to check that your power supply holds up

## What you'll need

- Your kit, with the matrix wired as shown in the [Kit Guide](index.md)
- `config.py` saved on the Pico
- Thonny open and connected to your Pico

## The program

This program fills the whole matrix with red, then green, then blue, then white. Each color stays for one and a half seconds.

```python title="05-fill-colors.py"
--8<-- "src/kits/16x16-matrix-accel/05-fill-colors.py"
```

Run it. The whole matrix changes color every one and a half seconds. The colors are dim on purpose. If your Pico disconnects or the lights flicker when white appears, stop the program and read the power section below.

```text
Test 05: Fill Colors (version 1.0.0)
Fill: red
Fill: green
Fill: blue
Fill: white
```

![A simulated 16x16 LED matrix with every pixel lit a dim red](./img/fill-red.png){ width="320" }

*This picture was drawn by a computer simulator, so your real matrix may look a little different.*

## How it works

### Read the setting

```python
LEVEL = config.LEVEL
```

`config.LEVEL` is a number in your `config.py` file. In this kit it is 8. All four colors use `LEVEL` as their biggest number, like `(LEVEL, 0, 0)` for red. If you change `LEVEL` in `config.py`, every color follows.

### Fill every pixel

```python
for i in range(NUMBER_PIXELS):
    strip[i] = color
strip.write()
```

`range(NUMBER_PIXELS)` counts from 0 up to 255. That is 256 numbers, because the last number is not included. The loop sets every pixel to the same color. Then one `strip.write()` sends all the colors at once.

### The power math

Every pixel has three tiny lights inside. Each light uses a little electricity. A **milliamp** (mA) is a small amount of electric current. One pixel at full white, `(255, 255, 255)`, uses about 60 mA. That works out to about 0.078 mA for each color number.

A **USB** (Universal Serial Bus) port gives about 500 mA. Let's check the white fill:

| Step | Math | Answer |
|------|------|--------|
| Color numbers in one white pixel | 8 + 8 + 8 | 24 |
| Color numbers in 256 pixels | 256 × 24 | 6,144 |
| Current | 6,144 × 0.078 | about 480 mA |

That is just under the 500 mA that USB supplies. White is the biggest fill in this program, so `LEVEL = 8` is the right size. Now see what full power would need:

| Step | Math | Answer |
|------|------|--------|
| Color numbers in one pixel at full white | 255 + 255 + 255 | 765 |
| Color numbers in 256 pixels | 256 × 765 | 195,840 |
| Current | 195,840 × 0.078 | more than 15,000 mA, or 15 amps |

!!! warning "Watch out!"
    <img src="../../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    Never fill all 256 pixels with big numbers like 255. A USB port cannot supply 15 amps. The Pico may restart, or the wires and the matrix could get hot.

## Try it yourself

1. Work out on paper how many mA the **red** fill uses at `LEVEL = 8`. Use the table above as a guide. The answer is about 160 mA.
2. Work out on paper what the white fill would need if `LEVEL = 16`. Do not run it. Compare your answer with 500 mA.
3. Change the order of the colors in the list. Which color do you want to see first?

## Check your understanding

1. What does `range(NUMBER_PIXELS)` count from and to?
2. Why does the program use `LEVEL` and not 255?
3. Which fill uses the most power: red, green, blue, or white? Why?
4. What would happen if all 256 pixels used `(255, 255, 255)`?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You lit all 256 pixels and kept the power safe. That's math protecting your kit!

**What's next:** In [Lab 6: Walk the Pixels](06-walk-pixels.md), one pixel visits every spot to show the numbering.
