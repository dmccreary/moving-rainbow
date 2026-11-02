# Session Log: Ring 24 Kit Documentation

- **Date:** 2026-11-02
- **Model:** Claude Opus 5.5 (Claude Code, desktop app)
- **Repo:** `/Users/dan/Documents/ws/moving-rainbow` (branch `master`)
- **Deliverable:** `docs/kits/ring-24/` plus the wiring diagram and kit README updates (committed and pushed with this log)

## 1. Outcome in one paragraph

The Ring 24 kit (24-pixel WS2812B ring, two buttons, 27 labs) now has a full student lesson at
`docs/kits/ring-24/index.md`, one page per lab (`01-...md` to `27-...md`), a schemdraw wiring diagram,
simulator pictures of every lab, a nav block in `mkdocs.yml` and an entry on the kits index page. The code
itself was committed first (`8009fa49`). Dan reported that all 27 programs passed on a real kit on
2026-11-02. The documentation was checked with the project-kit-generator skill's lesson checker and a
repo-clean MkDocs build. The pictures come from a desktop simulator, and the pages say so.

## 2. Prompts, verbatim, and how each was handled

### Prompt 1
> Note that in @src/kits/ring-24 that all the test have passed!

Handled by: removing "Not yet tested on hardware." from the headers of programs 02 to 27 and rewriting the
README's "What has been tested" section.

### Prompt 2
> Note that the user (me, Dan McCreary) is VERY happy with the quality of the demos.

Handled by: a feedback memory that records the ring-24 approach as the model for future kits.

### Prompt 3
> now please push to github and generate all the documentation using the project kit skill

Handled by: committing and pushing the kit (`8009fa49`). No skill named "kit skill" was installed, so work
started from the Halloween kit's pattern and the project's `circuit-diagram-generator` skill.

### Prompt 4
> Use this skill: /Users/dan/Documents/ws/learning-micropython/skills/project-kit-generator

Handled by: following its Phase 7 (docs) and Phase 8 (session log) for a kit that was already built and
tested. Phases 1 to 6 (hardware choice, lab ladder, display design, verification before hardware) did not
apply, because the kit has no sensor or display and had already passed on hardware.

## 3. Work timeline

1. Committed and pushed the kit code (`8009fa49`).
2. Read `CONTENT-GENERATION-GUIDE.md`, the Pixel character sheet and the Halloween kit pages.
3. Started three subagents to write lab pages 01-09, 10-18 and 19-27 in parallel.
4. Drew the wiring diagram (`src/kits/ring-24/circuit-diagram.py`) and fixed its first render.
5. Read the project-kit-generator skill and its docs and launch references.
6. Wrote a ring simulator, rendered one picture per lab and a labeled grid, and looked at them.
7. Tested the three lesson challenges on scratch copies of the labs.
8. Wrote the lesson page, added pictures to the lab pages, and updated nav, watch, the kits index and the README.
9. Ran `check_lesson.py`, a scratch MkDocs build, and a headless screenshot of the lesson.

## 4. What I found while reading (facts the design depends on)

1. **Pins.** `config.py`: ring on GP0, Button 1 on GP15, Button 2 on GP14, `TOP_PIXEL = 21`, `BRIGHTNESS = 0.25`.
2. **Buttons use internal pull-ups** (`Pin.PULL_UP` in every button lab), so each button goes from its pin straight to GND.
3. **Power comes from VBUS** (USB 5 V). There is no battery, so the diagram has no battery column.
4. **Labs 2, 5, 6, 7 and 10 count from pixel 0**, not from the top, so their patterns start at about 1:30.
5. **Lab 11's real rule** is that blade-and-gap pairs (`blades * 2`) must divide 24. The README said "2, 3, 4, 6 and 12 all divide evenly into 24", which is true but not the rule. The README now says it the right way.
6. **`upload-code.sh` uploaded every `*.py`**, so it would have copied `circuit-diagram.py` onto the Pico. It now skips it, like the 8x8 kit's script.

### Commands run against real hardware

None. No board was read or written in this session.

## 5. Design decisions and why

**D1. Keep both a lesson page and one page per lab.** The skill expects one lesson page; the repo's kits
(Halloween, 16x16) use one page per lab with the code embedded by snippets. The lesson is the front door with
wiring, checkpoints and teacher notes, and links to every lab page. Alternative: lesson only, which would lose
the per-lab code walkthroughs.

**D2. Use `mascot-*` admonitions on the lesson and `tip`/`success` on the lab pages.** The site's CSS supports
both. The lesson uses the skill's six mascot slots so `check_lesson.py` can check them. The lab pages match the
Halloween lab pages.

**D3. Undo `BRIGHTNESS` in the pictures.** The real colors are at a quarter of full power, which looks dark on
a screen but bright to the eye in a room. The simulator divides by 0.25 so the pictures look the way the ring
looks to a student. Each caption says the picture was drawn by a simulator.

**D4. Edit `mkdocs.yml`.** The skill says to add nav only when asked. Dan asked for "all the documentation",
the repo's earlier kits added nav in the same commit, and `mkdocs.yml` had no uncommitted edits. Also added
`src/kits/ring-24` to `watch:` so the embedded code rebuilds when a lab changes.

