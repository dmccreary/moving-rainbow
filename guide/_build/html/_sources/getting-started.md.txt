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

### Loading the CH340 Drivers

It is possible your version of the Arduino IDE does not have the correct drivers for the Arduino Nano CH340 USB interface chip.
If you do not see the serial port for the Arduino when you go to the Tools -> Port menu you need to check your driver.

The first step is to manually install the driver.  This can be done at the following URL:

[CH340 Driver Downloads](http://www.wch.cn/download/CH341SER_MAC_ZIP.html)

Make sure you have admin rights on your computer before you install this driver.

Note that as of August of 2015, the driver for the Mac is still "unsigned" and will not work on modern Mac OSs (Yousemite) .
The workaround this is to temporarly disable checking for a signed driver on the Mac.  To do this run the following
program in the Mac UNIX Console /Applications- > Utilities -> Terminal

     sudo nvram boot-args="kext-dev-mode=1"
     

The most current version of Mac (El Capitan) has some problems recognizing the NEO board.  Per [this Stack Exchange](http://arduino.stackexchange.com/questions/14018/arduino-not-detected-on-el-capitan-public-beta-6) thread, downloading a paid driver has helped one student in this demo.

After you run this command you must reboot the Mac for it to take effect.  This will allow the drivers to be loaded even though they are unsigned drivers.

See this helpful post on [Installing the CH340 Driver on Yosemite on the Mac](http://kiguino.moos.io/2014/12/31/how-to-use-arduino-nano-mini-pro-with-CH340G-on-mac-osx-yosemite.html)

After the driver is installed you should see a non-Bluetooth port appear.  
