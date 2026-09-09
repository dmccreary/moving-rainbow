# Tug of War

Remember [Buttons Move a Pixel](27-buttons-move-pixel.md)? This lesson
uses that exact same idea — buttons moving a marker along the strip — and
turns it into a two-player game with a winner.

!!! tip "Pixel says..."
    Grab a friend for this one! Two players, two buttons, one marker in
    the middle. Whoever pulls it to their end first wins.

## What you'll learn

- How to add a win condition to a moving-pixel program
- How to use a `game_over` flag to stop reacting to input once a game ends
- How to give each player their own end of the strip to defend

## What you'll need

- Your Pico, NeoPixel strip, and two buttons from the earlier lessons
- The kit's `config.py` file

## Adding a Winner to a Familiar Idea

The button handler moves `position` up or down exactly like it did in
lesson 27. The new part is checking, after every move, whether the marker
has reached either end of the strip:

```python
if position >= LAST_PIXEL:
    print("Player 1 wins!")
    game_over = True
```

## The Full Program

```python
# Two-player tug of war! Button 1 pulls the marker toward the high end.
# Button 2 pulls it toward the low end. First to reach their end wins!
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

LAST_PIXEL = config.NUMBER_PIXELS - 1
position = config.NUMBER_PIXELS // 2   # marker starts in the middle

DEBOUNCE_MS = 120
last_press = 0
game_over = False


def draw_marker():
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip[position] = (200, 0, 200)
    strip.write()


def button_handler(pin):
    global position, last_press, game_over
    if game_over:
        return
    now = ticks_ms()
    if now - last_press < DEBOUNCE_MS:
        return
    last_press = now

    if pin == button1:
        position += 1   # Player 1 pulls toward the high end
    else:
        position -= 1   # Player 2 pulls toward the low end

    draw_marker()

    if position >= LAST_PIXEL:
        print("Player 1 wins!")
        game_over = True
    elif position <= 0:
        print("Player 2 wins!")
        game_over = True


button1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

draw_marker()

while True:
    if game_over:
        # flash the winning end of the strip
        winner_pixel = LAST_PIXEL if position >= LAST_PIXEL else 0
        strip[winner_pixel] = (255, 255, 0)
        strip.write()
        sleep(0.2)
        strip[winner_pixel] = (0, 0, 0)
        strip.write()
        sleep(0.2)
    else:
        sleep(0.05)
```

Hand the Pico to two players — one mashes Button 1, the other mashes
Button 2. The marker moves toward whoever presses faster, and the winning
end flashes gold when someone reaches it.

!!! info "Pixel thinks..."
    Look at the very first line of `button_handler`:
    `if game_over: return`. Once someone wins, this stops the marker from
    moving again until you restart the program. Try removing that line —
    what happens to the flashing winner light?

## Try It Yourself

- Add a small buzzer sound effect by printing `"WIN!"` in big letters when
  a player wins.
- Make the marker need to reach the end *twice* (best of 3 rounds) before
  declaring a winner.

## Check Your Understanding

1. What does the `game_over` flag prevent from happening?
2. Why does `position` start in the middle of the strip instead of at 0?
3. What determines which end of the strip flashes at the end of the game?
4. How is this program similar to lesson 27? What's the one new idea?

!!! success "You've got this!"
    You just added a win condition to an existing program instead of
    starting from scratch — that's exactly how real projects grow.

**What's next:** in [Reaction Duel](45-reaction-duel.md), the two players
race against a random delay instead of against each other's button mashing.
