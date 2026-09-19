# Base Labs Cleanup Session Log

**Date:** 2026-09-18
**Project:** Moving Rainbow (`/Users/dan/Documents/ws/moving-rainbow`)
**Assistant:** Claude (Sonnet 5), with 10 general-purpose sub-agents as lab-page writers
**Scope:** Bring the "Hands on Labs" documentation back in sync with the renumbered base-kit source, move extra-hardware labs out of the base kit, and add new labs
**Status:** Complete and verified. Nothing committed or deployed. Nothing run on real hardware.

---

## 1. Results at a glance

| | Before | After |
|---|---|---|
| Base-kit programs (`src/kits/moving-rainbow-base/`) | 44 numbered (`01`-`44`), with `23` needing a potentiometer | 48 numbered (`01`-`48`), gapless, base-kit hardware only |
| Lab pages in `docs/labs/` | 41 old pages with stale code and old numbering, plus `index.md` and a stray `.py` | 48 lab pages (one per program) plus a new `index.md` |
| Code shown on lab pages | Pasted copies that had drifted from the source | The real `.py` file, embedded with `pymdownx.snippets` |
| Extra-sensor labs | Mixed into the base labs | `docs/additional-labs/` (3 pages) and `src/kits/moving-rainbow-extras/` (4 programs, `config.py`, upload script) |
| New labs | - | 5 (Heartbeat, Fading Stars, Bouncing Ball, Breathing Wave, Sunrise) |
| Lab pages checked mechanically | - | 48 of 48 pass (structure, banned words, verbatim excerpts, links, Pixel callouts) |
| Rendered-site check | - | All 48 pages contain every line of their source program |
| `mkdocs build` warnings | 28 (all in unrelated pages) | 28 (the same ones) |

Roughly 6,800 lines of lab prose were written. Lab pages run from 87 lines (Lab 02) to 249 lines (Lab 31).

---

## 2. The prompts, in order

Each prompt is quoted verbatim (typos included), followed by what was done in response.

### Prompt 1: the assignment

