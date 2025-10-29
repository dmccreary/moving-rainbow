# Halloween Party NeoPixel Pattern - Power Limited Edition
# Features orange and purple themed patterns for spooky effects
# Limited to 1/3 of pixels on at any time to reduce power consumption
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint
import config

# Hardware setup
NUMBER_PIXELS = config.NUMBER_PIXELS
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), NUMBER_PIXELS)

# Power limiting - maximum 1/3 of pixels can be lit
MAX_LIT_PIXELS = NUMBER_PIXELS // 3
print(f"Power Limited Mode: Maximum {MAX_LIT_PIXELS} pixels lit at once")

BUTTON_PIN_1 = config.BUTTON_PIN_1
BUTTON_PIN_2 = config.BUTTON_PIN_2

button_presses = 0
last_time = 0

builtin_led = machine.Pin(25, Pin.OUT)
button1 = machine.Pin(BUTTON_PIN_1, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(BUTTON_PIN_2, machine.Pin.IN, machine.Pin.PULL_UP)

# Halloween color palette
orange = (255, 80, 0)
orange_bright = (255, 120, 0)
orange_dim = (128, 40, 0)
orange_dark = (64, 20, 0)

purple = (128, 0, 255)
purple_bright = (180, 0, 255)
purple_dim = (64, 0, 128)
purple_dark = (32, 0, 64)

black = (0, 0, 0)
white_dim = (30, 30, 30)
green_spooky = (0, 50, 0)
red_blood = (150, 0, 0)

# Pattern configurations
mode_list = ['auto cycle', 'pumpkin pulse', 'witch chase', 'ghost fade', 
             'candy corn wave', 'spooky sparkle', 'monster eyes',
             'halloween rainbow', 'creeping shadows', 'potion bubbles']
mode_count = len(mode_list)

# Button interrupt handler
def button_pressed_handler(pin):
    global mode, last_time
    new_time = ticks_ms()
    if (new_time - last_time) > 200:
        pin_str = str(pin)
        gpio_index = pin_str.find("GPIO")
        if gpio_index != -1:
            start_index = gpio_index + 4
            end_index = start_index
            while end_index < len(pin_str) and pin_str[end_index].isdigit():
                end_index += 1
            pin_num = int(pin_str[start_index:end_index])
        else:
            if pin is button1:
                pin_num = BUTTON_PIN_1
            else:
                pin_num = BUTTON_PIN_2
        
        if pin_num == BUTTON_PIN_1:
            mode += 1
        else:
            mode -= 1
        mode = mode % mode_count
        last_time = new_time
        print(f'Mode: {mode} - {mode_list[mode]}')

button1.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed_handler)
button2.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_pressed_handler)

# Helper functions
def clear():
    for i in range(NUMBER_PIXELS):
        strip[i] = black
    strip.write()

def fade_color(color, factor):
    """Fade a color by a factor (0.0 to 1.0)"""
    return (int(color[0] * factor), int(color[1] * factor), int(color[2] * factor))

# Pattern functions
def pumpkin_pulse():
    """Orange pulsing effect like a jack-o'-lantern - power limited"""
    clear()
    # Only light every 3rd pixel for power saving
    for brightness in range(20, 100, 2):
        factor = brightness / 100
        for i in range(0, NUMBER_PIXELS, 3):  # Every 3rd pixel
            strip[i] = fade_color(orange_bright, factor)
        strip.write()
        sleep(0.02)
    for brightness in range(100, 20, -2):
        factor = brightness / 100
        for i in range(0, NUMBER_PIXELS, 3):  # Every 3rd pixel
            strip[i] = fade_color(orange_bright, factor)
        strip.write()
        sleep(0.02)

