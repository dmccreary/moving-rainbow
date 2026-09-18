# Lab 45: Sorting Visualizer

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Computers sort things all the time: names, scores, songs. Today we get to watch one do it, one small step at a time. Let's light this up!

**Program file:** [`45-sorting-visualizer.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/45-sorting-visualizer.py)

## What you'll learn

- What an **algorithm** is, and how **bubble sort** puts a list in order
- How a list of numbers becomes pixel brightness
- How to swap two list items in a single line
- How a **flag** variable (`swapped`) lets a loop stop early

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- No buttons are needed in this lab
- Helpful: two `for` loops, one inside the other, do most of the work. If loops are new, review [Chapter 4](../chapters/04-python-control-flow-loops/index.md)

## The program

This program gives every pixel a random brightness. Then it sorts the pixels from dimmest to brightest, and the two pixels being compared glow red.

```python title="45-sorting-visualizer.py"
--8<-- "src/kits/moving-rainbow-base/45-sorting-visualizer.py"
```

Run it. You see 30 green pixels of random brightness for one second. Then two red pixels move along the strip, comparing neighbors and swapping them. After about 20 seconds, the strip is in order: dimmest at pixel 0 and brightest at pixel 29.

The program prints the sorted list in the Shell and then stops. Press **Run** again to sort a new random order.

## How it works

### Brightness stands for a number

This line makes the list of numbers to sort.

```python
values = [randint(10, 255) for _ in range(NUMBER_PIXELS)]
```

A **list** is an ordered row of values. This list is named `values`. The `for _ in range(NUMBER_PIXELS)` part repeats 30 times, and each time `randint(10, 255)` picks a random whole number from 10 to 255. The `_` is a name for a counter that the loop does not need.

Each number belongs to the pixel at the same position. `values[0]` is for pixel 0, `values[1]` is for pixel 1, and so on. The smallest possible number is 10, so even the dimmest pixel still glows.

Random brightness averages about half of full. All 30 pixels together draw about 312 mA, which is under the 500 mA a USB port supplies. See [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go) for more.

### Draw the strip

This function turns the list into light.

```python
def draw(highlight_a=None, highlight_b=None):
    for i in range(NUMBER_PIXELS):
        brightness = values[i]
        if i == highlight_a or i == highlight_b:
            strip[i] = (brightness, 0, 0)   # the pair being compared: red
        else:
            strip[i] = (0, brightness, 0)   # everything else: green
    strip.write()
```

A bigger number means a brighter pixel. The two inputs, `highlight_a` and `highlight_b`, name the pair to color red. The `=None` gives them a starting value of "nothing". So `draw()` with nothing in the parentheses lights every pixel green.

### Compare and swap

An **algorithm** is a step-by-step recipe for solving a problem. **Bubble sort** is a recipe for putting a list in order. It looks at two neighbors. If they are in the wrong order, it swaps them.

```python
        if values[i] > values[i + 1]:
            values[i], values[i + 1] = values[i + 1], values[i]
            swapped = True
```

We want small numbers on the left. If the left number is bigger than the right number, the pair is in the wrong order. The middle line swaps them in one step. Python works out both values on the right side first and then puts them into the two places on the left, so nothing gets lost.

### Passes along the strip

One trip along the strip is called a **pass**. Two loops make the passes.

```python
for pass_num in range(NUMBER_PIXELS - 1):
    swapped = False
    for i in range(NUMBER_PIXELS - 1 - pass_num):
        draw(i, i + 1)
        sleep(0.03)
```

In the first pass, `i` goes from 0 to 28, so the red pair steps along 29 times. The brightest value wins every comparison it joins, so it gets carried to pixel 29. It rises to the end like a bubble.

After that, pixel 29 is finished. Each pass can stop one pixel sooner than the last. The `- pass_num` does this. The second pass makes 28 comparisons, the third makes 27, and so on.

### Stop early with a flag

This check ends the sorting as soon as the list is in order.

```python
    if not swapped:
        break   # nothing moved this pass - the list is already sorted
```

`swapped` starts every pass as `False`. Any swap sets it to `True`. If a whole pass ends with no swaps, every pair is in order. Then `break` leaves the loop early. A variable that remembers "did something happen?" is called a **flag**.

### How long does it take?

In the worst case, the program makes 29 + 28 + 27 + ... + 1 = 435 comparisons. Each one pauses for 0.03 seconds, so about 13 seconds go to comparing. A random list also needs about 217 swaps, and each swap adds another 0.03 seconds. Add them up and you can expect about 20 seconds.

### The finish

These last lines show the sorted strip and print the list.

```python
draw()   # final result: sorted dimmest to brightest
print("sorted!", values)
```

The program has no `while True`, so it ends here. The Shell shows `sorted!` followed by the 30 numbers in order.

## Try it yourself

1. Change both `sleep(0.03)` lines inside the inner loop to `sleep(0.2)`. Watch the red pair. Can you guess which pair will swap next?
2. Sort the other way. Change `>` to `<` in the line `if values[i] > values[i + 1]:`. Which end of the strip is brightest now?

## Check your understanding

1. In this program, what does a bigger number in `values` look like on the strip?
2. What does `values[i], values[i + 1] = values[i + 1], values[i]` do?
3. Why does the inner loop make fewer comparisons on each pass?
4. What does it mean when `swapped` is still `False` at the end of a pass?
5. Where does the brightest pixel end up after the first pass?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You watched a real algorithm think, one comparison at a time! Sorting is one of the most common jobs a computer does, and now you can see how it works.

**What's next:** In [Lab 46: Binary Search Visualizer](46-binary-search-visualizer.md), the strip guesses your secret pixel number, using your button presses as clues.
