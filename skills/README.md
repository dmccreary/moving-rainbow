# Skills for Moving Rainbow

Due to the fact that Claude Code only permits up to 30 skills loaded
at a time, all the skills related to this project have been moved
here.

## Two scopes: project-scoped vs. global

A skill in this directory can be made available to Claude Code in one of two
ways, and the choice matters because Claude Code only loads 30 skills at a
time.

**Project-scoped (preferred for anything Moving Rainbow specific).** Symlink
the skill into this repo's `.claude/skills/` directory. Claude Code loads it
when working in this repo and nowhere else, so it costs nothing against the
global budget:

```sh
ln -s ../../skills/{skill-name} .claude/skills/{skill-name}
```

**Global.** Symlink the skill into `~/.claude/skills/` so it loads in every
project. Reserve this for skills that are genuinely useful outside this repo.

## Installation

To install the global skills, run the installer script:

```sh
./scripts/install-skills.sh
```

This creates symbolic links from `~/.claude/skills/` to the skills in this
directory, allowing Claude Code to discover and use them while keeping
the source files in version control.

The installer **skips any skill that is already symlinked in
`.claude/skills/`** — that symlink is the signal that the skill is deliberately
project-scoped — and it removes a stale global link if it finds one. So the
installer can be re-run safely at any time without un-scoping a project skill.

## Available Skills

### pi-keys-generator (global)

Generates Python and shell scripts for controlling RGB LEDs on the
Raspberry Pi 500+ keyboard. Use this skill when you need to:

- Create keyboard lighting effects and animations
- Set specific keys to specific colors
- Build notification systems that flash the keyboard
- Develop typing-reactive effects

**Example prompts:**
- "Create a script that turns the F1-F12 keys blue"
- "Make a typing speed indicator that changes key colors"
- "Create a notification effect when I get an email"

**Contents:**
- `SKILL.md` - Main skill instructions and templates
- `references/api_reference.md` - Full RPiKeyboardConfig API documentation
- `scripts/template.py` - Python script starter template
- `scripts/template.sh` - Shell script starter template

### purchasing-guide-generator (project-scoped)

Turns a short parts list into a complete, teacher-ready **Purchasing Guide**
page at `docs/kits/{kit}/purchasing-guide/index.md`. Use this skill when you
need to:

- Build a bill of materials for a kit, with required parts before optional ones
- Price a kit both for one build and for a classroom order of 20+
- Find or source a photo for each part
- Generate eBay / AliExpress / Amazon search links so teachers can click to buy

**Example prompts:**
- "Write a purchasing guide for the Cylon Pumpkin kit"
- "What would it cost to order 20 of these kits for my class?"
- "Add search links and prices to the base kit parts list"

**Contents:**
- `SKILL.md` - Workflow, page structure, and part-section template
- `references/part-catalog.md` - Price bands, keywords and prep work for parts
  that recur across Moving Rainbow kits
- `references/sourcing-strategy.md` - Building honest price bands, marketplace
  selection, and the ordering mistakes worth warning teachers about
- `references/image-sourcing.md` - License rules and the image workflow
- `scripts/find_part_image.py` - Searches this repo and all sibling repos for
  an existing photo of a part
- `scripts/make_search_urls.py` - Emits the marketplace search-link block
- `assets/purchasing-guide-template.md` - Page skeleton with a worked example
- `assets/image-description-template.md` - Text-to-image brief for missing art
