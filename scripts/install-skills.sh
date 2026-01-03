#!/bin/bash
# Install Moving Rainbow skills by creating symbolic links
# from ~/.claude/skills/ to the skills in this project.
#
# Usage:
#   ./scripts/install-skills.sh
#
# This allows Claude Code to discover and use the skills while
# keeping the source files in version control with the project.

set -e

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
SKILLS_SOURCE="$PROJECT_DIR/skills"
SKILLS_TARGET="$HOME/.claude/skills"

echo "=========================================="
echo "  Moving Rainbow Skills Installer"
echo "=========================================="
echo ""
echo "Source: $SKILLS_SOURCE"
echo "Target: $SKILLS_TARGET"
echo ""

# Ensure target directory exists
if [ ! -d "$SKILLS_TARGET" ]; then
    echo "Creating ~/.claude/skills directory..."
    mkdir -p "$SKILLS_TARGET"
fi

# Find all skill directories (directories containing SKILL.md)
skill_count=0
for skill_dir in "$SKILLS_SOURCE"/*/; do
    # Skip if not a directory
    [ -d "$skill_dir" ] || continue

    # Check if it's a valid skill (has SKILL.md)
    if [ -f "$skill_dir/SKILL.md" ]; then
        skill_name=$(basename "$skill_dir")
        target_link="$SKILLS_TARGET/$skill_name"

        # Remove trailing slash from skill_dir for cleaner paths
        skill_dir="${skill_dir%/}"

        # Check if link already exists
        if [ -L "$target_link" ]; then
            # It's a symlink - check if it points to the right place
            current_target=$(readlink "$target_link")
            if [ "$current_target" = "$skill_dir" ]; then
                echo "  [skip] $skill_name (already linked)"
            else
                echo "  [update] $skill_name"
                rm "$target_link"
                ln -s "$skill_dir" "$target_link"
            fi
        elif [ -d "$target_link" ]; then
            # It's a real directory - warn and skip
            echo "  [warn] $skill_name - directory exists at target, skipping"
            echo "         Remove $target_link manually if you want to link"
        else
            # Create new link
            echo "  [link] $skill_name"
            ln -s "$skill_dir" "$target_link"
        fi

        ((skill_count++))
    fi
done

echo ""
if [ $skill_count -eq 0 ]; then
    echo "No skills found in $SKILLS_SOURCE"
    echo "Skills must contain a SKILL.md file to be recognized."
else
    echo "=========================================="
    echo "  Installed $skill_count skill(s)"
    echo "=========================================="
fi

echo ""
echo "To verify, run: ls -la ~/.claude/skills/"
