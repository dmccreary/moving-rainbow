# Gamma Correction

Gamma Correction is a way to adjust how bright things look to match how our eyes actually see them. When you change the brightness of something like an LED, the light doesn't always appear to change smoothly. This is because our eyes don't see light in a perfectly straight way.

Here's a simple way to think about it:

-   **Without Gamma Correction**: If you turn up the brightness by small amounts, the LED might look like it's getting bright too quickly at first and then not much brighter as you keep increasing the brightness. It doesn't feel smooth.

-   **With Gamma Correction**: We use a special formula to adjust the brightness in a way that matches how your eyes see it. So, when you change the brightness of the LED, it looks like it's increasing evenly from dim to bright.

Imagine trying to turn up the volume on a speaker: without correction, it might feel like the volume jumps too quickly, while with correction, the sound would get louder in a smooth and controlled way.

In short, **Gamma Correction** is like a tool that smooths out the changes in brightness so the LED looks like it's getting brighter in a way that feels natural to your eyes.

## Python Function to Do Gamma Correction

```py
from machine import Pin, PWM, ADC
import time
import math

# Setup PWM pin
pwm_pin = PWM(Pin(15))  # PWM pin connected to the base of the 2N2222 (e.g., GP15)
pwm_pin.freq(1000)      # PWM frequency of 1kHz

# Setup photoresistor circuit connected to ADC pin
adc_pin = ADC(Pin(26))  # Photoresistor connected to ADC pin (e.g., GP26)

# Gamma correction function
def gamma_correct(value, gamma):
    normalized = value / 255  # normalize input to range 0-1
    corrected = math.pow(normalized, gamma)  # apply gamma correction
    return int(corrected * 255)  # scale back to range 0-255

# Function to set PWM duty cycle with Gamma Correction
def set_led_brightness(brightness, gamma=2.2):
    corrected_brightness = gamma_correct(brightness, gamma)
    pwm_pin.duty_u16(int(corrected_brightness * 65535 / 255))  # Set corrected PWM value

# Test the setup by sweeping brightness values
def sweep_brightness():
    for i in range(256):
        set_led_brightness(i)  # Increase brightness
        time.sleep(0.01)
    for i in range(255, -1, -1):
        set_led_brightness(i)  # Decrease brightness
        time.sleep(0.01)

# Function to read the photoresistor value
def read_brightness():
    return adc_pin.read_u16()  # Returns a value from 0 to 65535

# Main loop to demonstrate brightness control
def main():
    gamma = 2.2  # Initial gamma value
    while True:
        brightness = 128  # Example fixed brightness level (can modify to test)
        set_led_brightness(brightness, gamma)
        measured_light = read_brightness()  # Measure the actual brightness using photoresistor
        print(f"Measured light: {measured_light}")  # Display brightness reading
        time.sleep(1)

# Start the program
if __name__ == "__main__":
    main()
```

### Explanation of Code:

1.  **PWM Setup**: The PWM signal is configured on a pin (GP15) connected to the base of the 2N2222 transistor through a 10K resistor. The frequency is set to 1kHz.

2.  **Gamma Correction Function**:

-   The function `gamma_correct(value, gamma)` applies a gamma curve to the brightness value. The value is normalized (0 to 255) and then raised to the power of the gamma correction value.
-   The gamma value of 2.2 is a typical default but can be adjusted based on how you want the LED brightness to behave.

### Testing Brightness Level

How do we know our gamma correction function is working and tha the constant value
of 2.2 is a good value to use?  We can test this by using a photoresistor
to measure the about of light generated by the LED.

-  We can use the `sweep_brightness()` function sweeps the brightness values from 0 to 255 (full range), testing the effect of gamma correction on brightness.
-  A photoresistor circuit connected to an ADC pin measures the actual brightness, providing feedback on how the LED is behaving.
-  We can observe the photoresistor readings to adjust the gamma correction for a more visually uniform brightness curve.

### Tuning Gamma Correction:

1.  **Gamma Value**: The `gamma` parameter can be modified in the `set_led_brightness` function. Start with a gamma of 2.2, then adjust higher for a steeper curve or lower for a flatter one.

-   **Lower gamma (<2.2)**: Makes the brightness ramp up more quickly at lower levels.
-   **Higher gamma (>2.2)**: Makes the brightness ramp up more slowly, giving more granularity at lower brightness levels.
2.  **Test Setup**:

- Connect the photoresistor circuit to an analog input on the Raspberry Pi Pico. Ensure that the photoresistor is positioned to detect light from the LED noodle.
-  Monitor the `measured_light` output in the `main()` loop and adjust the gamma based on the readings to achieve the desired brightness curve.


