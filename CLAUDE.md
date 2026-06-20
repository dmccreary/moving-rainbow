# CLAUDE.md

This file provides guidance to Claude Code, Codex or Google Antigravity Agents when working with code in this repository.

## Project Overview

This is the Moving Rainbow project - an educational resource for teaching computational thinking and computer science concepts using LED strips and microcontrollers. The project uses MicroPython for the Raspberry Pi Pico for hands-on learning with addressable LEDs (WS2812B/NeoPixels).

## Build and Documentation Commands

This project uses MkDocs with Material theme for documentation:

```bash
mkdocs serve        # Build and serve locally at http://127.0.0.1:8000
mkdocs build        # Build for production (outputs to /site/)
mkdocs gh-deploy    # Deploy to GitHub Pages
```

## Project Structure

User documentation is located in the `/docs/` like all standard mkdocs projects.
Source code that is uploaded into the Raspberry Pi Pico is "packaged" for
easy uploading into the kits and is not stored in the `/src/` directory.

### Documentation Structure (`/docs/`)

- **`chapters/`** - main chapter content
- **`lessons/`** - Progressive hands-on tutorials mapped to numbered source files
- **`sims/`** - Interactive MicroSims (mostly p5.js browser simulations) with `templates/` for creating new sims
- **`kits/`** - Kit-specific assembly and usage guides
- **`prompts/`** - GenAI prompts for content generation
- **`posters/`** - posters for displays, handouts or science fair events
- **`teachers-guide/`** - teacher-facing content (professional register, no Pixel mascot)

### Source Code (`/src/`)

- Code for downloading into project kits is stored in `/src/kits/{KIT_NAME}/`
- **`led-strip-two-buttons/`** - Main kit examples with numbered progression (01-blink.py through 60-pixel-demo.py). This is the canonical reference for lesson code.
- **`pi-500-keyboard/`** - Raspberry Pi 500+ keyboard RGB LED control scripts
- Kit-specific directories (e.g., `katies-busy-board/`, `tiki-bar-sign/`, `kits/holiday-hats/`)

## MicroPython Coding Standards

When generating MicroPython code for student learning, use the `CODING-GUIDELINES.md` file.

## Content Generation — REQUIRED READING

**Before generating any documentation, chapter content, lesson, sidebar, or
teacher's guide entry, read the content generation guide in full:**

> **[`CONTENT-GENERATION-GUIDE.md`](CONTENT-GENERATION-GUIDE.md)**

That guide defines:
- Two audiences (student vs. teacher) with distinct writing registers
- Rules for the **Pixel** mascot (student content only, they/them always)
- Reading level targets, vocabulary rules, and positive-framing requirements
- MkDocs formatting conventions
- A pre-submission checklist

The Pixel character sheet is the canonical visual and voice reference:

> **[`docs/img/mascot/character-sheet.md`](docs/img/mascot/character-sheet.md)**

Do not write any Pixel dialogue without anchoring to that character sheet.

## Educational Design Principles

- **Progressive complexity**: Lessons build incrementally (blink → motion → color → complex patterns)
- **Immediate visual feedback**: Every code change produces visible LED results
- **Low barrier to entry**: ~$15 total hardware cost, minimal wiring (3 wires for LED strip)

When modifying code or documentation, prioritize clarity for beginners over code elegance. Maintain the numbered lesson progression and consistent configuration patterns across kits.

