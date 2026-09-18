# Additional Lab: Brightness Control

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Time to add a knob! Turn it one way and the strip glows brighter. Turn it the other way and the
    strip fades out. It's a real dimmer switch, and you're building it. Let's light this up!

**Program file:** [`01-brightness-led-strip.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-extras/01-brightness-led-strip.py) in the [extras kit folder](https://github.com/dmccreary/moving-rainbow/tree/master/src/kits/moving-rainbow-extras)

## What you'll learn

- How a **potentiometer** (a knob that changes its resistance as you turn it) works
- How the Pico reads a knob with its **ADC** (analog-to-digital converter, a part that turns a voltage into a number)
- How to shrink a big number range down to the 0 to 255 range a pixel understands
- How to keep the whole strip at a safe brightness

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- **One extra part:** a potentiometer (a 10 kΩ one is a good choice)
- Three jumper wires
- The `config.py` from the extras kit folder, saved on the Pico in place of the base kit's `config.py`. It has every base-kit setting plus `POT_PIN = 26`. (Copy files the same way as in [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit).)

## Wiring the knob

A potentiometer has three legs. The two outer legs connect to the two ends of a strip of resistive material. The middle leg, called the **wiper**, slides along that strip as you turn the knob.

| Potentiometer leg | Goes to | Pico pin |
|-------------------|---------|----------|
| One outer leg | `3V3(OUT)`, the Pico's 3.3 volts | Pin 36 |
| Other outer leg | Ground | Pin 33 (`AGND`) or any `GND` pin |
| Middle leg (wiper) | `GP26` | Pin 31 |

As you turn the knob, the voltage on the wiper slides between 0 volts and 3.3 volts. The Pico measures that voltage on `GP26`.

## The program

This program reads the knob ten times a second and sets every pixel to the same shade of white.

```python title="01-brightness-led-strip.py"
--8<-- "src/kits/moving-rainbow-extras/01-brightness-led-strip.py"
```

Run it and turn the knob. The whole strip fades from dark to bright, and the Shell prints the number it read.

!!! warning "Power check"
    With the knob turned all the way up, all 30 pixels show full white. That is about 30 x 60 mA = **1,800 mA**. A USB port supplies only about 500 mA. See [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go) Turn the knob slowly, and use the first challenge below to set a safe limit before you leave the program running.

## How it works

### Read the knob

```python
pot = ADC(POT_PIN)
```

This makes an ADC object for the pin named in `POT_PIN`. The extras `config.py` sets it to 26, which is `GP26`. Only three Pico pins can do this job: `GP26`, `GP27`, and `GP28`.

```python
pot_value = pot.read_u16() # read the value from the pot
```

`read_u16()` gives a whole number from 0 (knob turned all the way to ground) to 65535 (all the way to 3.3 volts). The "u16" means an *unsigned* (never negative) number that fits in 16 bits.

### Shrink the number

```python
scaled_value = pot_value >> 8
```

A pixel wants a number from 0 to 255, not 0 to 65535. The `>> 8` operator slides all the bits of the number 8 places to the right. That works out to dividing by 256, and it turns 0 to 65535 into 0 to 255.

### Set every pixel

```python
for i in range(NUMBER_PIXELS):
    strip[i] = (scaled_value, scaled_value, scaled_value)
```

Equal amounts of red, green, and blue make white. The loop sets all 30 pixels to the same value. Then one `strip.write()` sends the whole frame to the strip.

## Try it yourself

1. Make the strip safe. Change `>> 8` to `>> 10`. Now the brightest value is 63 instead of 255. All 30 pixels together draw about 450 mA at most.
2. Let the knob choose a color instead of a brightness. Change the pixel line to `strip[i] = (scaled_value, 0, 0)` so the knob controls only red.

## Check your understanding

1. What does the middle leg of a potentiometer do?
2. What is the biggest number `read_u16()` can return?
3. Why does the program shift the value right by 8 bits?
4. Why is it a good idea to limit the knob's brightness?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You gave your Pico a knob to feel with! Reading a sensor, scaling the number, and using it to change the lights is the recipe for every sensor project.

**What's next:** Add a light sensor in the [Photoresistor lab](photoresistor.md) and make the strip react to the room.
