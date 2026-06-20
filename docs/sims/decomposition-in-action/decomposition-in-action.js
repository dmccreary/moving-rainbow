// Decomposition in Action - Moving Rainbow MicroSim
// Left panel: a moving rainbow on a simulated 30-LED strip.
// Right panel: the decomposition tree of sub-problems, revealed one level
// at a time so students see how a big problem breaks into small ones.
// CANVAS_HEIGHT: 420
let canvasWidth = 760;
let drawHeight = 370;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let margin = 15;
let defaultTextSize = 16;

const NUM_LEDS = 30;
let offset = 0;
let revealLevel = 0;        // 0 = root only, up to 3
let animateOn = true;
let selectedId = null;      // clicked tree node id (tooltip)

let decomposeButton, resetButton, animateCheckbox;
let nodes = [];

// Convert HSV (h:0-360, s,v:0-1) to an [r,g,b] array (0-255).
function hsvToRgb(h, s, v) {
  let c = v * s;
  let x = c * (1 - Math.abs(((h / 60) % 2) - 1));
  let m = v - c;
  let r = 0, g = 0, b = 0;
  if (h < 60)      { r = c; g = x; }
  else if (h < 120){ r = x; g = c; }
  else if (h < 180){ g = c; b = x; }
  else if (h < 240){ g = x; b = c; }
  else if (h < 300){ r = x; b = c; }
  else             { r = c; b = x; }
  return [(r + m) * 255, (g + m) * 255, (b + m) * 255];
}

function buildNodes() {
  // level: smallest reveal step at which the node becomes visible (root = 0)
  nodes = [
    {id:'root', lines:['Moving Rainbow','Animation'], level:0, col:[100,37,128], parent:null,
     desc:'The whole animation — before we break it into smaller pieces.'},
    {id:'a', lines:['Set pixel','colors'], level:1, col:[65,186,193], parent:'root',
     desc:'Decide what color each LED should be.'},
    {id:'b', lines:['Shift by 1','each frame'], level:1, col:[65,186,193], parent:'root',
     desc:'Move the whole pattern one pixel each frame.'},
    {id:'c', lines:['Loop','forever'], level:1, col:[65,186,193], parent:'root',
     desc:'Repeat the steps so the motion never stops.'},
    {id:'a1', lines:['hue = position','+ offset'], level:2, col:[232,144,58], parent:'a',
     desc:'A pixel hue depends on its position plus a moving offset.'},
    {id:'a2', lines:['Convert','hue to RGB'], level:2, col:[232,144,58], parent:'a',
     desc:'Translate each hue into red, green, and blue values.'},
    {id:'b1', lines:['offset += 1','each frame'], level:3, col:[232,144,58], parent:'b',
     desc:'Add one to the offset every frame to create motion.'},
    {id:'b2', lines:['Use % to','wrap around'], level:3, col:[232,144,58], parent:'b',
     desc:'Modulo keeps the offset inside the color wheel.'},
  ];
}

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));
  buildNodes();

  decomposeButton = createButton('Decompose');
  decomposeButton.position(10, drawHeight + 12);
  decomposeButton.mousePressed(() => { if (revealLevel < 3) revealLevel++; });

  resetButton = createButton('Reset');
  resetButton.position(110, drawHeight + 12);
  resetButton.mousePressed(() => { revealLevel = 0; selectedId = null; });

  animateCheckbox = createCheckbox('Animate', true);
  animateCheckbox.position(180, drawHeight + 14);
  animateCheckbox.changed(() => { animateOn = animateCheckbox.checked(); });

  describe('A moving rainbow on a simulated LED strip beside a decomposition ' +
    'tree that reveals the sub-problems of the animation one level at a time.', LABEL);
}

// Compute node x/y from the current right-panel geometry.
function layoutNodes(splitX, rightW) {
  const bw = Math.min(rightW * 0.3, 130);
  const cx = splitX + rightW / 2;
  for (const n of nodes) {
    if (n.id === 'root') { n.x = cx; n.y = 48; }
    else if (n.id === 'a') { n.x = splitX + rightW * 0.22; n.y = 140; }
    else if (n.id === 'b') { n.x = splitX + rightW * 0.55; n.y = 140; }
    else if (n.id === 'c') { n.x = splitX + rightW * 0.85; n.y = 140; }
    else if (n.id === 'a1') { n.x = splitX + rightW * 0.22; n.y = 222; }
    else if (n.id === 'a2') { n.x = splitX + rightW * 0.22; n.y = 296; }
    else if (n.id === 'b1') { n.x = splitX + rightW * 0.55; n.y = 222; }
    else if (n.id === 'b2') { n.x = splitX + rightW * 0.55; n.y = 296; }
    n.w = bw; n.h = 50;
  }
}

