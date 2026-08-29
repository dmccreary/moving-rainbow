# Charge-Up Game

Every button lesson so far reacted the instant you pressed a button. This
one reacts to something new: *how long* you hold it down. Hold Button 1,
watch the strip fill up, and try to let go exactly inside the target zone.

!!! tip "Pixel says..."
    Timing games are one of my favorite kinds of puzzle. You're not just
    pressing a button anymore — you're feeling out a rhythm!

## What you'll learn

- How to measure the time between a button press and its release
- How to turn elapsed time into a growing bar of pixels
- Why a simple polling loop can be the clearest tool for real-time games

## What you'll need

- Your Pico, NeoPixel strip, and one button from the earlier lessons
- The kit's `config.py` file

## Measuring a Hold, Not Just a Press

Every button lesson before this one asked "did the button just get
pressed?" This one asks a different question: "how long has the button
*been* pressed?" The trick is recording the time when the button goes
down, then checking the clock again while it's still held:

```python
press_time = ticks_ms()
...
held_seconds = ticks_diff(ticks_ms(), press_time) / 1000
```

## Why Polling Instead of Interrupts?

You've been using `irq()` for the last several lessons. This game goes
back to a simple polling loop instead, because the strip needs to update
continuously *while* the button is held — not just at the moment it
changes. Polling makes that easy to follow; interrupts would only
complicate it here.

## The Full Program

```python
# Hold Button 1 to fill the strip. Try to release exactly when the bar
# reaches the target zone (marked in blue) to win!
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms, ticks_diff
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)

FILL_SECONDS = 3.0     # time it takes to fill the whole strip
TARGET_START = config.NUMBER_PIXELS - 10
TARGET_END = config.NUMBER_PIXELS - 6


def draw_bar(lit_count):
    for i in range(config.NUMBER_PIXELS):
        in_target = TARGET_START <= i <= TARGET_END
        if i < lit_count:
            strip[i] = (255, 255, 0) if in_target else (0, 120, 0)
        else:
            strip[i] = (0, 0, 150) if in_target else (0, 0, 0)
    strip.write()


def flash(color, times=3):
    for _ in range(times):
        for i in range(config.NUMBER_PIXELS):
            strip[i] = color
        strip.write()
        sleep(0.15)
        for i in range(config.NUMBER_PIXELS):
            strip[i] = (0, 0, 0)
        strip.write()
        sleep(0.15)


draw_bar(0)

while True:
    # wait here until the button is pressed
    while button1.value() == 1:
        sleep(0.01)
    press_time = ticks_ms()

    # while the button stays down, grow the bar
    lit_count = 0
    while button1.value() == 0:
        held_seconds = ticks_diff(ticks_ms(), press_time) / 1000
        lit_count = min(config.NUMBER_PIXELS,
                         int((held_seconds / FILL_SECONDS) * config.NUMBER_PIXELS))
        draw_bar(lit_count)
        sleep(0.02)

    # the button was released - check the result
    if TARGET_START <= lit_count <= TARGET_END:
        print("You win! Released at pixel", lit_count)
        flash((0, 200, 0))
    else:
        print("Try again! Released at pixel", lit_count)
        flash((200, 0, 0))

    draw_bar(0)
    sleep(0.5)
```

The unlit target zone glows dim blue so you know where to aim. Hold the
button, watch the green bar grow, and let go inside the blue zone to win —
it turns yellow and the strip flashes green.

!!! warning "Watch out!"
    If you release too soon, `lit_count` will be small. Too late, and it
    hits `config.NUMBER_PIXELS`. Both count as a miss — only the target
    zone counts as a win.

## Try It Yourself

- Change `FILL_SECONDS` to `1.5` for a faster, harder game.
- Move the target zone to the very start of the strip instead of the end.

## Check Your Understanding

1. What does `ticks_diff(ticks_ms(), press_time)` calculate?
2. Why does this lesson use polling instead of the `irq()` interrupts from earlier lessons?
3. What happens to `lit_count` if you hold the button longer than `FILL_SECONDS`?
4. How would you make the target zone wider or narrower?

!!! success "You've got this!"
    You just built a real timing-based game. The exact same idea powers
    rhythm games and "stop the bar" carnival games.

**What's next:** in [Tug of War](44-tug-of-war.md), two players compete
using the button-moves-a-pixel idea from earlier in the book.
