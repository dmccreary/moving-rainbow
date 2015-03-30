Getting Started
=======
In this section you will learn:

* How to install the Arduino IDE
* How to download the Ardunio libraries
* How to install the LED Ardunio libraries to work with your Arduino software
* How to hook up your LED strip to your Arduino
* How configure your programs to match your LED strip
* How to test and debug your connections

### Download the Arduino Developer Tools
If you have not already done so, now is a good time to download the main Arudino software from the following location:.

[http://arduino.cc/en/Main/Software](http://arduino.cc/en/Main/Software)

follow the installation directions and then connect your Arduino to your computer using the USB cable.  
After the two are connected you should be able to go to the Files -> Examples -> Basic -> Blink and open the
blink program.  You should then be able to see the LED on the Arudion flash on and off.

### Download the Adafruit NeoPixel Libaries

Click the link below or copy the following URL in your browser:

[http://github.com/adafruit/Adafruit_NeoPixel](http://github.com/adafruit/Adafruit_NeoPixel)

and "download" the NeoPixel Library zip file.  Look for the "Download Zip" button in the lower right corner.


### Unzip and Rename
The software and you downloaded will be in a single zip file with the name:

Adafruit_NeoPixel-master.zip

You must first unzip this file onto your local hard drive.  One way to do this is to right click over
the file and look for an "unzip" option.

After you have unziped the file you will see a folder like "Adafruit_NeoPixel-master".

Next, you must rename folder to 'Adafruit_NeoPixel' (remove the -master suffix) and copy it into the correct location.
Typically this is in Arduino/Libraries folder in your home directory.


### Restart the Arduino IDE

After you have the library in the right location you must Restart Arduino IDE.  Then open 

    File->Sketchbook->Library->Adafruit_NeoPixel->strandtest sketch.

### Change the line that initializes the strip to use pin 12

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(12, 12, NEO_GRB + NEO_KHZ800);

### Make the following connections of the LED strip
    connect the red wire to the +5 
    connect the black wire to GND
    connect the yellow wire to pin 12
    
### Connect your Arduino to the USB and press the "upload" button. 

If you have any errors, check to make sure your Tools -> Port is set to the right USB port and make sure your board is set to be "Uno".