# Tilt-a-Rainbow Mini Kit

The little sibling of the [Tilt-a-Rainbow Kit](../16x16-matrix-accel/README.md). It has the same Pico,
sensor, buttons and pins, with an 8x8 matrix in place of the 16x16 one.

This kit contains:

- A Raspberry Pi Pico
- An 8x8 NeoPixel matrix (64 WS2812B pixels) with data on GPIO 0
- A LIS3DH accelerometer on I2C bus 0 (SDA on GPIO 16, SCL on GPIO 17)
- Two mode buttons, each wired from a GPIO pin to GND: GPIO 14 and GPIO 15

All pins are set in `config.py`. Save it on the Pico along with the programs.

## Programs

Run these in order the first time you wire up the kit.

| File | What it does |
|------|--------------|
| `01-blink-onboard-led.py` | The Pico runs MicroPython (blinks the LED on the Pico board) |
| `02-probe.py` | Detailed probe: board info, button and I2C pin levels, bus scan, LIS3DH WHO_AM_I and readings, ending in TEST PASS or TEST FAIL |
| `03-button-test.py` | Both mode buttons read correctly |
| `04-first-pixel.py` | Data wire works and the color order is red, green, blue |
| `05-fill-colors.py` | All 64 pixels light, and the power supply holds up |
| `06-walk-pixels.py` | Pixel order along the strip (zig-zag or straight rows) |
| `07-xy-corners.py` | The `xy()` column and row mapping puts corners where expected |
| `08-row-column-sweep.py` | Rows and columns sweep as straight lines |
| `09-smiley-face.py` | **Drawing:** a smiley face made from 8 lines of letters and a color key |
| `10-picture-show.py` | **Drawing:** the eight pictures in `pictures.py`. Button 1 is next, button 2 is back |
| `11-winking-face.py` | **Drawing:** an animation made of frames: the smiley blinks and winks |
| `12-scrolling-message.py` | **Drawing:** a message scrolls across the matrix, using the letters in `font.py` |
| `13-accel-print.py` | The accelerometer reads sensible x, y and z values |
| `14-accel-bubble.py` | A dot on the matrix slides as you tilt the kit |
| `15-sloshing-water.py` | A half-full pan of blue water that sloshes as you rock the board |
| `16-tilt-a-maze.py` | A nine-level tilt maze: roll the red ball to the green hole, then a rainbow |
| `17-tilt-a-sketch.py` | **Drawing:** draw your own picture by tilting. Button 1 changes the color, button 2 lifts the pen, a shake erases |
| `18-modes.py` | Twelve light shows in one program. Button 1 (GPIO 14) is the next mode, button 2 (GPIO 15) the previous mode |
| `19-template-main.py` | **Demo mode:** every show and game from programs 05 to 18 in one program, switched with the same two buttons. Save a copy as `main.py` and the kit starts it at power-up |

Programs 01 to 08, 13 to 16 and 18 are the thirteen programs of the 16x16 kit, resized for 64 pixels.
Programs 09 to 12 and 17 are new for this kit: they are the drawing programs. Program 19 is new too.

To run the probe from your computer after uploading, use `./run-probe.sh`.

## Watching for a Hang

Programs 13 to 19 blink the LED on the Pico board while they run. If it stops blinking, the
program has stopped; look in the Thonny Shell for an error.

The accelerometer code never stops the program on a bad reading. If a reading fails, it keeps
the last good one and turns the sensor on again. Once a second it also restarts the sensor if
readings come back exactly the same every time (stuck) or the sensor has lost its settings (a
power dip resets it to sleep). Setting up the sensor frees the I2C bus with nine clock pulses
first, in case the sensor was left holding SDA low. The I2C clock is 100 kHz instead of
400 kHz, which is less bothered by noise from the matrix wires. Programs 18 and 19 also catch
any other error in a mode, print it, and start that mode again.

## Differences from the 16x16 kit

| Setting | 16x16 kit | This kit | Why |
|---------|-----------|----------|-----|
| `MATRIX_WIDTH`, `MATRIX_HEIGHT` | 16 | 8 | The panel |
| `LEVEL` | 8 | 20 | A quarter of the pixels, so each one can be brighter (white fill is about 300 mA) |
| Text on the matrix | 3x5 letters drawn double size | 3x5 letters drawn at normal size | "L1" and "12" are 7 pixels wide, which fits in 8 |
| Maze | 8x8 cells, routes of 28 to 100 steps | 4x4 cells, routes of 12 to 28 steps | The maze needs a wall pixel between cells |
| Mode speeds | faster | slower, with fewer raindrops and rings | The same speed looks twice as fast on a panel half as wide |
| `BALL_SIZE` in `tilt_balls.py` | 1.05 | 1.25 | Stops two balls landing on one pixel in a crowded 8x8 |
| Modes | 10 | 12 | Adds the picture show and the scrolling message |

