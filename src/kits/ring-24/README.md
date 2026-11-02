# Ring 24 Kit

The Moving Rainbow base kit with a circle of lights in place of the strip. A ring has no ends, so
the labs here focus on patterns that only work well on a circle: orbits, clocks, spinners, waves
that join up with themselves and games that go round and round.

This kit contains:

- A Raspberry Pi Pico
- A 24-pixel NeoPixel ring (WS2812B) with data on GPIO 0
- Two buttons, each wired from a GPIO pin to GND: Button 1 on GPIO 15 and Button 2 on GPIO 14

All pins are set in `config.py`. Save it on the Pico along with the programs.

The student lesson and one page per lab are at `docs/kits/ring-24/` on the
[Moving Rainbow site](https://dmccreary.github.io/moving-rainbow/kits/ring-24/).

## Wiring Diagram

`circuit-diagram.py` draws `docs/kits/ring-24/img/circuit-diagram.png` and `.svg` with schemdraw.
It runs on a computer, not on the Pico, so `upload-code.sh` skips it. Run it again after any pin change:

```bash
python3 circuit-diagram.py
```

## Where the Pixels Are

The pixel numbers run clockwise. Pixel 0 sits at about 1:30 on a clock dial, so 12 o'clock is
pixel 21. That number is `TOP_PIXEL` in `config.py`.

Patterns that care where "up" is use a small function to count clockwise from the top:

```python
def pixel_at(position):
    return (TOP_PIXEL + position) % NUMBER_PIXELS
```

Position 0 is 12 o'clock, 6 is 3 o'clock, 12 is 6 o'clock and 18 is 9 o'clock. If you mount the ring
a different way, run `03-clock-positions.py` and change `TOP_PIXEL` until red is at the top.

## Programs

Run these in order the first time you wire up the kit.

| File | What it does |
|------|--------------|
| `01-blink-onboard-led.py` | **First steps:** the Pico runs MicroPython (blinks the LED on the Pico board) |
| `02-first-pixel.py` | Pixel 0 blinks red and pixel 1 stays green, which shows where the numbers start and which way they go |
| `03-clock-positions.py` | Marks 12, 3, 6 and 9 o'clock, and introduces `pixel_at()` |
| `04-button-test.py` | Each button lights half of the ring |
| `05-spin-dot.py` | **Going around:** one dot circles the ring, and `%` wraps it from pixel 23 to pixel 0 |
| `06-comet.py` | A comet with a fading tail that changes color each lap |
| `07-two-comets.py` | Two comets, always on opposite sides of the ring |
| `08-meet-and-flash.py` | Two dots go opposite ways, and the ring flashes when they meet |
| `09-color-wheel.py` | **Color:** a real color wheel, where each color depends on the angle |
| `10-spinning-rainbow.py` | The color wheel spins |
| `11-pinwheel.py` | Colored blades spin, and the number of blades changes (each blade comes with a gap, and 4, 6, 8, 12 and 24 blade-and-gap parts all divide evenly into 24) |
| `12-loading-spinner.py` | The busy spinner from a phone: an arc that grows and shrinks |
| `13-breathing-halo.py` | The whole ring breathes, with a new color at its darkest point |
| `14-sine-wave.py` | **Math and motion:** waves of light roll around and join up with themselves |
| `15-ripple.py` | Ripples spread both ways and crash together on the far side |
| `16-radar.py` | A beam sweeps the ring, and drifting targets glow when it passes them |
| `17-planets.py` | Four planets orbit at different speeds, gliding smoothly between pixels |
| `18-pendulum.py` | A ball swings along the bottom of the ring and slowly stops |
| `19-water-level.py` | Water climbs both sides of the ring at once and drains away |
| `20-ring-of-fire.py` | Flames that spread heat to the pixels on each side |
| `21-ring-automaton.py` | A cellular automaton with no edges, such as Rule 30 |
| `22-button-dial.py` | **Buttons:** Button 1 turns a dot clockwise and Button 2 turns it counter-clockwise |
| `23-speed-and-direction.py` | Button 1 changes the speed and Button 2 reverses a rainbow comet |
| `24-ring-clock.py` | A clock with red, green and blue hands. Button 1 adds an hour and Button 2 adds a minute |
| `25-prize-wheel.py` | **Games:** press a button to spin, and friction stops the pointer on a wedge |
| `26-cyclone-game.py` | Press a button when the dot is on the target. Each hit makes the game faster |
| `27-main-template.py` | Programs 05 to 21 in one program, except the still picture in 09. Button 1 is the next mode and Button 2 goes back |

Every program stands on its own and needs only `config.py`.

## Program 27: Main Template

Mode 0 is auto mode, which shows each pattern for 10 seconds. Modes 1 to 16 each show one pattern.

The Pico runs a file named `main.py` by itself whenever it powers up. To start the light show with
no computer attached, save a copy of `27-main-template.py` on the Pico as `main.py`:

```bash
mpremote cp 27-main-template.py :main.py
```

To add your own pattern, write a function that draws one step and add a line to the `patterns` list.

## Power

All 24 pixels at full white would draw about 1.4 amps, far beyond the half amp that USB can supply.
`BRIGHTNESS` in `config.py` is 0.25, and every program multiplies its colors by it. The brightest
moment in any program is about 240 mA, in `13-breathing-halo.py`. A full white ring at this
setting would be about 360 mA.

## Uploading

```bash
./upload-code.sh
```

It uploads `config.py` and all 27 programs. Quit or disconnect Thonny first, because only one program
can use the Pico's serial port at a time.

## What has been tested

Wiring and layout were checked on 2026-11-01, and every program was run on a real kit on
2026-11-02 (Raspberry Pi Pico, MicroPython 1.29.0). All the tests passed.

| Check | Result |
|-------|--------|
| Ring wiring | A person looked at a test pattern on GPIO 0: the colors were as expected |
| Pixel layout | A person looked at the same pattern: the numbers run clockwise and pixel 0 is at about 1:30, so `TOP_PIXEL = 21` |
| Buttons | Button 1 on GPIO 15 and Button 2 on GPIO 14 both work |
| Programs 01 to 27 | Every program ran on the kit and worked as described |

Before the kit test, programs 02 to 27 were also run on a computer, with stand-ins for the hardware.
A test script checked each one for errors, for bad pixel numbers and colors, and for two writes with
no sleep between them. It also pressed pretend buttons to step through every mode of program 27, and
it played the game in program 26.
