# Lab 9: Knob Brightness

In this lab, the knob finally does something useful. When you spin it, the
whole strip gets brighter or dimmer. The trick is a single value stored in your
code. The knob changes that value, and the value changes the lights.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    This is one of my favorite ideas in the whole kit! You're about to build a
    real dimmer switch. Spin the knob one way to glow brighter. Spin it the
    other way to fade down low. Let's light this up!

## What You'll Learn

By the end of this lab, you'll be able to:

- Store a setting in a **parameter** (a value your code remembers and uses)
- Spin the knob to raise or lower that parameter
- **Clamp** a value so it stays inside a safe range
- Scale a color by a fraction to dim the whole strip

## What You'll Need

- Your Rotary Spinner Box with the Pico inside
- The 12-pixel LED strip on GPIO pin 0
- The rotary encoder (the knob) on GPIO pins 12 and 13
- A USB cable and the Thonny program open on your computer

## The Big Idea: A Parameter

A **parameter** is a value your code stores and uses to make a choice. Think of
it like the volume number on a speaker. The number lives in one place. When you
change the number, the sound changes.

In this lab, our parameter is named `brightness`. The knob changes it. The
strip reads it. That one connection — input changes a value, value changes the
output — is the heart of every lab from here on.

## Setting Up the Parameter

First we make two variables to hold our brightness setting.

```python
# The brightness parameter: a value from 0 (off) to 20 (full)
brightness = 10
MAX_BRIGHTNESS = 20
```

`brightness` starts at `10`, which is halfway up. `MAX_BRIGHTNESS` is `20`, the
highest we will allow. The strip starts at a medium glow.

We also pick a base color before any dimming happens.

```python
# The base color of the strip before brightness is applied
BASE_COLOR = (255, 120, 0)
```

`BASE_COLOR` is a warm orange. The three numbers are the red, green, and blue
amounts. You'll see this orange at its brightest when `brightness` reaches the
top.

## Scaling the Color

To dim the strip, we shrink the color by a fraction. We divide the current
brightness by the maximum to get that fraction.

```python
def show_brightness():
    fade = brightness / MAX_BRIGHTNESS
    color = (int(BASE_COLOR[0] * fade),
             int(BASE_COLOR[1] * fade),
             int(BASE_COLOR[2] * fade))
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()
```

The line `fade = brightness / MAX_BRIGHTNESS` makes a number between `0` and
`1`. At `brightness = 10`, `fade` is `0.5`, so each color number is cut in
half. We multiply each part of `BASE_COLOR` by `fade`, then use `int()` to turn
it back into a whole number. The whole strip lights up at that dimmed color.

!!! info "Pixel thinks..."
    <img src="../../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    Why divide before we multiply? The fraction `fade` is like a dimmer dial set
    between 0 and 1. Multiply a color by `0.5` and you get half the light.
    Multiply by `1` and you get the full color. It's a smooth way to fade
    anything.

## Reading the Knob

The knob is a **rotary encoder** (a dial that reports each click as you turn
it). We watch two pins, `clk` and `dt`, to learn which way it spun.

```python
while True:
    current_clk = clk.value()
    if current_clk != last_clk and current_clk == 0:
        if dt.value() != current_clk:
            # clockwise: brighter (but not past the maximum)
            brightness = min(brightness + 1, MAX_BRIGHTNESS)
        else:
            # counterclockwise: dimmer (but not below zero)
            brightness = max(brightness - 1, 0)
        print('brightness:', brightness)
        show_brightness()
    last_clk = current_clk
```

When you spin the knob one click clockwise, `brightness` goes up by one. Spin it
the other way, and `brightness` goes down by one. Each turn redraws the strip,
so the lights respond right away.

## Clamping the Value

Here is the clever part. We never want `brightness` to go above `20` or below
`0`. **Clamping** means keeping a value inside a set range. We use two helper
functions to do it.

- `min(brightness + 1, MAX_BRIGHTNESS)` adds one, but never goes past `20`. The
  `min()` function picks the smaller of two numbers.

- `max(brightness - 1, 0)` subtracts one, but never drops below `0`. The
  `max()` function picks the larger of two numbers.

So even if you spin the knob hard, the brightness stops at the top and the
bottom. The value stays safe.

!!! warning "Watch out!"
    <img src="../../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    Without `min()` and `max()`, the brightness could climb way past `20` or
    fall below `0`. That would push the color math out of range and confuse the
    strip. Clamping keeps every value where it belongs.

## Try It Yourself

1. **Pick a new base color.** Change `BASE_COLOR = (255, 120, 0)` to
   `(0, 200, 255)` for a cool blue. Spin the knob and watch the new color fade.
2. **Add more steps.** Change `MAX_BRIGHTNESS = 20` to `MAX_BRIGHTNESS = 40`.
   Now the knob takes more clicks to reach full brightness. Does the fade feel
   smoother?
3. **Start dark.** Change `brightness = 10` to `brightness = 0`. The strip
   begins fully off. Spin clockwise to bring it to life.

## Check Your Understanding

1. What is a parameter, in your own words?
2. Which variable in this program is the parameter?
3. What does the `fade` value do to the color?
4. Why do we use `min()` and `max()` on the brightness?
5. What happens to the strip each time you turn the knob one click?

!!! success "Chapter complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You built a real dimmer with code! You stored a value, changed it with the
    knob, and kept it safe with clamping. This input-changes-a-value idea powers
    every lab ahead. You're already glowing!

## What's Next

In [Lab 10: Knob Color](10-rotary-color.md), you'll use the same knob to spin
through a whole rainbow of colors.
