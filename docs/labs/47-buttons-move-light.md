# Lab 47: Buttons Move a Light

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Until now, the patterns moved all by themselves. This time you're in the driver's seat! Press a button and the light hops where you tell it.

**Program file:** [`47-buttons-move-light.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/47-buttons-move-light.py)

## What you'll learn

- How to keep a light's place in a variable named `position`
- How a button **interrupt** changes `position` while the main loop keeps running
- How `%` makes the position wrap from one end of the strip to the other
- How to redraw the strip only when something has changed

## What you'll need

- Your base kit, including both push buttons wired as shown in [The Two Buttons](../kits/moving-rainbow-base/index.md#the-two-buttons). Each button reads `0` while you press it.
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- [Lab 34: Two Buttons](34-two-button-print.md) first. It teaches the interrupt and debounce pattern that this lab uses again.

## The program

This program lights one dim red pixel in the middle of the strip. Button 1 moves it up one pixel and Button 2 moves it down one pixel.

??? example "Full program: 47-buttons-move-light.py (98 lines)"
    ```python title="47-buttons-move-light.py"
    --8<-- "src/kits/moving-rainbow-base/47-buttons-move-light.py"
    ```

Run it. A dim red light appears at pixel 15. Each press of Button 1 moves it up one pixel, and each press of Button 2 moves it down one pixel. The Shell counts your presses, like this:

```text
button 1 pressed  3 times; button 2 pressed 1 times
```

## How it works

### The position is a variable

In earlier labs, a loop counter chose the pixel. Here, `position` is a plain variable. The buttons change it, and the main loop draws the light wherever `position` says.

```python
HALF_LENGTH = round(NUMBER_PIXELS/2)
position = HALF_LENGTH
```

`round(NUMBER_PIXELS/2)` is `15`, so the light starts at pixel 15, near the middle of the strip.

### The button handler

An **interrupt** is a signal that makes the Pico pause what it is doing, run a small function, and then go back to its work. The small function is called a **handler**. These two lines connect both buttons to the handler.

```python
button1.irq(trigger=Pin.IRQ_FALLING, handler = button_pressed_handler)
button2.irq(trigger=Pin.IRQ_FALLING, handler = button_pressed_handler)
```

`IRQ_FALLING` means "run the handler when the pin's value falls from 1 to 0." That is the moment you press a button, because a pressed button reads `0`.

The handler starts with a **debounce** check. A button's metal contacts can bounce for a moment, so one press can look like several. The check ignores any press that comes less than 200 milliseconds after the last one.

```python
def button_pressed_handler(pin):
    global position, last_time, button1_presses, button2_presses
    new_time = ticks_ms()
    # if it has been more than 1/5 of a second since the last event, we have a new event
    if (new_time - last_time) > 200:
```

The `global` line lets the handler change variables that live outside of it. `ticks_ms()` gives the number of milliseconds since the Pico started. So the light can move at most five times each second.

The handler gets a `pin` value that says which button was pressed. Button 1 moves the position up by one. Button 2 moves it down by one. Each button also keeps its own press count.

```python
        if pin == button1:
            position +=1
            button1_presses +=1
        else: #we know that a button has been pressed, and it's not button 1, so it must be button 2
            position -=1
            button2_presses +=1
```

The last lines of the handler wrap the position, remember the time, and print the counts.

```python
        # wrap around if we get too high
        position = position % NUMBER_PIXELS
        last_time = new_time
        print('button 1 pressed ', button1_presses, 'times; button 2 pressed', button2_presses, 'times')
```

### Wrap around with %

The strip has pixels 0 to 29, but `position` can step past either end. The **modulo** operator `%` gives the remainder after dividing, and that brings the number back onto the strip.

| Button press | `position` before `%` | `position` after `% 30` |
|:------------:|:---------------------:|:-----------------------:|
| Button 1 at pixel 16 | 17 | 17 |
| Button 1 at pixel 29 | 30 | 0 |
| Button 2 at pixel 0 | -1 | 29 |

So pressing Button 1 at the top of the strip sends the light to pixel 0. Pressing Button 2 at pixel 0 sends it to pixel 29. The comment in the code only mentions "too high", but the same line also fixes "too low". The [Modulo Wrap-Around Animation](../sims/modulo-wrap-simulation/index.md) shows the idea in motion.

### Draw only when something changed

This function moves the light. Its inputs are the old place (`lp`), the new place (`counter`), a color, and a pause in seconds.

```python
def move_dot(lp, counter, color, delay):
    strip[lp] = (0,0,0)
    strip[counter] = color
    strip.write()
    sleep(delay)
```

It does four things in order. It erases the old pixel in memory. It sets the new pixel's color in memory. It calls `strip.write()` once to send both changes. Then it waits.

The main loop uses `move_dot` like this.

```python
erase()
last_position = 0

while True:
    if position != last_position:
        move_dot(last_position, position, red_med, .1)
        last_position = position
```

`erase()` clears every pixel in memory, so the strip starts dark. The loop spins thousands of times a second. The test `position != last_position` makes it draw only when a button has changed `position`. Then `last_position = position` remembers where the light is now.

At the start, `position` is 15 and `last_position` is 0. They are different, so the first pass through the loop draws the light at pixel 15.

### Lines you can ignore

Some lines near the top came along from other programs and do nothing here. They are `randint`, the `builtin_led` pin, and every color except `red_med`. A comment in the file says the same. Leaving them alone is fine.

## Try it yourself

1. In the line `move_dot(last_position, position, red_med, .1)`, change `red_med` to `(0, 32, 0)`. What color is the light now?
2. Change `position = HALF_LENGTH` to `position = 0`. Run it. No light appears until you press a button. Why? Hint: look at `last_position` and the `if` in the main loop.

## Check your understanding

1. What does Button 1 do to `position`? What does Button 2 do?
2. What does `position % NUMBER_PIXELS` give when `position` is 30? What about when it is -1?
3. Why does the main loop compare `position` with `last_position`?
4. Why does the handler ignore a press that comes less than 200 milliseconds after the last one?
5. Name the four steps that `move_dot` does, in order.

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built a real controller! Your buttons now steer a light the way a game controller steers a character.

**What's next:** In [Lab 48: Pixel Demo](48-pixel-demo.md), the same two buttons pick between twelve light patterns.
