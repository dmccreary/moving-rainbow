from machine import Pin, PWM
from time import sleep

# lower left corner of the Pico
LED_PIN_1 = 15
# led_1 = machine.Pin(LED_PIN_1, machine.Pin.OUT)
pwm = PWM(Pin(LED_PIN_1))

pwm.freq(1000)
MAX_BRIGHTNESS = 65025

while True:
    for duty in range(MAX_BRIGHTNESS):
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(MAX_BRIGHTNESS, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)