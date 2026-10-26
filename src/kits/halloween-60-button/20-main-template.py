# Lab 20: Main Template
# Filename: 20-main-template.py
# Version: 1.0.0
# Not yet tested on hardware.
#
# All eleven Halloween patterns from Labs 06 to 16 in one program. Each
# press of the button moves to the next pattern, and after the last one
# it goes back to the first. Save a copy of this file on the Pico as
# main.py and your costume starts the light show on its own every time
# you plug in the battery.
#
# How it works: every pattern is a "draw" function that sets the colors
# for just ONE step and then returns. The main loop at the bottom calls
# the draw function for the current mode, writes the strip and sleeps.
# Because no pattern ever runs a long loop of its own, the program sees
# a button press right away.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms, ticks_diff
from urandom import randint
from math import sin
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BUTTON_PIN = config.BUTTON_PIN
BRIGHTNESS = config.BRIGHTNESS

DEBOUNCE_MS = 250        # ignore extra presses closer together than this

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)   # the button connects GPIO 15 to GND

# Halloween colors
orange = (255, 80, 0)
purple = (140, 0, 255)
black = (0, 0, 0)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the strip is safe on battery power
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# add two colors together, keeping each part at 255 or less
def mix(color1, color2):
    return (min(color1[0] + color2[0], 255),
            min(color1[1] + color2[1], 255),
            min(color1[2] + color2[2], 255))

# ---------------------------------------------------------------------
# The patterns. Each one draws one step. "step" counts up by one every
# time the main loop runs, and goes back to 0 when the mode changes.
# ---------------------------------------------------------------------

# Lab 06: an orange comet runs down while a purple comet runs up
def draw_chase(step):
    tail_length = 6
    position = step % NUMBER_PIXELS
    strip.fill(black)
    for t in range(tail_length):
        amount = 1 - t / tail_length
        orange_index = (position - t) % NUMBER_PIXELS
        purple_index = (NUMBER_PIXELS - 1 - position + t) % NUMBER_PIXELS
        strip[orange_index] = mix(strip[orange_index], fade(orange, amount))
        strip[purple_index] = mix(strip[purple_index], fade(purple, amount))

# Lab 07: the whole strip breathes orange
def draw_pumpkin_glow(step):
    # this counts 10, 12, ... 100, 98, ... 10 and repeats
    level = 10 + abs((step * 2) % 180 - 90)
    strip.fill(fade(orange, level / 100))

