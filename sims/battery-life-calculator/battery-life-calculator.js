// Battery Life Calculator MicroSim
// Educational simulation for calculating LED noodle costume battery life
// Based on the formula: Battery Life (hours) = Battery Capacity (mAh) ÷ Total Current Draw (mA)

// Canvas dimensions
let canvasWidth = 800;
let containerWidth = 800;

const drawHeight = 400;
const controlHeight = 130;
const canvasHeight = drawHeight + controlHeight;
let sliderLeftMargin = 250;
let containerHeight = canvasHeight;
let margin = 30;

// Battery specifications (mAh)
const batteryTypes = [
  { name: "AA Battery (single)", capacity: 2500 },
  { name: "AA Battery (2x)", capacity: 5000 },
  { name: "AA Battery (4x)", capacity: 10000 },
  { name: "9V Battery", capacity: 550 },
  { name: "USB Power Pack (small)", capacity: 5000 },
  { name: "USB Power Pack (medium)", capacity: 10000 },
  { name: "USB Power Pack (large)", capacity: 20000 }
];

// LED noodle parameters
const CURRENT_PER_NOODLE_MAX = 100; // 100 mA at full brightness, 50 mA at 50% brightness

// UI controls
let noodleSlider;
let brightnessSlider;
let batterySelect;

// Labels
let noodleLabel, brightnessLabel, batteryLabel;
let noodleValue, brightnessValue;


function setup() {
  // Create a canvas to match the parent container's size
  updateCanvasSize();
  const canvas = createCanvas(containerWidth, containerHeight);
  canvas.parent(document.querySelector('main'));

  describe('Interactive battery life calculator for LED noodle costumes showing battery capacity, current draw, and estimated runtime based on number of noodles, brightness, and battery type');

  // Create controls in the control region
  let controlY = drawHeight + 20;

  // Battery type selector
  batteryLabel = createDiv('Battery Type:');
  batteryLabel.position(20, controlY);
  batteryLabel.style('font-size', '16pt');

  batterySelect = createSelect();
  batterySelect.position(sliderLeftMargin, controlY);
  for (let i = 0; i < batteryTypes.length; i++) {
    batterySelect.option(batteryTypes[i].name, i);
  }
  batterySelect.selected(4); // Default to small USB power pack
  batterySelect.style('font-size', '14pt');

  controlY += 40;

  // Number of noodles slider
  noodleLabel = createDiv('Number of Noodles:');
  noodleLabel.position(20, controlY);
  noodleLabel.style('font-size', '16pt');

  noodleValue = createDiv('5');
  noodleValue.position(sliderLeftMargin - 40, controlY);
  noodleValue.style('font-size', '16pt');
  noodleValue.style('text-align', 'right');
  noodleValue.style('width', '30px');

  noodleSlider = createSlider(1, 20, 5, 1);
  noodleSlider.position(sliderLeftMargin, controlY);
  noodleSlider.size(canvasWidth - sliderLeftMargin - 20);

  controlY += 40;

  // Brightness slider
  brightnessLabel = createDiv('Brightness (%):');
  brightnessLabel.position(20, controlY);
  brightnessLabel.style('font-size', '16pt');

  brightnessValue = createDiv('50');
  brightnessValue.position(sliderLeftMargin - 40, controlY);
  brightnessValue.style('font-size', '16pt');
  brightnessValue.style('text-align', 'right');
  brightnessValue.style('width', '30px');

  brightnessSlider = createSlider(10, 100, 50, 5);
  brightnessSlider.position(sliderLeftMargin, controlY);
  brightnessSlider.size(canvasWidth - sliderLeftMargin - 20);
}

function draw() {
  updateCanvasSize();
  // Update slider values
  noodleValue.html(noodleSlider.value());
  brightnessValue.html(brightnessSlider.value());

  // Calculate battery life
  let selectedBattery = batteryTypes[batterySelect.value()];
  let numNoodles = noodleSlider.value();
  let brightnessFactor = brightnessSlider.value() / 100;

  let totalCurrent = numNoodles * CURRENT_PER_NOODLE_MAX * brightnessFactor;
  let batteryLife = selectedBattery.capacity / totalCurrent;

  // Draw background regions

  // Drawing region lis a light blue
  fill('aliceblue');
  stroke('silver');
  rect(0, 0, canvasWidth, drawHeight);

  fill('white');
  rect(0, drawHeight, canvasWidth, controlHeight);

  // Draw title centered at top
  fill('black');
  noStroke();
  textAlign(CENTER, TOP);
  textSize(28);
  text('LED Noodle Costume Battery Life Calculator', canvasWidth / 2, margin);
  textStyle(NORMAL);

  // Draw battery visualization. at (x,y)
  drawBattery(selectedBattery, batteryLife, 50, 80);

  // Draw LED noodles
  drawNoodles(numNoodles, brightnessFactor, canvasWidth - 300, 80);

  // Display calculations
  push();
    // adjust the positioning of the text block here
    translate(-20, -40);
    fill('black');
    noStroke();
    textAlign(LEFT);
    textSize(18);
    text('Battery Calculations:', 50, drawHeight - 140);

    textSize(16);
    text(`Battery Capacity: ${selectedBattery.capacity.toLocaleString()} mAh`, 50, drawHeight - 110);
    text(`Current per Noodle: ${CURRENT_PER_NOODLE_MAX*brightnessFactor} mA (max=100ma)`, 50, drawHeight - 85);
    text(`Brightness Factor: ${brightnessFactor.toFixed(2)}`, 50, drawHeight - 60);
    text(`Total Current Draw: ${totalCurrent.toFixed(1)} mA`, 50, drawHeight - 35);

    // Display result prominently
    fill('darkgreen');
    textSize(20);
    textStyle(BOLD);
    text(`Estimated Battery Life: ${batteryLife.toFixed(2)} hours`, 50, drawHeight - 5);
    textStyle(NORMAL);
  pop();
}

