from machine import Pin
import time

# input on the lower left of the Pico
# the other side of the button goes to ground
# if the switch is open the value is pulled up to 3.3 volts
button = Pin(15, Pin.IN, Pin.PULL_UP) 

while True:
    print(button.value())
    time.sleep(0.1) # wait 1/10th of a second
