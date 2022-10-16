# Twinkle


```python
def twinkle(delay):
    random_index = randint(0, NUMBER_PIXELS);
    # turn on
    strip[random_index] = (255,255,255) 
    strip.write();
    sleep(delay);
    # turn off
    strip[random_index] = (0,0,0) 
    strip.write();
```