def witch_chase():
    """Purple and orange dots chasing each other - power limited with tails"""
    global counter
    clear()
    # Create small comet tails (3 pixels each, 6 total)
    for i in range(3):
        # Purple comet moving forward
        purple_pos = (counter + i) % NUMBER_PIXELS
        intensity = 1.0 - (i * 0.3)  # Fade the tail
        strip[purple_pos] = fade_color(purple_bright, intensity)
        
        # Orange comet moving backward
        orange_pos = (NUMBER_PIXELS - counter - i) % NUMBER_PIXELS
        strip[orange_pos] = fade_color(orange_bright, intensity)
    
    strip.write()
    sleep(0.05)

def ghost_fade():
    """Ghostly white to purple fade effect - power limited"""
    global counter
    clear()
    fade_length = min(6, MAX_LIT_PIXELS)  # Maximum 6 pixels or 1/3 of strip
    for i in range(fade_length):
        pos = (counter + i * 2) % NUMBER_PIXELS  # Skip pixels to spread effect
        factor = 1.0 - (i / fade_length)
        if i < fade_length // 2:
            strip[pos] = fade_color(white_dim, factor)
        else:
            strip[pos] = fade_color(purple_dim, factor)
    strip.write()
    sleep(0.03)

def candy_corn_wave():
    """Orange, yellow, white bands moving like candy corn - power limited"""
    global counter
    clear()
    # Create sparse bands - only light specific positions
    band_positions = []
    for i in range(0, NUMBER_PIXELS, 3):  # Every 3rd position
        band_positions.append(i)
    
    for i, pos in enumerate(band_positions[:MAX_LIT_PIXELS]):
        actual_pos = (pos + counter) % NUMBER_PIXELS
        # Cycle through candy corn colors
        if i % 3 == 0:
            strip[actual_pos] = orange_bright
        elif i % 3 == 1:
            strip[actual_pos] = (255, 200, 0)  # yellow
        else:
            strip[actual_pos] = white_dim
    strip.write()
    sleep(0.05)

def spooky_sparkle():
    """Random orange and purple sparkles - power limited"""
    clear()
    # Limit sparkles to MAX_LIT_PIXELS
    lit_pixels = []
    
    # Generate random positions for sparkles
    for _ in range(min(MAX_LIT_PIXELS, randint(3, MAX_LIT_PIXELS))):
        pos = randint(0, NUMBER_PIXELS - 1)
        if pos not in lit_pixels:
            lit_pixels.append(pos)
            # Random color and intensity
            if randint(0, 1):
                color = orange_bright if randint(0, 1) else purple_bright
            else:
                color = orange_dim if randint(0, 1) else purple_dim
            strip[pos] = color
    
    strip.write()
    sleep(0.05)