## Program 18: Modes

Press button 1 for the next mode and button 2 for the previous one. The matrix shows the
mode number for a moment, then the mode starts.

| Mode | Show | Uses the tilt? |
|------|------|----------------|
| 1 | Three slow bouncing dots (red, green, blue) | no |
| 2 | Seven faster bouncing dots, one per rainbow color | no |
| 3 | Twelve colors that leave small trails | no |
| 4 | Rainbow rain | no |
| 5 | Ripple rings | no |
| 6 | Picture show: the eight gallery pictures slide past | no |
| 7 | Scrolling message in rainbow letters | no |
| 8 | One blue dot that rolls as you tilt | yes |
| 9 | Three dots (red, green, blue) that roll and bounce off each other | yes |
| 10 | Seven rainbow dots that roll and bounce off each other | yes |
| 11 | Sloshing water (program 15) | yes |
| 12 | Tilt-a-maze (program 16) | yes |

Each mode is a separate module that program 18 loads only when you switch to it, using
`__import__`, and throws away when you leave it. The Pico never holds more than one mode in
memory. To add a mode, write a module with a `run(settings)` function and add a line to `MODES`
in `18-modes.py`.

## Program 19: Demo Mode

Program 19 is for showing the kit off. It works like program 18, with the same buttons, but it
steps through every show and game from programs 05 to 18:

| Mode | Show | From program | Uses the tilt? |
|------|------|--------------|----------------|
| 1 | Fill colors: red, green, blue and white | 05 | no |
| 2 | Walk the pixels | 06 | no |
| 3 | Row and column sweep | 08 | no |
| 4 | Winking face | 09 and 11 | no |
| 5 | Picture show | 10 | no |
| 6 | Scrolling message in rainbow letters | 12 | no |
| 7 | Three slow bouncing dots | 18 | no |
| 8 | Seven faster bouncing dots | 18 | no |
| 9 | Twelve colors that leave small trails | 18 | no |
| 10 | Rainbow rain | 18 | no |
| 11 | Ripple rings | 18 | no |
| 12 | Accelerometer bubble | 14 | yes |
| 13 | One dot that rolls as you tilt | 18 | yes |
| 14 | Three dots that roll and bounce off each other | 18 | yes |
| 15 | Seven rainbow dots that roll and bounce off each other | 18 | yes |
| 16 | Sloshing water | 15 | yes |
| 17 | Tilt-a-maze | 16 | yes |
| 18 | Tilt-a-sketch: tilt to draw, shake to erase | 17 | yes |

It leaves out programs 01 to 04 and 07, which are wiring checks, and 13, which only prints numbers.

Programs 05 to 14 set up their own hardware and sleep with `sleep()`, which cannot notice a
button press. They stay that way, so each one still reads from top to bottom on its own. For
program 19, the ones it shows have a **demo version**: a module that does the same thing with
`kit.py`, and sleeps with `kit.wait()`, so a press of a mode button stops it.

In program 19 the buttons change modes, so the sketch in mode 18 cannot use them. It changes the
pen color by itself with every step (the `auto_color` setting), and a shake still erases.

The file is a template for `main.py`. The Pico runs a file named `main.py` by itself whenever it
powers up, so save a copy of `19-template-main.py` on the Pico as `main.py` and the kit starts
the demo with no computer attached. The Stop button in Thonny still stops it.

Power it from a USB wall charger. Many power banks switch themselves off when the current draw is
low, and with only a few dim pixels lit (modes like Walk the pixels or Tilt one dot) this kit draws
very little. The bank then cuts the power after a short time and the demo goes dark. Some power
banks have a low-current mode for earbuds and watches that keeps them on.

A printable one-page guide to all 18 modes is
`docs/kits/8x8-matrix-accel/demo-mode-guide.pdf` (and `.html`), and the student page is
`docs/kits/8x8-matrix-accel/19-template-main.md`. To rebuild the guide after a mode changes, run
`scripts/demo-mode-guide/build.sh`. It runs the real mode modules on your computer with stand-ins
for the hardware, draws each mode, and renders the PDF with Google Chrome.

