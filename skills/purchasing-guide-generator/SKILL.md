---
name: purchasing-guide-generator
description: >-
  Turn a short parts list into a complete, teacher-ready Purchasing Guide page
  for a kit — a summary bill of materials with required parts first and optional
  parts after, then one section per part with a photo, what the part does in the
  kit, any prep work (soldering 22-gauge leads, cutting a strip to length),
  single-unit and classroom-quantity-of-20 price estimates, the exact search
  keywords that find it, and live eBay / AliExpress / Amazon search links.
  Use this skill whenever the user asks for a purchasing guide, parts list,
  parts page, bill of materials, BOM, shopping list, sourcing guide, "where do I
  buy this", "how much does this kit cost", "what do I need to order for 20
  students", or wants to add or refresh purchasing information for a kit — even
  if they never say the words "purchasing guide". Also use it when updating an
  existing purchasing guide with prices, images, or search links.
---

# Purchasing Guide Generator

A Purchasing Guide is the page a teacher opens with a district purchase order
in one hand. It has to answer three questions without them leaving the page:
*what exactly do I order, what will it cost me for a class of 20, and where do
I click to buy it.* Everything in this skill exists to make one of those three
answers unambiguous.

The input is small — usually a handful of part names the user pastes in, or the
"Parts" section already sitting in a kit's `index.md`. The output is a long,
image-rich, link-rich page. Most of the work is sourcing: finding a clean photo,
finding a real price band, and finding the search phrase that actually surfaces
the right part instead of forty wrong ones.

## Where the output goes

```
docs/kits/{kit-name}/purchasing-guide/index.md
```

The guide gets its own directory so part-specific photos can live beside it.
Images that already exist in `docs/img/` stay where they are and are referenced
as `../../../img/name.png` (three levels up from the guide).

A model example to match for tone and depth is
[`docs/kits/moving-rainbow-base/purchasing-guide/index.md`](../../docs/kits/moving-rainbow-base/purchasing-guide/index.md).
It predates the search-link requirement, so it is the right register but an
incomplete structure — read it for voice, follow this skill for structure.

## Audience and register

