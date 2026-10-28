# Lab 19: Demo Mode

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Time to show off everything you built! One program runs all 18 shows and games.
    It can even start by itself when the kit gets power. Let's light this up!

**Program files:** [`19-template-main.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/8x8-matrix-accel/19-template-main.py) and five demo modules:
[`fill_colors.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/8x8-matrix-accel/fill_colors.py),
[`walk_pixels.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/8x8-matrix-accel/walk_pixels.py),
[`row_column_sweep.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/8x8-matrix-accel/row_column_sweep.py),
[`winking_face.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/8x8-matrix-accel/winking_face.py), and
[`accel_bubble.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/8x8-matrix-accel/accel_bubble.py)

**Printable guide:** the [Demo Mode Guide (PDF)](demo-mode-guide.pdf) shows and explains all 18 modes on one page.
Print it and set it next to your kit. There is also a [web version](demo-mode-guide.html).

## What you'll learn

- How one program can run every show and game in the kit
- Why `sleep()` cannot notice a button press, and how `kit.wait()` can
- How a file named `main.py` makes the Pico start a program by itself
- How `try` and `except` keep a show running when a part stops answering
- How to choose which modes your own demo shows

## What you'll need

- Your whole kit: the matrix, the accelerometer, and both buttons, wired as shown in the [Kit Guide](index.md)
- **Every** `.py` file from the kit folder saved on the Pico. The quickest way is `./upload-code.sh` (see [Get the Code onto the Pico](index.md#get-the-code-onto-the-pico))
- Thonny open and connected to your Pico
- A USB wall charger, like a phone charger, if you want the demo to run without a computer. Many power banks switch themselves off with this kit (see the warning in [Make the kit start by itself](#make-the-kit-start-by-itself))
- Ideas from [Lab 18: Modes](18-modes.md)

## The program

This program is a bigger mode machine. It works like Lab 18, but it holds every show and game from Labs 5 to 18.

```python title="19-template-main.py"
--8<-- "src/kits/8x8-matrix-accel/19-template-main.py"
```

Run it. A **1** appears on the matrix, then all 64 pixels fill with red. Press Button 1 (GP14) for the next mode and Button 2 (GP15) to go back. The Shell names each mode as it loads:

```text
Lab 19: Demo Mode (version 1.1.0)
Mode 1 - Fill colors (module fill_colors)
  RAM free: 200816 bytes
Mode 2 - Walk the pixels (module walk_pixels)
  RAM free: 209344 bytes
```

The `RAM free` number depends on your Pico. Here is one moment from each of the 18 modes:

![Eighteen small simulated 8x8 LED matrices, one for each mode: a red fill, one purple pixel, a green row, a winking smiley, a heart, the letter M, three dots, seven dots, colors with trails, rain, rings, a teal bubble, one, three and seven rolling dots, sloshing water, a maze, and a rainbow spiral drawn by tilting](./img/demo-modes.svg){ width="700" }

*These pictures were drawn by a computer simulator running the real code, so your real matrix may look a little different.*

| Mode | Show | From | Uses the tilt? |
|------|------|------|----------------|
| 1 | Fill colors | [Lab 5](05-fill-colors.md) | No |
| 2 | Walk the pixels | [Lab 6](06-walk-pixels.md) | No |
| 3 | Row and column sweep | [Lab 8](08-row-column-sweep.md) | No |
| 4 | Winking face | [Lab 9](09-smiley-face.md) and [Lab 11](11-winking-face.md) | No |
| 5 | Picture show | [Lab 10](10-picture-show.md) | No |
| 6 | Scrolling message | [Lab 12](12-scrolling-message.md) | No |
| 7 | Three slow bouncing dots | [Lab 18](18-modes.md) | No |
| 8 | Seven faster bouncing dots | Lab 18 | No |
| 9 | Twelve colors with trails | Lab 18 | No |
| 10 | Rainbow rain | Lab 18 | No |
| 11 | Ripple rings | Lab 18 | No |
| 12 | Accelerometer bubble | [Lab 14](14-accel-bubble.md) | Yes |
| 13 | One dot that rolls as you tilt | Lab 18 | Yes |
| 14 | Three dots that roll and bump | Lab 18 | Yes |
| 15 | Seven rainbow dots that roll and bump | Lab 18 | Yes |
| 16 | Sloshing water | [Lab 15](15-sloshing-water.md) | Yes |
| 17 | Tilt-a-maze | [Lab 16](16-tilt-a-maze.md) | Yes |
| 18 | Tilt-a-sketch | [Lab 17](17-tilt-a-sketch.md) | Yes |

Labs 1 to 4 and Lab 7 check your wiring, and Lab 13 only prints numbers, so the demo leaves them out.

## How it works

### The same mode machine as Lab 18

This list is the whole menu:

```python title="19-template-main.py (lines 53 to 83)"
--8<-- "src/kits/8x8-matrix-accel/19-template-main.py:53:83"
```

Each item names a mode, the module to load, and the settings to hand it. The loop after the list is the same loop as in Lab 18. It shows the mode number, loads the module with `__import__`, and calls its `run` function. A button press raises `ModeChange`, and the loop unloads the module and moves on. Lab 18 explains each step in [How it works](18-modes.md#how-it-works).

### Why the early labs need a demo version

Labs 5 to 14 each set up their own hardware and pause with `sleep()`. Here is the loop from Lab 5:

```python title="05-fill-colors.py (lines 30 to 36)"
--8<-- "src/kits/8x8-matrix-accel/05-fill-colors.py:30:36"
```

During `sleep(1.5)`, the Pico waits for one and a half seconds and looks at nothing else. A button press in that time goes unnoticed. The loop also never ends, so a mode machine could never get control back.

So each early lab in the demo has a **demo version**. A demo version is a module that does the same thing, but uses `kit.py` and pauses with `kit.wait()`. Here is the demo version of Lab 5:

```python title="fill_colors.py"
--8<-- "src/kits/8x8-matrix-accel/fill_colors.py"
```

Compare the two loops. The colors and the timing match, but `sleep(1.5)` became `kit.wait(HOLD_MS)`. You met `kit.wait()` in Lab 18. It sleeps in 10 millisecond pieces and checks the buttons after each piece, so a press stops the show right away.

| Lab | Its demo version |
|-----|------------------|
| Lab 5: Fill Colors | `fill_colors.py` |
| Lab 6: Walk the Pixels | `walk_pixels.py` |
| Lab 8: Row and Column Sweep | `row_column_sweep.py` |
| Labs 9 and 11: Smiley Face and Winking Face | `winking_face.py` |
| Lab 14: Accelerometer Bubble | `accel_bubble.py` |

The labs themselves stay the same, so each one still reads from top to bottom on its own. Labs 10 and 12 need no new module, because Lab 18 already has `picture_show.py` and `scroll_text.py`. Labs 15, 16, and 17 already keep their code in modules.

!!! info "Key idea"
    A program only notices a button while it is checking for one. Pausing in small pieces keeps it listening.

### Sharing the buttons

This item in `MODES` starts the sketch from Lab 17:

```python title="19-template-main.py (lines 81 to 82)"
--8<-- "src/kits/8x8-matrix-accel/19-template-main.py:81:82"
```

In Lab 17, Button 1 changes the pen color and Button 2 lifts the pen. In the demo, both buttons change modes, so the sketch leaves them alone. The setting `"auto_color": True` moves the pen to the next color with every step instead. Your line comes out in rainbow stripes, and a hard shake still erases it.

### When the tilt sensor stops answering

The tilt sensor talks to the Pico over the wires on GP16 and GP17. If one of its four wires loses contact, even for a moment, a reading fails. Python then raises an `OSError`. That is an **error** that means a piece of hardware did not answer.

Here is how `kit.py` reads the sensor:

```python title="kit.py (lines 254 to 261)"
--8<-- "src/kits/8x8-matrix-accel/kit.py:254:261"
```

`try` means "try these lines." `except OSError` means "if the sensor did not answer, do this instead." Then `read_tilt` hands back `last_tilt`, the last good reading, and the show keeps going. The function `sensor_lost` prints one message in the Shell:

```text
The tilt sensor is not answering. Check its wires: GP16, GP17, 3V3 and GND.
```

On the next reading, `kit.py` tries to turn the sensor on again. When it answers, the Shell says `The tilt sensor is answering again.` If you see the first message, press each of the sensor's four wires in firmly.

Once a second, `check_sensor` also makes sure the sensor kept its settings. A dip in the power can reset the sensor. A reset sensor goes to sleep and keeps sending the same reading, so tilting seems to do nothing. When that happens, the Shell says `The tilt sensor lost its settings. Turning it on again.`

The small LED on the Pico board blinks while the program runs. If it stops blinking, the program has stopped.

### Make the kit start by itself

When the Pico gets power, MicroPython looks for a file named `main.py`. If it finds one, it runs it right away, with no computer and no Thonny. That is why this program is a **template**: a starting file that you copy and save under a new name.

Follow these steps in Thonny:

1. Open `19-template-main.py`.
2. Choose **File > Save as**, then pick **Raspberry Pi Pico**.
3. Type the name `main.py` and click **OK**.
4. Unplug the kit from your computer.
5. Plug it into a USB wall charger, like a phone charger.

In a moment you should see a **1** on the matrix, then the red fill. The demo is running all by itself!

The brightest mode, Fill colors, draws about 300 mA, so any phone charger has plenty of power.

!!! warning "Power banks that switch themselves off"
    Many power banks turn themselves off when a device draws only a little **current** (the flow of electricity). They do this on purpose. When a phone is full, it stops drawing current, and the power bank switches off to save its battery.

    This kit often draws only a little current. In modes like Walk the pixels or Tilt one dot, only a few dim pixels are lit. The power bank decides nothing is plugged in, so after a short time it switches off and the matrix goes dark.

    - Use a USB wall charger instead. It stays on however little power the kit uses.
    - Some power banks have a low-current mode, made for earbuds and watches. Check its instructions to learn how to turn that mode on.
    - Press the power bank's button to turn it back on. The demo starts over at mode 1.

Plug the kit back into your computer, and the demo keeps running. Click Thonny's red **Stop** button to stop it. To turn off the self-start, rename `main.py`. Type this line into the Shell and press **Enter**:

```python
import os; os.rename("main.py", "main-off.py")
```

Now the Pico finds no `main.py` the next time it starts, so it waits for Thonny again.

## Try it yourself

1. Visit all 18 modes with Button 1. Then press Button 2 on mode 1. Which mode comes up? Why?
2. Make a short demo of your five favorite modes. Remove the other items from `MODES`. An item is the line with its name, plus the settings line under it if it has one. How many modes does Button 1 step through now?
3. Put your name in lights. In mode 6, change `"MOVING RAINBOW!"` to your own words. Use capital letters.
4. Change `MODE_NUMBER_MS = 700` to `MODE_NUMBER_MS = 2000`. What changes when you switch modes?
5. Save your favorite version as `main.py` and power the kit from a wall charger. Show it to a friend, and hand them the printed [Demo Mode Guide](demo-mode-guide.pdf).

## Check your understanding

1. Why can't the demo load `05-fill-colors.py` as a mode the way it is?
2. What does `kit.wait()` do that `sleep()` does not?
3. What does the Pico do when it powers up and finds a file named `main.py`?
4. Why does the pen in mode 18 change color by itself?
5. What happens in a tilt mode if the sensor misses one reading?

!!! success "Kit complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You turned 18 programs into one show that starts by itself! Print the guide, set out your kit,
    and let your friends press the buttons. You are a real light-maker now.

**What's next:** Share your demo at a club night or science fair, or head to the [Hands on Labs](../../labs/index.md) to learn more patterns for LED strips.
