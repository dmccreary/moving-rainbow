# Rainbow

Now let's bring some real color to this class!

Recall our color wheel MicroSim:

<iframe src="../../sims/color-wheel/main.html" height="450" scrolling="no"></iframe>

Let me introduce you to one of the most colorful functions
in the MicroPython world.  It is the famous `wheel` function.
When you think of the color wheel, think of the `wheel` function.
Wouldn't it be nice to just take a stroll around the color wheel
and walk through all the colors of the rainbow!  Well, `wheel` is here to help you do just that!

The `wheel` functions looks like this:

```py
wheel(color_number_0_to_255)
```
You just give it a number from 0 to 255 and it will return
a red, green and blue number that will span the spectrum from
red, orange, yellow, green, blue, indigo and violet and then
back to red again.

Here is the entire elegant wheel function in all its glory:

```py
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
```

Here is a markdown table with the values for 10 common colors from the wheel function. The wheel function creates a smooth transition from red to green to blue and back to red as the input value goes from 0 to 255.

# Common Colors in the Wheel Function

| Color Name | Wheel Position | RGB Values |
|------------|----------------|------------|
| Red        | 0              | (255, 0, 0) |
| Orange     | 32             | (159, 96, 0) |
| Yellow     | 64             | (63, 192, 0) |
| Green      | 85             | (0, 255, 0) |
| Teal       | 127            | (0, 129, 126) |
| Cyan       | 128            | (0, 128, 127) |
| Blue       | 170            | (0, 0, 255) |
| Purple     | 191            | (63, 0, 192) |
| Magenta    | 213            | (126, 0, 129) |
| Pink       | 234            | (189, 0, 66) |

This table shows how the wheel function generates a spectrum of colors by adjusting the RGB values based on the input position (0-255). Each position produces a unique combination of red, green, and blue values, creating the full color wheel.

I suggest you bookmark this page because for fun projects
we will come back to this function frequently.

## Testing the Wheel Program

Here is a full test program that will demonstrate how the `wheel` function is used in practice.

```py
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
# get the configuration information

NUMBER_PIXELS = 30
strip = NeoPixel(Pin(0), np)
# we have each pixel step through the color wheel
color_wheel_step = int(256 / NUMBER_PIXELS)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

current_color = 0
print('Drawing rainbow in', np, 'steps with step size of: ', color_wheel_step)
for i in range(0,NUMBER_PIXELS):
    strip[i] = wheel(current_color)
    current_color = current_color + color_wheel_step
    print(i, current_color, wheel(current_color))
    strip.write()
    sleep(.03)
```