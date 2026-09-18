# Lab 34: Two Buttons

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Two buttons, one counter, and a very quick listener! Today a button gets to tap your program on the shoulder the instant you press it. Let's light this up!

**Program file:** [`34-two-button-print.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/34-two-button-print.py)

## What you'll learn

- How an interrupt catches a button press the instant it happens
- How `irq()` connects a button to a handler function
- Why buttons need debouncing, and how a time check does it
- How `global` lets a function change a variable outside itself

## What you'll need

- Your base kit: a Pico, a breadboard, and both push buttons wired as shown in [The Two Buttons](../kits/moving-rainbow-base/index.md#the-two-buttons). Button 1 is `GP15` (pin 20) and Button 2 is `GP14` (pin 19).
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

This lab builds on [Lab 32](32-button-test.md) and [Lab 33](33-button-led-test.md). It does not use the LED strip.

## The program

This program keeps a running count. Button 2 adds one, Button 1 subtracts one, and the Shell shows the new count each time it changes. The idea comes from a sample at [coderdojotc.org](https://www.coderdojotc.org/micropython/basics/03-button/).

```python title="34-two-button-print.py"
--8<-- "src/kits/moving-rainbow-base/34-two-button-print.py"
```

Run it. The Shell starts with `0`. Press Button 2 a few times and the count climbs. Press Button 1 and the count falls, even below zero. The built-in LED flips on or off each time the count changes.

## How it works

### Polling or interrupts

Labs 32 and 33 used polling: the loop asked the button "Are you pressed?" over and over. A very quick tap can slip in between two questions.

An **interrupt** works the other way around. The button taps the Pico on the shoulder. The Pico stops what it is doing and runs a function called a **handler** right away. Then it goes back to its work.

Think of checking a mailbox every five seconds, compared with a mailbox that rings a bell when mail arrives.

### Give the buttons names

```python
BUTTON_PIN_A = BUTTON_PIN_2
BUTTON_PIN_B = BUTTON_PIN_1
```

`BUTTON_PIN_A` holds Button 2's pin, and `BUTTON_PIN_B` holds Button 1's pin. The count goes up for button A, so Button 2 adds one and Button 1 subtracts one.

!!! warning "Heads up"
    In Labs 35 and 36, Button 1 moves forward or speeds up. Here Button 1 subtracts, so watch which button does what.

The next two lines set up the buttons with pull-ups, as in Lab 32. A released button reads `1` and a pressed button reads `0`.

```python
button_a = Pin(BUTTON_PIN_A, Pin.IN, Pin.PULL_UP)
button_b = Pin(BUTTON_PIN_B, Pin.IN, Pin.PULL_UP)
```

!!! bug "Known issue"
    A comment above these lines says a button wire goes to the "3.3 rail". That comment is out of date. With `Pin.PULL_UP`, the other side of each button goes to the ground rail, as shown in the kit guide.

### The handler

The handler is the function the Pico runs when a button is pressed.

```python
def button_callback(pin):
    global button_presses, last_time
    new_time = utime.ticks_ms()
    # if it has been more that 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
```

The handler receives one **parameter** (a value handed to a function) named `pin`. Python fills it in with the button that was pressed.

The line `global button_presses, last_time` names two variables that live outside the function. These are **global** variables. Without `global`, Python would make new variables inside the function. They would vanish when the function ends, and the main loop would not see the new count.

The call `utime.ticks_ms()` gives a clock in **milliseconds** (thousandths of a second) that counts up from when the Pico started. Subtracting `last_time` tells us how long ago the last counted press happened.

### Debounce the press

A button does not switch cleanly. Its metal contacts bounce: they touch, separate, and touch again in a few thousandths of a second. One press can look like many.

**Debouncing** means ignoring extra presses that arrive too soon after the first. This handler counts a press only if more than 200 milliseconds (one fifth of a second) have passed since the last counted press.

Both buttons share one `last_time`. Pressing the second button within 200 milliseconds of the first is ignored too.

### Add or subtract

If the time check passes, the handler changes the count.

```python
        if pin == button_a:
            button_presses +=1
        else:
            button_presses -= 1
        last_time = new_time
```

If `pin` is `button_a`, the handler adds one. Otherwise it must be `button_b`, so it subtracts one. The `+=` sign is shorthand for "add to itself". Then `last_time` remembers when this press happened.

!!! info "Key idea"
    A handler should get in and out quickly. While it runs, the Pico pauses its main program. This handler only changes numbers. It leaves the printing to the main loop.

### Connect the handler to the buttons

```python
button_a.irq(trigger=Pin.IRQ_FALLING, handler = button_callback)
button_b.irq(trigger=Pin.IRQ_FALLING, handler = button_callback)
```

The `irq()` method sets up an interrupt. The name is short for "interrupt request". `Pin.IRQ_FALLING` means "fire when the pin's value falls from `1` to `0`". With a pull-up, that is the instant of a press.

The `handler = button_callback` part names the function to run. Both buttons share one handler, and that is why the handler checks `pin`.

### The main loop

The main loop watches the count and reports changes.

```python
while True:
    # only print on change in the button_presses value
    if button_presses != old_presses:
        print(button_presses)
        builtin_led.toggle()
        old_presses = button_presses
```

The `toggle()` method flips the LED: on becomes off, and off becomes on. Each change in the count gives you a blink of feedback. Right before the loop, `print(button_presses)` shows the starting `0`.

The built-in LED uses pin 25, as in Lab 33. On a Pico W, use `Pin("LED", Pin.OUT)` instead.

For more about bounce and debouncing, see [Chapter 18: Input Devices and Sensors](../chapters/18-input-devices-and-sensors/index.md).

## Try it yourself

1. Change the `200` in `if (new_time - last_time) > 200:` to `0`. Press a button slowly, one time. Does the count ever jump by more than one? Then try `50` and `500`.
2. Make Button 1 add and Button 2 subtract. Change the two lines that name the buttons to this:

```python title="Your change"
BUTTON_PIN_A = BUTTON_PIN_1
BUTTON_PIN_B = BUTTON_PIN_2
```

## Check your understanding

1. What is the difference between polling and an interrupt?
2. Why does the handler need the line `global button_presses, last_time`?
3. What does the `200` do in the handler? What problem does it solve?
4. In this program, which button adds one and which button subtracts one?
5. Why does the handler only change numbers and leave the printing to the main loop?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You caught a button press the instant it happened! Interrupts and debouncing make buttons feel fast and reliable.

**What's next:** In [Lab 35: Button Change Color](35-button-change-color.md), the same interrupt pattern changes the color of the whole LED strip.
