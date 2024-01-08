
# Challenges for Python LED Exercises

## 1. Blink.py
### a. Original intent:
- Understand the “strip[0]” position
- Understand RGB numbering
- Understand “sleep(1)” (1 = seconds)
- Introduce “while True:” looping concept

### b. Challenge:
- Select a different position
- Select a different color
- Select a different delay

## 2. Red-green-blue.py
### a. Original intent:
- Reinforce above concepts

### b. Challenge:
- Change brightness
- Make lights blink (turn off) before changing colors
- Add new colors (blending RGB)

## 3. Dimmer.py
### a. Original intent:
- Reinforce above
- Introduce ‘stepping’ parameter in for loop, and thus the concept of counting backwards

### b. Challenge:
- Select a different rate at which to increase and decrease brightness (different step value) – light up only the even-numbered LEDs (or odd)
- Have different lights dim/brighten – make each of the lights in the strip brighten/dim in sequence

## 4. Move.py
### a. Original intent:
- Reinforce above
- Introduce config.NUMBER_PIXELS & using that to control the end of loop
  - Note that NUMBER_PIXELS indicates the quantity of LEDs in the strip, but that the LEDs are indexed/identified starting with 0

### b. Challenge:
- Make the move backwards (well .. this is done in the next exercise)
- Illuminate every third LED on the strip
- Make the lights appear to “run faster” backwards than forwards

## 5. Up-and-down.py
### a. Original intent:
- Reinforce above

### b. Challenge:
- See challenges in Move.py

## 6. Color-wipe.py
### a. Original intent:
- Reinforce above

### b. Challenge:
- Make it so that the entire strip seems to change from R to G to B at once
- Make a stop light – top 1/3 = red, mid = yellow, lower 1/3 = green

## 7. Random.py
### a. Original intent:
- Reminder about “randint” function
- Reinforce RGB, looping

### b. Challenge:
- Have two LEDs lit at the same time, one randomly in the lower half of the strip and one in the upper half.
- Have two LEDs lit at the same time, each the same random distance from the center point

## 8. Color-wheel.py
### a. Original intent:
- Reminder about creating functions
- Use of “return”

### b. Challenge:
- Either make entire strip become a color wheel
- Or … make each LED in the strip become a color wheel, one by one with a slight pause between

## 9. Rainbow.py
### a. Original intent:
- Reinforce functions/return

### b. Challenge:
- Make it build rainbow backwards (so end result is VIBGYOR)

## 10. Rainbow-cycle.py
### a. Original intent:
- More of rainbow.py, but moving in continuous loop

### b. Challenge:
- Make it cycle forwards, then backwards