# Lab 08: candy corn stripes slide along the strip
candy_stripes = [(255, 180, 0), (255, 60, 0), (180, 180, 180)]
def draw_candy_corn(step):
    stripe_width = 4
    for i in range(NUMBER_PIXELS):
        stripe = ((i + step) // stripe_width) % len(candy_stripes)
        strip[i] = fade(candy_stripes[stripe], 1)

# Lab 09: random sparks that fade away
def draw_spooky_sparkle(step):
    for i in range(NUMBER_PIXELS):
        r, g, b = strip[i]
        strip[i] = (int(r * 0.85), int(g * 0.85), int(b * 0.85))
    for n in range(2):
        place = randint(0, NUMBER_PIXELS - 1)
        if randint(0, 1) == 0:
            strip[place] = fade(orange, 1)
        else:
            strip[place] = fade(purple, 1)

# Lab 10: a ghost floats down the strip and back
ghost = (160, 170, 255)
def draw_ghost_drift(step):
    tail_length = 8
    trip = NUMBER_PIXELS - 1           # steps to float from one end to the other
    p = step % (trip * 2)
    if p < trip:
        position = p                   # going down
        direction = 1
    else:
        position = trip * 2 - p        # coming back
        direction = -1
    strip.fill(black)
    for t in range(tail_length):
        index = position - t * direction
        if 0 <= index < NUMBER_PIXELS:
            strip[index] = fade(ghost, (1 - t / tail_length) ** 2)

# Lab 11: pairs of eyes blink at random times
eye_colors = [(255, 0, 0), (0, 255, 0), orange, purple]
eyes = []                # each pair is a list: [first pixel, color, next blink time]
for start in range(2, NUMBER_PIXELS - 1, 10):
    eyes.append([start, eye_colors[randint(0, 3)], ticks_ms() + randint(500, 4000)])
def draw_monster_eyes(step):
    now = ticks_ms()
    strip.fill(black)
    for pair in eyes:
        start, color, blink_at = pair
        time_left = ticks_diff(blink_at, now)
        if time_left > 0:
            strip[start] = fade(color, 1)
            strip[start + 1] = fade(color, 1)
        elif time_left < -150:
            pair[2] = now + randint(1000, 5000)

# Lab 12: drops form, fall with gravity and fill a pool
red = (255, 0, 0)
dark_red = (90, 0, 0)
drip = {"state": "grow", "grow": 0, "position": 0.0, "speed": 0.0, "pool": 0}
def draw_blood_drip(step):
    pool = drip["pool"]
    strip.fill(black)
    for p in range(pool):
        strip[NUMBER_PIXELS - 1 - p] = fade(dark_red, 1)
    bottom = NUMBER_PIXELS - 1 - pool
    if drip["state"] == "grow":
        drip["grow"] += 1
        strip[0] = fade(red, drip["grow"] / 30)
        if drip["grow"] >= 30:
            drip["state"] = "fall"
            drip["position"] = 0.0
            drip["speed"] = 0.0
    elif drip["state"] == "fall":
        drip["speed"] += 0.04
        drip["position"] += drip["speed"]
        head = min(int(drip["position"]), bottom)
        strip[head] = fade(red, 1)
        if head > 0:
            strip[head - 1] = fade(red, 0.3)
        if head >= bottom:
            drip["pool"] += 1
            drip["grow"] = 0
            drip["state"] = "drain" if drip["pool"] > 15 else "grow"
    elif drip["state"] == "drain":
        if step % 3 == 0:
            drip["pool"] -= 1
        if drip["pool"] <= 0:
            drip["pool"] = 0
            drip["state"] = "grow"

# Lab 13: bats fly at their own speeds
bat_positions = []
bat_speeds = []
for b in range(6):
    bat_positions.append(randint(0, NUMBER_PIXELS - 1))
    speed = randint(10, 40) / 100
    bat_speeds.append(speed if randint(0, 1) else -speed)
def draw_bat_swarm(step):
    strip.fill(fade((40, 30, 0), 1))   # the moonlit sky
    for b in range(len(bat_positions)):
        bat_positions[b] = (bat_positions[b] + bat_speeds[b]) % NUMBER_PIXELS
        index = int(bat_positions[b])
        strip[index] = fade(purple, 1 if (step + b) % 6 < 3 else 0.4)
        strip[(index + 1) % NUMBER_PIXELS] = fade(purple, 0.2)

# Lab 14: potion bubbles rise and pop
bubble_colors = [(0, 255, 40), purple]
bubbles = []             # each bubble is a list: [position, color, pop height]
def draw_cauldron_bubbles(step):
    if len(bubbles) < 6 and randint(1, 100) <= 15:
        bubbles.append([0, bubble_colors[randint(0, 1)], randint(NUMBER_PIXELS // 3, NUMBER_PIXELS - 1)])
    strip.fill(fade((0, 60, 10), 1))
    for bubble in bubbles[:]:
        position, color, pop_height = bubble
        if position >= pop_height:
            strip[position] = fade((200, 255, 200), 1)
            bubbles.remove(bubble)
        else:
            strip[position] = fade(color, 0.3 + 0.7 * position / pop_height)
            bubble[0] = position + 1

# Lab 15: a flickering jack-o'-lantern fire
heat = [0] * NUMBER_PIXELS
def heat_to_color(t):
    if t < 85:
        return (t * 3, 0, 0)
    elif t < 170:
        return (255, (t - 85) * 2, 0)
    else:
        return (255, 170 + (t - 170), (t - 170) // 2)
def draw_fire(step):
    for i in range(NUMBER_PIXELS):
        heat[i] = max(0, heat[i] - randint(0, (55 * 10) // NUMBER_PIXELS + 2))
    for i in range(NUMBER_PIXELS - 1, 1, -1):
        heat[i] = (heat[i - 1] + heat[i - 2] * 2) // 3
    if randint(0, 255) < 120:
        spot = randint(0, 6)
        heat[spot] = min(255, heat[spot] + randint(160, 255))
    for i in range(NUMBER_PIXELS):
        strip[i] = fade(heat_to_color(heat[i]), 1)

# Lab 16: a purple thunderstorm with lightning
storm = {"state": "calm", "next_strike": ticks_ms() + 2000, "flashes": 0,
         "end": 0, "start": 0, "stop": 0, "glow": 0.0}
def draw_lightning_storm(step):
    now = ticks_ms()
    for i in range(NUMBER_PIXELS):
        wave = (sin(i * 0.3 + step * 0.05) + 1) / 2
        strip[i] = fade((60, 0, 120), 0.1 + 0.4 * wave)
    state = storm["state"]
    if state == "calm":
        if ticks_diff(now, storm["next_strike"]) >= 0:
            storm["start"] = randint(0, NUMBER_PIXELS - 10)
            storm["stop"] = min(storm["start"] + randint(5, 20), NUMBER_PIXELS)
            storm["flashes"] = randint(2, 3)
            storm["state"] = "flash"
            storm["end"] = now + 60
    elif state == "flash":
        for i in range(storm["start"], storm["stop"]):
            strip[i] = fade((255, 255, 255), 1)
        if ticks_diff(now, storm["end"]) >= 0:
            storm["flashes"] -= 1
            if storm["flashes"] > 0:
                storm["state"] = "dark"
                storm["end"] = now + randint(50, 150)
            else:
                storm["state"] = "glow"
                storm["glow"] = 1.0
    elif state == "dark":
        if ticks_diff(now, storm["end"]) >= 0:
            storm["state"] = "flash"
            storm["end"] = now + 40
    elif state == "glow":
        for i in range(storm["start"], storm["stop"]):
            strip[i] = fade((120, 60, 255), storm["glow"])
        storm["glow"] -= 0.03
        if storm["glow"] <= 0:
            storm["state"] = "calm"
            storm["next_strike"] = now + randint(2000, 6000)

# ---------------------------------------------------------------------
# The mode list: a name, a draw function and a delay for every pattern.
# To add your own pattern, write a draw function and add a line here.
# ---------------------------------------------------------------------
modes = [
    ("orange and purple chase", draw_chase, 0.03),
    ("pumpkin glow", draw_pumpkin_glow, 0.02),
    ("candy corn", draw_candy_corn, 0.08),
    ("spooky sparkle", draw_spooky_sparkle, 0.04),
    ("ghost drift", draw_ghost_drift, 0.06),
    ("monster eyes", draw_monster_eyes, 0.02),
    ("blood drip", draw_blood_drip, 0.03),
    ("bat swarm", draw_bat_swarm, 0.03),
    ("cauldron bubbles", draw_cauldron_bubbles, 0.04),
    ("jack-o'-lantern fire", draw_fire, 0.03),
    ("lightning storm", draw_lightning_storm, 0.02),
]

mode = 0
last_press = 0

# this function runs by itself the moment the button is pressed
def button_pressed(pin):
    global mode, last_press
    now = ticks_ms()
    # a button "bounces" and can look like many presses, so we ignore
    # any press that comes too soon after the last one
    if ticks_diff(now, last_press) > DEBOUNCE_MS:
        mode = (mode + 1) % len(modes)      # % goes back to 0 after the last mode
        last_press = now

# call button_pressed when the pin falls from 1 (released) to 0 (pressed)
button.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)

print("Halloween costume ready! Press the button to change the pattern.")
current_mode = -1
step = 0
while True:
    if mode != current_mode:
        # the button changed the mode: start the new pattern fresh
        current_mode = mode
        step = 0
        strip.fill(black)
        print("Mode", current_mode, "-", modes[current_mode][0])
    name, draw, delay = modes[current_mode]
    draw(step)               # set the colors for this step
    strip.write()            # one write per step
    sleep(delay)
    step += 1
