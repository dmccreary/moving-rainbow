// Animated Wire Circuit Simulation
// This simulation draws a square wire circuit with animated circles moving along 
// the wires simulating the flow of electric current by representing electron flow.
// The speed and spacing of the circles can be controlled with sliders, 
// and the animation can be toggled on and off with a button.
// Modified to keep electrons visible when paused.

// Canvas dimensions following standard MicroSim layout
let canvasWidth = 400;                      // Initial width that will be updated responsively
let drawHeight = 400;                       // Height of simulation/drawing area
let controlHeight = 80;                     // Height of controls region
let canvasHeight = drawHeight + controlHeight; // Total canvas height
let margin = 25;                            // Margin for visual elements
let sliderLeftMargin = 115;                 // Left margin for slider positioning
let defaultTextSize = 16;                   // Base text size for readability

// Global variables for responsive design
let containerWidth;                         // Calculated from container upon resize
let containerHeight = canvasHeight;         // Usually fixed height on page

// Simulation variables
let isRunning = false;
let animationTime = 0;                      // Track animation time independently
let speedSlider;
let spacingSlider;
let startButton;
let resetButton;

// Wire drawing parameters
let wireMargin = 50;
let lineWidth = 8;

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(containerWidth, containerHeight);
  canvas.parent(document.querySelector('main'));
  
  // Create speed control slider
  speedSlider = createSlider(0.02, 0.5, 0.25, 0.03);
  speedSlider.position(sliderLeftMargin, drawHeight + 35);
  speedSlider.size(containerWidth - sliderLeftMargin - 25);
  
  // Create spacing control slider  
  spacingSlider = createSlider(0.15, 1.5, 1.0, 0.05);
  spacingSlider.position(sliderLeftMargin, drawHeight + 55);
  spacingSlider.size(containerWidth - sliderLeftMargin - 25);
  
  // Create start/pause button
  startButton = createButton('Start');
  startButton.position(10, drawHeight + 10);
  startButton.mousePressed(toggleSimulation);
  
  // Create reset button
  resetButton = createButton('Reset');
  resetButton.position(70, drawHeight + 10);
  resetButton.mousePressed(resetSimulation);

  describe('Wire circuit simulation showing electron flow through a square wire loop with controllable speed and spacing.', LABEL);
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
  textSize(24);
  textAlign(CENTER, TOP);
  text("Wire Circuit Simulation", containerWidth/2, margin/2);
  
  // Reset text properties for other elements
  textSize(defaultTextSize);
  textAlign(LEFT, CENTER);
  
  // Get current slider values
  let currentSpeed = speedSlider.value();
  let currentSpacing = spacingSlider.value();
  
  // Update animation time only when running
  if (isRunning) {
    animationTime += deltaTime;
  }
  
  // Calculate wire boundaries with responsive margins
  let circuitMargin = margin*2; // margin does not scale with width
  let rightEdge = containerWidth - circuitMargin;
  let bottomEdge = drawHeight - circuitMargin;
  
  // Draw the four wires forming a square circuit
  // Top wire (left to right)
  drawAnimatedWire(circuitMargin, circuitMargin, rightEdge, circuitMargin, currentSpeed, currentSpacing);
  
  // Right wire (top to bottom)  
  drawAnimatedWire(rightEdge, circuitMargin, rightEdge, bottomEdge, currentSpeed, currentSpacing);
  
  // Bottom wire (right to left)
  drawAnimatedWire(rightEdge, bottomEdge, circuitMargin, bottomEdge, currentSpeed, currentSpacing);
  
  // Left wire (bottom to top)
  drawAnimatedWire(circuitMargin, bottomEdge, circuitMargin, circuitMargin, currentSpeed, currentSpacing);
  
  // Draw control labels
  drawControlLabels();
}

// draw a black line with red circles as current from (x1,y1) to (y1,y2) 
function drawAnimatedWire(x1, y1, x2, y2, speed, spacing) {
  // Calculate wire properties
  let distance = dist(x1, y1, x2, y2);
  let spacingPixels = spacing * 50; // Convert spacing to pixels
  let numElectrons = Math.floor(distance / spacingPixels);
  
  // Draw the wire
  stroke('black');
  strokeWeight(lineWidth);
  line(x1, y1, x2, y2);
  
  // Draw moving electrons (always draw them, but only move when running)
  if (numElectrons > 0) {
    fill('red');
    noStroke();
    
    for (let i = 0; i <= numElectrons; i++) {
      // Calculate electron position using animationTime instead of millis()
      let electronPos = (animationTime * speed + i * spacingPixels) % distance;
      let x = lerp(x1, x2, electronPos / distance);
      let y = lerp(y1, y2, electronPos / distance);
      
      // Draw electron as red circle
      let electronSize = 8; // Fixed size for simplicity
      circle(x, y, electronSize);
    }
  }
}

function drawControlLabels() {
  push();
    // move both down
    translate(0, 30);
    fill('black');
    noStroke();
    textSize(defaultTextSize);
    textAlign(LEFT, CENTER);

    // Speed label and value
    text('Speed: ' + speedSlider.value().toFixed(3), 10, drawHeight + 15);

    // Spacing label and value  
    text('Spacing: ' + spacingSlider.value().toFixed(2), 10, drawHeight + 35);
  pop();
}

function toggleSimulation() {
  isRunning = !isRunning;
  startButton.html(isRunning ? 'Pause' : 'Start');
}

function resetSimulation() {
  // Reset sliders to default values
  speedSlider.value(0.25);
  spacingSlider.value(1.0);
  
  // Reset animation time
  animationTime = 0;
  
  // Stop simulation
  isRunning = false;
  startButton.html('Start');
  
  // Redraw to show reset state
  redraw();
}

// Required functions for responsive design
function windowResized() {
  updateCanvasSize();
  resizeCanvas(containerWidth, containerHeight);
  redraw();
  
  // Resize sliders to match new width
  speedSlider.size(containerWidth - sliderLeftMargin - 15);
  spacingSlider.size(containerWidth - sliderLeftMargin - 15);
}

function updateCanvasSize() {
  const container = document.querySelector('main').getBoundingClientRect();
  containerWidth = Math.floor(container.width);
  canvasWidth = containerWidth;
}