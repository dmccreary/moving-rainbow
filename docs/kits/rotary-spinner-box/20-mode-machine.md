# Lab 12: The Mode Machine

This is the big one. This program puts the whole box to work at once — the
strip, the knob, and both buttons. It can show five different light shows, and
you pick which one with the buttons. The knob then changes that show. This is
the file `20-mode-machine.py`.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    You've built every piece of this already — the dot, the scanner, the comet,
    the rainbow. Now we wire them all into one program that can wear many hats.
    A program that can be in one mode at a time is called a **state machine**,
    and it's how real apps work. Let's light this up!

## What You'll Learn

By the end of this lab, you'll be able to:

- Explain what a **state machine** is and how it switches between modes
- Use buttons to move from one mode to the next and back
- Use a **list** to remember a setting for each mode
- Use a **timer** instead of `sleep()` so the knob stays responsive
- Explain what an **interrupt** does

## What You'll Need

- Your Rotary Spinner Box with everything wired up
- The 12-pixel LED strip on pin 0
- The rotary knob (encoder) on pins 12 and 13
- Both push buttons on pins 14 and 15
- A USB cable and the Thonny program open

You'll use the whole box for this lab.

## What Is a State Machine?

A **state machine** is a program that can be in one of several **states**, or
**modes**, at a time. It does only one thing in each mode. A press of a button
moves it to a different mode. Think of a TV remote — the same buttons do
different things depending on the menu you're in.

Our mode machine has five modes. The buttons move between them. The knob
changes the look of whichever mode is showing.

| Mode | Name | What the knob does |
|------|------|--------------------|
| 0 | Knob Dot | Moves one bright pixel along the strip |
| 1 | Solid Color | Changes the color of the whole strip |
| 2 | Scanner | Changes how fast the dot bounces |
| 3 | Comet | Changes the length of the fading tail |
| 4 | Moving Rainbow | Changes how fast the rainbow scrolls |

When the box powers up, it starts in **Mode 0 (Knob Dot)**. That is the
**default** — the mode you get before you press anything.

## The List of Modes

The program keeps the mode names in a **list** (an ordered group of values). It
also keeps a variable named `mode` that says which one is showing right now.

```python
MODE_NAMES = ['Knob Dot', 'Solid Color', 'Scanner', 'Comet', 'Moving Rainbow']
NUM_MODES = len(MODE_NAMES)

mode = 0          # which mode is showing now (0 = Knob Dot, the default)
```

`mode` starts at `0`, so the box always wakes up in Knob Dot mode.

## One Setting for Each Mode

Each mode needs to remember its own setting. The Solid Color mode needs a
color. The Comet mode needs a tail length. The program holds all of these in
one list named `params` (short for **parameters**, the values that shape a
pattern).

```python
# Each mode stores one parameter value in this list
#         Knob pos, Solid hue, Scanner speed, Comet tail, Rainbow speed
params = [N // 2,   0,         10,            5,          10]
```

Position `0` in the list belongs to mode `0`, position `1` to mode `1`, and so
on. Because each mode has its own slot, a mode looks the way you left it when
you come back to it.

!!! info "Pixel thinks..."
    <img src="../../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    Here's the clever trick: `params[mode]` always points to the setting for the
    mode you're in. When the mode changes, that one little word `mode` changes
    too — so the knob automatically starts steering the right value. One list,
    five memories!

## The Buttons Switch Modes

Button 1 (pin 14) moves to the **next** mode. Button 2 (pin 15) moves to the
**previous** mode. The math uses `% NUM_MODES` so the modes wrap in a circle —
after the last mode you land back on the first.

```python
def button_callback(pin):
    global mode, mode_changed, last_button_time
    new_time = utime.ticks_ms()
    if utime.ticks_diff(new_time, last_button_time) > 200:
        if pin is button_next:
            mode = (mode + 1) % NUM_MODES   # next mode
        else:
            mode = (mode - 1) % NUM_MODES   # previous mode
        mode_changed = True
        last_button_time = new_time
```

Press a button and the strip changes to a new light show right away.

This function is called an **interrupt** handler. An **interrupt** is a way for
the chip to stop what it's doing the instant a button is pressed and run this
code. The program does not have to keep asking "is the button down yet?" The
press interrupts the program for you, so it never gets missed.

