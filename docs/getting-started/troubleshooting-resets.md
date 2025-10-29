# Troubleshooting Resets

It is a common problem when using the Thonny IDE that your
microcontroller will not reset.  This is often that the
`main.py` program starts up when the power comes on but
the device stops listening for interrupts.  This can be VERY frustrating
if you have just written lots of code using Thonny but
have not got a chance to back up your code.

Note that by typing the following command, you will know that
the USB port has been detectd:

```sh
ls -l /dev/cu.usbmodem101
```

If this does not work try this:

```sh
ls -l /dev/cu.usbmodem*
```

One workaround is to use the following command `screen` command:

```sh
screen /dev/cu.usbmodem101 115200
```

This will bring up the MicroREPL loop in your terminal.
You can the use the CONTROL-C command to stop the loop.

Next, you can rename the `main.py` file:

```sh
import os
os.rename('main.py', 'main_backup.py')
```

Then close your Terminal, reset the microcontroller and
restart Thonny.

The root cause of this problem is that the Raspberry Pi Pico
is in a "tight loop" and not listening for interrupt signals.
