from machine import Pin, PWM
from time import sleep

# lower left corner of the Pico
LED_PIN_1 = 15
led_1 = machine.Pin(LED_PIN_1, machine.Pin.OUT)
delay = 1.0 3 # one second on and one second off

# Main loop: Repeat the forever...
while True:
    print('high')
    led_1.high() # turn on the LED
    sleep(delay) # leave it on for 1 second
    
    print('low')
    led_1.low()  # Turn off the LED
    sleep(delay) # leave it off for 1 second
    