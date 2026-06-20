// Bike Light Circuit Diagram - Moving Rainbow MicroSim
// The full capstone wiring: power bank, Pico, button, and LED strip. Click a
// component for its role, or a wire to trace its path. (Apply: trace signals.)
// CANVAS_HEIGHT: 420
let canvasWidth = 700;
let drawHeight = 380;
let controlHeight = 40;
let canvasHeight = drawHeight + controlHeight;
let margin = 12;
let defaultTextSize = 16;

let selectedWire = -1, selectedComp = '';
let wires = [], comps = [];

const compNotes = {
  pico: 'Raspberry Pi Pico - the microcontroller that runs your code and drives the strip.',
  strip: 'WS2812B LED strip - 8 addressable pixels, each set by your program.',
  button: 'Momentary button - cycles the animation mode each time it is pressed.',
  power: 'USB power bank - the 5 V source that powers the whole bike light.',
};

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));
  describe('A wiring diagram of a bike light: a USB power bank, a Raspberry Pi Pico, ' +
    'a momentary button, and an 8-pixel LED strip, joined by clickable colored wires.', LABEL);
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill('aliceblue'); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  noStroke(); fill('black'); textSize(17); textAlign(LEFT, TOP);
  text('Bike Light Wiring', margin, 10);

  const cx = canvasWidth * 0.40, pw = 120, ph = 200, py = 110;
  const px = cx;

  // Pico pins
  const pinVBUS = [px + pw, py + 40], pinGNDr = [px + pw, py + 95], pinGP0 = [px + pw, py + 150];
  const pinGP15 = [px, py + 60], pinGNDl = [px, py + 130];

  // power bank (top-right)
  const powX = canvasWidth - 170, powY = 36, powW = 150, powH = 46;
  const pow5V = [powX, powY + 14], powGND = [powX, powY + 34];

  // strip (right)
  const strX = canvasWidth - 170, strY = 150, strW = 150, strH = 50;
  const str5V = [strX, strY + 10], strGND = [strX, strY + 25], strDIN = [strX, strY + 42];

  // button (left)
  const btnX = 30, btnY = 200, btnW = 70, btnH = 44;
  const btnL1 = [btnX + btnW, btnY + 12], btnL2 = [btnX + btnW, btnY + 32];

  // ----- wires (draw first, under components) -----
  wires = [
    {pts: [pow5V, pinVBUS, str5V], col: [210, 40, 40], name: '+5V power', sig: '+5 V from the power bank to the Pico VBUS pin and the strip 5V pin.'},
    {pts: [powGND, pinGNDr, strGND], col: [30, 30, 30], name: 'Ground (0V)', sig: 'Shared 0 V ground between the power bank, Pico, and strip.'},
    {pts: [pinGP0, strDIN], col: [220, 190, 40], name: 'Data (GP0)', sig: 'Color data from GP0 to the strip Data In. Add a 330Ω resistor in-line.'},
    {pts: [pinGP15, btnL1], col: [40, 170, 70], name: 'Button (GP15)', sig: 'GP15 reads the button press to change modes.'},
    {pts: [btnL2, pinGNDl], col: [30, 30, 30], name: 'Ground (0V)', sig: 'The other button leg returns to ground.'},
  ];
  for (let i = 0; i < wires.length; i++) {
    const w = wires[i];
    stroke(w.col[0], w.col[1], w.col[2]); strokeWeight(selectedWire === i ? 6 : 3); noFill();
    beginShape();
    for (const p of w.pts) vertex(p[0], p[1]);
    endShape();
  }

  // ----- components -----
  comps = [];
  // Pico
  fill(28, 110, 70); noStroke(); rect(px, py, pw, ph, 8);
  fill(200); textSize(11); textAlign(CENTER, TOP); text('Pico', px + pw / 2, py + 6);
  drawPad(pinVBUS, 'VBUS', 'right'); drawPad(pinGNDr, 'GND', 'right'); drawPad(pinGP0, 'GP0', 'right');
  drawPad(pinGP15, 'GP15', 'left'); drawPad(pinGNDl, 'GND', 'left');
  comps.push({ x: px, y: py, w: pw, h: ph, key: 'pico' });

  // power bank
  fill(70, 70, 80); rect(powX, powY, powW, powH, 6);
  noStroke(); fill(240); textSize(11); textAlign(CENTER, CENTER); text('USB Power Bank (5V)', powX + powW / 2, powY + powH / 2);
  comps.push({ x: powX, y: powY, w: powW, h: powH, key: 'power' });

  // strip
  fill(20); rect(strX, strY, strW, strH, 6);
  const n = 8, ps = (strW - 40) / n;
  for (let i = 0; i < n; i++) {
    const hue = (i / n) * 360, rgb = hsv(hue);
    noStroke(); fill(rgb[0], rgb[1], rgb[2]); rect(strX + 36 + i * ps + 1, strY + strH / 2 - 6, ps - 2, 12, 2);
  }
  noStroke(); fill(210); textSize(9); textAlign(LEFT, CENTER);
  text('5V', strX + 14, str5V[1]); text('GND', strX + 14, strGND[1]); text('DIN', strX + 14, strDIN[1]);
  comps.push({ x: strX, y: strY, w: strW, h: strH, key: 'strip' });

  // button
  fill(150); rect(btnX, btnY, btnW, btnH, 6);
  noStroke(); fill(40); textSize(10); textAlign(CENTER, TOP); text('Button', btnX + btnW / 2, btnY + 4);
  fill(80); circle(btnX + btnW / 2, btnY + btnH / 2 + 4, 16);
  comps.push({ x: btnX, y: btnY, w: btnW, h: btnH, key: 'button' });

  drawCard();

  noStroke(); fill('black'); textSize(12); textAlign(LEFT, CENTER);
  text(selectedWire >= 0 ? 'Wire: ' + wires[selectedWire].name + ' selected.'
       : selectedComp ? compNotes[selectedComp].slice(0, 60) + '...'
       : 'Click a wire to trace it, or a component to learn its role.', margin, drawHeight + 20);
  textSize(defaultTextSize);
}

