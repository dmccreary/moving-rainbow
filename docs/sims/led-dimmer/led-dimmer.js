// LED Dimmer Circuit Simulation
// This simulation demonstrates how an LED dimmer circuit works using a potentiometer,
// transistor (2N2222), resistors, and an LED. The potentiometer controls the base voltage
// of the transistor, which in turn controls the current flow through the LED.
// Components: 5V power supply, Standard LED, 220Ω resistor, 2N2222 NPN transistor,
// 10kΩ base resistor, 20kΩ potentiometer

// Canvas dimensions following standard MicroSim layout
let canvasWidth = 400;
let drawHeight = 500;
let controlHeight = 70;
let canvasHeight = drawHeight + controlHeight;
let margin = 25;
let sliderLeftMargin = 160;
let defaultTextSize = 16;

// Global variables for responsive design
let containerWidth;
let containerHeight = canvasHeight;

// Simulation variables
let isRunning = false;
let animationTime = 0;
let potSlider;
let startButton;
let resetButton;

// Circuit parameters
let potValue = 0.5; // 0 to 1
let baseVoltage = 0;
let collectorCurrent = 0;
let ledBrightness = 0;

// Component positions
let powerRailY = 80;
let groundRailY = 450;
let potX = 100;
let potY = 265;
let transistorX = 320;
let transistorY = 350;
let ledX = 420;
let ledY = 180;
let resistor10kX = 210;
let resistor10kY = 300;
let resistor220X = 420;
let resistor220Y = 265;

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(containerWidth, containerHeight);
  canvas.parent(document.querySelector('main'));

  // Create potentiometer control slider
  potSlider = createSlider(0, 100, 50, 1);
  potSlider.position(sliderLeftMargin, drawHeight + 35);
  potSlider.size(containerWidth - sliderLeftMargin - 25);

  // Create start/pause button
  startButton = createButton('Start');
  startButton.position(10, drawHeight + 10);
  startButton.mousePressed(toggleSimulation);

  // Create reset button
  resetButton = createButton('Reset');
  resetButton.position(70, drawHeight + 10);
  resetButton.mousePressed(resetSimulation);

  describe('LED dimmer circuit simulation showing how a potentiometer controls LED brightness through a transistor.', LABEL);
}

function draw() {
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
  text("LED Dimmer Circuit", containerWidth/2, 10);

  // Reset text properties
  textSize(defaultTextSize);
  textAlign(LEFT, CENTER);

  // Get current potentiometer value
  potValue = potSlider.value() / 100;

  // Calculate circuit values
  // Base voltage varies from 0 to 5V based on potentiometer
  baseVoltage = potValue * 5.0;

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
  drawPotentiometer(potX, potY, potValue);
  drawResistor(resistor10kX, resistor10kY, '10kΩ', 'horizontal');
  drawTransistor(transistorX, transistorY);
  drawLED(ledX, ledY, ledBrightness);
  drawResistor(resistor220X, resistor220Y, '220Ω', 'vertical');

  // Draw wiring with animated current flow
  drawCircuitWiring();

  // Draw labels
  drawComponentLabels();

  // Draw voltage/current readings
  drawReadings();

  // Draw control labels
  drawControlLabels();
}