```python
button_next.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)
button_prev.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)
```

The `.irq(...)` line tells the chip to run `button_callback` whenever that
button is pressed.

## The Knob Changes the Current Mode

Every time through the main loop, the program reads the knob. If you turned it,
the program changes `params[mode]` — the setting for the mode you're in.

```python
turn = read_knob()
if turn != 0:
    new_value = params[mode] + turn * PARAM_STEP[mode]
    if mode == 1:
        # Solid Color: the hue wraps around the color wheel
        params[mode] = new_value % 256
    else:
        # every other parameter stops at its limits instead of wrapping
        if new_value < PARAM_MIN[mode]:
            new_value = PARAM_MIN[mode]
        if new_value > PARAM_MAX[mode]:
            new_value = PARAM_MAX[mode]
        params[mode] = new_value
    draw(step)   # show the change right away
```

Turn the knob and the current mode's setting changes — the dot moves, the color
shifts, or the pattern speeds up — depending on the mode you're in.

## Drawing the Right Mode

A function named `draw` looks at `mode` and paints the matching pattern. This
choosing of one path out of many is called **dispatch**.

```python
def draw(step):
    if mode == 0:
        # Knob Dot: the knob moves a single bright pixel
        for i in range(N):
            strip[i] = (0, 0, 0)
        strip[params[0]] = (0, 90, 110)
    elif mode == 1:
        # Solid Color: the whole strip is one color from the wheel
        color = color_wheel(params[1])
        for i in range(N):
            strip[i] = color
    elif mode == 2:
        # Scanner: one bright dot bounces back and forth
        position, _ = bounce(step)
        ...
    strip.write()
```

The `if` and `elif` lines pick exactly one pattern to draw, based on the value
of `mode`.

Your strip is a **straight** 12-pixel strip, not a ring. So the Scanner and
Comet do not wrap around. They **bounce** off the two ends and travel back, like
a ball in a hallway. A helper named `bounce` does that math.

## A Timer Instead of Sleep

In earlier labs, `sleep()` paused the whole program between animation frames.
That works, but while the program sleeps, it can't read the knob. The knob would
feel frozen.

This program uses a **timer** instead. It checks the clock with `ticks_ms` (the
number of milliseconds since the chip started) and only advances the animation
when enough time has passed.

```python
now = utime.ticks_ms()
if utime.ticks_diff(now, last_frame) >= frame_delay():
    step += 1
    draw(step)
    last_frame = now
```

The animation still moves at a steady pace, but the loop never stops. The knob
stays smooth and responsive the whole time.

!!! tip "Pixel's tip"
    <img src="../../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel shares an idea">
    `ticks_diff` is the right way to compare two times on the Pico. It handles
    the moment when the clock rolls over and starts counting from zero again.
    Reach for `ticks_diff` any time you want to know "has enough time gone by?"

## Try It Yourself

1. **Add your favorite color.** In the `draw` function, find the Knob Dot line
   `strip[params[0]] = (0, 90, 110)`. Change those three numbers to a color you
   like, then run the program and turn the knob in Mode 0.

2. **Slow the rainbow's top speed.** In `frame_delay`, the Rainbow uses
   `130 - params[4] * 5`. Change the `5` to `3` so each knob click adds less
   speed. Does the rainbow feel easier to fine-tune?

3. **Make a longer comet.** The Comet tail can grow up to `N - 1` pixels. Switch
   to Mode 3 and turn the knob all the way up. How long can the tail get on a
   12-pixel strip?

## Check Your Understanding

1. What is a state machine, and what are its "states" in this program?
2. Which button moves to the next mode, and which moves to the previous one?
3. How does the list named `params` remember a setting for each mode?
4. What does an interrupt do when you press a button?
5. Why does this program use a `ticks_ms` timer instead of `sleep()`?

!!! success "Chapter complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You built a real state machine! Five light shows, two buttons, one knob, and
    a list that remembers them all. This is the same pattern that powers menus,
    game screens, and apps everywhere. You're already glowing — and now your
    whole box glows with you!

## What's Next

In [Lab 13: The Capability Demo](21-demo.md), you'll watch your box show off
everything it can do, all on its own.
