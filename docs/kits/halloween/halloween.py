# Halloween Party NeoPixel Pattern
# Features orange and purple themed patterns for spooky effects
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint
import config

# Hardware setup
NUMBER_PIXELS = config.NUMBER_PIXELS
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), NUMBER_PIXELS)

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
    """Orange pulsing effect like a jack-o'-lantern"""
    for brightness in range(20, 100, 2):
        factor = brightness / 100
        for i in range(NUMBER_PIXELS):
            strip[i] = fade_color(orange_bright, factor)
        strip.write()
        sleep(0.02)
    for brightness in range(100, 20, -2):
        factor = brightness / 100
        for i in range(NUMBER_PIXELS):
            strip[i] = fade_color(orange_bright, factor)
        strip.write()
        sleep(0.02)

def witch_chase():
    """Purple and orange dots chasing each other"""
    global counter
    # Purple dot moving forward
    strip[counter % NUMBER_PIXELS] = purple_bright
    # Orange dot moving backward
    strip[(NUMBER_PIXELS - counter) % NUMBER_PIXELS] = orange_bright
    strip.write()
    sleep(0.05)
    # Clear previous positions
    strip[counter % NUMBER_PIXELS] = black
    strip[(NUMBER_PIXELS - counter) % NUMBER_PIXELS] = black

def ghost_fade():
    """Ghostly white to purple fade effect"""
    global counter
    fade_length = 8
    for i in range(fade_length):
        pos = (counter + i) % NUMBER_PIXELS
        factor = 1.0 - (i / fade_length)
        if i < fade_length // 2:
            strip[pos] = fade_color(white_dim, factor)
        else:
            strip[pos] = fade_color(purple_dim, factor)
    strip.write()
    sleep(0.03)
    # Clear the tail
    strip[(counter - 1) % NUMBER_PIXELS] = black

def candy_corn_wave():
    """Orange, yellow, white bands moving like candy corn"""
    global counter
    band_size = NUMBER_PIXELS // 3
    for i in range(NUMBER_PIXELS):
        pos = (i + counter) % NUMBER_PIXELS
        if i < band_size:
            strip[pos] = orange_bright
        elif i < band_size * 2:
            strip[pos] = (255, 200, 0)  # yellow
        else:
            strip[pos] = white_dim
    strip.write()
    sleep(0.05)

def spooky_sparkle():
    """Random orange and purple sparkles"""
    # Add new sparkles
    for _ in range(3):
        pos = randint(0, NUMBER_PIXELS - 1)
        if randint(0, 1):
            strip[pos] = orange_bright if randint(0, 1) else purple_bright
    
    # Fade existing pixels
    for i in range(NUMBER_PIXELS):
        current = strip[i]
        if current != black:
            strip[i] = fade_color(current, 0.85)
    strip.write()
    sleep(0.05)

def monster_eyes():
    """Pairs of glowing eyes that blink"""
    global counter
    clear()
    # Create pairs of eyes
    eye_positions = [5, 15, 25]
    for pos in eye_positions:
        if pos < NUMBER_PIXELS - 1:
            # Blinking effect
            if counter % 40 < 35:  # Eyes open most of the time
                intensity = purple if (counter + pos) % 60 < 30 else orange
                strip[pos] = intensity
                strip[pos + 1] = intensity
    strip.write()
    sleep(0.05)

def halloween_rainbow():
    """Spooky rainbow with halloween colors"""
    global counter
    colors = [orange, purple, green_spooky, orange_dark, purple_dim, red_blood]
    color_count = len(colors)
    
    for i in range(NUMBER_PIXELS):
        color_index = ((i * color_count) // NUMBER_PIXELS + counter) % color_count
        strip[i] = colors[color_index]
    strip.write()
    sleep(0.03)

def creeping_shadows():
    """Dark shadows creeping with occasional orange/purple flashes"""
    global counter
    # Create dark base
    for i in range(NUMBER_PIXELS):
        strip[i] = (5, 0, 5)  # Very dark purple
    
    # Add creeping bright spots
    shadow_pos = counter % NUMBER_PIXELS
    for i in range(3):
        pos = (shadow_pos + i) % NUMBER_PIXELS
        if i == 1:  # Center is brightest
            strip[pos] = orange if counter % 40 < 20 else purple
        else:
            strip[pos] = orange_dark if counter % 40 < 20 else purple_dark
    strip.write()
    sleep(0.04)

def potion_bubbles():
    """Bubbling potion effect with purple and green"""
    # Random bubbles appear and rise
    if randint(0, 100) < 30:  # 30% chance of new bubble
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

print("Halloween Party Pattern Started!")
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