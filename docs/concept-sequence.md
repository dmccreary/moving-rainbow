# Moving Rainbow: 200 Key Concepts in Teaching Sequence

This document lists the 200 most important concepts in the Moving Rainbow course, ordered by the sequence they should be taught. Concepts build progressively from foundational prerequisites through advanced capstone project skills.

## Prerequisites & Foundations (Concepts 1-20)

### Basic Computer Skills
1. Using a keyboard and mouse
2. Opening and closing programs
3. Creating and saving files
4. Understanding file organization (folders and directories)
5. Copying and pasting text

### Basic Math Concepts
6. Whole numbers and counting (0-255)
7. Addition and subtraction
8. Multiplication and division
9. Percentages and fractions
10. Coordinate systems (x, y positions)

### Color Basics
11. Primary colors (red, blue, yellow)
12. Additive color mixing
13. RGB color model concept
14. Light vs. pigment color mixing
15. Color intensity and brightness

### Electricity Safety
16. Positive and negative terminals
17. Voltage as electrical pressure
18. Current as electrical flow
19. Safe handling of electronic components
20. USB power safety

## Week 1-2: Hardware Setup & First Programs (Concepts 21-50)

### Hardware Components
21. Microcontroller definition and purpose
22. Raspberry Pi Pico identification
23. GPIO pins and their function
24. LED (Light Emitting Diode) basics
25. Addressable LED concept
26. NeoPixel/WS2812B chip
27. Breadboard purpose and layout
28. Breadboard tie points and connections
29. USB cable types (micro-USB, USB-A)
30. Power vs. data connections

### Circuit Basics
31. Complete circuit path
32. Ground (GND) reference point
33. Power supply (5V, 3.3V)
34. Data signal line
35. Three-wire LED connection (power, ground, data)
36. Wire color conventions (red=power, black=ground)
37. Polarity (positive/negative orientation)
38. Short circuit prevention
39. Current limiting concepts
40. Power consumption basics

### Software Setup
41. IDE (Integrated Development Environment)
42. Thonny Python editor
43. Installing software on your computer
44. USB device recognition
45. Firmware definition
46. MicroPython language
47. BOOTSEL button function
48. Drag-and-drop programming
49. Serial console for output
50. File system on microcontroller

