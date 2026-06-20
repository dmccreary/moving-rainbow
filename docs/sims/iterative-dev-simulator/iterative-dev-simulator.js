// Iterative Development Simulator - Moving Rainbow MicroSim
// Build a working LED animation in four small, testable steps. Each step
// adds exactly one feature and produces visible, verifiable output.
// CANVAS_HEIGHT: 380
let canvasWidth = 760;
let drawHeight = 300;
let controlHeight = 80;
let canvasHeight = drawHeight + controlHeight;
let margin = 15;
let defaultTextSize = 16;

let currentStep = 0;     // 0 = initial (all off), 1..4 = stages applied
let offset = 0;
let applyButton, resetButton, pixelSlider, speedSlider;

const steps = [
  {title: 'Step 1 - One Pixel On',
   status: 'One pixel on! We can control a single LED.'},
  {title: 'Step 2 - All Pixels One Color',
   status: 'All 10 pixels on! We extended the same idea to the whole strip.'},
  {title: 'Step 3 - Rainbow Spread',
   status: "Each pixel has its own hue - that's a rainbow!"},
  {title: 'Step 4 - Animate',
   status: "It's moving! A full animation built in four tested steps."},
];

function hsvToRgb(h, s, v) {
  let c = v * s, x = c * (1 - Math.abs(((h / 60) % 2) - 1)), m = v - c;
  let r = 0, g = 0, b = 0;
  if (h < 60)      { r = c; g = x; }
  else if (h < 120){ r = x; g = c; }
  else if (h < 180){ g = c; b = x; }
  else if (h < 240){ g = x; b = c; }
  else if (h < 300){ r = x; b = c; }
  else             { r = c; b = x; }
  return [(r + m) * 255, (g + m) * 255, (b + m) * 255];
}

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));

  applyButton = createButton('Apply Next Step');
  applyButton.position(10, drawHeight + 10);
  applyButton.mousePressed(() => { if (currentStep < 4) currentStep++; });

  resetButton = createButton('Reset');
  resetButton.position(150, drawHeight + 10);
  resetButton.mousePressed(() => { currentStep = 0; offset = 0; });

  pixelSlider = createSlider(1, 30, 10, 1);
  pixelSlider.position(80, drawHeight + 45);
  pixelSlider.size(160);

  speedSlider = createSlider(1, 20, 4, 1);
  speedSlider.position(330, drawHeight + 45);
  speedSlider.size(120);

  describe('A simulated LED strip built up in four steps: one pixel on, all ' +
    'pixels on, a static rainbow, and finally a scrolling rainbow animation.', LABEL);
}

function numLeds() {
  return (currentStep >= 4) ? pixelSlider.value() : 10;
}

function ledColor(i, n) {
  if (currentStep === 0) return [40, 40, 40];
  if (currentStep === 1) return (i === 0) ? [255, 0, 0] : [40, 40, 40];
  if (currentStep === 2) return [255, 0, 0];
  if (currentStep === 3) return hsvToRgb(((i / 10) * 360) % 360, 1, 1);
  return hsvToRgb((((i + offset) / n) * 360) % 360, 1, 1);   // step 4
}

function draw() {
  updateCanvasSize();
  const splitX = Math.max(canvasWidth * 0.58, 300);

  // backgrounds
  noStroke();
  fill('white');
  rect(0, drawHeight, canvasWidth, controlHeight);
  fill(17);
  rect(0, 0, splitX, drawHeight);
  fill('aliceblue');
  stroke('silver');
  rect(splitX, 0, canvasWidth - splitX, drawHeight);

  drawLeds(splitX);
  drawStepPanel(splitX);

  // animate
  if (currentStep === 4) offset += speedSlider.value();

  drawControls();
}

function drawLeds(splitX) {
  const n = numLeds();
  const areaW = splitX - 2 * margin;
  const r = Math.min(areaW / n * 0.35, 16);
  const y = drawHeight * 0.42;
  for (let i = 0; i < n; i++) {
    const x = margin + areaW * (i + 0.5) / n;
    const rgb = ledColor(i, n);
    noStroke();
    if (currentStep > 0 && !(currentStep === 1 && i !== 0)) {
      for (let g = 3; g >= 1; g--) { fill(rgb[0], rgb[1], rgb[2], 40); circle(x, y, r * 2 + g * 5); }
    }
    fill(rgb[0], rgb[1], rgb[2]);
    stroke(60);
    strokeWeight(1);
    circle(x, y, r * 2);
  }
  // status message
  noStroke();
  fill(220);
  textSize(14);
  textAlign(CENTER, TOP);
  const msg = (currentStep === 0)
    ? 'All LEDs off. Click "Apply Next Step" to begin.'
    : steps[currentStep - 1].status;
  textWrap(WORD);
  text(msg, splitX / 2, drawHeight * 0.62, splitX - 2 * margin);
  textAlign(LEFT, CENTER);
}

function drawStepPanel(splitX) {
  noStroke();
  fill('black');
  textSize(15);
  textAlign(LEFT, TOP);
  text('Build It Step by Step', splitX + 12, 12);
  textSize(13);
  for (let i = 0; i < 4; i++) {
    const y = 44 + i * 34;
    const active = (currentStep === i + 1) || (currentStep === 0 && i === 0);
    if (active) {
      fill(65, 186, 193);
      rect(splitX + 8, y - 4, canvasWidth - splitX - 16, 28, 5);
      fill('white');
    } else {
      fill(60);
    }
    noStroke();
    text((i + 1) + '. ' + steps[i].title, splitX + 16, y + 2);
  }
  textAlign(LEFT, CENTER);
}

function drawControls() {
  noStroke();
  fill('black');
  textSize(13);
  textAlign(LEFT, CENTER);
  text('Step ' + currentStep + ' of 4', 215, drawHeight + 22);

  if (currentStep >= 4) {
    pixelSlider.show();
    speedSlider.show();
    text('Pixels: ' + pixelSlider.value(), 10, drawHeight + 55);
    text('Speed: ' + speedSlider.value(), 260, drawHeight + 55);
    fill(90);
    textSize(11);
    text('Extreme values are edge cases - test them now, not at the demo.',
         470, drawHeight + 55);
  } else {
    pixelSlider.hide();
    speedSlider.hide();
    fill(90);
    text('Reach Step 4 to unlock edge-case sliders (pixels & speed).',
         10, drawHeight + 55);
  }
  textSize(defaultTextSize);
}

function windowResized() {
  updateCanvasSize();
  resizeCanvas(canvasWidth, canvasHeight);
}

function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