**D5. Leave the Lab 26 timing bug in the code.** See Section 10. The kit passed on hardware, so the code was
not changed without asking.

## 6. Files

| File | Status | Notes |
|------|--------|-------|
| `docs/kits/ring-24/index.md` | new | the student lesson |
| `docs/kits/ring-24/01-...md` to `27-...md` | new | one page per lab, code embedded with `--8<--` |
| `docs/kits/ring-24/img/*.png` | new | 26 lab pictures, `all-patterns.png`, `circuit-diagram.png` and `.svg` |
| `docs/kits/index.md` | edited | Ring 24 entry |
| `mkdocs.yml` | edited | nav block and `watch:` entry |
| `src/kits/ring-24/circuit-diagram.py` | new | schemdraw wiring diagram |
| `src/kits/ring-24/upload-code.sh` | edited | skips `circuit-diagram.py` |
| `src/kits/ring-24/README.md` | edited | lesson link, wiring diagram note, Lab 11 rule |

### Wiring summary

Ring DI to GP0 (pin 1), ring 5V to VBUS (pin 40), ring GND to GND (pin 38), Button 1 from GP15 (pin 20) to
the ground rail, Button 2 from GP14 (pin 19) to the ground rail, and Pico GND (pin 18) to the rail.

## 7. Verification

### Method

A desktop simulator with stand-ins for `machine`, `neopixel`, `utime` and `urandom` ran each lab on a fake
clock, with scripted button presses. It checked every pixel index and color, and kept the frame with the most
lit pixels. The three challenges were applied to scratch copies and run the same way.

### Results

| Check | Result |
|-------|--------|
| Labs 02 to 27 in the simulator | all ran with no errors, bad pixels or bad colors |
| Challenge 1 (backward dot) | dot pixels 0, 23, 22, 21 ... |
| Challenge 2 (three comets) | comet heads at pixels 0, 8 and 16 |
| Challenge 3 (own pattern in Lab 27) | prints `Mode 17 - two halves` after one Button 2 press; left half lights blue |
| `check_lesson.py index.md` | 0 hard problems; 2 soft (long sentences in the teacher section) |
| `check_lesson.py` on 27 lab pages | 0 hard problems |
| Constants quoted on the lab pages | all match the code (other numbers are "try it" suggestions) |
| Scratch MkDocs build | exit 0, no warnings; snippets embedded; images resolve; 6 mascot blocks render |
| Headless screenshot of the lesson | looked at; one wrong cross-reference (Step 7 for Step 8) fixed |

### What this does not prove

- The simulator does not model `strip.write()` time, so real patterns may run a little slower than the timings quoted on some lab pages.
- The pictures are one frame each; they cannot show motion or how bright the real ring looks.
- The wiring steps were checked against `config.py` and the Pico pinout, not against a photo of the real kit.

## 8. Mistakes and corrections during the session

1. **First wiring diagram put the ground rail through the buttons.** It was placed 2 units below the Pico's GND pin, which is above GP15. Moved it below the lowest button.
2. **The simulator wrote `__pycache__/` into the kit folder** the first time it imported `config.py`. Removed it, and the simulator now sets `sys.dont_write_bytecode`.
3. **The skill's scratch build failed twice** because the scratch config resolved `custom_dir: theme` and the `watch:` paths against the scratch folder. Fixed with symlinks to `theme/` and `src/` in the scratch folder. The skill's `scratch_mkdocs_build.py` could rewrite those paths itself.
4. **The lesson's welcome callout had 4 sentences** (limit 3) and four long sentences. Found by `check_lesson.py` and fixed.

## 9. Check against project guidelines

| Rule | Status |
|------|--------|
| Student register, grade 5-7 reading level | Met: checker reports no long sentences outside the teacher section |
| Pixel uses they/them; at most 6 callouts; welcome first, celebration last | Met |
| Every term defined at first use | Met for the lesson; the checker found one undefined acronym (USB), now defined |
| Positive framing (no "don't", "just", "simply", "obviously", "easy") | Met: searched every page |
| Code shown is the code that runs | Met: every page embeds the real `.py` with snippets |
| Never start or stop `mkdocs serve` | Met: built into a scratch folder only |
| No `navigation.tabs` | Met: not present |

## 10. Loose ends and suggested next steps

1. **Lab 26 timing bug.** The game draws the dot, sleeps (when a press usually arrives), moves `position` on, and only then checks for a hit. A press is judged against the pixel after the visible dot. With the 1-pixel target (score 5 and up), pressing while the dot is on the target counts as a miss. Fix: check `button_was_pressed` right after `sleep(delay)`, before `position` moves. Needs a retest on the kit.
2. **Lab 27 auto mode only shows Rule 30 of the automaton**, because each rule runs 80 steps (16 s) and auto mode moves on after 10 s.
3. **A real photo of the kit** should replace the simulator picture at the top of the lesson.
4. **Box cover** (skill Phase 8): needs the real photo, a fun kit name, and the lesson URL.
5. **Purchasing guide** entries for the 24-pixel ring (the `purchasing-guide-generator` skill).
6. **The ring simulator** lives only in the session's scratch folder. To regenerate the pictures later, it would need to be saved somewhere, such as next to `circuit-diagram.py`.
