# Glossary of Terms

#### Abstraction
The practice of focusing on essential details while hiding unnecessary complexity.

**Example:** Using a `wheel()` function to generate colors without needing to understand the underlying RGB math.

#### ADC
Analog-to-Digital Converter; a circuit that converts continuous voltage signals into digital numbers a microcontroller can process.

**Example:** The Raspberry Pi Pico uses an ADC to read the voltage from a potentiometer and control LED brightness.

#### Addressable LED
A light-emitting diode that can be individually controlled through programming, unlike traditional LEDs that turn on and off together.

**Example:** Each pixel in a NeoPixel strip is an addressable LED that can display a different color.

#### Algorithm
A step-by-step procedure for solving a problem or completing a task.

**Example:** The rainbow cycle algorithm calculates color values, assigns them to pixels, and repeats to create a moving rainbow effect.

#### Animation
A visual pattern that changes over time by updating LED colors and positions.

**Example:** The comet tail animation creates the appearance of movement by fading pixels behind a bright leading pixel.

#### Anode
The positive terminal of an electronic component where electrical current enters.

**Example:** Connect the longer leg of an LED (the anode) to the positive voltage supply.

#### ARM Cortex M0+
A type of processor designed for low-power microcontrollers.

**Example:** The Raspberry Pi Pico uses two ARM Cortex M0+ processors running at 133 MHz.

#### Array
An ordered collection of values stored under a single variable name and accessed by position number.

**Example:** The colors array `(red, orange, yellow, green, blue, indigo, violet)` stores seven rainbow color values.

#### Assignment
The operation of storing a value in a variable using the equals sign.

**Example:** The statement `counter = 0` assigns the value zero to the variable named counter.

#### Autocomplete
A feature in programming software that suggests code as you type.

**Example:** Thonny's autocomplete shows available functions when you type `strip.` after creating a NeoPixel object.

#### Base
The control terminal of a transistor that allows a small current to control a larger current flow.

**Example:** Connecting a GPIO pin through a resistor to the base of an NPN transistor allows the microcontroller to switch LED noodles on and off.

#### Base Current
The small electrical current flowing into the base terminal of a transistor.

**Example:** A base current of 0.5 mA can control a collector current of 50 mA in a transistor with a gain of 100.

#### Battery
A device that stores electrical energy chemically and releases it as electrical current.

**Example:** A 3.7-volt LiPo battery can power a Raspberry Pi Pico and LED strip for portable projects.

#### Battery Capacity
The total amount of electrical energy a battery can store, measured in milliamp hours.

**Example:** A 2000 mAh battery can theoretically supply 2000 milliamps for one hour or 200 milliamps for ten hours.

#### Battery Charger
An electronic circuit that safely refills a rechargeable battery with electrical energy.

**Example:** The TC4056 chip is a battery charger that can charge a LiPo battery at up to 1 amp.

#### Battery Life
The duration a battery can power a device before requiring recharge or replacement.

**Example:** Calculate battery life by dividing battery capacity (2000 mAh) by current draw (200 mA) to get 10 hours.

#### Bench Power Supply
An adjustable laboratory device that provides controlled voltage and current for testing circuits.

**Example:** Set the bench power supply to 5 volts and 500 mA to safely test your LED strip circuit.

#### Bias Current
A small control current that sets the operating point of an electronic component.

**Example:** The bias current flowing into a transistor base determines whether the transistor is on or off.

#### Binary Data
Information represented using only two symbols, typically 0 and 1.

**Example:** The color value 255 is represented in binary data as 11111111.

#### Binary Encoding
The process of representing information using combinations of 0s and 1s.

**Example:** Use binary encoding to display numbers on an 8x8 matrix by treating each row as an 8-bit binary number.

#### Bit
The smallest unit of digital information, having a value of either 0 or 1.

**Example:** An 8-bit color value uses eight bits to represent 256 different brightness levels from 0 to 255.

#### Blink
A pattern where LEDs turn on and off repeatedly at regular intervals.

**Example:** The first lesson creates a simple blink pattern by turning the first pixel red for one second, then off for one second.

#### Boolean
A data type with only two possible values: True or False.

**Example:** The boolean expression `counter > 10` evaluates to True when the counter variable exceeds 10.

#### BOOTSEL Button
A button on the Raspberry Pi Pico that enters USB mass storage mode when held during power-up.

**Example:** Hold the BOOTSEL button while connecting USB to program the Pico by dragging a UF2 file.

#### Bootloader
A small program that runs when a device powers on and loads the main operating system or firmware.

**Example:** The Pico's bootloader allows you to program it by copying files when in BOOTSEL mode.

#### Branch
A separate version of code in a repository that allows changes without affecting the main version.

**Example:** Create a new branch in GitHub to experiment with a new animation pattern before merging it into the main code.

#### Breadboard
A plastic board with interconnected holes for building temporary electronic circuits without soldering.

**Example:** Insert the Pico into a breadboard to easily connect it to buttons and LED strips with jumper wires.

