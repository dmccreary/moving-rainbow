# Lab 31: Button Modes

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Twelve light shows live inside this one program, and your two buttons are the remote control. This is the showcase lab of the kit. Let's light this up!

**Program file:** [`31-modes.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/31-modes.py)

## What you'll learn

- What a **state machine** is, and how the `mode` variable acts as its state
- How a button **interrupt** changes the mode while the strip keeps moving
- How **debouncing** stops one press from counting many times
- How `%` (modulo) wraps a number around so the modes form a circle
- How an `if`/`elif` chain picks which pattern to run

## What you'll need

- Your base kit: a Pico, a breadboard, the 30-pixel LED strip, and two push buttons. Wire the buttons as shown in [The Two Buttons](../kits/moving-rainbow-base/index.md#the-two-buttons): Button 1 on `GP15` and Button 2 on `GP14`.
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico, with the Shell window showing

**This is a showcase lab.** It uses buttons, interrupts, and a mode variable. Labs 32 to 37 teach those ideas in small steps. You can run this lab first, to see where the kit is heading.

These small steps are good ones to read next:

- [Lab 34: Two Buttons](34-two-button-print.md)
- [Lab 36: Button Change Speed](36-button-change-speed.md)
- [Lab 37: Modes Auto Cycle](37-modes-auto-cycle.md)

## The program

This program holds twelve light patterns. Button 1 moves to the next pattern, and Button 2 moves back.

??? example "Full program: 31-modes.py (226 lines)"
    ```python title="31-modes.py"
    --8<-- "src/kits/moving-rainbow-base/31-modes.py"
    ```

Run it. The strip starts with the rainbow cycle, where a rainbow slides around the strip. Press Button 1 or Button 2 to change patterns, and watch the Shell for the name of each new mode.

!!! warning "Power check"
    The program starts in rainbow cycle mode, which lights all 30 pixels. Each pixel's three numbers add up to 255, or about 20 mA, so the strip draws about 600 mA. A USB port supplies about 500 mA (see [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go)). Divide the color numbers by 4 to reach about 150 mA, as Challenge 1 shows.

## The twelve modes

| Mode | Name | What you see |
|------|------|--------------|
| 0 | moving rainbow | A short rainbow band moves along the strip |
| 1 | moving red dot | One red dot moves along the strip |
| 2 | moving green dot | One green dot moves along the strip |
| 3 | moving blue dot | One blue dot moves along the strip |
| 4 | red comet | A bright red head with a fading tail moves along the strip |
| 5 | green comet | The same comet, in green |
| 6 | blue comet | The same comet, in blue |
| 7 | candle flicker | Random pixels flicker in warm orange and yellow |
| 8 | random dots | Random pixels light up in random colors |
| 9 | bounce | Two red dots start at the ends, meet in the middle, and move back out |
| 10 | running lights | Every fourth pixel is blue, and the pattern slides along the strip |
| 11 | rainbow cycle | The whole rainbow slides around the strip (the starting mode) |

## How it works

### One number picks the pattern

A **state machine** is a program that is in exactly one **state** at a time. An **event** moves it from one state to another. In this program, the state is the number in `mode`, and the event is a button press.

See the idea in the [State Machine Diagram](../sims/state-machine-diagram/index.md) MicroSim. It has three modes, and this program has twelve. [Chapter 18](../chapters/18-input-devices-and-sensors/index.md) explains state machines in more depth.

### Name the modes

```python
mode_list = ['moving rainbow', 'moving red dot', 'moving green dot', 'moving blue dot',
             'red comet', 'green comet', 'blue comet', 'candle flicker', 'random dots', 'bounce',
             'running lights', 'rainbow cycle']
mode_count = len(mode_list)
```

The list `mode_list` holds the name of each mode. Lists count from 0, so `mode_list[0]` is `'moving rainbow'` and `mode_list[11]` is `'rainbow cycle'`. The `len()` function counts the items in a list, so `mode_count` is 12.

The names are for the Shell. The strip only cares about the number.

### Start in mode 11

```python
mode = 11
counter = 0
last_mode = 1
```

The program starts in mode 11, the rainbow cycle. The variable `counter` starts at 0. The variable `last_mode` is used later to print the mode name only when it changes.

### Pick a pattern

```python
if mode == 0:
    moving_rainbow(counter, .05)
elif mode == 1:
    move_dot(counter, red, .05)
elif mode == 2:
    move_dot(counter, green, .05)
...
```

This **`if`/`elif` chain** checks the mode numbers one at a time and runs the first pattern that matches. It sits inside a `while True:` loop, so the program picks a pattern again on every pass.

Each pattern is a **function** (a named block of code) that draws one step of its show. The last number in each call is the delay, the seconds to wait after that step.

### Count the steps

```python
counter += 1
# wrap the counter using modulo
counter = counter % NUMBER_PIXELS
```

Each pass through the loop adds 1 to `counter`. The `%` sign is the **modulo** operator, which gives the remainder after dividing. When `counter` reaches 30, `30 % 30` is 0, so it wraps back to the start. That means `counter` counts 0 to 29 and around again.

Most patterns use `counter` as a position on the strip. Try the [Modulo Wrap-Around](../sims/modulo-wrap-simulation/index.md) MicroSim to watch a counter wrap.

### One pattern up close

```python
def move_dot(counter, color, delay):
    strip[counter] = color
    strip.write()
    sleep(delay)
    strip[counter] = (0,0,0)
```

The `move_dot()` function lights the pixel at `counter`, writes it, and waits. Then it turns that pixel off in memory. The next `strip.write()` shows the change. Because `counter` grows by 1 on every pass, the dot moves along the strip.

### Buttons and interrupts

```python
button1.irq(trigger=Pin.IRQ_FALLING, handler = button_pressed_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler = button_pressed_handler)
```

The main loop does not keep asking whether a button was pressed. Instead, each button gets an **interrupt**. An interrupt is a signal that pauses the Pico. The Pico runs one small function right away, and then goes back to its work.

The `handler` is the function to run. Here, both buttons share `button_pressed_handler`. The `trigger` says when to run it.

Your buttons read 1 when released and 0 when pressed. **Falling** means the value drops from 1 to 0, which is the moment of the press.

### Which button, and is it a new press?

```python
def button_pressed_handler(pin):
    global mode, last_time
    new_time = ticks_ms()
    if (new_time - last_time) > 200:
        ...
        last_time = new_time
```

The Pico passes the handler the `pin` that caused the interrupt. The `global` line lets the function change `mode` and `last_time`, which live outside it.

The `ticks_ms()` function gives the milliseconds since the Pico started.

A real button flutters for a few thousandths of a second when you press it. That can look like many presses. **Debouncing** means ignoring the flutter. The handler acts only if more than 200 milliseconds (0.2 seconds) have passed since the last press.

```python
if pin == button1:
    mode +=1
else:
    mode -=1
# wrap around if we get too high
mode = mode % mode_count
```

This code runs at the spot marked `...` in the 200 millisecond `if`. Button 1 adds 1 to `mode`, and Button 2 subtracts 1. Then `mode % mode_count` keeps the number between 0 and 11.

Try two examples. In mode 11, Button 1 makes 12, and `12 % 12` is 0. In mode 0, Button 2 makes -1, and `-1 % 12` is 11. So the modes form a circle.

### Print only when the mode changes

```python
# print only on change
if mode != last_mode:
    print('mode=', mode, 'running program', mode_list[mode])
    last_mode = mode
```

The `!=` sign means "is not equal to". The Shell prints a line only when `mode` differs from `last_mode`. Then `last_mode` catches up. Without this check, the Shell would print a line on every pass through the loop.

A button press can arrive at any moment, even in the middle of a pattern. The pattern finishes its current step, and the next pass of the loop uses the new mode.

### Changing modes

```python
# erase the entire strip
def erase():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,0)
        strip.write()
