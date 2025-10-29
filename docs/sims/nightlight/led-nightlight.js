// LED Nightlight Circuit Simulation
// This simulation demonstrates how an LED nightlight circuit works using a photoresistor,
// transistor (2N2222), resistors, and an LED. The photoresistor detects ambient light level
// and controls the base voltage of the transistor, which in turn controls the LED brightness.
// The LED gets brighter as the ambient light gets darker.
// Components: 5V power supply, Standard LED, 220Ω resistor, 2N2222 NPN transistor,
// 10kΩ base resistor, 100kΩ resistor, photoresistor

// Canvas dimensions following standard MicroSim layout
let canvasWidth = 600;
let drawHeight = 440;
let controlHeight = 40;
let canvasHeight = drawHeight + controlHeight;
let margin = 20;
let sliderLeftMargin = 230;
let defaultTextSize = 16;

// Global variables for responsive design
let containerWidth;
let containerHeight = canvasHeight;

// Simulation variables
let isRunning = false;
let animationTime = 0;
let ambientLight = .5;
let lightSlider;
let startButton;
let resetButton;

// Circuit parameters
let lightLevel = 0.5; // 0 (dark) to 1 (bright)
let baseVoltage = 0;
let collectorCurrent = 0;
let ledBrightness = 0;

// Component positions - use relative positioning when possible

let numberComponentColums = 5;
let circuitColumWidth = canvasWidth / numberComponentColums;

// For a width-responsive design, scale relative to the canvasWidth
// margin + title height + 5v label height
let powerRailY = margin + 40;
let groundRailY = 400;

// Column 1 components
let resistor100kX = circuitColumWidth;
let resistor100kY = 150;
let photoresistorX = circuitColumWidth;
let photoresistorY = 320;

// Column 2 components
let resistor10kX = circuitColumWidth * 2;
let resistor10kY = 280;

// Column 3 component
let transistorX = circuitColumWidth * 3;
let transistorY = resistor10kY;
let ledX = circuitColumWidth * 4;;
let ledY = powerRailY + 40;

// Column 4 component
let resistor220X = ledX;
let resistor220Y = ledY + 80;

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(containerWidth, containerHeight);
  canvas.parent(document.querySelector('main'));

  // Create light level control slider
  lightSlider = createSlider(0, 100, 50, 1);
  lightSlider.position(sliderLeftMargin, drawHeight + 10);
  lightSlider.size(containerWidth - sliderLeftMargin - 25);

  // Create start/pause button
  startButton = createButton('Start');
  startButton.position(10, drawHeight + 10);
  startButton.mousePressed(toggleSimulation);

  describe('LED nightlight circuit simulation showing how a photoresistor controls LED brightness through a transistor.', LABEL);
}

function draw() {
  updateCanvasSize();
  ambientLight = lightSlider.value();
  // Draw simulation area background
  fill('aliceblue');
  stroke('silver');
  strokeWeight(1);
  rect(0, 0, containerWidth, drawHeight);

  // Draw controls area background
  fill('white');
  stroke('silver');
  strokeWeight(1);
  rect(0, drawHeight, containerWidth, controlHeight);

  // Draw title
  fill('black');
  noStroke();
  textSize(20);
  textAlign(CENTER, TOP);
  text("LED Nightlight Circuit", containerWidth/2, 10);

  // Reset text properties
  textSize(defaultTextSize);
  textAlign(LEFT, CENTER);

  // Get current light level (0 = dark, 1 = bright)
  lightLevel = lightSlider.value() / 100;

  // Calculate circuit values
  // As light decreases (photoresistor resistance increases), base voltage increases
  // Inverted relationship: dark = high voltage, bright = low voltage
  baseVoltage = (1 - lightLevel) * 5.0;

  // Transistor starts conducting around 0.7V, full on around 2V
  if (baseVoltage < 0.7) {
    collectorCurrent = 0;
  } else {
    collectorCurrent = map(baseVoltage, 0.7, 5.0, 0, 1, true);
  }

  // LED brightness proportional to collector current
  ledBrightness = collectorCurrent;

  // Update animation time only when running
  if (isRunning) {
    animationTime += deltaTime;
  }

  // Draw power rails
  drawPowerRails();

  // Draw circuit components
  drawResistor(resistor100kX, resistor100kY, '100kΩ', 'vertical');
  drawPhotoresistor(photoresistorX, photoresistorY, 50, ambientLight);
  drawResistor(resistor10kX, resistor10kY, '10kΩ', 'horizontal');
  drawTransistor(transistorX, transistorY);
  drawLED(ledX, ledY, ledBrightness);
  drawResistor(resistor220X, resistor220Y, '220Ω', 'vertical');

  // Draw wiring with animated current flow
  drawCircuitWiring();

  // Draw voltage/current readings
  drawReadings();

  // Draw slider label in control region
  drawControlLabels();
}

