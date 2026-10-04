# Lab 3: Button Test

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Buttons are how you talk back to your program. Let's find out how a press looks to the Pico!

**Program file:** [`03-button-test.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/16x16-matrixs-accel/03-button-test.py)

## What you'll learn

- Why a button reads 0 when you press it
- How `button.value()` reads a pin
- How to notice a *change* by remembering the last value
- How to use `if` to print a message only when something happens

## What you'll need

- Your kit, with the buttons wired to GP14 and GP15 as shown in the [Kit Guide](index.md#step-4-wire-the-two-buttons)
- The matrix wired to GP0 (the corner pixels light up when you press)
- `config.py` saved on the Pico
- Thonny open and connected to your Pico

## The program

This program prints a message each time you press or let go of a button. It also lights a pixel in the top row while you hold a button down.

```python title="03-button-test.py"
--8<-- "src/kits/16x16-matrixs-accel/03-button-test.py"
```

Run it and press each button a few times. The Shell shows a message for every press and release. Button 1 lights the first pixel green while you hold it. Button 2 lights the last pixel of the top row blue.

```text
Test 03: Button Test (version 1.0.0)
Press each button. Press Ctrl-C to stop.
Button 1 (GP14): pressed
Button 1 (GP14): released
Button 2 (GP15): pressed
Button 2 (GP15): released
```

## How it works

### Pressed means zero

```python
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
```

`Pin.IN` means this pin listens instead of sending. `Pin.PULL_UP` turns on a tiny spring-like resistor inside the Pico. It pulls the pin up to 3.3 volts, so an untouched pin reads **1**. Your button connects the pin to ground. When you press, the pin drops to **0**.

That feels backwards, so say it out loud once: **pressed means zero.**

### Remember the last value

```python
last1 = 1
last2 = 1
```

To notice a *change*, the program needs to remember what the button said last time. Both buttons start at 1, which means not pressed.

### Spot a change

```python
now1 = button1.value()
now2 = button2.value()
if now1 != last1:
    print("Button 1 (GP%d):" % BUTTON_PIN_1, "pressed" if now1 == 0 else "released")
    last1 = now1
```

`button1.value()` reads the pin right now. The `!=` sign means "is not equal to". So the line `if now1 != last1:` asks a question. It asks, did the button change since last time? If yes, we print a message. The last part, `"pressed" if now1 == 0 else "released"`, picks the word: 0 means pressed, and anything else means released.

Then `last1 = now1` saves the new value for the next time around the loop.

### Light a pixel

```python
strip[PIXEL_1] = (0, 20, 0) if now1 == 0 else (0, 0, 0)
strip.write()
```

A color is three numbers: red, green, and blue, from 0 to 255. The color `(0, 20, 0)` is a dim green. The color `(0, 0, 0)` is off. Each trip through the loop picks the color from the button, then `strip.write()` sends it to the matrix.

!!! info "Key idea"
    Reading a button over and over, and comparing it with the last reading, is how a program notices a press. Every game controller does something like this.

## Try it yourself

1. Change the color of Button 1's pixel from green to red. Which of the three numbers do you change?
2. Press both buttons at the same time. What do you see in the Shell? What do you see on the matrix?
3. Hold a button down and watch the Shell. Does it print over and over, or just once? Why?

## Check your understanding

1. What does a button read when nobody is pressing it? What does it read when you press?
2. What does `Pin.PULL_UP` do?
3. Why does the program keep the variables `last1` and `last2`?
4. What does the `!=` sign mean?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    Your buttons work! Now your kit can listen as well as shine.

**What's next:** In [Lab 4: First Pixel](04-first-pixel.md), you will light one pixel in three colors.