```

This function turns off every pixel. But no line in the program calls `erase()`.

!!! bug "Known issue"
    The strip is not cleared when the mode changes, because no line calls `erase()`. Pixels from one pattern can stay lit under the next one. The "candle flicker" and "random dots" modes only add light, so they slowly fill the strip.

## Try it yourself

### Challenge 1: Make the rainbow safe

In `rainbow_cycle()`, divide each color number by 4 right after `color = wheel(color_index)`. The `//` sign divides and drops the remainder, so each number stays whole.

```python title="Your change"
def rainbow_cycle(counter, wait):
    for i in range(0, NUMBER_PIXELS):
        color_index = round(i*PERCENT_COLOR_WHEEL)
        color = wheel(color_index)
        color = (color[0] // 4, color[1] // 4, color[2] // 4)
        strip[(i + counter) % NUMBER_PIXELS] = color
        strip.write()
    sleep(wait)
```

Run it. The rainbow is dimmer, and the strip draws about 150 mA.

### Challenge 2: Clear the strip when the mode changes

Call `erase()` inside the `if mode != last_mode:` block in the main loop.

```python title="Your change"
while True:
    if mode != last_mode:
        print('mode=', mode, 'running program', mode_list[mode])
        erase()
        last_mode = mode
```

To test it, press Button 2 four times to reach "candle flicker" (mode 7). Wait until the strip fills. Then press Button 1 to reach "random dots". Does the old glow disappear before the new dots appear?

## Check your understanding

1. In this program, what is the state? What event changes it?
2. Which mode does the program start in, and what do you see first?
3. Button 1 is pressed in mode 11. Which mode comes next, and why?
4. Why does the handler ignore a press that comes less than 200 milliseconds after the last one?
5. Why does the main loop not need to check the buttons?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You explored a real state machine! One number, two buttons, and a chain of patterns turned your strip into a light-show remote control.

**What's next:** In [Lab 32: Button Test](32-button-test.md), you begin the small steps toward the buttons used here.
