# Heartbeat Lab

What if you were building a robot and you wanted to flash the LED to look like a human heartbeat? 
Instead of slowing fading in and out, you would want the brightness to follow the electrical signals coming from the heart. This is called an elecrto cardiogram (EKG) and it look like this:

![](../img/ekg-sample.png)

Notice that the signal is low for about one second and then it spikes up to maximum brightness and then comes back down. When we are moving the brightness up and down, we don't have to pause between each of the 256 brightness values. The eye can't usually see the intermediate brightness values if the brightness is changing quickly. To make our code efficient we can skip over 9 out of 10 of the brightness gradations between 0 and 255. We call this the skip_interval in our code below.

The following code emulates this heart beat pattern:

```py
from neopixel import NeoPixel
from time import sleep

# Most people have a heart rate of around 60-70 beats per minute
# If we add a once second delay between "beats" you can make and LED
# look like a beating heart.

NUMBER_PIXELS = 1
LED_PIN = 0

strip = NeoPixel(machine.Pin(LED_PIN), NUMBER_PIXELS)

ramp_delay = .001
beat_delay = 1
skip_interval = 10

while True:
    # ramp brightness up using the ramp_delay
    for i in range(0, 255, skip_interval):
        strip[0] = (i,0,0)
        strip.write()
        sleep(ramp_delay)
    # ramp brightness down using the same delay
    for i in range(255, 0, -skip_interval):
        strip[0] = (i,0,0)
        strip.write()
        sleep(ramp_delay)
    strip[0] = (0,0,0)
    strip.write()
    sleep(beat_delay)
    ```