# Pico Light Sensor Circuit

<iframe src="main.html" height="485" scrolling="no"></iframe>

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/pico-light-sensor/main.html" height="485px" scrolling="no"></iframe>
```

[Run the Pico Light Sensor MicroSim](main.html){ .md-button .md-button--primary }
<br/>
[Edit the MicroSim with the p5.js editor](https://editor.p5js.org/)

## About this MicroSim

This MicroSim demonstrates how a photoresistor voltage divider circuit works with a Raspberry Pi Pico's ADC (Analog to Digital Converter) input. The simulation shows:

- 5V power supply rails
- 47k ohm fixed resistor (top of voltage divider)
- Photoresistor (bottom of voltage divider)
- ADC0 input connection to the Pico (GP26 pin)
- Real-time ADC value display (0-255)

## How It Works

The circuit uses a **voltage divider** consisting of a 47k ohm fixed resistor and a photoresistor (light-dependent resistor or LDR):

1. **Voltage Divider**: The 47k ohm resistor and photoresistor form a voltage divider. The junction voltage between them varies based on light intensity.

2. **Light Response**:
   - **Bright light**: Photoresistor has LOW resistance, junction voltage is LOW, ADC reads LOW values (closer to 0)
   - **Dark conditions**: Photoresistor has HIGH resistance, junction voltage is HIGH, ADC reads HIGH values (closer to 255)

3. **ADC Conversion**: The Raspberry Pi Pico's ADC0 input (GP26) reads the junction voltage and converts it to a digital value from 0 to 255 (8-bit representation).

## Circuit Connections

| Component | Connection |
|-----------|------------|
| 47k ohm Resistor | +5V to Junction |
| Photoresistor | Junction to GND |
| ADC0 (GP26) | Connected to Junction |

## Features

- **Interactive Light Control**: Use the slider to simulate different ambient light levels
- **Animated Current Flow**: Red dots show electron flow through the circuit, with speed varying based on light intensity
- **Real-time ADC Display**: Large digital display shows the ADC value (0-255)
- **Brightness Interpretation**: Text label indicates the light condition (Very Bright, Bright, Medium, Dim, Dark)
- **Voltage Reading**: Shows the junction voltage in real-time

## Learning Objectives

This MicroSim teaches:

- How voltage dividers work with variable resistors
- The inverse relationship between photoresistor resistance and light intensity
- How analog signals are converted to digital values (ADC)
- Basic Raspberry Pi Pico GPIO pin configuration for analog input
- Reading light sensor values for nightlight or ambient light detection projects

## MicroPython Code Example

Here's how to read the light sensor on a real Raspberry Pi Pico:

```python
from machine import ADC, Pin
import time

# Set up ADC on GP26 (ADC0)
light_sensor = ADC(Pin(26))

while True:
    # Read 16-bit value and convert to 8-bit (0-255)
    raw_value = light_sensor.read_u16()
    adc_value = raw_value >> 8  # Shift right 8 bits for 0-255 range

    print(f"Light sensor ADC value: {adc_value}")
    time.sleep(0.5)
```

## Experimentation

Try these activities:

1. **Threshold Detection**: Find the ADC value where you would turn on a nightlight (typically around 200-230)

2. **Response Curve**: Note how the ADC value changes as you slowly adjust the light slider from 0% to 100%

3. **Current Flow**: Watch how the electron animation speed changes with light level - brighter light means lower resistance and faster current flow

4. **Voltage Reading**: Observe the junction voltage and compare it to the ADC value

## Applications

This circuit is commonly used in:

- Automatic nightlights
- Street light controllers
- Camera light meters
- Ambient light sensors for display brightness
- Security lighting systems

## Grade Level

8th-10th grade physical science, electronics, and robotics courses.

## References

- [Raspberry Pi Pico ADC Documentation](https://docs.micropython.org/en/latest/rp2/quickref.html#adc-analog-to-digital-conversion)
- [Voltage Dividers](https://learn.sparkfun.com/tutorials/voltage-dividers)
- [Photoresistors](https://en.wikipedia.org/wiki/Photoresistor)
