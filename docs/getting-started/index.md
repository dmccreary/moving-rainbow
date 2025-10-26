# Getting Started with Moving Rainbow

Welcome to the Moving Rainbow project! This section will guide you through everything you need to 
know to start creating colorful LED animations with programmable microcontrollers.

## What is Moving Rainbow?

Moving Rainbow is an educational system designed to teach computational thinking and 
Python programming using colorful LED strips and low-cost microcontrollers. 
The project emphasizes hands-on learning with bright, engaging visuals that students love to create and share.

**Why Moving Rainbow?**

1. **Colorful & Fun** - Kids love working with bright, moving LED patterns
2. **Easy to Start** - Simple USB connection and beginner-friendly Python programming
3. **Affordable** - Complete kits cost under $10
4. **Take-Home Projects** - Students can build wearables and decorations to show friends and family
5. **Proven Results** - Refined through years of classroom testing and student feedback

## Quick Start Path

Follow these guides in order to get up and running:

### 1. [About Moving Rainbow](about.md)
Learn about the project's background, educational philosophy, and why we use LED strips to teach programming. Discover how this curriculum evolved from Arduino to MicroPython and the principles that make it effective for students.

**What You'll Learn:**
- History and evolution of the project
- Why color and motion are powerful learning tools
- Licensing and how to contribute

### 2. [Standard Kits](kits.md)
Explore the pre-configured kits designed for classroom use. These kits include everything you need to get started with minimal setup time.

**What's Included:**
- Raspberry Pi Pico microcontroller ($4-6)
- 1/2-size breadboard with 400 tie points
- 30-LED addressable RGB strip (WS2812B)
- Two momentary push buttons
- Screw terminal headers (optional)
- Jumper wires

**Kit Variations:**
- LED fairy lights for costumes
- NeoPixel rings and matrices
- Waterproof options (IP65, IP67)

### 3. [Purchasing Your Own Parts](parts.md)
If you want to build your own kit at home, this guide shows you where to buy parts online and what to look for.

**Topics Covered:**
- Finding WS2812B LED strips on eBay and Amazon
- Understanding waterproofing ratings (IP20, IP65, IP67)
- Cost comparison and buying tips
- Recommended sellers and specifications

**Waterproofing Guide:**
- **IP20** - Indoor classroom use ($3/meter)
- **IP65** - Silicon coating for costumes and outdoor use
- **IP67** - PVC tube for underwater applications

### 4. [Development Boards](dev-boards.md)
Learn about the microcontrollers compatible with Moving Rainbow lessons, including detailed pinout diagrams.

**Supported Boards:**
- **Raspberry Pi Pico** - Standard $4 board with 26 GPIO pins
- **Raspberry Pi Pico W** - $6 version with WiFi capability
- **RP2040-Zero** - Compact version with USB-C connector
- Detailed pinout diagrams for all boards

**Key Features:**
- Dual-core ARM Cortex M0+ processor @ 133 MHz
- 264KB SRAM, 2MB flash memory
- Drag-and-drop programming via USB
- Temperature sensor and multiple I/O options

### 5. [Desktop Setup](desktop-setup.md)
Set up the free Thonny IDE on your computer (Windows, Mac, or Linux) and configure it for MicroPython development.

**Installation Steps:**
1. Download and install Thonny
2. Configure MicroPython firmware on your Pico
3. Verify interpreter settings
4. Test your first program

**What You'll Install:**
- Thonny Python IDE (free, open-source)
- MicroPython firmware for Raspberry Pi Pico
- USB drivers (automatic on most systems)

### 6. [Updating Firmware](updating-firmware.md)
Learn how to update the MicroPython firmware on your Raspberry Pi Pico when new versions are released.

**Quick Process:**
1. Download latest firmware from micropython.org
2. Hold BOOTSEL button while connecting USB
3. Drag firmware file to RPI-RP2 drive
4. Wait 10 seconds - done!

**When to Update:**
- Getting started with a new Pico
- New features are released
- Bug fixes are available
- Compatibility issues arise

### 7. [Electrical Connections](connections.md)
Understand the simple three-wire hookup for LED strips and how to connect components to your breadboard.

**Basic Connections:**
- **GND (Black)** - Ground/negative wire to Pico GND pin
- **+5V (Red)** - Power wire to Pico VBUS pin
- **Data (Yellow/Green)** - Signal wire to GPIO pin 0

**Breadboard Layout:**
- Pico placement in center
- Button connections on GPIO pins 14 and 15
- LED strip screw terminal connections

### 8. [Batteries](batteries.md)
Choose the right battery for portable LED projects, from small coin cells to large USB power packs.

**Battery Options:**
- **Coin Cells** - Tiny projects (200-250 mAh)
- **AA Batteries** - Beginner-friendly (2000-3000 mAh)
- **USB Power Packs** - Best for most projects (2000-20000 mAh)
- **LiPo Batteries** - Professional wearables (500-2000 mAh, requires care)
- **18650 Cells** - High-power applications (2000-3500 mAh)

**Safety Levels:**
- ✅ **Safe for Kids:** Coin cells, AA/AAA, USB power packs, 9V
- ⚠️ **Adult Supervision:** LiPo batteries, 18650 cells

### 9. [GitHub Summary](github-summary.md)
Learn the six essential Git commands needed to download lesson code and optionally contribute improvements back to the project.

**Essential Commands:**
- `git clone` - Download the repository
- `git pull` - Get latest updates
- `git add` - Stage your changes
- `git commit` - Save changes with description
- `git push` - Upload to GitHub
- `git status` - Check current state

**What You Can Access:**
- All lesson code and examples
- Documentation source files
- MicroSim interactive tools
- Kit assembly instructions

## What's Next?

After completing this Getting Started section, you'll be ready to:

1. **Start the [Lessons](../lessons/index.md)** - Begin with simple blink patterns and progress to complex animations
2. **Explore [Kits](../kits/index.md)** - Build specialized projects like nightlights and holiday decorations
3. **Try [MicroSims](../sims/index.md)** - Use interactive web tools to understand concepts
4. **Review the [Teachers Guide](../teachers-guide/index.md)** - Learn pedagogical approaches for teaching with Moving Rainbow

## Getting Help

If you have questions:

- Check the [Glossary](../glossary.md) for term definitions
- Review the [Resources](../resources.md) page for additional learning materials
- Contact Dan McCreary via [LinkedIn](https://www.linkedin.com/in/danmccreary/)
- Report issues on the [GitHub repository](https://github.com/dmccreary/moving-rainbow)

## License

All Moving Rainbow curricula are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/). You're free to use and modify materials for educational purposes, as long as you don't resell them for profit.

---

Ready to begin? Start with [About Moving Rainbow](about.md) to learn the story behind the project, or jump straight to [Standard Kits](kits.md) if you're ready to see what you need!
