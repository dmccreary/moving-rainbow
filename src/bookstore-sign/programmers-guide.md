# Bookstore Sign - Pattern User Guide

This guide explains *how* the patterns in
[`pattern-mode-test.py`](pattern-mode-test.py) work. It is written for students
who already know a little Python and want to understand the ideas behind the
colorful animations. If you just want to run the sign, start with the
[README](README.md).

## Four big ideas

Almost every pattern in this program is built from the same four ideas. Learn
these and the rest is easy.

### 1. A pixel is just three numbers

Each LED is set with a tuple of three values - **red**, **green**, and **blue**
- where each runs from `0` (off) to `255` (full brightness):

```python
strip[0] = (255, 0, 0)   # pixel 0 is bright red
strip[1] = (0, 255, 255) # pixel 1 is cyan (green + blue)
strip.write()            # send the colors to the real LEDs
```

Nothing lights up until you call `strip.write()`. A common beginner mistake is
to set colors but forget to "push" them to the strip.

### 2. The color wheel turns one number into a rainbow

Mixing red, green, and blue by hand is tedious. The `wheel()` function does it
for you: give it a single number from `0` to `255` and it returns a rainbow
color. The numbers travel **red → green → blue → back to red**, so the wheel
wraps around smoothly with no hard edges.

```python
def wheel(pos):
    pos = pos & 255            # keep pos in the range 0-255
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
```

The trick `pos & 255` is a fast way to "wrap" any number back into 0-255. If
`pos` reaches 256 it becomes 0 again, which is why the rainbow loops forever.

### 3. Animation = drawing one frame at a time

A movie is just many still pictures shown quickly. These patterns work the same
way. Each pattern function draws **exactly one frame** and then returns. The
main loop calls it again and again:

```python
step()        # draw one frame of the current pattern
sleep(delay)  # wait a moment so our eyes can see it
```

To make something *move*, a pattern keeps a number that changes a little each
frame - for example `rainbow_offset` slides the rainbow sideways, and
`comet_pos` moves the bright dot forward one pixel. These "remembered" numbers
are called **state**, and they live in global variables at the top of the
program.

Why one frame at a time instead of a long animation loop? **So the buttons stay
responsive.** If a pattern ran a 60-second loop, you would have to wait up to a
minute for a button press to take effect. Short frames let the program notice a
new mode almost instantly.

### 4. The buttons interrupt the program

The buttons use an **interrupt** (the same technique as
[`01-test-buttons.py`](01-test-buttons.py)). Instead of the main loop constantly
asking "is the button pressed yet?", the Pico hardware calls a small function
the instant a button goes down:

```python
def button_callback(pin):
    global mode, last_time
    new_time = ticks_ms()
    if ticks_diff(new_time, last_time) > 200:   # debounce
        if pin is button_up:
            mode = (mode + 1) % NUMBER_MODES
        else:
            mode = (mode - 1) % NUMBER_MODES
        last_time = new_time
```

Two details to notice:

- **Debounce.** A real button "bounces" - one physical press can make the
  electrical contact several times in a few milliseconds. The
  `ticks_diff(...) > 200` check ignores any extra triggers within 200
  milliseconds, so one press counts as one press.
- **Wrap-around.** `% NUMBER_MODES` (the modulo operator) keeps `mode` inside
  the valid range. Past the last mode it returns to 0; below 0 it jumps to the
  last mode.

## How each pattern works

The `mode` variable selects what to draw. Mode 1 maps to the first pattern in
the `PATTERNS` list, mode 2 to the second, and so on. Here is what each one
does.

### Mode 1 - Color Letters

The simplest pattern. A list called `LETTER_LAYOUT` says which pixels belong to
each letter and what color it should be. The function walks the list and fills
in every pixel:

```python
for letter, start, end, color in LETTER_LAYOUT:
    for i in range(start, end + 1):   # +1 because end is inclusive
        strip[i] = color
strip.write()
```

This picture never moves, so there is no state to update. It is the same idea
as [`06-color-letter-test.py`](06-color-letter-test.py).

### Mode 2 - Rainbow Flow

Spreads the entire rainbow across the sign at once, then scrolls it. Each pixel
gets a wheel position based on **where it is** plus a moving `rainbow_offset`:

```python
for i in range(config.NUMBER_PIXELS):
    wheel_pos = (i * 256 // config.NUMBER_PIXELS + rainbow_offset) & 255
    strip[i] = wheel(wheel_pos)
strip.write()
rainbow_offset = (rainbow_offset + 1) & 255
```

`i * 256 // NUMBER_PIXELS` stretches the 0-255 rainbow evenly over all 134
pixels. Adding `rainbow_offset` shifts the whole rainbow one step each frame, so
the colors appear to flow along the sign.

### Mode 3 - Rainbow Solid

The whole sign is **one** color at a time, and that color slowly walks around
the wheel:

```python
color = wheel(rainbow_offset)
for i in range(config.NUMBER_PIXELS):
    strip[i] = color
strip.write()
rainbow_offset = (rainbow_offset + 1) & 255
```

