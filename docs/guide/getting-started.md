Getting Started
=======
In this section you will learn How To:

* Connect the LED Strip to the Arduino
* Install the Arduino IDE
* Install the Library to use the LED Strip
* Configure, deploy, and run a first program using the LED Strip
* Optional: Install Device Driver for off-brand Arduino Nano

### Connect the LED Strip to the Arduino

    Connect the red wire to the +5 
    Connect the black wire to GND
    Connect the yellow wire to pin 12 -- Note: pin number used later in code.

### Install the Arduino IDE

If you have not already done so, now is a good time to download the main Arduino Integrated Development Environment (IDE) software from <a target="_blank" href="http://arduino.cc/en/Main/Software">http://arduino.cc/en/Main/Software</a>

Follow the IDE installation directions.  Then, connect the Arduino device to your computer via USB.  Note: It may be necessary to install additional Device Driver for the computer to successfully connect and talk to the Arduino device.  See the "Install Device Driver for off-brand Arduino Nano" section below.

After the two are connected, you should be able to go to the Files -> Examples -> Basic -> Blink and open the
blink Sketch.  A Program for Arduino is called a Sketch.  Select to Upload the Sketch.  If it works, you should then see a built-in LED on the Arduino flash on and off.  Note: It may be necessary to select different values for Board, Processor, and Port through the Tools menu.  This is briefly covered in the "Install Device Driver for off-brand Arduino Nano" section below.

### Install the Library to use the LED Strip

To use the LED Strip from an Arduino Sketch (programming code), it is necessary to <a target="_blank" href="https://www.arduino.cc/en/guide/libraries">Install an Additional Arduino Library</a>.  We will use the Adafruit NeoPixel Libary.  There are different ways to install a Library.  Two installation methods are described next.  (You only need to complete one installation method.)

#### Library Installation Method 1: Download, Unzip, Rename, and Move Folder

Download the newest version of the NeoPixel Library as a Zip file, from the NeoPixel project repository.

Download: <a href="https://github.com/adafruit/Adafruit_NeoPixel/archive/master.zip">https://github.com/adafruit/Adafruit_NeoPixel/archive/master.zip</a>

