# Lab 42: Reaction Duel

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    This game is all about reflexes! Watch for green, then press your button. Press while the strip is red, and your rival takes the round.

**Program file:** [`42-reaction-duel.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/42-reaction-duel.py)

## What you'll learn

- How to pick a random wait time with `randint()`
- How to build a game from **phases**: get ready, go, and result
- How to spot a **false start** (a press that comes too early)
- How `break` and `continue` change the path of a loop

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- Both buttons wired as shown in [The Two Buttons](../kits/moving-rainbow-base/index.md#the-two-buttons). A pressed button reads 0.
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico, with the Shell (the text area at the bottom) in view
- A friend to play against

This lab uses **polling** (checking a button again and again in a loop), the same way [Lab 40: Charge-Up Game](40-charge-up-game.md) does.

## The program

In this two-player game, the strip turns red, waits a random time, and turns green. The first player to press their button after green wins the round.

```python title="42-reaction-duel.py"
--8<-- "src/kits/moving-rainbow-base/42-reaction-duel.py"
```

Run it. The whole strip glows red, and the Shell says `Get ready...`. After 2 to 5 seconds, the strip turns green and the Shell says `GO!`. The Shell then names the winner and the reaction time in milliseconds, and the strip glows blue for 2 seconds before the next round starts. Rounds repeat until you press **Stop**.

## How it works

### Two helper functions

These functions fill the whole strip with one color and wait for both buttons to be let go.

```python
def fill_strip(color):
    for i in range(NUMBER_PIXELS):
        strip[i] = color
    strip.write()


def wait_for_release():
    # make sure both buttons are up before starting a new round
    while button1.value() == 0 or button2.value() == 0:
        sleep(0.01)
```

`wait_for_release()` keeps looping while either button reads 0 (pressed). Without it, a button still held from the last round could count as a false start in the next one.

### Phase 1: get ready

This code starts a round. It turns the strip red and picks a random wait between 2000 and 5000 milliseconds.

```python
wait_for_release()
fill_strip((200, 0, 0))   # red = get ready
print("Get ready...")

wait_ms = randint(2000, 5000)   # random 2-5 second delay
start_wait = ticks_ms()
```

`randint(2000, 5000)` gives a whole number from 2000 to 5000, and both ends can happen. The wait is different every round, so nobody can memorize the timing. `start_wait` saves the time when the wait began.

### Watch for a false start

While the wait runs, the program keeps checking both buttons.

```python
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
```

The loop runs while the time since `start_wait` is less than `wait_ms`. It checks the buttons about 200 times per second. A press during this phase is a false start, so the other player wins.

`break` ends the loop right away, even though the wait time is not over. The variable `false_start` remembers what happened. You can see how `break` works in the [break vs. continue Flow](../sims/break-continue-flowchart/index.md) MicroSim.

After the loop, this code handles a false start.

```python
if false_start:
    fill_strip((200, 0, 0))
    sleep(2)
    continue
```

`continue` skips the rest of the round and jumps back to the top of the `while True` loop. After 2 seconds, a new round begins. The strip is already red, so a false start looks like nothing happened on the strip. The Shell tells you who won.

### Phase 2: go

This code turns the strip green and waits for the first press.

```python
fill_strip((0, 200, 0))   # green = go!
go_time = ticks_ms()
print("GO!")

winner = None
while winner is None:
    if button1.value() == 0:
        winner = "Player 1"
    elif button2.value() == 0:
        winner = "Player 2"
```

`None` is Python's word for "no value yet." The loop keeps running until `winner` becomes a name. It has no `sleep()`, so it checks the buttons as fast as the Pico can.

Button 1 is checked first. If both players press at the exact same moment, Player 1 wins the tie.

### Phase 3: show the result

This code works out the reaction time, prints it, and shows blue for 2 seconds.

```python
reaction_ms = ticks_ms() - go_time
print(winner, "wins! Reaction time:", reaction_ms, "ms")
fill_strip((0, 0, 200))
sleep(2)
```

The reaction time is the time from the moment the strip turned green until the press. Many people react in about a quarter of a second, which is around 250 milliseconds. After the blue pause, the `while True` loop starts the next round.

## Try it yourself

1. Change `randint(2000, 5000)` to `randint(1000, 2000)`. The game speeds up, but can you still tell when green is coming?
2. Make a false start visible. In the `if false_start:` block, change `fill_strip((200, 0, 0))` to `fill_strip((200, 0, 200))` and watch the strip turn purple.

## Check your understanding

1. Why does the program pick a random wait time instead of a fixed one?
2. What happens if Player 2 presses while the strip is red?
3. What does `wait_for_release()` stop from happening at the start of a round?
4. If both players press at the same instant, who wins, and why?
5. What is the difference between `break` and `continue`?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built a fair reflex game with three phases! Race-start lights and quiz buzzers use this same idea: wait, signal, react.

**What's next:** In [Lab 43: Fire Simulation](43-fire-simulation.md), you leave games behind and build a flickering fire.