#### Brightness
The intensity of light emitted by an LED, typically controlled by the magnitude of color values.

**Example:** Reduce brightness by scaling all RGB values by 0.5, changing (255, 0, 0) to (128, 0, 0).

#### Buck Converter
An electronic circuit that efficiently reduces voltage while maintaining power.

**Example:** A buck converter converts 5 volts from USB to 3.3 volts for the microcontroller more efficiently than a resistor.

#### Candle Flicker
An animation pattern that simulates a flame by randomly varying orange and yellow colors.

**Example:** The candle flicker function randomly sets pixels to yellow or red-orange values to create a realistic fire effect.

#### Castellated Module
A circuit board with half-circle holes along the edges for surface-mount soldering.

**Example:** The RP2040-Zero is a castellated module that can be soldered directly onto a larger board.

#### Cathode
The negative terminal of an electronic component where electrical current exits.

**Example:** The shorter leg of an LED is the cathode and should be connected to ground.

#### Charging Current
The electrical current flowing into a battery during the charging process.

**Example:** The IP2312 charger supplies a charging current of up to 3 amps to quickly recharge LiPo batteries.

#### Charging Efficiency
The percentage of electrical energy that successfully enters a battery versus what is lost as heat.

**Example:** A charging efficiency of 85% means 15% of the power is wasted as heat during charging.

#### Circuit
A complete path through which electrical current can flow from positive to negative terminals.

**Example:** A basic LED circuit includes a power source, current-limiting resistor, LED, and connection back to ground.

#### Clock Speed
The rate at which a processor executes instructions, measured in megahertz or gigahertz.

**Example:** The RP2040 runs at a clock speed of 133 MHz, executing 133 million operations per second.

#### Clone
The action of creating a complete local copy of a remote code repository.

**Example:** Clone the Moving Rainbow repository from GitHub to download all lessons and example code to your computer.

#### Collector
The output terminal of an NPN transistor where controlled current flows to the load.

**Example:** Connect the LED noodle string to the collector of the transistor to switch them on and off.

#### Collector Current
The electrical current flowing through the collector terminal of a transistor.

**Example:** If the collector current is 50 mA and the LED noodles are at 3 volts, they consume 150 milliwatts of power.

#### Color Value
A number from 0 to 255 representing the intensity of a single color component.

**Example:** In the RGB tuple (255, 128, 0), the red color value is 255 (maximum), green is 128 (medium), and blue is 0 (off).

#### Color Wheel
A circular arrangement of colors showing smooth transitions through the visible spectrum.

**Example:** The `wheel()` function takes a number from 0 to 255 and returns an RGB color from the color wheel.

#### Color Wipe
An animation that fills the LED strip with a single color, one pixel at a time.

**Example:** The color wipe function uses a for loop to set each pixel to red sequentially with a short delay between them.

#### Comet Tail
An animation pattern featuring a bright leading pixel followed by progressively dimmer pixels creating a trailing effect.

**Example:** The comet tail animation uses brightness levels (255, 128, 64, 32, 16, 8, 4, 2, 1) to create a fading trail behind the moving pixel.

#### Comment
Text in code that is ignored by the computer but helps humans understand what the code does.

**Example:** The line `# turn the first pixel on` is a comment explaining the next line of code.

#### Commit
A saved set of changes to code with a description of what was modified.

**Example:** After fixing a bug in the rainbow function, create a commit with the message "Fixed rainbow color calculation".

#### Comparison
An operation that checks the relationship between two values, such as equal to, greater than, or less than.

**Example:** The comparison `counter < NUMBER_PIXELS` returns True when the counter is less than the total number of pixels.

#### Computational Thinking
A problem-solving approach that uses concepts from computer science to break down and solve problems.

**Example:** Use computational thinking to design a new LED pattern by decomposing it into smaller steps, recognizing color patterns, and creating an algorithm.

#### Concept Cards
Single-topic educational cards that teach one specific concept or skill.

**Example:** Each lesson in Moving Rainbow acts like a concept card, focusing on one animation technique such as moving pixels or color wheels.

#### Conditional
A programming construct that executes different code based on whether a condition is true or false.

**Example:** Use a conditional `if mode == 0:` to run the rainbow animation only when mode equals zero.

#### Constant Current
A power supply mode that maintains a fixed current regardless of voltage changes.

**Example:** A battery charger runs in constant current mode to safely charge a battery at 500 mA.

#### Constant Voltage
A power supply mode that maintains a fixed voltage regardless of current draw.

**Example:** USB provides constant voltage at 5 volts whether you draw 100 mA or 500 mA.

#### Current
The flow of electrical charge through a conductor, measured in amperes.

**Example:** An LED strip drawing 300 milliamps requires a current of 0.3 amperes from the battery.

#### Current Draw
The amount of electrical current a device consumes during operation.

**Example:** Calculate total current draw by multiplying the number of pixels (30) by the current per pixel (60 mA) to get 1800 mA.

#### Current Gain
The ratio of output current to input current in a transistor, also called beta.

