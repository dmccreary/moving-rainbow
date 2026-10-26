# Lab 20: Main Template

This program puts all eleven patterns from Labs 6 to 16 into one costume. Mode 0 changes the pattern every 10 seconds by itself. Each press of the button picks the next mode.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    This is it, the full costume! Everything you built comes together in one program.

**Program file:** [`20-main-template.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/20-main-template.py)

## What You'll Learn

- Turn each pattern into a **draw function** that draws one step
- Use an **interrupt** (code that runs the moment the button is pressed)
- Add a **debounce** so one press counts once
- Run the program on its own as `main.py`

## What You'll Need

- Your finished costume with the strip and the button
- All the lab files uploaded with `./upload-code.sh`

## The Program

This program draws one step of the current pattern, writes the strip and checks the mode again.

```python
--8<-- "src/kits/halloween-60-button/20-main-template.py"
```

The costume starts in auto mode and shows a new pattern every 10 seconds. Press the button to pick one pattern.

## The Modes

| Mode | Pattern | From |
|------|---------|------|
| 0 | Auto: a new pattern every 10 seconds | |
| 1 | Orange and Purple Chase | [Lab 6](06-orange-and-purple-chase.md) |
| 2 | Pumpkin Glow | [Lab 7](07-pumpkin-glow.md) |
| 3 | Candy Corn | [Lab 8](08-candy-corn.md) |
| 4 | Spooky Sparkle | [Lab 9](09-spooky-sparkle.md) |
| 5 | Ghost Drift | [Lab 10](10-ghost-drift.md) |
| 6 | Monster Eyes | [Lab 11](11-monster-eyes.md) |
| 7 | Blood Drip | [Lab 12](12-blood-drip.md) |
| 8 | Bat Swarm | [Lab 13](13-bat-swarm.md) |
| 9 | Cauldron Bubbles | [Lab 14](14-cauldron-bubbles.md) |
| 10 | Jack-o'-Lantern Fire | [Lab 15](15-jack-o-lantern-fire.md) |
| 11 | Lightning Storm | [Lab 16](16-lightning-storm.md) |

## How It Works

Each pattern is a draw function that sets the colors for just one step and returns. The main loop calls it, writes the strip and sleeps. No pattern runs a long loop, so the button works right away.

`button.irq()` tells the Pico to run `button_pressed()` the moment the pin falls to 0. The function ignores presses that come less than 250 ms apart. Buttons "bounce" and can look like many presses.

In mode 0, the loop checks the clock. After `AUTO_MS` (10,000 ms), it moves to the next pattern.

The Pico runs `main.py` by itself when it gets power. Save a copy of this file on the Pico as `main.py`, and your costume starts when you plug in the battery.

## Try It Yourself

1. Change `AUTO_MS` to `5000` for faster auto mode.
2. Add your own pattern: write a `draw_` function and add a line to the `patterns` list.

## Check Your Understanding

1. Why does each draw function only draw one step?
2. What is debouncing?
3. What file name does the Pico run by itself?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You built a whole light-up costume! Now go show it off. Happy Halloween!

## What's Next

Make the costume your own: change the colors, invent a new pattern, or go back to the [kit page](index.md).
