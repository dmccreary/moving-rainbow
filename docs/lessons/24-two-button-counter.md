# Two Buttons and Interrupts

So far your loop has checked the button over and over, as fast as it can.
That's called **polling**. In this lesson you'll wire a second button and
meet a different approach: **interrupts**, which tell your code the
instant a button is pressed.

!!! tip "Pixel says..."
    Polling is like checking the mailbox every five seconds. An interrupt
    is like the mailbox ringing a bell the moment mail arrives. Both work
    — but interrupts never miss a fast press!

## What you'll learn

- The difference between polling and interrupts
- How to wire a second button
- How to use `irq()` to run code automatically on a button press
- Why buttons need **debouncing**, and how a simple time check fixes it

## What you'll need

- Your Pico and Button 1 from the last two lessons
- A second momentary push button
- Two more jumper wires
- The kit's `config.py` file

## Wiring the Second Button

Wire Button 2 the same way you wired Button 1: corner to opposite corner,
one leg to `config.BUTTON_PIN_2` (GPIO 14) and the other to GND.

## Interrupts: irq()

An **interrupt** is a way of telling the Pico, "run this function the
instant this pin changes — don't wait for the main loop to get around to
checking it." You set one up with `irq()`:

```python
button1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
```

`IRQ_FALLING` means "trigger when the pin drops from `1` to `0`" — exactly
the moment a pull-up button gets pressed. `button_handler` is a function
you write that runs automatically when that happens.

## Button Bounce and Debouncing

A physical button doesn't switch cleanly. For a few thousandths of a
second, the metal contacts inside bounce and touch several times. Without
protection, one press can be counted as two, three, or more.

**Debouncing** fixes this by ignoring any press that happens too soon
after the last one. This lesson uses a simple time check for that — see
[Chapter 18](../chapters/18-input-devices-and-sensors/index.md) if you
want the full explanation of how software debouncing works.

## Counting Two Buttons

This program counts presses on each button separately, using an interrupt
for each one.

```python
# Count presses on two buttons using interrupts, with debouncing.
from machine import Pin
from utime import ticks_ms
import config

button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

button1_presses = 0
button2_presses = 0
DEBOUNCE_MS = 200
last_press = 0


def button_handler(pin):
    global button1_presses, button2_presses, last_press
    now = ticks_ms()
    if now - last_press < DEBOUNCE_MS:
        return   # too soon - this is probably bounce, not a new press

    # pin tells us which button object triggered the interrupt
    if pin == button1:
        button1_presses += 1
    else:
        button2_presses += 1

    last_press = now
    print("button 1:", button1_presses, " button 2:", button2_presses)


button1.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

while True:
    pass   # the buttons do all the work through interrupts
```

Press each button a few times. The Shell should print an accurate count
for each one — even if you press quickly.

!!! warning "Watch out!"
    Notice the main loop is just `while True: pass`. It looks like it does
    nothing, and that's the point — the real work happens in
    `button_handler`, which the Pico runs automatically whenever an
    interrupt fires.

You'll find this same idea saved in your kit as
[`32-two-button-print.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/led-strip-two-buttons/32-two-button-print.py).

## Try It Yourself

- Change `DEBOUNCE_MS` to `10`. Do you start seeing double-counted presses?
- Add a third variable that tracks the *total* number of presses on both buttons combined.

## Check Your Understanding

1. What is the difference between polling and an interrupt?
2. What does `IRQ_FALLING` mean for a pull-up button?
3. Why do we need debouncing at all?
4. In the code, how does `button_handler` know which button was pressed?

!!! success "You've got this!"
    Interrupts are a big step up — you'll use this exact pattern for
    every button-controlled project from here on, including the LED
    strip itself.

**What's next:** in [Button-Controlled Color](25-button-change-color.md),
you'll use these two buttons to cycle the whole LED strip through a list
of colors.