### First Python Concepts
51. Program definition
52. Code execution (running a program)
53. Comments (# symbol)
54. Print statement for output
55. Import statement
56. Library/module concept
57. Python indentation rules
58. Syntax (code grammar rules)
59. Syntax errors and how to read them
60. Case sensitivity in code

## Week 2-3: Basic Programming (Concepts 61-90)

### Variables & Data Types
61. Variable as named storage
62. Assignment operator (=)
63. Integer data type
64. Floating point (decimal) numbers
65. String (text) data type
66. Boolean (True/False) values
67. Variable naming rules
68. Constant values
69. Type conversion
70. Mathematical operators (+, -, *, /)

### Working with LEDs
71. Pixel as individual LED unit
72. Pixel indexing (starting at 0)
73. RGB tuple format (red, green, blue)
74. Color values (0-255 range)
75. 8-bit color depth
76. Setting a single pixel color
77. strip.write() command
78. Turning LEDs on and off
79. Creating custom colors
80. Black as all LEDs off (0,0,0)

### Time & Delays
81. Sleep function
82. Delay concept
83. Seconds as time unit
84. Milliseconds (thousandths of a second)
85. Animation frame rate
86. Timing control in animations
87. Program execution speed
88. Pause vs. stop
89. Real-time vs. programmed time
90. Time as a loop control

## Week 3-4: Loops & Motion (Concepts 91-120)

### Iteration & Loops
91. Loop definition (repetition)
92. While loop structure
93. While True (infinite loop)
94. For loop structure
95. Range function
96. Loop counter variable
97. Iteration (single loop execution)
98. Loop body (indented code)
99. Break statement (exit loop)
100. Continue statement (skip iteration)

### Motion Concepts
101. Animation as changing images over time
102. Frame-by-frame animation
103. Position variable for tracking location
104. Increment (adding one)
105. Decrement (subtracting one)
106. Moving a pixel to the next position
107. Direction of motion
108. Speed control through delays
109. Smooth motion techniques
110. Visual persistence

### Range & Boundaries
111. Strip length (NUMBER_PIXELS)
112. First pixel index (0)
113. Last pixel index (NUMBER_PIXELS - 1)
114. Index out of bounds error
115. Boundary checking
116. Wrapping around (going from end to start)
117. Modulo operator (%)
118. Remainder after division
119. Circular motion
120. Bounce effects (reversing direction)

### Arrays & Lists
121. Array/list concept (ordered collection)
122. Creating a list in Python
123. Accessing list elements by index
124. List length (len function)
125. Adding items to lists
126. Removing items from lists
127. Iterating through lists
128. Tuple (immutable list)
129. List of colors
130. Storing animation frames

## Week 4-5: Patterns & Functions (Concepts 131-160)

### Pattern Recognition
131. Repeating patterns in code
132. Pattern in animation sequences
133. Identifying common code blocks
134. DRY principle (Don't Repeat Yourself)
135. Code reuse benefits
136. Abstracting common operations
137. Generalizing specific solutions
138. Finding similarities in problems
139. Template-based solutions
140. Algorithm patterns

### Functions
141. Function definition (def keyword)
142. Function name
143. Function parameters (inputs)
144. Function body
145. Return value (output)
146. Calling a function
147. Function reusability
148. Local variables
149. Global variables
150. Variable scope

### Color Theory
151. Color wheel concept
152. Hue (pure color)
153. Saturation (color intensity)
154. Value/brightness
155. Complementary colors
156. Analogous colors
157. Color harmony
158. Warm vs. cool colors
159. Color transitions
160. Gradient effects

### Common Animation Functions
161. Color wipe pattern
162. Rainbow effect
163. Color wheel function
164. Fade in/fade out
165. Pulse effect
166. Chase pattern
167. Fill and empty
168. Random colors
169. Sparkle effect
170. Wave patterns

## Week 5-6: Conditionals & Interactivity (Concepts 171-190)

### Conditional Logic
171. If statement
172. Condition (test that returns True/False)
173. Comparison operators (==, !=, <, >, <=, >=)
174. Logical operators (and, or, not)
175. Else clause
176. Elif (else if) clause
177. Nested conditionals
178. Boolean expressions
179. Truthiness in Python
180. Conditional execution flow

### Button Input
181. Push button (momentary switch)
182. Button press detection
183. Digital input
184. Pull-down resistor concept
185. Button state (pressed/not pressed)
186. Polling vs. interrupts
187. Interrupt handler function
188. IRQ (Interrupt Request)
189. Event-driven programming
190. Callback functions

### Debouncing & Timing
191. Bounce in mechanical switches
192. Debouncing technique
193. Time-based debouncing
194. ticks_ms() function
195. Time difference calculation
196. Minimum time between events
197. False trigger prevention
198. State change detection
199. Rising edge vs. falling edge
200. Software vs. hardware debouncing

## Week 6-7: Advanced Topics (Concepts 201-230)

*(Continuing the numbering - note: this extends beyond 200 to complete the sequence)*

### Mode-Based Programs
201. Mode concept (different operating states)
202. Mode variable
203. Mode counter
204. Mode selection with buttons
205. Mode wrapping (cycling through modes)
206. Mode switching logic
207. Mode names list
208. Current mode display
209. Mode change detection
210. State machine concept

### Advanced Animations
211. Comet tail effect
212. Brightness levels array
213. Scaling colors for dimming
214. Larson scanner effect
215. Theater chase pattern
216. Twinkle/sparkle with random
217. Ripple effect
218. Heartbeat pattern
219. Candle flicker simulation
220. Fire effect algorithm

### Random Numbers
221. Random number generation
222. urandom module
223. randint() function
224. Random range specification
225. Seed concept
226. Pseudo-random vs. true random
227. Random color generation
228. Random position selection
229. Random timing variations
230. Controlled randomness

### Optimization & Efficiency
231. Code efficiency
232. Minimizing delays
233. Reducing redundant calculations
234. Memory usage
235. Battery life considerations
236. Power consumption optimization
237. Brightness vs. power tradeoff
238. Efficient looping
239. Avoiding unnecessary writes
240. Performance tuning

## Week 7: Sensors & Advanced Input (Concepts 241-260)

### Analog Input
241. Analog vs. digital signals
242. ADC (Analog-to-Digital Converter)
243. Voltage reading
244. Potentiometer (variable resistor)
245. Reading potentiometer values
246. Value scaling and mapping
247. Smoothing noisy readings
248. Threshold detection
249. Continuous value ranges
250. Converting analog to control parameters

### Light Sensing
251. Photoresistor operation
252. Light-dependent resistance
253. Voltage divider circuit
254. Ambient light detection
255. Day/night detection
256. Automatic brightness adjustment
257. Nightlight logic
258. Light threshold setting
259. Hysteresis (preventing flicker)
260. Environmental sensing

### Project Planning Concepts
261. Requirements gathering
262. Feature list creation
263. Prioritizing features
264. Must-have vs. nice-to-have
265. Breaking project into phases
266. Milestone planning
267. Timeline estimation
268. Resource requirements
269. Parts list creation
270. Budget planning

## Week 8: Capstone Planning (Concepts 271-290)

### Design Process
271. Brainstorming techniques
272. Sketching ideas
273. Wireframing
274. Prototype concept
275. Proof of concept
276. Iterative design
277. User requirements
278. Design constraints
279. Technical feasibility
280. Creative problem solving

### Documentation
281. Code comments best practices
282. Function documentation
283. Inline comments
284. Project description
285. README file
286. Setup instructions
287. Usage guide
288. Troubleshooting guide
289. Known issues list
290. Future improvements section

### Circuit Design
291. Circuit diagram reading
292. Wiring diagram creation
293. Component placement
294. Wire routing
295. Connection testing
296. Continuity checking
297. Power distribution
298. Ground connections
299. Signal integrity
300. Cable management

### Algorithm Design
301. Pseudocode writing
302. Flowchart creation
303. Step-by-step planning
304. Input-process-output model
305. Edge case identification
306. Error handling strategy
307. Testing scenarios
308. Expected behaviors
309. Failure modes
310. Recovery procedures

## Week 9: Implementation (Concepts 311-340)

### Debugging
311. Bug definition
312. Debugging process
313. Print debugging
314. Variable inspection
315. Logic errors vs. syntax errors
316. Systematic troubleshooting
317. Isolating problems
318. Testing hypotheses
319. Error messages interpretation
320. Stack traces

### Testing
321. Unit testing concept
322. Integration testing
323. System testing
324. Test plan creation
325. Test cases
326. Expected vs. actual results
327. Regression testing
328. User acceptance testing
329. Stress testing
330. Edge case testing

### Code Organization
331. Code structure
332. Logical grouping
333. Helper functions
334. Main program flow
335. Initialization section
336. Configuration section
337. Constants at top
338. Function definitions before use
339. Main loop at bottom
340. Clean code principles

### Version Control
341. Git basics
342. Repository concept
343. Commit (saving changes)
344. Commit message
345. Version history
346. Branching concept
347. Reverting changes
348. Tracking changes over time
349. Collaboration workflow
350. Backup through version control

## Week 10: Presentation & Reflection (Concepts 351-370)

### Technical Communication
351. Explaining technical concepts simply
352. Audience awareness
353. Demonstration techniques
354. Live demo preparation
355. Backup plans for demos
356. Visual aids
357. Slide presentation design
358. Speaking clearly and confidently
359. Answering questions
360. Accepting feedback gracefully

### Project Presentation
361. Problem statement
362. Solution overview
363. Design decisions explanation
364. Challenges encountered
365. How challenges were overcome
366. Demonstration of features
367. Code highlights
368. Future enhancements
369. Lessons learned
370. Acknowledgments

## Advanced & Extension Concepts (371-400)

### Professional Skills
371. Time management
372. Meeting deadlines
373. Asking for help
374. Giving help to others
375. Peer review
376. Constructive criticism
377. Iterative improvement
378. Learning from failure
379. Growth mindset
380. Persistence

### Hardware Extensions
381. Battery selection
382. Battery capacity (mAh)
383. Battery life calculation
384. Rechargeable batteries
385. LiPo battery safety
386. Charging circuits
387. Voltage regulators
388. Power switches
389. Portable power solutions
390. Wearable electronics considerations

### Software Extensions
391. Libraries and modules
392. Code reusability
393. Open source software
394. Software licensing
395. Code sharing etiquette
396. Reading others' code
397. Adapting example code
398. Contributing to projects
399. Community resources
400. Continuous learning

## Computational Thinking Throughout

These meta-concepts are reinforced across all weeks:

**Decomposition**
- Breaking complex animations into simple steps
- Dividing projects into manageable tasks
- Separating concerns (display, logic, input)

**Pattern Recognition**
- Identifying repeating code sequences
- Recognizing common animation structures
- Finding similarities across different effects

**Abstraction**
- Using functions to hide complexity
- Creating reusable components
- Focusing on essential features
- Generalizing specific solutions

**Algorithm Design**
- Planning step-by-step procedures
- Optimizing for efficiency
- Handling edge cases
- Creating robust solutions

**Debugging & Testing**
- Systematic problem solving
- Hypothesis testing
- Iterative refinement
- Learning from errors

---

## Teaching Notes

### Concept Dependencies
Many concepts build on earlier ones. For example:
- Functions require understanding variables and parameters
- Loops need comprehension of conditionals for exit conditions
- Advanced animations combine colors, timing, and mathematical operations

### Spiral Learning
Some concepts (like debugging, documentation, and testing) should be revisited multiple times throughout the course with increasing depth.

### Differentiation
- **Struggling students**: Focus on concepts 1-200, ensuring solid fundamentals
- **Advanced students**: Explore concepts 201-400 and beyond, adding complexity
- **Project variations**: Adjust complexity based on student readiness

### Assessment Checkpoints
Key concepts to assess for mastery:
- Week 2: Concepts 1-60 (setup and basic programming)
- Week 4: Concepts 61-130 (variables, loops, motion)
- Week 6: Concepts 131-200 (functions, conditionals, interactivity)
- Week 8: Concepts 201-310 (planning and design)
- Week 10: Concepts 311-400 (implementation and communication)

This sequence ensures students build a strong foundation before tackling more complex concepts, with computational thinking principles woven throughout the entire curriculum.
