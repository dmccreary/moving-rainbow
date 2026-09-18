# Lab 30: Random Bounce

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Six dots are about to wander along your strip, each with its own color and direction. Watch closely, because this program hides a puzzle. Every bug is a puzzle in disguise!

**Program file:** [`30-random-bounce.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/30-random-bounce.py)

## What you'll learn

- How a **list of lists** can hold the position, direction, and color of every dot
- Why each dot must be a list and not a tuple
- How `randint()` picks random starting spots and directions
- How a dot turns around at the ends of the strip
- How to trace a program by hand to find a puzzle in it

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico, with the Shell window showing (this program prints a lot)

## The program

This program starts six dots on the strip. Each dot moves one pixel at a time and turns around at the ends.

??? example "Full program: 30-random-bounce.py (104 lines)"
    ```python title="30-random-bounce.py"
    --8<-- "src/kits/moving-rainbow-base/30-random-bounce.py"
    ```

Run it. Six dots move along the strip in different colors, but each one leaves a colored trail behind it. The Shell fills with text very fast.

## How it works

### Each dot is a list

```python
pixel_list = [
  [10, 1, (255, 0, 0)],
  [20, -1, (0, 255, 0)],
  [30, 1, (0, 0, 255)],
]
```

A **list** is a row of values inside square brackets. Here `pixel_list` is a list of lists, and each inner list is one dot. Each dot holds three values:

| Index | What it holds | First dot |
|-------|---------------|-----------|
| `[0]` | The position (the pixel number) | 10 |
| `[1]` | The direction: 1 moves toward higher numbers, -1 toward lower ones | 1 |
| `[2]` | The color as (red, green, blue) | (255, 0, 0) |

So `pixel_list[0][0]` is the position of the first dot, which is 10. And `pixel_list[1][1]` is the direction of the second dot, which is -1. The first index picks the dot. The second index picks a value inside it.

The third dot starts at position 30. Your strip has pixels 0 to 29, so 30 is one past the end. You will see how the program handles that below.

### Add dots at random spots

```python
def add_pixel(my_list, delay, color):
    random_index = randint(0, NUMBER_PIXELS-1)
    # random dir is 1 or -1
    dir = randint(-1,1)
    if dir == 0:
        dir = -1
    print('adding pixel at', random_index, 'moving', dir)
    # must be a list since tuple is non-mutable
    my_list.append(list((random_index, dir, color)))
```

The `add_pixel()` function adds one more dot to the list. The `randint(a, b)` function picks a random whole number from `a` to `b`, including both ends.

- `randint(0, NUMBER_PIXELS-1)` picks any pixel from 0 to 29.
- `randint(-1,1)` picks -1, 0, or 1. Zero is not a direction, so the code changes it to -1. That makes moving down twice as likely as moving up.

The program calls the function three times:

```python
add_pixel(pixel_list, 1, yellow)
add_pixel(pixel_list, 1, cyan)
add_pixel(pixel_list, 1, purple)
```

These calls add a yellow, a cyan, and a purple dot. The function does not use the middle value, `1`. Together with the first three dots, the list now holds six.

### Why lists, not tuples

```python
# must be a list since tuple is non-mutable
my_list.append(list((random_index, dir, color)))
```

Something is **mutable** if it can change after you make it. A **tuple** (values in round brackets, like a color) is not mutable. A list is.

Every dot's position must change on every step, so every dot must be a list. The `list(...)` part turns the three values into a list. The `.append()` part adds that list to the end of `pixel_list`. The color stays a tuple, because a dot keeps the same color all the time.

### Draw every dot

```python
def display_pixel(id):
    if id[0] < NUMBER_PIXELS:
        strip[id[0]] = id[2]
        strip.write()
```

This function draws one dot. Its parameter `id` is one inner list, so `id[0]` is the position and `id[2]` is the color. The `if` line skips any position past the end of the strip. That is how the third dot, at position 30, stays hidden on the first step.

```python
def display_pixels(pixel_list):
    for i in range(0, len(pixel_list)):
        print('displaying', pixel_list[i])
        display_pixel(pixel_list[i])
```

This function draws all of the dots. The `len()` function counts the items in a list, so `len(pixel_list)` is 6. The loop also prints each dot to the Shell.

### Move every dot

```python
while True:
    # for each pixel
    display_pixels(pixel_list)
    # update positions
    for i in range(0, len(pixel_list)):
        print('current pixel', pixel_list[i])
        ...
    sleep(.1)
```

One trip through this loop is one **frame**. Each frame draws every dot, moves every dot one pixel, and then waits 0.1 seconds. That makes about 10 frames each second. Each frame prints 12 lines to the Shell: 6 from drawing and 6 from moving.

!!! tip "Tip"
    To quiet the Shell, put a `#` in front of the `print` lines that say `'displaying'` and `'current pixel'`. Printing many lines slows the program.

The code for a dot with direction 1 looks like this:

```python
if pixel_list[i][1] == 1:
    new_index = pixel_list[i][0] + 1
    if new_index > NUMBER_PIXELS - 1:
        new_index = NUMBER_PIXELS - 1
        # reverse direction
        pixel_list[i][1] = -1
    pixel_list[i][0] = new_index
```

The dot steps up by 1. If that goes past pixel 29, the code holds the dot on 29 and flips its direction to -1. So a dot rests on pixel 29 for two frames before it heads back down.

The third dot goes through this on its first frame. It starts at 30, so it is hidden. Then the code moves it to 29 and turns it around. It appears on pixel 29 on the second frame.

A dot with direction -1 runs the `else` branch instead:

```python
else:
    new_index = pixel_list[i][0] - 1
    if new_index < 0:
        pixel_list[i][0] = 0
        pixel_list[i][1] = 1
    pixel_list[i][0] = pixel_list[i][0] - 1
```

The dot steps down by 1. If that goes below 0, the code sets the position to 0 and the direction to 1. But the last line then subtracts 1 again. Trace a dot coming down: its positions are 2, 1, 0, -1, 0, 1, 2.

!!! bug "Known issue"
    When a dot reaches pixel 0, the last line still subtracts 1, so its position becomes -1. Python treats `strip[-1]` as the last pixel, so the dot is drawn at the far end for one frame. Then it comes back up from pixel 0.

### What the strip really shows

Look at the loop again. It draws the dots and it moves the dots, but nothing turns a pixel off. The source has a function named `update_pixel()` that can erase, but no line calls it.

So every dot leaves a trail of its own color. A pixel stays lit until another dot paints over it. After a few seconds, the whole strip is lit. It shows a patchwork of colors that shift as the dots overwrite each other.

!!! bug "Known issue"
    Nothing turns a pixel off, so every dot leaves a colored trail behind it. The header says the dots "appear to bounce." After a few seconds, the strip fills with color instead.

!!! warning "Power check"
    Because the trails stay lit, the strip can fill with full-brightness colors. That draws roughly 900 mA, and up to 1,200 mA if every pixel is yellow, cyan, or purple. A USB port supplies about 500 mA (see [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go)). Until you erase the trails, change each 255 to 64 in the `pixel_list` colors and in `yellow`, `cyan`, and `purple`.

Want to see a bounce with real physics? In [Lab 25: Bouncing Ball](25-bouncing-ball.md), a ball speeds up as it falls and loses energy with every bounce.

## Try it yourself

### Challenge 1: Erase the old pixel

Turn off each dot's old spot before the dot moves. Find the comment `# update positions`. The `for` line right after it starts the loop that moves the dots. Add the three lines that follow `for` below, and indent them to match the lines already there.

```python title="Your change"
for i in range(0, len(pixel_list)):
    old_index = pixel_list[i][0]
    if old_index < NUMBER_PIXELS:
        strip[old_index] = off
    # ...the rest of the loop stays the same
```

The `if` line matters. The third dot starts at position 30, and `strip[30]` would stop the program.

Run it now. Do the trails disappear? You can also see a dot blink at the far end each time a dot reaches pixel 0.

Bonus puzzle: the blink at the far end comes from the last line of the `else` branch, `pixel_list[i][0] = pixel_list[i][0] - 1`. Can you make that line run only when the dot did not bounce?

### Challenge 2: Add another dot

Add this line below the `add_pixel(pixel_list, 1, purple)` line. The color `orange` is already defined near the top of the program.

```python title="Your change"
add_pixel(pixel_list, 1, orange)
```

The Shell should now report 7 items in the list.

## Check your understanding

1. What three values does each inner list hold?
2. Why must each dot be a list and not a tuple?
3. Which direction number moves a dot toward pixel 0?
4. Why is the third dot not drawn on the first frame?
5. Why does the strip fill with color instead of showing six moving dots?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You tracked six dots with one list of lists, and you found the puzzles by tracing the code by hand. That is what real coders do!

**What's next:** In [Lab 31: Button Modes](31-modes.md), your two buttons switch between twelve light shows.
