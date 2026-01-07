# JASON Nightlight Development Session Log

**Date:** 2026-01-07
**Project:** Moving Rainbow - JASON LED Sign
**Files Created/Modified:**
- `src/jason-sign/main.py`
- `src/jason-sign/jason-colors.py`
- `src/jason-sign/config.py`

---

## Prompt 1: Create Initial JASON Sign Program

**User:**
> Please create a new MicroPython program for a LED sign that spells "JASON". Make each letter a different color.
>
> ```python
> # Test of the JASON sign
> from machine import Pin
> from neopixel import NeoPixel
> from utime import sleep
> import config
>
> strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
>
> # this is the 65th pixel where i=0 is the first pixel
> n = 64
>
> j = (0, 7)
> a = (8, 20)
> s = (21, 33)
> o = (34, 47)
> n = (48, 64)
>
> while True:
>     strip[n] = (100,0,0)
>     strip.write()
>     sleep(1)
>     strip[n] = (0,0,0)
>     strip.write()
>     sleep(1)
> ```

**Response:**
Created `src/jason-sign/jason-colors.py` with each letter assigned a different color:

| Letter | Pixels | Color |
|--------|--------|-------|
| J | 0-7 | Red |
| A | 8-20 | Orange |
| S | 21-33 | Green |
| O | 34-47 | Blue |
| N | 48-64 | Purple |

Also created `src/jason-sign/config.py` with 65 pixels configured.

---

## Prompt 2: Create Multi-Mode Main Program

**User:**
> Go into @src/jason-sign/ and create a new main.py file. This file uses the mode buttons to change the mode. The default mode is a nightlight. A rainbow pattern goes on when the light is out. The pattern stays on for 10 minutes and then slowly fades over the remaining 10 minutes. Turning the lights on will reset the sign to mode 0 - the default mode. If the user presses either mode button, the sign will display one color for each letter for mode = 1. For mode = 2 the sign will rotate through all the colors of the rainbow uniform for the entire sign the same color. For mode = 3 the colors will all be random slowly changing each pixel through 0-255 using the wheel() function.

**Response:**
Created `src/jason-sign/main.py` with 4 modes:

| Mode | Description |
|------|-------------|
| 0 | **Nightlight**: Rainbow pattern when dark. Full brightness for 10 min, then fades over next 10 min. Resets when lights come on. |
| 1 | **Static Letters**: J=Red, A=Orange, S=Green, O=Blue, N=Purple |
| 2 | **Rainbow Cycle**: Entire sign rotates through rainbow colors uniformly |
| 3 | **Random**: Each pixel independently drifts through wheel() colors |

**Controls:**
- **Button 1**: Mode +1 (cycles 0→1→2→3→0)
- **Button 2**: Mode -1 (cycles backwards)
- **Photosensor**: Triggers nightlight in mode 0 when dark

---

## Prompt 3: Full Rainbow Across Strip

**User:**
> This works but the one change is when in mode 0, set each pixel 0 to 64 to a value of wheel() so that the entire rainbow of colors is shown. Slowly move the colors down the strip.

**Response:**
Updated `mode_nightlight()` to spread the full rainbow spectrum across all 65 pixels using the formula:
```python
wheel_pos = (i * 255 // 64 + rainbow_offset) % 256
```

This maps pixel 0 to wheel position 0 and pixel 64 to position 255, showing the complete rainbow once across the sign. The `rainbow_offset` increment makes colors move down the strip.

---

## Prompt 4: Add Countdown Timer

**User:**
> Add a countdown timer on the console every 15 seconds to show how much time is left for the nightlight to turn off.

**Response:**
Added countdown timer that prints every 15 seconds:
```
Nightlight activated - 20:00 remaining
Nightlight: 19:45 remaining (full)
Nightlight: 19:30 remaining (full)
...
Nightlight: 09:45 remaining (fading)
...
Nightlight off - timer complete
```

The phase indicator shows "full" during the first 10 minutes and "fading" during the fade-out period.

---

## Prompt 5: Gamma Correction for Perceptual Fade

**User:**
> This code is pretty good. However, I would like to work on a gradual fade. Right now it "appears" that the sign is really bright when we turn the lights off about 19 minutes. It is only in the last 30 seconds that we perceive it to dim, and then it goes off really fast. Can you use a gamma corrected table of brightness so the brightness appears to fade slowly over the final 10 minutes? Keep just a few pixels on for the final minute.

**Response:**
Added gamma correction (GAMMA = 2.5) for perceptually linear fading:

**Gamma Correction Effect:**
- Linear 100% → Output 100%
- Linear 75% → Output ~41%
- Linear 50% → Output ~18%
- Linear 25% → Output ~3%