**Example:** A transistor with current gain of 100 allows a 1 mA base current to control a 100 mA collector current.

#### Current Limiting Resistor
A resistor placed in series with a component to prevent excessive current flow.

**Example:** Place a 220-ohm current limiting resistor between a GPIO pin and LED to prevent damage.

#### Current Monitor
A device or circuit that measures the electrical current flowing through a conductor.

**Example:** Use a current monitor to verify that your LED strip is drawing the expected 1.8 amps.

#### Curriculum
A structured plan of educational content organized by topic and difficulty.

**Example:** The Moving Rainbow curriculum progresses from simple blink patterns to complex multi-mode animations.

#### Data Line
A wire or connection that carries information signals rather than just power.

**Example:** The middle wire of the JST connector is the data line that sends color commands to the NeoPixel strip.

#### Data Signal
An electrical signal that carries information encoded as voltage changes.

**Example:** The Pico sends a data signal to the LED strip containing color values for each pixel.

#### Data Transmission
The process of sending information from one device to another.

**Example:** Data transmission from the Pico to the LED strip happens serially, one bit at a time at high speed.

#### Data Type
A category that defines what kind of information a variable can store.

**Example:** Common data types include integers for whole numbers, floats for decimals, and strings for text.

#### DC Voltage
Direct Current voltage that flows in only one direction with constant polarity.

**Example:** Batteries provide DC voltage, unlike household outlets which provide alternating current.

#### Debugging
The process of finding and fixing errors in code or circuits.

**Example:** Use print statements for debugging to see which values variables contain when your animation doesn't work correctly.

#### Decrement
The operation of reducing a variable's value by one or a specified amount.

**Example:** The statement `mode -= 1` decrements the mode variable by one when button 2 is pressed.

#### Deep Linking
A URL that points to a specific section within a webpage rather than just the page itself.

**Example:** Use deep linking to share the exact location in the documentation where the rainbow cycle function is explained.

#### Delay
A pause in program execution for a specified duration.

**Example:** Add a delay of 0.05 seconds between pixel updates to control animation speed.

#### Device ID
A unique number that identifies a specific piece of hardware.

**Example:** Each USB device has a device ID that helps the computer recognize what type of device is connected.

#### Diode
An electronic component that allows electrical current to flow in only one direction.

**Example:** The 1N4007 diode prevents reverse current from damaging the circuit if battery polarity is reversed.

#### Drag-and-Drop Programming
A method of programming by copying a file to a device appearing as a USB drive.

**Example:** Program the Pico using drag-and-drop programming by copying a UF2 file to the RPI-RP2 drive.

#### Dual-Core
A processor containing two independent processing units that can run tasks simultaneously.

**Example:** The RP2040 is dual-core, allowing it to run two programs at the same time.

#### Duty Cycle
The percentage of time a signal is in the "on" state during a cycle.

**Example:** A PWM signal with 75% duty cycle is on for three-quarters of each cycle, creating bright LED output.

#### Edge Pinout
The arrangement of connection pins along the edges of a circuit board.

**Example:** The Pico's edge pinout has 20 pins on each side, labeled with their GPIO numbers.

#### Emitter
The ground-connected terminal of an NPN transistor.

**Example:** Connect the emitter of the transistor to the circuit ground for proper operation.

#### Externally Powered
A device receiving electrical power from a wall adapter rather than a computer or battery.

**Example:** Use an externally powered USB hub when connecting multiple LED strips to avoid overloading your computer's USB ports.

#### Fade
A gradual change in LED brightness, either increasing or decreasing over time.

**Example:** The heartbeat pattern uses a fade to smoothly transition from dim to bright and back.

#### Fairy Lights
Lightweight LED strings commonly used for costumes and decorations.

**Example:** Sew fairy lights into Halloween costumes because they are flexible and battery-powered.

#### File System
The organizational structure for storing and retrieving files on a storage device.

**Example:** The Pico's file system stores your Python programs and config.py file in flash memory.

#### Firmware
Software that is permanently programmed into a hardware device to control its basic functions.

**Example:** Update the Pico's firmware to the latest version of MicroPython to access new features.

#### Flash Memory
Non-volatile storage that retains data when power is removed.

**Example:** The Pico has 2 MB of flash memory to store your Python programs permanently.

#### Floating Point
A data type for representing decimal numbers with fractional parts.

**Example:** The floating point value 0.05 represents a 50 millisecond delay when used with the sleep function.

#### For Loop
A programming loop that repeats code a specific number of times, often counting through a range.

**Example:** Use a for loop `for i in range(30):` to set colors for all 30 pixels in the strip.

#### Fork
Creating a personal copy of someone else's repository on GitHub that you can modify.

**Example:** Fork the Moving Rainbow repository to create your own version where you can add custom animations.

#### Forward Voltage Drop
The voltage consumed by a component when current flows through it in the correct direction.

**Example:** A diode has a forward voltage drop of about 0.7 volts, reducing the voltage available to other components.

#### Function
A named block of code that performs a specific task and can be reused multiple times.

