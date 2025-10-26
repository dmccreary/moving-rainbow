# Create Moving Rainbos Skill Prompt

!!! prompt
    Using the Anthropic Skill Creator, please create a skill for creating Moving Rainbow
    MicroPython programs.
    The Skill Creator is here: 
    https://github.com/anthropics/skills/tree/main/skill-creator.
    Place the new skill in /skills/moving-rainbow.
    Use the default Raspberry Pi Pico hardware with a 30 pixel NeoPixel LED strip with two buttons.  
    
    Use the following for the content of the 
    config.py file: 
    NEOPIXEL_PIN = 0
    NUMBER_PIXELS = 30
    BUTTON_PIN_1 = 14
    BUTTON_PIN_2 = 15