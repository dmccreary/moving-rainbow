from machine import ADC
from utime import sleep
pot = ADC(26)
while True:
    # print values from 0 to 255
    print(pot.read_u16() >> 8, end=" ")
    sleep(.1)