function drawPowerRails() {
  // horisontal +5V rail (red) at the top
  stroke('red');
  strokeWeight(8);
  line(20, powerRailY, containerWidth - 20, powerRailY);

  // horizontal Ground rail (black) at the bottom
  stroke('black');
  strokeWeight(8);
  line(20, groundRailY, containerWidth - 20, groundRailY);

  // Labels
  fill('red');
  noStroke();
  textSize(16);
  textAlign(CENTER);
  text('+5V', containerWidth/2, powerRailY - 15);

  fill('black');
  text('GND', containerWidth/2, groundRailY + 20);
}

function drawPhotoresistor(x, y, size, ambientLight) {
  let radius = size / 2;

  // Draw outer circle (component body)
  fill(240);
  stroke(0);
  strokeWeight(3);
  circle(x, y, size);

  // Draw inner light-sensitive area (slightly smaller circle)
  fill('white');
  strokeWeight(2);
  circle(x, y, size * 0.85);

  // Draw serpentine pattern (horizontal zigzag lines)
  drawSerpentinePattern(x, y, size * 0.4);

  // Draw two terminal connection points
  fill('lightgray');
  stroke(0);
  strokeWeight(1);
  let terminalSize = size * 0.10;
  circle(x - radius * 0.6, y, terminalSize);
  circle(x + radius * 0.6, y, terminalSize);
  
  // draw a yellow circle to show the amount of amblient light
  fill('yellow');
  stroke('silver');
  circle(x-60,y-50,ambientLight);
  
  // place label to the right of the photoresistor
  fill('black');
  noStroke();
  textAlign(CENTER, CENTER);
  text("Ambient\nLight", x-60, y+ambientLight*.5 - 20);
  textAlign(LEFT, CENTER);
  text("Photoresistor", x+35, y);
}

function drawSerpentinePattern(x, y, patternWidth) {
  // Draw horizontal serpentine lines with curved corners
  let numLines = 7; // number of horizontal segments
  let lineSpacing = patternWidth * 0.25; // vertical spacing between lines
  let amplitude = patternWidth * 0.45; // how wide the zigzag goes
  let startY = y - (numLines - 1) * lineSpacing / 2;
  let cornerRadius = lineSpacing * 0.5; // radius for curved corners

  stroke(0);
  strokeWeight(2);
  noFill();

  // Draw the serpentine path as a continuous curved line
  beginShape();

  // Start at top left
  vertex(x - amplitude, startY);

  for (let i = 0; i < numLines - 1; i++) {
    let currentY = startY + i * lineSpacing;
    let nextY = startY + (i + 1) * lineSpacing;
    let midY = (currentY + nextY) / 2;

    if (i % 2 === 0) {
      // Moving right, then curve down on right side
      // Horizontal line to corner start
      vertex(x + amplitude - cornerRadius, currentY);
      // First curve: horizontal to vertical (top-right quarter circle)
      quadraticVertex(x + amplitude, currentY, x + amplitude, midY);
      // Second curve: vertical to horizontal (bottom-right quarter circle)
      quadraticVertex(x + amplitude, nextY, x + amplitude - cornerRadius, nextY);
    } else {
      // Moving left, then curve down on left side
      // Horizontal line to corner start
      vertex(x - amplitude + cornerRadius, currentY);
      // First curve: horizontal to vertical (top-left quarter circle)
      quadraticVertex(x - amplitude, currentY, x - amplitude, midY);
      // Second curve: vertical to horizontal (bottom-left quarter circle)
      quadraticVertex(x - amplitude, nextY, x - amplitude + cornerRadius, nextY);
    }
  }

  // Final horizontal line
  let lastY = startY + (numLines - 1) * lineSpacing;
  if ((numLines - 1) % 2 === 0) {
    vertex(x + amplitude, lastY);
  } else {
    vertex(x - amplitude, lastY);
  }

  endShape();
}

