#!/bin/bash
# Pi 500+ Keyboard LED Control Shell Script Template
#
# This template provides common commands for controlling keyboard LEDs.
# Copy and modify for your specific use case.
#
# Requirements:
#   sudo apt install rpi-keyboard-config

# ========================================
# PRESET COMMANDS
# ========================================

# Cycle to a specific preset (0-6)
# rpi-keyboard-config preset index 3

# Get current preset settings
# rpi-keyboard-config preset get

# Save effect 25 to preset slot 2
# rpi-keyboard-config preset set 2 25

# ========================================
# EFFECT COMMANDS
# ========================================

# Set an effect by ID (0-44)
# rpi-keyboard-config effect 25

# Set effect with parameters
# rpi-keyboard-config effect 2 --hue 170 --sat 255 --speed 128

# List all available effects
# rpi-keyboard-config list-effects

# ========================================
# LED COLOR COMMANDS
# ========================================

# Clear all LEDs
# rpi-keyboard-config leds clear

# Set all LEDs to a color (HSV format: "hue,sat,val")
# rpi-keyboard-config leds set --colour "170,255,255"  # Blue

# Set all LEDs to a color (RGB format)
# rpi-keyboard-config leds set --colour "rgb(0,0,255)"  # Blue

# Set a specific key by row,column
# rpi-keyboard-config led set "2,3" --colour "rgb(0,255,255)"  # W key cyan

# Save current LED layout to EEPROM (stored as effect 1)
# rpi-keyboard-config leds save

# ========================================
# BRIGHTNESS COMMANDS
# ========================================

# Set brightness (0-255)
# rpi-keyboard-config brightness 255

# ========================================
# UTILITY COMMANDS
# ========================================

# Show keyboard ASCII map with key positions
# rpi-keyboard-config info --ascii

# Reset all presets to defaults
# rpi-keyboard-config reset-presets

# Play built-in Flappy Birds game
# rpi-keyboard-config game

# ========================================
# YOUR COMMANDS HERE
# ========================================

# Example: Cycle through hues on solid color effect
for hue in $(seq 0 10 255); do
    rpi-keyboard-config effect 2 --hue $hue
done

echo "Done!"
