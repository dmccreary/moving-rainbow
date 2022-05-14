Many of the low-cost Arduino Nanos use the popular CH34G drivers.

Unfortunatly, the Arduino IDE does not include these drivers.  It does include other drivers so we are not sure why the CH34G drivers and not used.

So you have to make sure to load the correct CH34G drivers!

Here is where you can get them:

http://www.wch.cn/download/CH341SER_MAC_ZIP.html

Yes, this page is in Chinese! :-)

There are drivers for both Windows and the Mac.  Each version of the Arduino IDE has be be synced with the operating system.  So the exact steps for each OS will be slightly different.  Google "CH34G Arduino Nano Drivers" to get more information on this topic.

Make sure you use the Arduino 1.6 platform (which should work with unsigned drivers) and reboot after you install the drivers.  Note that these drivers are "unsigned".

If you have a problem with some of the new mac OS that is picky about checking for signed drivers, you might have to disable the checking for a "signed" driver.

    sudo nvram boot-args=kext-dev-mode=1

You can re-enable driver signing after you are done:

    sudo nvram -d boot-args