function drawResistor(x, y, label, orientation) {
  push();
  translate(x, y);
  if (orientation === 'vertical') {
    rotate(HALF_PI);
  }

  // Resistor body
  fill('tan');
  stroke('black');
  strokeWeight(1);
  rect(-20, -6, 40, 12, 4);

  // Color bands (simplified)
  fill('brown');
  noStroke();
  rect(-12, -6, 3, 12);
  rect(-4, -6, 3, 12);
  rect(4, -6, 3, 12);

  // Leads
  stroke('black');
  strokeWeight(3);
  line(-30, 0, -20, 0);
  line(20, 0, 30, 0);

  // Label
  fill('black');
  noStroke();
  textSize(12);
  textAlign(CENTER);
  text(label, 0, orientation === 'vertical' ? 20 : -15);

  pop();
}

function drawTransistor(x, y) {
  // Transistor circle
  fill('lightgray');
  stroke('black');
  strokeWeight(2);
  circle(x, y, 50);

  // Base line
  stroke('black');
  strokeWeight(3);
  line(x - 10, y - 15, x - 10, y + 15);
  
  // Base line
  line(x - 30, y, x - 10, y);

  // Collector line
  line(x - 10, y - 10, x + 15, y - 25);

  // Emitter line with arrow
  line(x - 10, y + 10, x + 15, y + 25);

  // Arrow on emitter
  fill('gray');
  stroke('black');
  push();
    translate(x + 15, y + 25);
    let arrowAngle = atan2(15, 25);
    rotate(arrowAngle);
    triangle(0, 0, -6, -3, -6, 3);
  pop();

  // Terminal labels
  fill('black');
  noStroke();
  textSize(12);
  textAlign(CENTER);
  // left just above base wire
  text('B', x - 30, y - 10);
  // Upper right
  text('C', x + 15, y - 35);
  // Lower Left
  text('E', x + 25, y + 35);
  // label to right
  text('2N2222 NPN', transistorX + 70, transistorY);
}

function drawLED(x, y, brightness) {
  // LED body
  let ledColor = color(255, 0, 0, brightness * 255);
  fill(ledColor);
  stroke('darkred');
  strokeWeight(2);

  // LED as triangle (anode symbol)
  triangle(x - 15, y + 15, x + 15, y + 15, x, y - 15);

  // Cathode bar
  stroke('black');
  strokeWeight(3);
  line(x - 15, y + 15, x + 15, y + 15);

  // Glow effect when lit
  if (brightness > 0.1) {
    noStroke();
    fill(255, 100, 100, brightness * 100);
    circle(x, y, 60);
    fill(255, 200, 200, brightness * 150);
    circle(x, y, 40);
  }

  // Light rays when bright
  if (brightness > 0.3) {
    stroke(255, 255, 100, brightness * 200);
    strokeWeight(2);
    for (let i = 0; i < 8; i++) {
      let angle = i * 45;
      let x1 = x + 20 * cos(radians(angle));
      let y1 = y + 20 * cos(radians(angle));
      let x2 = x + 35 * cos(radians(angle));
      let y2 = y + 35 * sin(radians(angle));
      line(x1, y1, x2, y2);
    }
  }

  // Leads
  stroke('black');
  strokeWeight(3);
  line(x, y - 15, x, y - 30);  // Anode lead
  line(x, y + 15, x, y + 30);  // Cathode lead
  
  noStroke();
  fill('black')
  text('LED', ledX - 50, ledY);
}

