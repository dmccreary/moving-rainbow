# Fire Simulation for NeoPixel LED Strip
# Creates a realistic fire effect with flickering flames
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
import config

NUMBER_PIXELS = config.NUMBER_PIXELS
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), NUMBER_PIXELS)

# Fire color palette - from dark red to bright yellow/white
dark_red = (80, 0, 0)
red = (255, 0, 0)
orange_red = (255, 30, 0)
orange = (255, 80, 0)
bright_orange = (255, 120, 0)
yellow_orange = (255, 160, 0)
yellow = (255, 200, 0)
bright_yellow = (255, 220, 20)
white_yellow = (255, 240, 60)

# Create arrays to store the current fire state
heat = [0] * NUMBER_PIXELS  # Heat value for each pixel (0-255)
cooling_rate = 55  # How much does the air cool as it rises (0-255)
sparking = 120  # Chance of sparking new embers (0-255)

def heat_to_color(temperature):
    """Convert a heat value (0-255) to a fire color"""
    # Scale heat value to 0-255 range
    t = max(0, min(255, temperature))
    
    if t < 20:
        # Black/very dark red for coldest
        return (0, 0, 0)
    elif t < 60:
        # Dark red to red
        scale = (t - 20) / 40
        return (int(80 + 175 * scale), 0, 0)
    elif t < 100:
        # Red to orange-red
        scale = (t - 60) / 40
        return (255, int(30 * scale), 0)
    elif t < 140:
        # Orange-red to orange
        scale = (t - 100) / 40
        return (255, int(30 + 50 * scale), 0)
    elif t < 180:
        # Orange to yellow-orange
        scale = (t - 140) / 40
        return (255, int(80 + 80 * scale), 0)
    elif t < 220:
        # Yellow-orange to yellow
        scale = (t - 180) / 40
        return (255, int(160 + 40 * scale), 0)
    else:
        # Yellow to white-yellow for hottest
        scale = (t - 220) / 35
        return (255, int(200 + 40 * scale), int(60 * scale))

def fire_update():
    """Update the fire simulation for one frame"""
    global heat
    
    # Step 1: Cool down every cell a little
    for i in range(NUMBER_PIXELS):
        cooldown = randint(0, ((cooling_rate * 10) // NUMBER_PIXELS) + 2)
        if cooldown > heat[i]:
            heat[i] = 0
        else:
            heat[i] = heat[i] - cooldown
    
    # Step 2: Heat from each cell drifts up and diffuses slightly
    for i in range(NUMBER_PIXELS - 1, 1, -1):
        heat[i] = (heat[i - 1] + heat[i - 2] * 2) // 3
    
    # Step 3: Randomly ignite new sparks near the bottom
    if randint(0, 255) < sparking:
        # Pick a random position in the bottom third of the strip
        spark_position = randint(0, NUMBER_PIXELS // 3)
        # Add heat to create a new ember
        heat[spark_position] = heat[spark_position] + randint(160, 255)
        # Cap at 255
        if heat[spark_position] > 255:
            heat[spark_position] = 255
    
    # Step 4: Convert heat to LED colors and display
    for i in range(NUMBER_PIXELS):
        color = heat_to_color(heat[i])
        strip[i] = color
    
    strip.write()

def enhanced_fire():
    """Enhanced fire effect with multiple hot spots"""
    global heat
    
    # Cool down every cell
    for i in range(NUMBER_PIXELS):
        cooldown = randint(0, 50)
        if cooldown > heat[i]:
            heat[i] = 0
        else:
            heat[i] = heat[i] - cooldown
    
    # Heat drifts up and diffuses
    for i in range(NUMBER_PIXELS - 1, 1, -1):
        # Add some randomness to the drift
        drift = randint(0, 2)
        if i - drift >= 0:
            heat[i] = (heat[i - 1] + heat[i - 2] + heat[i - drift]) // 3
    
    # Create multiple sparking zones for more dynamic effect
    # Bottom zone - most active
    if randint(0, 255) < sparking:
        spark_pos = randint(0, NUMBER_PIXELS // 4)
        heat[spark_pos] = min(255, heat[spark_pos] + randint(180, 255))
    
    # Middle zone - occasional flare-ups
    if randint(0, 255) < sparking // 2:
        spark_pos = randint(NUMBER_PIXELS // 4, NUMBER_PIXELS // 2)
        heat[spark_pos] = min(255, heat[spark_pos] + randint(100, 200))
    
    # Add some random flickers throughout
    if randint(0, 100) < 30:
        flicker_pos = randint(0, NUMBER_PIXELS - 1)
        heat[flicker_pos] = min(255, heat[flicker_pos] + randint(20, 80))
    
    # Convert heat to colors and display
    for i in range(NUMBER_PIXELS):
        color = heat_to_color(heat[i])
        strip[i] = color
    
    strip.write()

def campfire_mode():
    """Gentler campfire effect with slower movements"""
    global heat
    
    # Gentler cooling
    for i in range(NUMBER_PIXELS):
        cooldown = randint(0, 30)
        if cooldown > heat[i]:
            heat[i] = 0
        else:
            heat[i] = heat[i] - cooldown
    
    # Slower heat drift
    for i in range(NUMBER_PIXELS - 1, 2, -1):
        heat[i] = (heat[i - 1] + heat[i - 2] + heat[i - 3]) // 3
    
    # Steady base embers
    for i in range(min(5, NUMBER_PIXELS // 6)):
        heat[i] = max(heat[i], 100 + randint(0, 50))
    
    # Occasional sparks
    if randint(0, 100) < 40:
        spark_pos = randint(0, NUMBER_PIXELS // 3)
        heat[spark_pos] = min(255, heat[spark_pos] + randint(150, 255))
    
    # Display
    for i in range(NUMBER_PIXELS):
        color = heat_to_color(heat[i])
        strip[i] = color
    
    strip.write()

def clear():
    """Clear the LED strip"""
    for i in range(NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()

# Initialize
print("Starting Fire Simulation")
print("Press Ctrl+C to stop")
clear()

# Main loop
mode = 0  # 0 = standard fire, 1 = enhanced fire, 2 = campfire
frame_delay = 0.02  # Delay between frames (smaller = faster animation)

try:
    while True:
        if mode == 0:
            fire_update()
        elif mode == 1:
            enhanced_fire()
        else:
            campfire_mode()
        
        sleep(frame_delay)
        
except KeyboardInterrupt:
    print("\nFire extinguished!")
    clear()
