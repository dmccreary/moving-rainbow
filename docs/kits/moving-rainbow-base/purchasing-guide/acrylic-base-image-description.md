# Image Brief: Acrylic Base

Written for a text-to-image model because no suitably licensed photograph of a
Moving Rainbow acrylic base exists in this repo or any sibling repo. The
`find_part_image.py` search for "acrylic base" and "plexiglass" returned only
unrelated diagram files.

Delete this file and remove the placeholder from
`purchasing-guide/index.md` once a real photo or generated image is in place.

## Prompt

> A rectangular sheet of clear 3mm acrylic, roughly 4 by 8 inches, lying flat on
> a plain white seamless background. A small white solderless breadboard is
> mounted on top of it, and a short strip of addressable RGB LEDs runs along the
> front long edge of the acrylic. The acrylic's cut edges catch the light and
> glow faintly. Soft, even product-photography lighting with no harsh shadows.
> Shot from a low three-quarter angle so the thickness of the sheet is visible.
> The assembly fills roughly 70% of the frame. Sharp focus throughout, high
> detail, no text overlay, no watermark, no hands, no packaging.

## Physical details that must be right

A teacher will use this image to understand what to cut and how it goes
together, so these features carry the meaning:

- **Size:** roughly 4" × 8" (100mm × 200mm), 3mm thick
- **Material:** clear transparent acrylic (not frosted, not colored), with
  visible edge thickness so the reader can judge the 3mm
- **Breadboard:** half-size 400-tie-point white breadboard, adhesive-mounted
  flat on the acrylic, positioned toward the back half of the sheet
- **LED strip:** a short WS2812B strip along the front long edge, unlit or only
  faintly lit — a fully lit strip blows out the exposure and hides the base,
  which is the actual subject
- **Distinguishing marks:** the protective film is fully peeled; edges are
  cleanly cut, not snapped

## What it must not look like

- **Not a finished commercial product enclosure.** This is a flat mounting
  plate, not a case with walls or a lid. Anything that reads as an injection-
  molded box sends readers looking for a product that does not exist.
- **Not frosted or white acrylic.** The transparency is the point — it is why
  the edge glows.
- **Not thick cast acrylic.** A 10mm slab looks like a display block and costs
  several times as much.
- **The LED strip must not dominate.** The base is the subject; other sections
  of the guide already show the strip on its own.

## Aspect ratio and size

- Aspect ratio: 4:3 landscape
- Target: at least 1000px on the long edge

## Where it goes

- File: `docs/kits/moving-rainbow-base/purchasing-guide/acrylic-base.png`
- Referenced from: `docs/kits/moving-rainbow-base/purchasing-guide/index.md`
- Alt text to use: `Clear acrylic base with a breadboard and LED strip mounted on it`
