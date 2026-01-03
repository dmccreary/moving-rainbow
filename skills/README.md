# Skills for Moving Rainbow

Due to the fact that Claude Code only permits up to 30 skills loaded
at a time, all the skills related to this project have been moved
here.

## Installation

To make these skills available to Claude Code, run the installer script:

```sh
./scripts/install-skills.sh
```

This creates symbolic links from `~/.claude/skills/` to the skills in this
directory, allowing Claude Code to discover and use them while keeping
the source files in version control.

The installer can be re-run safely at any time to add new skills.

## Available Skills

### pi-keys-generator

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
