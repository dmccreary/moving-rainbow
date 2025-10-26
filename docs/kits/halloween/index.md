# Halloween Party NeoPixel Patterns 🎃👻 - Power Limited Edition

## Overview
This Halloween-themed NeoPixel pattern collection creates spooky lighting effects using orange and purple colors - perfect for your Halloween party! 

**Power Limited Design**: This version limits the number of lit pixels to 1/3 of your strip (maximum 10 pixels for a 30-pixel strip), making it safe for USB power and preventing overdraw issues.

## Power Safety Features

- **Maximum 1/3 pixels lit**: Automatically calculates and enforces a limit based on your strip length
- **USB-safe**: Can be safely powered from USB without external power supply
- **Optimized patterns**: All effects redesigned to look great within power constraints
- **No brightness reduction needed**: Pixels can run at full brightness without risk

## Pattern Descriptions

### Mode 0: Auto Cycle
Automatically cycles through all patterns every 5 seconds for a dynamic party atmosphere.

### Mode 1: Pumpkin Pulse 🎃
A warm orange pulsing effect on every 3rd pixel, creating a flickering jack-o'-lantern effect with power efficiency.

### Mode 2: Witch Chase 🧙‍♀️
Purple and orange comet tails (3 pixels each) chase each other around the strip in opposite directions.

### Mode 3: Ghost Fade 👻
A sparse ghostly white-to-purple fade that sweeps across the strip with strategic pixel spacing.

### Mode 4: Candy Corn Wave 🍬
Moving dots of orange, yellow, and white that create a candy corn pattern with efficient spacing.

### Mode 5: Spooky Sparkle ✨
Random orange and purple sparkles limited to safe power levels - creates a magical firefly effect.

### Mode 6: Monster Eyes 👀
Multiple pairs of glowing eyes that blink in orange and purple - automatically spaced for power limits.

### Mode 7: Halloween Rainbow 🌈
A sparse rainbow effect using Halloween colors with strategic pixel selection for power efficiency.

### Mode 8: Creeping Shadows 🌑
A moving window of shadows with bright orange and purple centers creating an eerie effect.

### Mode 9: Potion Bubbles 🧪
Controlled bubbling effect with purple and green "bubbles" rising up the strip - limits active bubbles.

## Installation

1. Make sure your `config.py` file is properly configured with:
   - `NEOPIXEL_PIN = 0` (or your pin number)
   - `NUMBER_PIXELS = 30` (or your strip length)
   - `BUTTON_PIN_1 = 15`
   - `BUTTON_PIN_2 = 14`

2. Upload `halloween-party.py` to your Raspberry Pi Pico

3. Connect your NeoPixel strip to the configured pin

4. Optional: Connect buttons to pins 14 and 15 for mode switching

## Usage

- **Button 1 (Pin 15)**: Cycle forward through patterns
- **Button 2 (Pin 14)**: Cycle backward through patterns
- **No buttons**: Starts in auto-cycle mode

## Color Palette

The patterns use a Halloween-themed color palette:
- **Orange variations**: Bright pumpkin orange, dim orange, dark orange
- **Purple variations**: Bright purple, dim purple, dark purple
- **Accent colors**: Spooky green, blood red, ghostly white

## Customization Tips

You can easily customize the patterns by:

1. **Adjusting speeds**: Change the `sleep()` values in each pattern function
2. **Modifying colors**: Edit the color tuples at the top of the file
3. **Changing auto-cycle duration**: Modify `PATTERN_DURATION` (currently 5000ms)
4. **Adding new patterns**: Create a new function and add it to the mode list

## Power Considerations

### Power-Limited Design Benefits
- **Safe for USB power**: No external power supply needed for strips up to 60 pixels
- **Automatic limiting**: Code automatically calculates safe pixel count (1/3 of total)
- **No overheating**: Prevents power regulator stress on Raspberry Pi Pico
- **Full brightness**: Pixels that are lit can run at full brightness safely

### Power Usage Examples
- 30-pixel strip: Maximum 10 pixels lit (approx. 600mA at full white)
- 60-pixel strip: Maximum 20 pixels lit (approx. 1.2A at full white)
- 120-pixel strip: Maximum 40 pixels lit (approx. 2.4A at full white)

### If You Need More Brightness
To increase the number of lit pixels:
1. Add an external 5V power supply rated for your needs
2. Modify the `MAX_LIT_PIXELS` calculation in the code
3. Consider using a level shifter for better signal integrity with longer strips

## Party Setup Ideas

- **Entrance**: Use "Ghost Fade" or "Creeping Shadows" for a spooky welcome
- **Dance floor**: "Halloween Rainbow" or "Auto Cycle" for dynamic effects  
- **Refreshment table**: "Potion Bubbles" near the punch bowl
- **Dark corners**: "Monster Eyes" for surprise scares
- **Jack-o'-lanterns**: Place strips inside with "Pumpkin Pulse" mode

Enjoy your spooky Halloween party! 🎃👻🦇
