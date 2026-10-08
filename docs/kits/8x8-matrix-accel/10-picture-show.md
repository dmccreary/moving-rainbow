# Lab 10: Picture Show

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    One picture is nice. Eight pictures is a show! Your two buttons will flip through a gallery:
    a heart, an alien, a ghost, and more. Let's light this up!

**Program files:** [`10-picture-show.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/8x8-matrix-accel/10-picture-show.py) and [`pictures.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/8x8-matrix-accel/pictures.py)

## What you'll learn

- How a **module** can hold pictures for other programs to share
- How a list can hold pairs of things, like a name and a picture
- How the `%` sign makes a count wrap around
- How to use a button press to step forward or back
- How a program keeps time without stopping to sleep

## What you'll need

- Your kit, with the matrix and both buttons wired as shown in the [Kit Guide](index.md)
- These files saved on the Pico: `config.py`, `pictures.py`, and `10-picture-show.py`
- Thonny open and connected to your Pico
- The `draw` function from [Lab 9](09-smiley-face.md) and the button ideas from [Lab 3](03-button-test.md)

## The program

This program shows eight pictures, one at a time. Button 1 moves to the next picture, and Button 2 moves back.

```python title="10-picture-show.py"
--8<-- "src/kits/8x8-matrix-accel/10-picture-show.py"
```

Run it. The smiley face appears first. Press Button 1 to see the next picture. Press Button 2 to go back. If you press nothing for three seconds, the show moves on by itself. The Shell prints the name of each picture.

```text
Lab 10: Picture Show (version 1.0.0)
Picture 1 - Smiley
Button 1 is next. Button 2 is back. Press Ctrl-C to stop.
Picture 2 - Heart
Picture 3 - Alien
```

Here are all eight pictures in the gallery:

![Eight small simulated 8x8 LED matrices, each showing one picture: a yellow smiley, a red heart, a green alien, a white ghost with blue eyes, a rainbow with white clouds, a pink flower, a blue-green fish, and a white rocket with red fins](./img/gallery.png){ width="640" }

*This picture was drawn by a computer simulator, so your real matrix may look a little different.*

## How it works

### A file full of pictures

The pictures do not live in the program. They live in their own file, `pictures.py`. A Python file that other programs can load is called a **module**. The line `import pictures` loads it.

Here is the color key from that file. It has more letters than the key in Lab 9, so the pictures can use more colors.

```python title="pictures.py (lines 13 to 25)"
--8<-- "src/kits/8x8-matrix-accel/pictures.py:13:25"
```

Here is one of the pictures. It uses R for red and one P for a pink shine.

```python title="pictures.py (lines 38 to 47)"
--8<-- "src/kits/8x8-matrix-accel/pictures.py:38:47"
```

To use something from a module, write the module name, a dot, and the thing's name. So `pictures.COLORS` is the color key inside `pictures.py`.

### A list of pairs

```python title="pictures.py (lines 115 to 125)"
--8<-- "src/kits/8x8-matrix-accel/pictures.py:115:125"
```

`GALLERY` is a list. Each item is a pair in parentheses: a name and a picture. The list sets the order of the show.

```python
name, picture = pictures.GALLERY[number]
```

This line takes one pair out of the list and gives each half its own name. When `number` is 0, `name` is `"Smiley"` and `picture` is the smiley picture.

### Wrap around with `%`

```python
number = (number + step) % count
```

The variable `step` is 1 for next and -1 for back. There are 8 pictures, so `count` is 8, and the picture numbers go from 0 to 7. What happens after picture 7? The `%` sign gives the remainder after dividing, and that makes the count wrap around.

| `number` | `step` | `number + step` | `% 8` | What you see |
|----------|--------|-----------------|-------|--------------|
| 2 | 1 | 3 | 3 | The next picture |
| 7 | 1 | 8 | 0 | Back to the first picture |
| 0 | -1 | -1 | 7 | Around to the last picture |

In Python, `-1 % 8` is 7. So stepping back from the first picture lands on the last one.

### Spot a press

```python
if now1 == 0 and last1 == 1:        # button 1 was just pressed
    step = 1
```

Remember that pressed means zero. This line asks two questions at once. Is the button down now? Was it up last time? Both must be true. That way one press moves one picture, even if you hold the button down.

### Keep time without sleeping

```python
if step == 0 and ticks_diff(ticks_ms(), shown_at) >= HOLD_MS:
    step = 1                        # nobody pressed, so move on
```

A long `sleep` would make the program deaf to your buttons. So this program looks at a clock. `ticks_ms()` is the Pico's stopwatch. It counts **milliseconds**, which are thousandths of a second. The variable `shown_at` remembers when the picture appeared. `ticks_diff` works out how long ago that was.

When 3,000 milliseconds have passed, the show moves on. The loop still runs 50 times a second, so a button press is never missed.

!!! info "Key idea"
    Checking a clock lets a program do two jobs at once. This one waits for the next picture *and* listens for buttons.

## Try it yourself

1. Speed up the show. Change `HOLD_MS = 3000` to `HOLD_MS = 1000`. How many seconds does each picture stay now?
2. Run the show backwards. Find the line `step = 1` with the comment `nobody pressed`. Change it to `step = -1`. Which picture comes after the smiley now?
3. Add your own picture. Open `pictures.py` and add this tree above the `GALLERY` list.

    ```python
    TREE = [
        "...YY...",
        "...GG...",
        "..GGGG..",
        "..GRGG..",
        ".GGGGGG.",
        ".GGGGRG.",
        "GGGGGGGG",
        "...NN...",
    ]
    ```

    Then add this line at the end of `GALLERY`, right before the closing `]`. Save `pictures.py` onto the Pico and run the show again.

    ```python
        ("Tree", TREE),
    ```

4. Change the order. Move the lines in `GALLERY` so the rocket comes first.

## Check your understanding

1. What is a module? Which module holds the pictures?
2. What two things are in each item of `GALLERY`?
3. `number` is 7 and you press Button 1. What is the new `number`? Show the math.
4. Why does the program remember `last1` and `last2`?
5. Why does this program check a clock, and not use one long `sleep`?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built a picture gallery with buttons! Phones and tablets flip through photos the same way.

**What's next:** In [Lab 11: Winking Face](11-winking-face.md), you will make a picture move.
