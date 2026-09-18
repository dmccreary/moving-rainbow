# Lab 25: Bouncing Ball

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    A ball made of light is about to bounce along your strip! It falls faster and faster, hits the floor, and hops back up a little lower each time. Let's light this up!

**Program file:** [`25-bouncing-ball.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/25-bouncing-ball.py)

## What you'll learn

- How to keep track of where the ball is (its position) and how fast it moves (its velocity)
- How one small rule, repeated every frame, makes a falling ball speed up
- How a minus sign and a number below 1 turn a fast fall into a slower bounce
- How a true-or-false variable can end a loop
- Why `round()` turns a decimal into a whole pixel number

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- Optional: hold the strip upright with the Pico end at the bottom, so the ball really falls

## The program

This program drops one orange ball from the top of the strip. It bounces on pixel 0 until it settles, rests for a second, and drops again.

```python title="25-bouncing-ball.py"
--8<-- "src/kits/moving-rainbow-base/25-bouncing-ball.py"
```

Run it. One orange pixel falls from the top and speeds up as it drops. It bounces on pixel 0, and each bounce is lower than the one before. After a little more than three seconds, the ball settles. It rests for one second, and then it drops again.

## How it works

### The settings at the top

```python
BALL_COLOR = (140, 60, 0)   # orange
GRAVITY = 0.2               # how much faster the ball falls each frame
BOUNCE = 0.8                # the ball keeps 80% of its speed after a bounce
MIN_SPEED = 0.6             # slower than this and the ball stops bouncing
FRAME_DELAY = 0.03          # seconds per frame
```

These five names are settings. Each one is set once, and the rest of the program reads it. You can change a setting without touching any other line.

| Setting | What it does |
|---------|--------------|
| `BALL_COLOR` | The ball's color as (red, green, blue). Orange is a lot of red and a little green. |
| `GRAVITY` | How much faster the ball falls each frame. |
| `BOUNCE` | The share of its speed the ball keeps after a bounce. 0.8 means 80 percent. |
| `MIN_SPEED` | If a bounce is slower than this, the ball stops bouncing. |
| `FRAME_DELAY` | Seconds to wait after each **frame** (one picture on the strip). 0.03 gives about 30 pictures a second. |

Only one pixel is lit at a time, so this program is gentle on your USB port.

### Position and velocity

```python
position = NUMBER_PIXELS - 1
velocity = 0            # pixels per frame: up is positive, down is negative
bouncing = True
```

A moving ball needs two facts: where it is, and how it is moving. These lines set both facts for the start of a drop.

The **position** is where the ball is. Pixel 0 is the floor. It is the end of the strip nearest the Pico. Pixel 29 is the top, and `NUMBER_PIXELS - 1` is 29. So each drop starts from the top.

The **velocity** is speed with a direction. It counts pixels per frame. A positive velocity means up, and a negative velocity means down. Starting at 0 means the ball begins at rest, like a ball the moment you let go.

Both numbers start as whole numbers. The first frame turns them into **floats** (numbers with a decimal point), like 28.8. The ball moves only 0.2 pixels in its first frame, so it needs fractions of a pixel.

### Gravity changes the speed

```python
velocity = velocity - GRAVITY
position = position + velocity
```

These two lines run once every frame. **Gravity** is something that changes the velocity by the same amount every frame. Here, gravity takes 0.2 away from the velocity. Then the new velocity moves the ball.

So each frame the ball falls a little faster than the frame before. The order matters: change the speed first, and then move the ball.

Here are the first frames of a drop. The table shows `position` rounded to one decimal place.

| Frame | `velocity` | `position` | Pixel lit |
|-------|------------|------------|-----------|
| 1 | -0.2 | 28.8 | 29 |
| 2 | -0.4 | 28.4 | 28 |
| 3 | -0.6 | 27.8 | 28 |
| 4 | -0.8 | 27.0 | 27 |
| 5 | -1.0 | 26.0 | 26 |
| ... | ... | ... | ... |
| 15 | -3.0 | 5.0 | 5 |
| 16 | -3.2 | 1.8 | 2 |

Look at the last column. In frames 2 and 3, the ball stays on pixel 28, because it moves less than one pixel per frame. By frame 16, the ball moves 3.2 pixels per frame. It skips right over pixels 4 and 3. That growing jump is the speed-up you see.

The same two lines also work on the way up. A positive velocity gets smaller each frame, because gravity keeps taking 0.2 away. It reaches 0 at the top of the hop. Then it turns negative, and the ball falls again. One rule makes the whole arc: up, pause, and down.

!!! tip "Tip"
    Want to see the real numbers? Add `print(round(position, 1), round(velocity, 1))` below the `position = position + velocity` line. Indent it to match. Thonny's Shell fills with the same kind of numbers as the table.

### The bounce

```python
if position <= 0:
    position = 0
    velocity = -velocity * BOUNCE
    if velocity < MIN_SPEED:
        bouncing = False
```

This block runs when the ball reaches the floor. On frame 17 of the first drop, gravity makes the velocity -3.4. The move puts the ball at 1.8 - 3.4 = -1.6, which is below the floor. The `if` line catches that. Then three things happen:

1. `position = 0` puts the ball back on the floor, so it stays at pixel 0 or above.
2. `-velocity` flips the sign. The ball was moving down at -3.4, so it now moves up at 3.4.
3. `* BOUNCE` keeps 80 percent of that speed: 3.4 x 0.8 = 2.72. Real balls lose some energy when they hit the floor, so they bounce lower.

Multiplying by a number below 1, again and again, is the shrinking trick from [Lab 24: Fading Stars](24-fading-stars.md). There, `level * 3 // 4` faded a star. Here, `velocity * BOUNCE` shrinks the ball's speed.

!!! info "Key idea"
    A minus sign flips a direction. Multiplying by a number below 1 shrinks a value. Together they turn a fast fall into a slower rise.

Each bounce is lower than the one before. Working through the numbers, the ball starts at pixel 29. Its next hops reach pixels 17, 10, 6, 3, 2, and 1. Each height is roughly 60 percent of the one before. The heights shrink faster than the speed does, because a slower ball has less time to climb.

The inner `if` decides when to stop. It asks: is the new speed below `MIN_SPEED`? On the seventh time the ball touches the floor, its new speed is about 0.56. That is below 0.6, so the code sets `bouncing = False`.

The `bouncing` variable is a **flag** (a variable that holds `True` or `False` and tells the program whether to keep going). The loop `while bouncing:` runs as long as the flag is `True`. When the flag turns `False`, the loop ends. The rest of that frame still runs, so the ball is drawn at rest on pixel 0.

### Keep the ball on the strip

```python
if position > NUMBER_PIXELS - 1:
    position = NUMBER_PIXELS - 1
```

This is a **guard**: an `if` that protects the program from a value that could cause trouble. Pixel 29 is the last pixel, and there is no pixel 30.

With `BOUNCE` at 0.8, the ball stays at or below its starting height, so the guard stays quiet. If you set `BOUNCE` above 1, each bounce adds speed. The ball could then rise past pixel 29, and the program would stop. The guard holds the ball at the top instead. You'll try this in Challenge 2.

### Draw one pixel each frame

```python
strip[old_pixel] = (0, 0, 0)
pixel = round(position)
strip[pixel] = BALL_COLOR
strip.write()
old_pixel = pixel
sleep(FRAME_DELAY)
```

These six lines draw one frame:

1. Erase the ball's old spot. This only changes a note in the Pico's memory.
2. `round(position)` turns a decimal like 24.8 into the nearest whole number, 25. A pixel number must be whole.
3. Light the new pixel with `BALL_COLOR`.
4. `strip.write()` sends the picture to the strip. It runs once per frame, the same rule as [Lab 05: Move a Pixel](05-move.md).
5. `old_pixel = pixel` remembers the spot, so the next frame can erase it.
6. `sleep(FRAME_DELAY)` waits 0.03 seconds before the next frame.

Erasing comes first and lighting comes second. That order keeps the ball lit when it stays on the same pixel for two frames. Exactly one pixel is lit in every frame.

### Two loops: one drop, then again

```python
old_pixel = 0
while True:
    ...
    while bouncing:
        ...
    sleep(1)    # the ball rests for a moment, then drops again
```

This program has two loops, one inside the other. The inner loop, `while bouncing:`, draws one frame each time around. It runs until the flag turns `False`. That is one drop.

The outer loop, `while True:`, repeats forever. When a drop ends, `sleep(1)` lets the ball rest for one second. Then the loop starts over. The three setup lines from earlier put `position`, `velocity`, and `bouncing` back where they began, and the ball drops from the top again. Press **Stop** in Thonny to end the program.

The line `old_pixel = 0` gives the very first frame a pixel to erase. At the end of every drop, `old_pixel` holds 0 again, because the ball rests on the floor. So the first frame of the next drop erases the resting ball.

Work through the numbers, and one drop takes 109 frames. At 0.03 seconds each, that is about 3.3 seconds. It is a little more once you add the time to write each frame. The ball first touches the floor on frame 17, about half a second after the drop starts. With the one-second rest, the whole cycle takes a little more than four seconds.

### A real bounce

[Lab 30: Random Bounce](30-random-bounce.md) also has dots that bounce, but they are very different. Those dots move one pixel per step at a steady speed and turn around at the ends. This ball has gravity, so its speed changes every frame, and each bounce takes some speed away. That is what makes it look like a real ball.

## Try it yourself

### Challenge 1: Change the planet

Find the line `GRAVITY = 0.2`. Change it to `GRAVITY = 0.05`, and run the program. Gravity is weaker, so the ball should float down like a ball on the moon. Then try `GRAVITY = 0.5` for a heavy planet. Predict what you will see before you run each one.

Look at how long the first fall takes. With `GRAVITY = 0.05`, the ball should take about twice as long to land as it does with 0.2.

### Challenge 2: Change the bounce

Find the line `BOUNCE = 0.8`. Try these values, one at a time:

- `BOUNCE = 0.5`: a dead thud. How many hops does the ball make before it stops?
- `BOUNCE = 1.0`: a super ball. The ball keeps all of its speed. Does it ever stop?
- `BOUNCE = 1.1`: the ball gains speed each time. Which line keeps it on the strip?

Change it back to `0.8` when you are done.

### Challenge 3: Pick a new color

Find the line `BALL_COLOR = (140, 60, 0)`. Change the three numbers to make a ball in your favorite color. Try `(0, 0, 100)` for blue or `(100, 0, 100)` for purple. The [Additive and Subtractive Mixing](../sims/additive-subtractive-mixing/index.md) MicroSim shows how the three numbers blend.

### Bonus: for big thinkers

These two ideas change more of the program. Take your time with them.

- **Add a fading tail.** Keep a list with one brightness number for each pixel, like in Lab 24. Each frame, set the ball's pixel to full brightness. Then shrink every pixel's number a little, so the tail fades. You will need to replace the erase line.
- **Add a second ball.** Each ball needs its own `position`, `velocity`, and `old_pixel`. Start the second ball at a different height, or a few frames later.

## Check your understanding

1. Why does the ball speed up while it falls?
2. What does the minus sign in `-velocity * BOUNCE` do? What does `* BOUNCE` do?
3. What would happen if `BOUNCE` were 0? Use `MIN_SPEED` in your answer.
4. What makes the `bouncing` flag turn `False`, and which loop does that end?
5. Which lines keep the ball on the strip if `BOUNCE` is 1.5, and why are they needed?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You gave a light its own gravity! One rule to speed up and one rule to bounce made a ball that looks alive. Game makers use the same trick.

**What's next:** In [Lab 26: Breathing Wave](26-breathing-wave.md), a wave of blue light rolls along the strip as every pixel breathes in and out.
