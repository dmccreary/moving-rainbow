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

Programs 01 to 08, 13 to 16 and 18 are the thirteen programs of the 16x16 kit, resized for 64 pixels.
Programs 09 to 12 and 17 are new for this kit: they are the drawing programs.

To run the probe from your computer after uploading, use `./run-probe.sh`.

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

| Module | Used by |
|--------|---------|
| `kit.py` | programs 15 to 18: the matrix, accelerometer, buttons, colors and helpers |
| `font.py` | the letter shapes: program 12, `kit.py` and mode 7 |
| `pictures.py` | the picture gallery: program 10 and mode 6 |
| `bounce_dots.py` | modes 1, 2 and 3 |
| `rain.py` | mode 4 |
| `rings.py` | mode 5 |
| `picture_show.py` | mode 6 |
| `scroll_text.py` | mode 7 |
| `tilt_balls.py` | modes 8, 9 and 10 |
| `sloshing_water.py` | mode 11, and program 15 |
| `tilt_a_maze.py` | mode 12, and program 16 |

Programs 15 and 16 are short wrappers around their modules, so run `./upload-code.sh` to put
all the `.py` files on the Pico before you run them.

## Power

All 64 pixels at full white would draw about 3.8 amps, far beyond the half amp that USB can supply.
`LEVEL` in `config.py` sets the color numbers for programs that light the whole panel. The pictures
use small color numbers too: the brightest picture draws about 220 mA.

## Uploading

```bash
./upload-code.sh
```

It uploads 30 files: every `.py` file here except `circuit-diagram.py`, which draws the wiring
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

Not yet tried by hand: nobody has pressed the buttons or tilted the kit while programs 03, 10 and 14 to 18
were running, and nobody has looked at each picture on the real matrix. Those programs say so in their headers.
