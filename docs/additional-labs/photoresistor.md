# Additional Lab: Photoresistor

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Let's give your Pico a sense of sight! A photoresistor is like a tiny eye. The more light it
    sees, the more electricity it lets through. We can measure that and turn it into LED colors.

**Program files:** [`02-photoresistor-test.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-extras/02-photoresistor-test.py),
[`03-photoresistor-bar.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-extras/03-photoresistor-bar.py), and
[`04-photoresistor-nightlight.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-extras/04-photoresistor-nightlight.py)
in the [extras kit folder](https://github.com/dmccreary/moving-rainbow/tree/master/src/kits/moving-rainbow-extras)

A **photoresistor** (a part that changes its resistance when light hits it) lets your Pico "see"
how bright a room is. In this lab we read the light level, print it, show it as a bar on the LED
strip, and then build a nightlight.

## What you'll learn

- What a photoresistor is and how it changes with light
- How to read an analog value with the Pico's ADC
- How to turn a light reading into a bar of LED colors
- How a nightlight uses a **threshold** (a cut-off number) to decide when to turn on

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- **Two extra parts:** a photoresistor and a fixed resistor (10 kΩ is a common choice)
- Jumper wires
- The `config.py` from the extras kit folder, saved on the Pico (see below)

!!! note "Not yet tested on hardware"
    The three programs for this lab are in `src/kits/moving-rainbow-extras/`. They follow the same pattern as the base-kit programs, but they have not been run on a real kit yet. Each one says so in its header. If something does not work, check the wiring and the numbers in `config.py` first.

## Wiring the sensor

The photoresistor is one half of a **voltage divider** (two parts that split a voltage between them). Wire it like this:

| Part | Goes between | Pico pin |
|------|--------------|----------|
| Photoresistor | `3V3(OUT)` and the middle point | Pin 36 |
| Fixed resistor | The middle point and ground | Any `GND` pin |
| Middle point (the wire to the Pico) | Where the two parts meet | `GP28`, pin 34 |

As the light changes, the voltage at the middle point changes too. More light means less resistance in the photoresistor, so the voltage at the middle point goes up. Try the [Pico Light Sensor Circuit](../sims/pico-light-sensor/index.md) simulation to see it happen. The [Photoresistor Component](../sims/photoresistor-component/index.md) simulation shows the part itself.

## The extras `config.py`

The base kit's `config.py` has no sensor pins, because the base kit has no sensors. The extras kit has its own `config.py`. It holds every base-kit setting plus the pins for the extra parts. Save it on your Pico in place of the base one.

```python title="config.py"
--8<-- "src/kits/moving-rainbow-extras/config.py"
```

The line `PHOTORESISTOR_PIN = 28` tells the programs that the sensor is wired to `GP28`.

## Reading the light level

The Pico reads the middle-point voltage with its **ADC** (analog-to-digital converter, a part that turns a voltage into a number). The number runs from 0 to 65535.

!!! info "Key idea"
    A bigger number means more light. In a dark room you might read about 1,500. In a bright room you might read about 55,000. Your room will be different, so test it first!

This first program reads the light level and prints it. Run it, then wave your hand over the sensor or cover it with your finger.

```python title="02-photoresistor-test.py"
--8<-- "src/kits/moving-rainbow-extras/02-photoresistor-test.py"
```

You should see numbers stream by in the Shell. Cover the sensor and the numbers drop. Shine a light on it and they jump up.

!!! tip "Tip"
    Write down your darkest number and your brightest number. You will use them in the next program.

## Showing the light level on the strip

This program turns the light reading into a bar of colored pixels. The darker the room, the fewer pixels light up.

```python title="03-photoresistor-bar.py"
--8<-- "src/kits/moving-rainbow-extras/03-photoresistor-bar.py"
```

You should see a bar that grows when the room is bright and shrinks when you cover the sensor.

!!! warning "Heads up"
    If the bar never changes, your sensor's numbers may be different from 2000 and 55000. Go back to the first program, find your real dark and bright numbers, and put them in `DARK_VALUE` and `BRIGHT_VALUE`.

## The nightlight

A **nightlight** flips the idea around. It turns the pixels *on* when the room gets *dark*. We pick a threshold. When the light reading drops below the threshold, the strip turns on.

```python title="04-photoresistor-nightlight.py"
--8<-- "src/kits/moving-rainbow-extras/04-photoresistor-nightlight.py"
```

Cover the sensor and the strip glows warm. Uncover it and the strip turns off. Pick a `LIGHT_THRESHOLD` between your dark and bright numbers.

### Two ways to build a nightlight

- An **analog** nightlight uses no code. A transistor and a photoresistor act as a switch, and the light turns on by itself when it gets dark. See the [Analog Nightlight kit](../kits/analog-nightlight/index.md).
- A **digital** nightlight uses the Pico and the code above. Because it runs code, you can add patterns, colors, and brightness control. See the [Digital Nightlight kit](../kits/digital-nightlight/index.md).

## Try it yourself

1. Change `LIGHT_THRESHOLD` so the light comes on at dusk instead of full dark.
2. Make the bar use a rainbow of colors instead of blue, green, and red. The `wheel()` function from [Lab 09: Color Wheel](../labs/09-color-wheel.md) can help.

## Check your understanding

1. What does a photoresistor do when more light hits it?
2. What range of numbers does the Pico's ADC return?
3. Why do we test the sensor before choosing a threshold?
4. What is the difference between an analog and a digital nightlight?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You taught your Pico to react to the world around it! Robots, weather stations, and smart lights all start with this same idea.

**What's next:** Head back to the [Hands on Labs](../labs/index.md) to try a game, or design a nightlight that is all your own.
