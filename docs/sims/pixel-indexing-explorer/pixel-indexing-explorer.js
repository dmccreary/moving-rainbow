// Pixel Indexing Explorer - Moving Rainbow MicroSim
// Set any pixel 0-9 to a color and see the Python that produces it. "Write"
// animates the data wave down the strip. (Apply: predict which pixel lights.)
// CANVAS_HEIGHT: 290
let canvasWidth = 700;
let drawHeight = 194;
let controlHeight = 96;
let canvasHeight = drawHeight + controlHeight;
let margin = 12;
let defaultTextSize = 16;

const N = 10;
const OFF = [40, 40, 40];
let pixels = [];
let lastCode = 'Set a pixel to see its Python code.';
let writeFront = -1;   // -1 = idle, 0..N during animation

let indexInput, colorSelect, setButton, clearButton, writeButton;
const colorMap = {
  red: [255, 0, 0], green: [0, 255, 0], blue: [0, 0, 255],
  white: [255, 255, 255], yellow: [255, 255, 0], off: OFF,
};

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));
  for (let i = 0; i < N; i++) pixels.push(OFF.slice());

  indexInput = createInput('3', 'number');
  indexInput.position(55, drawHeight + 10); indexInput.size(46);

  colorSelect = createSelect();
  colorSelect.position(170, drawHeight + 10);
  for (const k of ['red', 'green', 'blue', 'white', 'yellow', 'off']) colorSelect.option(k);
  colorSelect.selected('green');

  setButton = createButton('Set Pixel');
  setButton.position(270, drawHeight + 10);
  setButton.mousePressed(setPixel);

  clearButton = createButton('Clear All');
  clearButton.position(55, drawHeight + 50);
  clearButton.mousePressed(() => { for (let i = 0; i < N; i++) pixels[i] = OFF.slice(); lastCode = 'strip.fill((0, 0, 0))   # all pixels off'; });

  writeButton = createButton('Write');
  writeButton.position(150, drawHeight + 50);
  writeButton.style('background-color', '#41BAC1');
  writeButton.style('color', 'white');
  writeButton.mousePressed(() => writeFront = 0);

  describe('A ten-pixel LED strip where students set a pixel by index and color, ' +
    'see the matching Python code, and animate the data wave with Write.', LABEL);
}

function setPixel() {
  let idx = parseInt(indexInput.value(), 10);
  if (isNaN(idx)) return;
  idx = constrain(idx, 0, N - 1);
  indexInput.value(idx);
  const key = colorSelect.value();
  const c = colorMap[key];
  pixels[idx] = c.slice();
  lastCode = 'strip[' + idx + '] = (' + (key === 'off' ? '0, 0, 0' : c.join(', ')) + ')   # ' + key;
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill(20); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  noStroke(); fill(230); textSize(15); textAlign(LEFT, TOP); text('strip = NeoPixel strip (10 pixels)', margin, 10);

  const areaW = canvasWidth - 2 * margin;
  const spacing = areaW / N;
  const r = Math.min(spacing * 0.32, 22);
  const y = 86;
  for (let i = 0; i < N; i++) {
    const x = margin + spacing * (i + 0.5);
    const lit = !(pixels[i][0] === OFF[0] && pixels[i][1] === OFF[1] && pixels[i][2] === OFF[2]);
    noStroke();
    if (lit) for (let g = 3; g >= 1; g--) { fill(pixels[i][0], pixels[i][1], pixels[i][2], 40); circle(x, y, r * 2 + g * 6); }
    fill(pixels[i][0], pixels[i][1], pixels[i][2]);
    stroke(70); strokeWeight(1); circle(x, y, r * 2);
    // write wave highlight
    if (writeFront === i) { noFill(); stroke('white'); strokeWeight(3); circle(x, y, r * 2 + 12); }
    noStroke(); fill(180); textSize(13); textAlign(CENTER, TOP); text(i, x, y + r + 6);
  }

  // advance write wave
  if (writeFront >= 0) {
    if (frameCount % 4 === 0) writeFront++;
    if (writeFront >= N) writeFront = -1;
  }

  // code line
  noStroke(); fill(40, 50, 60); rect(margin, drawHeight - 34, canvasWidth - 2 * margin, 26, 4);
  fill('lightgreen'); textFont('monospace'); textSize(14); textAlign(LEFT, CENTER);
  text(lastCode, margin + 8, drawHeight - 21);
  textFont('sans-serif');

  // control labels
  noStroke(); fill('black'); textSize(12); textAlign(LEFT, CENTER);
  text('Index', 14, drawHeight + 22);
  text('Color', 118, drawHeight + 22);
  text('After Set, press Write to send the colors down the strip.', 250, drawHeight + 62);
  textSize(defaultTextSize);
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
