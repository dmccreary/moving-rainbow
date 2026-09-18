# Lab 32: Button Test

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    So far, your programs have only talked to the lights. Now we'll teach the Pico to listen! A button lets you talk back.

**Program file:** [`32-button-test.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/32-button-test.py)

## What you'll learn

- How a push button connects to the Pico with two wires
- What `Pin.PULL_UP` does, and why a pressed button reads `0`
- How to read a pin with `button.value()`
- How to watch a stream of numbers in the Thonny Shell

## What you'll need

- Your base kit: a Pico, a breadboard, and a push button wired as shown in [The Two Buttons](../kits/moving-rainbow-base/index.md#the-two-buttons). This lab uses Button 1 only.
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

This lab does not use the LED strip, so it can stay plugged in or come out.

## The program

This program reads Button 1 ten times every second and prints what it finds.

```python title="32-button-test.py"
--8<-- "src/kits/moving-rainbow-base/32-button-test.py"
```

Run it and look at the Thonny **Shell** (the panel at the bottom where `print()` shows its text). While you leave the button alone, a stream of `1`s scrolls by. Hold the button down and the stream turns into `0`s. Let go, and the `1`s come back.

## How it works

### Wire the button

A **push button** connects two wires only while you hold it down. When you let go, a spring breaks the connection.

| One side goes to | The other side goes to |
|------------------|------------------------|
| `GP15` (pin 20) | The ground rail |

Your button has four legs, but they are really two pairs that are joined inside. Wire from one corner to the opposite corner, and you always reach one leg from each pair. The kit guide shows the full picture in [The Two Buttons](../kits/moving-rainbow-base/index.md#the-two-buttons).

### Set up the pin

```python
button = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
```

This line makes a `button` object on the pin number from `config.py`. `Pin.IN` makes the pin an **input**, which means it listens instead of sending.

`Pin.PULL_UP` turns on the Pico's **internal pull-up resistor**. This is a tiny resistor inside the chip that holds the pin at 3.3 volts until something pulls it lower. That is why the breadboard needs no resistor.

### Pressed means zero

| Button | What the pin connects to | `button.value()` |
|--------|--------------------------|------------------|
| Released | 3.3 volts (pulled up) | `1` |
| Pressed | Ground (0 volts) | `0` |

!!! info "Key idea"
    This feels backwards, so say it out loud once: **pressed means zero**. Pressing the button connects the pin to ground, and that pulls the `1` down to `0`.

### Read, print, repeat

```python
while True:
    print(button.value())
    time.sleep(0.1) # wait 1/10th of a second
```

`button.value()` asks the pin for its value right now. `print()` shows that value in the Shell. The `time.sleep(0.1)` line waits a tenth of a second, so the loop runs about ten times every second. Without the wait, the numbers would scroll by too fast to read.

Checking a button again and again in a loop is called **polling**. It works well for a first test. In [Lab 34](34-two-button-print.md), you'll meet a faster way to catch a press.

[Chapter 18: Input Devices and Sensors](../chapters/18-input-devices-and-sensors/index.md) goes deeper on buttons, pull-ups, and bounce.

!!! warning "Heads up"
    If the Shell shows only `0`s when nobody is pressing, the button may be wired across a joined pair of legs. If it shows only `1`s, check the ground wire. See [When Something Doesn't Work](../kits/moving-rainbow-base/index.md#when-something-doesnt-work) for the full checklist.

## Try it yourself

1. Change `time.sleep(0.1)` to `time.sleep(1)`. Tap the button as fast as you can. Can you catch every tap? The Pico only looks at the button when it prints.
2. Print words instead of numbers. Replace the loop with this version:

```python title="Your change"
while True:
    if button.value() == 0:
        print("pressed")
    else:
        print("released")
    time.sleep(0.1)
```

## Check your understanding

1. What does `Pin.PULL_UP` do?
2. What does `button.value()` return when the button is released? What does it return when the button is pressed?
3. Why does the loop call `time.sleep(0.1)`?
4. Where does the second wire of the button go?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You can hear a button! Your program now reads the world outside the Pico, and every interactive project starts right here.

**What's next:** In [Lab 33: Button and Built-in LED](33-button-led-test.md), the button turns the Pico's own LED on and off.
