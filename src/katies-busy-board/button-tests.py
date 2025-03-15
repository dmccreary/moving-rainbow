import config
from machine import Pin
import time
import neopixel

# Configuration pins
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
MODE_BUTTON_PIN = config.MODE_BUTTON_PIN
ROTARY_ENCODER_1_A_PIN = config.ROTARY_ENCODER_1_A_PIN
ROTARY_ENCODER_1_B_PIN = config.ROTARY_ENCODER_1_B_PIN
ROTARY_ENCODER_1_BUTTON_PIN = config.ROTARY_ENCODER_1_BUTTON_PIN
ROTARY_ENCODER_2_A_PIN = config.ROTARY_ENCODER_2_A_PIN
ROTARY_ENCODER_2_B_PIN = config.ROTARY_ENCODER_2_B_PIN
ROTARY_ENCODER_2_BUTTON_PIN = config.ROTARY_ENCODER_2_BUTTON_PIN
INTERNAL_BUTTON_PIN_1 = config.INTERNAL_BUTTON_PIN_1
INTERNAL_BUTTON_PIN_2 = config.INTERNAL_BUTTON_PIN_2

print('ROTARY_ENCODER_1_A_PIN:', ROTARY_ENCODER_1_A_PIN)
print('Starting button and rotary encoder monitor...')

# Initialize NeoPixels
np = neopixel.NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Set up button pins with pull-up resistors
mode_button = Pin(MODE_BUTTON_PIN, Pin.IN, Pin.PULL_UP)
re1_button = Pin(ROTARY_ENCODER_1_BUTTON_PIN, Pin.IN, Pin.PULL_UP)
re2_button = Pin(ROTARY_ENCODER_2_BUTTON_PIN, Pin.IN, Pin.PULL_UP)
internal_button1 = Pin(INTERNAL_BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
internal_button2 = Pin(INTERNAL_BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

# Set up rotary encoder pins
re1_a = Pin(ROTARY_ENCODER_1_A_PIN, Pin.IN, Pin.PULL_UP)
re1_b = Pin(ROTARY_ENCODER_1_B_PIN, Pin.IN, Pin.PULL_UP)
re2_a = Pin(ROTARY_ENCODER_2_A_PIN, Pin.IN, Pin.PULL_UP)
re2_b = Pin(ROTARY_ENCODER_2_B_PIN, Pin.IN, Pin.PULL_UP)

# Track button states and encoder values
button_states = {
    'mode_button': mode_button.value(),
    're1_button': re1_button.value(),
    're2_button': re2_button.value(),
    'internal_button1': internal_button1.value(),
    'internal_button2': internal_button2.value()
}

# Track encoder values and states
encoder_values = {
    'encoder1': 0,
    'encoder2': 0
}

encoder_states = {
    'encoder1': (re1_a.value(), re1_b.value()),
    'encoder2': (re2_a.value(), re2_b.value())
}

# Lookup table for rotary encoder state transitions
# Each state is (A, B) and can be 0b00, 0b01, 0b10, or 0b11
# The value in the table is the direction of rotation: 1 (clockwise) or -1 (counterclockwise)
encoder_table = {
    # Current state, New state => Direction
    (0, 0): {(0, 1): 1, (1, 0): -1},
    (0, 1): {(1, 1): 1, (0, 0): -1},
    (1, 0): {(0, 0): 1, (1, 1): -1},
    (1, 1): {(0, 1): -1, (1, 0): 1}
}

# Function to update NeoPixels based on encoder values
def update_neopixels():
    # Map encoder1 value to first half of pixels
    half_pixels = NUMBER_PIXELS // 2
    
    # Simple visualization - each encoder controls brightness of its section
    brightness1 = min(255, max(0, encoder_values['encoder1'] % 256))
    brightness2 = min(255, max(0, encoder_values['encoder2'] % 256))
    
    for i in range(half_pixels):
        np[i] = (brightness1, 0, 0)  # Red for encoder 1
    
    for i in range(half_pixels, NUMBER_PIXELS):
        np[i] = (0, 0, brightness2)  # Blue for encoder 2
    
    np.write()

# Function to check button state changes
def check_buttons():
    global button_states
    
    # Check each button for changes
    new_mode_button = mode_button.value()
    if new_mode_button != button_states['mode_button']:
        button_states['mode_button'] = new_mode_button
        print(f"Mode button: {'released' if new_mode_button else 'pressed'}")
    
    new_re1_button = re1_button.value()
    if new_re1_button != button_states['re1_button']:
        button_states['re1_button'] = new_re1_button
        print(f"Encoder 1 button: {'released' if new_re1_button else 'pressed'}")
    
    new_re2_button = re2_button.value()
    if new_re2_button != button_states['re2_button']:
        button_states['re2_button'] = new_re2_button
        print(f"Encoder 2 button: {'released' if new_re2_button else 'pressed'}")
    
    new_internal_button1 = internal_button1.value()
    if new_internal_button1 != button_states['internal_button1']:
        button_states['internal_button1'] = new_internal_button1
        print(f"Internal button 1: {'released' if new_internal_button1 else 'pressed'}")
    
    new_internal_button2 = internal_button2.value()
    if new_internal_button2 != button_states['internal_button2']:
        button_states['internal_button2'] = new_internal_button2
        print(f"Internal button 2: {'released' if new_internal_button2 else 'pressed'}")

# Function to check rotary encoder state changes
def check_encoders():
    global encoder_states, encoder_values
    
    # Check encoder 1
    new_state1 = (re1_a.value(), re1_b.value())
    if new_state1 != encoder_states['encoder1']:
        old_state = encoder_states['encoder1']
        encoder_states['encoder1'] = new_state1
        
        # Look up direction in the table
        if old_state in encoder_table and new_state1 in encoder_table[old_state]:
            direction = encoder_table[old_state][new_state1]
            encoder_values['encoder1'] += direction
            print(f"Encoder 1 value: {encoder_values['encoder1']}")
    
    # Check encoder 2
    new_state2 = (re2_a.value(), re2_b.value())
    if new_state2 != encoder_states['encoder2']:
        old_state = encoder_states['encoder2']
        encoder_states['encoder2'] = new_state2
        
        # Look up direction in the table
        if old_state in encoder_table and new_state2 in encoder_table[old_state]:
            direction = encoder_table[old_state][new_state2]
            encoder_values['encoder2'] += direction
            print(f"Encoder 2 value: {encoder_values['encoder2']}")

# Main loop
print("Monitoring buttons and encoders. Press Ctrl+C to stop.")
try:
    while True:
        check_buttons()
        check_encoders()
        update_neopixels()
        time.sleep(0.01)  # Short delay to prevent CPU hogging
except KeyboardInterrupt:
    print("Program stopped by user")
    # Turn off all NeoPixels
    for i in range(NUMBER_PIXELS):
        np[i] = (0, 0, 0)
    np.write()