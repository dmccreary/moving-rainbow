# Lab 5: Button Test

Your costume has one button. This program shows what the Pico sees when you press it.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Now your costume can listen to you! Press the button and watch the numbers change.

**Program file:** [`05-button-test.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/05-button-test.py)

## What You'll Learn

- Read a button with `button.value()`
- Learn why a pressed button reads 0
- Use an `if` statement to make a choice

## What You'll Need

- Your costume with the button wired from GPIO 15 to GND
- Thonny open so you can see the Shell

## The Program

This program prints the button's value ten times a second and lights the onboard LED while you press.

```python
--8<-- "src/kits/halloween-60-button/05-button-test.py"
```

The Shell shows a column of 1s. Press the button and you see 0s, and the onboard LED lights up.

## How It Works

The button connects GPIO 15 to GND (ground). `Pin.PULL_UP` holds the pin at 1 when the button is up. Pressing the button connects it to ground, so it reads 0.

`if value == 0:` checks for a press. The `else:` part runs when the button is not pressed.

## Try It Yourself

1. Print the word `pressed` instead of the number when the button is down.
2. Count how many times the button was pressed and print the count.

## Check Your Understanding

1. What value does the button have when you press it?
2. What does `Pin.PULL_UP` do?
3. Which pin is the button on?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 6: Orange and Purple Chase](06-orange-and-purple-chase.md).
