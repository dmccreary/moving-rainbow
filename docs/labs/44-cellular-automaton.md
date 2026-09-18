# Lab 44: Cellular Automaton

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    One tiny rule, used again and again, can grow a pattern that looks random! Mathematicians still study the rule in this lab. Let's light this up!

**Program file:** [`44-cellular-automaton.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/44-cellular-automaton.py)

## What you'll learn

- What a **cellular automaton** is: a row of on-or-off cells that follow one rule
- How a cell and its two neighbors turn into a number from 0 to 7
- Why the rule is called "Rule 30" (the number 30 hides the rule, written in binary)
- How `% n` bends the strip into a ring, so pixel 29 sits next to pixel 0

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- No buttons are needed in this lab
- Helpful: [Lab 39: Binary Counter](39-binary-counter.md), which shows how binary numbers work

## The program

This program lights one pixel in the middle of the strip. Then it uses Rule 30 to work out each new row of pixels and shows that row for 0.3 seconds.

```python title="44-cellular-automaton.py"
--8<-- "src/kits/moving-rainbow-base/44-cellular-automaton.py"
```

Run it. One teal pixel glows in the middle of the strip. More pixels join it, and the row keeps changing in a pattern that looks random. Press **Stop** in Thonny to end it.

!!! warning "Power check"
    Rule 30 lights about 15 of the 30 pixels on average. That draws about 412 mA. Some rows light as many as 26 pixels, which is about 714 mA. A USB port supplies about 500 mA (see [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go)). To stay safe, change `ON_COLOR = (0, 150, 200)` to `ON_COLOR = (0, 37, 50)`. That divides each number by 4 and cuts the worst case to about 178 mA.

## How it works

### Cells and generations

A **cellular automaton** is a row of **cells** that follow one rule. Each cell is either on (`1`) or off (`0`). All the cells change together, in steps called **generations**. In this lab, each pixel is one cell.

This code builds the first generation.

```python
# start with a single lit pixel in the middle
cells = [0] * NUMBER_PIXELS
cells[NUMBER_PIXELS // 2] = 1
```

`[0] * NUMBER_PIXELS` builds a **list** (an ordered row of values) with 30 zeros. Then `NUMBER_PIXELS // 2` works out to `15`. The `//` symbol divides and drops any leftover. So cell 15 turns on and every other cell stays off.

### Draw one generation

This function shows one generation on the strip.

```python
def draw(cells):
    for i in range(len(cells)):
        strip[i] = ON_COLOR if cells[i] else OFF_COLOR
    strip.write()
```

For each cell, `ON_COLOR if cells[i] else OFF_COLOR` picks teal when the cell is `1` and black when it is `0`. Then `strip.write()` sends all 30 colors at once.

The main loop draws a generation, waits 0.3 seconds, and then swaps in the next generation.

```python
while True:
    draw(cells)
    sleep(0.3)
    cells = next_generation(cells)
```

The strip shows only one generation at a time. You watch a single row change, not the whole history.

### Each cell looks at its neighbors

To find the new state of a cell, the rule looks at three cells. They are the cell itself and its two **neighbors** (the cells right next to it). Together they make the cell's **neighborhood**.

```python
        left = cells[(i - 1) % n]
        center = cells[i]
        right = cells[(i + 1) % n]
```

Three cells that are each on or off can be arranged in 2 × 2 × 2 = 8 ways. So every cell has one of 8 possible neighborhoods.

### Wrap around the edges

Pixel 0 has no neighbor on its left, because the strip ends there. The `% n` fixes that. The **modulo** operator `%` gives the remainder after dividing. Here `n` is 30, so `(0 - 1) % 30` is `29`. The left neighbor of pixel 0 is pixel 29.

At the other end, `(29 + 1) % 30` is `0`. So the right neighbor of pixel 29 is pixel 0. The strip acts like a ring. The [Modulo Wrap-Around Animation](../sims/modulo-wrap-simulation/index.md) shows this idea in motion.

### Turn the neighbors into a number

This line joins the three cells into one number from 0 to 7.

```python
        pattern = (left << 2) | (center << 1) | right
```

**Binary** numbers use only the digits 0 and 1. Each place in a binary number is worth twice the place to its right: 1, 2, 4, and so on. One binary digit is called a **bit**.

The `<<` symbol slides a bit to the left, which makes it worth more. So `left << 2` makes left worth 4, `center << 1` makes center worth 2, and `right` stays worth 1. The `|` symbol glues the three together. In plain math, `pattern` is 4 × left + 2 × center + right.

Left on, center off, and right on gives 4 + 0 + 1 = 5.

### Look up the answer in Rule 30

This line finds the new state of the cell.

```python
        new_cells[i] = (RULE >> pattern) & 1
```

The number 30 in binary is `00011110`. It has eight bits, one for each pattern number from 0 to 7. Each bit is the answer for one neighborhood.

The `>>` symbol slides 30 to the right by `pattern` places. That puts the bit we want in the last place. Then `& 1` keeps only that last bit, so the answer is `0` or `1`.

| Left | Center | Right | Pattern number | New center |
|:----:|:------:|:-----:|:--------------:|:----------:|
| 1 | 1 | 1 | 7 | 0 |
| 1 | 1 | 0 | 6 | 0 |
| 1 | 0 | 1 | 5 | 0 |
| 1 | 0 | 0 | 4 | 1 |
| 0 | 1 | 1 | 3 | 1 |
| 0 | 1 | 0 | 2 | 1 |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 0 | 0 | 0 | 0 |

Read the last column from top to bottom: `0 0 0 1 1 1 1 0`. That is 30 in binary. That is why the rule is called Rule 30.

Here is the first step by hand. Only pixel 15 is on. Look at pixel 14. Its left neighbor is off, it is off, and its right neighbor (pixel 15) is on. That is pattern 1. `30 >> 1` is `15`, and `15 & 1` is `1`, so pixel 14 turns on. Pixels 15 and 16 also turn on. Every other pixel stays off. The second generation lights pixels 14, 15, and 16.

## The pattern behind the strip

The strip shows one row at a time. If you wrote each row on paper, one below the other, a picture would appear. Here are the first 12 generations worked out by following the rule. The top row is generation 0. A `#` is a lit pixel and a `.` is a dark one.

```text
...............#..............
..............###.............
.............##..#............
............##.####...........
...........##..#...#..........
..........##.####.###.........
.........##..#....#..#........
........##.####..######.......
.......##..#...###.....#......
......##.####.##..#...###.....
.....##..#....#.####.##..#....
....##.####..##.#....#.####...
```

The left edge grows a neat diagonal line. The inside looks random. The pattern spreads one pixel farther toward each side in every generation. After about 15 generations it reaches the ends of the strip and wraps around the ring.

A ring of 30 cells can make only about a billion different rows, so the pattern must repeat someday. In this program, the first repeat comes after more than 30 hours.

## Try it yourself

1. Change `RULE = 30` to `RULE = 90`. Run it and watch. Then try `RULE = 110`. How does each strip look different from Rule 30?
2. See the triangle for yourself. Replace the `while True:` loop at the bottom of the program with this loop. The Shell then prints each generation as a row of `#` and `.` characters.

```python title="Your change"
while True:
    draw(cells)
    line = ""
    for c in cells:
        line += "#" if c else "."
    print(line)
    sleep(0.3)
    cells = next_generation(cells)
```

## Check your understanding

1. Which three cells decide whether a pixel is on in the next generation?
2. Which part of the code makes pixel 0 the right neighbor of pixel 29?
3. A cell has its left neighbor on, itself off, and its right neighbor off. What is `pattern`? Does the cell turn on?
4. What is 30 in binary, and where do those digits show up in the table?
5. If every bit of `RULE` were 0, what would the strip show after the first generation?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You ran a real piece of mathematics on a strip of light! One rule, eight answers, and a pattern that looks random.

**What's next:** In [Lab 45: Sorting Visualizer](45-sorting-visualizer.md), you'll watch a bubble sort put pixel brightness in order.
