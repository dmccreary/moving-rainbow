# RGB Project Box
This box has three potentiometers on it that control the intensity of the red, green and blue LEDs in a LED strip.

# Wriring Diagram
The top and bottom connectors of each potentiometer are connected to the +5v and ground rails of the breadboard.
The center tap of the first potentiomer goes to first analog input called pin A0.
The center tap of the second potentiometer goes to the second analog input called the A1 pin.
The center tap of the third potentiometer goes to the third analog input called the A2 pin.

# Code
We use the Adafruit Neopixel libraries.

The main loop does an analog read on each potentiomter and then converts the analog value from a scale of 0 to 1023 to a LED intensity of 0 to 255.  We use the map() function to do this.

We can also adjust the top and bottom maximum values so that we check that the values are within a range.  This takes into account that the potentiometer may not go exactly from zero resistence to maximum resistence.

