from machine import Pin, ADC
from neopixel import NeoPixel
from utime import sleep
# get the configuration information
import config

# Initialize the NeoPixel strip
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# Initialize the potentiometer (ADC - Analog to Digital Converter)
pot1 = ADC(Pin(config.POT_PIN_1))

# Clear all pixels initially
def clear_strip():
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()

# Main loop
while True:
    # Read the potentiometer value (0 to 65535)
    pot_value = pot1.read_u16()
    
    # Print the pot value to console
    print(f"Potentiometer value: {pot_value}")
    
    # Map the pot value (600-64900) to number of pixels (0-12)
    # We use 12 levels: 0 pixels, then 1-12 pixels
    # Account for actual pot range: min=600, max=64900
    pot_range = pot_value - 600  # Subtract minimum value
    if pot_range < 0:
        pot_range = 0  # Clamp to 0 if somehow below minimum
    
    num_pixels = int((pot_range / (64900 - 600)) * 12)
    
    # Clamp to maximum of 12 pixels in case pot goes higher than expected
    if num_pixels > 12:
        num_pixels = 12
    
    # Clear all pixels first
    clear_strip()
    
    # Light up pixels from 0 to num_pixels-1 in red
    for i in range(num_pixels):
        strip[i] = (25, 0, 0)  # Red color, not too bright
    
    # Update the strip
    strip.write()
    
    # Small delay to prevent excessive updates
    sleep(0.1)