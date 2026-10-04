# Lab 9: Accelerometer Print

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Your kit can feel which way is down! In this lab we'll listen to the tilt sensor and print what it says.
    Let's light this up!

**Program file:** [`09-accel-print.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/16x16-matrixs-accel/09-accel-print.py)

## What you'll learn

- What the x, y, and z numbers from an accelerometer mean
- How the Pico asks a chip for numbers over **I2C** (a two-wire connection)
- How six bytes turn into three readings
- How to change a raw reading into **g**
- How to print numbers in neat columns

## What you'll need

- Your kit, with the accelerometer wired as shown in the [Kit Guide](index.md#step-3-wire-the-accelerometer)
- `config.py` saved on the Pico
- Thonny open and connected to your Pico
- A passing [Lab 2: Hardware Probe](02-probe.md)

## The program

This program reads the accelerometer five times a second and prints x, y, and z in g.

```python title="09-accel-print.py"
--8<-- "src/kits/16x16-matrixs-accel/09-accel-print.py"
```

Run it with the kit lying flat on the table. The numbers should look like this, with z close to 1 and x and y close to 0. Then pick the kit up and tilt it slowly. Watch the numbers change.

```text
Test 09: Accelerometer Print (version 1.0.0)
WHO_AM_I: 0x33 (0x33 is a LIS3DH)
x:  0.01  y:  0.02  z:  1.03
x:  0.00  y:  0.01  z:  1.04
x:  0.01  y:  0.02  z:  1.03
```

When one of our test kits was tipped up, the numbers looked like this:

```text
x:  0.44  y: -0.18  z:  0.70
x:  0.70  y: -0.18  z:  0.61
x:  0.87  y: -0.20  z:  0.46
```

## How it works

### Open a line to the chip

```python
i2c = I2C(ACCEL_I2C_ID, sda=Pin(ACCEL_SDA_PIN), scl=Pin(ACCEL_SCL_PIN), freq=400000)
```

This line sets up the two I2C wires. It says which pin is the data wire (`sda`) and which is the clock wire (`scl`). The number `freq=400000` is the speed: 400,000 ticks of the clock every second.

### Wake the chip

```python
i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG1, b'\x57')
i2c.writeto_mem(ACCEL_ADDRESS, CTRL_REG4, b'\x88')
```

The chip has numbered mailboxes inside it called **registers**. Writing a number into a control register sets a switch. The chip starts powered down, so we send two messages. The first one turns on the x, y, and z sensors and sets 100 readings a second. The second one picks the measuring range, plus or minus 2 g. It also keeps each reading steady while we read it.

The `b'\x57'` is one **byte**, a number from 0 to 255, written in hexadecimal.

### Read six bytes

```python
raw = i2c.readfrom_mem(ACCEL_ADDRESS, ACCEL_DATA_REGISTER, 6)
x, y, z = ustruct.unpack('<hhh', raw)
```

The first line asks the chip for six bytes. Each reading uses two bytes, and there are three readings: x, y, and z. The second line, `ustruct.unpack`, turns those six bytes into three whole numbers. The letters `hhh` mean "three numbers that can be positive or negative."

### Change the numbers into g

```python
print("x: %5.2f  y: %5.2f  z: %5.2f" % (x / COUNTS_PER_G, y / COUNTS_PER_G, z / COUNTS_PER_G))
```

The chip says 16384 when it feels exactly 1 g. That is why the program divides by `COUNTS_PER_G`, which is 16384. For example, a raw z of 16900 divided by 16384 is 1.03 g.

The `%5.2f` is a **format code**. It means: print a decimal number, 5 characters wide, with 2 digits after the point. That keeps the columns neat.

### What do x, y, and z mean?

Gravity always pulls toward the floor. The sensor measures how much of that pull points along each of its three directions. Flat on the table, gravity points along z, so z is about 1. Stand the kit on its edge, and the pull shifts to x or y.

Here is a neat check. The total pull always stays about 1 g, no matter how you tilt. Use the tipped reading from above, `x: 0.87  y: -0.20  z: 0.46`, and add up the squares:

0.87 × 0.87 + 0.20 × 0.20 + 0.46 × 0.46 = 0.757 + 0.040 + 0.212 = 1.009

The square root of 1.009 is about 1.00. The three numbers share one g between them!

!!! info "Key idea"
    An accelerometer cannot tell gravity from a push. It feels both. That is why shaking the kit changes the numbers. Real sensors are also a tiny bit off, so a flat reading of 1.03 instead of 1.00 is normal.

## Try it yourself

1. Stand the kit on each of its four edges, one at a time. Which axis reads close to 1 or -1 for each edge?
2. Shake the kit gently. Do the numbers go above 1? Why?
3. Change `sleep(0.2)` to `sleep(0.05)`. Predict how the numbers will look before you run it.
4. Print only z. Change the `print` line to `print("z:", z / COUNTS_PER_G)`. Then try rounding it with `round(z / COUNTS_PER_G, 2)`.

## Check your understanding

1. What does 1 g mean?
2. When the kit lies flat, which axis reads about 1?
3. Why does the program divide by `COUNTS_PER_G`?
4. How many bytes does the program read each time? How many readings do they make?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You read a real sensor and turned bytes into g! Next, we'll use the sensor to move a light.

**What's next:** In [Lab 10: Accelerometer Bubble](10-accel-bubble.md), tilting the kit will slide a dot across the matrix.
