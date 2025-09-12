// LED Current for Base Limiting Resistor MicroSim
// Canvas dimensions
let canvasWidth = 500;
let drawHeight = 400;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let margin = 60;
let defaultTextSize = 16;
// the left edge of the slider - static
let leftSiderMargin = 160;

// Global variables for responsive design
let containerWidth; // calculated by container upon resize
let containerHeight = canvasHeight; // fixed height on page

// Chart parameters
let chartMargin = 60;
let chartWidth, chartHeight;

let maxR = 35;

// Data points from the table
let dataPoints = [
  {resistance: 4.6, current: 150},
  {resistance: 6.0, current: 120},
  {resistance: 9.9, current: 75},
  {resistance: 20.9, current: 32},
  {resistance: 27.7, current: 25},
  {resistance: 31.0, current: 20}
];

// Linear regression line parameters
// note this is NOT a linear function!
let slope, intercept;

// UI Controls
let resistorSlider;
let resistorValue = 10; // default 10K ohms

function setup() {
  // Create a canvas to match the parent container's size
  updateCanvasSize();
  const canvas = createCanvas(containerWidth, containerHeight);
  canvas.parent(document.querySelector('main'));
  textSize(defaultTextSize);
  
  // Create resistor slider (3 to 50 K ohms)
  resistorSlider = createSlider(3, 40, 10, 0.1);
  resistorSlider.position(leftSiderMargin, drawHeight + 25);
  resistorSlider.size(containerWidth - 230);
  
  // Calculate chart dimensions
  chartWidth = canvasWidth - 2 * chartMargin;
  chartHeight = drawHeight - 2 * chartMargin;
  
  // Calculate least squares fit
  calculateLeastSquaresFit();
  
  describe('LED Current vs Base Limiting Resistor MicroSim showing the relationship between resistance and current with interactive slider control.', LABEL);
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
  
  // Calculate and display predicted current
  let predictedCurrent = slope * resistorValue + intercept;
  text(`Predicted Current: ${predictedCurrent.toFixed(1)} mA`, canvasWidth - 250, drawHeight + 15);
}

// this is a standard least squares fit used
// to calculate the slope and intercept of a line
// given list of points
function calculateLeastSquaresFit() {
  // Calculate least squares regression: y = mx + b
  let n = dataPoints.length;
  let sumX = 0, sumY = 0, sumXY = 0, sumXX = 0;
  
  for (let point of dataPoints) {
    sumX += point.resistance;
    sumY += point.current;
    sumXY += point.resistance * point.current;
    sumXX += point.resistance * point.resistance;
  }
  
  // Calculate slope (m) and intercept (b)
  slope = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX);
  intercept = (sumY - slope * sumX) / n;
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
  
  // Vertical grid lines (resistance)
  for (let r = 5; r <= maxR; r += 5) {
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
  text("Resistance (KΩ)", chartWidth/2, chartHeight + maxR);
  
  // Y-axis label (rotated)
  push();
  translate(-maxR, chartHeight/2);
  rotate(-PI/2);
  text("Current (mA)", 0, 0);
  pop();
  
  // Draw axis tick labels
  textSize(12);
  textAlign(CENTER, TOP);
  
  // X-axis ticks
  for (let r = 0; r <= maxR; r += 10) {
    let x = map(r, 0, maxR, 0, chartWidth);
    text(r, x, chartHeight + 5);
  }
  
  // Y-axis ticks
  textAlign(RIGHT, CENTER);
  for (let c = 0; c <= 160; c += 20) {
    let y = map(c, 0, 160, chartHeight, 0);
    text(c, -5, y);
  }
  
  // Draw regression line
  stroke('blue');
  strokeWeight(3);
  noFill();
  beginShape();
  for (let r = 3; r <= maxR; r += 1) {
    let current = slope * r + intercept;
    let x = map(r, 0, maxR, 0, chartWidth);
    let y = map(current, 0, 160, chartHeight, 0);
    vertex(x, y);
  }
  endShape();
  
  // Draw data points
  fill('red');
  stroke('darkred');
  strokeWeight(2);
  for (let point of dataPoints) {
    let x = map(point.resistance, 0, maxR, 0, chartWidth);
    let y = map(point.current, 0, 160, chartHeight, 0);
    circle(x, y, 8);
  }
  
  // Draw current resistor value point
  let currentX = map(resistorValue, 0, maxR, 0, chartWidth);
  let predictedCurrent = slope * resistorValue + intercept;
  let currentY = map(predictedCurrent, 0, 160, chartHeight, 0);
  
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