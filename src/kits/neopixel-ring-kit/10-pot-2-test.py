from machine import ADC
from utime import sleep
import config

pot = ADC(config.POT_2_PIN)
while True:
    print(pot.read_u16())
    sleep(.2)