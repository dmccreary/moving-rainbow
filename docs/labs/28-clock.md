# Lab 28: Binary Clock

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    We're turning your strip into a clock that tells time in 1s and 0s. Each pixel is on or off, and together they spell out the hour, minute, and second. Let's light this up!

**Program file:** [`28-clock.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/28-clock.py)

## What you'll learn

- How **binary** (counting with only 0 and 1) shows any number from 0 to 63 on six pixels
- How a function turns a number into a list of bits with `%` and `//`
- How `localtime()` gives you the hour, minute, and second
- How to trace a program to find a block of code that gets skipped

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico, with the Shell window showing (this program prints the time there)

## The program

This program shows the time as three groups of six pixels. Seconds are red, minutes are green, and hours are blue.

??? example "Full program: 28-clock.py (103 lines)"
    ```python title="28-clock.py"
    --8<-- "src/kits/moving-rainbow-base/28-clock.py"
    ```

Run it. Six dim white marker pixels appear, with a red, a green, and a blue group between them. The red group changes every second.

## How to read the clock

Each group has six pixels. Each pixel stands for one **bit** (a single binary digit: 1 means on, 0 means off). The pixel closest to the start of the group is the 1s place. Each pixel after it is worth double the one before.

| Pixel in the group | 1st | 2nd | 3rd | 4th | 5th | 6th |
|--------------------|-----|-----|-----|-----|-----|-----|
| Worth | 1 | 2 | 4 | 8 | 16 | 32 |

Suppose the 1st, 3rd, and 6th pixels of the red group are lit. Add their values: 1 + 4 + 32 = 37. It is 37 seconds past the minute.

On paper, we write binary with the biggest place first. This clock puts the smallest place first. Six bits make 64 different patterns, so a group can count from 0 to 63. That covers seconds and minutes (0 to 59) and hours (1 to 12).

Here is where each group sits on the strip:

| Group | Color | Pixels | White markers |
|-------|-------|--------|---------------|
| Seconds | red | 1 to 6 | 0 and 7 |
| Minutes | green | 10 to 15 | 9 and 16 |
| Hours | blue | 20 to 25 | 19 and 26 |

## How it works

### Three lists hold the bits

```python
sec_bits = [0,0,0,0,0,0]
min_bits = [0,0,0,0,0,0]
hr_bits = [0,0,0,0,0,0]
```

A **list** is a row of values inside square brackets. Each of these lists holds six bits, one for each pixel in a group. They all start at 0.

### Turn a number into bits

```python
def decimal_to_binary(n, a):
    global sec_bits
    for i in range(0,6):
        if n % 2:
            a[i] = 1
        else:
            a[i] = 0
        ## n halfed
        n //= 2
```

A **function** is a named block of code you can run again and again. This one takes a number `n` and a list `a`, and it fills `a` with the bits of `n`.

Two math tools do the work. The `%` sign is the **modulo** operator, which gives the remainder after dividing. So `n % 2` is 1 for an odd number and 0 for an even one. The `//=` line cuts `n` in half and drops any leftover.

Here is the loop working on 37:

| Step `i` | `n` | `n % 2` | Bit stored in `a[i]` | `n` after halving |
|----------|-----|---------|----------------------|-------------------|
| 0 | 37 | 1 | 1 | 18 |
| 1 | 18 | 0 | 0 | 9 |
| 2 | 9 | 1 | 1 | 4 |
| 3 | 4 | 0 | 0 | 2 |
| 4 | 2 | 0 | 0 | 1 |
| 5 | 1 | 1 | 1 | 0 |

The list ends up as `[1, 0, 1, 0, 0, 1]`. The first bit stored goes into `a[0]`, so `a[0]` is the 1s place. The program prints this list to the Shell, so you can compare it with the pixels.

### Draw the bits

```python
def display_binary(binary, index, color):
    for i in range(0, 6):
        ...
        if binary[i] == 1:
            strip[index+i] = color
        else:
            strip[index+i] = (0,0,0)
    strip.write()
```

This function draws one group. The `index` is the first pixel of the group, so `index+i` walks along the group. A 1 lights the pixel in `color`, and a 0 turns it off. One `strip.write()` at the end shows the whole group at once.

Because the color is a parameter, the same function draws the red, green, and blue groups. The colors are dim on purpose: `(10,0,0)` is only 10 out of 255, so the clock glows softly.

### Mark the groups

```python
def display_mark(loc):
    strip[loc] = (5,5,5)
    strip.write()
```

The color `(5,5,5)` is a very dim white. The program calls this function six times, two markers per group:

```python
display_mark(0)
display_mark(7)
```

Those two calls bracket the seconds group. The later calls use 9 and 16 for minutes, and 19 and 26 for hours.

### Read the time

```python
now = localtime()
hour = now[3]
# use AM/PM 12 hour time
if hour > 12:
    hour = hour - 12
minute = now[4]
```

The `localtime()` function returns a **tuple** (a fixed row of values). It holds the year, month, day, hour, minute, second, and more. Position 3 is the hour, 4 is the minute, and 5 is the second.

The `if` line turns 13 into 1, 14 into 2, and so on. Now the hours run from 1 to 12. At midnight `hour` is 0, so no blue pixels light.

!!! warning "Heads up"
    The Pico has no battery to keep time while it is unplugged. It knows the right time only if something set its clock. Check the numbers the program prints in the Shell against a real clock. If they are wrong, the strip shows the Pico's time instead of yours.

### The loop

```python
while True:
    now = localtime()
    ...
    sec = now[5]
    print(hour, ':', minute, ' ', sec, sep='')
    ...
    decimal_to_binary(sec, sec_bits)
    print('sec:', sec, sec_bits)
    display_binary(sec_bits, 1, (10,0,0))
    ...
    sleep(1)
```

Every pass through the loop reads the time again. It prints the hour, minute, and second in the Shell, like `3:42 37`. The `sep=''` part tells `print` to add no spaces between the pieces.

Next, the loop converts the seconds to bits and draws the red group, starting at pixel 1. Then `sleep(1)` waits one second.

### The block that gets skipped

```python
if sec == 60:
    minute = minute + 1
    sec = 0
    decimal_to_binary(minute, min_bits)
```

This block is meant to update the minutes when a minute ends. It waits for `sec` to reach 60. But `localtime()` counts seconds from 0 to 59 and then starts again at 0. So `sec == 60` is always false, and the computer skips the block every time.

!!! bug "Known issue"
    The minutes and hours are drawn once, when the program starts. The `if sec == 60:` test always fails, because seconds only count from 0 to 59. After startup, only the red seconds group changes.

## Try it yourself

### Challenge 1: Find the bug

Run the program and wait for the minute number in the Shell to change. Does the green group change with it? To solve the puzzle, remember the last minute you drew. Then redraw the group whenever `minute` is different.

Add the first line above `while True:`. Add the `if` block inside the loop, right after `minute = now[4]`.

```python title="Your change"
last_minute = -1   # put this above the while True: line

while True:
    now = localtime()
    minute = now[4]
    # put this block inside the loop, after minute = now[4]
    if minute != last_minute:
        decimal_to_binary(minute, min_bits)
        display_binary(min_bits, 10, (0,10,0))
        last_minute = minute
    sleep(1)
```

The `!=` sign means "is not equal to". Now do the same for the hours. Use `last_hour`, `hr_bits`, pixel `20`, and the color `(0,0,10)`.

### Challenge 2: Brighten the seconds

On the line `display_binary(sec_bits, 1, (10,0,0))`, change `(10,0,0)` to `(40,0,0)`. How does the red group look now?

## Check your understanding

1. In a group of six pixels, which pixel is the 1s place?
2. The 1st, 2nd, and 4th pixels of the seconds group are lit. What second is it?
3. Why does each group use six pixels?
4. What does `n % 2` tell `decimal_to_binary()` about the number?
5. Why does the computer skip the `if sec == 60:` block every time?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You told time with light! Binary is how computers store numbers inside, and now you can read it right off a strip.

**What's next:** In [Lab 29: Larson Scanner](29-larson-scanner.md), a red eye sweeps back and forth along the strip.
