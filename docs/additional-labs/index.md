# Additional Labs

The [Hands on Labs](../labs/index.md) use only the parts that come in the base kit: a Pico, a
breadboard, a 30-pixel LED strip, and two push buttons. The labs on this page go a step further.
Each one needs **one extra part** that is not in the base kit.

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Finished the base labs and hungry for more? Add one small part and your Pico can sense the
    world around it. Let's light this up!

## The Additional Labs

| Lab | What you add | What you learn | Programs |
|-----|--------------|----------------|----------|
| [Brightness Control](potentiometer-brightness.md) | A **potentiometer** (a knob that changes resistance) | Read a knob with the Pico and use it as a dimmer for the whole strip | `01-brightness-led-strip.py` |
| [Photoresistor](photoresistor.md) | A **photoresistor** (a part that changes resistance with light) and a fixed resistor | Read the light in a room and build a nightlight | `02-photoresistor-test.py`, `03-photoresistor-bar.py`, `04-photoresistor-nightlight.py` |

## Where the code lives

The programs for these labs are in their own kit folder,
[`src/kits/moving-rainbow-extras/`](https://github.com/dmccreary/moving-rainbow/tree/master/src/kits/moving-rainbow-extras),
separate from the base kit. The folder has its own `config.py`. It holds every base-kit setting plus the pins
for the extra parts, so save it on your Pico in place of the base kit's `config.py`.
The folder also has an `upload-code.sh` script that works the same way as the
[base kit's script](../kits/moving-rainbow-base/index.md#the-fast-way-for-a-whole-class).

## Why are these separate?

The base kit is built to cost about $15 and still teach the big ideas. Each part you add costs a
little more and needs a little more wiring. Keeping these labs separate means every student can
finish the Hands on Labs with only the base kit.

Both extra parts are common, low-cost electronics components. The
[Purchasing Guide](../kits/moving-rainbow-base/purchasing-guide/index.md) shows where the base kit parts
come from, and it is a good place to start shopping.

## Ready first?

If you have not done the base labs yet, start with [Lab 01: Blink the Onboard LED](../labs/01-blink-onboard-led.md)
and work up. These additional labs will be waiting for you.
