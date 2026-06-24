---
title: "About This Book"
description: "About Moving Rainbow — its purpose, audience, design, and the decade of classroom use behind it."
---

# About This Book

![](./img/students-in-classroom.png)
## Welcome from Pixel

!!! mascot-welcome "Welcome!"
    ![Pixel waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }

    Hi, I'm **Pixel** — an anthropomorphic WS2812B addressable LED, and I'm your guide through this whole book! I'm the exact same kind of chip you'll be programming, so everything my rainbow ring does is everything *your* LEDs will do. We'll start by making a single light blink, and before long you'll be writing your own moving rainbows, comet tails, and twinkle patterns. Every bug is just a puzzle in disguise, so don't worry if your code doesn't work the first time — mine usually doesn't either! You're already glowing — now **let's light this up!**

## Why This Intelligent Textbook

Computing has escaped the screen. It now lives in clothing, jewelry, signs, toys, room decorations, and art installations — anything that can hold a tiny microcontroller and a string of lights. *Moving Rainbow* teaches students to be the people who **make** those things, not just buy them. Working with a $4 Raspberry Pi Pico and a $6 LED strip, every line of code a student writes produces an instant, visible result, turning abstract programming ideas into something they can hold, wear, and show off.

That matters because the demand for these skills is real, and the supply of accessible on-ramps is not.

**In the United States:**

- The U.S. Bureau of Labor Statistics projects that overall employment will grow just **3.1%** from 2024 to 2034 — but computer and information technology occupations are projected to grow **much faster than average**, with computer and information research scientist roles up **20%** and software developer roles up about **15%** over the same period[^1]
- Only **60% of U.S. public high schools** offered a foundational computer science course in the 2024–25 school year, and just **6.1% of students** were enrolled in one — an access-and-participation gap affecting millions of teenagers[^2]
- Momentum is building: **32 states** now require high schools to offer at least one computer science course, yet far fewer provide teachers with ready-to-use, hands-on curriculum materials[^3]

**Worldwide:**

- The number of connected Internet-of-Things devices is growing **14% year over year to roughly 21.1 billion** by the end of 2025 — every one of them a small computer embedded in a physical object, exactly the kind of system this book teaches students to build[^4]

These numbers represent your students — curious kids who are ready to create with technology but have nowhere affordable to start. This textbook exists to give every one of them a working project and the confidence to keep building.

This book takes a fundamentally different approach. It is built on a **learning graph of 485 interconnected concepts** organized into **14 categories**, so each idea is introduced only after its prerequisites are in place and understanding builds naturally from chapter to chapter. Throughout the book you will find **interactive MicroSims** — browser-based simulations that let students explore color models, predict battery life, and experiment with LED behavior before they ever touch hardware. The entire textbook is **open source and free** — no paywalls, no access codes, no expensive annual editions — and it is written at an accessible reading level with every technical term defined the first time it appears.

## Field-Tested Since 2014

*Moving Rainbow* is not a brand-new experiment. It began as a hands-on coding project for **CoderDojo Twin Cities**, a free volunteer-led club where young people learn to program, and its history is recorded commit by commit in public on GitHub.

- The **very first commit dates to October 11, 2014** — more than eleven years of continuous development as of 2026
- The project's open repository holds **over 560 commits** spanning more than a decade, from the original interrupt-driven button experiments and single-pixel rainbow labs of 2014 through today's complete 20-chapter intelligent textbook[^5]
- Across those years the labs have been taught, broken, fixed, and improved in real classrooms and dojo sessions with real students — every animation pattern and wiring diagram in this book has survived contact with beginners

What you are reading is the distillation of that decade-plus of classroom experience into a structured, modern MicroPython curriculum. The lessons that confused students were rewritten; the projects that lit up their faces were kept and expanded.

## How to Use This Book

This textbook is designed for self-paced study and for classroom use alike. Each chapter builds on previous material, so reading in order is recommended. The book includes:

- **20 chapters** progressing from computational thinking and Python basics through Pico hardware, color theory, NeoPixel programming, animation patterns, electronics, sensors, and a capstone project
- **Interactive MicroSims** embedded throughout — browser-based simulations such as the Color Wheel, Battery Life Calculator, LED Current Predictor, and LED Dimmer that you can manipulate to explore concepts before touching hardware
- **Hands-on NeoPixel lessons** mapped to numbered MicroPython programs, from *Blink* through *Larson Scanner*, *Theater Chase*, and *Moving Rainbow*
- **A Glossary** with clear, precise definitions for every key term
- **A Teachers Guide** with mentoring best practices, concept cards, and classroom workflow tips
- **Project Kits** — wearable hats, signs, nightlights, and more — for applying the skills to real builds
- **A Learning Graph** visualizing how all 485 concepts depend on one another
- **Search** available from any page using the search bar

