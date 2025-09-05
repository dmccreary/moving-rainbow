from machine import Pin, ADC
from neopixel import NeoPixel
from utime import sleep
# get the configuration information
import config

# Initialize the NeoPixel strip
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# Initialize the photoresistor (ADC - Analog to Digital Converter)
photo_pin = ADC(Pin(config.PHOTORESISTOR_PIN))

# Clear all pixels initially
def clear_strip():
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()

# Main loop
while True:
    # Read the photoresistor value (0 to 65535)
    light_value = photo_pin.read_u16()
    
    # Print the light value to console for debugging
    print(f"Light sensor value: {light_value}")
    
    # Map the light value to number of pixels (0-12)
    # Light range: 2000 (very dark) to 55000 (very bright)
    # Below 2000: 0 LEDs
    # Above 55000: all 12 LEDs
    
    if light_value < 2000:
        num_pixels = 0
    elif light_value > 55000:
        num_pixels = 12
    else:
        # Map values between 2000 and 55000 to 0-12 pixels
        light_range = light_value - 2000
        num_pixels = int((light_range / (55000 - 2000)) * 12)
        
        # Ensure we don't exceed 12 pixels
        if num_pixels > 12:
            num_pixels = 12
    
    # Clear all pixels first
    clear_strip()
    
    # Light up pixels from 0 to num_pixels-1
    # Use different colors to indicate light levels
    for i in range(num_pixels):
        if i < 4:  # Low light levels - blue
            strip[i] = (0, 0, 25)
        elif i < 8:  # Medium light levels - green
            strip[i] = (0, 25, 0)
        else:  # High light levels - red
            strip[i] = (25, 0, 0)
    
    # Update the strip
    strip.write()
    
    print(f"Number of pixels lit: {num_pixels}")
    print("---")
    
    # Small delay to prevent excessive updates
    sleep(0.2)