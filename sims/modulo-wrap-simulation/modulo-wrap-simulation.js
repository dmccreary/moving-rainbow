// Modulo Wrap-Around Simulation - Moving Rainbow MicroSim
// Step a position counter down a 10-pixel strip. When pos reaches 10 the
// modulo wraps it back to 0. (Understand: why % creates wrap-around.)
// CANVAS_HEIGHT: 300
let canvasWidth = 700;
let drawHeight = 200;
let controlHeight = 100;
let canvasHeight = drawHeight + controlHeight;
let margin = 15;
let defaultTextSize = 16;

const N = 10;
let pos = 0;
let prevPos = N - 1;      // position before the last step
let rawNext = N;          // prevPos + 1, before modulo, for the formula
let autoOn = false;
let wrapFlash = 0;        // frames left to show the wrap overlay
let stepButton, autoCheckbox;

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));

  stepButton = createButton('Step');
  stepButton.position(15, drawHeight + 15);
  stepButton.mousePressed(stepOnce);

  autoCheckbox = createCheckbox('Auto (5 steps/sec)', false);
  autoCheckbox.position(90, drawHeight + 17);
  autoCheckbox.changed(() => autoOn = autoCheckbox.checked());

  describe('A ten-pixel strip where a lit pixel advances each step and wraps from ' +
    'position 9 back to 0 using the modulo operator.', LABEL);
}

function stepOnce() {
  prevPos = pos;
  rawNext = prevPos + 1;
  pos = rawNext % N;
  if (pos === 0) wrapFlash = 40;
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill(20); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  if (autoOn && frameCount % 12 === 0) stepOnce();
  if (wrapFlash > 0) wrapFlash--;

  // position counter
  noStroke(); fill(230); textSize(16); textAlign(LEFT, TOP);
  text('position = ' + pos, margin, 14);

  // strip
  const areaW = canvasWidth - 2 * margin;
  const spacing = areaW / N;
  const r = Math.min(spacing * 0.32, 24);
  const y = 100;
  for (let i = 0; i < N; i++) {
    const x = margin + spacing * (i + 0.5);
    const on = (i === pos);
    noStroke();
    if (on) for (let g = 3; g >= 1; g--) { fill(255, 40, 40, 45); circle(x, y, r * 2 + g * 7); }
    fill(on ? color(255, 40, 40) : color(45));
    stroke(70); strokeWeight(1); circle(x, y, r * 2);
    noStroke(); fill(on ? 255 : 150); textSize(13); textAlign(CENTER, TOP); text(i, x, y + r + 6);
  }

  // formula
  noStroke(); fill('lightgreen'); textFont('monospace'); textSize(16); textAlign(CENTER, TOP);
  text('pos = (' + prevPos + ' + 1) % ' + N + '  =  ' + rawNext + ' % ' + N + '  =  ' + pos,
       canvasWidth / 2, 158);
  textFont('sans-serif');

  // wrap overlay
  if (wrapFlash > 0) {
    const a = Math.min(255, wrapFlash * 8);
    noStroke(); fill(255, 196, 0, a); rect(canvasWidth / 2 - 120, 40, 240, 40, 8);
    fill(40, 30, 0, a); textSize(18); textAlign(CENTER, CENTER); textFont('monospace');
    text(N + ' % ' + N + ' = 0  (wrap!)', canvasWidth / 2, 60);
    textFont('sans-serif');
  }

  noStroke(); fill('black'); textSize(13); textAlign(LEFT, CENTER);
  text('Modulo (%) keeps the position inside 0-' + (N - 1) + ', so the strip loops forever.',
       15, drawHeight + 60);
  textSize(defaultTextSize);
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
