// LED Current for Base Limiting Resistor MicroSim
// Using inverse relationship: Current = a/Resistance + b
// Canvas dimensions
let canvasWidth = 500;
let drawHeight = 400;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let margin = 60;
let defaultTextSize = 16;
// the left edge of the slider - static
let leftSliderMargin = 160;

// Global variables for responsive design
let containerWidth; // calculated by container upon resize
let containerHeight = canvasHeight; // fixed height on page

// Chart parameters
let chartMargin = 60;
let chartWidth, chartHeight;

let maxR = 330; // Extended range to show more data points

// Data points from the table (extended dataset)
let dataPoints = [
    {"resistance": 4.6, "current": 150},
    {"resistance": 6.0, "current": 120},
    {"resistance": 9.9, "current": 75},
    {"resistance": 14.7, "current": 55},
    {"resistance": 20.9, "current": 32},
    {"resistance": 27.7, "current": 25},
    {"resistance": 31.0, "current": 20},
    {"resistance": 43, "current": 23},
    {"resistance": 92, "current": 13.3},
    {"resistance": 125, "current": 10.9},
    {"resistance": 151, "current": 8.7},
    {"resistance": 221, "current": 6.5},
    {"resistance": 330, "current": 5.9}
];

// Inverse relationship parameters: Current = a/Resistance + b
// These coefficients come from the Python regression analysis
let a = 1037;  // coefficient of 1/R
let b = -9.8;    // constant term

// UI Controls
let resistorSlider;
let resistorValue = 10; // default 10K ohms

function setup() {
  // Create a canvas to match the parent container's size
  updateCanvasSize();
  const canvas = createCanvas(containerWidth, containerHeight);
  canvas.parent(document.querySelector('main'));
  textSize(defaultTextSize);
  
  // Create resistor slider (3 to 350 K ohms) - extended range
  resistorSlider = createSlider(3, 350, 10, 0.1);
  resistorSlider.position(leftSliderMargin, drawHeight + 25);
  resistorSlider.size(containerWidth - 230);
  
  // Calculate chart dimensions
  chartWidth = canvasWidth - 2 * chartMargin;
  chartHeight = drawHeight - 2 * chartMargin;
  
  describe('LED Current vs Base Limiting Resistor MicroSim using inverse relationship formula for accurate predictions across a wide resistance range.', LABEL);
}

function draw() {
  // Draw area
  fill('aliceblue');
  stroke('silver');
  strokeWeight(1);
  rect(0, 0, canvasWidth, drawHeight);
  
  // Controls area
  fill('white');
  stroke('silver');
  strokeWeight(1);
  rect(0, drawHeight, canvasWidth, controlHeight);
  
  // Update resistor value from slider
  resistorValue = resistorSlider.value();
  
  // Title
  fill('black');
  noStroke();
  textSize(24);
  textAlign(CENTER, TOP);
  text("LED Current for Base Limiting Resistor", canvasWidth/2, 15);
  
  // Draw the chart
  drawChart();
  
  // Draw control labels
  fill('black');
  textSize(defaultTextSize);
  textAlign(LEFT, CENTER);
  text(`Resistor: ${resistorValue.toFixed(1)} KΩ`, 20, drawHeight + 35);
  
  // Calculate and display predicted current using inverse formula
  let predictedCurrent = calculateCurrent(resistorValue);
  text(`Predicted Current: ${predictedCurrent.toFixed(1)} mA`, canvasWidth - 250, drawHeight + 15);
}

// Calculate current using inverse relationship: I = a/R + b
function calculateCurrentv1(resistance) {
  return a / resistance + b;
}

// Power Law coefficients for resistance ≤ 30KΩ
let a_low = 517.7487;    // amplitude coefficient
let b_low = 0.713491;    // power exponent (note: used as positive in Math.pow with negative sign)
let c_low = -24.3330;    // offset constant

// Inverse formula coefficients for resistance > 30KΩ
let a_high = 700  // coefficient of 1/R
let b_high = -3;    // constant term

// Threshold resistance value in KΩ
let threshold_resistance = 30.0;
function calculateCurrent(resistance) {
  if (resistance <= threshold_resistance) {
    // Low resistance region: Power Law formula
    // I = a_low * R^(-b_low) + c_low
    return a_low * Math.pow(resistance, -b_low) + c_low;
  } else {
    // High resistance region: Inverse formula
    // I = a_high / R + b_high
    return a_high / resistance + b_high;
  }
}

