# Lab 27: Main Template
# Filename: 27-main-template.py
# Version: 1.0.0
#
# All the light patterns from Labs 05 to 21 in one program. Mode 0 is auto
# mode: it shows every pattern for 10 seconds and then moves on by itself.
# Button 1 moves to the next mode and Button 2 moves back. Save a copy of
# this file on the Pico as main.py and the ring starts the light show on its
# own every time it gets power.
#
# How it works: every pattern is a "draw" function that sets the colors
# for just ONE step and then returns. The main loop at the bottom calls
# the draw function for the current mode, writes the ring and sleeps.
# Because no pattern ever runs a long loop of its own, the program sees
# a button press right away.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms, ticks_diff
from urandom import randint
from math import sin, pi
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BUTTON_PIN_1 = config.BUTTON_PIN_1
BUTTON_PIN_2 = config.BUTTON_PIN_2
BRIGHTNESS = config.BRIGHTNESS
TOP_PIXEL = config.TOP_PIXEL

DEBOUNCE_MS = 250        # ignore extra presses closer together than this
AUTO_MS = 10000          # in auto mode, each pattern shows for 10 seconds

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

off = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 60, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
violet = (138, 43, 226)
white = (255, 255, 255)
colors = (red, orange, yellow, green, cyan, blue, violet)
color_count = len(colors)

HALF = NUMBER_PIXELS // 2

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# add two colors together, keeping each part at 255 or less
def mix(color1, color2):
    return (min(color1[0] + color2[0], 255),
            min(color1[1] + color2[1], 255),
            min(color1[2] + color2[2], 255))

# turn a position counted clockwise from the top into a pixel number
def pixel_at(position):
    return (TOP_PIXEL + position) % NUMBER_PIXELS

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

# share one color between the two pixels closest to a decimal position
def draw_soft(position, color):
    lower = int(position)
    upper = (lower + 1) % NUMBER_PIXELS
    part = position - lower
    strip[lower] = mix(strip[lower], fade(color, 1 - part))
    strip[upper] = mix(strip[upper], fade(color, part))

# ---------------------------------------------------------------------
# The patterns. Each one draws one step. "step" counts up by one every
# time the main loop runs, and goes back to 0 when the mode changes.
# ---------------------------------------------------------------------

# Lab 05: one dot goes around
def draw_spin_dot(step):
    strip.fill(off)
    strip[step % NUMBER_PIXELS] = fade(red, 1)

