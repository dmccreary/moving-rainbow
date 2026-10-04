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

To run the probe from your computer after uploading, use `./run-probe.sh`.

## Power

All 256 pixels at full white would draw more than 15 amps, far beyond what USB can supply.
`LEVEL` in `config.py` caps the color numbers for programs that light the whole panel.

## Uploading

```bash
./upload-code.sh
```

The programs have not yet been run on real hardware. The accelerometer is a LIS3DH at address 0x19
(confirmed by `02-probe.py`).