function nodeById(id) { return nodes.find(n => n.id === id); }

function draw() {
  updateCanvasSize();
  const splitX = Math.max(canvasWidth * 0.42, 180);
  const rightW = canvasWidth - splitX - margin;
  layoutNodes(splitX, rightW);

  // Control region background
  noStroke();
  fill('white');
  rect(0, drawHeight, canvasWidth, controlHeight);

  // ---- Left panel: LED strip ----
  noStroke();
  fill(17);
  rect(0, 0, splitX, drawHeight);
  drawLeds(splitX);

  // ---- Right panel: decomposition tree ----
  fill(240);
  stroke('silver');
  rect(splitX, 0, canvasWidth - splitX, drawHeight);
  drawTree();

  // Title
  noStroke();
  fill('black');
  textSize(20);
  textAlign(LEFT, TOP);
  text('Decomposition in Action', margin, 10);
  textAlign(LEFT, CENTER);
  textSize(defaultTextSize);

  // Tooltip
  if (selectedId) drawTooltip(splitX);

  // Animate
  if (animateOn) offset += 1;

  // Control labels
  noStroke();
  fill('black');
  textSize(13);
  textAlign(LEFT, CENTER);
  text('Clicks reveal levels: ' + revealLevel + ' / 3   (click a node to learn about it)',
       300, drawHeight + 25);
  textSize(defaultTextSize);
}

function drawLeds(splitX) {
  const leftW = splitX;
  const cols = 10, rowsN = 3;
  const cellW = (leftW - 2 * margin) / cols;
  const cellH = 60;
  const startY = drawHeight / 2 - cellH;
  const r = Math.min(cellW, cellH) * 0.32;
  for (let i = 0; i < NUM_LEDS; i++) {
    const row = Math.floor(i / cols);
    const col = i % cols;
    const x = margin + cellW * (col + 0.5);
    const y = startY + cellH * row + cellH / 2;
    const hue = (((i + offset) / NUM_LEDS) * 360) % 360;
    const rgb = hsvToRgb(hue, 1, 1);
    // glow
    noStroke();
    for (let g = 4; g >= 1; g--) {
      fill(rgb[0], rgb[1], rgb[2], 40);
      circle(x, y, r * 2 + g * 6);
    }
    fill(rgb[0], rgb[1], rgb[2]);
    circle(x, y, r * 2);
  }
  noStroke();
  fill(200);
  textSize(12);
  textAlign(CENTER, TOP);
  text('30 simulated LEDs', leftW / 2, startY + cellH * rowsN + 8);
  textAlign(LEFT, CENTER);
}

function drawTree() {
  // connector lines first
  stroke(120);
  strokeWeight(1.5);
  for (const n of nodes) {
    if (n.level > revealLevel || !n.parent) continue;
    const p = nodeById(n.parent);
    line(p.x, p.y + p.h / 2, n.x, n.y - n.h / 2);
  }
  // nodes
  for (const n of nodes) {
    if (n.level > revealLevel) continue;
    const hot = (n.id === selectedId);
    stroke(hot ? 'black' : 'white');
    strokeWeight(hot ? 3 : 1);
    fill(n.col[0], n.col[1], n.col[2]);
    rectMode(CENTER);
    rect(n.x, n.y, n.w, n.h, 8);
    rectMode(CORNER);
    noStroke();
    fill('white');
    textSize(12);
    textAlign(CENTER, CENTER);
    for (let k = 0; k < n.lines.length; k++) {
      text(n.lines[k], n.x, n.y - 7 + k * 15);
    }
  }
  textAlign(LEFT, CENTER);
}

function drawTooltip(splitX) {
  const n = nodeById(selectedId);
  if (!n) return;
  const boxW = splitX - 2 * margin;
  const boxH = 54;
  const bx = margin, by = drawHeight - boxH - 10;
  noStroke();
  fill(255, 255, 255, 235);
  stroke(180);
  strokeWeight(1);
  rect(bx, by, boxW, boxH, 8);
  noStroke();
  fill(20);
  textSize(13);
  textAlign(LEFT, TOP);
  textWrap(WORD);
  text(n.desc, bx + 10, by + 8, boxW - 20, boxH - 12);
  textAlign(LEFT, CENTER);
}

function mousePressed() {
  // hit test tree nodes
  for (const n of nodes) {
    if (n.level > revealLevel) continue;
    if (Math.abs(mouseX - n.x) < n.w / 2 && Math.abs(mouseY - n.y) < n.h / 2) {
      selectedId = (selectedId === n.id) ? null : n.id;
      return;
    }
  }
}

function windowResized() {
  updateCanvasSize();
  resizeCanvas(canvasWidth, canvasHeight);
}

function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
