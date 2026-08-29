from neopixel import NeoPixel
from machine import ADC, Pin
from utime import sleep
import config

# Pin definitions
NEOPIXEL_PIN = 0
NUMBER_PIXELS = 16

# Initialize NeoPixels
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Initialize potentiometers
brightness_pot = ADC(config.POT_1_PIN)  # First potentiometer for brightness
speed_pot = ADC(config.POT_2_PIN)       # Second potentiometer for speed

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

# Set initial color position
position = 0

print('Rainbow control started. Use potentiometers to adjust:')
print('- Pot 1: Brightness')
print('- Pot 2: Rotation speed')

while True:
    # Read potentiometer values (0-65535)
    brightness_value = brightness_pot.read_u16()
    speed_value = speed_pot.read_u16()
    
    # Convert brightness to a factor between 0.0 and 1.0
    brightness_factor = brightness_value / 65535.0
    
    # Convert speed to a delay between 0.001 (fast) and 0.1 (slow) seconds
    # Invert the relationship so turning the pot clockwise increases speed
    # speed_delay = 0.01 - ((speed_value / 65535.0) * 0.099)
    speed_delay = 0.01 - ((speed_value / 65535.0) * 0.2)

    
    # Calculate color for each pixel
    for i in range(NUMBER_PIXELS):
        # Calculate color wheel position for this pixel
        color_pos = (position + i * (256 // NUMBER_PIXELS)) % 256
        
        # Get base color from wheel
        base_color = wheel(color_pos)
        
        # Adjust brightness
        adjusted_color = adjust_brightness(base_color, brightness_factor)
        
        # Set pixel color
        strip[i] = adjusted_color
    
    # Update the strip
    strip.write()
    
    # Increment position for rotation effect
    # increment the color by 1 each loop
    # position = (position + 1) % 256
    
    # this doubles the rate by incrmenting the color faster
    position = (position + 2) % 256
    
    # Pause based on speed potentiometer
    sleep(speed_delay)