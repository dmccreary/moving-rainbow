// Color Wheel MicroSim
// Canvas dimensions
let canvasWidth = 400;
// The top drawing region above the interactive controls
let drawHeight = 400;
// control region height
let controlHeight = 50;
// The total height of both the drawing region height + the control region height
let canvasHeight = drawHeight + controlHeight;
// margin around the active plotting region
let margin = 25;
let sliderLeftMargin = 125;
// larger text so students in the back of the room can read the labels
let defaultTextSize = 16;

// global variables for width and height
let containerWidth; // calculated by container upon resize
let containerHeight = canvasHeight; // fixed height on page

let rotationSlider;
let rotationValue = 0;
let currentRGB = [255, 0, 0]; // Default to red

function setup() {
  // Create a canvas to match the parent container's size
  updateCanvasSize();
  const canvas = createCanvas(containerWidth, containerHeight);
  canvas.parent(document.querySelector('main'));
  
  // Create the rotation slider
  rotationSlider = createSlider(0, 255, 0);
  rotationSlider.position(sliderLeftMargin, drawHeight + 15);
  rotationSlider.size(containerWidth - sliderLeftMargin - margin);
  
  describe('A color wheel MicroSim with an interactive rotation slider to explore colors.', LABEL);
}

function draw() {
  // Draw area with light blue background
  fill('aliceblue');
  stroke('silver');
  strokeWeight(1);
  rect(0, 0, canvasWidth, drawHeight);
  
  // Controls area with white background
  fill('white');
  rect(0, drawHeight, canvasWidth, controlHeight);
  
  // Update rotation value from slider
  rotationValue = rotationSlider.value();
  
  // Calculate the center and radius of the wheel
  let centerX = canvasWidth / 2;
  let centerY = drawHeight / 2;
  let wheelRadius = min(drawHeight, canvasWidth) / 2 - margin * 2;
  
  // Draw color wheel
  drawColorWheel(centerX, centerY, wheelRadius);
  
  // Draw the rotation line and calculate current RGB
  currentRGB = wheel(rotationValue);
  drawRotationLine(centerX, centerY, wheelRadius, rotationValue, currentRGB);
  
  // Draw the slider label
  fill('black');
  noStroke();
  textSize(defaultTextSize);
  textAlign(LEFT, CENTER);
  text('Rotation: ' + rotationValue, margin, drawHeight + 25);
  
  // Draw RGB values in lower left corner
  fill('black');
  textAlign(LEFT, BOTTOM);
  textSize(defaultTextSize);
  text(`R: ${currentRGB[0]}  G: ${currentRGB[1]}  B: ${currentRGB[2]}`, 
       margin, drawHeight - margin);
}

function drawColorWheel(centerX, centerY, radius) {
  // Draw segments of the color wheel
  colorMode(RGB);
  
  for (let angle = 0; angle < 360; angle++) {
    // Calculate the color based on angle position
    let pos = map(angle, 0, 360, 0, 255);
    let rgb = wheel(pos);
    
    // Draw the segment
    push();
    translate(centerX, centerY);
    rotate(radians(angle));
    stroke(rgb[0], rgb[1], rgb[2]);
    strokeWeight(2);
    line(0, 0, radius, 0);
    pop();
  }
  
  // Draw center circle
  fill(255);
  stroke(150);
  strokeWeight(1);
  circle(centerX, centerY, 20);
}

function drawRotationLine(centerX, centerY, radius, rotationValue, rgb) {
  // Map rotation value to angle
  let angle = map(rotationValue, 0, 255, 0, 360);
  
  // Draw line from center to edge
  push();
  translate(centerX, centerY);
  rotate(radians(angle));
  
  // Black line
  stroke(0);
  strokeWeight(3);
  line(0, 0, radius, 0);
  
  // Calculate the endpoint in canvas coordinates
  let endX = cos(radians(angle)) * radius;
  let endY = sin(radians(angle)) * radius;
  pop();
  
  // Draw the upright callout
  let calloutX = centerX + endX;
  let calloutY = centerY + endY;
  
  // Draw a line to connect the rotation line to the callout
  stroke(0);
  strokeWeight(1);
  line(calloutX, calloutY, calloutX + 20, calloutY);
  
  // Draw the callout ellipse (25% larger)
  noStroke();
  fill(255);
  let calloutWidth = 80; // 40 * 1.25
  let calloutHeight = 40; // 25 * 1.25
  ellipse(calloutX + 25, calloutY, calloutWidth, calloutHeight);
  
  // Draw color swatch in the callout
  fill(rgb[0], rgb[1], rgb[2]);
  stroke(0);
  strokeWeight(1);
  rect(calloutX, calloutY - 8, 15, 15);
  
  // Draw the index in the callout (25% larger font)
  fill(0);
  textAlign(CENTER, CENTER);
  textSize(18); // 14 * 1.25 (rounded)
  text(rotationValue, calloutX + 35, calloutY);
}

// Implement the wheel function from Python to JavaScript
function wheel(pos) {
  // Input a value 0 to 255 to get a color value.
  // The colors are a transition r - g - b - back to r.
  if (pos < 0 || pos > 255) {
    return [0, 0, 0];
  }
  if (pos < 85) {
    return [255 - pos * 3, pos * 3, 0];
  }
  if (pos < 170) {
    pos -= 85;
    return [0, 255 - pos * 3, pos * 3];
  }
  pos -= 170;
  return [pos * 3, 0, 255 - pos * 3];
}

function windowResized() {
  // Update canvas size when the container resizes
  updateCanvasSize();
  resizeCanvas(containerWidth, containerHeight);
  redraw();
  
  // Resize the slider to match the new canvasWidth
  rotationSlider.size(containerWidth - sliderLeftMargin - margin);
}

function updateCanvasSize() {
  // Get the exact dimensions of the container
  const container = document.querySelector('main').getBoundingClientRect();
  containerWidth = Math.floor(container.width);  // Avoid fractional pixels
  canvasWidth = containerWidth;
}