function drawPad(p, label, side) {
  noStroke(); fill(212, 175, 55); rect(p[0] - 6, p[1] - 6, 12, 12, 2);
  noStroke(); fill(255); textSize(9);
  if (side === 'right') { textAlign(LEFT, CENTER); text(label, p[0] - 38, p[1]); }
  else { textAlign(RIGHT, CENTER); text(label, p[0] + 38, p[1]); }
}

function hsv(h) {
  let c = 1, x = 1 * (1 - Math.abs(((h / 60) % 2) - 1)), r = 0, g = 0, b = 0;
  if (h < 60) { r = c; g = x; } else if (h < 120) { r = x; g = c; }
  else if (h < 180) { g = c; b = x; } else if (h < 240) { g = x; b = c; }
  else if (h < 300) { r = x; b = c; } else { r = c; b = x; }
  return [r * 255, g * 255, b * 255];
}

function drawCard() {
  let txt = '';
  if (selectedWire >= 0) txt = wires[selectedWire].name + ': ' + wires[selectedWire].sig;
  else if (selectedComp) txt = compNotes[selectedComp];
  else return;
  const cw = 280, cx0 = margin, cy = 300;
  noStroke(); fill(255, 255, 255, 240); stroke(120); rect(cx0, cy, cw, 70, 8);
  noStroke(); fill(20); textSize(12); textAlign(LEFT, TOP); textWrap(WORD);
  text(txt, cx0 + 10, cy + 10, cw - 20);
}

function mousePressed() {
  for (let i = 0; i < wires.length; i++) {
    const pts = wires[i].pts;
    for (let k = 0; k < pts.length - 1; k++) {
      if (distToSeg(mouseX, mouseY, pts[k][0], pts[k][1], pts[k + 1][0], pts[k + 1][1]) < 8) {
        selectedWire = i; selectedComp = ''; return;
      }
    }
  }
  for (const c of comps) {
    if (mouseX > c.x && mouseX < c.x + c.w && mouseY > c.y && mouseY < c.y + c.h) {
      selectedComp = c.key; selectedWire = -1; return;
    }
  }
  selectedWire = -1; selectedComp = '';
}

function distToSeg(px, py, x1, y1, x2, y2) {
  const dx = x2 - x1, dy = y2 - y1;
  const t = (dx === 0 && dy === 0) ? 0 : Math.max(0, Math.min(1, ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)));
  return dist(px, py, x1 + t * dx, y1 + t * dy);
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
