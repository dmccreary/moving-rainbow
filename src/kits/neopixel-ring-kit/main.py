from neopixel import NeoPixel
from machine import ADC, Pin
from utime import sleep, ticks_ms
import config
import random

# Pin definitions
NEOPIXEL_PIN = 0
NUMBER_PIXELS = 16
BUTTON_PIN_A = 14  # Button to go to next mode
BUTTON_PIN_B = 15  # Button to go to previous mode

# Initialize NeoPixels
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Initialize potentiometers
brightness_pot = ADC(config.POT_1_PIN)  # First potentiometer for brightness
speed_pot = ADC(config.POT_2_PIN)       # Second potentiometer for speed

# Initialize buttons with pull-up resistors
button_a = Pin(BUTTON_PIN_A, Pin.IN, Pin.PULL_UP)
button_b = Pin(BUTTON_PIN_B, Pin.IN, Pin.PULL_UP)

# Set up the built-in LED for visual feedback on button presses
builtin_led = Pin(25, Pin.OUT)

# Global variables for button control
current_mode = 0
MAX_MODES = 9  # Total number of modes (0-8)
last_time = 0  # Used for debouncing
button_change = False  # Flag to indicate mode change

def wheel(pos):
    """
    Input a value 0 to 255 to get a color value.
    The colors are a transition r - g - b - back to r.
    """
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def adjust_brightness(color, brightness_factor):
    """
    Adjust RGB color brightness by multiplying each component by brightness_factor (0.0-1.0)
    """
    r, g, b = color
    r = int(r * brightness_factor)
    g = int(g * brightness_factor)
    b = int(b * brightness_factor)
    return (r, g, b)

# Button callback function for mode changes
def button_callback(pin):
    global current_mode, last_time, button_change
    new_time = ticks_ms()
    # Debounce - if it has been more that 1/5 of a second since the last event
    if (new_time - last_time) > 200:
        if pin == button_a:
            # Increment mode
            current_mode = (current_mode + 1) % MAX_MODES
        else:
            # Decrement mode (with wrap-around)
            current_mode = (current_mode - 1) % MAX_MODES
        
        last_time = new_time
        button_change = True
        builtin_led.toggle()  # Toggle LED for visual feedback
        print(f"Mode changed to: {current_mode}")

# Register button interrupt handlers
button_a.irq(trigger=Pin.IRQ_FALLING, handler=lambda p: button_callback(button_a))
button_b.irq(trigger=Pin.IRQ_FALLING, handler=lambda p: button_callback(button_b))

