# light level measurement
# read the voltage across a voltage divider where one end is a photoresistor
import machine
from utime import sleep
import config

# The ADC pins on the pico are 26, 27 o4 28
PHOTORESISTOR_PIN = config.PHOTORESISTOR_PIN

photo_pin = machine.ADC(PHOTORESISTOR_PIN)

# a pitch black room is about 1500
# a brightly lit room is 55000
# The nightlight should go on below 10,000?
while True:
    val = photo_pin.read_u16()
    print(val)
    sleep(.2)