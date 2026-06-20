# Content Generation Guide

This guide governs all text and code content written for the Moving Rainbow
intelligent textbook. Read it in full before generating any page, chapter
section, lesson, sidebar, or teacher's guide entry.

---

## Two Audiences, Two Registers

Every page in this project belongs to exactly one of two audiences. The writing
style, vocabulary, reading level, and mascot presence differ completely between
them.

| | Student Content | Teacher's Guide Content |
|---|---|---|
| **Location** | `docs/chapters/`, `docs/lessons/`, `docs/kits/`, `docs/sims/` | `docs/teachers-guide/` |
| **Reader** | Grades 6–9, first-time coders, age 11–15 | Adult educators, college-level readers |
| **Reading level** | Flesch–Kincaid grade 5–7 | College / professional |
| **Mascot (Pixel)** | Yes — appears in callout boxes and chapter openings | No — omit Pixel entirely |
| **Tone** | Warm, playful, encouraging, conversational | Clear, professional, pedagogically precise |
| **Sentence length** | Short (10–15 words average) | Standard academic prose |
| **Jargon** | Define every technical term before using it | May assume standard CS / pedagogy vocabulary |
| **Code examples** | Every line annotated if needed; run-able as-is | Excerpts are fine; focus on rationale |
| **Perspective** | "We" and "you" — always a teammate | "Students will…" or "Instructors should…" |

If you are unsure which audience a page targets, check the file path.
When in doubt, err toward the student register — it is easier to promote
vocabulary than to recover from alienating a nervous beginner.

---

## Pixel: The Moving Rainbow Mascot

Before writing any student-facing content, read the canonical character sheet:

> **[`docs/img/mascot/character-sheet.md`](docs/img/mascot/character-sheet.md)**

That file is the single source of truth for Pixel's appearance, voice,
personality, and pose set. Every rule below is derived from it.

### Who Is Pixel?

Pixel is an anthropomorphic WS2812B addressable LED — the same chip students
are programming. Pixel has a matte charcoal body, a rainbow halo ring, expressive
cartoon eyes, and oversized white-glove hands. Pixel uses **they/them** pronouns
exclusively. Never write "he" or "she" for Pixel.

### When Pixel Appears

Pixel shows up in student content only — never in the Teacher's Guide.
Use Pixel at these moments:

| Moment | Pixel Pose | MkDocs Admonition |
|--------|-----------|-------------------|
| Chapter opening | `welcome.png` | `!!! tip "Pixel says..."` |
| New concept introduced | `thinking.png` | `!!! info "Pixel thinks..."` |
| Helpful shortcut or trick | `tip.png` | `!!! tip "Pixel's tip"` |
| Common mistake to avoid | `warning.png` | `!!! warning "Watch out!"` |
| Hard section, keep going | `encouraging.png` | `!!! success "You've got this!"` |
| End of chapter | `celebration.png` | `!!! success "Chapter complete!"` |

### Pixel's Voice Rules

These rules apply wherever Pixel speaks (inside admonition blocks):

1. **Short sentences.** If a sentence needs a comma, see if it can be two
   sentences instead.
2. **"You" and "we" always.** Pixel is a teammate. "We're going to make this
   LED blink" not "The student will observe…"
3. **Define jargon immediately.** "A `for` loop — that's code that repeats
   itself — will run this line 30 times."
4. **Light-and-color puns are welcome** but must never replace clarity.
   Puns are dessert, not the main course.
5. **Mistakes are discoveries, not failures.** Never write "you made an
   error." Write "that's a puzzle to solve!" or "let's find the sneaky bug."
6. **Use Pixel's signature phrases** when they fit naturally — don't force them:
   - *"Let's light this up!"* — chapter openings, rallying cries
   - *"Every bug is just a puzzle in disguise!"* — when code doesn't work
   - *"You're already glowing — now let's make your LEDs glow too!"* — hard
     moments, early in the book

### Pixel Admonition Syntax

```markdown
!!! tip "Pixel says..."
    Your 1–3 sentence Pixel message here. Keep it short, warm, and punchy.
    Remember: they/them pronouns, no jargon without an explanation right behind it.
```

```markdown
!!! warning "Watch out!"
    Pixel holds up both hands — not to alarm, just to care.
    "This is the part where a lot of coders get tripped up. Here's what to look for…"
```

### Pixel Frequency

- **Chapter opener:** always include one Welcome-pose callout.
- **Per section:** at most one Pixel callout. Do not repeat Pixel more than
  twice per page. Overuse dilutes the warmth.
- **End of chapter:** always include one Celebration-pose callout.
- **Inline text:** Pixel never narrates outside of admonition blocks. Main
  prose is written in a neutral friendly voice, not in Pixel's first person.

---

## Student Content Writing Rules

Apply these rules to everything in `docs/chapters/`, `docs/lessons/`,
`docs/kits/`, and `docs/sims/`.

### Reading Level

- Target Flesch–Kincaid grade **5–7** (roughly ages 10–13).
- Prefer single-syllable or common two-syllable words when a choice exists.
- No sentence longer than 20 words without a very strong reason.
- No paragraph longer than 4 sentences.

