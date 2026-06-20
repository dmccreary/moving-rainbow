// NeoPixel Wiring Diagram - Moving Rainbow MicroSim
// A Pico wired to a 10-pixel NeoPixel strip with three wires. Click a wire to
// learn what it does and what happens if you forget it. (Apply: wire a strip.)
// CANVAS_HEIGHT: 400
let canvasWidth = 700;
let drawHeight = 360;
let controlHeight = 40;
let canvasHeight = drawHeight + controlHeight;
let margin = 12;
let defaultTextSize = 16;

let selectedWire = -1;
let hoverPixel = -1;
let wires = [];

const wireInfo = [
  {name: 'Red wire: VSYS -> +5V', col: [220, 40, 40],
   does: 'Carries +5 V power from the Pico to the strip.',
   forget: 'Forget it and the strip gets no power - it stays completely dark.'},
  {name: 'Black wire: GND -> GND', col: [40, 40, 40],
   does: 'Completes the circuit - the shared 0 V reference for both boards.',
   forget: 'Forget it and nothing works, or the strip flickers unpredictably.'},
  {name: 'Green wire: GP0 -> DIN', col: [40, 170, 70],
   does: 'Carries the color data signal from the Pico into the strip.',
   forget: 'Forget it and the strip has power but never receives any colors.'},
];

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));
  describe('A wiring diagram connecting a Raspberry Pi Pico to a NeoPixel strip ' +
    'with power, ground, and data wires that can be clicked for explanations.', LABEL);
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill('aliceblue'); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  noStroke(); fill('black'); textSize(17); textAlign(LEFT, TOP);
  text('Wiring a NeoPixel Strip', margin, 10);

  // ---- Pico ----
  const px = 60, pw = 110, ph = 170, py = 70;
  noStroke(); fill(28, 110, 70); rect(px, py, pw, ph, 8);
  fill(200); textSize(11); textAlign(CENTER, TOP); text('Pico', px + pw / 2, py + 6);
  const picoPads = [
    {label: 'VSYS', y: py + 50}, {label: 'GND', y: py + 95}, {label: 'GP0', y: py + 140},
  ];
  for (const pad of picoPads) {
    fill(212, 175, 55); rect(px + pw - 6, pad.y - 6, 12, 12, 2);
    noStroke(); fill(255); textSize(10); textAlign(RIGHT, CENTER); text(pad.label, px + pw - 10, pad.y);
  }

  // ---- Strip ----
  const sw = 230, sx = canvasWidth - sw - 30, sy = 90, sh = 54;
  fill(20); rect(sx, sy, sw, sh, 6);
  const pads = [
    {label: '+5V', y: sy + 12}, {label: 'GND', y: sy + 27}, {label: 'DIN', y: sy + 42},
  ];
  for (const pad of pads) {
    fill(212, 175, 55); rect(sx - 6, pad.y - 5, 12, 10, 2);
    noStroke(); fill(230); textSize(9); textAlign(LEFT, CENTER); text(pad.label, sx + 8, pad.y);
  }
  // pixels
  const n = 10, pxSize = (sw - 70) / n;
  const pixY = sy + sh / 2;
  hoverPixel = -1;
  for (let i = 0; i < n; i++) {
    const cxp = sx + 60 + i * pxSize + pxSize / 2;
    const hue = (i / n) * 360;
    const rgb = hsv(hue);
    noStroke(); fill(rgb[0], rgb[1], rgb[2]); rect(cxp - pxSize * 0.38, pixY - 8, pxSize * 0.76, 16, 2);
    if (dist(mouseX, mouseY, cxp, pixY) < pxSize * 0.5) hoverPixel = i;
  }
  // data direction arrow
  noStroke(); fill(120); textSize(10); textAlign(CENTER, TOP);
  text('data flows ->', sx + sw / 2, sy + sh + 6);
  if (hoverPixel >= 0) {
    const cxp = sx + 60 + hoverPixel * pxSize + pxSize / 2;
    fill('black'); textSize(12); textAlign(CENTER, BOTTOM); text('index ' + hoverPixel, cxp, pixY - 12);
  }

  // ---- Wires ----
  wires = [
    {a: [px + pw, picoPads[0].y], b: [sx, pads[0].y]},
    {a: [px + pw, picoPads[1].y], b: [sx, pads[1].y]},
    {a: [px + pw, picoPads[2].y], b: [sx, pads[2].y]},
  ];
  for (let i = 0; i < 3; i++) {
    const w = wires[i], info = wireInfo[i];
    stroke(info.col[0], info.col[1], info.col[2]);
    strokeWeight(selectedWire === i ? 6 : 4);
    noFill();
    bezier(w.a[0], w.a[1], w.a[0] + 60, w.a[1] + (i - 1) * 10, w.b[0] - 60, w.b[1] + (i - 1) * 10, w.b[0], w.b[1]);
  }

  drawInset();
  drawWireCard();

  noStroke(); fill('black'); textSize(13); textAlign(LEFT, CENTER);
  text(selectedWire >= 0 ? 'Click another wire, or hover a pixel for its index.'
                         : 'Click a wire to learn what it does. Hover a pixel for its index.',
       margin, drawHeight + 20);
  textSize(defaultTextSize);
}

