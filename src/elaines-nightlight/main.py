from machine import Pin, ADC
from neopixel import NeoPixel
from utime import sleep
# get the configuration information
import config

# Initialize the NeoPixel strip
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# Initialize both potentiometers (ADC - Analog to Digital Converter)
pot1 = ADC(Pin(config.POT_PIN_1))  # Brightness control
pot2 = ADC(Pin(config.POT_PIN_2))  # Color control

# Initialize the photoresistor
photo_sensor = ADC(Pin(config.PHOTORESISTOR_PIN))

# Initialize the button
button = Pin(config.BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Light sensor threshold - LED strip only turns on when room is darker than this
LIGHT_THRESHOLD = 10000  # Based on sensor testing: dark=1500, bright=55000

# Pattern control variables
pattern_mode = 0  # Start with mode 0 (solid color)
max_patterns = 4  # Total number of patterns
button_pressed = False
last_button_state = True  # Button is pulled up, so True = not pressed

# Animation variables
animation_counter = 0
animation_speed = 5  # Higher number = slower animation

# Function to convert HSV to RGB
def hsv_to_rgb(h, s, v):
    """
    Convert HSV color to RGB
    h: hue (0-360)
    s: saturation (0-1)
    v: value/brightness (0-1)
    Returns RGB tuple (0-255, 0-255, 0-255)
    """
    h = h / 60.0
    i = int(h)
    f = h - i
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))
    
    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    else:
        r, g, b = v, p, q
    
    return (int(r * 255), int(g * 255), int(b * 255))

# Clear all pixels
def clear_strip():
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()

# Check if room is dark enough to turn on nightlight
def is_room_dark():
    light_level = photo_sensor.read_u16()
    return light_level < LIGHT_THRESHOLD

# Pattern 0: Solid color (original behavior)
def pattern_solid(rgb):
    for i in range(config.NUMBER_PIXELS):
        strip[i] = rgb

# Pattern 1: Single moving dot
def pattern_moving_dot(rgb):
    clear_strip()
    position = (animation_counter // animation_speed) % config.NUMBER_PIXELS
    strip[position] = rgb

# Pattern 2: Chase pattern (3 pixels moving)
def pattern_chase(rgb):
    clear_strip()
    position = (animation_counter // animation_speed) % config.NUMBER_PIXELS
    for i in range(3):  # 3 pixels in the chase
        pixel_pos = (position + i) % config.NUMBER_PIXELS
        # Fade the trailing pixels
        brightness_factor = (3 - i) / 3
        faded_rgb = (int(rgb[0] * brightness_factor), 
                    int(rgb[1] * brightness_factor), 
                    int(rgb[2] * brightness_factor))
        strip[pixel_pos] = faded_rgb

# Pattern 3: Bouncing dot
def pattern_bounce(rgb):
    clear_strip()
    # Create bouncing effect by going back and forth
    cycle_length = (config.NUMBER_PIXELS - 1) * 2
    position_in_cycle = (animation_counter // animation_speed) % cycle_length
    
    if position_in_cycle < config.NUMBER_PIXELS:
        position = position_in_cycle
    else:
        position = cycle_length - position_in_cycle
    
    strip[position] = rgb

# Handle button press to cycle through patterns
def check_button():
    global pattern_mode, button_pressed, last_button_state
    
    current_button_state = button.value()
    
    # Detect button press (transition from high to low)
    if last_button_state and not current_button_state and not button_pressed:
        button_pressed = True
        pattern_mode = (pattern_mode + 1) % max_patterns
        print(f"Pattern mode changed to: {pattern_mode}")
    
    # Reset button pressed flag when button is released
    if current_button_state:
        button_pressed = False
    
    last_button_state = current_button_state

# Main loop
while True:
    # Check for button presses
    check_button()
    
    # Read light sensor to determine if nightlight should be on
    light_level = photo_sensor.read_u16()
    room_is_dark = is_room_dark()
    
    # If room is too bright, turn off all LEDs and skip pattern logic
    if not room_is_dark:
        clear_strip()
        # Print light level for debugging (less frequently)
        if animation_counter % 50 == 0:
            print(f"Room too bright (light level: {light_level}), nightlight off")
        animation_counter += 1
        sleep(0.1)
        continue
    
    # Room is dark enough - proceed with normal nightlight operation
    
    # Read both potentiometer values (0 to 65535)
    pot1_value = pot1.read_u16()  # Brightness
    pot2_value = pot2.read_u16()  # Color
    
    # Debug: Print raw potentiometer values
    print(f"  -> Raw Pot1: {pot1_value}, Raw Pot2: {pot2_value}")
    
    # Map pot1 (0-65535) to brightness (0-1) - using full range
    brightness = pot1_value / 65535
    if brightness > 1.0:
        brightness = 1.0
    
    # For testing: ensure minimum brightness so we can see if it's working
    if brightness < 0.1:
        brightness = 0.1  # Temporary minimum for debugging
    
    # Map pot2 (0-65535) to hue (0-360 degrees) - using full range
    hue = (pot2_value / 65535) * 360
    if hue > 360:
        hue = 360
    
    # Convert HSV to RGB (full saturation, brightness from pot1)
    rgb = hsv_to_rgb(hue, 1.0, brightness)
    
    # Apply the selected pattern
    if pattern_mode == 0:
        pattern_solid(rgb)
    elif pattern_mode == 1:
        pattern_moving_dot(rgb)
    elif pattern_mode == 2:
        pattern_chase(rgb)
    elif pattern_mode == 3:
        pattern_bounce(rgb)
    
    # Update the strip
    strip.write()
    
    # Increment animation counter for moving patterns
    animation_counter += 1
    
    # Print values for debugging (less frequently to avoid spam)
    if animation_counter % 50 == 0:
        print(f"Light: {light_level}, Mode: {pattern_mode}, Brightness: {brightness:.2f}, Hue: {hue:.1f}°, RGB: {rgb}")
    
    # Small delay to prevent excessive updates
    sleep(0.1)