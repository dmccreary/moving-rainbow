import machine
import time
photo_pin = machine.ADC(26)

while True:
    // shift the ADC value over eight bits so we get a value between 0 and 255
    val = photo_pin.read_u16() >> 8
    print(val)
    time.sleep(.1)