## Modules

| Module | Program 18 modes | Program 19 modes | Also used by |
|--------|------------------|------------------|--------------|
| `kit.py` | all | all | programs 15 to 17: the matrix, accelerometer, buttons, colors and helpers |
| `font.py` | 7 | 6 | program 12, and `kit.py` for the mode numbers: the letter shapes |
| `pictures.py` | 6 | 5 | program 10: the picture gallery |
| `fill_colors.py` | - | 1 | - (the demo version of program 05) |
| `walk_pixels.py` | - | 2 | - (the demo version of program 06) |
| `row_column_sweep.py` | - | 3 | - (the demo version of program 08) |
| `winking_face.py` | - | 4 | - (the demo version of programs 09 and 11) |
| `picture_show.py` | 6 | 5 | - |
| `scroll_text.py` | 7 | 6 | - |
| `bounce_dots.py` | 1, 2 and 3 | 7, 8 and 9 | - |
| `rain.py` | 4 | 10 | - |
| `rings.py` | 5 | 11 | - |
| `accel_bubble.py` | - | 12 | - (the demo version of program 14) |
| `tilt_balls.py` | 8, 9 and 10 | 13, 14 and 15 | - |
| `sloshing_water.py` | 11 | 16 | program 15 |
| `tilt_a_maze.py` | 12 | 17 | program 16 |
| `tilt_a_sketch.py` | - | 18 | program 17 |

Programs 15, 16 and 17 are short wrappers around their modules, so run `./upload-code.sh` to put
all the `.py` files on the Pico before you run them.

## Power

All 64 pixels at full white would draw about 3.8 amps, far beyond the half amp that USB can supply.
`LEVEL` in `config.py` sets the color numbers for programs that light the whole panel. The pictures
use small color numbers too: the brightest picture draws about 220 mA.

## Uploading

```bash
./upload-code.sh
```

It uploads 37 files: every `.py` file here except `circuit-diagram.py`, which draws the wiring
picture on your computer.

## What has been tested

Tested on 2026-10-08 on a real kit (Raspberry Pi Pico, MicroPython 1.29.0).

| Check | Result |
|-------|--------|
| Pixel layout | A person looked at a test pattern: pixel 8 is right below pixel 0, so `SERPENTINE = False`, and red, green and blue are in the right order |
| Tilt direction | A person tipped the kit four ways and a bar lit on the low edge each time, so `FLIP_X = False`, `FLIP_Y = True`, `SWAP_XY = False` |
| `02-probe.py` | `TEST PASS` (LIS3DH at 0x19, WHO_AM_I 0x33, 1.01 g lying flat) |
| Programs 01 to 18 | Each one ran on the Pico with no errors, and the colors it sent to the matrix were read back and matched (for example, the smiley face and the level 1 maze) |
| All 12 modes | Loaded and unloaded twice in a row on the Pico. Free memory stayed near 211,000 bytes and the shows ran at 24 to 43 frames a second |
| Maze levels 1 to 9 | Played through on a computer by a script that tilts toward the hole: 12, 12, 16, 16, 20, 20, 24, 24 and 28 moves |
| All 18 modes of program 19 | Tested on 2026-10-22 on the same kit. A test script pressed the mode buttons in software: every mode loaded, drew on the matrix and unloaded, twice in a row, and button 2 on mode 1 went back to mode 18. Free memory when a mode loaded stayed between 197,000 and 209,000 bytes on both rounds |
| A sensor that stops answering | Once, a real run of program 19 stopped in mode 12 with `OSError: [Errno 5] EIO`: the sensor missed one reading. Right after, 485 reads in 5 seconds worked, and 1,411 more with the whole matrix flashing, so a sensor wire probably lost contact for a moment. `kit.read_tilt()` now keeps the last good reading, says so once in the Shell, and sets the sensor up again when it answers. A test script made the bus fail 20 times in a row to check this |
| `tilt_a_sketch.py` | A test script gave it a pretend tilt to the right. On its own (program 17) the pen drew a red line; with `auto_color` (program 19) the line came out red, orange, yellow, green |

Program 19 was tried by hand on 2026-10-22: a person stepped through the modes with the buttons, then
saved it as `main.py` and watched the demo start by itself from a USB charger.

Not yet tried by hand: nobody has pressed the buttons or tilted the kit while programs 03, 10 and 14 to 18
were running, and nobody has looked at each picture on the real matrix. Those programs say so in their headers.
