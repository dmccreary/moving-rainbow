# TODO: Fix MicroSim Metadata

**MicroSim:** solar-powered-nightlight
**Repository:** moving-rainbow
**Generated:** 2026-01-23

## Issues Found

The following issues prevented automatic metadata generation:

1. Missing main.html file
2. No meaningful title found (only generated from directory name)
3. No description found

## Required Actions

### High Priority

- [ ] Create or fix `main.html` - the main simulation file
- [ ] Add a meaningful title that describes the simulation
- [ ] Write a clear description (2-3 sentences) explaining what the MicroSim does

### Medium Priority

- [ ] Create `index.md` with proper YAML frontmatter:
  ```yaml
  ---
  title: "Your Title Here"
  description: "Brief description for SEO"
  ---
  ```
- [ ] Add an iframe to display the simulation
- [ ] Add a "Run Fullscreen" button

### Low Priority

- [ ] Add a lesson plan section
- [ ] Add references section
- [ ] Create a screenshot for social media preview

## Detected Information

- **Framework:** vanilla-js
- **Detected subjects:** Other
- **Visualization types:** interactive-demo
- **Has main.html:** No
- **Has index.md:** Yes

## After Fixing

Once you've addressed the issues above, run the metadata standardization:

```bash
# Use Claude Code's microsim-utils skill to standardize
# Or manually create metadata.json following the schema
```

Delete this TODO.md file after creating proper metadata.json.