# Lab 06: a comet that changes color after every lap
def draw_comet(step):
    tail_length = 10
    position = step % NUMBER_PIXELS
    color = colors[(step // NUMBER_PIXELS) % color_count]
    strip.fill(off)
    for t in range(tail_length):
        strip[(position - t) % NUMBER_PIXELS] = fade(color, (1 - t / tail_length) ** 2)

# Lab 07: two comets on opposite sides
def draw_two_comets(step):
    tail_length = 8
    strip.fill(off)
    for t in range(tail_length):
        amount = (1 - t / tail_length) ** 2
        strip[(step - t) % NUMBER_PIXELS] = fade(blue, amount)
        strip[(step + HALF - t) % NUMBER_PIXELS] = fade(orange, amount)

# Lab 08: two dots go opposite ways and flash when they meet
def draw_meet_and_flash(step):
    distance = step % NUMBER_PIXELS
    if distance % HALF == 0:
        strip.fill(fade(white, 0.5))
    else:
        strip.fill(off)
        strip[pixel_at(distance)] = fade(cyan, 1)
        strip[pixel_at(-distance)] = fade(violet, 1)

# Lab 10: the color wheel spins
def draw_spinning_rainbow(step):
    for i in range(NUMBER_PIXELS):
        color = wheel(i * 256 // NUMBER_PIXELS)
        strip[(i + step) % NUMBER_PIXELS] = fade(color, 1)

# Lab 11: colored blades spin, and the number of blades changes
blade_colors = (red, yellow, green, blue)
blade_counts = (2, 3, 4, 6, 12)
def draw_pinwheel(step):
    blades = blade_counts[(step // 25) % len(blade_counts)]
    width = NUMBER_PIXELS // (blades * 2)
    for i in range(NUMBER_PIXELS):
        section = ((i + step) // width) % (blades * 2)
        if section % 2 == 0:
            strip[i] = fade(blade_colors[(section // 2) % len(blade_colors)], 1)
        else:
            strip[i] = off

# Lab 12: an arc grows and shrinks as it goes around
spinner = {"tail": 0, "length": 2, "growing": True, "hue": 0}
def draw_loading_spinner(step):
    length = spinner["length"]
    color = wheel(spinner["hue"])
    strip.fill(off)
    for t in range(length):
        strip[(spinner["tail"] + t) % NUMBER_PIXELS] = fade(color, (t + 1) / length)
    if spinner["growing"]:
        spinner["tail"] = (spinner["tail"] + 1) % NUMBER_PIXELS
        spinner["length"] = length + 1
        if spinner["length"] >= 20:
            spinner["growing"] = False
    else:
        spinner["tail"] = (spinner["tail"] + 2) % NUMBER_PIXELS
        spinner["length"] = length - 1
        if spinner["length"] <= 2:
            spinner["growing"] = True
            spinner["hue"] = (spinner["hue"] + 40) % 256

# Lab 13: the whole ring breathes, with a new color at the darkest point
def draw_breathing_halo(step):
    half_breath = 100
    # adding half_breath means the first color starts at the darkest point
    place = (step + half_breath) % (half_breath * 2)
    level = abs(place - half_breath) / half_breath
    color = colors[(step // (half_breath * 2)) % color_count]
    strip.fill(fade(color, 0.02 + 0.98 * level * level))

# Lab 14: two waves of light roll around the ring
def draw_sine_wave(step):
    color = wheel(step % 256)
    phase = step * 0.15
    for i in range(NUMBER_PIXELS):
        angle = 2 * pi * 2 * i / NUMBER_PIXELS
        wave = (sin(angle - phase) + 1) / 2
        strip[i] = fade(color, wave * wave)

# Lab 15: ripples spread both ways and meet on the far side
ripples = []             # each ripple is a list: [center pixel, radius, color]
def draw_ripples(step):
    for i in range(NUMBER_PIXELS):
        r, g, b = strip[i]
        strip[i] = (int(r * 0.6), int(g * 0.6), int(b * 0.6))
    if len(ripples) < 3 and randint(1, 100) <= 12:
        ripples.append([randint(0, NUMBER_PIXELS - 1), 0, wheel(randint(0, 255))])
    for ripple in ripples[:]:
        center, radius, color = ripple
        amount = 1 - 0.7 * radius / HALF
        for pixel in (center + radius, center - radius):
            pixel = pixel % NUMBER_PIXELS
            strip[pixel] = mix(strip[pixel], fade(color, amount))
        if radius >= HALF:
            ripples.remove(ripple)
        else:
            ripple[1] = radius + 1

# Lab 16: a radar beam finds hidden targets
targets = [randint(0, NUMBER_PIXELS - 1) for t in range(3)]
glow = [0.0] * NUMBER_PIXELS
def draw_radar(step):
    tail_length = 12
    beam = step % NUMBER_PIXELS
    strip.fill(off)
    for t in range(tail_length):
        strip[(beam - t) % NUMBER_PIXELS] = fade(green, (1 - t / tail_length) ** 3)
    if beam in targets:
        glow[beam] = 1.0
    for i in range(NUMBER_PIXELS):
        if glow[i] > 0.02:
            strip[i] = fade(red, glow[i])
            glow[i] = glow[i] * 0.93
        else:
            glow[i] = 0.0
    if beam == NUMBER_PIXELS - 1:
        for t in range(len(targets)):
            targets[t] = (targets[t] + randint(-1, 1)) % NUMBER_PIXELS

# Lab 17: planets glide around at different speeds
planets = [
    [0.0, 0.32, (255, 150, 0)],
    [6.0, 0.20, (255, 255, 255)],
    [12.0, 0.13, (0, 80, 255)],
    [18.0, 0.08, (255, 0, 0)],
]
def draw_planets(step):
    strip.fill(off)
    for planet in planets:
        draw_soft(planet[0], planet[2])
        planet[0] = (planet[0] + planet[1]) % NUMBER_PIXELS

# Lab 18: a ball swings like a pendulum and slowly stops
pendulum = {"swing": 10.0, "time": 0.0, "color": 0}
def draw_pendulum(step):
    bottom = TOP_PIXEL + HALF
    strip.fill(off)
    strip[TOP_PIXEL] = fade(white, 0.1)
    position = (bottom + pendulum["swing"] * sin(pendulum["time"])) % NUMBER_PIXELS
    draw_soft(position, colors[pendulum["color"]])
    pendulum["time"] += 0.07
    pendulum["swing"] = pendulum["swing"] * 0.997
    if pendulum["swing"] < 0.5:
        pendulum["swing"] = 10.0
        pendulum["time"] = 0.0
        pendulum["color"] = (pendulum["color"] + 1) % color_count

# Lab 19: water fills from the bottom and drains away
deep_water = (0, 40, 255)
surface = (120, 220, 255)
def draw_water_level(step):
    full = HALF + 1
    level = full - abs(step % (full * 2) - full)
    for position in range(NUMBER_PIXELS):
        distance = abs(position - HALF)
        if distance < level - 1:
            strip[pixel_at(position)] = fade(deep_water, 1)
        elif distance == level - 1:
            strip[pixel_at(position)] = fade(surface, 1)
        else:
            strip[pixel_at(position)] = off

# Lab 20: flames spread around the ring
heat = [0] * NUMBER_PIXELS
def heat_to_color(heat_value):
    if heat_value < 85:
        return (heat_value * 3, 0, 0)
    if heat_value < 170:
        return (255, (heat_value - 85) * 2, 0)
    return (255, 170 + (heat_value - 170), (heat_value - 170) // 2)
def draw_ring_of_fire(step):
    global heat
    new_heat = [0] * NUMBER_PIXELS
    for i in range(NUMBER_PIXELS):
        left = heat[(i - 1) % NUMBER_PIXELS]
        right = heat[(i + 1) % NUMBER_PIXELS]
        new_heat[i] = max(0, (left + heat[i] * 2 + right) // 4 - randint(0, 36))
    for s in range(2):
        spot = randint(0, NUMBER_PIXELS - 1)
        new_heat[spot] = min(255, new_heat[spot] + randint(120, 255))
    heat = new_heat
    for i in range(NUMBER_PIXELS):
        strip[i] = fade(heat_to_color(heat[i]), 1)

# Lab 21: a cellular automaton with no edges
rules = (30, 90, 110, 54, 150)
automaton_cells = [0] * NUMBER_PIXELS
def draw_ring_automaton(step):
    global automaton_cells
    generation = step % 80
    if generation == 0 or sum(automaton_cells) == 0:
        # a new rule is starting, or every cell has gone out
        automaton_cells = [0] * NUMBER_PIXELS
        automaton_cells[TOP_PIXEL] = 1
    rule = rules[(step // 80) % len(rules)]
    color = wheel(generation * 3 % 256)
    new_cells = [0] * NUMBER_PIXELS
    for i in range(NUMBER_PIXELS):
        strip[i] = fade(color, automaton_cells[i])
        left = automaton_cells[(i - 1) % NUMBER_PIXELS]
        right = automaton_cells[(i + 1) % NUMBER_PIXELS]
        pattern = left * 4 + automaton_cells[i] * 2 + right
        new_cells[i] = (rule >> pattern) & 1
    automaton_cells = new_cells

# ---------------------------------------------------------------------
# The pattern list: a name, a draw function and a delay for every pattern.
# To add your own pattern, write a draw function and add a line here.
# ---------------------------------------------------------------------
patterns = [
    ("spin a dot", draw_spin_dot, 0.06),
    ("comet", draw_comet, 0.04),
    ("two comets", draw_two_comets, 0.05),
    ("meet and flash", draw_meet_and_flash, 0.08),
    ("spinning rainbow", draw_spinning_rainbow, 0.05),
    ("pinwheel", draw_pinwheel, 0.09),
    ("loading spinner", draw_loading_spinner, 0.05),
    ("breathing halo", draw_breathing_halo, 0.02),
    ("sine wave", draw_sine_wave, 0.03),
    ("ripples", draw_ripples, 0.07),
    ("radar", draw_radar, 0.07),
    ("planets", draw_planets, 0.03),
    ("pendulum", draw_pendulum, 0.03),
    ("water level", draw_water_level, 0.18),
    ("ring of fire", draw_ring_of_fire, 0.05),
    ("ring automaton", draw_ring_automaton, 0.2),
]

# Mode 0 is auto mode. Modes 1 to 16 each show one pattern:
# mode 1 is patterns[0], mode 2 is patterns[1] and so on.
MODE_COUNT = len(patterns) + 1

mode = 0
last_press = 0

# this function runs by itself the moment Button 1 is pressed
def button1_pressed(pin):
    global mode, last_press
    now = ticks_ms()
    # a button "bounces" and can look like many presses, so we ignore
    # any press that comes too soon after the last one
    if ticks_diff(now, last_press) > DEBOUNCE_MS:
        mode = (mode + 1) % MODE_COUNT      # % goes back to 0 after the last mode
        last_press = now

# this function runs by itself the moment Button 2 is pressed
def button2_pressed(pin):
    global mode, last_press
    now = ticks_ms()
    if ticks_diff(now, last_press) > DEBOUNCE_MS:
        mode = (mode - 1) % MODE_COUNT      # % goes to the last mode from mode 0
        last_press = now

# call the function when the pin falls from 1 (released) to 0 (pressed)
button1.irq(trigger=Pin.IRQ_FALLING, handler=button1_pressed)
button2.irq(trigger=Pin.IRQ_FALLING, handler=button2_pressed)

print("Ring ready! Button 1 is the next mode and Button 2 goes back.")
current_mode = -1
current_pattern = -1
auto_start = 0           # when auto mode switched to its current pattern
step = 0
while True:
    if mode != current_mode:
        # a button changed the mode
        current_mode = mode
        if current_mode == 0:
            print("Mode 0 - auto: a new pattern every", AUTO_MS // 1000, "seconds")
            pattern = 0
            auto_start = ticks_ms()
        else:
            pattern = current_mode - 1
            print("Mode", current_mode, "-", patterns[pattern][0])
    elif current_mode == 0 and ticks_diff(ticks_ms(), auto_start) >= AUTO_MS:
        # auto mode: time is up, so move on to the next pattern
        pattern = (pattern + 1) % len(patterns)
        auto_start = ticks_ms()

    if pattern != current_pattern:
        # a new pattern is starting: clear the ring and start it fresh
        current_pattern = pattern
        step = 0
        strip.fill(off)
        if current_mode == 0:
            print("  auto:", patterns[pattern][0])

    name, draw, delay = patterns[current_pattern]
    draw(step)               # set the colors for this step
    strip.write()            # one write per step
    sleep(delay)
    step += 1