> We have now cleaned up and renumbered all the source code in our base moving rainbow kit here: @src/kits/moving-rainbow-base - We want to ONLY put hands on lab lessons for the source code in our base moving rainbow kit.  If there are labs that use other devices like a photosensor we want to move them to an "Additional Labs" folder for now.
>
> Next, we want to make sure the documentation in the "Hands on Labs" is consistent.
>
> The old documentation is in @docs/labs/* but the docs and the src got out of sync.  Please do your best to get them back in sync.  First use the new file numbers in the @src/kits/moving-rainbow-base - and then make sure there is a lesson plan in the @docs/labs for each of these programs.  Then decide if the remainder of the labs make sense.
>
> Please update the documentation at @docs/labs to track the new source code in the moving rainbow base now.

**What was done**

- Read all 44 programs, `CONTENT-GENERATION-GUIDE.md`, `CODING-GUIDELINES.md`, the Pixel character sheet, the kit user's guide, and the old labs.
- Found that `docs/lessons/` had already been renamed to `docs/labs/` (untracked) and the nav already said "Hands on Labs", so the real work was content, links and structure.
- Built one exemplar lab by hand (Lab 02), a written spec, and a checker script. Then ran seven parallel writers, one per group of labs.
- Created the `docs/additional-labs/` section, rewrote the labs index, regenerated the nav, and fixed inbound links (kit guide, README, Getting Started, LED noodle nightlight page).
- Verified with the checker, a full site build, and a rendered-HTML comparison against the source.

### Prompt 2: clean up the stale pages

> delete the stale old-numbered lab pages

**What was done**

- The first attempt to delete them (and then to move them out of the way) was blocked by the tool's safety classifier, because those files were untracked. Claude did not try to work around the block, and reported it.
- After this explicit instruction, Claude computed the exact list (42 files), confirmed each was byte-identical to both `HEAD:docs/lessons/` and a scratchpad backup, then deleted by explicit filename list (not a wildcard), because six writers were still creating new pages in the same folder.

### Prompt 3: an extras kit

> let's move the potentiometer and the photoreceptor labs to an new dir @src/kits/moving-rainbow-extras for kits with extra sensor parts

**What was done**

- Created `src/kits/moving-rainbow-extras/`. Moved the potentiometer program in, and turned the photoresistor lab's inline code into three real program files. Added a superset `config.py` and a copy of `upload-code.sh`.
- Re-pointed both Additional Lab pages at the new files. Ran all four programs against stubbed hardware.
- Ended by asking whether to close the numbering gap left at Lab 23 (see decision 5.7).

### Prompt 4: new patterns for the gap

> Can you think of two new program that could fit into that spot?  Perhaps a new pattern?

**What was done**

- Surveyed the book first. Chapters 13 and 14 already teach a fading trail with a brightness array, a heartbeat and sine breathing, and `docs/challenges.md` asks for a heartbeat. No base-kit program used `math` at all.
- Recommended Fading Stars and Breathing Wave, with Heartbeat, Bouncing Ball and Sunrise as runners-up, and pointed out the numbering consequence of adding two programs.

### Prompt 5: pick Bouncing Ball, add them all

> I love the all of these, however the Bouncing Ball lab looks really nice.  Make that be the new lab 25.  Note that the other ones also look fun and they seem like omissions.  How do you recommend added all the new ideas?

**What was done**

- Recommended one contiguous block of five labs (23-27) with Bouncing Ball at 25, and shifted the old Labs 24-44 up by four to 28-48 (decision 5.8).
- Wrote and simulated all five programs, then wrote five lab pages with three parallel writers. Renumbered everything with one script and verified it three ways.

### Prompt 6: explain the brightness caps

> yes, please add an explanation of the brightness caps

(This answered a question at the end of the previous reply: whether to add a note about the low brightness caps in Breathing Wave and Sunrise to the kit guide's power section.)

**What was done**

- Added a "Why Some Programs Use Small Numbers" subsection to the kit guide (decision 5.10) and pointed Labs 26 and 27 at it.

### Prompt 7: this log

> I am really happy about how these labs all turned out.  The kids are really going to love them.  Please create a detailed session log in logs/base-labs-cleanup.md and include my prompts and your design decisions.

---

## 3. What was found at the start

- `git status` showed `docs/lessons/*` deleted and `docs/labs/` untracked. The nav in `mkdocs.yml` was already renamed to "Hands on Labs" but still listed the old file names.
- Five source files had uncommitted edits (`27-modes.py`, `44-pixel-demo.py`, `auto-cycle.py`, `main-demo-cycle.py`, `main-old.py`). These were left alone, and they moved with their files when renamed.
- The old lab pages fell into two groups. Pages 22-29 and 41-49 already followed the content guide's structure, but embedded stale code and linked by old numbers. Pages 00-21 were loose and unstructured.
- The old photoresistor lab needed `config.PHOTORESISTOR_PIN`, which the base `config.py` does not define.
- `pymdownx.snippets` was already enabled in `mkdocs.yml` but unused.
- `CLAUDE.md` called `src/led-strip-two-buttons/` the canonical reference, but that folder still uses the older numbering.
- Chapter 8 already covers how NeoPixels work (single-wire protocol, 24 bits per pixel, data stripping).

---

## 4. Old page disposition

Numbers below are the final lab numbers. Old lesson names come from `HEAD:docs/lessons/`.

| Old page | Disposition |
|---|---|
| `00-blink-onboard-led` | Lab 01 |
| `01-blink` | Lab 02 (exemplar) |
| `02-fade-in-and-out` | Folded into Lab 04 |
| `03-heartbeat` | Folded into Lab 04 as a challenge, then became the new program Lab 23 |
| `04-red-green-blue` | Lab 03 |
| `05-color-wheel` | Lab 09 |
| `06-linear-dimmer` | Folded into Lab 04 "Going further" (gamma), linking the MicroSim and the gamma page; the gamma table was not reproduced |
| `07-motion` | Labs 05 and 06 |
| `07-random`, `15-random` | Labs 08 and 10 |
| `08-color-wipe` | Lab 07 |
| `08-moving-bands` | Labs 14 and 15 |
| `08-rainbow` | Lab 11 |
| `08-rainbow.py` | Deleted. It was a matplotlib plotting helper, not a Pico program |
| `09-comet-tail` | Lab 16 |
| `10-moving-rainbow` | Labs 13 and 17 |
| `11-rainbow-cycle` | Lab 12 |
| `16-candle`, `17-theater-chase`, `18-ripple`, `18-twinkle` | Labs 18, 19, 20, 21 |
| `19-larson-scanner`, `20-clock` | Labs 29 and 28 |
| `21-photo-resistor` | Moved to Additional Labs and rewritten around real program files |
| `22-button-test` ... `29-button-modes` | Labs 32, 33, 34, 35, 36, 47, 37, 31 |
| `40-how-neopixels-work` | Dropped: a 32-line generic page that Chapter 8 already covers |
| `41-traffic-light` ... `49-binary-search-visualizer` | Labs 38-46 |
| `index` | Rewritten |

Programs with no old page: Random Walk (22), Random Bounce (30), Pixel Demo (48), and the five new labs.

---

## 5. Design decisions and rationale

### 5.1 Embed the real source instead of pasting it

**Decision:** Every lab page shows its program with `--8<-- "src/kits/moving-rainbow-base/NN-name.py"` (pymdownx.snippets) inside a normal code fence.

**Why:** The whole reason for this task was that docs and source drifted apart. Pasted copies drift again. Embedding makes drift impossible for the listing itself. It also removed any chance of copy errors across 48 pages.

**How it was made safe**

- A scratch build proved snippets render in a plain fence and inside a collapsible.
- The site build was checked so that each of the 48 rendered pages contains every non-blank line of its program.
- `watch:` was added to `mkdocs.yml` so `mkdocs serve` rebuilds when a program changes.
- Short teaching excerpts are still inline, but the checker requires every line of them to be verbatim from a real program.

### 5.2 One page per program, named after the program

`05-move.py` gets `05-move.md`. Cross-links, nav entries and the index can then be generated from one table and checked mechanically. Lab number, file name and page name can no longer disagree.

### 5.3 Page structure follows the content guide

Every lab uses the same section order: title, Pixel welcome, What you'll learn, What you'll need, The program, How it works, Try it yourself, Check your understanding, Pixel celebration, What's next.

Choices and their reasons:

- **Exactly two Pixel callouts per page** (welcome at the top, "Lab complete!" at the end), because the guide caps Pixel at two per page. Any other callout is plain and carries no Pixel image or voice.
- **Pixel uses they/them** and speaks only inside callouts.
- **Grade 5-7 reading level, no "just/simply/obviously/easy", positive framing.** The checker estimates reading grade. Every page scored below 5, and the new brightness section scored about 5.6.
- **Programs over 90 lines go in a collapsible** (`??? example "Full program: ..."`), and the page teaches from short excerpts instead. Five labs use this: 28, 30, 31, 47, 48.
- **Code that is not in the source** (a hint for a challenge) goes in a fence titled `Your change`. It must be valid Python and is exempt from the verbatim rule, so invented code can never pass as the real program.

### 5.4 Conventions introduced for future lab authors

| Convention | Meaning |
|---|---|
| `!!! bug "Known issue"` | The source does something different from its header comment, or has a bug. The page describes the real behavior. The title is exact, so `grep -rn 'Known issue' docs/labs` finds them all to remove after a source fix. |
| `!!! warning "Power check"` | Whole-strip current is estimated as the sum over lit pixels of (r+g+b)/255 x 20 mA, rounded **up**. Anything over about 500 mA gets the note, a link to the kit guide, and one concrete fix. 13 labs carry one. |
| `**Program file:**` line | Links to the source on GitHub, so teachers can find it. |
| No claims of hardware testing | Nothing in the labs says a program was run on a real kit. |

The source programs were **not edited** to fix bugs. The docs describe what the code actually does. Fixing the source is Dan's call, and the callouts are easy to find and delete afterward.

### 5.5 Where the extra-hardware labs live

**Docs:** a separate top-level `docs/additional-labs/` section (not a subfolder of labs), so `docs/labs/` contains only base-kit labs. That matches the instruction to put hands-on labs *only* for the base kit there.

**Source (after Prompt 3):** `src/kits/moving-rainbow-extras/`

- **Its own numbering** (`01-`...`04-`, header `# Extras Lab 01: ...`), because a folder of `23-...` alone would look odd.
- **A superset `config.py`.** It holds every base-kit setting plus `POT_PIN = 26` and `PHOTORESISTOR_PIN = 28`. Students save one file in place of the base config instead of editing lines by hand. Programs read their pins from `config`, matching the coding guidelines.
- **A copy of `upload-code.sh`.** The script resolves its own folder and uploads every `.py` there, so it works for the extras kit unchanged.
- **The photoresistor lab's inline code became three real files** (`02`-`04`), marked "Not yet tested on hardware" in their headers. The doc originally said "add this line to `config.py`", which was replaced by "use the extras `config.py`" (also embedded from the real file).
- **The potentiometer wiring** (3V3 pin 36, GND pin 33, wiper GP26 pin 31) and the photoresistor divider (GP28, pin 34) were written from the Pico pinout, with the photoresistor on the high side so more light gives a bigger number.

### 5.6 Deleting the stale pages

The safety classifier blocked two deletion attempts (`rm`, then a bulk `mv`) because the files were untracked, and that was treated as a real constraint. It was not bypassed. Work continued on everything else, and the blocker was reported.

After Dan's explicit instruction, safeguards made it reversible anyway:

- Diffed every stale file against `HEAD:docs/lessons/` and against a scratchpad backup (all identical).
- Deleted by an explicit 42-name list, never a wildcard, because writers were still adding files to the same folder.
- `git checkout HEAD -- docs/lessons` restores any of them.

### 5.7 The gap at Lab 23

Moving the potentiometer program out left the base kit numbered 22 -> 24. Renumbering 24-44 would touch about 60 files, so Claude did not do it unasked. Instead the guidelines and the labs index stated the gap plainly, and the choice was put to Dan. Dan's answer to that question was to fill the gap with new programs.

### 5.8 Where to add five new labs, and the renumbering strategy

**Choices considered**

| Option | Cost |
|---|---|
| Interleave each new lab next to its relatives (Heartbeat after Dimmer, Fading Stars after Twinkle, ...) | Renames 40+ programs and pages |
| One contiguous block just before the clock, with links back from the related early labs | Renames 21 programs (24-44 shift by +4) |
| Fill only 23 and append the rest at the end | Puts new patterns after the capstone demo, which reads oddly |

**Chosen:** a contiguous block, Labs 23-27, titled "Brightness, motion and math" in the index. Bouncing Ball is 25, as Dan asked. The old 24-44 became 28-48. The order runs simplest to most math-heavy:

| Lab | Idea | New concept |
|---|---|---|
| 23 Heartbeat | Two pulses and a rest | A function with a parameter, timing |
| 24 Fading Stars | Random flares that fade | A per-pixel brightness list, decay by multiplication |
| 25 Bouncing Ball | Gravity and energy loss | Position and velocity, floats, a flag variable |
| 26 Breathing Wave | Sine breathing that travels | `import math`, phase, `%` |
| 27 Sunrise | Blend colors over time | Linear interpolation, lists of colors |

Fading Stars comes before the ball on purpose: shrinking a number each frame (`* 3 // 4`) leads into shrinking the ball's speed (`* BOUNCE`). Labs 04, 21, 22 and 30 got forward links so students find the new labs from the ones they resemble.

**Safeguards for the mass renumber**

- Backed up `docs/labs` and the source folders first, because `docs/labs/` has no git history.
- The rename script did a dry run first, asserted that every source exists and no destination collides, and renamed in descending order.
- **One simultaneous regex pass** for stems and "Lab NN" forms, so 24 -> 28 could never be re-shifted to 32. It also handled "Labs 28 to 33", "Labs 30 and 43", and similar.
- After the run, a cross-check verified that every "Lab NN: Title" mention in the docs matches the canonical numbering (217 mentions, 0 mismatches). It caught exactly what was expected: the index table rows, whose link text had no "Lab" prefix. The index was regenerated from one table.
- The labs index and the nav are both generated from a single table, so they cannot disagree with each other or with the files.

### 5.9 The new programs

All five were simulated against stub `machine` / `neopixel` / `utime` modules before any lab page was written. They have **not** been run on hardware.

- **Bouncing Ball (25).** The physics was tuned by simulation on a 30-pixel strip. Constants: `GRAVITY = 0.2`, `BOUNCE = 0.8`, `MIN_SPEED = 0.6`, `FRAME_DELAY = 0.03`.
  - A drop is 109 frames (about 3.3 s), with arcs peaking at pixels 29, 17, 10, 6, 3, 2 and 1. It stops on the seventh floor touch (new speed 0.56 < 0.6), which the writer's page also states.
  - Exactly one pixel is lit in every frame.
  - A **ceiling guard** was added after testing `BOUNCE` above 1: without it a student experiment could push the ball past pixel 29 and crash. With it, `BOUNCE` 1.0, 1.1 and 1.5 all ran 3,000 frames cleanly, and 1.0 never settles.
  - The ball erases its old pixel in memory and writes once per frame, following the source rule about back-to-back writes.
  - Position is a float rounded with `round()`. The order of the two update lines (speed first, then position) is explained on the page.
- **Heartbeat (23).** 12+12 steps and 8+8 steps, 0.9 s of sleeping per beat: about 67 beats a minute before write time. Every write is followed by a sleep.
- **Fading Stars (24).** Uses `level * 3 // 4`. The natural alternative, `level - level // 4`, stalls forever at level 3 (`3 // 4` is 0), so it is used as a deliberate puzzle on the page. A simulation showed at most 9 lit pixels at once and about 88 mA at peak.
- **Breathing Wave (26).** `phase` wraps at 2 x pi so it never grows without bound. The wave moves toward pixel 0. `WAVE_SPACING = 0` makes all 30 pixels breathe together. Brightness is capped at 60.
- **Sunrise (27).** An explicit `blend()` function with three plain lines, instead of a generator expression, to keep it readable for beginners. The colors are kept small: the brightest, `day`, is `(80, 60, 20)`, about 377 mA.

### 5.10 Why the brightness caps got their own explanation

Sunrise uses an 80 in `day`, which breaks the kit guide's "keep values at 64 or below" rule. Rather than hide the exception, the guide now explains that the rule is a shortcut and the real rule is the **total** current.

The new subsection, "Why Some Programs Use Small Numbers":

- gives the three-step arithmetic;
- works an example (`(80, 60, 20)` is about 12.5 mA per pixel and about 377 mA for 30);
- contrasts colors (solid red at 200 is about 471 mA, solid white at 200 is about 1,412 mA);
- tabulates Labs 26 and 27;
- gives a target for students' own patterns (450 mA or less).

Labs 26 and 27 link straight to it. Every figure was recomputed, and Lab 26's "about 210" was corrected to 212.

### 5.11 Process: exemplar, spec, parallel writers, mechanical checks

**Why parallel writers:** 47 pages was too much to write serially and keep consistent.

**How consistency was kept**

1. Claude wrote Lab 02 by hand as the exemplar.
2. A spec file defined structure, style, accuracy rules, the conventions in 5.4, and the full lab table.
3. Each writer got the facts Claude had already verified from the source (loop bounds, timings, quirks). Each was told to verify the facts again and to report source problems rather than hide or fix them.
4. A checker script gated every page.

**What the checker enforces** (it is the reason the pages could be trusted without reading all 6,800 lines):

- H1 number matches the file name
- the six required `##` sections, in order
- a snippet embed of the correct program, and a collapsible above 90 lines
- every plain `python` excerpt line is verbatim from a real program
- `Your change` blocks compile
- exactly two Pixel callouts with the right images
- banned words, they/them for Pixel, and heading level jumps
- link targets and image paths exist
- long-sentence and reading-grade warnings

Two more checks ran across the whole docs tree: the "Lab NN: Title" cross-check and a "does every `NN-name.py` mentioned in the docs actually exist" check (157 mentions, 0 missing).

**Writers:** wave 1 was 7 writers (42 pages, with Lab 02 already done). Wave 2 was 3 writers for the 5 new labs, with Bouncing Ball on its own writer as the featured lab.

**Independent verification of writer claims.** Several numbers were re-derived instead of trusted:

- Lab 39's power estimate: a fresh simulation gave a mean of 864 mA and a max of 1,140 mA, against the page's "about 900 average, about 1,200 peak".
- Lab 19's "phases 2 and 3 light 7 pixels".
- Lab 26's random-direction bias.
- Lab 25's frame table and seventh-touch claim.

### 5.12 Housekeeping decisions

- Guidance files were updated to match reality: `CLAUDE.md` (labs and extras folders, canonical source) and `CODING-GUIDELINES.md` (numbering, extras rules, a warning to renumber by script and cross-check afterward). `CONTENT-GENERATION-GUIDE.md` (locations) got the same treatment.
- `CLAUDE.md` first called `led-strip-two-buttons/` an "older copy". That was softened to what could be verified: it "still uses the older numbering".
- The user's rule about `mkdocs serve` was respected. Verification used one-shot `mkdocs build` into a scratch directory, with the social plugin off, and a plain static file server on a private port for visual checks (stopped afterward, both times).

---

## 6. Verification performed

| Check | Result |
|---|---|
| Checker on all 48 lab pages | 48 ok, 0 fail |
| "Lab NN: Title" mentions vs canonical numbering | 219 mentions, 0 mismatches |
| Program filenames mentioned in docs exist in source | 157 mentions, 0 missing |
| Numbering gapless `01`-`48`; 48 programs, 48 pages | Yes |
| Rendered site: every source line present on its lab page | 48 of 48 |
| Rendered site: extras programs and `config.py` on Additional Lab pages | All present |
| `mkdocs build` | Exit 0, 28 warnings, identical to the pre-existing baseline |
| Programs compile (`compile()`) | All base and extras programs |
| Extras and new programs against stub hardware | Pins read from config, value ranges, bar lengths, thresholds, single lit pixel per frame, wave direction |
| Visual check in browser | Charge-Up Game (Known issue box), Button Modes (collapsible full listing), Bouncing Ball (embedded program and table of contents). The first two were checked before the renumbering, when they were Labs 36 and 27. |

**The 28 baseline warnings** are all in pages this work did not touch:

- `learning-graph/mascot-test.md` (15)
- `learning-graph/chapter-metrics.md` (4)
- `kits/bookstore-sign/programmers-guide.md` (4)
- `img/mascot/character-sheet.md` (1)
- `getting-started/parts.md` (1)
- `about.md` (1)
- nav entries for `kits/signs/index.md` and `kits/tiki-bar-sign/index.md` (2)

**Not verified:** anything on a real Pico and strip. Timings, power estimates and appearance come from code tracing and simulation.

---

## 7. Source problems found (not fixed)

Labs with a `Known issue` callout (11 callouts on 10 pages) are marked with a callout column. Numbers are final.

| Lab / file | What was found | Callout |
|---|---|---|
| 03 Red, Green and Blue | The comment above the third block says "green" but the code sets blue | Yes |
| 07 Color Wipe | A stray heartbeat comment above `strip = ...` | No (not taught) |
| 11 Rainbow | The `print` runs after the color step, so the Shell shows the next pixel's color | Yes |
| 13 Moving Rainbow (wheel) | `RAINBOW_LENGTH = 7` but `range(0, RAINBOW_LENGTH-1)` draws 6 colors; pixel 0 never lights; `erase()` unused | Yes |
| 28 Binary Clock | `if sec == 60` is never true, so minutes and hours never update after startup; no hour pixels at midnight; a comment says "this is not working" | Yes |
| 30 Random Bounce | Nothing erases old pixels, so dots leave trails (about 900 mA once full); a dot heading down lands on index -1 for a frame; `randint(-1,1)` makes down twice as likely as up (two callouts) | Yes |
| 31 Button Modes and 48 Pixel Demo | Nothing clears the strip on a mode change and `erase()` is never called, so pixels from the previous mode stay lit | Yes (both) |
| 34 Two Buttons | A stale "3.3 rail" comment; Button 2 counts up and Button 1 down, the opposite of Labs 35-36 | Yes |
| 40 Charge-Up Game | The winning range is one pixel earlier than the blue zone (`lit_count` is a count) | Yes |
| 41 Tug of War | The debounce is shared between both players; the start pixel gives Player 1 14 presses and Player 2 15; `game_over` is never reset | Yes |
| 06 Up and Down | Pixel 29 is lit twice in a row (turnaround) | Taught as a puzzle |
| 16 Comet | The tail loop uses `color_count` where `level_count` was meant; it works only because both lists have 9 entries | Taught as a puzzle |
| 17 Moving Rainbow (list) | Six hard-coded erase lines work only for exactly 7 colors | Heads up |
| 19 Theater Chase | 30 is not a multiple of 4, so phases 2 and 3 light 7 pixels instead of 8 | Explained |
| 34, 35, 36 | One debounce timer is shared by both buttons, so a press on the other button within 200 ms is ignored (explained on Lab 34's page); Lab 36 never clears the strip at start | Heads up |
| 42 Reaction Duel | A false start leaves the strip red, so only the Shell shows it | Explained |
| 14 and 15 | Header comment typo "strp" | No |
| `main-demo-cycle.py` | The comments swap green and blue for patterns 3, 4, 6 and 7 (code is right) | No page |

**Power (over about 500 mA at full brightness):** the `Power check` box appears on Labs 07, 10, 11, 12, 14, 15, 18, 30, 31, 35, 43, 44 and 48, each with an estimate and a smaller number to try.

---

## 8. Corrections made along the way

Mistakes caught during the session, and how:

- **Banned words in the assistant's own text.** The exemplar said "just" and "easy on your eyes", and the Additional Labs pages used "just" and "easy to find". The checker flagged them, and they were fixed.
- **A checker patch that half-applied.** The extras folder was added to the checker, but the excerpt-verification loop kept ignoring it because of a quoting slip. It was noticed before the results were trusted, then fixed and re-run.
- **A wrong brief to a writer.** Claude said pixel 0 is lit twice in Lab 06. The writer traced the loop and found the real duplicate is pixel 29 at the top, so the page follows the writer's correct version.
- **Rounding.** Round-up was the stated rule, so Sunrise "376 mA" became 377, Breathing Wave "210" became 212, and the whole-strip Heartbeat "282" became 283.
- **A too-confident wording.** Breathing Wave's "the top is 59" was softened by its writer to "usually 59", because the Pico's 32-bit floats can round `sin()` to exactly 1.0 and give 60.
- **Blank browser screenshots** after scripted scrolling were a repaint delay. Layout was confirmed from the DOM, then a second screenshot.
- **Claims avoided because they could not be verified:** that Thonny sets the Pico's clock, and that `NeoPixel.fill()` is available (the labs use explicit loops instead).

---

## 9. Final lab map

Sections match the labs index. Base-kit only unless noted.

| No | Title | Program |
|---|---|---|
| 01 | Blink the Onboard LED | `01-blink-onboard-led.py` |
| 02 | Blink | `02-blink.py` |
| 03 | Red, Green and Blue | `03-red-green-blue.py` |
| 04 | Dimmer | `04-dimmer.py` |
| 05 | Move a Pixel | `05-move.py` |
| 06 | Up and Down | `06-up-and-down.py` |
| 07 | Color Wipe | `07-color-wipe.py` |
| 08 | Random | `08-random.py` |
| 09 | Color Wheel | `09-color-wheel.py` |
| 10 | Random Colors | `10-random-colors.py` |
| 11 | Rainbow | `11-rainbow.py` |
| 12 | Rainbow Cycle | `12-rainbow-cycle.py` |
| 13 | Moving Rainbow with the Color Wheel | `13-moving-rainbow.py` |
| 14 | Band | `14-band.py` |
| 15 | Moving Band | `15-moving-band.py` |
| 16 | Comet | `16-comet.py` |
| 17 | Moving Rainbow with a Color List | `17-moving-rainbow.py` |
| 18 | Candle Flicker | `18-candle-flicker.py` |
| 19 | Theater Chase | `19-theater-chase.py` |
| 20 | Ripple | `20-ripple.py` |
| 21 | Twinkle Colors | `21-twinkle-colors.py` |
| 22 | Random Walk | `22-random-walk.py` |
| 23 | Heartbeat (new) | `23-heartbeat.py` |
| 24 | Fading Stars (new) | `24-fading-stars.py` |
| 25 | Bouncing Ball (new) | `25-bouncing-ball.py` |
| 26 | Breathing Wave (new) | `26-breathing-wave.py` |
| 27 | Sunrise (new) | `27-sunrise.py` |
| 28 | Binary Clock | `28-clock.py` |
| 29 | Larson Scanner | `29-larson-scanner.py` |
| 30 | Random Bounce | `30-random-bounce.py` |
| 31 | Button Modes | `31-modes.py` |
| 32 | Button Test | `32-button-test.py` |
| 33 | Button and Built-in LED | `33-button-led-test.py` |
| 34 | Two Buttons | `34-two-button-print.py` |
| 35 | Button Change Color | `35-button-change-color.py` |
| 36 | Button Change Speed | `36-button-change-speed.py` |
| 37 | Modes Auto Cycle | `37-modes-auto-cycle.py` |
| 38 | Traffic Light | `38-traffic-light.py` |
| 39 | Binary Counter | `39-binary-counter.py` |
| 40 | Charge-Up Game | `40-charge-up-game.py` |
| 41 | Tug of War | `41-tug-of-war.py` |
| 42 | Reaction Duel | `42-reaction-duel.py` |
| 43 | Fire Simulation | `43-fire-simulation.py` |
| 44 | Cellular Automaton | `44-cellular-automaton.py` |
| 45 | Sorting Visualizer | `45-sorting-visualizer.py` |
| 46 | Binary Search Visualizer | `46-binary-search-visualizer.py` |
| 47 | Buttons Move a Light | `47-buttons-move-light.py` |
| 48 | Pixel Demo | `48-pixel-demo.py` |

Additional Labs (extras kit, own numbering): Brightness Control (`01-brightness-led-strip.py`) and Photoresistor (`02`-`04`).

Lab 31 (Button Modes) is a showcase that uses ideas taught in Labs 32-37, so the index and the page say it can be run first or revisited after Lab 37.

---

## 10. Files changed

**Created**

- `docs/labs/`: 48 lab pages and a new `index.md`
- `docs/additional-labs/`: `index.md`, `potentiometer-brightness.md`, `photoresistor.md`
- `src/kits/moving-rainbow-base/`: 5 new programs (`23`-`27`)
- `src/kits/moving-rainbow-extras/`: `01`-`04` programs, `config.py`, `upload-code.sh`
- `logs/base-labs-cleanup.md`: this file

**Renamed** (plain `mv`, so git shows delete plus new file until staged)

- `src/kits/moving-rainbow-base/` `24`-`44` became `28`-`48`, with header lines updated. `23-brightness-led-strip.py` moved to `moving-rainbow-extras/01-...`.
- 21 matching lab pages in `docs/labs/`

**Edited**

- `mkdocs.yml`: regenerated the "Hands on Labs" nav and added an "Additional Labs" block; added `watch:` for both kit folders
- `docs/kits/moving-rainbow-base/index.md`: links, both program tables, "What You Can Build" bullets, "What's Next", and the new power subsection
- `docs/getting-started/index.md`, `docs/kits/led-noodle-nightlight/index.md`, `README.md`: links to the old `lessons/` path
- `CLAUDE.md`, `CODING-GUIDELINES.md`, `CONTENT-GENERATION-GUIDE.md`
- Labs 04, 21, 22, 26, 27 and 30: forward links and the brightness-cap link (after writers finished)

**Deleted:** 42 stale files in `docs/labs/` (41 old pages and `08-rainbow.py`), all recoverable from `HEAD:docs/lessons/`.

**Not touched:** the source programs' logic (only header lines in the renamed ones, plus the moved potentiometer program's header and `POT_PIN`), anything under `docs/sims/` and `docs/chapters/`, and the running `mkdocs serve`.

---

## 11. Open items and suggested follow-ups

1. **Review and commit.** `git add -A` will pair the renames. The user's earlier uncommitted edits to the modes and demo programs moved with the files (`31-modes.py`, `48-pixel-demo.py`, `auto-cycle.py`, `main-demo-cycle.py`, `main-old.py`). Publishing (`git push`, `mkdocs gh-deploy`) was not done.
2. **Fix source bugs, then remove the callouts.** See section 7. `grep -rn 'Known issue' docs/labs` lists them. The clock (28), Random Bounce (30), Charge-Up (40) and Tug of War (41) have the most student-visible effects.
3. **Test on a real kit.** Especially the five new programs and the three photoresistor programs, which say so in their headers.
4. **Consider a stale-comment sweep.** The "lower left corner ... 3.3 rail" comment is copied through several programs, and header typos remain in 14 and 15.
5. **Check the other 28 build warnings** when convenient. None come from this work.
6. **Save the verification scripts.** The checker, the renumbering script, the title cross-check and the index/nav generator lived in the session scratchpad, which is temporary. They could be saved under `scripts/` if Dan wants to reuse them when adding future labs.

---

## Appendix: how to add a lab in the future

1. Add the program to `src/kits/moving-rainbow-base/` using the next free number and the standard header (`# Lab NN: Title`, `# Filename:`, `# Version: 1.0.0`).
2. Write `docs/labs/NN-name.md` from the structure in section 5.3, embedding the program with `--8<--`.
3. Add it to `docs/labs/index.md`, the nav, and the kit guide tables.
4. If it needs a part outside the base kit, put it in `src/kits/moving-rainbow-extras/` and `docs/additional-labs/` instead.
5. If inserting mid-sequence, renumber with a single-pass script and then check every "Lab NN: Title" mention. Do not renumber by hand.
6. Check the built page contains every line of the program, and that `mkdocs build` shows no new warnings.
