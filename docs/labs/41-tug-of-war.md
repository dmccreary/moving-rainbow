# Lab 41: Tug of War

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Grab a friend for this one! Two players, two buttons, and one glowing marker. Whoever pulls it to their end first wins.

**Program file:** [`41-tug-of-war.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/41-tug-of-war.py)

## What you'll learn

- How two buttons can share one **handler** (a function that runs when a button is pressed)
- How to add a win condition to a program that moves a light
- How **debouncing** stops one press from counting twice
- How a `game_over` flag stops the game after someone wins

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- Both buttons wired as shown in [The Two Buttons](../kits/moving-rainbow-base/index.md#the-two-buttons). A pressed button reads 0.
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- A friend to play against

This lab uses **interrupts**, which you met in [Lab 34: Two Buttons](34-two-button-print.md).

## The program

In this two-player game, Button 1 pulls a marker toward the high end of the strip and Button 2 pulls it toward the low end.

```python title="41-tug-of-war.py"
--8<-- "src/kits/moving-rainbow-base/41-tug-of-war.py"
```

Run it. A purple marker glows at pixel 15. Each press of Button 1 moves it up one pixel, and each press of Button 2 moves it down one pixel. When it reaches pixel 29, the Shell prints `Player 1 wins!`. When it reaches pixel 0, the Shell prints `Player 2 wins!`.

After a win, the winning end pixel blinks yellow. Nothing in the program starts a new game, so the blinking continues until you press **Stop** and then **Run** to play again.

## How it works

### Where the marker starts

These lines mark the last pixel and put the marker in the middle.

```python
LAST_PIXEL = NUMBER_PIXELS - 1
position = NUMBER_PIXELS // 2   # marker starts in the middle
```

Pixels count from 0, so with 30 pixels the last one is number 29. The `//` symbol divides and drops any decimal part, so `30 // 2` is 15. The variable `position` holds the marker's pixel number.

### Draw the marker

This function turns every pixel off, lights one purple pixel at `position`, and sends the picture to the strip.

```python
def draw_marker():
    for i in range(NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip[position] = (200, 0, 200)
    strip.write()
```

### Buttons that interrupt

These two lines connect both buttons to the same handler.

```python
button1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
```

An **interrupt** pauses the main program for a moment and runs a small function. `Pin.IRQ_FALLING` means "when the pin's value falls from 1 to 0." That is the moment a button goes down. The function is `button_handler`, and Python gives it the `pin` that fired, so the handler can tell which button was pressed.

### Ignore bounces

This is the start of the handler. It stops early if the game is over or if the press came too soon.

```python
def button_handler(pin):
    global position, last_press, game_over
    if game_over:
        return
    now = ticks_ms()
    if now - last_press < DEBOUNCE_MS:
        return
    last_press = now
```

Normally, a variable that a function changes belongs only to that function. The `global` line tells Python to use the shared `position`, `last_press`, and `game_over` instead. The [Variable Scope Explorer](../sims/variable-scope-explorer/index.md) MicroSim shows how this works.

When you press a button, the metal contacts can chatter and send several signals in a few thousandths of a second. This is called **bounce**. **Debouncing** means ignoring any signal that arrives too soon after the last real one. Here, the handler ignores presses that come less than `DEBOUNCE_MS` (120 milliseconds) after the last counted press.

!!! bug "Known issue"
    Both buttons share one `last_press` timer, so a press by the other player within 120 ms of your press is ignored. Also, the marker starts at pixel 15, so Player 1 needs 14 presses to reach pixel 29 while Player 2 needs 15 to reach pixel 0.

### Move the marker and check for a winner

This part of the handler moves the marker toward the button's player and redraws it.

```python
def button_handler(pin):
    ...
    if pin == button1:
        position += 1   # Player 1 pulls toward the high end
    else:
        position -= 1   # Player 2 pulls toward the low end

    draw_marker()
```

Then the handler checks whether the marker has reached an end.

```python
if position >= LAST_PIXEL:
    print("Player 1 wins!")
    game_over = True
elif position <= 0:
    print("Player 2 wins!")
    game_over = True
```

The variable `game_over` is a **flag**, a True-or-False switch that records what has happened. Once it is `True`, the first lines of the handler return right away, so the marker stops moving.

### The main loop

The main loop stays quiet while the game is on. After a win, it blinks the winning end.

```python
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

Which end blinks depends on where the marker stopped. The blink is yellow for 0.2 seconds and dark for 0.2 seconds. Nothing ever sets `game_over` back to `False`, so the loop blinks until you press Stop.

## Try it yourself

1. Change `DEBOUNCE_MS = 120` to `DEBOUNCE_MS = 60`. Does the game feel faster? If one push starts to count twice, the number is too small.
2. Advanced challenge: make the debounce fair. Give each button its own timer, such as `last_press1` and `last_press2`, and choose between them with the `if pin == button1:` test.

## Check your understanding

1. What does the `game_over` flag stop from happening?
2. Which button moves the marker toward pixel 29?
3. How many presses does each player need to win, starting from pixel 15?
4. Why does the handler need the `global` line?
5. What is debouncing, and why does the handler use it?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You added a winner to a moving light! That's how real games grow: one rule at a time.

**What's next:** In [Lab 42: Reaction Duel](42-reaction-duel.md), two players race to react to a random signal.
