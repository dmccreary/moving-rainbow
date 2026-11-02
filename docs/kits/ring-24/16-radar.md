# Lab 16: Radar

A green beam sweeps around the ring like a radar screen. When the beam finds a hidden target, the target glows red and slowly fades.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Beep... beep... target found! Let's build a radar that scans the whole sky.

**Program file:** [`16-radar.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/ring-24/16-radar.py)

![A green radar beam near the top of the ring with a fading trail, and dim red targets](img/16-radar.png){ width="260" }

*Drawn by a ring simulator on a computer, so your real ring may look a little different. On the real ring it moves.*

## What You'll Learn

- Make a fading tail with an **exponent** (a small number that says how many times to multiply a number by itself)
- Use `in` to check if a number is in a list
- Keep a **glow** value (how brightly something shines, from 0.0 to 1.0) for every pixel and shrink it each step
- Use random numbers to make targets **drift** (move a little at a time)

## What You'll Need

- Your ring kit with the ring on GPIO 0
- `config.py` saved on the Pico

## The Program

This program sweeps a beam around the ring and lights up the targets it passes.

```python
--8<-- "src/kits/ring-24/16-radar.py"
```

You should see a green beam with a long glowing tail sweep clockwise around the ring. Targets flash red as the beam passes them and then fade. After each sweep, a target may drift one pixel.

## How It Works

`beam` is the pixel where the beam points. Each step it goes up by 1, and `%` wraps it from 23 back to 0. The tail sits behind the beam, at `beam - t`, and it is `TAIL_LENGTH` (12) pixels long.

The tail's brightness is `(1 - t / TAIL_LENGTH) ** 3`. The `**` sign means "to the power of," so `** 3` multiplies a number by itself three times. For example, `0.5 ** 3` is 0.5 × 0.5 × 0.5 = 0.125. This makes the glow drop fast right behind the beam and then fade out gently.

`targets` is a list of 3 pixel numbers picked with `randint()`. `if beam in targets` is true when the beam points at a target. Then `glow[beam]` is set to 1.0, which is full glow. Once in a while two targets land on the same pixel, so you may see only two.

`glow` holds one number for each of the 24 pixels. Each step, a glowing pixel is drawn red, and its glow is multiplied by `GLOW_FADE` (0.93). So it keeps 93% of its glow each step. The red is drawn after the beam, so it shows on top of the green.

A glow takes about 50 steps to fade out, but one sweep is only 24 steps. So a target still glows faintly when the beam comes back around. When `beam` returns to 0, `randint(-1, 1)` picks -1, 0 or 1 for each target. The target moves back one pixel, stays put, or moves ahead one pixel.

## Try It Yourself

1. Change `TARGET_COUNT` to `6`. How busy is the sky now?
2. Change `GLOW_FADE` to `0.8`. Do the targets fade faster or slower? Do they stay hidden until the beam comes back?

## Check Your Understanding

1. What does `2 ** 3` equal?
2. What does `beam in targets` check?
3. How far can a target drift after one sweep?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    Target locked! Your radar scans the sky like a pro.

## What's Next

Go on to [Lab 17: Planets](17-planets.md).
