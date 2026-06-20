# MicroSim Screenshot TODO

This file tracks MicroSims that are included in the gallery (`index.md`) but are
missing a preview screenshot. Logged: 2026-06-20.

Cards for these MicroSims currently render with a title and description but no
thumbnail image. Run the capture command below for each one, then regenerate the
index so the card picks up the new `<name>.png`.

## Missing Screenshots

### Battery Life Calculator
```bash
~/.local/bin/bk-capture-screenshot docs/sims/battery-life-calculator
```

### Claude Code Hooks Workflow
```bash
~/.local/bin/bk-capture-screenshot docs/sims/claude-code-hooks-workflow
```

### Color Wheel MicroSim
```bash
~/.local/bin/bk-capture-screenshot docs/sims/color-wheel
```

### Learning Graph Viewer
```bash
~/.local/bin/bk-capture-screenshot docs/sims/graph-viewer
```

### LED Dimmer Circuit
```bash
~/.local/bin/bk-capture-screenshot docs/sims/led-dimmer
```

### Photoresistor Component Visualization
```bash
~/.local/bin/bk-capture-screenshot docs/sims/photoresistor-component
```

### Pico Light Sensor Circuit
```bash
~/.local/bin/bk-capture-screenshot docs/sims/pico-light-sensor
```

## Notes

- `current-predictor` uses `dimmer-current-base.png` and `nightlight` uses
  `photoresistor.png` instead of a `<name>.png`; the index references those
  existing files. Rename to `<name>.png` later for consistency if desired.
- The following directories are intentionally **excluded** from the gallery:
  `templates/` and `animated-wire/` (MicroSim templates/scaffolding),
  `graph-viewer-v1/` (superseded by `graph-viewer/`), and
  `solar-powered-nightlight/` (empty stub `index.md`).
