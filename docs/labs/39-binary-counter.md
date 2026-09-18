# Lab 39: Binary Counter

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Deep down, every computer thinks in patterns of on and off. That's what I am: a tiny light that is on or off! Today we'll watch numbers turn into light.

**Program file:** [`39-binary-counter.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/39-binary-counter.py)

## What you'll learn

- How **binary** uses only 0s and 1s to write any number
- How five pixels can show every number from 0 to 31
- How `<<` and `&` check one bit of a number
- How `%` wraps a counter back to 0

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico, with the Shell (the text area at the bottom) in view

This lab does not use the buttons.

## The program

This program counts from 0 to 31 in binary, using the first five pixels as lights. It adds 1 every second and prints the number in the Shell.

```python title="39-binary-counter.py"
--8<-- "src/kits/moving-rainbow-base/39-binary-counter.py"
```

Run it. The five pixels change every second, and the Shell prints a line like `5 = 0b101`. After 31, all five pixels go dark and the count starts over at 0.

## How it works

### Numbers made of bits

We write numbers with ten digits, 0 through 9. **Binary** uses only two digits, 0 and 1. Each binary digit is called a **bit**, and one pixel can show one bit. A lit pixel means 1, and a dark pixel means 0.

Each pixel has a **place value**, and the place values double as you move along the strip.

| Pixel | 0 | 1 | 2 | 3 | 4 |
|-------|---|---|---|---|---|
| Place value | 1 | 2 | 4 | 8 | 16 |

To read the number, add up the place values of the lit pixels. If pixels 0 and 2 are lit, the number is 1 + 4 = 5. If all five are lit, it is 1 + 2 + 4 + 8 + 16 = 31. If none are lit, it is 0. That gives 32 different patterns, so five pixels can show 0 to 31.

On paper, we write the 1s place on the right, so 5 looks like `00101`. On the strip, the 1s place is pixel 0, at the start of the strip. If you built [Lab 28: Binary Clock](28-clock.md), you have already seen binary on the strip.

### Test one bit

This function lights each pixel if its bit is 1 and turns it off if its bit is 0.

```python
def show_binary(n):
    for bit in range(NUM_BITS):
        # (1 << bit) makes a mask like 00001, 00010, 00100...
        # n & mask checks if that one bit is a 1 or a 0
        if n & (1 << bit):
            strip[bit] = ON_COLOR
        else:
            strip[bit] = OFF_COLOR
    strip.write()
```

The `for` loop counts `bit` from 0 to 4, one number for each pixel. The `if` line has two new tools.

`1 << bit` makes a **mask**, which is a number with a single 1 in it. The `<<` symbol slides the 1 to the left by `bit` places.

| `bit` | `1 << bit` | In binary |
|-------|------------|-----------|
| 0 | 1 | `00001` |
| 1 | 2 | `00010` |
| 2 | 4 | `00100` |
| 3 | 8 | `01000` |
| 4 | 16 | `10000` |

`n & mask` uses the `&` symbol, which means "and." It compares two numbers bit by bit. The answer has a 1 only where both numbers have a 1. Here is what happens when `n` is 5, which is `00101`.

| Check | Binary | Answer | Pixel |
|-------|--------|--------|-------|
| `5 & 4` (bit 2) | `00101` and `00100` | `00100`, which is 4 | On |
| `5 & 2` (bit 1) | `00101` and `00010` | `00000`, which is 0 | Off |

An `if` treats 0 as false and any other number as true. So `if n & (1 << bit):` asks, "Is this bit a 1?" The function then calls `strip.write()` once, after the loop, so all five pixels change together.

### Count and print

This loop shows the count, prints it, waits a second, and adds 1.

```python
count = 0
while True:
    show_binary(count)
    print(count, "=", bin(count))
    sleep(1)
    count = (count + 1) % (2 ** NUM_BITS)   # wrap back to 0 after 31
```

`bin(count)` turns a number into binary text. For example, `bin(5)` gives `0b101`. The `0b` at the front means "binary," and leading zeros are left off.

The `%` symbol is the **modulo** operator, which gives the remainder after a division. The `**` symbol means "to the power of," so `2 ** NUM_BITS` is 32. After 31, `count + 1` is 32, and 32 divided by 32 leaves a remainder of 0. That is how the counter wraps back to 0. You can see wrapping in action in the [Modulo Wrap](../sims/modulo-wrap-simulation/index.md) MicroSim.

## Try it yourself

1. Change `NUM_BITS = 5` to `NUM_BITS = 3`. What is the biggest number the counter reaches now?
2. Make the strip read like paper, with the 1s place at the far end. Change both `strip[bit]` lines to use `strip[NUM_BITS - 1 - bit]`.

## Check your understanding

1. Which number do lit pixels 1 and 3 make?
2. What does `1 << 3` make, and how does it look in binary?
3. What does the `&` symbol do in the line `if n & (1 << bit):`?
4. What is the biggest number five bits can show?
5. Why does the counter go back to 0 after 31?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You can read binary now! Every number inside every computer looks like this, only with many more lights.

**What's next:** In [Lab 40: Charge-Up Game](40-charge-up-game.md), you'll measure how long a button is held down.
