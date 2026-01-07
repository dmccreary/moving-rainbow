// Pico Light Sensor Circuit Simulation
// This simulation demonstrates how a photoresistor voltage divider works
// with a Raspberry Pi Pico's ADC (Analog to Digital Converter) input.
// The photoresistor detects ambient light level and the voltage at the
// junction point is read by ADC0, converted to a digital value 0-255.
// When it's bright, ADC reads high (255). When dark, ADC reads low (0).
// Components: 5V power supply, 47kΩ resistor, photoresistor

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
let ambientLight = 50;
let lightSlider;
let startButton;

// Circuit parameters
let lightLevel = 0.5; // 0 (dark) to 1 (bright)
let junctionVoltage = 0;
let adcValue = 0;

// Component positions - use relative positioning when possible
let numberComponentColums = 4;
let circuitColumWidth = canvasWidth / numberComponentColums;

// For a width-responsive design, scale relative to the canvasWidth
let powerRailY = margin + 40;
let groundRailY = 400;

// Column 1 components (voltage divider)
// Photoresistor on top (connected to +5V), 47K resistor on bottom (connected to GND)
let photoresistorX = circuitColumWidth;
let photoresistorY = 150;
let resistor47kX = circuitColumWidth;
let resistor47kY = 320;

// Column 2 component (ADC input icon)
let adcInputX = circuitColumWidth * 2;
let adcInputY = 235;

// Column 3 - ADC value display area
let adcDisplayX = circuitColumWidth * 3;
let adcDisplayY = 200;

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

  describe('Pico light sensor circuit simulation showing how a photoresistor voltage divider provides analog input to a Raspberry Pi Pico ADC.', LABEL);
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
  text("Pico Light Sensor Circuit", containerWidth/2, 10);

  // Reset text properties
  textSize(defaultTextSize);
  textAlign(LEFT, CENTER);

  // Get current light level (0 = dark, 1 = bright)
  lightLevel = lightSlider.value() / 100;

  // Calculate circuit values
  // Voltage divider with photoresistor on top, 47K on bottom:
  // Vjunction = Vcc * R_47k / (R_photo + R_47k)
  // As light increases, photoresistor resistance decreases, junction voltage INCREASES
  // As light decreases, photoresistor resistance increases, junction voltage DECREASES
  // Simplified model: when bright (lightLevel=1), low photoresistor R, high voltage
  // when dark (lightLevel=0), high photoresistor R, low voltage
  junctionVoltage = lightLevel * 5.0;

  // ADC value: maps junction voltage 0-5V to 0-255
  // Bright = high voltage = high ADC value (255)
  // Dark = low voltage = low ADC value (0)
  adcValue = Math.round(map(junctionVoltage, 0, 5, 0, 255));

  // Update animation time only when running
  // Speed adjusts based on ambient light - brighter = faster current flow
  if (isRunning) {
    animationTime += deltaTime * (0.5 + lightLevel * 1.5);
  }

  // Draw power rails
  drawPowerRails();

  // Draw circuit components (photoresistor on top, 47K resistor on bottom)
  drawPhotoresistor(photoresistorX, photoresistorY, 50, ambientLight);
  drawResistor(resistor47kX, resistor47kY, '47k\u03A9', 'vertical');
  drawADCInput(adcInputX, adcInputY);

  // Draw wiring with animated current flow
  drawCircuitWiring();

  // Draw ADC value display
  drawADCDisplay();

  // Draw voltage/current readings
  drawReadings();

  // Draw slider label in control region
  drawControlLabels();
}

function drawPowerRails() {
  // horizontal +5V rail (red) at the top
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

  // draw a yellow circle to show the amount of ambient light
  fill('yellow');
  stroke('orange');
  strokeWeight(2);
  circle(x - 60, y - 50, ambientLight);

  // place label to the right of the photoresistor
  fill('black');
  noStroke();
  textAlign(CENTER, CENTER);
  text("Ambient\nLight", x - 60, y + ambientLight * 0.5 - 20);
  textAlign(LEFT, CENTER);
  text("Photoresistor", x + 35, y);
}