function drawPowerRails() {
  // +5V rail (red)
  stroke('red');
  strokeWeight(8);
  line(20, powerRailY, containerWidth - 20, powerRailY);

  // Ground rail (black)
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

function drawPotentiometer(x, y, value) {
  // Potentiometer body
  fill(80);
  stroke('black');
  strokeWeight(2);
  rect(x - 25, y - 40, 50, 80, 5);

  // Top terminal
  fill('silver');
  circle(x, y - 40, 8);

  // Bottom terminal
  circle(x, y + 40, 8);

  // Center tap terminal
  circle(x + 25, y, 8);

  // Knob
  fill(60);
  circle(x, y, 30);

  // Knob indicator
  stroke('white');
  strokeWeight(2);
  let angle = map(value, 0, 1, -135, 135);
  let indicatorX = x + 12 * cos(radians(angle));
  let indicatorY = y + 12 * sin(radians(angle));
  line(x, y, indicatorX, indicatorY);

  // Resistance symbol inside
  noFill();
  stroke('white');
  strokeWeight(1);
  for (let i = 0; i < 3; i++) {
    let zigX = x - 8 + i * 8;
    line(zigX, y - 5, zigX + 4, y + 5);
    line(zigX + 4, y + 5, zigX + 8, y - 5);
  }
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
  rect(-20, -6, 40, 12);

  // Color bands (simplified)
  fill('brown');
  noStroke();
  rect(-12, -6, 3, 12);
  rect(-4, -6, 3, 12);
  rect(4, -6, 3, 12);

  // Leads
  stroke('gray');
  strokeWeight(2);
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
  fill(50);
  stroke('black');
  strokeWeight(2);
  circle(x, y, 50);

  // Base line
  stroke('gray');
  strokeWeight(3);
  line(x - 10, y - 15, x - 10, y + 15);

  // Collector line
  line(x - 10, y - 10, x + 15, y - 25);

  // Emitter line with arrow
  line(x - 10, y + 10, x + 15, y + 25);

  // Arrow on emitter
  fill('gray');
  noStroke();
  push();
  translate(x + 15, y + 25);
  let arrowAngle = atan2(15, 25);
  rotate(arrowAngle);
  triangle(0, 0, -6, -3, -6, 3);
  pop();

  // Terminal labels
  fill('white');
  noStroke();
  textSize(10);
  textAlign(CENTER);
  text('C', x + 20, y - 30);
  text('B', x - 25, y);
  text('E', x + 20, y + 35);
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
  stroke('gray');
  strokeWeight(2);
  line(x, y - 15, x, y - 30);  // Anode lead
  line(x, y + 15, x, y + 30);  // Cathode lead
}

function drawCircuitWiring() {
  let speed = isRunning ? 0.15 : 0;
  let spacing = 0.8;

  // Wire from +5V to potentiometer top
  drawAnimatedWire(potX, powerRailY, potX, potY - 40, speed, spacing, collectorCurrent);

  // Wire from potentiometer bottom to ground
  drawAnimatedWire(potX, potY + 40, potX, groundRailY, speed, spacing, collectorCurrent);

  // Wire from potentiometer center tap to 10k resistor
  drawAnimatedWire(potX + 25, potY, resistor10kX - 30, resistor10kY, speed, spacing, collectorCurrent);

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

function drawComponentLabels() {
  fill('black');
  noStroke();
  textSize(11);
  textAlign(CENTER);

  text('20kΩ POT', potX, potY + 60);
  text('2N2222', transistorX, transistorY + 55);
  text('LED', ledX + 30, ledY);
}

function drawReadings() {
  fill('navy');
  noStroke();
  textSize(13);
  textAlign(LEFT);

  text('Base V: ' + baseVoltage.toFixed(2) + 'V', 10, 40);
  text('Current: ' + (collectorCurrent * 100).toFixed(0) + '%', 10, 60);
  text('LED: ' + (ledBrightness * 100).toFixed(0) + '%', 10, 80);
}

function drawControlLabels() {
  push();
  translate(0, 30);
  fill('black');
  noStroke();
  textSize(defaultTextSize);
  textAlign(LEFT, CENTER);

  text('Potentiometer: ' + (potValue * 100).toFixed(0) + '%', 10, drawHeight + 15);
  pop();
}

function toggleSimulation() {
  isRunning = !isRunning;
  startButton.html(isRunning ? 'Pause' : 'Start');
}

function resetSimulation() {
  potSlider.value(50);
  animationTime = 0;
  isRunning = false;
  startButton.html('Start');
  redraw();
}

function windowResized() {
  updateCanvasSize();
  resizeCanvas(containerWidth, containerHeight);
  redraw();

  potSlider.size(containerWidth - sliderLeftMargin - 25);
}

function updateCanvasSize() {
  const container = document.querySelector('main').getBoundingClientRect();
  containerWidth = Math.floor(container.width);
  if (containerWidth < 400) containerWidth = 400;
  canvasWidth = containerWidth;
}
