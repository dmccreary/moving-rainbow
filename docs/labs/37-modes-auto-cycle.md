# Lab 37: Modes Auto Cycle

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    This one has no buttons, but it holds the secret of every multi-pattern light show. One number decides which pattern is on. Let's teach the program to change that number by itself!

**Program file:** [`37-modes-auto-cycle.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/37-modes-auto-cycle.py)

## What you'll learn

- What a mode is, and how a mode variable remembers it
- How `run_mode()` uses `if`, `elif`, and `else` to pick a pattern
- How to switch on a timer with `ticks_ms()` instead of `sleep(4)`
- How `% NUM_MODES` wraps the mode back to the start

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

This lab needs no buttons.

## The program

This program fills the whole strip with one color for four seconds, then switches to the next color: red, green, blue, and around again.

```python title="37-modes-auto-cycle.py"
--8<-- "src/kits/moving-rainbow-base/37-modes-auto-cycle.py"
```

Run it. The strip glows red. About four seconds later it turns green, then blue, then red again. The Shell prints the new mode number at each switch. The loop repeats forever, so press the **Stop** button in Thonny when you are done.

## How it works

### One number picks the pattern

A **mode** is one way the strip can behave. A **mode variable** is a number that remembers which mode is on right now.

```python
mode = 0
run_mode(mode)
mode_start_time = ticks_ms()
```

Here mode 0 means solid red, mode 1 means solid green, and mode 2 means solid blue. The program starts in mode 0, shows it, and notes the time on the clock.

In [Lab 31: Button Modes](31-modes.md), buttons change the mode number instead of a timer. That lab has twelve modes. This lab practices the same idea with three. The [State Machine for a 3-Mode LED Controller](../sims/state-machine-diagram/index.md) MicroSim draws the three modes as boxes with arrows between them. Here, the clock is what moves along an arrow.

### Run the mode

The `run_mode()` function looks at the mode number and lights the matching color.

```python
def run_mode(mode):
    if mode == 0:
        fill_strip((200, 0, 0))    # mode 0: solid red
    elif mode == 1:
        fill_strip((0, 200, 0))    # mode 1: solid green
    else:
        fill_strip((0, 0, 200))    # mode 2: solid blue
```

The `elif` word means "else if". Python checks the tests in order and runs the first one that is true. If `mode` is not `0` and not `1`, the `else` part runs, so mode 2 lights blue.

The `fill_strip()` helper works as in [Lab 35](35-button-change-color.md).

```python
def fill_strip(color):
    for i in range(NUMBER_PIXELS):
        strip[i] = color
    strip.write()
```

Each color uses 200 on one channel, and the other two channels are 0. With all 30 pixels lit, that is about 471 mA, which is under the 500 mA that a USB port supplies. See [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go)

### Check the clock

Now the main loop decides when it is time to switch.

```python
while True:
    elapsed_seconds = (ticks_ms() - mode_start_time) / 1000

    if elapsed_seconds >= SECONDS_PER_MODE:
        mode = (mode + 1) % NUM_MODES   # advance to the next mode, then wrap
        run_mode(mode)
        mode_start_time = ticks_ms()
        print("mode:", mode)

    sleep(0.1)
```

The call `ticks_ms()` reads a clock that counts **milliseconds** (thousandths of a second). Subtracting `mode_start_time` gives the time since the mode began. Dividing by `1000` turns milliseconds into seconds.

When `elapsed_seconds` reaches `SECONDS_PER_MODE` (4), it is time to switch. The mode goes up by one. The `% NUM_MODES` part wraps it: 2 + 1 is 3, and 3 % 3 is 0, so blue is followed by red.

Then `mode_start_time = ticks_ms()` restarts the stopwatch. Every mode gets its own full four seconds, no matter when the last switch happened.

### Why check the clock instead of sleeping?

One way to wait four seconds is `sleep(4)`. But while the Pico sleeps, it does nothing else for four whole seconds.

This loop naps for only a tenth of a second (`sleep(0.1)`), then wakes up and checks the clock. It wakes ten times every second. That keeps the loop responsive, so you could add other work inside it, such as checking a button.

Because the check happens every 0.1 seconds, each mode lasts about four seconds, plus up to a tenth of a second.

## Try it yourself

1. Change `SECONDS_PER_MODE = 4` to `SECONDS_PER_MODE = 1`. Watch the faster show.
2. Add a fourth mode. Change `NUM_MODES = 3` to `NUM_MODES = 4`. Then replace `run_mode()` with this version, which adds a dim cyan (green plus blue):

```python title="Your change"
def run_mode(mode):
    if mode == 0:
        fill_strip((200, 0, 0))    # mode 0: solid red
    elif mode == 1:
        fill_strip((0, 200, 0))    # mode 1: solid green
    elif mode == 2:
        fill_strip((0, 0, 200))    # mode 2: solid blue
    else:
        fill_strip((0, 64, 64))    # mode 3: dim cyan
```

## Check your understanding

1. What does the mode variable store?
2. What does `run_mode()` do with the number it receives?
3. How does the program know that four seconds have passed?
4. Why does the program reset `mode_start_time` after each switch?
5. You add a fourth mode but leave `NUM_MODES = 3`. What happens?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    Your program now switches modes on its own! One number, one clock, and one wrap-around were all it took.

**What's next:** In [Lab 38: Traffic Light](38-traffic-light.md), three pixels act like a traffic light, and each color stays on for a different amount of time.
