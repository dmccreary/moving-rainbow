# Lab 1: Blink the Onboard LED

Your first program blinks the tiny green LED that is built onto the Pico. You do not need the strip or the button yet. This lab checks that your Pico, your cable and Thonny all work together.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Every costume starts with one small step. This one is a blink! If the little light flashes, your Pico is awake and ready. Let's light this up!

**Program file:** [`01-blink-onboard-led.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/halloween-60-button/01-blink-onboard-led.py)

## What You'll Learn

- Run a program on the Raspberry Pi Pico
- Turn an LED on and off with code
- Use a **loop** (code that repeats) to keep blinking
- Change a **variable** (a named value) to change the speed

## What You'll Need

- A Raspberry Pi Pico
- A USB cable that carries data (some cables only charge)
- Thonny open on your computer

## The Program

This program switches the onboard LED on and off forever.

```python
--8<-- "src/kits/halloween-60-button/01-blink-onboard-led.py"
```

You should see the small LED next to the USB plug blink about twice a second.

## How It Works

`Pin(BUILT_IN_LED_PIN, Pin.OUT)` sets up pin 25 as an **output** (a pin the Pico controls). Every Pico has its LED on pin 25.

`led.toggle()` flips the LED. If it is off, it turns on. If it is on, it turns off. Then `sleep(BLINK_DELAY)` waits before the loop runs again.

This is the only lab that does not use `config.py`. It runs even before you copy the other files onto the Pico.

## Try It Yourself

1. Change `BLINK_DELAY` to `1` for a slow blink. Then try `0.05`. What happens?
2. Can you make the LED stay on longer than it stays off? Hint: use `led.on()`, `led.off()` and two `sleep()` lines.

## Check Your Understanding

1. Which pin is the onboard LED on?
2. What does `led.toggle()` do?
3. What would happen if you took out the `sleep()` line?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    You did it! Your costume just learned a new trick.

## What's Next

Go on to [Lab 2: Hardware Probe](02-probe.md).