### Vocabulary

- Define every technical term at first use. Put the definition in parentheses
  or in a following sentence.
  - Good: "An **integer** (a whole number with no decimal point) is the most
    common data type in NeoPixel code."
  - Bad: "Integers are used extensively here."
- Never use passive voice when active voice is possible.
- Contractions are fine and preferred — "you'll" is warmer than "you will."

### Code Examples

- Every code example must run as-is on the target hardware (Pico +
  NeoPixel strip using `config.py`).
- Add a plain-English comment on any line a beginner might not immediately
  understand.
- Follow the project's coding conventions: `import config`, use
  `config.NEOPIXEL_PIN`, `config.NUMBER_PIXELS`, etc.
- Precede every code block with one sentence saying what the code does.
- Follow every code block with one sentence saying what the student should see.

### Structure

Use the following section order for every chapter or lesson:

1. **Chapter / Lesson title** (`#`)
2. **Pixel Welcome callout** (tip admonition, welcome pose)
3. **What you'll learn** — a bullet list of 3–5 outcomes
4. **What you'll need** — hardware/software checklist (if applicable)
5. **Body sections** (`##`) — content, interleaved with Pixel callouts as needed
6. **Try it yourself** — one or two short coding challenges
7. **Check your understanding** — 3–5 short review questions
8. **Pixel Celebration callout** (success admonition, celebration pose)
9. **What's next** — one sentence bridging to the following chapter

### Positive Framing

- Never write "Don't do X." Write "Do Y instead of X, because…"
- Never write "This is easy." (Dismisses anyone for whom it isn't.)
- Never write "Obviously" or "Simply" or "Just" before an instruction.
- Do write "This one might feel tricky at first — that's normal."
- Do write "If your LED doesn't light up, check these three things…"

---

## Teacher's Guide Writing Rules

Apply these rules to everything in `docs/teachers-guide/`.

### Tone and Register

- Professional, collegial, peer-to-peer.
- Assume the reader has taught before and understands basic pedagogy terminology
  (scaffolding, formative assessment, differentiation, etc.).
- Third person for student references ("students will…", "learners who…").
- First person plural is acceptable for collegial asides ("We recommend…").

### Reading Level

- No artificial ceiling — write at the complexity the topic requires.
- Technical precision over simplicity. If there are two words and one is more
  exact, use the exact one and trust the reader.
- Standard academic paragraph length (5–8 sentences) is fine.

### Content Focus

Teacher's Guide pages should answer:
1. **Why** this topic appears here (pedagogical rationale, learning graph
   dependency context).
2. **How** to facilitate the lesson (discussion prompts, common misconceptions,
   differentiation strategies).
3. **What to watch for** (assessment signals, signs a student is stuck vs.
   bored vs. ready to advance).
4. **Connections** to prior and subsequent chapters, and to real-world
   applications.

### Mascot

Pixel does **not** appear in the Teacher's Guide. Do not reference Pixel in
teacher-facing text. The Teacher's Guide is a professional resource.

---

## Shared Rules (Both Audiences)

### Inclusivity

- No gendered language for students. Use "they/them" or rephrase to avoid
  pronouns entirely.
- Pixel uses they/them — enforce this every time.
- Avoid idioms that don't translate well across cultures.
- Hardware cost and accessibility are design constraints: never assume students
  have additional equipment beyond the ~$15 kit.

### Accuracy

- All code must be tested or clearly marked `# untested — adapt for your setup`.
- Pin numbers, library names, and API signatures must match the current
  MicroPython and NeoPixel library versions.
- Electrical values (voltage, current, milliamps) must be physically accurate.
  Never round in a direction that could damage hardware.

### Links and References

- Link to other chapters using relative MkDocs paths: `[Chapter 3](../03-python-functions-modules-practices/index.md)`.
- Link to the character sheet from any page that introduces Pixel to a new
  context: `[Pixel character sheet](../img/mascot/character-sheet.md)`.
- Link to source code in `/src/` when referencing a complete working example.

### MkDocs Formatting

- Always include a blank line before and after bullet lists (MkDocs requirement).
- Use fenced code blocks with language hints: ` ```python `, ` ```bash `.
- Heading hierarchy: `#` (page title) → `##` (major section) → `###` (subsection).
  Never skip levels.
- Use `**bold**` for new vocabulary terms at first introduction.
- Use `backticks` for all code symbols, function names, file names, and
  library names inline.

---

## Checklist Before Submitting Content

- [ ] Identified the correct audience (student vs. teacher)
- [ ] Applied the correct register and reading level
- [ ] Pixel appears (student content) or is absent (teacher's guide)
- [ ] Every technical term defined at first use (student content)
- [ ] All code examples are run-able and follow `config.py` conventions
- [ ] Positive framing throughout — no "don't," "obviously," "just," or "simply"
- [ ] Pixel pronouns are they/them with no exceptions
- [ ] MkDocs formatting is correct (blank lines before lists, correct heading levels)
- [ ] Character sheet consulted for any new Pixel callout: [`docs/img/mascot/character-sheet.md`](docs/img/mascot/character-sheet.md)
