# Photoresistor Component Visualization

This is a simple p5.js visualization showing the characteristic structure of a photoresistor (Light Dependent Resistor).

[View the Photoresistor Component](main.html){:target="_blank"}

## About Photoresistors

A **photoresistor** is a light-sensitive component whose electrical resistance decreases with increasing incident light intensity.

### Key Features:

- **Serpentine Pattern**: The distinctive zigzag pattern you see is the light-sensitive material. This pattern maximizes the surface area exposed to light within a compact space.
- **Variable Resistance**:
  - In darkness: ~1MΩ (1,000,000 ohms) or higher
  - In bright light: ~50-100Ω
- **Common Uses**: Nightlights, street lamps, camera light meters, alarm systems

### How It Works

The serpentine pattern is made of a semiconductor material (often cadmium sulfide). When light photons hit this material, they excite electrons, making it easier for current to flow, which decreases the resistance.

## Circuit Applications

Photoresistors are typically used in a **voltage divider circuit** paired with a fixed resistor. As light levels change, the voltage at the midpoint of the divider changes, which can be read by a microcontroller or used to control other components like transistors.

See the [LED Nightlight Circuit](../nightlight/) for an example of a photoresistor in action.