(If that direct link to download the zip file stops working, an alternative may be available from the NeoPixel repository at <a target="_blank" href="http://github.com/adafruit/Adafruit_NeoPixel">http://github.com/adafruit/Adafruit_NeoPixel</a> .)

Unzip, Rename, and Move Folder

The downloaded NeoPixel Library is in a single zip file, likely named Adafruit_NeoPixel-master.zip.  The contents of this file must be unzipped, renamed, and moved to a specific location.

One way to unzip this file onto your local computer is to right-click the file and look for an "unzip" option.  Once unzipped, you will see a folder likely named "Adafruit_NeoPixel-master".

Rename the folder to 'Adafruit_NeoPixel' (remove the '-master' suffix), and move it to one of these three locations:
1. For Linux and Mac computers, the `Arduino/Libraries/` folder in your `~` home directory
1. For Windows computers, the `Documents\Arduino\libraries\` folder in your home directory -- Often `C:\Users\USERNAME\`
1. For Windows computers, to install the Library for all users, place it in the `libraries` folder of the Arduino IDE installation -- Often `C:\Program Files (x86)\Arduino\libraries\`.  Note that this installation option is "fragile", where updates to the Arduino IDE installation might remove items added to its `libraries` folder.

#### Library Installation Method 2: Install via Arduino IDE Library Manager

Using the Arduino IDE, select Sketch -> Include Library -> Manage Libraries...

Search for Adafruit NeoPixel

Select "Install" button for the newest version (1.1.8 as of 2019-03-11).

This method automatically downloads a zip file to `C:\Users\USERNAME\AppData\Local\Arduino15\staging\libraries` and installs the Library to `C:\Users\USERNAME\Documents\Arduino\libraries\Adafruit_NeoPixel`.

#### Restart the Arduino IDE

After installing the library in the right location, it may be necessary to close and restart the Arduino IDE.

### Configure, deploy, and run a first program using the LED Strip

Using the Arduino IDE, open the strandtest Sketch.  It is available via

    File -> Sketchbook -> Library -> Adafruit_NeoPixel -> strandtest
	OR
	File -> Examples -> Adafruit NeoPixel -> strandtest

Change the code that initializes the LED Strip so that it uses pin 12, as connected to during the "Connect the LED Strip to the Arduino" step above.  Either:

    Adafruit_NeoPixel strip = Adafruit_NeoPixel(12, 12, NEO_GRB + NEO_KHZ800);

or change `#define PIN 6` to `#define PIN 12`

Connect Arduino to the computer via USB.  Then, in the Tools menu, it may be necessary to change the values for Board, Processor, and Port.  Depending on the Arduino device and connection, working values might be "Arduino Nano", "ATmega328P (Old Bootloader)", and "COM3" or "COM4".

Select "Upload" in the Arduino IDE.

If successful, the output console dislays the message "Done uploading." and the LED Strip should rotate through differing LED flashing and color patterns.

If the output console dislays a message other than "Done uploading." followed by details of Sketch size and variables memory size, then things are likely not working, and it's time for troubleshooting.  Maybe the board type you have is "Uno" and not "Nano".  Maybe the Arduino device is connected on a different port.  Maybe the necessary device driver is not yet installed.

### Optional: Install Device Driver for off-brand Arduino Nano

If you do not see the serial port for the connected Arduino device when you go to the Tools -> Port menu in the Arduino IDE, it may be that your computer does not yet have the CH340 device driver needed to connect to the off-brand Arduino Nano used with this project.  Follow these steps to install the CH340 driver.

Note: Local admin rights on your computer are needed when installing the driver.

#### For Windows 10

There are two options for installing the CH340 Driver that are confirmed to be working as of 2019-03-11.  After completing either of these installation options, restart the computer.

Installation Option 1: Use Device Manager

With the Arduino device connected to the computer via USB, run the Windows Device Manager program with Administrator permissions.  If Device Manager lists a problem device, such as "Other devices -> USB2.0-Serial" with "Device status" of "The drivers for this device are not installed.", select to "Update Driver" and select to allow Windows to search all locations, i.e., the internet, for a driver.  If successful, the driver for device "USB-SERIAL CH340" will be installed.  In Device Manager, the device will then be listed in the "Ports (COM & LPT)" section, and the "Device status" will have changed to "This device is working properly."

Driver Details as of 2019-03-11:

    Driver:
    Provider: wch.cn
    Date: 2014-08-08
    Version: 3.4.2014.8
    Signer: Microsoft Windows Hardware Compatibility Publisher

Restart the computer.

Installation Option 2: Download and Run

Download the "setup executable" version of the FTDI Driver from <a target="_blank" href="https://www.ftdichip.com/Drivers/VCP.htm">https://www.ftdichip.com/Drivers/VCP.htm</a>

As of 2019-03-11, the latest version 2.12.28 released 2017-08-30 was available directly at <a target="_blank" href="https://www.ftdichip.com/Drivers/CDM/CDM21228_Setup.zip">https://www.ftdichip.com/Drivers/CDM/CDM21228_Setup.zip</a>

Unzip the downloaded file, and run the Setup.exe installation program.

Restart the computer.

#### For Mac

Download the CH340 Driver from <a target="_blank" href="http://www.wch.cn/download/CH341SER_MAC_ZIP.html">http://www.wch.cn/download/CH341SER_MAC_ZIP.html</a>

Note that as of August of 2015, the driver for the Mac is still "unsigned" and will not work on modern Mac OSs (Yousemite).

The workaround this is to temporarly disable checking for a signed driver on the Mac.  To do this run the following program in the Mac UNIX Console /Applications -> Utilities -> Terminal

     sudo nvram boot-args="kext-dev-mode=1"

The most current version of Mac (El Capitan) has some problems recognizing the NEO board.  Per [this Stack Exchange](http://arduino.stackexchange.com/questions/14018/arduino-not-detected-on-el-capitan-public-beta-6) thread, downloading a paid driver has helped one student in this demo.

After you run this command you must reboot the Mac for it to take effect.  This will allow the driver to be loaded, though it is unsigned.

See this helpful post on [Installing the CH340 Driver on Yosemite on the Mac](http://kiguino.moos.io/2014/12/31/how-to-use-arduino-nano-mini-pro-with-CH340G-on-mac-osx-yosemite.html)

After the driver is installed you should see a non-Bluetooth port appear.  