function drawBattery(battery, hoursRemaining, x, y) {
  // Draw battery icon
  let batteryWidth = 120;
  let batteryHeight = 60;

  // Battery body
  stroke('black');
  strokeWeight(3);
  fill('white');
  rect(x, y, batteryWidth, batteryHeight, 5);

  // Battery terminal
  fill('gray');
  rect(x + batteryWidth, y + 15, 10, 30, 0, 5, 5, 0);

  // Battery fill level (based on typical runtime expectations)
  let maxExpectedHours = 40; // Maximum we expect for visualization
  let fillLevel = constrain(hoursRemaining / maxExpectedHours, 0, 1);

  // Color code the fill
  let fillColor;
  if (fillLevel > 0.5) {
    fillColor = color(0, 200, 0); // Green
  } else if (fillLevel > 0.25) {
    fillColor = color(255, 200, 0); // Yellow
  } else {
    fillColor = color(255, 0, 0); // Red
  }

  noStroke();
  fill(fillColor);
  let fillWidth = (batteryWidth - 10) * fillLevel;
  rect(x + 5, y + 5, fillWidth, batteryHeight - 10, 3);

  // Label
  fill('black');
  noStroke();
  textAlign(CENTER);
  textSize(14);
  text(battery.name, x + batteryWidth / 2, y + batteryHeight + 20);
  text(`${battery.capacity} mAh`, x + batteryWidth / 2, y + batteryHeight + 38);
}

function drawNoodles(count, brightness, x, y) {
  // Draw LED noodles as glowing lines
  noStroke();
  fill('black');
  textAlign(CENTER);
  textSize(14);
  text(`${count} LED Noodle${count > 1 ? 's' : ''}`, x + 100, y - 10);

  let noodleWidth = 15;
  let noodleHeight = 200;
  let spacing = 20;

  // Calculate grid layout
  // Move grid down a bit

  let cols = min(count, 5);
  let rows = ceil(count / cols);

  for (let i = 0; i < count; i++) {
    let col = i % cols;
    let row = floor(i / cols);

    let nx = x + col * spacing;
    // 20 is the y for the LEDs
    let ny = y + 20 + row * (noodleHeight / rows + 10);
    let nh = noodleHeight / rows - 5;

    // Draw noodle glow
    for (let j = 0; j < 3; j++) {
      let glowAlpha = 50 * brightness * (3 - j) / 3;
      fill(255, 150, 0, glowAlpha);
      rect(nx - j * 2, ny - j * 2, noodleWidth + j * 4, nh + j * 4, 8);
    }

    // Draw noodle body
    fill(255, 100 + 155 * brightness, 0);
    rect(nx, ny, noodleWidth, nh, 5);

    // Draw LED segments
    let segments = 5;
    for (let s = 0; s < segments; s++) {
      fill(255, 200 + 55 * brightness, 100, 200 * brightness);
      let segY = ny + (nh / segments) * s + 5;
      ellipse(nx + noodleWidth / 2, segY, 8, 8);
    }
  }
}

function windowResized() {
  // Update canvas size to match container
  updateCanvasSize();
  resizeCanvas(containerWidth, containerHeight);

  // Resize sliders
  noodleSlider.style('width', (canvasWidth - sliderLeftMargin - 20) + 'px');
  brightnessSlider.style('width', (canvasWidth - sliderLeftMargin - 20) + 'px');
}


function updateCanvasSize() {
  const main = document.querySelector('main');
  if (main) {
    containerWidth = main.offsetWidth || 800;
  } else {
    containerWidth = 800;
  }
  containerHeight = drawHeight + controlHeight + 2;
  canvasWidth = containerWidth;
}