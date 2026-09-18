# Lab 48: Pixel Demo

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    This is the big finale! One program, twelve light patterns, and two buttons to pick between them. See how many patterns you already know. Let's light this up!

**Program file:** [`48-pixel-demo.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/48-pixel-demo.py)

## What you'll learn

- How one program holds twelve patterns, using a `mode` number and an `if` / `elif` chain
- How one number, `BASE_DELAY`, sets the speed of the patterns
- Which lab taught each pattern
- How to make the demo start by itself when you plug in power

## What you'll need

- Your base kit, including both push buttons wired as shown in [The Two Buttons](../kits/moving-rainbow-base/index.md#the-two-buttons). Each button reads `0` while you press it.
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- Recommended: [Lab 31: Button Modes](31-modes.md). Lab 48 is nearly the same program, and Lab 31 explains each pattern in detail.
- Recommended: [Lab 34: Two Buttons](34-two-button-print.md) and [Lab 47: Buttons Move a Light](47-buttons-move-light.md). They teach the interrupt and debounce pattern behind the buttons.

## The program

This program runs twelve light patterns. Button 1 moves to the next pattern, and Button 2 moves back to the previous one.

??? example "Full program: 48-pixel-demo.py (233 lines)"
    ```python title="48-pixel-demo.py"
    --8<-- "src/kits/moving-rainbow-base/48-pixel-demo.py"
    ```

Run it. A short rainbow slides along the strip. Press Button 1 and a red dot runs along the strip instead. Each press of Button 1 moves to the next pattern, and each press of Button 2 moves back. The Shell prints the name of the pattern every time it changes.

!!! warning "Power check"
    Three patterns can light all 30 pixels at once. Rainbow cycle and random dots use color-wheel colors, so a full strip draws about 600 mA. Candle flicker fills the strip with warm colors and draws about 660 mA. A USB port supplies about 500 mA (see [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go)). To stay safe, divide the color numbers by 4. In `wheel()`, change each returned number to a form like `(pos * 3) // 4` or `(255 - pos * 3) // 4`. That cuts rainbow cycle and random dots to about 150 mA. In `candle()`, use `12 + randint(0,38)` for `green` and `green + randint(0,12)` for `red`. That cuts candle flicker to about 160 mA.

## How it works

### One number picks the pattern

A list of names matches each mode number to a pattern.

```python
mode_list = ['moving rainbow', 'moving red dot', 'moving green dot', 'moving blue dot',
             'red comet', 'green comet', 'blue comet', 'candle flicker', 'random dots', 'bounce',
             'running lights', 'rainbow cycle']
mode_count = len(mode_list)
```

Mode 0 is the first name, `'moving rainbow'`. Mode 11 is the last name, `'rainbow cycle'`. Because `mode_count` is `len(mode_list)`, it stays right if you add names.

The main loop runs forever. It prints the pattern name when the mode changes. Then it runs the function for the current mode.

```python
while True:
    # print only on change
    if mode != last_mode:
        print('mode=', mode, 'running program', mode_list[mode])
        last_mode = mode
    if mode == 0:
        moving_rainbow(counter, bd)
```

The full loop has one `if` or `elif` branch for each mode, 0 through 11. A program that is in exactly one mode at a time, and that moves to another mode when something happens, is called a **state machine**. The [State Machine Diagram](../sims/state-machine-diagram/index.md) shows the idea as a picture.

At the bottom of the loop, `counter` steps forward and starts over at 0 after pixel 29.

```python
    counter += 1
    # wrap the counter using modulo
    counter = counter % NUMBER_PIXELS
```

Most patterns use `counter` as the pixel where the action happens.

### The buttons change the mode

The handler uses the same interrupt and debounce pattern as Labs 34 and 47. It ignores any press that comes less than 200 milliseconds after the last one.

```python
        if pin == button1:
            mode +=1
        else:
            mode -=1
        # wrap around if we get too high
        mode = mode % mode_count
```

Button 1 adds 1 to `mode`, and Button 2 subtracts 1. The `% mode_count` wraps the number around. Button 1 at mode 11 goes to mode 0, and Button 2 at mode 0 goes to mode 11. The new pattern starts when the old pattern finishes its current step.

### What is different from Lab 31

Lab 48 is nearly the same program as [Lab 31: Button Modes](31-modes.md). There are two changes.

**First, the starting mode.** Lab 31 starts at mode 11, the rainbow cycle. Lab 48 starts here, at mode 0, the moving rainbow.

```python
mode = 0
```

**Second, the speeds.** Lab 31 types a fixed delay into each pattern. Lab 48 builds most delays from one number.

```python
BASE_DELAY = 0.005
```

Three short names come from that number. Here `bd` stands for "base delay".

```python
bd = BASE_DELAY
bd2 = bd*2
bd5 = bd*5
```

So `bd` is 0.005 seconds, `bd2` is 0.01 seconds, and `bd5` is 0.025 seconds. Most branches of the loop pick one of them.

```python
    elif mode == 1:
        move_dot(counter, red, bd2)
```

This table compares the waits in the two labs. The waits in Lab 48 are shorter, so most patterns run faster.

| Pattern | Lab 31 wait | Lab 48 wait |
|---------|:-----------:|:-----------:|
| Moving rainbow | 0.05 | `bd` = 0.005 |
| Moving dots | 0.05 | `bd2` = 0.01 |
| Comets | 0.01 | `bd` = 0.005 |
| Candle flicker | 0.01 | `bd` = 0.005 |
| Random dots | 0.01 | `bd` = 0.005 |
| Bounce | 0.15 | `bd5` = 0.025 |
| Running lights | 0.2 | 0.2 (a fixed number) |
| Rainbow cycle | 0.05 | `bd` = 0.005 |

Change `BASE_DELAY` once, and every pattern that uses `bd`, `bd2`, or `bd5` changes speed. Running lights keeps its fixed 0.2.

### Where each pattern came from

You have already met almost every pattern in this demo. This table shows where to find each one.

| Mode | Pattern | Function | Learn it in |
|:----:|---------|----------|-------------|
| 0 | Moving rainbow | `moving_rainbow` | [Lab 13](13-moving-rainbow.md) |
| 1, 2, 3 | Moving red, green, and blue dot | `move_dot` | [Lab 05](05-move.md) |
| 4, 5, 6 | Red, green, and blue comet | `comet_tail` | [Lab 16](16-comet.md) |
| 7 | Candle flicker | `candle` | [Lab 18](18-candle-flicker.md) |
| 8 | Random dots (color-wheel colors at random pixels) | `random_color` | [Lab 10](10-random-colors.md) |
| 9 | Bounce (two dots race in from the ends, meet in the middle, and bounce back out) | `bounce` | New here. Labs [25](29-larson-scanner.md) and [26](30-random-bounce.md) have related back-and-forth ideas. |
| 10 | Running lights (every fourth pixel is lit, and the pattern steps along) | `running_lights` | The idea of [Lab 19](19-theater-chase.md) |
| 11 | Rainbow cycle | `rainbow_cycle` | [Lab 12](12-rainbow-cycle.md) |

The moving rainbow, random dots, and rainbow cycle all use the `wheel()` function from [Lab 09](09-color-wheel.md).

!!! bug "Known issue"
    Changing the mode does not clear the strip, and candle flicker and random dots only add pixels. Old pixels can stay lit and slowly fill the strip. The `erase()` function is in the file but nothing calls it; `main-demo-cycle.py` calls it on every mode change.

## Run it without a computer

When the Pico gets power, MicroPython looks for a file named `main.py` and runs it. To make the demo start by itself, save a copy on your Pico under that name.

1. Open `48-pixel-demo.py` in Thonny.
2. Choose **File**, then **Save as**, and pick **Raspberry Pi Pico**.
3. Type the name `main.py` and save.
4. Make sure `config.py` is also on the Pico, because the demo imports it.

Now unplug the USB cable from your computer and plug the kit into a USB phone charger or a battery pack. The light show starts on its own. To edit the program again, read [Running Without a Computer](../kits/moving-rainbow-base/index.md#running-without-a-computer) first.

## More demo programs

The kit folder also holds demo programs that are not numbered labs. They are handy for a science fair or a classroom open house. Open them in Thonny and compare them with Lab 48.

| File | What it does |
|------|--------------|
| [`auto-cycle.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/auto-cycle.py) | Steps through sixteen light patterns automatically, repeating each one a few times before moving on. It adds bounce in three colors and running lights in three colors. |
| [`main-demo-cycle.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/main-demo-cycle.py) | Mode 0 cycles through all twelve patterns, five seconds each. Modes 1 to 12 each repeat one pattern. The buttons change the mode, and the strip is cleared on each change. |
| [`main-old.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/main-old.py) | An older version of the demo. Each pattern runs for one pass along the strip, and then the next one starts. The buttons also change the pattern. It has one extra pattern, a Cylon scanner like Lab 29. |

## Try it yourself

1. Slow the whole show down. Change `BASE_DELAY = 0.005` to `BASE_DELAY = 0.02`. Which pattern keeps its old speed, and why?
2. Add a pattern of your own. This is a great capstone project. First, add a new name to the end of `mode_list`.

```python title="Your change"
mode_list = ['moving rainbow', 'moving red dot', 'moving green dot', 'moving blue dot',
             'red comet', 'green comet', 'blue comet', 'candle flicker', 'random dots', 'bounce',
             'running lights', 'rainbow cycle', 'violet dot']
```

Then add a branch for mode 12. In the real file, the new `elif` goes right after `elif mode == 11:` and above the last `else:`.

```python title="Your change"
if mode == 11:
    rainbow_cycle(counter, bd)
elif mode == 12:
    move_dot(counter, violet, bd2)
```

Run it and press Button 1 until you reach mode 12. Then swap in your own colors, or write a brand-new pattern function.

## Check your understanding

1. What does Button 2 do when the demo is in mode 0? Why?
2. Which line sets the starting mode, and which pattern does it start with?
3. What is `bd2`, and how many seconds does it wait?
4. Which pattern keeps its speed when you change `BASE_DELAY`? Why?
5. Which two files must be on your Pico for the demo to start by itself?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You made it to the end of the labs! You know how every pattern in this demo works, and you can add your own. Now go build something that is all yours.

**What's next:** Return to the [labs list](index.md), or build your own capstone by adding a pattern to the mode list.
