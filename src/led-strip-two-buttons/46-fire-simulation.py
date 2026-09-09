# A flickering fire effect using a simple heat simulation. Heat cools
# down over time, drifts upward, and new sparks appear near the bottom.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

COOLING = 55      # how fast each pixel cools down (higher = shorter flames)
SPARKING = 120    # chance (0-255) of a new spark appearing each frame
heat = [0] * config.NUMBER_PIXELS


def heat_to_color(h):
    # turn a heat value (0-255) into a fire color: black -> red -> yellow -> white
    if h < 85:
        return (h * 3, 0, 0)
    elif h < 170:
        return (255, (h - 85) * 3, 0)
    else:
        return (255, 255, (h - 170) * 3)


while True:
    # Step 1: cool down every pixel a little
    for i in range(config.NUMBER_PIXELS):
        cooldown = randint(0, (COOLING * 10) // config.NUMBER_PIXELS + 2)
        heat[i] = max(0, heat[i] - cooldown)

    # Step 2: heat drifts upward and mixes with its neighbors
    for i in range(config.NUMBER_PIXELS - 1, 1, -1):
        heat[i] = (heat[i - 1] + heat[i - 2] + heat[i - 2]) // 3

    # Step 3: randomly spark a new flame near the bottom of the strip
    if randint(0, 255) < SPARKING:
        spark_pixel = randint(0, 2)
        heat[spark_pixel] = min(255, heat[spark_pixel] + randint(160, 255))

    # Step 4: draw the heat values as fire colors
    for i in range(config.NUMBER_PIXELS):
        strip[i] = heat_to_color(heat[i])
    strip.write()

    sleep(0.03)
