#!/bin/bash
# Cycle through all hues on the Pi 500+ keyboard
# Uses effect 2 (Solid Color) with varying hue values

for hue in $(seq 0 10 255); do
    rpi-keyboard-config effect 2 --hue $hue
done
