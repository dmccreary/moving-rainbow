# Changes to docs/chapters/02-pi-500-keyboard/index.md

**Date:** 2026-01-02

## Spelling Corrections (British to US English)

| Original | Corrected |
|----------|-----------|
| theses | these |
| colours | colors |
| colour | color |
| behaviour | behavior |
| favourites | favorites |
| favourite | favorite |
| customising | customizing |
| visualisation | visualization |
| initialises | initializes |
| equlivilant | equivalent |
| ussually | usually |

**Note:** The `--colour` flag in CLI commands was preserved as-is since it is the actual parameter name used by the `rpi-keyboard-config` tool.

## Markdown Formatting Fixes

### Structure
- Added `## Contents` section with proper markdown anchor links
- Converted flat "What You Will Need" list to proper bullet points with `## What You Will Need` heading
- Added proper `##` headings for all major sections

### Code Blocks
- Wrapped all shell commands in ` ```sh ` fenced code blocks
- Wrapped all Python code examples in ` ```python ` fenced code blocks

### Inline Formatting
- Added backticks around keyboard shortcuts: `FN + F4`, `FN+F5`, `FN+F6`
- Added backticks around file names: `simple_colour.py`, `fire.py`, `game_of_life.py`, `fire_interpolated.py`, `speed_test.py`, `flash_demo.py`, `snake.py`, `screensaver.py`
- Added backticks around function/method names: `send_leds()`
- Added backticks around paths: `/home/pi`, `/home/pi/fire.py`
- Added backticks around key sequences: `Ctrl + X`, `Y`, `Enter`
- Added backticks around library names: `random`, `time`, `RPiKeyboardConfig`

### Other Fixes
- Fixed capitalization: "Crontab -e" changed to "crontab -e"
- Fixed grammar: "to takes about" changed to "it takes about"
- Fixed grammar: "going diving" changed to "going to dive"
- Fixed grammar: "orange amd purple" changed to "orange and purple"
