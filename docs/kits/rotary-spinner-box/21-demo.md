# Lab 13: The Capability Demo

This is the grand finale. One program shows off **nine** light patterns. You
press a button to pick a pattern. You spin the knob to change it. This is the
program that runs at science fairs and STEM nights as a 60-second "demo of
capability" — a quick way to show everything your box can do.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    You made it to the last lab! This program is my favorite. It packs nine
    light shows into one file. The secret is that I don't write nine separate
    programs. I write *one* smart program and feed it nine sets of numbers.
    Let's light this up one more time!

## What You'll Learn

By the end of this lab, you'll be able to:

- Explain **abstraction** — hiding details so one piece of code does many jobs
- Use small **lists** (tables of numbers) to drive nine different patterns
- See how the knob changes something in *every* mode
- Pick a random color that looks **vivid** (bright and clear), not muddy
- Read a big program and find the part you want to change

## What You'll Need

- Your fully built Rotary Spinner Box
- A USB cable to connect the box to your computer
- The whole box working: the **strip**, the **knob**, and **both buttons**

This program is also copied into `main.py`. That means your box runs it
automatically when you plug it in — no computer needed.

## One Program, Nine Patterns

Most of this book used one program per pattern. This lab does something
smarter. It uses **abstraction** — that means hiding the small differences so
one piece of code can do many jobs.

The buttons choose the pattern. The knob changes one thing in that pattern.
Here is what the knob does in each mode.

| # | Pattern | What the knob changes |
|---|---------|-----------------------|
| 0 | Knob Dot | Moves a single bright pixel along the strip |
| 1 | Bar / Level | How many pixels are lit, like a volume meter |
| 2 | Solid Color | The color of the whole strip |
| 3 | Larson Scanner | The color of the sweeping "eye" |
| 4 | Comet | The length of the glowing tail |
| 5 | Theater Chase | The spacing between the lit "bulbs" |
| 6 | Sparkle | How many sparkles twinkle at once |
| 7 | Candle Flicker | How bright the flame glows |
| 8 | Rainbow | Slides the whole rainbow along the strip |

Your strip is a straight 12-pixel line, not a ring. So the moving patterns
**bounce** off the ends instead of wrapping around.

## The Data That Drives Everything

Here is the heart of the program. Instead of nine programs, we keep nine
small **lists** (rows of values, one slot per mode). Each list holds one number
for each pattern.

```python
MODE_NAMES = ['Knob Dot', 'Bar / Level', 'Solid Color', 'Larson Scanner',
              'Comet', 'Theater Chase', 'Sparkle', 'Candle Flicker', 'Rainbow']

# Each mode stores one value that the knob changes.
params =    [N // 2, N // 2, 0,    0,    5,     3,  5,   20,  0]
PARAM_MIN = [0,      0,      0,    0,    1,     2,  1,   3,   0]
PARAM_MAX = [N - 1,  N,      255,  255,  N - 1, 6,  N,   40,  255]
PARAM_STEP = [1,     1,      8,    8,    1,     1,  1,   2,   8]
WRAP =      [False,  False,  True, True, False, False, False, False, True]
FRAME_MS =  [80,     80,     80,   60,   60,    90, 60,  70,  80]
```

When you spin the knob in mode 4, the program looks at slot 4 in each list. To
add a new pattern, you'd add one value to each list — not write a whole new
program. That is the power of **data-driven design** (letting tables of numbers
control the code).

!!! info "Pixel thinks..."
    <img src="../../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    Read those lists like columns on a chart. `PARAM_MIN` is the smallest the
    knob can go. `PARAM_MAX` is the biggest. `FRAME_MS` is how many
    milliseconds (thousandths of a second) wait between frames. Each pattern
    gets its own column of settings. Neat, right?

## How the Knob Stays in Bounds

Every spin of the knob changes one value. Some values should stop at a limit,
like brightness. Other values should **wrap** (roll over from the top back to
the bottom), like colors on a wheel. The `WRAP` list decides which is which.

```python
turn = read_knob()          # +1 for clockwise, -1 the other way, 0 for none
if turn != 0:
    if WRAP[mode]:
        # colors roll over: 255 + 1 becomes 0 again
        params[mode] = (params[mode] + turn * PARAM_STEP[mode]) % 256
    else:
        # everything else stops, or "clamps," at its limits
        new_value = params[mode] + turn * PARAM_STEP[mode]
        if new_value < PARAM_MIN[mode]:
            new_value = PARAM_MIN[mode]
        if new_value > PARAM_MAX[mode]:
            new_value = PARAM_MAX[mode]
        params[mode] = new_value
```

When you spin the knob, the strip changes right away — every single mode reacts.
**Clamping** means a value stops at its edge instead of going past it.

## The Random Color Trick

The Sparkle pattern needs random colors. But there's a smart way and a muddy
way to pick one. We pick a random **hue** (a spot on the color wheel) and run it
through `color_wheel`. We do *not* pick three random red, green, and blue
numbers.

```python
def random_vivid_hue():
    # Pick one random spot on the color wheel, 0 to 255.
    return random.randint(0, 255)
```

Random hues come out bright and easy to tell apart. Random red-green-blue
numbers come out dull and similar, like mud. One random number beats three.

!!! tip "Pixel's tip"
    <img src="../../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel shares a tip">
    Want to remember the trick? A hue is a *pure* color from the rainbow.
    Three random color channels usually mix into a brownish blur. So spin the
    wheel, don't roll three dice. Your sparkles will pop!

## A Look at One Pattern

Each pattern lives in its own little block inside the `draw` function. Here is
the Rainbow pattern. The knob value `params[8]` slides the colors along.

```python
elif mode == 8:
    # Rainbow: a full rainbow across the strip.  The knob rotates it.
    offset = params[8]
    for i in range(N):
        strip[i] = color_wheel(int(i * 256 / N) + offset)
```

When you spin the knob in this mode, the rainbow slides smoothly down the strip.
All nine patterns share this same `draw` function, picked by the `mode` number.

## Try It Yourself

1. **Speed up a pattern.** Find the `FRAME_MS` list. Change the first value
   from `80` to `30`. Run the program and watch the Knob Dot mode. It moves
   faster now.
2. **Stretch the comet's tail.** In `PARAM_MAX`, the Comet's slot is `N - 1`.
   The value before it is the Comet step. Spin the knob in Comet mode and watch
   the tail grow until it hits its limit. Then change `PARAM_STEP` for Comet
   from `1` to `2`. How does the knob feel different?
3. **Brighten the candle.** In `PARAM_MAX`, the Candle Flicker slot is `40`.
   Change it to `120`. Spin the knob in Candle mode. The flame can now glow
   much brighter.

## Check Your Understanding

1. What does **abstraction** mean in this program?
2. How many patterns does one button cycle through?
3. What does the `WRAP` list decide for each mode?
4. Why do we pick a random *hue* instead of three random color numbers?
5. To add a tenth pattern, what would you add to each list?

!!! success "Chapter complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You did it — you finished the whole kit! You started by blinking one tiny
    light. Now you can run a nine-pattern light show driven by smart tables of
    numbers. That is real computational thinking. Every coder who walks up to
    your box at a science fair will see what you can build. I am so proud of
    you. You're glowing brighter than ever!

## What's Next

This is the final lab — congratulations! You've learned sequencing, loops,
colors, buttons, knobs, interrupts, timers, and now abstraction.

Head back to the [Rotary Spinner Box](index.md) home page to revisit any lab.
Then open `21-demo.py` and read the whole program. Find a pattern you love,
copy its block, and invent a brand-new pattern of your own. The box is yours
now — go make it shine.
