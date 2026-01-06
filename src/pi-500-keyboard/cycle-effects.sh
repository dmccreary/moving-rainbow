#!/bin/bash
# Cycle through all Pi 500+ keyboard effects
# Displays each effect for 3 seconds with ASCII art name
# Requires: figlet (sudo apt install figlet)

# Keystroke-triggered effect IDs: 29, 31-42
KEYSTROKE_EFFECTS=(29 31 32 33 34 35 36 37 38 39 40 41 42)

# Function to check if effect is keystroke-triggered
is_keystroke_effect() {
    local id=$1
    for k in "${KEYSTROKE_EFFECTS[@]}"; do
        if [[ "$id" -eq "$k" ]]; then
            return 0
        fi
    done
    return 1
}

# Show help message
show_help() {
    echo "Usage: $(basename "$0") [OPTION]"
    echo ""
    echo "Cycle through Pi 500+ keyboard RGB effects."
    echo ""
    echo "Options:"
    echo "  -a, --all        Show all effects (default)"
    echo "  -k, --keystroke  Show only keystroke-triggered effects"
    echo "  -n, --no-keystroke  Show only non-keystroke effects"
    echo "  -h, --help       Show this help message"
    echo ""
    echo "Keystroke-triggered effects react to key presses (e.g., Reactive, Splash)."
    echo "Non-keystroke effects are passive animations."
    echo ""
    echo "Requires: figlet (sudo apt install figlet) for ASCII art display."
    exit 0
}

# Parse command-line arguments
FILTER="all"
while [[ $# -gt 0 ]]; do
    case $1 in
        -a|--all)
            FILTER="all"
            shift
            ;;
        -k|--keystroke)
            FILTER="keystroke"
            shift
            ;;
        -n|--no-keystroke)
            FILTER="no-keystroke"
            shift
            ;;
        -h|--help)
            show_help
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information."
            exit 1
            ;;
    esac
done

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
DELAY=4

# Build list of effect IDs to display based on filter
effect_ids=()
for id in "${!effects[@]}"; do
    if [[ "$FILTER" == "all" ]]; then
        effect_ids+=("$id")
    elif [[ "$FILTER" == "keystroke" ]]; then
        if is_keystroke_effect "$id"; then
            effect_ids+=("$id")
        fi
    elif [[ "$FILTER" == "no-keystroke" ]]; then
        if ! is_keystroke_effect "$id"; then
            effect_ids+=("$id")
        fi
    fi
done

total_effects=${#effect_ids[@]}

# Display header based on filter
filter_desc="All"
[[ "$FILTER" == "keystroke" ]] && filter_desc="Keystroke-Triggered"
[[ "$FILTER" == "no-keystroke" ]] && filter_desc="Non-Keystroke"

echo "========================================"
echo "  Pi 500+ Keyboard Effects Demo"
echo "  Filter: $filter_desc ($total_effects effects)"
echo "  Press Ctrl+C to exit"
echo "========================================"
echo ""

# Cycle through filtered effects
current=0
for id in "${effect_ids[@]}"; do
    ((current++))
    name="${effects[$id]}"

    # Clear screen
    clear

    # Display effect ID and name
    echo "========================================"
    printf "  Effect ID: %2d  (%d of %d)\n" "$id" "$current" "$total_effects"
    echo "  Filter: $filter_desc"
    echo "========================================"
    echo ""

    # Display ASCII art name
    # Assume the screen width is 120 characters
    if [ "$USE_FIGLET" = true ]; then
        figlet -w 120 "$name"
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
