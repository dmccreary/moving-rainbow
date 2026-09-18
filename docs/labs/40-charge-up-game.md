# Lab 40: Charge-Up Game

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Ready for a timing game? Hold the button, watch the light climb, and let go at the perfect moment. Feel the rhythm!

**Program file:** [`40-charge-up-game.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/40-charge-up-game.py)

## What you'll learn

- How to measure how long a button is held with `ticks_ms()` and `ticks_diff()`
- How to turn a length of time into a bar of lit pixels
- How **polling** (checking a button again and again in a loop) works
- How to test whether a number lands inside a target range

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- Button 1 wired as shown in [The Two Buttons](../kits/moving-rainbow-base/index.md#the-two-buttons). A pressed button reads 0, and a released button reads 1.
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

If you want to practice reading a button first, try [Lab 32: Button Test](32-button-test.md).

## The program

In this game you hold Button 1 to fill the strip with light. Try to let go when the bar reaches the blue target zone.

```python title="40-charge-up-game.py"
--8<-- "src/kits/moving-rainbow-base/40-charge-up-game.py"
```

Run it. Five dim blue pixels near the far end of the strip mark the target. Hold Button 1 and a green bar grows from pixel 0, adding about one pixel every tenth of a second. When you let go, the strip flashes green for a win or red for a miss, and the Shell says what happened.

## How it works

### The target zone

These lines set how long the bar takes to fill and where the target sits.

```python
FILL_SECONDS = 3.0     # time it takes to fill the whole strip
TARGET_START = NUMBER_PIXELS - 10
TARGET_END = NUMBER_PIXELS - 6
```

The bar fills all 30 pixels in 3 seconds, so it adds one pixel about every 0.1 seconds. With 30 pixels, `TARGET_START` is 20 and `TARGET_END` is 24. The target zone is five pixels: 20, 21, 22, 23, and 24.

### Draw the bar

This function redraws all 30 pixels each time it runs. The input `lit_count` is the number of pixels that should be lit, starting from pixel 0.

```python
def draw_bar(lit_count):
    for i in range(NUMBER_PIXELS):
        in_target = TARGET_START <= i <= TARGET_END
        if i < lit_count:
            strip[i] = (255, 255, 0) if in_target else (0, 120, 0)
        else:
            strip[i] = (0, 0, 150) if in_target else (0, 0, 0)
    strip.write()
```

The line `TARGET_START <= i <= TARGET_END` is a **chained comparison**. It is true when `i` is 20 or more and 24 or less. Each pixel gets one of four looks, using the conditional expressions you met in [Lab 38](38-traffic-light.md).

- Lit and inside the zone: yellow, `(255, 255, 0)`
- Lit and outside the zone: green, `(0, 120, 0)`
- Not lit and inside the zone: dim blue, `(0, 0, 150)`
- Not lit and outside the zone: dark

### Wait for the press

This loop waits until the button goes down, then saves the time.

```python
# wait here until the button is pressed
while button1.value() == 1:
    sleep(0.01)
press_time = ticks_ms()
```

A released button reads 1, so the loop keeps running while the button is up. Checking a button over and over like this is called **polling**. The `sleep(0.01)` means the Pico checks 100 times every second.

`ticks_ms()` gives the number of **milliseconds** (thousandths of a second) since the Pico started. The program saves that number as `press_time`, so it knows when the hold began.

Labs 34 to 36 used interrupts, which run a function when a button is pressed. This game uses polling instead, because the strip must keep changing while you hold the button. A loop that watches the button keeps that flow clear.

### Measure the hold

This loop runs for as long as the button stays down. Each time around, it works out how many pixels to light.

```python
# while the button stays down, grow the bar
lit_count = 0
while button1.value() == 0:
    held_seconds = ticks_diff(ticks_ms(), press_time) / 1000
    lit_count = min(NUMBER_PIXELS,
                     int((held_seconds / FILL_SECONDS) * NUMBER_PIXELS))
    draw_bar(lit_count)
    sleep(0.02)
```

Here is the math, one step at a time.

1. `ticks_diff(ticks_ms(), press_time)` gives the milliseconds since the press. `ticks_diff()` stays correct even when the clock counter rolls over.
2. Dividing by 1000 turns milliseconds into `held_seconds`.
3. Dividing `held_seconds` by `FILL_SECONDS` gives how full the bar is, from 0 to 1.
4. Multiplying by `NUMBER_PIXELS` turns that fraction into a number of pixels.
5. `int()` drops the decimal part, and `min()` keeps the answer from going past 30.

For example, after 1.55 seconds the math is 1.55 ÷ 3.0 × 30 = 15.5, and `int()` makes that 15. So `lit_count` is 15, and pixels 0 to 14 are lit. If you hold longer than 3 seconds, `lit_count` stays at 30.

### Win or miss

After you let go, this code checks the result and flashes the strip.

```python
if TARGET_START <= lit_count <= TARGET_END:
    print("You win! Released at pixel", lit_count)
    flash((0, 200, 0))
else:
    print("Try again! Released at pixel", lit_count)
    flash((200, 0, 0))
```

The test passes when `lit_count` is 20, 21, 22, 23, or 24. With the 3-second fill, that means a hold of about 2.0 to 2.5 seconds. In other words, let go when the green bar reaches the blue zone, and before the last blue pixel turns yellow.

The Shell message says "pixel," but `lit_count` is a count of lit pixels, not a pixel number.

!!! bug "Known issue"
    The blue zone is drawn on pixels 20 to 24, but the win test uses `lit_count`, which counts lit pixels. That puts the winning window one pixel early. Releasing with 20 lit pixels wins, but releasing with 25 lit pixels (the whole blue zone yellow) is a miss.

This function makes the flashing you see after each try.

```python
def flash(color, times=3):
    for _ in range(times):
        for i in range(NUMBER_PIXELS):
            strip[i] = color
        strip.write()
        sleep(0.15)
        for i in range(NUMBER_PIXELS):
            strip[i] = (0, 0, 0)
        strip.write()
        sleep(0.15)
```

The `times=3` part is a **default value**. The function flashes 3 times unless you ask for a different number. The name `_` in the `for` loop means "repeat this, and skip the counter." Each flash is 0.15 seconds on and 0.15 seconds off.

Once the flashing ends, `draw_bar(0)` resets the strip and `sleep(0.5)` pauses briefly. Then the outer `while True` loop waits for your next press.

## Try it yourself

1. Change `FILL_SECONDS = 3.0` to `FILL_SECONDS = 1.5`. The bar climbs twice as fast, so the winning window gets half as wide. Can you still win?
2. Advanced challenge: fix the Known issue. Change the `if TARGET_START <= lit_count <= TARGET_END:` line so a win happens when the last lit pixel is inside the blue zone. Hint: the last lit pixel is number `lit_count - 1`.

## Check your understanding

1. What does `ticks_diff(ticks_ms(), press_time)` measure?
2. Why does this game check the button in a loop instead of using an interrupt?
3. If you hold the button for 1.55 seconds, how many pixels are lit?
4. What happens to `lit_count` if you hold longer than `FILL_SECONDS`?
5. Which `lit_count` values count as a win in this program?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built a real timing game! Rhythm games and "stop the bar" carnival games use this same idea.

**What's next:** In [Lab 41: Tug of War](41-tug-of-war.md), two players compete to pull a marker to their end of the strip.
