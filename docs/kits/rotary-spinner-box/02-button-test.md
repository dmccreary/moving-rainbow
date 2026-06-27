# Lab 2: Test the Buttons

This program makes your code react to *you*. Each time you press a button on
your box, the Pico prints a message to the screen. You'll learn how a chip
notices a press the very moment it happens.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Up until now, your code did all the talking. Now it's your turn to talk
    back! When you press a button, the chip listens and answers. This is how
    every game controller and remote in the world works. Let's light this up!

## What You'll Learn

By the end of this lab, you'll be able to:

- Read a button using a **pull-up resistor**
- Use an **interrupt** so the chip notices a press right away
- Add a **debounce** so one press counts as one press
- Print messages to the **console** (the screen in Thonny)
- Explain what an **event** is in a program

## What You'll Need

- Your Rotary Spinner Box with the two push buttons
- A USB cable to connect the box to your computer
- The Thonny program open on your computer

You do **not** need the LED strip or the knob for this lab.

## What Is an Event?

So far your code ran from top to bottom on its own. An **event** is something
that happens *outside* your code, like a button press. Code that waits for
events and reacts to them is the heart of every app you use.

This program watches two buttons. **Button 1** is on GPIO pin 14. **Button 2**
is on GPIO pin 15. A **GPIO pin** is one of the metal connection points on the
chip that we can read or control.

## Setting Up the Buttons

First the program brings in its tools and reads the pin numbers from the
`config.py` file. That file holds settings for your kit.

```python
import utime
import machine
from machine import Pin

import config
```

This loads the tools we need and our pin settings. You won't see anything on
screen yet.

Next we set up each button as an **input** with a **pull-up resistor**.

```python
# Set up both buttons as inputs with internal pull-up resistors
button_1 = machine.Pin(config.PUSH_BUTTON_PIN_1, machine.Pin.IN, machine.Pin.PULL_UP)
button_2 = machine.Pin(config.PUSH_BUTTON_PIN_2, machine.Pin.IN, machine.Pin.PULL_UP)
```

This tells the chip to read these pins instead of powering them. The pin reads
`1` when the button is up and `0` when you press it down.

!!! info "Pixel thinks..."
    <img src="../../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    Why a pull-up resistor? A loose pin is like a light switch with no wall
    behind it — it floats between on and off. The pull-up gently holds the pin
    at `1` (up) until you press the button, which pulls it to `0` (down). Now
    the chip always knows where the button stands.

## Reacting the Instant You Press

The chip could check the buttons over and over in a loop. Instead, this program
uses an **interrupt**. An interrupt is a way to tell the chip, "stop what you're
doing and run this code the moment a button is pressed."

```python
# Register the handler for the falling edge (button press) of each button
button_1.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)
button_2.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)
```

These lines connect each button to a function called `button_callback`. The
**falling edge** is the moment the pin drops from `1` to `0` — that's the press.

Here is the function that runs on every press. It adds one to a counter and
prints a message.

```python
def button_callback(pin):
    global button_1_count, button_2_count, last_time
    new_time = utime.ticks_ms()
    # only act if it has been more than 200ms since the last event
    if utime.ticks_diff(new_time, last_time) > 200:
        if pin is button_1:
            button_1_count += 1
            print('BUTTON 1 pressed (pin', config.PUSH_BUTTON_PIN_1,
                  ') - count:', button_1_count)
        else:
            button_2_count += 1
            print('BUTTON 2 pressed (pin', config.PUSH_BUTTON_PIN_2,
                  ') - count:', button_2_count)
        builtin_led.toggle()
        last_time = new_time
```

When you press a button, you'll see a line like `BUTTON 1 pressed (pin 14 ) -
count: 1` appear in the console.

## The Debounce: One Press, One Count

A button is a tiny piece of metal. When you press it, the metal can bounce for
a few milliseconds. The chip is so fast that it might count one press as three
or four! That extra counting is a real puzzle to solve.

The fix is a **debounce**. We check the clock with `utime.ticks_ms()`, which
counts milliseconds. If less than 200 milliseconds have passed since the last
press, we ignore it. That's what this line does:

```python
    if utime.ticks_diff(new_time, last_time) > 200:
```

With the debounce, one press counts once. Without it, the count would jump up
too fast.

!!! warning "Watch out!"
    <img src="../../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    If your count goes up by 2 or 3 on a single press, the bounce is sneaking
    through. That's a puzzle to solve, not a failure! Try making the `200` a
    bigger number, like `300`, to give the metal more time to settle.

## Running the Main Loop

The interrupts do all the work, so the main loop has almost nothing to do. It
waits one second, over and over.

```python
while True:
    utime.sleep(1)
```

The program seems to sit still, but it's wide awake. Press a button and a
message pops up right away.

## Try It Yourself

1. **Watch the count climb.** Press Button 1 five times. Does the count reach
   `5`? Now press fast — does it still match?
2. **Change the debounce.** Change `200` to `50`. Press fast and see if the
   count jumps by more than one. Then change it to `400`.
3. **Add your own message.** Inside the Button 2 part, add a new line:
   `print('Nice press!')`. Now you get two messages each time.

## Check Your Understanding

1. What is an **event** in a program?
2. What does a **pull-up resistor** do to the button pin?
3. Why do we use an **interrupt** instead of checking in a loop?
4. What problem does the **debounce** solve?
5. Does the pin read `1` or `0` when you press the button down?

!!! success "Chapter complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You taught your code to listen! Buttons, interrupts, and debouncing show up
    in everything from elevators to video games. Every bug you chase along the
    way is just a puzzle in disguise. You're already glowing!

## What's Next

In [Lab 3: Test the Knob](03-rotary-test.md), you'll read the spinning knob and
turn it into numbers your code can use.
