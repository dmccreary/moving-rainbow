# Fade In and Out Lab

What if instead of the first LED just turning on and off we want to slowly make the LED get brighter and then slowly dimmer?  To do this we will change the brightness of the red from off (0) to fully on (255) in steps
with a small delay of 1/100th of a second between the steps.

```py
from neopixel import NeoPixel
from time import sleep

NUMBER_PIXELS = 1
LED_PIN = 0

strip = NeoPixel(machine.Pin(LED_PIN), NUMBER_PIXELS)

# the time between each of the 255 brightness steps
delay = .01

while True:
    # slowly get brighter
    for i in range(0, 255):
        strip[0] = (i,0,0) # red=255, green and blue are 0
        strip.write() # send the data from RAM down the wire
        sleep(delay)
    # slowly get dimmer
    for i in range(255, 0, -1):
        strip[0] = (i,0,0)
        strip.write()
        sleep(delay)
```