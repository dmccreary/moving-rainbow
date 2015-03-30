Getting Started
=======
In this section you will learn:

* How to download the Ardunio libraries
* How to install the LED Ardunio libraries to work with your Arduino software
* How to hook up your LED strip to your Arduino
* How configure your programs to match your LED strip
* How to test and debug your connections

### Download the Adafruit NeoPixel Libaries


Put the following URL in your browser:

[http://github.com/adafruit/Adafruit_NeoPixel](http://github.com/adafruit/Adafruit_NeoPixel)

and "download" the NeoPixel Library zip file.  Look for the "Download Zip" button in the lower right corner.


### Unzip the software and you should see a folder like "Adafruit_NeoPixel-master"


### Rename folder to 'Adafruit_NeoPixel' and install in Arduino/Libraries folder.


### Restart Arduino IDE, then open File->Sketchbook->Library->Adafruit_NeoPixel->strandtest sketch.
### Change the line that initializes the strip to use pin 12

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(12, 12, NEO_GRB + NEO_KHZ800);

### Make the following connections of the LED strip
    connect the red wire to the +5 
     connect the black wire to GND
     connect the yellow wire to pin 12
### Connect your Arduino to the USB and press the "upload" button. 

If you have any errors, check to make sure your Tools -> Port is set to the right USB port and make sure your board is set to be "Uno".