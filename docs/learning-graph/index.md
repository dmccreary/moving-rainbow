# Learning Graph for Moving Rainbow

[Open Learning Graph Viewer Fullscreen](../sims/graph-viewer/main.html){ .md-button .md-button--primary }

<iframe src="../sims/graph-viewer/main.html" width="100%" height="600px" frameborder="0"></iframe>

This section contains the learning graph for the Moving Rainbow intelligent textbook. A learning graph is
a graph of concepts used in this course. Each concept is represented by a
node in a network graph. Concepts are connected by directed edges that indicate
what concepts each node depends on before that concept is understood by the student.

A learning graph is the foundational data structure for intelligent textbooks that can recommend learning paths.
A learning graph is like a roadmap of concepts to help students arrive at their learning goals.

At the left of the learning graph are prerequisite or foundational concepts. They
have no inbound edges — nothing is required to understand them before starting. At the far right
we have the most advanced concepts in the course. To master these concepts you
must understand all the concepts that they point to.

This learning graph contains **485 concepts** across **12 topic categories** with **851 dependency edges** and a longest learning path of **18 steps** from foundational Python to interactive LED programming.

## Foundational Entry Points

The following 14 concepts have no prerequisites and form the entry points into the learning graph:

- **Python Programming Language** — the language used for all lesson code
- **Raspberry Pi Pico** — the microcontroller hardware platform
- **NeoPixel LED** — the addressable LED hardware
- **RGB Color Model** — the color representation system
- **Voltage** — electrical potential, the starting point for circuit concepts
- **Electrical Current** — the flow of charge
- **Resistance** — opposition to current flow
- **Breadboard** — the prototyping tool used in all circuits
- **Decomposition** — breaking problems into smaller parts (CT pillar)
- **Pattern Recognition** — finding similarities (CT pillar)
- **Abstraction** — focusing on essential details (CT pillar)
- **Algorithm Design** — step-by-step problem solving (CT pillar)
- **Git Version Control** — the version control system
- **Project Ideation** — the starting point of the design process

## Course Description

We use the [Course Description](../course-description.md) as
the source document for the concepts included in this course.
The course description uses the 2001 Bloom Taxonomy to order learning objectives.

## List of Concepts

We use generative AI to convert the course description into a [Concept List](./concept-list.md).
Each concept is in the form of a short Title Case label with most labels under 32 characters long.
This graph contains 485 concepts covering Python programming, MicroPython, NeoPixel hardware, color theory, animation patterns, electronics, computational thinking, interactivity, and project design.

## Concept Dependency Graph

We use generative AI to create a Directed Acyclic Graph (DAG). DAGs do not have cycles where
concepts depend on themselves. We provide the DAG in two formats: a [CSV file](learning-graph.csv) and a
[JSON file](learning-graph.json) that uses the vis-network JavaScript library format. The vis-network format uses `nodes`, `edges`, and `metadata`
elements with edges containing `from` and `to` properties. This makes it easy to view and edit the learning
graph using an editor built with the vis-network tools.

## Analysis and Documentation

### Course Description Quality Assessment

This report rates the overall quality of the course description for the purpose of generating a learning graph.

- Course description fields and content depth analysis
- Validates course description has sufficient depth for generating 200+ concepts
- Identifies content gaps and strengths
- Quality score: **91/100 — Excellent**

[View the Course Description Quality Assessment](course-description-assessment.md)

### Learning Graph Quality Validation

This report gives you an overall assessment of the quality of the learning graph.
It uses graph algorithms to look for specific quality patterns.

- Graph structure validation — all 485 concepts are connected in a single component
- DAG validation — no cycles detected ✅
- 14 foundational entry-point concepts
- 851 total dependency edges
- Average 1.81 dependencies per concept
- Longest dependency chain: 18 steps

[View the Learning Graph Quality Validation](quality-metrics.md)

### Concept Taxonomy

In order to see patterns in the learning graph, it is useful to assign colors
to each concept based on its category. We use generative AI to
create 12 categories for our concepts and then place each concept
into a single primary classifier.

- 12 categories covering all course topics
- No category exceeds 14.4% of total concepts
- Categories range from Python Programming (55) to Hardware Platforms (10)
- Clear 2–5 letter abbreviations for each category

[View the Concept Taxonomy](concept-taxonomy.md)

### Taxonomy Distribution

This report shows how many concepts fit into each category of the taxonomy.
Our goal is a balanced taxonomy where each category holds a
reasonable number of concepts and no category exceeds 30%.

| Category | ID | Count | % |
|----------|----|-------|---|
| Electronics and Circuits | ELEC | 70 | 14.4% |
| Animation Patterns | ANIM | 65 | 13.4% |
| Python Programming | PYTH | 55 | 11.3% |
| MicroPython and Pico | UPICO | 45 | 9.3% |
| NeoPixel Hardware | NEO | 40 | 8.2% |
| Color Theory | COLOR | 40 | 8.2% |
| Input and Interactivity | INPUT | 35 | 7.2% |
| Project Design | PROJ | 35 | 7.2% |
| Computational Thinking | CT | 30 | 6.2% |
| Dev Tools and Workflow | TOOLS | 30 | 6.2% |
| Mathematics | MATH | 30 | 6.2% |
| Hardware Platforms | HW | 10 | 2.1% |

[View the Taxonomy Distribution Report](./taxonomy-distribution.md)
