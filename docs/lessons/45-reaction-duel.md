# Reaction Duel

This is a classic reflex game. The strip flashes red while you wait, then
turns green at a random moment. Whoever presses their button first — after
green, not before — wins.

!!! tip "Pixel says..."
    This is my favorite kind of challenge — pure reflexes! Just don't
    jump the gun. Pressing too early costs you the round.

## What you'll learn

- How to pick a random wait time with `urandom.randint()`
- How to structure a program around game **phases**: waiting, armed, and go
- How to detect a "false start" before the real event happens

## What you'll need

- Your Pico, NeoPixel strip, and two buttons from the earlier lessons
- The kit's `config.py` file

## A Program with Phases

Earlier button programs reacted to presses the instant they happened,
using `irq()`. A duel needs to treat presses differently depending on
*when* they happen — a press during the red "wait" phase is a false
start, but the same press during the green "go" phase is a win. That's
easier to write as a sequence of polling loops, one phase at a time.

```python
wait_ms = randint(2000, 5000)   # a different wait time every round
```

Picking a random wait time is what makes the game fair — nobody can
memorize the timing and jump the gun on purpose.

## The Full Program

```python
# Reaction Duel! Wait for the strip to flash green, then be the first
# to press your button. Press too early and you lose!
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)


def fill_strip(color):
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()


def wait_for_release():
    # make sure both buttons are up before starting a new round
    while button1.value() == 0 or button2.value() == 0:
        sleep(0.01)


while True:
    wait_for_release()
    fill_strip((200, 0, 0))   # red = get ready
    print("Get ready...")

    wait_ms = randint(2000, 5000)   # random 2-5 second delay
    start_wait = ticks_ms()

    false_start = False
    while ticks_ms() - start_wait < wait_ms:
        if button1.value() == 0:
            print("Player 1 jumped early - Player 2 wins!")
            false_start = True
            break
        if button2.value() == 0:
            print("Player 2 jumped early - Player 1 wins!")
            false_start = True
            break
        sleep(0.005)

    if false_start:
        fill_strip((200, 0, 0))
        sleep(2)
        continue

    fill_strip((0, 200, 0))   # green = go!
    go_time = ticks_ms()
    print("GO!")

    winner = None
    while winner is None:
        if button1.value() == 0:
            winner = "Player 1"
        elif button2.value() == 0:
            winner = "Player 2"

    reaction_ms = ticks_ms() - go_time
    print(winner, "wins! Reaction time:", reaction_ms, "ms")
    fill_strip((0, 0, 200))
    sleep(2)
```

Hand the Pico to two players. The strip turns red, waits a random amount
of time, then flashes green. Watch the Shell for the winner and their
exact reaction time in milliseconds.

!!! warning "Watch out!"
    The false-start check and the winner check look almost identical —
    both watch for a button press. The difference is *which phase* the
    program is in when the press happens. That's the whole idea behind
    phase-based games.

## Try It Yourself

- Narrow the random range to `randint(1000, 2000)` for a faster-paced game.
- Track and print the best (lowest) reaction time across multiple rounds.

## Check Your Understanding

1. Why does the program pick a random wait time instead of a fixed one?
2. What makes a press count as a "false start" instead of a win?
3. What does `wait_for_release()` prevent from happening at the start of a new round?
4. How many separate phases does one round of this game have? Name them.

!!! success "You've got this!"
    You just built a fair, reflex-based competitive game — the same
    fundamental idea behind sprint-start lights at a real track meet.

**What's next:** in [Fire Simulation](46-fire-simulation.md), you'll
leave games behind for a moment and build the most advanced ambient
effect in the book.
