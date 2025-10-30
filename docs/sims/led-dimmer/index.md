# LED Dimmer Circuit

<iframe src="main.html" height="600"></iframe>


```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/led-dimmer/main.html" height="400px" scrolling="no"></iframe>
```

[Run the MicroSim](main.html){ .md-button .md-button--primary }
<br/>
[Edit the Microsim with the p5.js editor](https://editor.p5js.org/dmccreary/sketches/x4TgEDaHm)

## Sample iframe

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/led-dimmer/main.html" height="600" scrolling="no"></iframe>
```

## About this MicroSim

This MicroSim demonstrates how an LED dimmer circuit works using a potentiometer to control LED brightness through a transistor. The simulation shows the complete circuit including:

- 5 volt power supply
- 20kΩ potentiometer (voltage divider)
- 10kΩ base resistor
- 2N2222 NPN transistor
- Standard red LED
- 220Ω current-limiting resistor

## How It Works

The LED dimmer circuit has three main parts:

1. **Voltage Divider (Potentiometer)**: The 20kΩ potentiometer acts as a voltage divider. As you turn the knob, the center tap voltage varies between 0V and 5V. The slider in the simulation lets you adjust this value.

2. **Amplifier Switch (Transistor Circuit)**: The voltage from the potentiometer goes through the 10kΩ resistor to the base of the 2N2222 transistor. The transistor acts like an electronic valve - a small voltage at the base controls a much larger current through the collector and emitter. When the base voltage increases, the transistor "opens up" allowing more current to flow.

3. **LED Circuit**: Current flows from +5V through the LED, through the 220Ω current-limiting resistor, through the transistor's collector and emitter, to ground. The 220Ω resistor ensures the LED receives safe current levels even at maximum brightness.

## Features

- **Interactive Potentiometer**: Use the slider to adjust the potentiometer from 0% to 100%
- **Animated Current Flow**: Red dots show electron flow through the circuit when current is flowing
- **Real-time Readings**: Displays base voltage, current percentage, and LED brightness
- **Visual LED Brightness**: The LED glows brighter as more current flows, with light rays at high brightness
- **Start/Pause Animation**: Control the electron flow animation
- **Reset Button**: Return all settings to default values

## Learning Objectives

This MicroSim teaches:

- How a voltage divider works with a potentiometer
- The role of a transistor as an amplifier and switch
- Current limiting with resistors
- The relationship between base voltage and collector current in an NPN transistor
- How to control LED brightness using analog circuits

## Circuit Connections

1. The potentiometer outer terminals connect to +5V and ground
2. The potentiometer center tap connects through the 10kΩ resistor to the transistor base
3. The LED anode (+) connects to +5V
4. The LED cathode (-) connects to the 220Ω resistor
5. The 220Ω resistor connects to the transistor collector
6. The transistor emitter connects to ground

## Experimentation

Try these activities:

1. **Low Voltage**: Set the potentiometer to 0-10% and observe that the LED doesn't light up. This is because the transistor needs about 0.7V at the base to start conducting.

2. **Threshold**: Slowly increase the potentiometer and watch for when the LED first starts to glow (around 14% or 0.7V).

3. **Linear Response**: Continue increasing and observe how LED brightness increases with potentiometer position.

4. **Maximum Brightness**: Set to 100% and see the LED at full brightness with animated light rays.

5. **Current Flow**: Watch the animated red dots (electrons) flow through the circuit. Notice they only flow when there's sufficient base voltage.

## Grade Level

9th-10th grade physical science, electronics, and circuits.

## References

- [Transistor as a Switch](https://en.wikipedia.org/wiki/Transistor#Transistor_as_a_switch)
- [LED Current Limiting](https://www.electronics-tutorials.ws/blog/resistor-for-led.html)
- [Voltage Dividers](https://learn.sparkfun.com/tutorials/voltage-dividers)
- [2N2222 Datasheet](https://www.onsemi.com/pdf/datasheet/p2n2222a-d.pdf)