Purchasing guides are teacher-facing even though they live under `docs/kits/`.
Write them the way `CONTENT-GENERATION-GUIDE.md` describes the Teacher's Guide
register: professional, collegial, peer-to-peer, technically precise. **Pixel
never appears in a purchasing guide** — nobody wants a mascot cheering while
they reconcile a purchase order. Use "we" for house practice ("We buy ours in
packs of ten"), third person for students.

## Workflow

### 1. Pin down the parts list and split it

Get the list from the user, or read the kit's `index.md` — most kits already
have a "Parts" or "What you'll need" section, and reusing it keeps the two pages
consistent. Then split it in two:

- **Required** — the kit does not function without it.
- **Optional** — durability, convenience, or enrichment (screw headers, acrylic
  bases, battery packs, spare buttons).

Required parts come first in both the summary list and the body sections. A
teacher on a tight budget should be able to stop reading halfway down the page
and still have ordered a working kit.

If a part in the list is ambiguous ("LED strip"), resolve it against the kit's
code and wiring before writing — 60 pixels/meter and 144 pixels/meter are
different orders, and a purchasing guide that gets that wrong costs real money.

### 2. Source a photo for every part

Order of preference, best first:

1. **An image already in this workspace.** Run the finder — it searches this
   repo and every sibling repo's `docs/img/`:

   ```bash
   python3 skills/purchasing-guide-generator/scripts/find_part_image.py momentary push button
   ```

   Images from sibling repos are already license-clean and match the house look.
   Copy the file into the guide's directory rather than linking across repos.

2. **Wikimedia Commons** or another explicitly free source, when nothing local
   fits. See `references/image-sourcing.md` for the license rules, the
   attribution line, and the watermark check.

3. **A generation brief.** If you cannot find a high-quality image that is
   unwatermarked and free of copyright restrictions, do not settle for a bad
   one and do not silently omit the picture. Write
   `docs/kits/{kit}/purchasing-guide/{part-slug}-image-description.md` from
   `assets/image-description-template.md`, and leave a clearly-marked
   placeholder in the page so it is obvious what still needs art.

Never hotlink a product photo from eBay, Amazon, or AliExpress. Those are
copyrighted seller assets, they rot within weeks, and a broken image on a
purchasing page reads as an abandoned page.

### 3. Write each part section

Start from `assets/purchasing-guide-template.md` — it is the page skeleton with
one fully worked part section (the WS2812B strip) showing the target depth.
Copy it, then replace. Working from the skeleton is faster than assembling the
page from the fragments in this file, and it keeps guides consistent across
kits.

Use the section template below, in order, with no sections skipped. The order
matters: a reader scanning for the part they are unsure about recognizes it by
the photo, confirms it by the description, and then commits by the price and
the link.

### 4. Price it twice

Every part gets both a single-unit price and a classroom price. See
`references/sourcing-strategy.md` for how to build the bands honestly, and
`references/part-catalog.md` for house-observed bands on the parts that recur
across Moving Rainbow kits.

### 5. Generate the search links

Do not hand-write marketplace URLs; the query syntax differs per site and typos
are invisible until a teacher clicks. Run:

```bash
python3 skills/purchasing-guide-generator/scripts/make_search_urls.py "WS2812B LED strip 60/m 5V IP20"
```

Add `--sites ebay,aliexpress,amazon,microcenter` for parts where a specialty
retailer genuinely beats the marketplaces (the Pico at Micro Center is the
standing example), and `--alt "alternate phrasing"` when the part is sold under
two different names.

### 6. Wire the page in

- Add a link from the kit's `index.md` near the top of its parts section.
- Add a nav entry in `mkdocs.yml` under that kit, titled `Purchasing Guide`.
- Verify every image path resolves from the guide's directory and that the
  summary-list anchors match the actual heading slugs.

## Page structure

Follow this shape exactly — teachers move between kits, and a predictable page
means they learn the layout once.

````markdown
# Purchasing Guide for the {Kit Name} Kit

![{Kit name} kit parts laid out](./kit-parts.jpg)

{One paragraph: what the finished kit does, the all-in cost for one kit and the
per-student cost at a class of 20, and how long the slow-shipping route takes.
This paragraph is the whole page in miniature — a teacher who reads only this
should know whether the kit fits their budget and their calendar.}

!!! note "Prices checked {Month Year}"
    Component prices move, and marketplace listings turn over constantly.
    Treat every figure here as a planning estimate, not a quote.

## Summary of Parts List

**Required**

- [{Part name}](#part-anchor) — {one clause on what it does} ({qty-1 price})
- ...

**Optional**

- [{Part name}](#part-anchor) — {what it adds} ({qty-1 price})
- ...

**Estimated total:** ${X} for one kit · ${Y} per student for a class of 20

## {Required Part 1}

...one section per part, required parts first, in the order they appear above...

## Purchasing Strategy

{The lead-time and bulk-buying guidance — see the section below.}

## Classroom Order Worksheet

| Part | Required? | Qty for 1 kit | Qty for 20 kits | Est. cost for 20 |
|------|-----------|---------------|-----------------|------------------|
| ...  | Required  | 1             | 20              | $XX              |
| **Total** | | | | **$XXX** |
````

## Part section template

````markdown
## {Part Name}

![{descriptive alt text}](../../../img/{image}.png)

{Two to four sentences: what the part is, what job it does *in this kit*, and
what a buyer needs to get right when choosing between listings — voltage,
pixel density, pin pitch, tactile-switch lead spacing. Name the specific
failure: "the 12V version of this strip will not work with the Pico's 5V
supply" is worth more than "make sure you get the right one".}

**Prep work:** {What has to happen between the box arriving and a student
using it — soldering 22-gauge solid-core leads to the strip's pads so it
seats in a breadboard, cutting a 1-meter strip at the 30-pixel mark, marking
rails with a permanent marker, tinning stranded wire. Say roughly how long it
takes per kit, since that is prep time a teacher has to schedule. Write "None
— it is breadboard-ready as shipped." when there genuinely is none, because
the absence of prep work is itself useful information.}

**Cost:** ~${X} each in quantity 1 · ~${Y} each in a classroom order of 20+
({what drives the difference — pack sizes, free-shipping thresholds, origin}).

**Search keywords:** `{primary phrase}`, `{alias}`, `{part number}`

**Where to buy:**

- [Search eBay for "..."](...)
- [Search AliExpress for "..."](...)
- [Search Amazon for "..."](...)
````

Two judgment calls worth making deliberately:

**Alt text.** Describe the part, not the file. `![Momentary push button with
four leads](...)` helps a screen-reader user and helps anyone whose image
failed to load. `![](...)` helps no one.

**Keywords.** The point is to give the reader the phrase that *works*, which is
often not the formal name. "WS2812B" finds the strip; "NeoPixel" mostly finds
Adafruit-branded product at three times the price; "addressable RGB LED strip"
finds a mix. Say so when the distinction costs money. Include part numbers
(`2N2222`, `PCF8574`) — they are the highest-signal search term there is.

## Purchasing strategy section

Every guide closes with this guidance. Adapt the specifics, keep the substance:

- **Lead time is the real tradeoff.** Direct-from-China listings on AliExpress
  and many eBay sellers run roughly 40–70% cheaper than Amazon Prime for the
  same commodity part, at 2–3 weeks of transit — sometimes 4–6 weeks around
  Lunar New Year, when Chinese factories and shipping largely stop for two
  weeks or more. Order a semester ahead and the savings are free; order the
  week before the unit starts and you pay the Amazon premium for the privilege.
- **Buy one, then buy twenty.** Order a single unit from a seller first,
  confirm it is the right part, *then* place the classroom order — ideally with
  the same seller, since listings for commodity parts vary in quality far more
  than the photos suggest.
- **Order spares.** 10–15% over the class count. Buttons get lost, strips get
  cut short, someone reverses power and ground. Spares are cheaper than a
  dead station in the middle of a lesson.
- **Watch the pack sizes.** Much of the classroom savings comes from pack
  breakpoints (breadboards in tens, buttons in hundreds) rather than negotiated
  per-unit discounts. Round the class order up to the pack, not to the roster.
- **Check the school's purchasing rules before promising the cheap route.**
  Many districts cannot reimburse AliExpress or direct international orders and
  require a domestic vendor with a W-9. If that is the constraint, the Amazon
  price is the real price — say so rather than quoting a number the teacher
  cannot actually use.

## Reference material

- `references/part-catalog.md` — house-observed price bands, search keywords,
  prep work, and known images for parts recurring across Moving Rainbow kits.
  **Read this before pricing anything** — it saves rediscovering the same
  numbers and keeps guides consistent with each other.
- `references/sourcing-strategy.md` — how to build a defensible price band,
  which marketplace wins for which part class, and the failure modes worth
  warning teachers about.
- `references/image-sourcing.md` — the license rules, the Wikimedia workflow,
  and when to write a generation brief instead.
- `assets/purchasing-guide-template.md` — the page skeleton to copy, with one
  worked part section showing the target depth.
- `assets/image-description-template.md` — the text-to-image brief to fill in
  when no usable photo of a part exists.

## Before you call it done

- Required parts appear before optional parts in the summary *and* the body.
- Every part section has all six pieces: image, description, prep work, both
  prices, keywords, and search links.
- Every summary bullet's anchor matches a real heading on the page.
- Every image path resolves from `docs/kits/{kit}/purchasing-guide/`.
- No image is hotlinked from a marketplace; anything sourced externally carries
  its license and attribution.
- Any part still missing art has a companion `*-image-description.md`.
- The page carries a "Prices checked {Month Year}" note.
- The order worksheet totals actually add up.
- Pixel does not appear anywhere on the page.
