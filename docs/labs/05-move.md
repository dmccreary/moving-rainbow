# Lab 05: Move a Pixel

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Time to send a light on a trip! One pixel will travel along your whole strip.
    That's real animation, and it starts right here.

**Program file:** [`05-move.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/05-move.py)

## What you'll learn

- How a loop variable like `i` picks a different pixel each time with `strip[i]`
- How `range(0,NUMBER_PIXELS)` visits every pixel on the strip
- How to erase a pixel in memory
- Why we write once per step, then sleep
- How the `sleep` time sets the speed of the motion

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- A quick look at `range` in [Lab 04: Dimmer](04-dimmer.md), since this lab uses it again

## The program

This program lights one red pixel at a time, moving from the first pixel to the last, and then starts over.

```python title="05-move.py"
--8<-- "src/kits/moving-rainbow-base/05-move.py"
```

Run it. A single red pixel runs down your strip in about three seconds, then jumps back to the start and runs again.

## How it works

### Let the loop pick the pixel

```python
for i in range(0,NUMBER_PIXELS):
    strip[i] = (100,0,0)
```

In Lab 02 we wrote `strip[0]` to pick the first pixel. Here the number in the brackets is `i`, the counter from the `for` loop. Each trip through the loop, `i` gets bigger, so a different pixel lights up.

`NUMBER_PIXELS` is 30 for the base kit. The `stop` number in `range` is not included, so `i` counts 0, 1, 2, and so on up to 29. Those are the 30 pixels on your strip. You can see how each index points to a pixel in the [Pixel Indexing Explorer](../sims/pixel-indexing-explorer/index.md).

### Write, then wait

```python
strip[i] = (100,0,0)
strip.write()
sleep(.1)
```

The `strip.write()` line sends the strip's colors down the wire, and pixel `i` lights up. Then `sleep(.1)` holds the picture for one tenth of a second. There are 30 steps of 0.1 seconds, so one pass takes about three seconds. The writes add a tiny bit more.

### Erase it in memory

```python
# erase the pixel. The next strip.write() shows the change, so we
# do not write again right away (the strip can miss back-to-back writes)
strip[i] = (0,0,0)
```

Remember from Lab 02 that `strip[i] = ...` only changes a note in the Pico's memory. This line changes pixel `i` back to `(0,0,0)`, which is off. The strip has not heard about it yet.

That is fine. The next step sets pixel `i+1` to red and calls `strip.write()`. That single write sends the whole strip: the old pixel is off, and the new pixel is on. One write does both jobs. The last pixel is erased the same way. Its change is sent by the first write of the next pass.

!!! info "Key idea"
    Write once per step, then sleep. After each write, the strip needs a short quiet moment to lock in the picture. Many strips need about 280 **microseconds** (millionths of a second) of quiet.

    On the Pico, two writes in a row leave only about 150 microseconds between them, so the strip can miss the second one. In an earlier version of this lab, writing twice in a row made the strip show only the first pixel.

### Repeat forever

The `for` loop sits inside `while True:`. When `i` reaches 29, the `for` loop ends, and `while True:` starts it again from pixel 0. Press **Stop** in Thonny to end the program.

## Try it yourself

1. Change the speed. Change `sleep(.1)` to `sleep(.03)`, then to `sleep(.01)`. Then try `sleep(.001)`. Does it still look faster? Each write for 30 pixels takes about a thousandth of a second, so very small sleeps stop making a difference.
2. Change the trip. Change `range(0,NUMBER_PIXELS)` to `range(0,10)`. Which pixels light up now? Then predict what `range(10,20)` will do before you try it.
3. Make a trail. Put a `#` at the start of the line `strip[i] = (0,0,0)`, so Python skips it. Predict what you will see, then run it. Remove the `#` when you are done.

## Check your understanding

1. What does the `i` in `strip[i]` stand for? Which values does it take?
2. About how long does one pass down the strip take? How did you work it out?
3. Why does the program erase the pixel without calling `strip.write()` right after?
4. What single write shows both the old pixel turning off and the new pixel turning on?
5. What happens after the last pixel?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You made a light travel! A loop, an index, and one write per step: that's the heart of animation.

**What's next:** In [Lab 06: Up and Down](06-up-and-down.md), the pixel runs to the end of the strip and comes back.
