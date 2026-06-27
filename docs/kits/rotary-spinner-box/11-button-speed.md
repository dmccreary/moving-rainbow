# Lab 11: Button Speed

In this lab, you'll run the bouncing dot from Lab 5 again. A small dot of
light slides back and forth along the strip. This time, your two buttons
control how fast the dot moves. The trick is that the animation never stops
to wait for a button. The buttons work in the background.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    This one is my favorite kind of magic. The light keeps zipping along, and
    the moment you press a button, the speed changes. The animation never
    pauses to listen for you. It can do both at once! Let's light this up!

## What You'll Learn

By the end of this lab, you'll be able to:

- Explain what an **interrupt** is and why it helps
- Use a **callback** that runs the instant a button is pressed
- Share one **variable** between the callback and the main loop
- Describe how a smaller delay makes the dot move faster
- **Clamp** a value so it stays between a low and a high limit

## What You'll Need

- Your Rotary Spinner Box with the 12-pixel strip
- The two push buttons on the box
- A USB cable to connect the box to your computer
- The Thonny program open on your computer

You do **not** need the knob for this lab.

## The Problem With Waiting

Think about the bouncing dot. The main loop is busy. It turns pixels off,
lights one pixel, and waits a moment before moving the dot. That waiting is
the animation's heartbeat.

So how can the code also watch the buttons? If the loop stopped to check the
buttons, the dot would freeze. We need a way to react to a button **without
waiting** for it.

The answer is an **interrupt**. An interrupt is a signal that pauses the main
code for a split second, runs a small piece of code, and then lets the main
code pick up right where it left off.

## Setting Up the Interrupt

First the program imports its tools and builds the strip. It also picks a
color and sets the starting speed.

```python
from neopixel import NeoPixel
import utime
import machine
from machine import Pin

import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

DOT_COLOR = (0, 60, 80)

# The speed parameter is the delay between steps, in seconds.
# A SMALLER delay means a FASTER spinner.
delay = 0.08
MIN_DELAY = 0.01
MAX_DELAY = 0.30
```

When this runs, nothing lights up yet. The program is getting its pieces ready.

The **speed** is really the `delay` — the wait between each step. A small wait
means the dot jumps to its next spot quickly, so it looks fast. A big wait
means the dot moves slowly. `MIN_DELAY` and `MAX_DELAY` are the fastest and
slowest speeds we will allow.

Next the program sets up the two buttons. Each button uses a **pull-up
resistor** (a tiny part inside the chip that keeps the pin "high" until you
press the button).

```python
# Buttons with internal pull-up resistors
button_faster = machine.Pin(config.PUSH_BUTTON_PIN_1, machine.Pin.IN, machine.Pin.PULL_UP)
button_slower = machine.Pin(config.PUSH_BUTTON_PIN_2, machine.Pin.IN, machine.Pin.PULL_UP)
```

Button 1 lives on pin 14 and means "faster." Button 2 lives on pin 15 and
means "slower." Nothing happens on screen yet.

## The Callback Runs in the Background

A **callback** is a function that the chip runs for you at the right moment.
We do not call it ourselves. The chip calls it the instant a button is pressed.

```python
def button_callback(pin):
    global delay, last_time
    new_time = utime.ticks_ms()
    if utime.ticks_diff(new_time, last_time) > 200:
        if pin is button_faster:
            # faster means a smaller delay
            delay = max(delay - 0.01, MIN_DELAY)
        else:
            # slower means a bigger delay
            delay = min(delay + 0.01, MAX_DELAY)
        print('delay:', round(delay, 3), 'seconds')
        last_time = new_time
```

When you press a button, this code changes `delay` and then ends right away.

The word `global` is important. It tells the callback to change the **same**
`delay` that the main loop reads. The callback and the loop share one variable.
The callback writes to it, and the loop reads from it. That is how a button
press in the background can speed up the dot in front of you.

!!! info "Pixel thinks..."
    <img src="../../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    The `ticks_ms` and `200` lines are a little timer. A button can "bounce"
    and fire many times in one press. This timer ignores any extra signals
    that come within 200 milliseconds. It keeps one press from counting twice.

## Clamping the Speed

Look closely at the two speed lines. They use `max` and `min` to keep the
delay inside its limits. This is called **clamping** — holding a value between
a low and a high edge.

```python
delay = max(delay - 0.01, MIN_DELAY)   # never faster than MIN_DELAY
delay = min(delay + 0.01, MAX_DELAY)   # never slower than MAX_DELAY
```

After this runs, the delay always stays between `0.01` and `0.30` seconds.

`max(delay - 0.01, MIN_DELAY)` picks the larger of the two numbers. So the
delay can shrink, but never below `MIN_DELAY`. The dot has a top speed. The
same idea with `min` gives the dot a slowest speed. Clamping keeps the
animation smooth and safe.

## Connecting the Buttons to the Callback

This pair of lines is the connection. It tells the chip to run our callback
whenever a button is pressed down.

```python
button_faster.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)
button_slower.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_callback)
```

After this, both buttons are armed and listening on their own.

The word `irq` stands for **interrupt request**. `IRQ_FALLING` means "run the
callback the moment the pin falls from high to low" — which happens when you
press the button. From now on, you can press a button any time.

## The Main Loop Keeps Animating

Here is the loop that never stops. It draws the bouncing dot and waits the
current `delay`.

```python
while True:
    # turn every pixel off, then light only the current one
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip[position] = DOT_COLOR
    strip.write()
    utime.sleep(delay)

    # bounce off the ends instead of jumping back to the start
    if position == 0:
        direction = 1
    elif position == config.NUMBER_PIXELS - 1:
        direction = -1
    position = position + direction
```

You see one bright dot slide along the strip, then turn around at each end.

Each time around, the loop reads `delay`. If you pressed a button, the value
is different now, so the dot speeds up or slows down. The dot **bounces**
because your strip is a straight line of 12 pixels, not a ring. When the dot
reaches an end, `direction` flips and the dot heads back the other way.

!!! warning "Watch out!"
    <img src="../../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    Press the "faster" button many times and the dot may move so quickly it
    looks like the whole strip is glowing. That's the `MIN_DELAY` limit doing
    its job. Press the "slower" button to bring the dot back into view.

## Try It Yourself

1. **Bigger steps.** Change both `0.01` step amounts to `0.05`. Now each press
   changes the speed by a larger jump. Does the speed feel easier or harder to
   control?
2. **A faster top speed.** Lower `MIN_DELAY` from `0.01` to `0.005`. How fast
   can the dot go now?
3. **A slower floor.** Raise `MAX_DELAY` from `0.30` to `0.60`. Press "slower"
   until the dot crawls. Can you still see it move?

## Check Your Understanding

1. What does an interrupt let your code do while the animation keeps running?
2. Which variable do the callback and the main loop share?
3. Does a smaller `delay` make the dot faster or slower?
4. What does clamping with `max` and `min` keep the delay between?
5. Why does the dot bounce instead of going around in a circle?

!!! success "Chapter complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You taught your box to do two things at once! The dot keeps dancing while
    your buttons quietly change its speed in the background. Interrupts are a
    huge idea in real computers, and now you've used one. You're glowing!

## What's Next

In [Lab 12: The Mode Machine](20-mode-machine.md), you'll use your buttons to
switch between whole light shows, not just change one speed.
