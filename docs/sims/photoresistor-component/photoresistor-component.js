// Photoresistor Component Visualization
// This sketch draws a minimalistic black and white representation of a photoresistor
// showing its characteristic serpentine (zigzag) pattern that makes it light-sensitive.

// Canvas dimensions
let canvasWidth = 400;
let canvasHeight = 400;

// Global variables for responsive design
let containerWidth;
let containerHeight = canvasHeight;

// Component parameters
let photoresistorSize = 180; // diameter of the circular component
let centerX, centerY;

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(containerWidth, containerHeight);
  canvas.parent(document.querySelector('main'));

  // Calculate center position
  centerX = containerWidth / 2;
  centerY = containerHeight / 2;

  // Static drawing - no animation needed
  noLoop();

  describe('Minimalistic black and white illustration of a photoresistor component showing its characteristic serpentine pattern.', LABEL);
}

function draw() {
  // White background
  background(255);

  // Update center position for responsive design
  centerX = containerWidth / 2;
  centerY = containerHeight / 2;

  // Draw the photoresistor
  drawPhotoresistor(centerX, centerY, photoresistorSize);

  // Draw label
  fill(0);
  noStroke();
  textSize(16);
  textAlign(CENTER, CENTER);
  text('Photoresistor (LDR)', centerX, centerY + photoresistorSize/2 + 30);
}

function drawPhotoresistor(x, y, size) {
  let radius = size / 2;

  // Draw outer circle (component body)
  fill(240);
  stroke(0);
  strokeWeight(3);
  circle(x, y, size);

  // Draw inner light-sensitive area (slightly smaller circle)
  fill(255);
  strokeWeight(2);
  circle(x, y, size * 0.85);

  // Draw serpentine pattern (horizontal zigzag lines)
  drawSerpentinePattern(x, y, size * 0.45);

  // Draw two terminal connection points
  fill(200);
  stroke(0);
  strokeWeight(2);
  let terminalSize = size * 0.12;
  circle(x - radius * 0.6, y, terminalSize);
  circle(x + radius * 0.6, y, terminalSize);
}

function drawSerpentinePattern(x, y, patternWidth) {
  // Draw horizontal serpentine lines with curved corners
  let numLines = 7; // number of horizontal segments
  let lineSpacing = patternWidth * 0.25; // vertical spacing between lines
  let amplitude = patternWidth * 0.45; // how wide the zigzag goes
  let startY = y - (numLines - 1) * lineSpacing / 2;
  let cornerRadius = lineSpacing * 0.5; // radius for curved corners

  stroke(0);
  strokeWeight(5);
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

function windowResized() {
  updateCanvasSize();
  resizeCanvas(containerWidth, containerHeight);
  redraw();
}

function updateCanvasSize() {
  const container = document.querySelector('main').getBoundingClientRect();
  containerWidth = Math.floor(container.width);
  if (containerWidth < 400) containerWidth = 400;
  containerHeight = canvasHeight; // Keep height fixed
}
