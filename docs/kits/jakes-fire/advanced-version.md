# Jake's Fire - Advanced Version

The [basic version](./index.md) makes fire by lighting random pixels
with random orange colors. It looks good, but it doesn't really *flow*
like a real fire. This advanced version models heat itself, so the flames
rise, flicker, and cool down the way real embers do.

!!! tip "Pixel says..."
    Real fire isn't random — it's heat moving around! Here we give every
    pixel a heat number. Heat rises, cools off, and now and then a new
    spark jumps up from the embers. Watch it breathe!

## What's Different

The basic version picks colors at random each frame. The advanced version
keeps a **heat map** — a list of heat values, one per pixel. Each frame we
do four steps:

1. **Cool down.** Every pixel loses a little heat.
2. **Drift up.** Heat spreads from each pixel to the next one along the ring.
3. **Spark.** Now and then a pixel near the base gets a burst of new heat.
4. **Paint.** We turn each pixel's heat number into a fire color.

This is a small version of a classic fire algorithm. The key idea is
**state** — the strip remembers its heat from one frame to the next,
instead of starting fresh every time.

!!! info "Pixel thinks..."
    A higher cooling number makes a shorter, flickery flame. More sparks
    make a taller, hotter fire. Try changing `COOLING` and `SPARKING` to
    get the look Jake wants for each game.

## Heat to Color

A real flame goes from dark red at the cool edges, up through orange and
yellow, to near-white at the hottest core. This function maps a heat
value (0 to 255) onto that range:

```python
# Turn a heat value (0-255) into a fire color (red, green, blue).
def heat_to_color(heat):
    # scale heat down into 0-191 so we can split it into three bands
    t = (heat * 191) // 255
    band = t & 0x3F          # the lower part within a band (0-63)
    band = band * 4          # spread it out to 0-252

    if t > 0x80:             # hottest third: orange -> white
        return (255, 255, band)
    elif t > 0x40:           # middle third: red -> orange
        return (255, band, 0)
    else:                    # coolest third: black -> red
        return (band, 0, 0)
```

## The Full Program

This program runs the heat model on both NeoPixel rings using the same
`dual_ring_config.py` file as the basic version. The potentiometer
changes how hot and tall the fire gets.

```python
# Jake's Fire - Advanced heat-model version
# Uses a heat map so flames rise, flicker, and cool like real fire.
# untested - adapt the COOLING and SPARKING values for your setup
from machine import Pin, ADC
from neopixel import NeoPixel
from utime import sleep
from urandom import randint

import dual_ring_config

pot = ADC(dual_ring_config.POT_PIN)

NUMBER_PIXELS0 = dual_ring_config.NUMBER_PIXELS0   # 24 (outer ring)
NUMBER_PIXELS1 = dual_ring_config.NUMBER_PIXELS1   # 12 (inner ring)

strip0 = NeoPixel(Pin(dual_ring_config.NEOPIXEL_PIN0), NUMBER_PIXELS0)
strip1 = NeoPixel(Pin(dual_ring_config.NEOPIXEL_PIN1), NUMBER_PIXELS1)

# How fast pixels lose heat. Bigger = shorter, flickerier flames.
COOLING = 55
# How often a new spark appears near the base. Bigger = taller fire.
SPARKING = 120

# One heat value per pixel, all starting cold (0).
heat0 = [0] * NUMBER_PIXELS0
heat1 = [0] * NUMBER_PIXELS1

# Turn a heat value (0-255) into a fire color.
def heat_to_color(heat):
    t = (heat * 191) // 255
    band = (t & 0x3F) * 4
    if t > 0x80:
        return (255, 255, band)
    elif t > 0x40:
        return (255, band, 0)
    else:
        return (band, 0, 0)

# Run one frame of the fire model on a single ring.
def update_fire(heat, num_pixels, strip, sparking):
    # Step 1: cool every pixel down by a small random amount.
    for i in range(num_pixels):
        cooldown = randint(0, ((COOLING * 10) // num_pixels) + 2)
        heat[i] = max(0, heat[i] - cooldown)

    # Step 2: drift heat upward (around the ring).
    for i in range(num_pixels - 1, 1, -1):
        heat[i] = (heat[i - 1] + heat[i - 2] + heat[i - 2]) // 3

    # Step 3: now and then, add a spark near the base.
    if randint(0, 255) < sparking:
        i = randint(0, 6)
        heat[i] = min(255, heat[i] + randint(160, 255))

    # Step 4: paint the heat onto the pixels.
    for i in range(num_pixels):
        strip[i] = heat_to_color(heat[i])
    strip.write()

# Turn both rings off.
def clear():
    for i in range(NUMBER_PIXELS0):
        strip0[i] = (0, 0, 0)
    strip0.write()
    for i in range(NUMBER_PIXELS1):
        strip1[i] = (0, 0, 0)
    strip1.write()

try:
    print("Advanced fire running - Press Ctrl+C to stop")
    while True:
        # The pot sets the spark rate: turn it up for a bigger blaze.
        sparking = 40 + (pot.read_u16() >> 8)   # ranges about 40-295
        update_fire(heat0, NUMBER_PIXELS0, strip0, sparking)
        update_fire(heat1, NUMBER_PIXELS1, strip1, sparking)
        sleep(0.03)
except KeyboardInterrupt:
    print("\nStopping fire effect")
    clear()
```

You should see flames that rise and fade smoothly instead of flickering
at random. Turning the potentiometer up makes a taller, hotter fire.

!!! warning "Watch out!"
    A full, bright fire on both rings draws a lot of power. If the rings
    flicker or the Pico resets, lower the colors in `heat_to_color` or
    power the rings from a separate 5V supply instead of USB.

## Code Walk-Through

- **`heat0` and `heat1`** are the heat maps — the fire's memory. Each
  number is how hot one pixel is right now.
- **Cooling** subtracts a small random amount from every pixel. Random
  cooling is what makes the flicker look natural.
- **Drifting** averages each pixel with the two before it. This smooths
  the heat and makes it climb the ring.
- **Sparking** adds fresh heat near the base only some of the time. That
  randomness is why no two flames look the same.
- **Painting** converts heat to color with `heat_to_color`, so cool
  pixels are dark red and the hottest are near white.

## Try It Yourself

- Lower `COOLING` to 20 for a tall, lazy flame. Raise it to 90 for a
  small, busy one.
- Add a second color map that makes a blue or green "magic" fire for a
  different game.
- Use the button instead of the pot to switch between fire colors.

!!! note "For the maintainer"
    This advanced version is built from the classic heat-map fire model
    and has **not yet been tested on Jake's actual two-ring hardware**.
    Before publishing, run it on the rings and tune `COOLING`,
    `SPARKING`, and the brightness in `heat_to_color` to match the
    diffusion sheet. If a tested advanced sketch already exists, drop it
    into `src/kits/jakes-fire/` and replace the code block above.
