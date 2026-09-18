# Lab 46: Binary Search Visualizer

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Pick a secret pixel number, and the strip will find it in five guesses or fewer. It feels like a magic trick, but it's really clever thinking. Let's light this up!

**Program file:** [`46-binary-search-visualizer.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/46-binary-search-visualizer.py)

## What you'll learn

- What **binary search** is and why it finds an answer so fast
- How `low` and `high` shrink the range of possible answers
- How `(low + high) // 2` finds the middle of a range
- How to read a button by checking it over and over, and how `wait_for_release()` stops one press from counting twice

## What you'll need

- Your base kit, including both push buttons wired as shown in [The Two Buttons](../kits/moving-rainbow-base/index.md#the-two-buttons). Each button reads `0` while you press it.
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- Helpful: [Lab 32: Button Test](32-button-test.md), which shows how to read a button with `value()`

## The program

This program plays a guessing game. You think of a secret pixel number from 0 to 29, and the strip finds it by guessing the middle of the possible range each time.

```python title="46-binary-search-visualizer.py"
--8<-- "src/kits/moving-rainbow-base/46-binary-search-visualizer.py"
```

Run it. The Shell asks you to think of a pixel number. Then the strip lights up, and it is your turn to play.

## Play the game

1. Think of a secret number from 0 to 29 and keep it in your head. You have two seconds.
2. The strip lights up. **Dim blue** pixels are numbers that are still possible. The **white** pixel is the current guess. Dark pixels are ruled out.
3. Compare your number with the white pixel. Press **Button 1** if your number is higher. Press **Button 2** if your number is lower or equal.
4. Watch the blue range shrink. Keep answering until only one pixel is left. It flashes green four times, and then a new round starts.

!!! warning "Heads up"
    If the white pixel is exactly your number, press Button 2. The program does not ask "Is that right?" It keeps narrowing the range until one pixel is left. Button 2 keeps your number safely inside the range.

## How it works

### Draw the range

This function paints the strip for the current guess.

```python
def draw_range(low, high, guess):
    for i in range(NUMBER_PIXELS):
        if i == guess:
            strip[i] = (255, 255, 255)   # current guess: white
        elif low <= i <= high:
            strip[i] = (0, 0, 80)        # still in range: dim blue
        else:
            strip[i] = (0, 0, 0)         # ruled out: off
    strip.write()
```

The test `low <= i <= high` asks, "Is `i` between `low` and `high`?" The guess is white. Pixels in the range are dim blue. Every other pixel is off.

### Wait for an answer

A **function** is a named block of code that you can run whenever you need it. This function waits until you press a button.

```python
def wait_for_button():
    while True:
        if button1.value() == 0:
            return "higher"
        if button2.value() == 0:
            return "lower"
        sleep(0.01)
```

The loop checks both buttons, then waits 0.01 seconds, then checks again. That is about 100 checks every second. Checking over and over like this is called **polling**. (Lab 47 uses interrupts instead.) A pressed button reads `0`. When one reads `0`, `return` sends back the word `"higher"` or `"lower"` and ends the function.

### Wait for the button to come back up

This second function waits until you let go.

```python
def wait_for_release():
    while button1.value() == 0 or button2.value() == 0:
        sleep(0.01)
```

The loop keeps waiting while either button is still down. This matters because the Pico is much faster than your finger. Without this wait, one press could answer several guesses in a row.

### Start a round

`low` and `high` are the two ends of the range where your number could be.

```python
    low, high = 0, NUMBER_PIXELS - 1
    guesses = 0

    while low < high:
        guess = (low + high) // 2
```

The first line sets `low` to 0 and `high` to 29 in one step. The guess is the middle of the range. The `//` symbol divides and drops any leftover, so `(0 + 29) // 2` is `14`. The loop `while low < high` keeps going while more than one pixel is possible.

### Shrink the range

Your answer decides which half of the range to keep.

```python
        if answer == "higher":
            low = guess + 1
        else:
            high = guess
```

If your number is higher, the guess and every pixel below it are ruled out, so `low` moves up to `guess + 1`. Otherwise your number is lower or equal, so it is the guess or something below it. Then `high` drops to `guess`. Either way, about half the pixels disappear.

Here is a round where the secret number is 20.

| Guess | Range before | Guess pixel | You press | Range after |
|:-----:|:------------:|:-----------:|:---------:|:-----------:|
| 1 | 0 to 29 | 14 | Button 1 (higher) | 15 to 29 |
| 2 | 15 to 29 | 22 | Button 2 (lower) | 15 to 22 |
| 3 | 15 to 22 | 18 | Button 1 (higher) | 19 to 22 |
| 4 | 19 to 22 | 20 | Button 2 (equal) | 19 to 20 |
| 5 | 19 to 20 | 19 | Button 1 (higher) | 20 to 20 |

Now `low` and `high` are both 20, so the loop stops. The strip found the number in 5 guesses.

### Why halving is so fast

Each guess throws away about half of the pixels that are left. In the worst case, the number of possible pixels goes 30, then 15, then 8, then 4, then 2, then 1. That is at most 5 guesses.

Guessing 0, then 1, then 2, and so on could take up to 30 guesses. Halving wins by a lot. It also grows slowly. Doubling the pixels adds only one more guess. A 60-pixel strip needs at most 6 guesses. A strip of 1,000 pixels needs at most 10.

### Found it

When the loop ends, only one pixel is left. The program shows it and prints a message.

```python
    draw_range(low, high, low)
    print("Found it! Your number was", low, "in", guesses, "guesses")
```

Then the found pixel flashes green.

```python
    for _ in range(4):
        strip[low] = (0, 255, 0)
        strip.write()
        sleep(0.2)
        strip[low] = (0, 0, 0)
        strip.write()
        sleep(0.2)
```

The pixel is on for 0.2 seconds and off for 0.2 seconds, four times. After a one-second pause, the outer `while True:` starts a new round. This program keeps running until you press **Stop**.

## Try it yourself

1. Make the win flash longer and a different color. Change `range(4)` to `range(10)`. Then change `(0, 255, 0)` to `(255, 0, 255)`.
2. Play five rounds with the secret numbers 0, 14, 15, 29, and one of your choice. The Shell prints each guess and the total. Most numbers take five guesses. Which of yours took only four?

## Check your understanding

1. Why does the program guess `(low + high) // 2` instead of counting 0, 1, 2, and so on?
2. What does it mean when `low` and `high` become equal?
3. Your number is exactly the white pixel. Which button do you press, and why?
4. What might go wrong if `wait_for_release()` were missing?
5. About how many guesses would a 60-pixel strip need in the worst case? (Hint: doubling the pixels adds one guess.)

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built one of the most famous recipes in computer science, and you can play it with your own two buttons! Cutting the possibilities in half is a trick real programs use every day.

**What's next:** In [Lab 47: Buttons Move a Light](47-buttons-move-light.md), the buttons take control of a lit pixel.
