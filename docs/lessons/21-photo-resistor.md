# Photoresistor

A **photoresistor** (a part that changes its resistance when light hits it)
lets your Pico "see" how bright a room is. In this lesson we read the
light level, print it, and then use it to control the LED strip.

!!! tip "Pixel says..."
    Let's give your Pico a sense of sight! A photoresistor is like a
    tiny eye. The more light it sees, the more electricity it lets
    through. We can measure that and turn it into LED colors.

## What you'll learn

- What a photoresistor is and how it changes with light
- How to read an analog value with the Pico's ADC
- How to turn a light reading into LED colors
- How a nightlight uses light to decide when to turn on

## What you'll need

- A Moving Rainbow kit with a photoresistor wired to pin 28
- A NeoPixel strip on pin 0
- The kit's standard `config.py` file

## How a Photoresistor Works

A photoresistor is wired as part of a **voltage divider** (two parts
that split a voltage between them). As the light changes, the voltage at
the middle of the divider changes too.

The Pico reads that voltage with its **ADC** (Analog-to-Digital
Converter — a part that turns a voltage into a number). The Pico's ADC
gives us a number from 0 to 65535.

!!! info "Pixel thinks..."
    A bigger number means more light. In a dark room you might read
    about 1,500. In a bright room you might read about 55,000. Your
    room will be different — that's why we test it first!

## Testing the Photoresistor

This first program reads the light level and prints it to the screen.
Run it, then wave your hand over the sensor or cover it with your finger.

```python
# Read the light level from a photoresistor and print it.
import machine
from utime import sleep
import config

# The ADC (light-reading) pins on the Pico are 26, 27, and 28
photo_pin = machine.ADC(config.PHOTORESISTOR_PIN)

while True:
    val = photo_pin.read_u16()   # read a number from 0 to 65535
    print(val)                   # show it in the console
    sleep(0.2)                   # wait a fifth of a second
```

You should see numbers stream by in the console. Cover the sensor and
the numbers drop. Shine a light on it and they jump up.

!!! tip "Pixel's tip"
    Write down your darkest number and your brightest number. You'll
    use them in the next program to set your nightlight's "trigger"
    point.

## Showing Light Level on the Strip

Now let's turn the light reading into a bar of color. The darker the
room, the fewer LEDs light up. The brighter the room, the more light up.

```python
# Show the room's light level as a bar of colored LEDs.
from machine import Pin, ADC
from neopixel import NeoPixel
from utime import sleep
import config

# Set up the LED strip and the light sensor
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
photo_pin = ADC(Pin(config.PHOTORESISTOR_PIN))

# Turn every pixel off.
def clear_strip():
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()

while True:
    light_value = photo_pin.read_u16()    # read the light level

    # Turn the light level into a number of pixels (0 to 12).
    # Change 2000 and 55000 to match the numbers you wrote down.
    if light_value < 2000:
        num_pixels = 0
    elif light_value > 55000:
        num_pixels = 12
    else:
        light_range = light_value - 2000
        num_pixels = int((light_range / (55000 - 2000)) * 12)

    clear_strip()

    # Light up the bar with blue, then green, then red.
    for i in range(num_pixels):
        if i < 4:
            strip[i] = (0, 0, 25)     # low light: blue
        elif i < 8:
            strip[i] = (0, 25, 0)     # medium light: green
        else:
            strip[i] = (25, 0, 0)     # high light: red
    strip.write()

    sleep(0.2)
```

You should see a bar of LEDs that grows when the room is bright and
shrinks when you cover the sensor.

!!! warning "Watch out!"
    If the bar never changes, your sensor's numbers may be different
    from 2000 and 55000. Go back to the test program, find your real
    dark and bright numbers, and put them in this code.

## The Nightlight

A **nightlight** flips the idea around: it turns the LEDs *on* when the
room gets *dark*. We pick a **threshold** (a cut-off number). When the
light reading drops below the threshold, the strip turns on.

```python
if light_value < LIGHT_THRESHOLD:
    # room is dark - turn the nightlight on
    ...
else:
    # room is bright - turn the nightlight off
    clear_strip()
```

There are two ways to build a nightlight, and the Moving Rainbow kits
include both.

### Analog Nightlight

An **analog** nightlight uses no code at all. A transistor and a
photoresistor act as a switch. When it gets dark, the transistor turns
the LED on by itself.

[See the Analog Nightlight kit](../kits/analog-nightlight/index.md)

### Digital Nightlight

A **digital** nightlight uses the Pico and the code you just learned.
Because it runs code, you can add patterns, colors, brightness control,
and even an automatic shutoff timer.

[See the Digital Nightlight kit](../kits/digital-nightlight/index.md)

!!! success "You've got this!"
    You just taught your Pico to react to the world around it. That's
    the first step toward every sensor project — robots, weather
    stations, and smart lights all start right here.

## Try It Yourself

- Change `LIGHT_THRESHOLD` so the light comes on at dusk instead of full dark.
- Make the bar use a rainbow of colors instead of blue, green, and red.
- Print "Nightlight ON" or "Nightlight OFF" each time the state changes.

## Check Your Understanding

1. What does a photoresistor do when more light hits it?
2. What range of numbers does the Pico's ADC return?
3. Why do we test the sensor before setting a threshold?
4. What is the difference between an analog and a digital nightlight?