function drawCircuitWiring() {
  let speed = isRunning ? 0.15 : 0;
  let spacing = 0.8;

  // Wire from +5V to 100k resistor top
  drawAnimatedWire(resistor100kX, powerRailY, resistor100kX, resistor100kY - 30, speed, spacing, collectorCurrent);

  // Wire from 100k resistor bottom to photoresistor top (voltage divider midpoint)
  let midpointY = (resistor100kY + photoresistorY) / 2;
  drawAnimatedWire(resistor100kX, resistor100kY + 30, resistor100kX, photoresistorY - 25, speed, spacing, collectorCurrent);

  // Wire from photoresistor bottom to ground
  drawAnimatedWire(photoresistorX, photoresistorY + 25, photoresistorX, groundRailY, speed, spacing, collectorCurrent);

  // Wire from voltage divider midpoint to 10k resistor
  let tapY = (resistor100kY + 30 + photoresistorY - 40) / 2;
  drawAnimatedWire(photoresistorX, tapY, resistor10kX - 30, resistor10kY, speed, spacing, collectorCurrent);

  // Wire from 10k resistor to transistor base
  drawAnimatedWire(resistor10kX + 30, resistor10kY, transistorX - 25, transistorY, speed, spacing, collectorCurrent);

  // Wire from +5V to LED anode
  drawAnimatedWire(ledX, powerRailY, ledX, ledY - 30, speed, spacing, collectorCurrent);

  // Wire from LED cathode to 220Ω resistor top
  drawAnimatedWire(ledX, ledY + 30, ledX, resistor220Y - 30, speed, spacing, collectorCurrent);

  // Wire from 220Ω resistor bottom to transistor collector
  drawAnimatedWire(resistor220X, resistor220Y + 30, transistorX + 15, transistorY - 25, speed, spacing, collectorCurrent);

  // Wire from transistor emitter to ground
  drawAnimatedWire(transistorX + 15, transistorY + 25, transistorX + 15, groundRailY, speed, spacing, collectorCurrent);
}

function drawAnimatedWire(x1, y1, x2, y2, speed, spacing, currentLevel) {
  // Calculate wire properties
  let distance = dist(x1, y1, x2, y2);
  let spacingPixels = spacing * 50;
  let numElectrons = Math.floor(distance / spacingPixels);

  // Draw the wire
  stroke('black');
  strokeWeight(3);
  line(x1, y1, x2, y2);

  // Draw moving electrons only if there's current
  if (numElectrons > 0 && currentLevel > 0.05) {
    fill('red');
    noStroke();

    for (let i = 0; i <= numElectrons; i++) {
      let electronPos = (animationTime * speed + i * spacingPixels) % distance;
      let x = lerp(x1, x2, electronPos / distance);
      let y = lerp(y1, y2, electronPos / distance);

      // Electron size based on current level
      let electronSize = 6 + currentLevel * 4;
      circle(x, y, electronSize);
    }
  }
}

function drawReadings() {
  fill('navy');
  noStroke();
  textSize(13);
  textAlign(LEFT);
  push();
    translate(circuitColumWidth*1.5, 100);
    text('Base V: ' + baseVoltage.toFixed(2) + 'V', 0, 40);
    text('Current in LED: ' + (collectorCurrent * 20).toFixed(0) + ' milliamps', 0, 60);
    text('LED Brightness: ' + (ledBrightness * 100).toFixed(0) + '%', 0, 80);
  pop()
}

function drawControlLabels() {
  fill('black');
  noStroke();
  textSize(defaultTextSize);
  textAlign(LEFT, CENTER);
  text('Ambient Light: ' + (lightLevel * 100).toFixed(0) + '%', 70, drawHeight + 20);
}

function toggleSimulation() {
  isRunning = !isRunning;
  startButton.html(isRunning ? 'Pause' : 'Start');
}

function windowResized() {
  updateCanvasSize();
  resizeCanvas(containerWidth, containerHeight);
  redraw();
  // put all component x positions here...
  circuitColumWidth = canvasWidth / 5
  resistor100kX = circuitColumWidth;
  photoresistorX = circuitColumWidth;
  transistorX = circuitColumWidth * 3;
  ledX = circuitColumWidth * 4;;
  resistor10kX = circuitColumWidth * 2;
  resistor220X = ledX;
  lightSlider.size(containerWidth - sliderLeftMargin - 25);
}

function updateCanvasSize() {
  const container = document.querySelector('main').getBoundingClientRect();
  containerWidth = Math.floor(container.width);
  if (containerWidth < 400) containerWidth = 400;
  canvasWidth = containerWidth;
}
