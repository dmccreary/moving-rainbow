# Moving Bands of Color

In this lesson, we will create a program that will move a set of bands of color down the LED strip.  To do this we will create a function called ```draw_band(start, end, color)``` that will fill a range of pixels with a given color.

```python
def draw_band(start, end, color, delay):
    # draw the band from start to end
    for i in range(start, end):
        strip[i % NUMBER_PIXELS] = color
```

This works, but we also have the problem that the last pixel does not get erased


```python
def draw_band(start, end, color, erase_tail, delay):
    # draw the band from start to end
    for i in range(start, end):
        strip[i % NUMBER_PIXELS] = color
    # erase the last pixel on the erase tail band
    if erase_tail and start > 0:
        strip[(start-1) % NUMBER_PIXELS] = (0,0,0)
    strip.write()
    sleep(delay)
```

We can then draw three "bands" of color like this:

```python
draw_band(0, 9, 'red')
draw_band(10, 19, 'green')
draw_band(20, 29, 'blue')
```

We can make this group of bands appear to move by adding a offset to the start like this:

```python
for i in range(0, NUMBER_PIXELS)
    draw_band(i, i+9, 'red')
    draw_band(i+10, i+19, 'green')
    draw_band(i+20, i+29, 'blue')
```

This will work fine until the value of i plus the offset exceeds the length of the LED strip.  To get around this, we should never write to location i by itself.  We should always divide i by the strip lenght and write to the remainder, what is call the modulo.  We just have to change one line in the draw_band function:

```python
def draw_band(start, end, color):
    for i in range(start, end):
        strip[i%NUMBER_PIXELS] = color
    strip.write()
```