**Updated Timeline:**
| Time | Phase | Behavior |
|------|-------|----------|
| 0-10 min | full | Full brightness rainbow |
| 10-19 min | fading | Gamma-corrected fade, all pixels |
| 19-20 min | final | Only 5 pixels (one per letter), max 30% brightness, fading to off |

**Final Pixels:** `[3, 14, 27, 40, 56]` - one pixel near the middle of each letter (J, A, S, O, N)

---

## Final Code: main.py

```python
# JASON LED Sign - Multi-Mode Controller
# Modes:
#   0 - Nightlight: Rainbow when dark, fades after 10 min, off after 20 min
#   1 - Static: Each letter a different color
#   2 - Rainbow cycle: Entire sign rotates through rainbow colors
#   3 - Random: Each pixel slowly changes through random colors
# Now with gamma correction for smoother fading!

from machine import Pin, ADC
from neopixel import NeoPixel
from utime import sleep, ticks_ms, ticks_diff
import config
import random

# Hardware setup
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
button1 = Pin(config.BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button2 = Pin(config.BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)
photosensor = ADC(Pin(config.ADC_PIN_0))

# Constants
LIGHT_THRESHOLD = 30000  # Below this = dark (adjust based on your sensor)
NIGHTLIGHT_ON_TIME = 10 * 60 * 1000    # 10 minutes in ms
NIGHTLIGHT_FADE_TIME = 10 * 60 * 1000  # 10 minutes fade in ms
NIGHTLIGHT_FINAL_MIN = 1 * 60 * 1000   # Final minute - just a few pixels
DEBOUNCE_TIME = 200  # Button debounce in ms
GAMMA = 2.5  # Gamma correction for perceptually linear fade

# Pixels to keep on during final minute (one per letter, middle-ish)
FINAL_PIXELS = [3, 14, 27, 40, 56]

# State variables
current_mode = 0
nightlight_start = 0
nightlight_active = False
last_button_time = 0
last_countdown_time = 0
rainbow_offset = 0
pixel_values = [0] * config.NUMBER_PIXELS  # For mode 3

COUNTDOWN_INTERVAL = 15 * 1000  # Print countdown every 15 seconds

# Colors for each letter (mode 1)
LETTER_COLORS = {
    'J': (255, 0, 0),      # Red
    'A': (255, 128, 0),    # Orange
    'S': (0, 255, 0),      # Green
    'O': (0, 0, 255),      # Blue
    'N': (128, 0, 255)     # Purple
}

def wheel(pos):
    """Generate rainbow colors across 0-255 positions"""
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

def scale_color(color, brightness):
    """Scale a color tuple by brightness (0.0 to 1.0)"""
    return (int(color[0] * brightness),
            int(color[1] * brightness),
            int(color[2] * brightness))

def gamma_correct(linear_brightness):
    """Apply gamma correction for perceptually linear fade"""
    return linear_brightness ** GAMMA

def clear_strip():
    """Turn off all pixels"""
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()

def is_dark():
    """Check if room is dark based on photosensor"""
    reading = photosensor.read_u16()
    return reading < LIGHT_THRESHOLD

def check_buttons():
    """Check for button presses and change mode"""
    global current_mode, last_button_time, nightlight_active

    now = ticks_ms()
    if ticks_diff(now, last_button_time) < DEBOUNCE_TIME:
        return False

    if button1.value() == 0 or button2.value() == 0:
        last_button_time = now
        nightlight_active = False  # Exit nightlight mode on button press

        if button1.value() == 0:
            current_mode = (current_mode + 1) % 4
        else:
            current_mode = (current_mode - 1) % 4

        print("Mode:", current_mode)
        return True

    return False

def mode_nightlight():
    """Mode 0: Nightlight with rainbow pattern"""
    global nightlight_start, nightlight_active, rainbow_offset, last_countdown_time

    if is_dark():
        now = ticks_ms()

        if not nightlight_active:
            # Just became dark - start nightlight
            nightlight_active = True
            nightlight_start = now
            last_countdown_time = now
            print("Nightlight activated - 20:00 remaining")

        elapsed = ticks_diff(now, nightlight_start)
        total_time = NIGHTLIGHT_ON_TIME + NIGHTLIGHT_FADE_TIME

        # Print countdown every 15 seconds
        if ticks_diff(now, last_countdown_time) >= COUNTDOWN_INTERVAL:
            last_countdown_time = now
            remaining_ms = total_time - elapsed
            if remaining_ms > 0:
                remaining_sec = remaining_ms // 1000
                minutes = remaining_sec // 60
                seconds = remaining_sec % 60
                if elapsed < NIGHTLIGHT_ON_TIME:
                    phase = "full"
                elif elapsed < total_time - NIGHTLIGHT_FINAL_MIN:
                    phase = "fading"
                else:
                    phase = "final"
                print("Nightlight: {:02d}:{:02d} remaining ({})".format(minutes, seconds, phase))

        if elapsed < NIGHTLIGHT_ON_TIME:
            # Full brightness rainbow
            brightness = 1.0
            in_final_minute = False
        elif elapsed < total_time - NIGHTLIGHT_FINAL_MIN:
            # Main fading phase (9 minutes) - apply gamma correction
            fade_elapsed = elapsed - NIGHTLIGHT_ON_TIME
            fade_duration = NIGHTLIGHT_FADE_TIME - NIGHTLIGHT_FINAL_MIN
            linear_brightness = 1.0 - (fade_elapsed / fade_duration)
            brightness = gamma_correct(linear_brightness)
            in_final_minute = False
        elif elapsed < total_time:
            # Final minute - just a few dim pixels
            final_elapsed = elapsed - (total_time - NIGHTLIGHT_FINAL_MIN)
            linear_brightness = 1.0 - (final_elapsed / NIGHTLIGHT_FINAL_MIN)
            brightness = gamma_correct(linear_brightness) * 0.3  # Max 30% in final minute
            in_final_minute = True
        else:
            # Fully faded - turn off
            brightness = 0.0
            in_final_minute = False
            if nightlight_active:
                print("Nightlight off - timer complete")

        # Display pattern
        for i in range(config.NUMBER_PIXELS):
            if in_final_minute:
                # Only light the few selected pixels during final minute
                if i in FINAL_PIXELS:
                    wheel_pos = (i * 255 // 64 + rainbow_offset) % 256
                    color = wheel(wheel_pos)
                    strip[i] = scale_color(color, brightness)
                else:
                    strip[i] = (0, 0, 0)
            else:
                # Full rainbow spectrum across all pixels
                wheel_pos = (i * 255 // 64 + rainbow_offset) % 256
                color = wheel(wheel_pos)
                strip[i] = scale_color(color, brightness)
        strip.write()
        rainbow_offset = (rainbow_offset + 1) % 256

    else:
        # Room is lit - reset nightlight
        if nightlight_active:
            nightlight_active = False
            clear_strip()
            print("Nightlight deactivated - room is lit")

def mode_static_letters():
    """Mode 1: Each letter a different static color"""
    for letter, (start, end) in config.LETTERS.items():
        color = LETTER_COLORS[letter]
        for i in range(start, end + 1):
            strip[i] = color
    strip.write()

def mode_rainbow_cycle():
    """Mode 2: Entire sign rotates through rainbow colors"""
    global rainbow_offset

    color = wheel(rainbow_offset)
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()
    rainbow_offset = (rainbow_offset + 1) % 256

def mode_random_pixels():
    """Mode 3: Each pixel slowly changes through random wheel positions"""
    global pixel_values

    for i in range(config.NUMBER_PIXELS):
        # Slowly increment each pixel's wheel position by random small amount
        pixel_values[i] = (pixel_values[i] + random.randint(1, 3)) % 256
        strip[i] = wheel(pixel_values[i])
    strip.write()

# Initialize random pixel values for mode 3
for i in range(config.NUMBER_PIXELS):
    pixel_values[i] = random.randint(0, 255)

print("JASON Sign Starting - Mode 0 (Nightlight)")
clear_strip()

# Main loop
while True:
    # Check for button presses
    check_buttons()

    # Run current mode
    if current_mode == 0:
        mode_nightlight()
        sleep(0.05)
    elif current_mode == 1:
        mode_static_letters()
        sleep(0.1)
    elif current_mode == 2:
        mode_rainbow_cycle()
        sleep(0.02)
    elif current_mode == 3:
        mode_random_pixels()
        sleep(0.05)
```

---

## Config File: config.py

```python
# Moving Rainbow Configuration file
# This file contains the hardware configuration for your kit

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 65

# Pins to change the sign mode
BUTTON_PIN_1 = 15
BUTTON_PIN_2 = 14

# Photoresistor ADC pin
ADC_PIN_0 = 26

# Define pixel ranges for each letter (start, end) - end is inclusive
LETTERS = {
    'J': (0, 7),
    'A': (8, 20),
    'S': (21, 33),
    'O': (34, 47),
    'N': (48, 64)
}
```

---

## Key Learnings

1. **Gamma Correction**: Human perception of brightness is logarithmic. Linear fading appears to stay bright then suddenly drop. Using `brightness ** 2.5` creates perceptually smooth fading.

2. **Nightlight UX**: A gradual transition from full display to just a few dim pixels helps users fall asleep without abrupt darkness.

3. **wheel() Function**: Maps 0-255 to full RGB rainbow spectrum, useful for smooth color transitions.

4. **Photosensor Integration**: Using ADC to read ambient light levels enables automatic nightlight activation.
