# Binary Counter

Computers don't actually store numbers the way we write them. They store
**binary** — patterns of 1s and 0s. In this lesson, five pixels count from
0 to 31 in binary, right in front of you.

!!! tip "Pixel says..."
    Deep down, I'm just patterns of on and off — that's what an LED
    really is! Counting in binary is like seeing how my circuits think.

## What you'll learn

- What binary numbers are and how they represent decimal numbers
- How to use a **bit mask** to check a single bit inside a number
- How the `<<` (shift) and `&` (and) operators work together
- What Python's built-in `bin()` function shows you

## What you'll need

- Your Pico and NeoPixel strip
- The kit's `config.py` file
- No buttons are needed for this lesson

## Reading a Number in Binary

A decimal number like `13` is written in binary as `01101`. Each position
stands for a power of two: 16, 8, 4, 2, 1. Add up the positions with a `1`:
`8 + 4 + 1 = 13`. Five pixels are enough to show any number from 0 to 31.

## Checking One Bit at a Time

To find out if a particular bit is `1` or `0`, this program uses a **bit
mask** — a number with only one bit turned on:

```python
if n & (1 << bit):
```

`1 << bit` shifts the number `1` to the left by `bit` places, making a mask
like `00001`, `00010`, or `00100`. The `&` operator compares `n` to that
mask, bit by bit, and the result is only non-zero if both numbers have a
`1` in that same position.

## The Full Program

```python
# Count up in binary, using the first 5 pixels as bits.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

NUM_BITS = 5    # 5 bits can count from 0 to 31
ON_COLOR = (0, 150, 0)
OFF_COLOR = (0, 0, 0)


def show_binary(n):
    for bit in range(NUM_BITS):
        # (1 << bit) makes a mask like 00001, 00010, 00100...
        # n & mask checks if that one bit is a 1 or a 0
        if n & (1 << bit):
            strip[bit] = ON_COLOR
        else:
            strip[bit] = OFF_COLOR
    strip.write()


count = 0
while True:
    show_binary(count)
    print(count, "=", bin(count))
    sleep(1)
    count = (count + 1) % (2 ** NUM_BITS)   # wrap back to 0 after 31
```

Watch the first five pixels and the Shell at the same time. Every second,
the count goes up by one, and you can watch the binary pattern change to
match the printed number.

!!! info "Pixel thinks..."
    Python's `bin()` function turns a number into a binary text string,
    starting with `0b`. Try typing `bin(13)` straight into the Thonny
    Shell and see what it prints.

## Try It Yourself

- Change `NUM_BITS` to `3`. What's the highest number you can now count to?
- Reverse the display so pixel 0 shows the *largest* bit instead of the smallest.

## Check Your Understanding

1. What does the expression `1 << 3` produce, in binary?
2. What does the `&` operator do in the line `if n & (1 << bit):`?
3. What is the highest number 5 bits can represent?
4. Why does the counter wrap back to 0 instead of continuing past 31?

!!! success "You've got this!"
    You just watched your Pico count the same way every computer does
    underneath all the code you write. That's a real look under the hood!

**What's next:** in [Charge-Up Game](43-charge-up-game.md), you'll measure
*how long* a button is held down, not just whether it's pressed.
