# Hands on Labs

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to the labs! Every lab is one small program you can run on your kit. You change a
    number, you see a light change. That's how coders learn. Let's light this up!

Each lab matches one program in the kit's source folder. The lab number is the program's number:
Lab 05 is `05-move.py`, and Lab 28 is `28-clock.py`. Every lab uses only the parts in the
[base kit](../kits/moving-rainbow-base/index.md): a Raspberry Pi Pico, a 30-pixel LED strip, and two push buttons.

## How to use a lab

1. Wire your kit as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md).
2. Save `config.py` on your Pico. Every program reads its pin numbers from that file. Lab 01 is the only one that does not need it.
3. Open the lab's program in Thonny and press **Run**.
4. Read the lab page, then try the challenges at the bottom.

All the programs live in
[`src/kits/moving-rainbow-base/`](https://github.com/dmccreary/moving-rainbow/tree/master/src/kits/moving-rainbow-base)
on GitHub. The lab pages show the real program files, so the code you read here is the code that runs on your kit.

## First steps with one pixel (Labs 01 to 06)

Start here. These labs use one pixel at a time and teach the basics: colors, `strip.write()`, loops, and moving along the strip.

| Lab | What you'll see |
|-----|-----------------|
| [01: Blink the Onboard LED](01-blink-onboard-led.md) | The Pico's own tiny LED blinks. No wiring needed. |
| [02: Blink](02-blink.md) | One red pixel blinks on and off |
| [03: Red, Green and Blue](03-red-green-blue.md) | One pixel steps through red, green, and blue |
| [04: Dimmer](04-dimmer.md) | One pixel fades up and back down |
| [05: Move a Pixel](05-move.md) | A red dot slides along the strip |
| [06: Up and Down](06-up-and-down.md) | The dot slides up the strip and back down |

## Color and randomness (Labs 07 to 13)

Fill the strip with color, add some chance, and build the color wheel that makes every rainbow in this book.

| Lab | What you'll see |
|-----|-----------------|
| [07: Color Wipe](07-color-wipe.md) | Each color fills the strip one pixel at a time |
| [08: Random](08-random.md) | A pixel flashes in a random color at a random place |
| [09: Color Wheel](09-color-wheel.md) | One pixel steps through every color of the rainbow |
| [10: Random Colors](10-random-colors.md) | Color-wheel colors pop up at random places |
| [11: Rainbow](11-rainbow.md) | A still rainbow across the whole strip |
| [12: Rainbow Cycle](12-rainbow-cycle.md) | The rainbow rotates around the strip |
| [13: Moving Rainbow with the Color Wheel](13-moving-rainbow.md) | A short rainbow slides along the strip |

## Patterns and animation (Labs 14 to 22)

Bands, comets, candles, and chases: the classic LED strip patterns.

| Lab | What you'll see |
|-----|-----------------|
| [14: Band](14-band.md) | Six bands of color fill the strip |
| [15: Moving Band](15-moving-band.md) | The bands slide along the strip |
| [16: Comet](16-comet.md) | A bright head with a fading tail |
| [17: Moving Rainbow with a Color List](17-moving-rainbow.md) | A seven-color rainbow slides along the strip |
| [18: Candle Flicker](18-candle-flicker.md) | A warm, random flicker like a candle flame |
| [19: Theater Chase](19-theater-chase.md) | Classic marquee chase lights |
| [20: Ripple](20-ripple.md) | Ripples spread out like drops in a pond |
| [21: Twinkle Colors](21-twinkle-colors.md) | A random pixel twinkles in a random color |
| [22: Random Walk](22-random-walk.md) | A dim pixel wanders left and right by chance |

## Brightness, motion and math (Labs 23 to 27)

A heartbeat, fading stars, a bouncing ball, a breathing wave, and a sunrise. These labs bring in lists that
remember a brightness for every pixel, a little physics, sine waves, and blending one color into another.

| Lab | What you'll see |
|-----|-----------------|
| [23: Heartbeat](23-heartbeat.md) | One pixel beats like a heart: a strong pulse, a soft pulse, and a rest |
| [24: Fading Stars](24-fading-stars.md) | Stars flare up at random places and fade away smoothly |
| [25: Bouncing Ball](25-bouncing-ball.md) | A ball drops, speeds up, and bounces lower and lower until it rests |
| [26: Breathing Wave](26-breathing-wave.md) | A wave of blue light breathes its way along the strip |
| [27: Sunrise](27-sunrise.md) | The whole strip blends from night to dawn to sunrise to day, then sets again |

## Clock, scanner and bounce (Labs 28 to 30)

| Lab | What you'll see |
|-----|-----------------|
| [28: Binary Clock](28-clock.md) | The time shown in binary, using colored pixels |
| [29: Larson Scanner](29-larson-scanner.md) | The Cylon eye sweeps back and forth |
| [30: Random Bounce](30-random-bounce.md) | Dots move back and forth along the strip |

## Buttons and modes (Labs 31 to 37)

These labs add the two push buttons. Lab 31 is a showcase: it runs twelve patterns from one program. It uses
ideas that Labs 32 to 37 teach in small steps, so you can run it first for fun, or come back to it after Lab 37.

| Lab | What you'll see | Buttons used |
|-----|-----------------|--------------|
| [31: Button Modes](31-modes.md) | Twelve patterns in one program, and the buttons switch between them | 1 and 2 |
| [32: Button Test](32-button-test.md) | The Shell prints `1` and `0` as you press Button 1 | 1 |
| [33: Button and Built-in LED](33-button-led-test.md) | The Pico's own LED lights while you press Button 1 | 1 |
| [34: Two Buttons](34-two-button-print.md) | A counter goes up with one button and down with the other | 1 and 2 |
| [35: Button Change Color](35-button-change-color.md) | The buttons step through a list of colors | 1 and 2 |
| [36: Button Change Speed](36-button-change-speed.md) | The buttons speed up and slow down a moving pixel | 1 and 2 |
| [37: Modes Auto Cycle](37-modes-auto-cycle.md) | The strip changes mode by itself on a timer | None |

## Advanced patterns and games (Labs 38 to 46)

Each of these builds on skills from earlier labs. The first ones need no buttons. The games use them.

| Lab | What you'll see | Buttons used |
|-----|-----------------|--------------|
| [38: Traffic Light](38-traffic-light.md) | Red, green, and yellow pixels change on a timer | None |
| [39: Binary Counter](39-binary-counter.md) | Pixels count from 0 to 31 in binary | None |
| [40: Charge-Up Game](40-charge-up-game.md) | Hold the button to fill the strip and let go in the target zone | 1 |
| [41: Tug of War](41-tug-of-war.md) | Two players race to pull a marker to their end of the strip | 1 and 2 |
| [42: Reaction Duel](42-reaction-duel.md) | Two players race to press when the strip turns green | 1 and 2 |
| [43: Fire Simulation](43-fire-simulation.md) | A flickering flame built from a heat simulation | None |
| [44: Cellular Automaton](44-cellular-automaton.md) | One simple rule grows a complex pattern | None |
| [45: Sorting Visualizer](45-sorting-visualizer.md) | Watch a bubble sort put pixel brightness in order | None |
| [46: Binary Search Visualizer](46-binary-search-visualizer.md) | The Pico guesses your secret pixel in a few tries | 1 and 2 |

## Putting it together (Labs 47 and 48)

| Lab | What you'll see | Buttons used |
|-----|-----------------|--------------|
| [47: Buttons Move a Light](47-buttons-move-light.md) | The buttons push a lit pixel up and down the strip | 1 and 2 |
| [48: Pixel Demo](48-pixel-demo.md) | The full demo: twelve patterns, and the buttons step through them | 1 and 2 |

## Demo programs

The source folder also holds a few programs that are *not* numbered labs. They are handy for showing off a
kit at a science fair or a classroom open house.

| File | What it does |
|------|--------------|
| `auto-cycle.py` | Steps through sixteen light patterns automatically, repeating each one a few times |
| `main-demo-cycle.py` | Mode 0 cycles through all twelve patterns, five seconds each. Modes 1 to 12 each repeat one pattern. The buttons change the mode. |
| `main-old.py` | An older version of the demo program |

## Want more?

The [Additional Labs](../additional-labs/index.md) add one extra part, such as a potentiometer or a
photoresistor, so your Pico can sense the world around it.