Compare this with Rainbow Flow: same moving `rainbow_offset`, but here every
pixel shares the *same* wheel position instead of being spread out.

### Mode 4 - Color Sparkle

Each pixel has its **own** wheel position stored in the `pixel_values` list.
Every frame, each position nudges forward by a small random amount, so the
pixels drift through colors independently and the sign shimmers:

```python
for i in range(config.NUMBER_PIXELS):
    pixel_values[i] = (pixel_values[i] + random.randint(1, 3)) & 255
    strip[i] = wheel(pixel_values[i])
strip.write()
```

Because each pixel started at a random color (set in `reset_pattern_state`) and
moves at a slightly different rate, no two pixels stay in step.

### Mode 5 - Color Wipe

Fills the whole sign with one bright color from the `WIPE_COLORS` list, holds
it for a moment, then switches to the next color. A frame counter creates the
"hold":

```python
color = WIPE_COLORS[wipe_index]
for i in range(config.NUMBER_PIXELS):
    strip[i] = color
strip.write()
wipe_frame += 1
if wipe_frame >= WIPE_HOLD_FRAMES:   # held long enough?
    wipe_frame = 0
    wipe_index = (wipe_index + 1) % len(WIPE_COLORS)
```

At 0.05 seconds per frame and `WIPE_HOLD_FRAMES = 16`, each color shows for
about 0.8 seconds. Counting frames (instead of using a long `sleep`) keeps the
buttons responsive.

### Mode 6 - Comet

A bright dot races along the sign and leaves a glowing tail behind it. The trick
is to **dim every pixel a little** each frame, then redraw a bright head:

```python
for i in range(config.NUMBER_PIXELS):
    r, g, b = strip[i]
    strip[i] = (r * 3 // 4, g * 3 // 4, b * 3 // 4)  # fade the tail
strip[comet_pos] = wheel(comet_hue)                  # bright head
strip.write()
comet_pos = (comet_pos + 1) % config.NUMBER_PIXELS
comet_hue = (comet_hue + 2) & 255
```

Multiplying each color by `3 // 4` (three-quarters) every frame makes older
pixels fade toward black, which is what gives the comet its tail. The head also
slowly changes color because `comet_hue` creeps around the wheel.

## How Mode 0 (Auto-Cycle) works

Mode 0 plays every pattern in turn, 60 seconds each, without you touching the
buttons. It uses a **timer** instead of a long `sleep` so it can still react to
button presses.

The program remembers when the current pattern started (`auto_start`). Every
loop it checks how much time has passed:

```python
now = ticks_ms()
if ticks_diff(now, auto_start) >= AUTO_CYCLE_MS:   # 60 seconds?
    auto_start = now
    auto_index = (auto_index + 1) % len(PATTERNS)  # next pattern
    clear_strip()
    reset_pattern_state()
```

`ticks_ms()` returns the number of milliseconds since the Pico started, and
`ticks_diff()` safely measures the gap between two readings. When 60,000
milliseconds have passed, it advances to the next pattern and resets its state
for a clean start.

## Switching modes cleanly

Whenever `mode` changes, the main loop notices that it differs from `old_mode`
and does some tidy-up so patterns never bleed into each other:

```python
if mode != old_mode:
    old_mode = mode
    builtin_led.toggle()      # blink the on-board LED
    clear_strip()             # blank the sign
    reset_pattern_state()     # reset offsets, counters, sparkle colors
    ...
```

`reset_pattern_state()` sets `rainbow_offset`, `wipe_index`, `comet_pos`, and
the rest back to known values and re-randomizes the sparkle colors, so each
pattern always begins the same way.

## Try it yourself

Once you understand the patterns, experiment:

- **Change the speed.** Each entry in `PATTERNS` ends with a delay in seconds.
  Smaller numbers animate faster.
- **Change the auto-cycle time.** Edit `AUTO_CYCLE_MS` (it is `60 * 1000` for 60
  seconds). Try `10 * 1000` for a quick demo.
- **Recolor the letters.** Edit the colors in `LETTER_LAYOUT` (Mode 1) or the
  list in `WIPE_COLORS` (Mode 5).
- **Add your own pattern.** Write a function that draws one frame, then add a
  `('My Pattern', my_function, 0.05)` line to the `PATTERNS` list. The mode count
  updates automatically - no other changes needed.

## Troubleshooting

| Problem | Likely cause |
|---------|--------------|
| Nothing lights up | Forgot `strip.write()`, or `NEOPIXEL_PIN` is wrong in `config.py` |
| One press skips two modes | The button is bouncing - increase the `200` in the debounce check |
| Buttons feel sluggish | A pattern's delay is too long; lower the delay in `PATTERNS` |
| Wrong letters light up | The pixel ranges in `LETTER_LAYOUT` don't match your wiring |
| Colors look dim or pinkish | Power supply can't drive all 134 LEDs at full brightness |