def monster_eyes():
    """Pairs of glowing eyes that blink - power limited"""
    global counter
    clear()
    # Limit eye pairs to stay within power budget
    max_pairs = MAX_LIT_PIXELS // 2  # Each pair uses 2 pixels
    
    # Create pairs of eyes with proper spacing
    eye_spacing = max(4, NUMBER_PIXELS // max_pairs)
    
    for i in range(max_pairs):
        pos = (i * eye_spacing) % NUMBER_PIXELS
        if pos < NUMBER_PIXELS - 1:
            # Blinking effect
            if counter % 40 < 35:  # Eyes open most of the time
                # Alternate colors between pairs
                intensity = purple if i % 2 == 0 else orange
                strip[pos] = intensity
                strip[pos + 1] = intensity
    strip.write()
    sleep(0.05)

def halloween_rainbow():
    """Spooky rainbow with halloween colors - power limited"""
    global counter
    clear()
    colors = [orange, purple, green_spooky, orange_dark, purple_dim, red_blood]
    color_count = len(colors)
    
    # Only light every Nth pixel to stay within power limit
    step = max(3, NUMBER_PIXELS // MAX_LIT_PIXELS)
    
    for i in range(0, NUMBER_PIXELS, step):
        color_index = ((i * color_count) // NUMBER_PIXELS + counter) % color_count
        strip[i] = colors[color_index]
    strip.write()
    sleep(0.03)

def creeping_shadows():
    """Dark shadows creeping with occasional orange/purple flashes - power limited"""
    global counter
    clear()
    
    # Create a moving window of lit pixels
    window_size = min(5, MAX_LIT_PIXELS)
    shadow_pos = counter % NUMBER_PIXELS
    
    for i in range(window_size):
        pos = (shadow_pos + i * 2) % NUMBER_PIXELS  # Spread out the effect
        if i == window_size // 2:  # Center is brightest
            strip[pos] = orange if counter % 40 < 20 else purple
        else:
            # Dimmer surrounding pixels
            strip[pos] = orange_dark if counter % 40 < 20 else purple_dark
    strip.write()
    sleep(0.04)

def potion_bubbles():
    """Bubbling potion effect with purple and green - power limited"""
    global counter
    
    # Count currently lit pixels
    lit_count = sum(1 for i in range(NUMBER_PIXELS) if strip[i] != black)
    
    # Add new bubble only if under limit
    if lit_count < MAX_LIT_PIXELS and randint(0, 100) < 30:
        bubble_start = randint(0, NUMBER_PIXELS // 2)
        strip[bubble_start] = purple_bright if randint(0, 1) else green_spooky
    
    # Move bubbles up and fade
    temp = [black] * NUMBER_PIXELS
    for i in range(NUMBER_PIXELS - 1):
        current = strip[i]
        if current != black:
            # Move up with slight fade
            next_pos = i + 1
            if next_pos < NUMBER_PIXELS:
                temp[next_pos] = fade_color(current, 0.9)
    
    # Apply the new positions
    for i in range(NUMBER_PIXELS):
        strip[i] = temp[i]
    strip.write()
    sleep(0.03)

# Auto cycle parameters
auto_cycle_time = 0
PATTERN_DURATION = 5000  # 5 seconds per pattern in auto mode
current_auto_pattern = 0

# Main variables
mode = 0
counter = 0
last_mode = -1

print("Halloween Party Pattern Started! 🎃")
print(f"Power Limited Mode: Maximum {MAX_LIT_PIXELS}/{NUMBER_PIXELS} pixels lit")
print(f"Mode: {mode} - {mode_list[mode]}")

# Main loop
while True:
    if mode != last_mode:
        clear()
        counter = 0
        last_mode = mode
        if mode != 0:
            print(f'Mode: {mode} - {mode_list[mode]}')
    
    # Auto cycle mode
    if mode == 0:
        current_time = ticks_ms()
        if current_time - auto_cycle_time > PATTERN_DURATION:
            current_auto_pattern = (current_auto_pattern + 1) % (mode_count - 1)
            auto_cycle_time = current_time
            clear()
            print(f'Auto cycling to: {mode_list[current_auto_pattern + 1]}')
        
        # Run current auto pattern
        if current_auto_pattern == 0:
            pumpkin_pulse()
        elif current_auto_pattern == 1:
            witch_chase()
        elif current_auto_pattern == 2:
            ghost_fade()
        elif current_auto_pattern == 3:
            candy_corn_wave()
        elif current_auto_pattern == 4:
            spooky_sparkle()
        elif current_auto_pattern == 5:
            monster_eyes()
        elif current_auto_pattern == 6:
            halloween_rainbow()
        elif current_auto_pattern == 7:
            creeping_shadows()
        elif current_auto_pattern == 8:
            potion_bubbles()
    
    # Manual mode patterns
    elif mode == 1:
        pumpkin_pulse()
    elif mode == 2:
        witch_chase()
    elif mode == 3:
        ghost_fade()
    elif mode == 4:
        candy_corn_wave()
    elif mode == 5:
        spooky_sparkle()
    elif mode == 6:
        monster_eyes()
    elif mode == 7:
        halloween_rainbow()
    elif mode == 8:
        creeping_shadows()
    elif mode == 9:
        potion_bubbles()
    
    counter += 1
    counter = counter % (NUMBER_PIXELS * 10)  # Larger counter for varied effects