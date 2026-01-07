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
