# Session Log: Tilt-a-Rainbow Kit

- **Date:** 2026-10-03 to 2026-10-04 (one continuous session, 38 prompts)
- **Model:** Claude Sonnet 5.5 (`claude-sonnet-5-5`), in Claude Code (Claude desktop app, Code tab). See [Model and token efficiency](#2-model-and-token-efficiency)
- **Repo:** `/Users/dan/Documents/ws/moving-rainbow` (branch `master`)
- **Deliverables:** `src/kits/16x16-matrix-accel/`, `docs/kits/16x16-matrix-accel/`, a new section in `docs/kits/moving-rainbow-base/purchasing-guide/index.md`, `artwork/thinking-spot/16x16-matrix.html`, and this log. The kit, docs and purchasing guide were committed and deployed (6 commits). A seventh commit, `a86b4f82`, pushed to GitHub (not deployed) the box cover, its cropped photo, your edits to the kit guide, your four new images, and the first version of this log. The final rename to "Tilt-a-Rainbow Kit" (prompt 38) and the log updates that go with it are **not** committed. The LinkedIn post text was only given in chat.

---

## 1. Outcome in one paragraph

A new classroom kit, **Tilt-a-Rainbow**: a Raspberry Pi Pico driving a 16x16 NeoPixel matrix (256 pixels, data on GPIO 0), a LIS3DH accelerometer on I2C0 (SDA GPIO 16, SCL GPIO 17), and two mode buttons (GPIO 14 and GPIO 15). It has 13 numbered MicroPython programs, a shared helper module and six mode modules (22 `.py` files, about 1,830 lines), one `config.py`, a wiring-diagram script, and an uploader. The programs climb from a blinking LED and a hardware probe, through pixel and X-Y labs and a tilt sensor, to a sloshing-water simulator, a 9-level generated tilt maze, and a 10-mode "mode machine" loaded by two buttons. Around the code sit a student guide plus 13 lab pages written for 6th graders (about 14,000 words, 15 simulator pictures, and a wiring diagram), a purchasing-guide section for the matrix, a printable box cover, and a LinkedIn announcement. **Verified on a real Pico by the user:** the I2C scan and the probe (`TEST PASS`), both buttons, accelerometer readings, the tilt bubble (after two fixes), the row/column sweep, the sloshing water, the tilt maze (levels 1 and 2 played), and the 10-mode program. **Not confirmed on hardware:** programs 04 to 07 (first pixel, fill colors, walk pixels, X-Y corners), levels 3 to 9 of the maze, and modes 1 to 8 individually.

### Results at a glance

| | Result |
|---|---|
| Programs | 13 numbered (`01`-`13`), plus `kit.py`, `bounce_dots.py`, `rain.py`, `rings.py`, `tilt_balls.py`, `sloshing_water.py`, `tilt_a_maze.py`, `config.py` |
| Source folder | 25 files, 22 `.py`, about 1,830 lines (including the 192-line wiring-diagram script that never goes on the Pico) |
| Docs folder | 14 pages (guide + 13 labs), about 14,000 words, 21 files in the image folder (15 simulator pictures, the wiring diagram as PNG and SVG, and four files you added: three photos and `box-cover.png`) |
| Light shows | 10 modes, 9 maze levels, 1 rainbow finish |
| Parts cost (estimate) | $25.50 for one kit |
| Commits | 6 (listed in section 4) |
| Lesson checker (skill's `check_lesson.py`) | 0 hard problems and 0 soft warnings on all 14 pages |
| Challenges on the pages | Every code-changing challenge was run under real MicroPython before it was printed |
| Site build | `mkdocs` exit code 0, no warnings from the new pages |

---

## 2. Model and token efficiency

All of the work in this log was done by **Claude Sonnet 5.5**. Dan's observation, which this log records as the author's note: **Sonnet 5.5 was VERY token efficient for this job.**

What I can back up with numbers is limited, and I will not invent more:

- The session's token counter is a **per-turn budget**. It reset to about 15,000,000 at the start of every prompt and counted down within the turn, so it cannot give one clean whole-session total.
- The heaviest turn was the documentation turn (prompt 25: 14 pages, 15 simulator pictures, a wiring diagram, a checker run on every page, a MicroPython test of every challenge, and a full site build). By the counter it used on the order of a couple hundred thousand tokens at most. Most other turns, including the three new programs with their tests, used a small fraction of that. These figures are approximate and were read off the counter during the session.
- Several things kept the cost down: embedding real code with `pymdownx.snippets` line ranges instead of retyping it, rendering pictures from the real program code instead of drawing them, using the repo's existing purchasing-guide prices instead of searching for all of them, and testing under a real MicroPython interpreter once instead of re-reasoning about syntax.

---

## 3. Prompts, verbatim, and how each was handled

Prompts are quoted exactly, typos included. Pasted console output is included in full.

### Prompt 1: the assignment (it arrived cut off)

> I have a new kit.  The hardware is a Pico with a 16x16 matrix on GPIO 0 and an accelerometer with SCK on GPIO17 and SDR on GPIO16.  There are two Mode buttons tied to GND on GPIO 14 and GPIO 5.  Please create a new kit at @src/kits/16x16-matrixs-accel with the right config.py file and a collection of

Handled by: read the base kit's `config.py`, `CODING-GUIDELINES.md`, an older matrix kit and the upload script. Created the folder, then noticed the message was cut off and said so. Read "SCK/SDR" as SCL/SDA.

### Prompt 2: the rest of the sentence (arrived mid-turn)

> a collection of test programs.

Handled by: wrote `config.py` and nine test programs (blink was added in prompt 4), a README, and the uploader. Assumed an MPU-6050 accelerometer at 0x68 because the repo had MPU-6050 sketches. That turned out to be wrong.

### Prompt 3

> MPY: soft reboot
> Found 0x19: LIS3DH accelerometer
> config.py ACCEL_ADDRESS is 0x68 but it was not found.

Handled by: switched `config.py` to 0x19 and rewrote the accelerometer programs for the LIS3DH (WHO_AM_I `0x33`, little-endian readings, 16384 counts per g).

### Prompt 4

> make 01 flash the on-board LED and 02 do a detailed probe like the other kits

Handled by: `01` became the base kit's blink program. The old `01`-`09` shifted to `03`-`10`. I first wrote an I2C probe as `02`, then (prompt 5) rewrote it.

### Prompt 5

> Here are some sample of probes: ls ../../../../stem-robots/src/kits/*/*probe.py
> ../../../../stem-robots/src/kits/9-dof-imu-display/01-probe.py	../../../../stem-robots/src/kits/compass-hmc5883l/01-probe.py
> ../../../../stem-robots/src/kits/9-dof-imu/01-probe.py		../../../../stem-robots/src/kits/imu-mpu6050/01-probe.py

Handled by: read the MPU-6050 and 9-DOF probes and `run-probe.sh`, then rewrote `02-probe.py` in that style: board info, pin levels, I2C scan without internal pull-ups, WHO_AM_I, a swapped-wires fallback, and a final `TEST PASS` or `TEST FAIL`. Added `run-probe.sh`.

### Prompt 6

> please use the mpremote to run the probe youself

Handled by: checked the Pico with a read-only `ls`, copied only `config.py` over (the old one had the wrong address), and ran `./run-probe.sh`. Result: `TEST PASS` (details in section 5).

### Prompt 7

> add program name and a version to all printing to the Thonny console

Handled by: added a one-line banner (`Test NN: Title (version X)`) to all 10 programs, built from each file's own header. A later attempt to confirm it on the Pico was blocked because Thonny held the serial port.

### Prompt 8

> Note BUTTON_PIN_2 = 15

Handled by: changed `config.py`, the probe's wiring comment and the README from GPIO 5 to GPIO 15. (I had flagged GPIO 5 as unusual in my first report.)

### Prompt 9 (pasted output, no other text)

> >>> %Run -c $EDITOR_CONTENT
>
> MPY: soft reboot
> Test 09: Accelerometer Print (version 1.0.0)
> WHO_AM_I: 0x33 (0x33 is a LIS3DH)
> x:  0.01  y:  0.02  z:  1.03
> x:  0.00  y:  0.01  z:  1.04
> x:  0.01  y:  0.02  z:  1.03
> x:  0.01  y:  0.02  z:  1.02
> x:  0.00  y:  0.02  z:  1.03
> x: -0.00  y:  0.02  z:  1.03
> x:  0.00  y:  0.02  z:  1.03
> x:  0.01  y:  0.02  z:  1.02
> x:  0.00  y:  0.02  z:  1.02
> x:  0.00  y: -0.03  z:  1.04
> x:  0.02  y: -0.02  z:  1.03
> x:  0.00  y:  0.02  z:  1.03
> x:  0.05  y:  0.03  z:  1.03
> x: -0.08  y: -0.01  z:  0.93
> x:  0.21  y: -0.08  z:  1.19
> x:  0.44  y: -0.18  z:  0.70
> x:  0.70  y: -0.18  z:  0.61
> x:  0.81  y: -0.17  z:  0.63
> x:  0.87  y: -0.20  z:  0.46
> x:  0.89  y: -0.17  z:  0.51
> x:  0.87  y: -0.18  z:  0.49
> x:  0.83  y: -0.19  z:  0.79
> x:  0.21  y: -0.21  z:  0.86
> x: -0.09  y: -0.18  z:  1.06
> x: -0.09  y: -0.17  z:  1.06
> x: -0.07  y: -0.29  z:  0.73
> x: -0.11  y: -0.76  z:  0.33
> x: -0.09  y: -0.83  z:  0.34
> x: -0.15  y: -0.74  z:  0.61
> x: -0.11  y: -0.35  z:  1.10
> x: -0.13  y: -0.38  z:  1.04
> x: -0.19  y: -0.27  z:  1.05
> x: -0.44  y: -0.13  z:  0.60
> x: -0.71  y: -0.16  z:  0.35
> x: -0.97  y: -0.01  z:  0.31
> x: -0.77  y:  0.05  z:  0.51
> x: -0.58  y:  0.30  z:  0.90
> x: -0.22  y:  0.64  z:  0.47
> x: -0.22  y:  0.72  z:  0.41
> x: -0.41  y:  0.74  z:  0.86
> x: -0.24  y:  0.42  z:  0.64
> x: -0.08  y:  0.15  z:  0.67
> x:  0.48  y:  0.07  z:  0.82
> x:  0.77  y: -0.01  z:  0.81
> x:  0.23  y: -0.01  z:  0.95
> x: -0.09  y:  0.04  z:  0.79
> x: -0.11  y:  0.16  z:  1.14
> x:  0.05  y:  0.12  z:  1.02
> x:  0.05  y:  0.00  z:  1.04
> x:  0.01  y:  0.01  z:  1.02
> x:  0.00  y:  0.03  z:  1.03
> x:  0.00  y:  0.02  z:  1.03
> x:  0.01  y:  0.01  z:  1.03
> x:  0.01  y:  0.01  z:  1.03
> x:  0.01  y:  0.01  z:  1.03
> x:  0.01  y:  0.01  z:  1.03
> x:  0.01  y:  0.02  z:  1.03
> x:  0.01  y:  0.02  z:  1.02
> x:  0.02  y:  0.02  z:  1.02
>
> ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
> Traceback (most recent call last):
>   File "<stdin>", line 42, in <module>
> KeyboardInterrupt:
>
> MPY: soft reboot
> MicroPython v1.29.0 on 2026-08-24; Raspberry Pi Pico with RP2040
> Type "help()" for more information.
> >>>

Handled by: read it as proof that the banner, the LIS3DH identity and all three axes work. Flat, z reads 1.03 g. Tilting swung x to +0.89 and -0.97 and y to about -0.83 and +0.74. Pointed the user to program 10's flip settings.

### Prompt 10

> Here is run of 10.  When I tilt the board towards me the cyan squares move toward the top edge (back of the matrix).  When I tip left and right the squares separate right and left.  When I tilt the board backwards (back edge down and front edge up). the squares move toward the  the front edge of the board.

Handled by: diagnosed two bugs. (1) The 2x2 dot split into two halves going opposite ways, which means the code assumed a zig-zag panel but the panel runs every row left to right, so `SERPENTINE = False`. (2) The dot moved to the high side, but the header promised the low side, so `FLIP_Y = True`.

### Prompt 11

> Perfect!  As I tilt left and right the four lit pixels tilt left and right correctly.

Handled by: confirmed the flips (`FLIP_X False`, `FLIP_Y True`, `SWAP_XY False`) and `SERPENTINE = False` as correct. Listed what was still unconfirmed (programs 04 to 07).

### Prompt 12 (pasted output)

> The button test works perfectly:
>
> MPY: soft reboot
> Test 03: Button Test (version 1.0.0)
> Press each button. Press Ctrl-C to stop.
> Button 1 (GP14): pressed
> Button 1 (GP14): released
> Button 1 (GP14): pressed
> Button 1 (GP14): released
> Button 1 (GP14): pressed
> Button 1 (GP14): released
> Button 2 (GP15): pressed
> Button 2 (GP15): released
> Button 2 (GP15): pressed
> Button 2 (GP15): released
> Button 2 (GP15): pressed
> Button 2 (GP15): released

Handled by: noted that this also confirmed the `BUTTON_PIN_2 = 15` change on the real board.

### Prompt 13

> PY: soft reboot
> Test 08: Row and Column Sweep (version 1.0.0)
>
> I see the rows and columns being drawn correctly

Handled by: took it as proof that the `xy()` mapping and `SERPENTINE = False` are right. Listed 04 to 07 as the remaining unconfirmed programs.

### Prompt 14

> publish now

Handled by: committed the kit, pushed, and ran `mkdocs gh-deploy`. Commit `dfe15b3f`.

### Prompt 15: the sloshing water

> add a new program 11-sloshing-water.py that will simulate sloshing water in a pan.  Use blue for the water.  Tilting the board vertical should fill 1/2 the pixels.  If I rotate the board back while it is on it's side,, rocking it back and and forth slightly the water should appear to be sloshing back and forth like it is in a flat square container.

Handled by: wrote `11-sloshing-water.py` (design decisions D14 to D17). Tested the pixel count at every tilt and the spring behavior on the host before handing it over.

### Prompt 16

> very nice!

Handled by: offered to publish.

### Prompt 17

> publish now

Handled by: committed `11-sloshing-water.py` and the README row. Commit `6da2f3ba`.

### Prompt 18: the tilt maze

> please create a new "12-tilt-a-maze.py".  In this program you draw a maze using light blue,  A ball is a red pixel in one corner of the maze.  A finished hole is a green pixel in the opposite corner of the maze.  Start with a simple maze, and slowly make the maze slightly harder each level.  Draw "L1" before the first level and draw "LN" for level "N" from 1 to 9.  Draw a colorful rainbow when the user finishes level 9.
> Note that pixel 0 is in the upper left corner.  Place the red ball there for L1.

Handled by: wrote `12-tilt-a-maze.py` (design decisions D18 to D24), chose the maze seeds with a host search, and played all nine levels with a scripted tilt before handing it over.

### Prompt 19

> L1 worked great, but The program froze at the start of L2.

Handled by: investigated. All nine mazes build and every level plays through on a regular Python host, so I got a real MicroPython interpreter (in a throwaway conda environment in the scratch folder) and ran the maze builder and the text drawing for every level there as well. Everything passed. The user then interrupted.

### Prompt 20

> [Request interrupted by user]
> My error!  I was looking at the wrong dot.  It is working fine now.

Handled by: no code change. The ball starts in the upper-right on level 2 (the corner rotates each level), so it is easy to follow the wrong dot. Kept the extra verification.

### Prompt 21

> publish now

Handled by: committed `12-tilt-a-maze.py` and the README row. Commit `ea5d10f6`.

### Prompt 22: the mode machine

> add a new program 13 that uses the mode buttons to load different modes.  The first mode=1  just draws a single colorful  pattern of slowly moving dots using three pixels, one red, one green and one blue that appear to bounce around the matrix.  A boring pattern. When the user presses the GPIO 14 button move to the next mode = 2.  This pattern is a little more fun.  More colors, and a slightly faster pattern.  Use seven colored pixels.
> Mode=3 is much more complicated, as you use more colors and the colors leave small trails of their color. 
>
> Continue with two additional modes 4 and 5 that just use more patterns, but do not use the tilt.
>
> Next, create a mode 6 that has a single blue pixel that moves when you tilt the board.  Then create mode 7 that has three dots (red, green and blue) that all bounce around as the board tilts.
>
> Mode 8 is seven different colors of dots that all bounce around according to the tilt of the board.
>
> Mode 9 is the slosh mode you did in lab 11 (11-sloshing-water.py) and mode 12 is the 12-tilt-a-maze.py).
>
> You might have to refactor some of the demos so they are in modules that are dynamically loaded.

Handled by: wrote `13-modes.py` and eight modules (design decisions D25 to D33). Read "mode 12" as mode 10. Refactored programs 11 and 12 into modules and made them thin wrappers. Tested every mode, the button handling and the mode manager under real MicroPython.

### Prompt 23

> perfect!

Handled by: offered to publish.

### Prompt 24

> publish

Handled by: committed program 13 and the modules. Commit `1736e977`.

### Prompt 25: the documentation

> Now please use the following skill ../../../../learning-micropython/skills/project-kit-generator/ to create step-by-step documentation for this project.  Assume the reader is a 6th grand 11-year old student that is just learning Python.

Handled by: read the skill and the repo's content guide, then wrote a kit guide and 13 lab pages (design decisions D34 to D45). Rendered pictures from the real code, drew a wiring diagram with the repo's house-style skill, and checked every page.

### Prompt 26

> use the pixel warning admonitions for the warnings

Handled by: added the Pixel warning picture to all five warning boxes (three on the guide, one in Lab 4, one in Lab 5), using the base kit page's markup.

### Prompt 27 (arrived mid-turn)

> publish

Handled by: before publishing, checked that all 78 images in the built pages resolve. Committed the docs and diagram script, and pushed. Commit `eaaf5181`. The first `mkdocs gh-deploy` failed at the final push of `gh-pages`; the retry succeeded.

### Prompt 28

> add the nav entries to mkdocs.yml

Handled by: added an Intro entry and 13 lab entries after the Rotary Spinner Box, in the same style. Checked that all 14 files exist and that the rendered sidebar shows them. Left the `watch:` list alone and offered it.

### Prompt 29

> Please rename the two directories to fix a typo I made.  Change the dir name "16x16-matrixs-accel" to be "16x16-matrix-accel" in both the @docs/kits and the @src/kits

Handled by: `git mv` on both folders, then replaced the old name in 15 files (nav, docs, embedded program paths, GitHub links, the diagram script). Confirmed zero remaining references, then rebuilt and spot-checked embeds.

### Prompt 30

> in the @docs/kits/16x16-matrix-accel/#kit-contents there is a table of parts.  Change the column name "How Many" to be "Approximate Cost" and then put the cost in that column.  Add one row for total cost at the end of the table and sum the total part cost.  Just put (QTY=2) on the button row.

Handled by: no prices were given, so I used the repo's own purchasing-guide prices where they existed and a web search for the matrix and sensor (D46). Total $35.50 at first (matrix $20).

### Prompt 31

> Please add a section on 16x16 matrix to @docs/kits/moving-rainbow-base/purchasing-guide and use this image @docs/img/16x16-matrix-on-aliexpress.png which has a price of $7.25. from AliExpress.  Provide sample search string URLs for eBay, AliExpress and Amazon.

Handled by: added a "16x16 NeoPixel Matrix" section after the LED strip section, in the guide's own format, and a line in its Optional parts list (D47 and D48).

### Prompt 32

> Yes, make the approximate cost be $10 for the 16x16 matrix but then put a link to the purchasing guide in the table of parts.

Handled by: matrix $10.00, total $25.50, and the part name now links to the new purchasing-guide section.

### Prompt 33

> publish

Handled by: one commit containing the rename, nav, cost table, purchasing guide and screenshot. Commit `a144319c`. (My first `git add` failed on a path that no longer existed; I restaged only paths that exist.)

### Prompt 34: the box cover

> Now please generate a new box cover for this kit.  You will find a sample for the base kit at @artwork/thinking-spot/box-cover.html but call this the file 16x16-matrix.html. You will find a photo of the kit at @docs/kits/16x16-matrix-accel/img/16x16-matrix-tilt-kit.jpg
>
> Please come up with a fun name for the kit that describes the fun tilt feature

Handled by: named the kit **Tilt-a-Rainbow** and built `artwork/thinking-spot/16x16-matrix.html` (design decisions D49 to D52).

### Prompt 35

> please generate a LinkedIn annoncement about this fun new project.  I love the Tilt and Rainbow title!

Handled by: followed the repo's LinkedIn guide: three variations, link only in a UTM-tagged first comment, 11 to 12 hashtags, and an AI-transparency line (design decision D53).

### Prompt 36 (this log)

> Please create a detailed session log of your wonderful work creating this really fun kit.  Put the log file in logs/tilt-a-rainbow-kit.md - Make sure you include every one of my prompts as well as describe all the design decisions you made to create this fun kit.  Note that the Sonnet 5.5 model was used and it is VERY token efficient.

Handled by: this file.

### Prompt 37

> push to GitHub

Handled by: checked that all seven pending items belonged to this work (your guide edits, your four new images, the box cover and its cropped photo, and the log), committed them by explicit path, and pushed. Commit `a86b4f82`. Did not run `mkdocs gh-deploy`, because only GitHub was asked for, and said the live site was therefore still the older version.

### Prompt 38

> Change all the names to be "Tilt-a-Rainbow"

Handled by: searched the repo for every name the kit had gone by and made them one name, **Tilt-a-Rainbow Kit**: the nav entry in `mkdocs.yml`, the kit guide's front matter title and heading, two links in the purchasing guide, the kit README heading, the `config.py` header comment, the diagram script's docstring and title, and the wiring diagram itself (PNG and SVG regenerated, same layout). The box cover and the posts already used it. See D54.

---

## 4. Work timeline

| When | Step |
|------|------|
| 2026-10-03 | Read the repo's conventions. Created the kit folder, `config.py`, and nine test programs assuming an MPU-6050 |
| | Scan showed a LIS3DH at 0x19. Rewrote the accelerometer programs. Added `01` blink and a stem-robots-style `02` probe |
| | Ran the probe on the Pico with `mpremote`: `TEST PASS`. Added the name-and-version banners |
| | User fixed `BUTTON_PIN_2 = 15`, then tried 03, 08, 09 and 10. Fixed `SERPENTINE` and `FLIP_Y` |
| 21:51 | **Commit `dfe15b3f`**: the kit with hardware test programs |
| 21:59 | **Commit `6da2f3ba`**: `11-sloshing-water.py` |
| 22:13 | **Commit `ea5d10f6`**: `12-tilt-a-maze.py` |
| | User reported a "freeze" at level 2, which turned out to be a wrong-dot misread |
| 22:42 | **Commit `1736e977`**: `13-modes.py` with `kit.py` and six mode modules; programs 11 and 12 became wrappers |
| | Read the project-kit-generator skill and the repo's content guide. Rendered 16 pictures (one unused one was deleted later, leaving 15), drew the wiring diagram, wrote 14 pages, ran the checker, tested every challenge, built the site |
| 23:07 | **Commit `eaaf5181`**: the student documentation |
| 2026-10-04 | Added nav entries, renamed both folders, added the cost table and the purchasing-guide section |
| 07:20 | **Commit `a144319c`**: rename, nav, cost table, purchasing guide |
| | Cropped the kit photo, built the QR code, wrote the box cover and checked it in a browser |
| | Wrote the LinkedIn posts and the first version of this log |
| | **Commit `a86b4f82`**: box cover, photos, guide edits and log, pushed to GitHub (not deployed) |
| | Renamed every name for the kit to "Tilt-a-Rainbow Kit" and regenerated the wiring diagram |

---

## 5. What I found while reading (facts the design depends on)

1. **The repo has strict program conventions.** `CODING-GUIDELINES.md` requires `import config`, settings copied into same-named variables at the top, a three-line header (`Lab NN: Title`, `Filename`, `Version`), and "write once per step, then sleep". The base kit's `01` runs before `config.py` exists, so it does not import it. All of this shaped the programs.
2. **No power cap existed for a 256-pixel panel.** The docs gave a rule of thumb (160 color units across 30 pixels draws about 377 mA, so about 0.0785 mA per unit). At that rate all 256 pixels at full white need over 15 amps and USB supplies about 0.5. This drove `LEVEL = 8` in `config.py` (white at 8 draws about 480 mA).
3. **The older matrix kit used a compass, not an accelerometer.** `neopixel-matrix-motion` has a GY-273 on the same two pins. That is why I did not trust any chip name, and why the probe identifies the chip by its WHO_AM_I register.
4. **GPIO 16 and 17 are a valid I2C0 pair.** GPIO 16 can only be SDA and 17 only SCL. The probe's comments say so, and a swapped-wires fallback uses `SoftI2C`.
5. **The repo's mascot is Pixel (they/them), not "Monty".** The project-kit-generator skill was written around a different repo's mascot. The repo's own `CONTENT-GENERATION-GUIDE.md` wins, so all student pages use Pixel.
6. **Two guides disagree on Pixel count.** The guide says at most twice per page, but the user asked for Pixel warning boxes, which put five on the kit guide. I followed the user.
7. **The existing purchasing guide had prices** for the Pico ($3.99), breadboard, buttons, wire and cable, and a house format for each part (photo, prep work, cost, search keywords, three "where to buy" links).
8. **A real MicroPython interpreter is available cheaply.** `conda install micropython` into a throwaway environment in the scratch folder gave a unix build, so tests could run under the real language and not only CPython.

### Commands run against real hardware

| Command | Effect on the Pico |
|---|---|
| `mpremote connect auto ls` | Read-only. Listed the older files on the Pico |
| `mpremote connect auto cp config.py :config.py` | **Wrote one file**: replaced the Pico's old `config.py` (which had the wrong accelerometer address) with the new one |
| `./run-probe.sh` (runs `02-probe.py` via `mpremote run`) | Ran the probe from the computer. It sets two sensor control registers and reads values. Wrote no file |
| `./upload-code.sh --clean` | **Never run.** It erases the Pico, so I only described it |

Later attempts to reach the Pico failed because Thonny held the serial port. Nothing else was written to the device. The old numbering's files were left on the Pico and the user was told.

---

## 6. Design decisions and why

### Hardware and configuration

**D1. One `config.py` holds every pin and setting.** It carries the matrix pin, width, height and pixel count, a `SERPENTINE` flag, `LEVEL`, both button pins, and the accelerometer's I2C id, pins and address. The alternative was hard-coding pins in each program. One file means a different wiring needs one edit, matching the base kit.

**D2. The accelerometer address is a setting, and the probe finds it for you.** After the 0x68 mistake, the probe checks the configured address, then the two real LIS3DH addresses, and prints the line to change if they differ.

**D3. `SERPENTINE = False`.** Many 16x16 panels zig-zag, so I assumed `True`. The user's description of the dot "separating" showed the panel runs every row left to right. The programs still support both layouts through the same `xy()` function, and Lab 6 teaches students to tell which they have.

**D4. `LEVEL = 8` is a safety cap, not a style choice.** It is the largest color number that keeps a fully lit panel near USB limits (about 480 mA for white). Programs that light only a few pixels use bigger numbers. The alternative was a hardware brightness limiter in `kit.py`; I kept it as a visible number so Lab 5 can teach the math.

**D5. Buttons use the Pico's internal pull-ups, with the other side to GND.** Pressed reads 0. This matches the base kit and needs no resistors.

**D6. Sensor setup is two register writes and one burst read.** `CTRL_REG1 = 0x57` (100 readings a second, x y z on), `CTRL_REG4 = 0x88` (high resolution, plus or minus 2 g, steady readings), then a 6-byte read from `0x28 | 0x80` unpacked as `'<hhh'` and divided by 16384 per g. I used raw registers and no driver library, so students can see every step and no library has to be installed.

**D7. `FLIP_Y = True`, with `FLIP_X` and `SWAP_XY` kept as visible constants.** The mounting direction of the sensor cannot be known from the code, so the three flips are easy-to-find constants. The user's tilt descriptions fixed the values, and the same three constants appear in programs 10, 11 and 12 and in `kit.py`.

### The test ladder

**D8. Numbered programs that each test one thing.** `01` blink, `02` probe, `03` buttons, `04` first pixel, `05` fill colors, `06` walk pixels, `07` X-Y corners, `08` row/column sweep, `09` accelerometer print, `10` accelerometer bubble. Each part is proven alone before parts are combined, so a later failure already points at the broken part.

**D9. `01` is a copy of the base kit's blink program.** It runs before `config.py` is on the Pico, as in the base kit. It is the first proof that Python and Thonny work.

**D10. The probe copies the stem-robots probes' structure.** Board info, pin checks with pull-ups, a scan without pull-ups (to test the sensor board's own), WHO_AM_I, a swapped-SDA/SCL fallback, then `TEST PASS` or `TEST FAIL` with a reason per failure. I added button checks, register read-back, and ten readings that check about 1 g total and a steady spread. It uses `import config` for pins, unlike some of the originals. The alternative was keeping the I2C-only scan, which could not catch a stuck button or a moving board.

**D11. Every program prints its name and version at start.** The user asked for it. I built each banner from the file's own header and placed it after the imports, so even programs that otherwise print nothing show what is running.

**D12. Programs 04 to 08 each create their own `NeoPixel` object.** They are small teaching programs that run on their own. The shared `kit.py` came later, for the modes, so the early labs stay simple.

**D13. Each program was syntax-checked with `py_compile`, then run under stand-ins.** This caught issues before the user touched the board.

### Sloshing water (program 11)

**D14. The matrix is a square pan seen from the side, and exactly half the pixels are water.** Tilting must change the shape, never the amount. The brief says half the pixels when the board is upright.

**D15. Sorting finds the water line.** Each pixel gets a "depth" (how far downhill it sits). Sorting all 256 depths and taking the one at position 128 as the cutoff always lights exactly 128 pixels. The alternatives were solving for the line analytically, which has awkward corner cases when it tilts, or simulating particles, which would cost far more on a Pico. A tiny per-pixel "nudge" breaks ties so a straight upright surface never lights 127 or 129.

**D16. A damped spring makes the slosh.** The water's idea of "down" follows gravity like a weight on a rubber band: `SPRING = 90` (about 1.5 slosh per second) and `DAMPING = 2.5`. The test showed a 30 degree tilt overshoots to about 47 degrees and rings several times. Docs tell students which number to change for a faster or longer slosh.

**D17. When the board is nearly flat, the water stays where it was.** Below `MIN_TILT = 0.2 g` there is no meaningful "downhill", and chasing noise would make the surface twitch. Hard shakes are clamped to 1.5 g.

### Tilt maze (program 12)

**D18. The maze is built from an 8x8 grid of cells, one pixel per cell, with a wall pixel between.** Cell `(cx, cy)` lives at pixel `(2*cx, 2*cy)`, and the last row and column act as the right and bottom walls. The ball starts at pixel 0, as asked. The alternative of a free-form pixel maze cannot guarantee a path.

**D19. A depth-first "wander and back up" recipe guarantees one way through.** It visits every cell once and leaves a single route between any two. Students can follow it, and it is a real algorithm worth naming.

**D20. Levels get harder by removing fewer shortcuts.** After building the one-route maze, level 1 knocks out 40 more walls and level 9 knocks out none (`EXTRA_OPENINGS = [40, 30, 22, 16, 11, 7, 4, 2, 0]`). This is the "slightly harder each level" the user asked for.

**D21. Each level has a fixed seed, chosen by a host search.** I measured the shortest route for 1,500 seeds per level and picked seeds so the route grows steadily: 28, 32, 36, 40, 48, 56, 72, 84, 100 steps (`MAZE_SEEDS = [1, 87, 194, 108, 499, 236, 7, 701, 95]`). The same level is the same maze every time, which a classroom can use ("who finished level 7?"). Random mazes would sometimes hand out a level 2 harder than level 5.

**D22. A tiny random-number maker with a seed.** I used `state = (state*75 + 74) % 65537`, which uses only small integers, so it gives identical numbers in regular Python and on the Pico, which let the host search choose seeds for the real code.

**D23. The ball moves one pixel at a time, faster when you tilt farther.** The step delay runs from 260 ms (gentle) to 90 ms (hard). It tries the strongest direction first and then the other, so the ball slides along a wall and never sticks to it. Pushing into a wall does nothing (tested 39 times).

**D24. Level titles use a 3x5 pixel font scaled 2x, and the finish is a seven-band rainbow arch.** "L1" to "L9" fit the 16x16 panel with margins. The rainbow is drawn as bands by distance from the bottom-middle, then colors rotate outward for about nine seconds before the game restarts. Colors are kept dim so the arch stays near 340 mA.

### The mode machine (program 13)

**D25. Each mode is a module with `run(settings)`, loaded only when selected.** `13-modes.py` calls `__import__(name)`, runs the mode, and on the way out deletes the module from `sys.modules` and calls `gc.collect()`. The user asked for modules that load dynamically, and this keeps only one show in memory on a Pico with about 230 KB of RAM. The free RAM is printed each time a mode loads.

**D26. A button press ends a mode with an exception.** `kit.wait(ms)` sleeps in 10 ms pieces and checks the buttons between them. When one is pressed it raises `ModeChange(1)` or `ModeChange(-1)`, and the manager catches it. The alternative was every mode polling a flag and returning, which would have meant changing every loop (including the maze's blocking pauses). The exception ends a mode from anywhere, even mid-title.

**D27. Button 1 is next, Button 2 is previous, and both wrap around.** The user defined only Button 1 on GPIO 14. A previous-mode button is the natural use of the second one. A 200 ms debounce counts a press once, and holding a button does not repeat.

**D28. The maze is mode 10, not 12.** The user wrote "mode 12 is the 12-tilt-a-maze". The next number after the slosh mode (9) is 10, so I used 10 and flagged it. Mode numbers are just list order in `MODES`.

**D29. Modes share engines.** Modes 1 to 3 use `bounce_dots.py` with different settings (three slow dots; seven faster dots; twelve colors with a fade trail). Modes 6 to 8 use `tilt_balls.py` (one, three or seven balls). Fewer files, and the settings dictionary shows students how one module can behave three ways.

**D30. I chose the two unspecified no-tilt modes.** Mode 4 is rainbow rain (drops fall with fading tails) and mode 5 is ripple rings (circles spread and fade). Both are cheap to draw and clearly different from bouncing dots.

**D31. Tilt balls bounce off each other.** With no collisions, seven balls under steady tilt would all pile into one pixel and vanish. Overlapping balls push apart and trade speed, so a tilt gives seven separate dots. Tested: the lit-pixel count never dropped below the ball count.

**D32. Programs 11 and 12 became thin wrappers.** The code moved into `sloshing_water.py` and `tilt_a_maze.py` (same logic, now using `kit.py` and `kit.wait`). The wrappers keep the lab numbers and run on their own; versions went to 1.1.0. One copy of each program means no drift. The cost: the early run-from-Thonny habit now needs the modules on the Pico, which the docs and the guide's file table explain.

**D33. A flat folder.** All modules sit next to the numbered programs so `upload-code.sh` (which copies `*.py`) needs no change beyond skipping the diagram script. The mode number is also drawn on the matrix for 0.7 seconds on every switch, so students can tell which mode they are in without a console.

### The documentation (prompt 25)

**D34. A kit guide plus one page per program.** The repo already documents multi-lab kits this way (the Rotary Spinner Box), and a 6th grader needs small steps. The guide covers parts, wiring, the pin map, uploading, power safety and troubleshooting. A single long lesson page was the skill's default, but 13 programs made one page too long.

**D35. The repo's content guide governs, and the skill's guidance fills gaps.** I adopted the guide's section order (welcome, learn, need, body, try it, check understanding, celebration, what's next), its Pixel rules, and its short sentences (20 words or fewer). From the skill I took numbered hardware steps, a pin table, one idea per example, tested challenges, honest captions, and the lesson checker.

**D36. Real code is embedded, never retyped.** Short programs use `--8<--` with the whole file. Longer ones use line ranges (`file:start:end`), which cannot drift from the source. I opened a rendered page to confirm the excerpts matched.

**D37. Console output blocks use real runs where one exists.** Lab 3 and Lab 9 use the user's pasted output. The probe's excerpt comes from the real run, edited only for the GPIO 15 change. Others describe what to see.

**D38. Pictures come from the real code.** I ran the programs and modules under stand-ins and drew each of the 256 LEDs as a glowing dot: level titles, pixel numbers, corners, row and column sweeps, the bubble, water upright and tilted, three mazes, the rainbow, and a contact sheet of all ten modes. Every caption says it was drawn by a simulator. I opened the images to check them, since numbers cannot show an ugly picture.

**D39. A wiring diagram in the repo's house style.** Using the circuit-diagram skill: red power rail on top, black ground on the bottom, amber signals, straight horizontal signal wires. Pins come from `config.py`. I put 3V3 on the Pico's right side so its wire to the sensor is a straight run. I widened two blocks after seeing a title collide with a pin label.

**D40. Wiring power is an assumption.** The user gave signal pins only. I drew the matrix on 5 V from VBUS and the sensor on 3V3, the safe default and the same as the base kit. This is flagged in every report as the one thing to check.

**D41. Warnings use Pixel's warning picture.** The user asked for it (prompt 26). It raises the Pixel count on the kit guide beyond the repo guide's limit, which I flagged.

**D42. Every challenge on a page was run before it was printed.** The double blink, the yellow pixel, the four loop ranges in Lab 6, the center pixel, the diagonal, the serpentine corner swap, the diagonal sweep, the 3x3 bubble at extreme tilts, the quarter-full pan, `LAST_LEVEL = 3`, and the new `color_cycle.py` mode all ran under MicroPython.

**D43. Reading level is checked mechanically, with a stated limit.** The skill's checker enforces sentence length, banned words, acronym expansion and image alt text. It does not compute a Flesch-Kincaid score, so I cannot claim a measured grade level. I rewrote every flagged long sentence.

**D44. A clean site build and a path check.** I built to a scratch folder (so no `.cache` appeared in the repo) and checked that all images resolve. The skill's build script needed two symlinks (`theme` and `src`) for this repo's relative paths.

**D45. The folder name was fixed on request.** The typo `matrixs` was in the folder name, the nav, embedded paths and links, so I replaced it everywhere in one pass and confirmed no copies remained.

### Cost and purchasing

**D46. The cost table uses repo prices first.** Pico, breadboard, buttons, wire and cable come from the base kit's purchasing guide. The matrix and sensor came from a web search (eBay and retailer listings for the matrix; Adafruit and others for the LIS3DH). The user then set the matrix at $10 (between the $7.25 sale and the roughly $15 regular price), giving a $25.50 total.

**D47. The purchasing section is honest about the sale.** The AliExpress screenshot says "one-time offer: applies to one item only" and the sale ends in days, so the section budgets about $15 per panel (about $295 for 20) and says so. It also warns that panels differ in row direction and may ship as bare boards. I removed a sentence of my own that was only true at the regular price.

**D48. Search links follow the guide's format.** One string, three marketplaces, built like the existing links. I did not open them.

### The box cover and the announcement

**D49. The name is Tilt-a-Rainbow.** It borrows the Tilt-a-Whirl ride and keeps the "Rainbow" brand. The tagline "Tip it. Roll it. Slosh it!" lists the three tilt tricks. Alternates offered: Wobble Lights, Tip & Tumble, Slosh & Roll.

**D50. The cover keeps the sample's skeleton and puts the real photo first.** Same 6x4 card, two per sheet, logo, rainbow corner, colored chips, Pixel, URL and QR. The new parts are a rainbow-framed kit photo and a "Let's light this up!" bubble.

**D51. Fourteen chips, and only things the kit does.** For example "256 Addressable RGB LEDs", "Tilt-a-Maze: 9 Levels", "13 Step-by-Step Labs". I left out "No Soldering Required" because I did not know whether the matrix needed wires soldered on.

**D52. The photo is a derived copy.** The original is 5712 pixels wide. A cropped 1100 px copy (280 KB) sits next to the cover, and the original is untouched. The QR code goes to the kit's lesson page and was decoded back from the rendered cover with macOS's QR detector.

**D53. The LinkedIn post follows the user's own guide.** Three lengths, no link in the body, a UTM-tagged link in the first comment, and 7 to 12 hashtags. It states plainly that Claude Code helped write the programs, tests and lessons.

**D54. One name, "Tilt-a-Rainbow Kit", with the hyphens.** The kit had picked up three names: "16x16 Matrix Accelerometer Kit" (my first README), "16x16 Matrix Tilt Kit" (my guide and nav) and "Tilt a Rainbow Kit" (your edit). I used your hyphenated form, since you asked for "Tilt-a-Rainbow", and kept "Kit" as the plain noun the base kit's pages also use. The wiring diagram carries its title inside the picture, so it was regenerated rather than left stale. I kept the folder and file names (`16x16-matrix-accel`, `16x16-matrix.html`) because they describe the hardware and renaming them would break links and the uploader. Lab 12's maze keeps the name Tilt-a-Maze.

---

## 7. Files

| File | Status | Notes |
|------|--------|-------|
| `src/kits/16x16-matrix-accel/config.py` | committed | Pins, size, layout, `LEVEL`, address |
| `.../01-blink-onboard-led.py` to `10-accel-bubble.py` | committed | Test programs (01 blink, 02 probe, 03 buttons, 04 to 08 pixel labs, 09 and 10 sensor labs) |
| `.../11-sloshing-water.py`, `12-tilt-a-maze.py` | committed | Thin wrappers (version 1.1.0) |
| `.../13-modes.py` | committed | The mode manager (10 modes) |
| `.../kit.py` | committed | Shared helpers: matrix, sensor, buttons, colors, font, `wait()` |
| `.../bounce_dots.py`, `rain.py`, `rings.py`, `tilt_balls.py` | committed | Mode engines |
| `.../sloshing_water.py`, `tilt_a_maze.py` | committed | The two programs as modules |
| `.../circuit-diagram.py` | committed | Draws the wiring picture on a computer; skipped by the uploader |
| `.../run-probe.sh`, `upload-code.sh`, `README.md` | committed | Helpers and the kit README |
| `docs/kits/16x16-matrix-accel/index.md` and `01-` to `13-*.md` | committed (`eaaf5181`; your later edits to the guide were committed in `a86b4f82`) | Guide plus 13 labs. Your later edit to `index.md`: front matter, the page title changed to "Tilt a Rainbow Kit", the box cover and kit photo at the top, a back-of-board photo in Step 2, and a LIS3DH photo in Step 3. I did not make or revert these |
| `docs/kits/16x16-matrix-accel/img/` | committed | 21 files: 15 simulator pictures, the wiring diagram (PNG and SVG), and four files the user added (the kit photo, a LIS3DH photo, a back-of-board photo, and `box-cover.png`) |
| `docs/kits/16x16-matrix-accel/img/16x16-matrix-tilt-kit.jpg` | the user's file | Not touched; not part of my commits |
| `docs/kits/moving-rainbow-base/purchasing-guide/index.md` | committed | New 16x16 matrix section |
| `docs/img/16x16-matrix-on-aliexpress.png` | committed | The user's listing screenshot |
| `mkdocs.yml` | committed | 14 nav entries |
| `artwork/thinking-spot/16x16-matrix.html` | committed (`a86b4f82`) | The box cover |
| `artwork/thinking-spot/16x16-matrix-kit-photo.jpg` | committed (`a86b4f82`) | Cropped copy of the kit photo |
| `logs/tilt-a-rainbow-kit.md` | committed (`a86b4f82`), since updated | This file |

### Wiring summary

| Part | Pin | Pico |
|---|---|---|
| Matrix DIN | GP0 | pin 1 |
| Matrix 5 V (assumed) | VBUS | pin 40 |
| Matrix GND | GND | pin 38 |
| Accelerometer SCL | GP17 | pin 22 |
| Accelerometer SDA | GP16 | pin 21 |
| Accelerometer VIN (assumed) | 3V3 (OUT) | pin 36 |
| Accelerometer GND | GND | pin 23 |
| Button 1 | GP14 to GND | pin 19 |
| Button 2 | GP15 to GND | pin 20 |

---

## 8. Verification

### Method

- **On the real Pico (by the user, and one run by me):** the probe, program 03, program 08, program 09, program 10, program 11, program 12 (levels 1 and 2), and program 13.
- **Under stand-ins on a computer:** every program was run with fake hardware (a fake clock, fake pins, a fake strip, a scripted tilt). A real MicroPython interpreter (unix build, in a throwaway conda environment) ran the maze builder, all 10 modes, the button debounce, the mode manager, and every challenge on the pages.
- **Searches and solvers:** a breadth-first search solved every maze and measured route lengths; a seed search picked the seeds; a scripted tilt that follows the solution played all nine levels, with and without the title screens, and the rainbow.
- **Docs:** the skill's lesson checker on all 14 pages, a clean MkDocs build, a check that every image in the built pages resolves, and screenshots of rendered pages.
- **Box cover:** rendered in headless Chrome at normal and double size, and the QR code decoded with macOS CoreImage.

### Results

| Check | Result |
|-------|--------|
| Probe on the Pico | `TEST PASS` (LIS3DH at 0x19, WHO_AM_I `0x33`, about 1.02 g, spread 0.042 g) |
| Buttons on the Pico | Press and release for both, GP14 and GP15 |
| Tilt on the Pico | Flat: z 1.03 g; tilting reached about plus 0.89 and minus 0.97 on x and about minus 0.83 and plus 0.74 on y |
| Bubble, slosh, maze, modes on the Pico | User reported each working ("perfect", "very nice", "L1 worked great") |
| Water pixel count | Exactly 128 lit at every tilt from 0 to 180 degrees |
| Maze levels | All nine solvable; shortest routes 28, 32, 36, 40, 48, 56, 72, 84, 100 |
| All 10 modes under MicroPython | Ran without error; tilt dots stayed separate; peak power at most about 340 mA |
| Mode manager | Visited 1 to 10, wrapped to 1, then went back (10, then 9) |
| Button debounce | Off means ignored; held button fires once; a bounce is ignored |
| Page challenges | All passed (the one apparent failure was my test asking for 8 colors from a 7-color cycle) |
| Lesson checker | 0 hard, 0 soft on all 14 pages |
| Built site | Exit code 0, no new warnings; 78 images resolve |
| Kit guide after your edits | Build still exit code 0, no warnings. The lesson checker now reports **4 hard problems**: the four images you added (`box-cover.png`, `16x16-matrix-tilt-kit.jpg`, `wires-on-back.jpg`, `lis3dh-on-breadboard.jpg`) have no alt text. Its 3 soft warnings come from the new front-matter lines, not the prose. I did not change your additions |
| QR code on the cover | Decoded to the kit page URL, which returns HTTP 200 |

### What this does not prove

- **Programs 04 to 07 on real hardware.** Their headers say "Not yet tested on hardware" and the user never reported them. Many headers still say so even for programs the user has run; none were updated.
- **Maze levels 3 to 9 and modes 1 to 8 as individual shows on the Pico.** The user reported the maze and the mode machine working overall, and everything else was tested on a computer.
- **Real timing, memory and flicker.** Frame speed, the real free RAM per mode, and the feel of the tilt controls are only known from the user's reports. The stand-in clock only advances in `sleep` and `wait`.
- **The power wiring.** The 5 V and 3.3 V pins in the guide are my assumption, and power draw (about 480 mA worst case) is an estimate from a rule of thumb, not a meter reading.
- **Reading level.** The checker measures sentence length and vocabulary rules, not a grade score. No 6th grader has used the pages.
- **The cover on paper.** I looked at it on screen and decoded the QR from a screenshot. I did not print it or scan it with a phone.
- **Prices and links.** Costs are single-kit estimates from October 2026. The search links use the guide's existing formats and I did not open them.

---

## 9. Mistakes and corrections during the session

1. **I assumed the wrong accelerometer.** The repo had MPU-6050 sketches, so I wrote for it. The scan showed a LIS3DH. Lesson: probe the hardware before writing drivers; the probe is now first in the ladder.
2. **I assumed a zig-zag panel.** `SERPENTINE = True` is common, and it made the bubble's 2x2 dot split. The user's description diagnosed it. Lesson: ask or test the layout first.
3. **The bubble moved the wrong way on Y.** The header promised "toward the low side" but the first version went to the high side. Fixed with `FLIP_Y = True`.
4. **GPIO 5 for Button 2 looked wrong from the start.** I flagged it but built to it. The user confirmed it should be 15.
5. **Thonny kept the serial port.** `mpremote` failed twice for that reason. I did not close Thonny, which is the user's, and asked them to.
6. **A stub file did not take effect.** The unix MicroPython has a built-in `utime`, so my fake-clock file was ignored in early tests, which therefore ran on real time. I found it when a challenge test needed the fake sleep counter, and fixed it by registering the stub in `sys.modules`. The earlier results were still valid (they only waited longer).
7. **I chased a "freeze" that was the user's wrong dot.** It cost a MicroPython install and some tests, but it did prove all nine mazes build under the real interpreter.
8. **Two wrong claims in lab pages.** Lab 9 blamed a flat reading of 1.03 g on "bumps and your hand"; the real reason is that sensors are slightly off. Lab 12 said the rainbow's center was "below the matrix" when it is the bottom row. Both were fixed before publishing. Lab 12's example score was also changed from the perfect 28 to a typical 34.
9. **A wrong claim in the purchasing guide.** I wrote that the panel costs more than the rest of the base kit parts combined, which is only true at the regular price. Fixed to say "at the regular price".
10. **Path depth mistakes.** The Pixel images on the kit guide needed `../../img`, not `../../../img`, and the purchasing-guide's kit links needed `../../` not `../`. Both were caught by checking built paths, the second by a link check on the built page.
11. **A `git add` aborted on a path that no longer existed** after the rename. I restaged only existing paths and checked the staged summary before committing.
12. **`mkdocs gh-deploy` failed once** at the final push and succeeded on retry. I did not find the cause.
13. **Shell slips.** Echoing a line of `=====` triggers a zsh error, and `sed -i` needs `''` on macOS. Both cost a retry each.
14. **The skill's build script needed help.** It did not handle this repo's relative `theme` and `src` paths. I worked around it with symlinks in the scratch folder and did not change the skill.
15. **Process note.** Several commits were made only when the user said "publish"; nothing was pushed unasked.

---

## 10. Check against project guidelines

| Rule | Status |
|------|--------|
| Programs use `import config` and copy settings into same-named variables | Met (probe, labs 03 to 13, and modules; `01` is the documented exception) |
| Three-line header with Filename and Version | Met on all numbered programs; modules use a `Module:` header |
| One `config.py` for pins and settings | Met |
| Write once per step, then sleep | Met in the labs; the animation modes write once per frame |
| Student pages: Flesch-Kincaid 5-7, sentences of 20 words or less | Partly: sentence length and vocabulary rules checked mechanically; no grade score computed |
| Pixel uses they/them; welcome first and celebration last | Met on every lab page; "he/she" grep returned nothing |
| Pixel at most twice per page | Not met on the kit guide (five), by the user's request |
| Code examples run as-is | Met (every challenge was run; headers still say "Not yet tested" where true) |
| Positive framing ("Do Y instead of X") | Partly: a few warnings use "never" (for example the VBUS warning); not rewritten |
| No `navigation.tabs` in `mkdocs.yml` | Met (checked after the nav edit) |
| Never start or kill `mkdocs serve` | Met (used a scratch build and `mkdocs gh-deploy` only) |
| Never use git worktrees | Met |
| Include the repo name in a MicroSim path | Not applicable (no MicroSim) |
| Only commit when asked | Met (6 commits, each after a "publish") |

---

## 11. Loose ends and suggested next steps

1. **Run programs 04 to 07 on the Pico**, then remove "Not yet tested on hardware" from the headers of everything now confirmed.
2. **Confirm the power wiring** (matrix on VBUS 5 V, sensor on 3V3) and fix the guide if your kit differs.
3. **Print one box cover** at Letter, Portrait, Scale 100%, Background graphics on, and scan its QR with a phone.
4. **Commit the rename and the log update** (prompt 38), then run `mkdocs gh-deploy` when you want the live site to show your guide edits and the new name.
5. **Add alt text to the four images you added to the kit guide.** The checker flags them (a one-sentence description of each picture is enough). The new photos did the job I had listed here as a gap.
6. **Add `src/kits/16x16-matrix-accel` to the `watch:` list in `mkdocs.yml`**, so `mkdocs serve` reloads when a program changes.
7. **Re-run `./upload-code.sh --clean`** (it asks for `yes`) to remove the old numbering's files from the Pico.
8. ~~Pick one spelling of the name.~~ Done in prompt 38: the kit is "Tilt-a-Rainbow Kit" everywhere. The program called **Tilt-a-Maze** (lab 12) is a different thing and keeps its name.
9. **Optional next pieces:** a teacher's guide page with quiz answers, a print-guide page for the box cover, a purchasing guide just for this kit, and a trial of the labs with a real 6th grader.
