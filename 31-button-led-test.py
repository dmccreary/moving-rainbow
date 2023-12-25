from machine import Pin
import time

# input on the lower left of the Pico
# the other side of the button goes to ground
# if the switch is open the value is pulled up to 3.3 volts
BUTTON_PIN = 15

# Create a button object on the pin
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP) 

BUILT_IN_LED_PIN = 25
# create an LED object
led = Pin(BUILT_IN_LED_PIN, Pin.OUT)

button_value = 0
old_value = 0
while True:
    # get the new value
    button_value = button.value()
    
    # change the LED to on when the button is pressed
    if button_value == 1:
        led.off()
    else:
        led.on()
        
    # only print on if there is a change
    if button_value != old_value:
        print(button_value)
        old_value = button_value
