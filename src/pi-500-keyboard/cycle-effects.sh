#!/bin/bash
# Cycle through all Pi 500+ keyboard effects
# Displays each effect for 3 seconds with ASCII art name
# Requires: figlet (sudo apt install figlet)

# Effect names array (indexed 0-44)
effects=(
    "OFF"
    "Direct"
    "Solid Color"
    "Alphas Mods"
    "Gradient Up Down"
    "Gradient Left Right"
    "Breathing"
    "Band Sat"
    "Band Val"
    "Band Pinwheel Sat"
    "Band Pinwheel Val"
    "Band Spiral Sat"
    "Band Spiral Val"
    "Cycle All"
    "Cycle Left Right"
    "Cycle Up Down"
    "Rainbow Chevron"
    "Cycle Out In"
    "Cycle Out In Dual"
    "Cycle Pinwheel"
    "Cycle Spiral"
    "Dual Beacon"
    "Rainbow Beacon"
    "Rainbow Pinwheels"
    "Raindrops"
    "Jellybean Raindrops"
    "Hue Breathing"
    "Hue Pendulum"
    "Hue Wave"
    "Typing Heatmap"
    "Digital Rain"
    "Reactive Simple"
    "Solid Reactive"
    "Reactive Wide"
    "Reactive Multiwide"
    "Reactive Cross"
    "Reactive Multicross"
    "Reactive Nexus"
    "Reactive Multinexus"
    "Splash"
    "Multisplash"
    "Solid Splash"
    "Solid Multisplash"
    "Pixel Rain"
    "Pixel Fractal"
)

# Check if figlet is installed
if ! command -v figlet &> /dev/null; then
    echo "figlet is not installed. Install with: sudo apt install figlet"
    echo "Continuing without ASCII art..."
    USE_FIGLET=false
else
    USE_FIGLET=true
fi

# Display duration in seconds
DELAY=3

echo "========================================"
echo "  Pi 500+ Keyboard Effects Demo"
echo "  Press Ctrl+C to exit"
echo "========================================"
echo ""

# Cycle through all effects
for id in "${!effects[@]}"; do
    name="${effects[$id]}"

    # Clear screen
    clear

    # Display effect ID and name
    echo "========================================"
    printf "  Effect %2d of 44\n" "$id"
    echo "========================================"
    echo ""

    # Display ASCII art name
    if [ "$USE_FIGLET" = true ]; then
        figlet -w 80 "$name"
    else
        echo ">>> $name <<<"
    fi

    echo ""
    echo "----------------------------------------"

    # Set the keyboard effect
    rpi-keyboard-config effect "$id"

    # Wait before next effect
    sleep $DELAY
done

# Return to default preset
echo ""
echo "Demo complete! Returning to preset 0..."
rpi-keyboard-config preset index 0
