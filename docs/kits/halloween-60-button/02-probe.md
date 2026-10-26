# Lab 2: Hardware Probe

A **probe** is a test program. It does not make a light show. It checks each part of your costume and prints a report that ends with `TEST PASS` or `TEST FAIL`.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Before we add the spooky stuff, let's check that every part is awake. Every bug is just a puzzle in disguise, and this program finds the puzzles for us!

**Program file:** [`02-probe.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/02-probe.py)

## What You'll Learn

- What a probe program is and why it saves time
- How to read `TEST PASS` and `TEST FAIL`
- What a pin level of 1 or 0 means
- How much **current** (the flow of electricity) 60 pixels can use

## What You'll Need

- Your costume wired as shown on the [kit page](index.md#how-the-parts-connect)
- `config.py` saved on the Pico
- Thonny open, or the `run-probe.sh` script on a Mac

## The Program

This program checks `config.py`, the button pin and the strip, then waits for you to press the button.

```python
--8<-- "src/kits/halloween-60-button/02-probe.py"
```

The first, middle and last pixels light red, green and blue. Press the button when the report asks, and the whole strip flashes orange.

You can also run the probe from a Mac terminal. Close Thonny first, then run:

```bash
./run-probe.sh
```

The end of a good report looks like this:

```text
Button press check
==================================================
Press the button now (you have 10 seconds)...
Button press seen after 2.3 seconds.

TEST PASS - config.py, the button and the strip pins look right
```

## How It Works

The probe turns on the Pico's **pull-up resistor** for each pin. A pull-up holds a pin at 1 when nothing is touching it. If a pin reads 0 when nobody is pressing anything, a wire is touching ground by mistake.

It also does some math. Each pixel has a red, green and blue LED. Each one can use about 20 milliamps (mA). That is 60 x 3 x 20 = 3,600 mA at full brightness! With `BRIGHTNESS = 0.25`, the most is about 900 mA. A USB battery pack can handle that.

The probe cannot see the strip. You are its eyes! Check that pixels 0, 30 and 59 light up.

## Try It Yourself

1. Change `BRIGHTNESS` in `config.py` to `0.5` and run the probe. What does it say?
2. Unplug the button wire and run the probe. Which line changes?

## Check Your Understanding

1. What does a pull-up resistor do?
2. Why do we keep `BRIGHTNESS` low on battery power?
3. If no pixels light up, what is the first thing to check?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 3: Blink the First Pixel](03-blink-first-pixel.md).
