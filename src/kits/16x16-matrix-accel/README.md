# 16x16 Matrix Accelerometer Kit

This kit contains:

- A Raspberry Pi Pico
- A 16x16 NeoPixel matrix (256 WS2812B pixels) with data on GPIO 0
- An accelerometer on I2C bus 0 (SDA on GPIO 16, SCL on GPIO 17)
- Two mode buttons, each wired from a GPIO pin to GND: GPIO 14 and GPIO 15

All pins are set in `config.py`. Save it on the Pico along with the programs.

## Hardware Test Programs

Run these in order the first time you wire up the kit.

| File | What it checks |
|------|----------------|
| `01-blink-onboard-led.py` | The Pico runs MicroPython (blinks the LED on the Pico board) |
| `02-probe.py` | Detailed probe: board info, button and I2C pin levels, bus scan, LIS3DH WHO_AM_I and readings, ending in TEST PASS or TEST FAIL |
| `03-button-test.py` | Both mode buttons read correctly |
| `04-first-pixel.py` | Data wire works and the color order is red, green, blue |
| `05-fill-colors.py` | All 256 pixels light, and the power supply holds up |
| `06-walk-pixels.py` | Pixel order along the strip (zig-zag or straight rows) |
| `07-xy-corners.py` | The `xy()` column and row mapping puts corners where expected |
| `08-row-column-sweep.py` | Rows and columns sweep as straight lines |
| `09-accel-print.py` | The accelerometer reads sensible x, y and z values |
| `10-accel-bubble.py` | A dot on the matrix slides as you tilt the kit |
| `11-sloshing-water.py` | A half-full pan of blue water that sloshes as you rock the board |
| `12-tilt-a-maze.py` | A nine-level tilt maze: roll the red ball to the green hole, then a rainbow |
| `13-modes.py` | Ten light shows in one program. Button 1 (GPIO 14) is the next mode, button 2 (GPIO 15) the previous mode |

To run the probe from your computer after uploading, use `./run-probe.sh`.

## Program 13: Modes

Press button 1 for the next mode and button 2 for the previous one. The matrix shows the
mode number for a moment, then the mode starts.

| Mode | Show | Uses the tilt? |
|------|------|----------------|
| 1 | Three slow bouncing dots (red, green, blue) | no |
| 2 | Seven faster bouncing dots, one per rainbow color | no |
| 3 | Twelve colors that leave small trails | no |
| 4 | Rainbow rain | no |
| 5 | Ripple rings | no |
| 6 | One blue dot that rolls as you tilt | yes |
| 7 | Three dots (red, green, blue) that roll and bounce off each other | yes |
| 8 | Seven rainbow dots that roll and bounce off each other | yes |
| 9 | Sloshing water (program 11) | yes |
| 10 | Tilt-a-maze (program 12) | yes |

Each mode is a separate module that program 13 loads only when you switch to it, using
`__import__`, and throws away when you leave it. The Pico never holds more than one mode in
memory. To add a mode, write a module with a `run(settings)` function and add a line to `MODES`
in `13-modes.py`.

| Module | Used by |
|--------|---------|
| `kit.py` | everything: the matrix, accelerometer, buttons, colors and helpers |
| `bounce_dots.py` | modes 1, 2 and 3 |
| `rain.py` | mode 4 |
| `rings.py` | mode 5 |
| `tilt_balls.py` | modes 6, 7 and 8 |
| `sloshing_water.py` | mode 9, and program 11 |
| `tilt_a_maze.py` | mode 10, and program 12 |

Programs 11 and 12 are short wrappers around their modules, so run `./upload-code.sh` to put
all the `.py` files on the Pico before you run them.

## Power

All 256 pixels at full white would draw more than 15 amps, far beyond what USB can supply.
`LEVEL` in `config.py` caps the color numbers for programs that light the whole panel.

## Uploading

```bash
./upload-code.sh
```

The programs have not yet been run on real hardware. The accelerometer is a LIS3DH at address 0x19
(confirmed by `02-probe.py`).