function drawSerpentinePattern(x, y, patternWidth) {
  // Draw horizontal serpentine lines with curved corners
  let numLines = 7;
  let lineSpacing = patternWidth * 0.25;
  let amplitude = patternWidth * 0.45;
  let startY = y - (numLines - 1) * lineSpacing / 2;
  let cornerRadius = lineSpacing * 0.5;

  stroke(0);
  strokeWeight(2);
  noFill();

  beginShape();
  vertex(x - amplitude, startY);

  for (let i = 0; i < numLines - 1; i++) {
    let currentY = startY + i * lineSpacing;
    let nextY = startY + (i + 1) * lineSpacing;
    let midY = (currentY + nextY) / 2;

    if (i % 2 === 0) {
      vertex(x + amplitude - cornerRadius, currentY);
      quadraticVertex(x + amplitude, currentY, x + amplitude, midY);
      quadraticVertex(x + amplitude, nextY, x + amplitude - cornerRadius, nextY);
    } else {
      vertex(x - amplitude + cornerRadius, currentY);
      quadraticVertex(x - amplitude, currentY, x - amplitude, midY);
      quadraticVertex(x - amplitude, nextY, x - amplitude + cornerRadius, nextY);
    }
  }

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

function drawADCInput(x, y) {
  // Draw a rounded rectangle representing the Pico ADC input
  let boxWidth = 100;
  let boxHeight = 50;

  // Box body
  fill('#2E7D32'); // Green color like Pico board
  stroke('black');
  strokeWeight(2);
  rect(x - boxWidth/2, y - boxHeight/2, boxWidth, boxHeight, 8);

  // Inner rectangle for visual depth
  fill('#388E3C');
  noStroke();
  rect(x - boxWidth/2 + 4, y - boxHeight/2 + 4, boxWidth - 8, boxHeight - 8, 6);

  // ADC0 label
  fill('white');
  noStroke();
  textSize(14);
  textAlign(CENTER, CENTER);
  text('ADC0', x, y - 10);
  text('Pico Input', x, y + 10);

  // Input wire connection point (left side)
  fill('gold');
  stroke('black');
  strokeWeight(1);
  circle(x - boxWidth/2, y, 8);

  // Label the pin
  fill('black');
  noStroke();
  textSize(16);
  textAlign(RIGHT, CENTER);
  text('GP26', x - boxWidth/2 - 10, y + 20);
}

function drawADCDisplay() {
  // Large ADC value display on the right
  let displayWidth = 120;
  let displayHeight = 150;
  let x = adcDisplayX;
  let y = adcDisplayY;

  // Display box
  fill('#1a1a2e');
  stroke('#4a4a6a');
  strokeWeight(3);
  rect(x - displayWidth/2, y - displayHeight/2, displayWidth, displayHeight, 10);

  // Inner screen
  fill('#0f0f1a');
  noStroke();
  rect(x - displayWidth/2 + 8, y - displayHeight/2 + 8, displayWidth - 16, displayHeight - 16, 6);

  // ADC label
  fill('#00ff00');
  textSize(14);
  textAlign(CENTER, TOP);
  text('ADC Value', x, y - displayHeight/2 + 15);

  // Large ADC value
  textSize(48);
  textAlign(CENTER, CENTER);
  // Color based on value - green to red gradient
  let r = map(adcValue, 0, 255, 0, 255);
  let g = map(adcValue, 0, 255, 255, 100);
  fill(r, g, 50);
  text(adcValue, x, y + 10);

  // Range label
  fill('#888888');
  textSize(12);
  text('(0-255)', x, y + displayHeight/2 - 25);

  // Brightness interpretation (higher ADC = brighter light)
  textSize(11);
  fill('#aaaaaa');
  let brightnessText = "";
  if (adcValue > 230) {
    brightnessText = "Very Bright";
    fill('#ffff00');
  } else if (adcValue > 180) {
    brightnessText = "Bright";
    fill('#cccc00');
  } else if (adcValue > 100) {
    brightnessText = "Medium";
    fill('#888800');
  } else if (adcValue > 50) {
    brightnessText = "Dim";
    fill('#666600');
  } else {
    brightnessText = "Dark";
    fill('#444400');
  }
  text(brightnessText, x, y + displayHeight/2 - 10);
}

function drawCircuitWiring() {
  // Current flow speed varies with light level
  // Brighter light = lower resistance in photoresistor = faster current
  let speed = isRunning ? 0.1 + lightLevel * 0.2 : 0;
  let spacing = 0.8;

  // Current level also varies with light
  let currentLevel = 0.3 + lightLevel * 0.7;

  // Wire from +5V to photoresistor top
  drawAnimatedWire(photoresistorX, powerRailY, photoresistorX, photoresistorY - 25, speed, spacing, currentLevel);

  // Wire from photoresistor bottom to 47K resistor top (voltage divider midpoint)
  drawAnimatedWire(photoresistorX, photoresistorY + 25, resistor47kX, resistor47kY - 30, speed, spacing, currentLevel);

  // Wire from 47K resistor bottom to ground
  drawAnimatedWire(resistor47kX, resistor47kY + 30, resistor47kX, groundRailY, speed, spacing, currentLevel);

  // Wire from voltage divider junction to ADC input
  let junctionY = (photoresistorY + 25 + resistor47kY - 30) / 2;

  // Horizontal wire to ADC input
  drawAnimatedWire(photoresistorX, junctionY, adcInputX - 50, adcInputY, speed * 0.3, spacing, currentLevel * 0.5);

  // Junction point indicator
  fill('blue');
  noStroke();
  circle(photoresistorX, junctionY, 8);

  // Label the junction
  fill('navy');
  textSize(11);
  textAlign(LEFT, CENTER);
  text('Vjunction', photoresistorX + 10, junctionY - 15);
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
      let electronSize = 5 + currentLevel * 3;
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
    translate(circuitColumWidth * 1.5, 260);
    text('Junction Voltage: ' + junctionVoltage.toFixed(2) + 'V', 0, 40);
    text('Light Level: ' + (lightLevel * 100).toFixed(0) + '%', 0, 60);
    text('Photoresistor R: ' + ((1 - lightLevel) * 100 + 10).toFixed(0) + 'k\u03A9', 0, 80);
  pop();
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
  // Update component positions based on new width
  circuitColumWidth = canvasWidth / 4;
  photoresistorX = circuitColumWidth;
  resistor47kX = circuitColumWidth;
  adcInputX = circuitColumWidth * 2;
  adcDisplayX = circuitColumWidth * 3;
  lightSlider.size(containerWidth - sliderLeftMargin - 25);
}

function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) {
    containerWidth = Math.floor(container.getBoundingClientRect().width);
  }
  if (containerWidth < 400) containerWidth = 400;
  canvasWidth = containerWidth;
}
