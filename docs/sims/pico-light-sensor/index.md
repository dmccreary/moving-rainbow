# Pico Light Sensor Circuit

<iframe src="main.html" height="485" scrolling="no"></iframe>

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/pico-light-sensor/main.html" height="485px" scrolling="no"></iframe>
```

[Run the Pico Light Sensor MicroSim](main.html){ .md-button .md-button--primary }
<br/>
[Edit the MicroSim with the p5.js editor](https://editor.p5js.org/dmccreary/sketches/k6hv8wZPc/)

## About this MicroSim

This MicroSim demonstrates how a photoresistor voltage divider circuit works with a Raspberry Pi Pico's ADC (Analog to Digital Converter) input. The simulation shows:

- 5V power supply rails
- Photoresistor (top of voltage divider, connected to +5V)
- 47k ohm fixed resistor (bottom of voltage divider, connected to GND)
- ADC0 input connection to the Pico (GP26 pin)
- Real-time ADC value display (0-255)

## How It Works

The circuit uses a **voltage divider** with the photoresistor on top and 47k ohm fixed resistor on bottom:

1. **Voltage Divider**: The photoresistor connects to +5V and the 47k resistor connects to GND. The junction voltage between them varies based on light intensity.

2. **Light Response**:
   - **Bright light**: Photoresistor has LOW resistance, more current flows, junction voltage is HIGH, ADC reads HIGH values (closer to 255)
   - **Dark conditions**: Photoresistor has HIGH resistance, less current flows, junction voltage is LOW, ADC reads LOW values (closer to 0)

3. **ADC Conversion**: The Raspberry Pi Pico's ADC0 input (GP26) reads the junction voltage and converts it to a digital value from 0 to 255 (8-bit representation).

## Circuit Connections

| Component | Connection |
|-----------|------------|
| Photoresistor | +5V to Junction |
| 47k ohm Resistor | Junction to GND |
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

1. **Threshold Detection**: Find the ADC value where you would turn on a nightlight (typically around 25-50, since dark = low ADC)

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

---

## Lesson Plan

### Overview

This 45-minute lesson introduces students to analog sensors, voltage dividers, and analog-to-digital conversion using the interactive Pico Light Sensor MicroSim. Students will explore how photoresistors change resistance based on light intensity and how the Raspberry Pi Pico reads analog values.

### Learning Objectives

By the end of this lesson, students will be able to:

1. Explain how a voltage divider circuit works
2. Describe the relationship between light intensity and photoresistor resistance
3. Interpret ADC values and relate them to real-world light conditions
4. Apply their understanding to design simple light-sensing projects

### Materials Needed

- Computer with web browser
- Pico Light Sensor MicroSim
- Optional: Raspberry Pi Pico, photoresistor, 47k ohm resistor, breadboard, and jumper wires for hands-on extension

### Lesson Timeline

| Time | Activity |
|------|----------|
| 5 min | Introduction and prior knowledge check |
| 10 min | Guided exploration of the MicroSim |
| 10 min | Concept explanation: Voltage dividers and ADC |
| 10 min | Hands-on experimentation with the simulation |
| 5 min | Quiz and wrap-up discussion |
| 5 min | Extension activity introduction |

### Procedure

**1. Introduction (5 minutes)**

Ask students: "How do automatic nightlights know when to turn on?" Discuss how electronic devices can sense light levels. Introduce the concept that sensors convert real-world phenomena into electrical signals.

**2. Guided Exploration (10 minutes)**

Have students open the MicroSim and explore:

- Move the light slider from 0% to 100%
- Observe how the ADC value changes
- Watch the current flow animation
- Note the voltage reading at the junction

**3. Concept Explanation (10 minutes)**

Explain the key concepts:

- **Voltage Divider**: Two resistors in series create a junction voltage proportional to the resistance ratio
- **Photoresistor Behavior**: Resistance DECREASES as light INCREASES (inverse relationship)
- **ADC Conversion**: The analog voltage is converted to a digital number (0-255 in 8-bit)

Key insight: In this circuit configuration, **bright light = high ADC value** and **dark = low ADC value** because the photoresistor is on top of the voltage divider.

**4. Hands-on Experimentation (10 minutes)**

Students complete the experimentation activities:

- Find the threshold ADC value for a nightlight (when would you want lights to turn on?)
- Record ADC values at 0%, 25%, 50%, 75%, and 100% light levels
- Compare junction voltage to ADC values

**5. Assessment and Wrap-up (5 minutes)**

Complete the quiz questions below. Discuss real-world applications.

**6. Extension Activity**

For students who finish early or want to explore further:

- Write pseudocode for a nightlight that turns on when ADC < 30
- Design a circuit that reverses the behavior (swap resistor positions)
- Research other analog sensors that use voltage dividers

### Differentiation

**For struggling learners:**

- Provide a graphic organizer showing the relationship between light, resistance, and ADC values
- Use the MicroSim in pairs with guided questions

**For advanced learners:**

- Calculate the actual junction voltage using the voltage divider formula
- Modify the MicroPython code to implement hysteresis (prevent flickering)

---

## Quiz

Test your understanding of voltage dividers, photoresistors, and ADC conversion with these questions.

---

#### 1. In the light sensor circuit, what happens to the photoresistor's resistance when light intensity increases?

<div class="upper-alpha" markdown>
1. Resistance increases proportionally with light
2. Resistance decreases as light increases
3. Resistance stays the same regardless of light
4. Resistance fluctuates randomly with light changes
</div>

??? question "Show Answer"
    The correct answer is **B**. Photoresistors have an inverse relationship with light intensity - as light increases, their resistance decreases. This is because light energy frees electrons in the semiconductor material, allowing more current to flow. In bright light, a photoresistor may have only a few hundred ohms of resistance, while in darkness it can have megaohms of resistance.

    **Concept Tested:** Photoresistor Behavior

---

#### 2. In this voltage divider circuit with the photoresistor on top (connected to +5V), what ADC value would you expect in complete darkness?

<div class="upper-alpha" markdown>
1. A high value close to 255
2. A low value close to 0
3. A medium value around 128
4. The ADC cannot read in darkness
</div>

??? question "Show Answer"
    The correct answer is **B**. In darkness, the photoresistor has very high resistance (much higher than the 47k fixed resistor). This means most of the voltage drops across the photoresistor, leaving very little voltage at the junction where the ADC reads. Low junction voltage results in a low ADC value close to 0. This is why the circuit reads "dark = low ADC" and "bright = high ADC."

    **Concept Tested:** Voltage Divider Operation

---

#### 3. What is the purpose of the 47k ohm fixed resistor in this light sensor circuit?

<div class="upper-alpha" markdown>
1. To limit the current and protect the Pico from damage
2. To form a voltage divider that produces a variable voltage based on light
3. To convert digital signals to analog signals
4. To amplify the signal from the photoresistor
</div>

??? question "Show Answer"
    The correct answer is **B**. The 47k ohm fixed resistor forms the bottom half of a voltage divider with the photoresistor. As the photoresistor's resistance changes with light, the ratio between the two resistors changes, which changes the voltage at their junction. This variable voltage is what the ADC reads. While current limiting (A) is a secondary benefit, the primary purpose is to create a measurable voltage that varies with light intensity.

    **Concept Tested:** Voltage Divider Purpose

---

#### 4. The Raspberry Pi Pico's ADC converts the analog voltage to a digital value. If the ADC reads a value of 200 out of 255, approximately what percentage of the supply voltage is present at the junction?

<div class="upper-alpha" markdown>
1. About 20%
2. About 50%
3. About 78%
4. About 100%
</div>

??? question "Show Answer"
    The correct answer is **C**. An 8-bit ADC produces values from 0 to 255, where 0 represents 0V and 255 represents the full reference voltage. To find the percentage: (200 ÷ 255) × 100 = approximately 78%. This means the junction voltage is about 78% of the supply voltage. Understanding this conversion is essential for interpreting sensor readings and setting appropriate thresholds in your code.

    **Concept Tested:** ADC Conversion

---

#### 5. You are designing an automatic nightlight that should turn on when it gets dark. Based on this circuit's behavior, which code logic would correctly turn on an LED when it's dark?

<div class="upper-alpha" markdown>
1. `if adc_value > 200: led.on()`
2. `if adc_value < 30: led.on()`
3. `if adc_value == 128: led.on()`
4. `if adc_value > 30 and adc_value < 200: led.on()`
</div>

??? question "Show Answer"
    The correct answer is **B**. Since this circuit produces low ADC values in darkness and high values in bright light, a nightlight should turn on when the ADC value falls below a threshold. A threshold of 30 is reasonable for detecting dark conditions. Option A would turn on the light when it's bright (opposite of desired behavior). Option C only works at exactly one light level. Option D would turn on at medium light levels but not in darkness.

    **Concept Tested:** Applying ADC Values in Code
