# Lab 11: Monster Eyes

Pairs of glowing eyes hide along your costume. Each pair blinks at its own random time, as if monsters are watching.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Something is watching you... and it is your own code! Lists help us keep track of many monsters at once.

**Program file:** [`11-monster-eyes.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/11-monster-eyes.py)

## What You'll Learn

- Keep a list of lists, one for each pair of eyes
- Use the clock with `ticks_ms()` (milliseconds since the Pico started)
- Plan a random time for each blink

## What You'll Need

- Your costume with the strip connected

## The Program

This program draws every pair of open eyes, and shuts each pair for a short blink at its own time.

```python
--8<-- "src/kits/halloween-60-button/11-monster-eyes.py"
```

You should see six pairs of red, green, orange or purple eyes that blink at different times.

## How It Works

Each pair of eyes is a small list: `[first pixel, color, next blink time]`. All pairs live in the big `eyes` list.

`ticks_diff(blink_at, now)` tells us how many milliseconds until the blink. While it is more than 0, the eyes are open.

When the blink is over, we pick a new random blink time from 1 to 5 seconds away.

## Try It Yourself

1. Change `EYE_SPACING` to `6` for more monsters.
2. Make the blinks longer by changing `BLINK_TIME`.

## Check Your Understanding

1. What three things does each pair of eyes remember?
2. What does `ticks_ms()` return?
3. Why does each pair blink at a different time?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 12: Blood Drip](12-blood-drip.md).