# Mode 0: Rainbow colors (original mode)
def mode_rainbow(position, brightness_factor):
    for i in range(NUMBER_PIXELS):
        color_pos = (position + i * (256 // NUMBER_PIXELS)) % 256
        base_color = wheel(color_pos)
        strip[i] = adjust_brightness(base_color, brightness_factor)

# Mode 1: Red, white, and blue spinning
def mode_rwb(position, brightness_factor):
    colors = [(255, 0, 0), (255, 255, 255), (0, 0, 255)]  # Red, White, Blue
    for i in range(NUMBER_PIXELS):
        color_index = (position//10 + i) % 3
        strip[i] = adjust_brightness(colors[color_index], brightness_factor)

# Mode 2: Red and green spinning
def mode_red_green(position, brightness_factor):
    colors = [(255, 0, 0), (0, 255, 0)]  # Red, Green
    for i in range(NUMBER_PIXELS):
        color_index = (position//10 + i) % 2
        strip[i] = adjust_brightness(colors[color_index], brightness_factor)

# Mode 3: Green and white spinning
def mode_green_white(position, brightness_factor):
    colors = [(0, 255, 0), (255, 255, 255)]  # Green, White
    for i in range(NUMBER_PIXELS):
        color_index = (position//10 + i) % 2
        strip[i] = adjust_brightness(colors[color_index], brightness_factor)

# Mode 4: Purple and green spinning
def mode_purple_green(position, brightness_factor):
    colors = [(160, 32, 240), (0, 255, 0)]  # Purple, Green
    for i in range(NUMBER_PIXELS):
        color_index = (position//10 + i) % 2
        strip[i] = adjust_brightness(colors[color_index], brightness_factor)

# Mode 5: Random colors for each pixel
def mode_random(position, brightness_factor):
    # Only update colors occasionally based on position to avoid constant flickering
    if position % 5 == 0:
        for i in range(NUMBER_PIXELS):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            strip[i] = adjust_brightness((r, g, b), brightness_factor)

# Mode 6: Yellow and orange candle flickering
def mode_candle(position, brightness_factor):
    base_colors = [(255, 180, 0), (255, 100, 0)]  # Yellow, Orange
    
    for i in range(NUMBER_PIXELS):
        # Alternate base colors
        base_color = base_colors[i % 2]
        
        # Add random flickering
        flicker = random.uniform(0.7, 1.0)
        r = int(base_color[0] * flicker)
        g = int(base_color[1] * flicker)
        b = int(base_color[2] * flicker)
        
        strip[i] = adjust_brightness((r, g, b), brightness_factor)

# Mode 7: Theater chase of red, green, and blue
def mode_theater_chase(position, brightness_factor):
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
    
    chase_pos = position % 3
    for i in range(NUMBER_PIXELS):
        if i % 3 == chase_pos:
            color_index = (i // 3) % 3
            strip[i] = adjust_brightness(colors[color_index], brightness_factor)
        else:
            strip[i] = (0, 0, 0)  # Off

# Mode 8: Blue comet tail
def mode_comet(position, brightness_factor):
    # Clear all pixels
    for i in range(NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    
    # Calculate comet head position
    head_pos = position % NUMBER_PIXELS
    
    # Set comet head (brightest)
    strip[head_pos] = adjust_brightness((0, 64, 255), brightness_factor)
    
    # Set comet tail (fading)
    for i in range(1, 5):  # Tail length of 4 pixels
        tail_pos = (head_pos - i) % NUMBER_PIXELS
        tail_brightness = (5-i) / 5.0  # Fade from 4/5 to 1/5 brightness
        strip[tail_pos] = adjust_brightness((0, 32, 128), brightness_factor * tail_brightness)

# Main function to handle all modes
def update_display(mode, position, brightness_factor):
    if mode == 0:
        mode_rainbow(position, brightness_factor)
    elif mode == 1:
        mode_rwb(position, brightness_factor)
    elif mode == 2:
        mode_red_green(position, brightness_factor)
    elif mode == 3:
        mode_green_white(position, brightness_factor)
    elif mode == 4:
        mode_purple_green(position, brightness_factor)
    elif mode == 5:
        mode_random(position, brightness_factor)
    elif mode == 6:
        mode_candle(position, brightness_factor)
    elif mode == 7:
        mode_theater_chase(position, brightness_factor)
    elif mode == 8:
        mode_comet(position, brightness_factor)

# Set initial position
position = 0

print('Multimode NeoPixel control started.')
print('- Pot 1: Brightness')
print('- Pot 2: Speed')
print('- Button A: Next mode')
print('- Button B: Previous mode')
print(f'Current Mode: {current_mode}')

while True:
    # Read potentiometer values (0-65535)
    brightness_value = brightness_pot.read_u16()
    speed_value = speed_pot.read_u16()
    
    # Convert brightness to a factor between 0.0 and 1.0
    brightness_factor = brightness_value / 65535.0
    
    # Convert speed to a delay between 0.001 (fast) and 0.1 (slow) seconds
    # Invert the relationship so turning clockwise increases speed
    speed_delay = 0.1 - ((speed_value / 65535.0) * 0.099)
    
    # Update display based on current mode
    update_display(current_mode, position, brightness_factor)
    
    # Update the strip
    strip.write()
    
    # Increment position for animation effects
    position = (position + 1) % 256
    
    # Reset button change flag
    if button_change:
        button_change = False
    
    # Pause based on speed potentiometer
    sleep(speed_delay)