function hsv(h) {
  let c = 1, x = 1 * (1 - Math.abs(((h / 60) % 2) - 1)), m = 0, r = 0, g = 0, b = 0;
  if (h < 60) { r = c; g = x; } else if (h < 120) { r = x; g = c; }
  else if (h < 180) { g = c; b = x; } else if (h < 240) { g = x; b = c; }
  else if (h < 300) { r = x; b = c; } else { r = c; b = x; }
  return [(r + m) * 255, (g + m) * 255, (b + m) * 255];
}

function drawInset() {
  const ix = margin, iy = 250, iw = 200, ih = 96;
  noStroke(); fill(255, 255, 255, 235); stroke(170); rect(ix, iy, iw, ih, 8);
  noStroke(); fill(60); textSize(11); textAlign(LEFT, TOP); text('Inside one WS2812B pixel', ix + 8, iy + 6);
  // chip
  fill(40); rect(ix + 70, iy + 30, 60, 50, 4);
  noStroke(); fill(200); textSize(9); textAlign(CENTER, CENTER); text('Control IC', ix + 100, iy + 55);
  // RGB dies
  fill(255, 60, 60); circle(ix + 80, iy + 38, 7);
  fill(60, 255, 60); circle(ix + 100, iy + 38, 7);
  fill(60, 60, 255); circle(ix + 120, iy + 38, 7);
  fill(80); textSize(9); textAlign(RIGHT, CENTER); text('DIN', ix + 66, iy + 55);
  textAlign(LEFT, CENTER); text('DOUT', ix + 134, iy + 55);
}

function drawWireCard() {
  if (selectedWire < 0) return;
  const info = wireInfo[selectedWire];
  const cw = 300, cx0 = canvasWidth - cw - margin, cy = 200;
  noStroke(); fill(255, 255, 255, 240); stroke(info.col[0], info.col[1], info.col[2]); strokeWeight(2);
  rect(cx0, cy, cw, 130, 8);
  noStroke(); fill(info.col[0], info.col[1], info.col[2]); textSize(14); textAlign(LEFT, TOP);
  text(info.name, cx0 + 12, cy + 10);
  fill(40); textSize(13); textWrap(WORD);
  text('What it does: ' + info.does, cx0 + 12, cy + 36, cw - 24);
  fill(150, 40, 40);
  text('If you forget it: ' + info.forget, cx0 + 12, cy + 84, cw - 24);
}

function mousePressed() {
  for (let i = 0; i < wires.length; i++) {
    const w = wires[i];
    if (distToSeg(mouseX, mouseY, w.a[0], w.a[1], w.b[0], w.b[1]) < 10) { selectedWire = i; return; }
  }
  selectedWire = -1;
}

function distToSeg(px, py, x1, y1, x2, y2) {
  const dx = x2 - x1, dy = y2 - y1;
  const t = Math.max(0, Math.min(1, ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)));
  return dist(px, py, x1 + t * dx, y1 + t * dy);
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
