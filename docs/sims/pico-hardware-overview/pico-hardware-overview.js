// Raspberry Pi Pico Hardware Overview - Moving Rainbow MicroSim
// A top-down map of the Pico board. Click any labeled region to open a card
// with its name, description, and a fact. (Remember: identify board parts.)
// CANVAS_HEIGHT: 430
let canvasWidth = 700;
let drawHeight = 390;
let controlHeight = 40;
let canvasHeight = drawHeight + controlHeight;
let margin = 12;
let defaultTextSize = 16;

let selected = null;
let regions = [];

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));
  describe('A labeled top-down diagram of the Raspberry Pi Pico board; clicking a ' +
    'region opens a card describing that part.', LABEL);
}

function buildRegions(cx, y0, bw, bh) {
  const L = cx - bw / 2, R = cx + bw / 2;
  regions = [
    {x: cx - 26, y: y0 - 14, w: 52, h: 22, name: 'USB connector',
     desc: 'Micro-USB port.', fact: 'Connects to your computer for power and programming.'},
    {x: L + 6, y: y0 + 16, w: 34, h: 20, name: 'BOOTSEL button',
     desc: 'Firmware-flash button.', fact: 'Hold it while plugging in USB to load new firmware.'},
    {x: cx + 34, y: y0 + 22, w: 22, h: 16, name: 'Onboard LED',
     desc: 'Built-in green LED.', fact: 'Wired to GPIO 25 - great for your first blink.'},
    {x: cx - 38, y: y0 + bh * 0.40, w: 76, h: 76, name: 'RP2040 chip',
     desc: 'The microcontroller.', fact: 'Dual ARM Cortex-M0+ cores running up to 133 MHz.'},
    {x: L - 8, y: y0 + 60, w: 14, h: bh - 150, name: 'Left GPIO bank',
     desc: 'Pins GP0-GP14.', fact: 'General-purpose input/output - our LED data pin GP0 lives here.'},
    {x: R - 6, y: y0 + 60, w: 14, h: bh - 200, name: 'Right GPIO bank',
     desc: 'Pins GP15-GP28.', fact: 'More GPIO, plus ADC pins for analog sensors.'},
    {x: R - 6, y: y0 + bh - 132, w: 14, h: 16, name: 'GND pin',
     desc: 'Ground pin.', fact: 'The common reference for every circuit you build.'},
    {x: R - 6, y: y0 + bh - 108, w: 14, h: 16, name: '3.3V OUT pin',
     desc: 'Regulated 3.3 V output.', fact: 'Powers sensors and small components.'},
    {x: R - 6, y: y0 + bh - 84, w: 14, h: 16, name: 'VSYS pin',
     desc: 'Raw supply voltage.', fact: 'From USB or a battery, 4.5-5.5 V.'},
  ];
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill('aliceblue'); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  const bw = 150, bh = 320, y0 = 44;
  const cx = canvasWidth * 0.34;
  buildRegions(cx, y0, bw, bh);

  // board
  noStroke(); fill(28, 110, 70); rect(cx - bw / 2, y0, bw, bh, 10);
  // pin headers (decorative)
  fill(212, 175, 55);
  for (let i = 0; i < 20; i++) {
    rect(cx - bw / 2 - 6, y0 + 60 + i * 12, 8, 8, 2);
    rect(cx + bw / 2 - 2, y0 + 60 + i * 12, 8, 8, 2);
  }
  // USB
  fill(200); rect(cx - 24, y0 - 12, 48, 18, 3);
  // RP2040
  fill(20); rect(cx - 38, y0 + bh * 0.40, 76, 76, 4);
  noStroke(); fill(180); textSize(11); textAlign(CENTER, CENTER); text('RP2040', cx, y0 + bh * 0.40 + 38);
  // onboard LED
  fill('lime'); circle(cx + 40, y0 + 30, 10);
  // BOOTSEL
  fill(120); rect(cx - bw / 2 + 6, y0 + 16, 30, 16, 2);

  // highlight selected region
  if (selected) {
    noFill(); stroke('yellow'); strokeWeight(3);
    rect(selected.x, selected.y, selected.w, selected.h, 3);
  }

  // title
  noStroke(); fill('black'); textSize(18); textAlign(LEFT, TOP);
  text('Raspberry Pi Pico', margin, 12);

  drawCard();

  noStroke(); fill('black'); textSize(13); textAlign(LEFT, CENTER);
  text(selected ? 'Click another part, or the board to close.' : 'Click a labeled part of the board.',
       margin, drawHeight + 20);
  textSize(defaultTextSize);
}

function drawCard() {
  const cx0 = canvasWidth * 0.58;
  const cw = canvasWidth - cx0 - margin;
  if (cw < 120) return;
  noStroke(); fill(255, 255, 255, 240); stroke(170); rect(cx0, 60, cw, 150, 10);
  noStroke();
  if (!selected) {
    fill(120); textSize(14); textAlign(CENTER, CENTER);
    text('Tap any labeled region\nto learn what it is.', cx0 + cw / 2, 135);
    return;
  }
  fill(20, 60, 110); textSize(18); textAlign(LEFT, TOP);
  text(selected.name, cx0 + 14, 74);
  fill(40); textSize(14); textWrap(WORD);
  text(selected.desc, cx0 + 14, 104, cw - 28);
  fill(90); textSize(13);
  text('Fact: ' + selected.fact, cx0 + 14, 138, cw - 28);
}

function mousePressed() {
  for (const r of regions) {
    if (mouseX > r.x && mouseX < r.x + r.w && mouseY > r.y && mouseY < r.y + r.h) {
      selected = (selected === r) ? null : r; return;
    }
  }
  selected = null;
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
