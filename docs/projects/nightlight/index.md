# Nightlight Circuit Design

## Circuit Description

This circuit uses a light-dependent resistor (LDR) as a sensor, a 2N2222 NPN transistor as a switch, and two potentiometers for adjustability.

## Circuit Diagram (Text Description)

```
+5V ────┬─── R1 (1kΩ) ─── Base (2N2222)
        │
        ├─── RV1 (10kΩ pot) ─── LDR (20kΩ dark) ─── GND
        │
        └─── RV2 (1kΩ pot) ─── LEDs ─── Collector (2N2222)
                                        │
                                        Emitter ─── GND
```

## Components Needed

- **Power Supply**: 5V, 100mA (provided)
- **LDR**: 20kΩ in darkness (provided)
- **Transistor**: 2N2222 NPN (provided)
- **R1**: 1kΩ base resistor
- **RV1**: 10kΩ potentiometer (sensitivity control)
- **RV2**: 1kΩ potentiometer (brightness control)
- **LEDs**: White LEDs (quantity depends on desired brightness)
- **R_LED**: Current limiting resistors for LEDs

## How It Works

1. **Light Sensing**: The LDR and sensitivity potentiometer (RV1) form a voltage divider
2. **Switching**: When it gets dark, the LDR resistance increases, raising the voltage at the transistor base
3. **LED Control**: The transistor switches on, allowing current to flow through the brightness potentiometer (RV2) and LEDs

## Detailed Calculations

### Voltage Divider (Sensitivity Circuit)
- **Bright conditions**: LDR ≈ 1kΩ
- **Dark conditions**: LDR ≈ 20kΩ
- **Trigger voltage**: Need ~0.7V at base to turn on transistor

**Voltage at base = 5V × (LDR / (RV1 + LDR))**

With RV1 set to middle position (5kΩ):
- Bright: V_base = 5V × (1kΩ / 6kΩ) = 0.83V
- Dark: V_base = 5V × (20kΩ / 25kΩ) = 4V

### LED Current Calculation
**Maximum LED current** (with RV2 at minimum resistance):
- Available voltage for LEDs: 5V - 0.2V (transistor drop) = 4.8V
- With white LEDs (~3.2V forward voltage): 4.8V - 3.2V = 1.6V across RV2
- Maximum current: 1.6V / 100Ω = 16mA per LED string

## Assembly Instructions

1. **Connect the power rails**: +5V and GND
2. **Install the light sensor**:
   - Connect LDR between the sensitivity pot (RV1) wiper and GND
   - Connect one end of RV1 to +5V, other end to transistor base through R1
3. **Install the transistor**:
   - Base to junction of R1 and RV1 wiper
   - Emitter to GND
   - Collector to LED circuit
4. **Connect the LED brightness control**:
   - One end of RV2 to +5V
   - Wiper of RV2 through current limiting resistors to LEDs
   - LEDs to transistor collector

## Adjustment Procedure

1. **Set initial positions**: Both potentiometers to middle position
2. **Test in bright light**: LEDs should be off
3. **Cover LDR**: LEDs should turn on
4. **Adjust sensitivity (RV1)**:
   - Turn clockwise for higher sensitivity (turns on in brighter conditions)
   - Turn counter-clockwise for lower sensitivity (needs darker conditions)
5. **Adjust brightness (RV2)**:
   - Turn clockwise for brighter LEDs
   - Turn counter-clockwise for dimmer LEDs

## Safety Notes

- Keep current draw under 100mA total
- Use appropriate current limiting resistors for LEDs
- Ensure proper heat dissipation for transistor if driving multiple LEDs
- Test circuit on breadboard before permanent assembly

## Troubleshooting

**LEDs always on**: Check LDR connections, adjust sensitivity pot
**LEDs never turn on**: Verify transistor connections, check base voltage
**LEDs too dim/bright**: Adjust brightness potentiometer or LED current limiting resistors