The [Learning Graph](learning-graph/index.md) visualizes how concepts connect across chapters. If you want to explore non-linearly or check the prerequisites for a specific topic, start there.

## About the Author

![](./img/dan-headshot-small.png){ width="150px" align="right"}

Dan McCreary is a semi-retired AI researcher, solution architect, and educator who has spent more than three decades helping Fortune 100 organizations reason over massive datasets. At Optum he founded the Generative AI Center of Excellence and led the team that built one of the world's largest healthcare knowledge graphs — spanning over 25 billion vertices — to unify member, provider, and patient insights. Dan's deep background in knowledge representation and systems thinking underpins the precise learning graphs and intelligent textbook workflows used throughout this course.

He is the co-author of *Making Sense of NoSQL* (Manning Publications), the founding chair of the NoSQL Now! conference, and a frequent keynote speaker on semantic search, ontology strategy, and AI hardware. *Moving Rainbow* grew directly out of Dan's work as a **STEM volunteer with CoderDojo Twin Cities, which he began in 2014** — the same year the project's first code was committed. More than a decade later, he applies the same rigor to building open educational resources. You can visit the [Intelligent Textbooks Case Studies](https://dmccreary.github.io/intelligent-textbooks/case-studies/) to see over 87 textbooks that Dan has created or co-created with other authors.

**Selected Credentials**

- B.A. in Physics and Computer Science from Carleton College
- M.S.E.E. from the University of Minnesota
- MBA coursework at the University of St. Thomas
- Patent holder in semantic search and ontology management techniques
- Advocate for large-scale Enterprise Knowledge Graph adoption across healthcare and education
- Long-time promoter of accessible, low-cost AI-powered learning experiences

## How to Cite This Book

If you reference this textbook in academic work, curriculum proposals, lesson plans, or other publications, please use one of the following citation formats.

**APA (7th edition)**

McCreary, D. (2026). *Moving Rainbow: Computational Thinking with LED Programming*. https://dmccreary.github.io/moving-rainbow/

**Chicago (17th edition)**

McCreary, Dan. 2026. *Moving Rainbow: Computational Thinking with LED Programming*. https://dmccreary.github.io/moving-rainbow/.

**MLA (9th edition)**

McCreary, Dan. *Moving Rainbow: Computational Thinking with LED Programming*. 2026, dmccreary.github.io/moving-rainbow/.

**BibTeX**

```bibtex
@book{mccreary2026movingrainbow,
  title     = {Moving Rainbow: Computational Thinking with LED Programming},
  author    = {McCreary, Dan},
  year      = {2026},
  url       = {https://dmccreary.github.io/moving-rainbow/},
  note      = {Interactive intelligent textbook}
}
```

To cite a specific chapter, append the chapter number and title — for example:

McCreary, D. (2026). Chapter 1: Introduction and Computational Thinking Foundations. In *Moving Rainbow: Computational Thinking with LED Programming*. https://dmccreary.github.io/moving-rainbow/chapters/01-intro-and-computational-thinking/

## License

This work is released under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](license.md). You are free to share and adapt the material for non-commercial purposes as long as you give appropriate credit and share your adaptations under the same license.

## References

[^1]: U.S. Bureau of Labor Statistics. (2025). *Computer and Information Technology Occupations*. Occupational Outlook Handbook. https://www.bls.gov/ooh/computer-and-information-technology/
[^2]: Code.org Advocacy Coalition. (2025). *2025 State of Computer Science Education*. https://advocacy.code.org/stateofcs/
[^3]: Code.org. (2024). *2024 State of Computer Science Education Highlights Growing Investment from Policymakers, Continued Gaps in Access*. https://www.prnewswire.com/news-releases/2024-state-of-computer-science-education-highlights-growing-investment-from-policymakers-continued-gaps-in-access-302282502.html
[^4]: IoT Analytics. (2025). *State of IoT 2025: Number of connected IoT devices growing 14% to 21.1 billion globally*. https://iot-analytics.com/number-connected-iot-devices/
[^5]: McCreary, Dan. (2014–2026). *Moving Rainbow* source repository, commit history beginning October 11, 2014. GitHub. https://github.com/dmccreary/moving-rainbow
