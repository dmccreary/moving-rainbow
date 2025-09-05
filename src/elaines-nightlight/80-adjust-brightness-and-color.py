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

# Clear all pixels initially
def clear_strip():
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()

# Main loop
while True:
    # Read both potentiometer values (0 to 65535)
    pot1_value = pot1.read_u16()  # Brightness
    pot2_value = pot2.read_u16()  # Color
    
    # Map pot1 (600-64900) to brightness (0-1)
    brightness_range = pot1_value - 600
    if brightness_range < 0:
        brightness_range = 0
    brightness = brightness_range / (64900 - 600)
    if brightness > 1.0:
        brightness = 1.0
    
    # Map pot2 (600-64900) to hue (0-360 degrees)
    color_range = pot2_value - 600
    if color_range < 0:
        color_range = 0
    hue = (color_range / (64900 - 600)) * 360
    if hue > 360:
        hue = 360
    
    # Convert HSV to RGB (full saturation, brightness from pot1)
    rgb = hsv_to_rgb(hue, 1.0, brightness)
    
    # Apply the color to all pixels
    for i in range(config.NUMBER_PIXELS):
        strip[i] = rgb
    
    # Update the strip
    strip.write()
    
    # Print values for debugging
    print(f"Pot1 (Brightness): {pot1_value}, Brightness: {brightness:.2f}")
    print(f"Pot2 (Color): {pot2_value}, Hue: {hue:.1f}°, RGB: {rgb}")
    print("---")
    
    # Small delay to prevent excessive updates
    sleep(0.1)