**Example:** Define a function `def move_dot(counter, color, delay):` to encapsulate the moving dot animation code.

#### Gamma Correction
An adjustment to brightness values that compensates for non-linear human perception of light.

**Example:** Apply gamma correction using a lookup table so brightness changes appear smooth to the human eye.

#### Gamma Table
A predefined list of adjusted brightness values used for gamma correction.

**Example:** A gamma table maps linear values 0-255 to corrected values that appear evenly spaced to human vision.

#### GitHub
An online platform for storing, sharing, and collaborating on code projects.

**Example:** The Moving Rainbow project is hosted on GitHub at [http://github.com/dmccreary/moving-rainbow](http://github.com/dmccreary/moving-rainbow).

#### GitHub Pages
A free website hosting service provided by GitHub for project documentation.

**Example:** The Moving Rainbow documentation website is published using GitHub Pages at [http://dmccreary.github.io/moving-rainbow](http://dmccreary.github.io/moving-rainbo).

#### Global Variable
A variable that can be accessed and modified from anywhere in a program.

**Example:** Declare `global mode` inside a function to modify the mode variable defined outside the function.

#### GPIO
General Purpose Input/Output; programmable pins on a microcontroller that can send or receive electrical signals.

**Example:** GPIO pin 0 on the Pico is commonly used as the data output for NeoPixel strips.

#### Ground
The reference point in a circuit for voltage measurements, typically the negative terminal.

**Example:** Connect all black wires to ground (GND) to complete the electrical circuit.

#### Header Pins
Metal pins extending from a circuit board used for making electrical connections.

**Example:** Solder header pins to the Pico so it can be inserted into a breadboard.

#### Heat Dissipation
The process of transferring excess heat away from a component to prevent overheating.

**Example:** The TC4056 charger chip requires heat dissipation when charging at high current, which is why it gets warm.

#### Heat Sink
A metal component attached to electronics to improve heat dissipation.

**Example:** Attach a heat sink to the voltage regulator if it gets too hot when running many LEDs.

#### Heartbeat
An animation pattern that pulses LEDs brighter and dimmer to simulate a beating heart.

**Example:** The heartbeat function uses a fade in and fade out cycle with a brief pause between beats.

#### Hue
A pure color without considering brightness or saturation.

**Example:** Red, green, and blue are different hues, while pink and dark red are the same hue with different brightness and saturation.

#### I2C
Inter-Integrated Circuit; a communication protocol allowing multiple devices to communicate using two wires.

**Example:** Use the I2C protocol to connect multiple sensors to the Pico using only two GPIO pins.

#### IDE
Integrated Development Environment; software that provides tools for writing, testing, and debugging code.

**Example:** Thonny is a free IDE designed for Python programming with features like syntax highlighting and autocomplete.

#### If Statement
A conditional programming construct that executes code only when a specified condition is true.

**Example:** The if statement `if counter > 15:` runs the following code only when counter exceeds 15.

#### Import
A command that loads external code libraries or modules into a program.

**Example:** The statement `import config` loads the hardware configuration values from the config.py file.

#### Increment
The operation of increasing a variable's value by one or a specified amount.

**Example:** The statement `counter += 1` increments the counter variable by one on each loop iteration.

#### Index
A number indicating the position of an item in a list or array, starting from zero.

**Example:** Access the first pixel using index 0 with `strip[0] = (255, 0, 0)`.

#### Ingress Protection
A standardized rating system for water and dust resistance using IP codes.

**Example:** An IP67 rating means the LED strip is protected against dust and can be temporarily submerged in water.

#### Integer
A data type for whole numbers without decimal points.

**Example:** The integer value 30 represents the total number of pixels in the LED strip.

#### Interpreter
Software that reads and executes code one line at a time.

**Example:** The MicroPython interpreter running on the Pico translates your Python code into actions the processor can perform.

#### IP20
An ingress protection rating indicating no water resistance.

**Example:** Indoor LED strips are often IP20, suitable only for dry environments.

#### IP65
An ingress protection rating indicating water resistance from spray but not submersion.

**Example:** IP65 LED strips with silicon coating can be used outdoors but should not be submerged.

#### IP67
An ingress protection rating indicating waterproof protection allowing temporary submersion.

**Example:** IP67 LED strips in silicon tubes can be used underwater in fountains or pools.

#### Iteration
A single execution of code within a loop, or the process of repeating.

**Example:** Each iteration of the while loop updates the LED pattern and increments the counter.

#### JST Connector
A standardized 3-pin connector commonly used for LED strips with positive, data, and ground wires.

**Example:** Plug the JST connector from the LED strip into the matching socket on your controller board.

#### Kilohm
A unit of electrical resistance equal to 1,000 ohms.

**Example:** Use a 10 kilohm (10kΩ) potentiometer to adjust brightness or speed by varying resistance.

#### Larson Scanner
An animation pattern where a bright LED sweeps back and forth with a fading tail.

**Example:** The Larson Scanner effect, inspired by the Knight Rider TV show, creates a dramatic sweeping light pattern.

#### LED Noodle
A flexible filament LED designed for wearable projects, typically requiring 3 volts.

**Example:** LED noodles are ideal for Halloween costumes because they are lightweight and flexible.

#### LED Strip
A flexible strip containing multiple LEDs connected in series.

**Example:** A 30-pixel LED strip allows you to create animations by controlling each pixel individually.

#### Library
A collection of pre-written code that provides specific functionality.

**Example:** Import the neopixel library to access functions for controlling addressable LED strips.

#### Linear Charger
A battery charging circuit that regulates voltage using resistive elements, generating heat.

**Example:** A linear charger is simpler but less efficient than a buck converter for charging batteries.

#### Linear Dimmer
A brightness control method that directly scales LED values proportionally.

**Example:** A linear dimmer reduces (255, 0, 0) to (128, 0, 0) by multiplying by 0.5, though this doesn't appear half as bright to human eyes.

#### LiPo Battery
Lithium Polymer rechargeable battery known for high energy density and light weight.

**Example:** A 3.7-volt LiPo battery provides portable power for wearable LED projects.

#### List
Python's data structure for storing ordered collections of values that can be modified.

**Example:** Create a list of colors with `colors = [red, orange, yellow, green, blue]` to cycle through rainbow colors.

#### Local Variable
A variable that exists only within a specific function and cannot be accessed elsewhere.

**Example:** A local variable defined inside the `move_dot()` function is not accessible in other functions.

#### Loop
A programming construct that repeats a section of code multiple times.

**Example:** The main loop `while True:` runs continuously, updating the LED animation until the program is stopped.

#### Markdown
A simple text formatting language using symbols to create headers, lists, and emphasis.

**Example:** Write documentation in Markdown using `####` for headers and `**bold**` for bold text.

#### Maximum Current
The highest electrical current a component can safely handle without damage.

**Example:** The GPIO pins have a maximum current of 16 mA, requiring transistors to control higher current loads.

#### Micro-USB
A small USB connector type commonly used for charging and programming.

**Example:** Connect the Pico to your computer using a micro-USB cable to upload programs and provide power.

#### Microcontroller
A small computer on a single chip designed to control electronic devices.

**Example:** The Raspberry Pi Pico is a microcontroller that runs your Python programs to control LED animations.

#### MicroPython
A version of Python optimized to run on microcontrollers with limited memory and processing power.

**Example:** MicroPython on the Pico lets you write LED control programs in Python instead of C++.

#### Microsecond
A unit of time equal to one-millionth of a second.

**Example:** NeoPixel timing uses microseconds to precisely control the data signals sent to each LED.

#### Millisecond
A unit of time equal to one-thousandth of a second.

**Example:** Set a delay of 50 milliseconds (0.05 seconds) between animation frames for smooth motion.

#### Milliamp
A unit of electrical current equal to one-thousandth of an ampere.

**Example:** Each NeoPixel draws up to 60 milliamps when displaying bright white.

#### Milliamp Hours
A unit of battery capacity indicating total charge storage.

**Example:** A 2000 milliamp hour battery can supply 1000 mA for 2 hours or 200 mA for 10 hours.

#### Milliwatt
A unit of power equal to one-thousandth of a watt.

**Example:** A single LED pixel at full brightness might consume 180 milliwatts of power.

#### MkDocs
A static website generator that creates documentation websites from Markdown files.

**Example:** The Moving Rainbow documentation is built using MkDocs and published to GitHub Pages.

#### Mode
A distinct operating state or pattern in a program, typically switched by user input.

**Example:** Press button 1 to increment the mode variable and switch from rainbow mode to comet tail mode.

#### Module
A file containing Python code that can be imported into other programs.

**Example:** The config module contains hardware pin assignments used by all lesson programs.

#### Modulo Function
A mathematical operation that returns the remainder after division.

**Example:** Use the modulo function `counter % 30` to wrap the counter from 29 back to 0 for continuous animation.

#### Momentary Push Button
A button that makes electrical contact only while being pressed, returning to open when released.

**Example:** Wire a momentary push button between a GPIO pin and ground to create interactive controls.

#### Moving Rainbow
An animation pattern where a rainbow-colored band travels along the LED strip.

**Example:** The moving rainbow effect displays seven rainbow colors that shift position on each loop iteration.

#### NeoPixel
Adafruit's brand name for addressable RGB LED strips using WS2812B chips.

**Example:** Import the neopixel library to control NeoPixel strips with simple Python commands.

#### Normalized Value
A number scaled to fit within the range 0 to 1.

**Example:** Convert a brightness percentage to a normalized value by dividing by 100, so 75% becomes 0.75.

#### NPN Transistor
A type of transistor where a small positive current at the base controls larger current flow from collector to emitter.

**Example:** Use an NPN transistor like the 2N2222 to allow a GPIO pin to switch high-current LED loads.

#### Operator
A symbol representing a mathematical or logical operation.

**Example:** The operator `+` adds numbers, while `*` multiplies them, as in `total = pixels * 60`.

#### Overcurrent Protection
A safety circuit that automatically limits or stops current flow when it exceeds safe levels.

**Example:** USB ports have overcurrent protection that shuts off power if you try to draw more than 500 mA.

#### Overcharge Protection
A safety circuit that prevents battery damage by stopping charging when the battery is full.

**Example:** The TC4056 charger has overcharge protection that stops at 4.2 volts to extend LiPo battery life.

#### Parallel Circuit
An electrical circuit where components are connected across the same voltage with multiple current paths.

**Example:** In a parallel circuit, each LED branch receives the full battery voltage independently.

#### Parameter
A value passed into a function to customize its behavior.

**Example:** The function `move_dot(counter, color, delay)` accepts three parameters: position, color, and timing.

#### Pattern
A repeating design or sequence in an animation.

**Example:** The theater chase pattern creates a marquee effect by turning on every third LED and shifting the pattern.

#### Pattern Recognition
The ability to identify similarities and recurring elements in problems or data.

**Example:** Use pattern recognition to notice that many animations follow the same structure: update pixels, write to strip, delay, repeat.

#### Photo-Sensor
A device that detects the presence or intensity of light.

**Example:** Connect a photo-sensor to an analog pin to make LEDs automatically brighten when room lighting dims.

#### Photoresistor
A component whose electrical resistance changes based on the amount of light hitting it.

**Example:** Use a photoresistor in a voltage divider to create a nightlight that turns on in darkness.

#### PIO
Programmable Input/Output; specialized hardware on the RP2040 for creating custom timing-critical protocols.

**Example:** The NeoPixel library uses PIO state machines to generate precisely-timed data signals.

#### Pixel
An individual controllable LED unit in an addressable LED strip.

**Example:** Set pixel 5 to blue with the command `strip[5] = (0, 0, 255)`.

#### Potentiometer
A variable resistor with an adjustable knob used to control electrical resistance.

**Example:** Connect a 10kΩ potentiometer to an analog pin to create a manual brightness control for your LED strip.

#### Power Consumption
The amount of electrical energy a device uses per unit of time.

**Example:** Calculate power consumption by multiplying voltage (5V) by current (1.8A) to get 9 watts.

#### Power Dissipation
The conversion of electrical energy into heat within a component.

**Example:** A current-limiting resistor has power dissipation calculated by squaring the current and multiplying by resistance.

#### Power Rating
The maximum amount of power a component can safely handle.

**Example:** Check the power rating of resistors to ensure they can handle the expected power dissipation without overheating.

#### Power Supply
A device that provides electrical energy to other components.

**Example:** Connect a 5-volt power supply capable of 2 amps to safely power a 30-pixel LED strip at full brightness.

#### Preamble
The beginning section of a program containing import statements and initial setup code.

**Example:** The preamble of most lessons imports the machine, neopixel, and config modules.

#### Product ID
A number that identifies the specific model or type of a device.

**Example:** The Raspberry Pi Pico has a unique product ID that helps your computer recognize it as a MicroPython device.

#### Pull
The action of downloading the latest changes from a remote repository.

**Example:** Pull updates from the Moving Rainbow repository to get new lessons and bug fixes.

#### Push
The action of uploading your local code changes to a remote repository.

**Example:** After adding a new animation, push your changes to GitHub to share them with others.

#### PWM
Pulse Width Modulation; a technique for controlling power by rapidly switching between on and off states.

**Example:** Use PWM to dim non-addressable LEDs by varying the duty cycle from 0% (off) to 100% (full brightness).

#### Python
A high-level programming language known for readability and ease of learning.

**Example:** MicroPython is a compact version of Python designed to run on microcontrollers.

#### Rainbow Cycle
An animation displaying all rainbow colors across the strip that rotates through the color spectrum.

**Example:** The rainbow cycle function uses the wheel function to assign different colors to each pixel based on position.

#### Range
A sequence of numbers generated for use in loops.

**Example:** The range `range(0, 30)` generates numbers from 0 to 29 for iterating through all pixels.

#### Raspberry Pi Foundation
A British educational charity that creates affordable computing devices for learning.

**Example:** The Raspberry Pi Foundation designed the Raspberry Pi Pico to teach physical computing.

#### Raspberry Pi Pico
A low-cost microcontroller board featuring the RP2040 chip and 26 GPIO pins.

**Example:** The Raspberry Pi Pico costs about $4 and is perfect for learning to control LEDs with MicroPython.

#### Recursive
A programming technique where a function calls itself to solve a problem.

**Example:** A recursive function can count down by calling itself with a decreased value until reaching zero.

#### Refresh Rate
The frequency at which a display updates its content.

**Example:** Update the LED strip at a refresh rate of 20 times per second (50 ms delay) for smooth animations.

#### Repository
A storage location for code and related files, typically on GitHub.

**Example:** Clone the Moving Rainbow repository to access all lesson code and documentation.

#### Resistance
Opposition to electrical current flow through a material, measured in ohms.

**Example:** A 220-ohm resistance limits current flow to safe levels for an LED.

#### Resistor
An electronic component that impedes current flow by a specified resistance.

**Example:** Connect a 220-ohm resistor in series with an LED to prevent excessive current.

#### Return Value
Data sent back from a function after it completes its task.

**Example:** The wheel function's return value is an RGB color tuple based on the input position.

#### Reverse Flow
Electrical current moving in the opposite direction from normal operation.

**Example:** A diode blocks reverse flow, protecting the circuit if battery polarity is accidentally reversed.

#### RGB
Red, Green, Blue; a color model mixing these three primary colors to create any visible color.

**Example:** Set a pixel to purple using RGB values (255, 0, 255) for maximum red and blue with no green.

#### RGB LED
A light-emitting diode containing separate red, green, and blue elements that can mix to produce any color.

**Example:** Each NeoPixel contains an RGB LED and control chip in a single 5mm square package.

#### Rhizomatic Learning
A non-linear educational approach where learners explore connections between topics in a network rather than following a fixed path.

**Example:** The Moving Rainbow project supports rhizomatic learning by allowing students to jump between lessons based on interest.

#### Ripple
An animation pattern creating expanding waves of color, like a stone dropped in water.

**Example:** The ripple effect starts at a center point and expands outward with fading brightness.

#### RP2040
The dual-core ARM Cortex M0+ microcontroller chip designed by Raspberry Pi Foundation.

**Example:** The RP2040 chip inside the Pico runs at 133 MHz and has 264KB of RAM.

#### RP2040-Zero
A compact development board featuring the RP2040 in a smaller form factor with castellated edges.

**Example:** The RP2040-Zero is half the size of a Pico, making it ideal for small wearable projects.

#### Runtime Library
Essential code that must be present for programs to execute properly.

**Example:** The MicroPython runtime library provides fundamental functions like print() and sleep().

#### Saturation
The intensity or purity of a color, from gray (low saturation) to vivid (high saturation).

**Example:** Pure red (255, 0, 0) has maximum saturation, while pink (255, 128, 128) has lower saturation.

#### Schematic
A diagram showing electrical connections using standardized symbols for components.

**Example:** Refer to the schematic to see which GPIO pin connects to the LED strip data line.

#### Scope
The region of code where a variable can be accessed.

**Example:** A variable defined inside a function has local scope and cannot be used outside that function.

#### Screw Headers
Terminal blocks with screws for securing wires without soldering.

**Example:** Use screw headers to make removable connections between the Pico and LED strip wires.

#### Serial Console
A text-based communication interface for interacting with a microcontroller.

**Example:** View print statement output in the serial console at the bottom of Thonny.

#### Serial Data
Information transmitted one bit at a time over a single wire.

**Example:** NeoPixels receive serial data containing color information at 800,000 bits per second.

#### Series Circuit
An electrical circuit where components are connected end-to-end in a single path.

**Example:** In a series circuit, current must flow through each component sequentially.

#### Short Circuit
An unintended connection creating a very low resistance path for current.

**Example:** Prevent short circuits by ensuring positive and negative wires never touch directly.

#### Signal Processing
The analysis and manipulation of electrical signals carrying information.

**Example:** The WS2812B chip performs signal processing to decode color data from the timing of voltage pulses.

#### Sleep
A function that pauses program execution for a specified duration.

**Example:** The command `sleep(0.1)` pauses for one-tenth of a second between animation frames.

#### Solar Panel
A device that converts light energy into electrical energy.

**Example:** Connect a 6-volt solar panel to a battery charger circuit to create a self-powered nightlight.

#### Solderless Breadboard
Another term for breadboard, emphasizing that no soldering is required.

**Example:** Build prototype circuits quickly on a solderless breadboard before creating a permanent version.

#### SPI
Serial Peripheral Interface; a synchronous communication protocol using separate clock and data lines.

**Example:** Some LED matrices use the SPI protocol for faster data transmission than basic serial.

#### Spectrum
The range of all possible colors in order of wavelength.

**Example:** The rainbow displays the visible spectrum from red through violet.

#### SRAM
Static Random-Access Memory; fast temporary storage that retains data while powered.

**Example:** The RP2040 has 264KB of SRAM for storing variables while programs run.

#### State Machine
A programmable logic system that changes outputs based on inputs and current state.

**Example:** The PIO state machines in the RP2040 generate precise NeoPixel timing signals.

#### String
A data type representing text as a sequence of characters.

**Example:** Use a string like `"rainbow mode"` to display the current animation name.

#### Strip
The variable name commonly used to represent a NeoPixel LED strip object.

**Example:** Initialize the strip with `strip = NeoPixel(Pin(0), 30)` to create a 30-pixel strip on GPIO pin 0.

#### Sushi Cards
Bite-sized educational cards teaching single concepts, named after the CoderDojo project.

**Example:** Create sushi cards for each lesson showing the key concept and code snippet.

#### Syntax
The grammar rules that define how code must be written for a programming language.

**Example:** Python syntax requires consistent indentation and colons after if statements.

#### Syntax Highlighting
Automatic color-coding of different parts of code to improve readability.

**Example:** Thonny's syntax highlighting shows keywords in orange, strings in green, and comments in gray.

#### Tactile Switch
Another term for a momentary push button with tactile feedback when pressed.

**Example:** Wire tactile switches to GPIO pins 14 and 15 for interactive mode control.

#### Temperature Sensor
A device that measures heat and converts it to an electrical signal.

**Example:** The RP2040 includes a built-in temperature sensor you can read to monitor chip temperature.

#### Theater Chase
An animation pattern resembling marquee lights, with groups of LEDs moving along the strip.

**Example:** The theater chase function lights every third pixel and shifts the pattern to create a chasing effect.

#### Thermal Feedback
Automatic adjustment of operation based on temperature measurements.

**Example:** Battery chargers use thermal feedback to reduce charging current if the chip gets too hot.

#### Thonny
A free Python IDE designed for beginners with simple interface and built-in debugging tools.

**Example:** Use Thonny to write MicroPython programs and upload them to the Pico.

#### Tie Points
The individual connection holes in a breadboard that are electrically connected in groups.

**Example:** A half-size breadboard typically has 400 tie points arranged in rows of 5 connected holes.

#### Transistor
A semiconductor component that acts as an electronic switch or amplifier.

**Example:** Use a transistor to let a low-current GPIO pin control high-current LED noodles.

#### Trickle Charge
A very small charging current used to maintain a battery without overcharging.

**Example:** After a battery is full, the charger switches to trickle charge mode to keep it topped off.

#### Tuple
An ordered, immutable collection of values in Python.

**Example:** RGB colors are stored as tuples like `(255, 0, 0)` where the values cannot be changed individually.

#### Twinkle
An animation pattern with random pixels blinking on and off to simulate stars.

**Example:** The twinkle effect randomly selects pixels and sets them to white before fading them out.

#### UART
Universal Asynchronous Receiver-Transmitter; a protocol for serial communication between devices.

**Example:** The Pico uses UART protocol to send print statement output to your computer via USB.

#### UF2 Format
USB Flashing Format; a file type for programming microcontrollers by copying to a USB drive.

**Example:** Download the MicroPython UF2 file and drag it to the RPI-RP2 drive to program the Pico.

#### USB Connector
A standardized plug for connecting devices, providing both power and data communication.

**Example:** Plug a USB connector into your computer to program the Pico and power the LED strip.

#### USB Device
Any hardware that connects to a computer through a USB port.

**Example:** The Pico appears as a USB device when connected, allowing file transfer and serial communication.

#### USB Hub
A device that expands one USB port into multiple ports.

**Example:** Use an externally powered USB hub to connect multiple LED projects without overloading your computer's USB ports.

#### USB Power Pack
A portable battery with USB output for charging devices.

**Example:** A 10,000 mAh USB power pack can run a 30-pixel LED strip for several hours.

#### USB-C
The newest reversible USB connector type supporting higher power and data rates.

**Example:** Some newer development boards use USB-C instead of micro-USB for more reliable connections.

#### Variable
A named storage location in a program that holds a value which can change.

**Example:** Create a variable `counter = 0` to keep track of the current pixel position in an animation.

#### Vendor ID
A unique number assigned to each manufacturer of USB devices.

**Example:** All Raspberry Pi products share the same vendor ID, helping computers recognize them.

#### Voltage
The electrical potential difference between two points, measured in volts.

**Example:** The Pico operates at 3.3 volts for logic signals while most LED strips require 5 volts.

#### Voltage Regulator
A circuit that maintains constant output voltage despite changes in input voltage or current draw.

**Example:** A voltage regulator converts 5V from USB down to 3.3V for the Pico's processor.

#### Watt
A unit of electrical power equal to one joule per second.

**Example:** A 30-pixel LED strip at full brightness consumes approximately 1.8 watts of power.

#### Waterproofing
Protection that prevents water from entering or damaging electronics.

**Example:** Choose waterproofing level based on use: IP20 for indoors, IP65 for outdoor, IP67 for underwater.

#### Wheel Function
A function that converts a number from 0-255 into an RGB color, cycling through the spectrum.

**Example:** Call `wheel(128)` to get a cyan color halfway through the color wheel.

#### While Loop
A loop that continues executing as long as a specified condition remains true.

**Example:** The main animation loop `while True:` runs forever because the condition True never becomes false.

#### Wiring Diagram
A simplified drawing showing physical connections between components.

**Example:** Follow the wiring diagram to connect the LED strip's red wire to 5V, black to ground, and green to GPIO pin 0.

#### Write
The command that sends color data from the program to the physical LED strip.

**Example:** After setting pixel colors, call `strip.write()` to make the changes visible on the strip.

#### WS2812B
The specific integrated circuit chip standard used in addressable RGB LEDs.

WS2812B are also known as [NeoPixels](#neopixel).

**Example:** WS2812B chips contain an RGB LED and control circuitry in a single 5mm package, allowing individual addressing of each pixel.
