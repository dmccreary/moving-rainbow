# Binary Search Visualizer

This is the final lesson in the book, and it ties everything together:
buttons, algorithms, and a classic party trick. Think of a pixel number in
your head. Your Pico will find it in just a few guesses — no matter which
number you pick.

!!! tip "Pixel says..."
    This one always gets a reaction the first time you try it. Thirty
    pixels, and I'll never need more than five guesses. Let's light this up!

## What you'll learn

- What **binary search** is and why it's so much faster than guessing one at a time
- How to narrow a range using a `low` and `high` boundary
- Why halving the search space each time finds an answer in very few steps
- How to combine buttons, printing, and an algorithm into one finished project

## What you'll need

- Your Pico, NeoPixel strip, and two buttons from the earlier lessons
- The kit's `config.py` file

## Guess the Middle, Every Time

Instead of guessing pixel 0, then 1, then 2, and so on, **binary search**
always guesses the *middle* of whatever range is left. You answer
"higher" or "lower," and the program throws away half the remaining
pixels every single guess:

```python
guess = (low + high) // 2
```

With 30 pixels, guessing one at a time could take up to 30 tries. Cutting
the range in half each time takes at most 5.

## The Full Program

```python
# Binary Search: think of a pixel number from 0 to NUMBER_PIXELS-1 in
# your head. Press Button 1 if your number is HIGHER than the lit pixel.
# Press Button 2 if it's LOWER than or equal to the lit pixel. Watch how
# few guesses it takes to find your number!
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

n = config.NUMBER_PIXELS


def draw_range(low, high, guess):
    for i in range(n):
        if i == guess:
            strip[i] = (255, 255, 255)   # current guess: white
        elif low <= i <= high:
            strip[i] = (0, 0, 80)        # still in range: dim blue
        else:
            strip[i] = (0, 0, 0)         # ruled out: off
    strip.write()


def wait_for_button():
    while True:
        if button1.value() == 0:
            return "higher"
        if button2.value() == 0:
            return "lower"
        sleep(0.01)


def wait_for_release():
    while button1.value() == 0 or button2.value() == 0:
        sleep(0.01)


while True:
    print("Think of a pixel number from 0 to", n - 1)
    sleep(2)

    low, high = 0, n - 1
    guesses = 0

    while low < high:
        guess = (low + high) // 2
        draw_range(low, high, guess)
        guesses += 1
        print("Guess", guesses, "-> pixel", guess)

        answer = wait_for_button()
        wait_for_release()

        if answer == "higher":
            low = guess + 1
        else:
            high = guess

    draw_range(low, high, low)
    print("Found it! Your number was", low, "in", guesses, "guesses")

    for _ in range(4):
        strip[low] = (0, 255, 0)
        strip.write()
        sleep(0.2)
        strip[low] = (0, 0, 0)
        strip.write()
        sleep(0.2)

    sleep(1)
```

Pick a pixel number in your head, then answer honestly each time the
strip lights up a white "guess" pixel: Button 1 if your number is higher,
Button 2 if it's lower or exactly that pixel. Watch the dim blue range get
smaller every round until only one pixel is left — yours.

!!! info "Pixel thinks..."
    Notice the loop condition: `while low < high`. The moment `low` and
    `high` meet, there's only one possible pixel left — no more guessing
    needed. That's the algorithm finishing itself, not a special case you
    had to write.

## Try It Yourself

- Print how many guesses binary search *should* take at most for 30
  pixels, using the idea from the intro. Does your game match it?
- Change the game so it searches for a *color* instead of a pixel position.

## Check Your Understanding

1. Why does the program always guess `(low + high) // 2` instead of just counting up from 0?
2. What does it mean when `low` and `high` become equal?
3. At most, how many guesses should this take for a 30-pixel strip? For a 1,000-pixel strip?
4. How is this lesson connected to the Sorting Visualizer lesson before it?

!!! success "You've got this!"
    You just built binary search — one of the most important algorithms
    in computer science — and used your own buttons to run it live. That's
    a genuinely huge accomplishment. You've come a long way from a single
    blinking LED!

**What's next:** you've reached the end of the built-in lessons. Try
combining ideas from different lessons — a fire effect with a button-controlled
speed, or a traffic light with a binary-counter timer — and build something
that's entirely your own.
