# Lab 2: Hardware Probe

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Before we build, let's check that every part is awake. This program asks each part a question: are you there?
    Every bug is just a puzzle in disguise, and this one finds the puzzles for us!

**Program file:** [`02-probe.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/16x16-matrixs-accel/02-probe.py)

## What you'll learn

- What a **probe** program is and why it saves time
- How to read `TEST PASS` and `TEST FAIL`
- What a pin level of 1 or 0 means
- What an **I2C scan** (a check of the two-wire connection to the sensor) does
- How to use the report to find a wiring mistake

## What you'll need

- Your kit, wired as shown in the [Kit Guide](index.md)
- The `config.py` file saved on the Pico (see [Get the Code onto the Pico](index.md#get-the-code-onto-the-pico))
- Thonny open and connected to your Pico
- Do not touch the buttons while the probe runs

## The program

A **probe** is a test program. It does not make a light show. It checks each part and prints a report. This program is long, so we will look at three small pieces. Open `02-probe.py` in Thonny and click **Run**.

Keep the kit flat and still for about two seconds while the sensor takes its readings. The report looks like this. The numbers for memory and the three tilt readings will be a little different on your kit.

```text
Test 02: Hardware Probe (version 1.0.0)
==================================================
Board / system info
==================================================
machine : Raspberry Pi Pico with RP2040

==================================================
Button pin check (GPIO14 and GPIO15, internal pull-ups enabled)
==================================================
Button 1 (GPIO14) idle level: 1 (1 = not pressed, as expected)
Button 2 (GPIO15) idle level: 1 (1 = not pressed, as expected)

==================================================
I2C0 scan (SDA=GPIO16, SCL=GPIO17, no internal pull-ups - testing board's own pull-ups)
==================================================
Found 1 device(s):
  decimal  25  hex 0x19  <-- LIS3DH (SDO high)

==================================================
WHO_AM_I check (register 0x0F at device 0x19)
==================================================
WHO_AM_I returned: 0x33

TEST PASS - LIS3DH found at 0x19, WHO_AM_I confirms 0x33, readings look right
```

The report has more lines than we show here. The last line is the one that matters. `TEST PASS` means every check worked. `TEST FAIL` means something needs a fix, and the lines above it tell you what.

## How it works

### Is a wire stuck?

```python title="02-probe.py (lines 122 to 127)"
--8<-- "src/kits/16x16-matrixs-accel/02-probe.py:122:127"
```

A pin that nothing is driving reads **1** or **0**. These two lines turn on the Pico's tiny internal pull-up resistor, which holds the pin at 3.3 volts. A healthy pin then reads **1**. If a pin reads **0**, it is stuck to ground, and the wire may be touching something it should not.

The variable `lines_ok` becomes `True` only when both the clock and data pins read 1.

### Who is on the I2C wires?

```python title="02-probe.py (lines 244 to 252)"
--8<-- "src/kits/16x16-matrixs-accel/02-probe.py:244:252"
```

**I2C** is a two-wire way for parts to talk. Every part on the wires has its own **address**, like a house number. The line `devices = i2c.scan()` knocks on every address and collects the ones that answer.

Addresses are printed in **hexadecimal** (hex for short). Hex counts in sixteens instead of tens. The hex number `0x19` is the same as 25. Our accelerometer answers at `0x19`.

### Is it really the right chip?

```python title="02-probe.py (lines 165 to 172)"
--8<-- "src/kits/16x16-matrixs-accel/02-probe.py:165:172"
```

Our chip has a **register** (a numbered mailbox inside the chip) that always holds the number `0x33`. It is named `WHO_AM_I`. The line with `readfrom_mem` opens that mailbox and reads it. If the answer is `0x33`, we know the chip is a LIS3DH.

The `try` and `except` lines are a safety net. If the chip does not answer, Python runs the `except` lines and prints `TEST FAIL` instead of crashing.

!!! info "Key idea"
    A probe tests parts one at a time. When something fails later, you already know which parts are fine.

## If you see TEST FAIL

| What the report says | What to try |
|----------------------|-------------|
| `a button reads pressed` | Let go of the buttons and run again. If it still says pressed, check that button's wires |
| `SCL idle level: 0` or `SDA idle level: 0` | Check for a wire touching ground. Check that SCL and SDA go to GP17 and GP16 |
| `No I2C devices found` | Check VIN (3.3 volts), GND, SCL, and SDA. The probe also tries the wires swapped for you |
| `DIAGNOSIS` about swapped wires | Swap the SCL and SDA wires on the breadboard |
| `config.py ACCEL_ADDRESS` does not match | Change `ACCEL_ADDRESS` in `config.py` to the address the probe found |

## Try it yourself

1. Unplug the **USB** (Universal Serial Bus) cable. Move the SDA wire to a different pin. Plug in and run the probe. What does the report say? Put the wire back and run it again.
2. Run the probe while you hold Button 1 down. Which line of the report changes?
3. Find the line that prints the average readings. Which axis points down when your kit lies flat?

## Check your understanding

1. What does `TEST PASS` tell you?
2. What number should a button pin read when nobody presses the button?
3. What is an I2C address? Which address does the accelerometer use?
4. Why does the probe run a test one part at a time?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    Your kit passed its checkup! Every part answered, so we can build with confidence.

**What's next:** In [Lab 3: Button Test](03-button-test.md), you will watch your two buttons work.