function drawChart() {
  push();
  translate(chartMargin, chartMargin);
  
  // Draw axes
  stroke('black');
  strokeWeight(2);
  
  // Y-axis
  line(0, 0, 0, chartHeight);
  
  // X-axis
  line(0, chartHeight, chartWidth, chartHeight);
  
  // Draw grid lines
  stroke('lightgray');
  strokeWeight(1);
  
  // Vertical grid lines (resistance) - adjusted for wider range
  let gridSpacing = maxR > 100 ? 50 : 25;
  for (let r = gridSpacing; r <= maxR; r += gridSpacing) {
    let x = map(r, 0, maxR, 0, chartWidth);
    line(x, 0, x, chartHeight);
  }
  
  // Horizontal grid lines (current)
  for (let c = 0; c <= 160; c += 20) {
    let y = map(c, 0, 160, chartHeight, 0);
    line(0, y, chartWidth, y);
  }
  
  // Draw axis labels
  fill('black');
  noStroke();
  textAlign(CENTER, CENTER);
  textSize(14);
  
  // X-axis label
  text("Resistance (KΩ)", chartWidth/2, chartHeight + 35);
  
  // Y-axis label (rotated)
  push();
  translate(-35, chartHeight/2);
  rotate(-PI/2);
  text("Current (mA)", 0, 0);
  pop();
  
  // Draw axis tick labels
  textSize(12);
  textAlign(CENTER, TOP);
  
  // X-axis ticks - adjusted for wider range
  let tickSpacing = maxR > 100 ? 50 : 25;
  for (let r = 0; r <= maxR; r += tickSpacing) {
    let x = map(r, 0, maxR, 0, chartWidth);
    text(r, x, chartHeight + 5);
  }
  
  // Y-axis ticks
  textAlign(RIGHT, CENTER);
  for (let c = 0; c <= 160; c += 20) {
    let y = map(c, 0, 160, chartHeight, 0);
    text(c, -5, y);
  }
  
  // Draw inverse curve
  stroke('blue');
  strokeWeight(3);
  noFill();
  beginShape();
  for (let r = 3; r <= maxR; r += maxR/200) { // Smooth curve with many points
    let current = calculateCurrent(r);
    let x = map(r, 0, maxR, 0, chartWidth);
    let y = map(current, 0, 160, chartHeight, 0);
    
    // Only draw points within the chart bounds
    if (current >= 0 && current <= 160) {
      vertex(x, y);
    }
  }
  endShape();
  
  // Draw data points
  fill('red');
  stroke('darkred');
  strokeWeight(2);
  for (let point of dataPoints) {
    // Only draw points within the current chart range
    if (point.resistance <= maxR) {
      let x = map(point.resistance, 0, maxR, 0, chartWidth);
      let y = map(point.current, 0, 160, chartHeight, 0);
      circle(x, y, 8);
    }
  }
  
  // Draw current resistor value point (only if within range)
  if (resistorValue <= maxR) {
    let currentX = map(resistorValue, 0, maxR, 0, chartWidth);
    let predictedCurrent = calculateCurrent(resistorValue);
    let currentY = map(predictedCurrent, 0, 160, chartHeight, 0);
    
    // Only draw if current is within visible range
    if (predictedCurrent >= 0 && predictedCurrent <= 160) {
      fill('green');
      stroke('darkgreen');
      strokeWeight(3);
      circle(currentX, currentY, 12);
      
      // Draw vertical line from x-axis to current point
      stroke('green');
      strokeWeight(2);
      line(currentX, chartHeight, currentX, currentY);
      
      // Draw horizontal line from y-axis to current point
      line(0, currentY, currentX, currentY);
    }
  }
  
  // Add formula text to the chart
  fill('navy');
  noStroke();
  textAlign(LEFT, TOP);
  textSize(14);
  text(`I = ${a.toFixed(0)}/R + ${b.toFixed(1)}`, 30, 10);
  text(`(Inverse Relationship)`, 30, 30);
  
  pop();
}

function windowResized() {
  // Update canvas size when the container resizes
  updateCanvasSize();
  resizeCanvas(containerWidth, containerHeight);
  
  // Update chart dimensions
  chartWidth = canvasWidth - 2 * chartMargin;
  chartHeight = drawHeight - 2 * chartMargin;
  
  // Resize the slider to match the new canvasWidth
  resistorSlider.size(containerWidth - 230);
  
  redraw();
}

function updateCanvasSize() {
  // Get the exact dimensions of the container
  const container = document.querySelector('main').getBoundingClientRect();
  containerWidth = Math.floor(container.width);  // Avoid fractional pixels
  canvasWidth = containerWidth;
}