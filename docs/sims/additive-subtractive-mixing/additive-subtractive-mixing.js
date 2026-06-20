// Additive vs Subtractive Color Mixing - Moving Rainbow MicroSim
// Left: light (LEDs) mixes by ADDING. Right: paint mixes by SUBTRACTING.
// Hover over an overlap to see what the mix makes. (Understand the difference.)
// CANVAS_HEIGHT: 360
let canvasWidth = 700;
let drawHeight = 310;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let margin = 12;
let defaultTextSize = 16;

let mode = 'Light';      // 'Light' or 'Paint' (which panel is emphasized)
let modeButton;
let leftCircles = [], rightCircles = [];
let hoverMsg = '';

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));
  modeButton = createButton('Emphasize: Light Mode');
  modeButton.position(10, drawHeight + 12);
  modeButton.mousePressed(() => {
    mode = (mode === 'Light') ? 'Paint' : 'Light';
    modeButton.html('Emphasize: ' + mode + ' Mode');
  });
  describe('Two panels comparing additive light mixing (red, green, blue) with ' +
    'subtractive paint mixing (cyan, magenta, yellow), with hover explanations.', LABEL);
}

function panelCircles(px, pw, pcol) {
  const cx = px + pw / 2, cy = 50 + (drawHeight - 70) / 2;
  const r = Math.min(pw * 0.34, 120);
  const o = r * 0.42;
  return [
    {x: cx, y: cy - o, r, c: pcol[0]},
    {x: cx - o, y: cy + o * 0.7, r, c: pcol[1]},
    {x: cx + o, y: cy + o * 0.7, r, c: pcol[2]},
  ];
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill('aliceblue'); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  const pw = (canvasWidth - 3 * margin) / 2;
  const lx = margin, rx = margin * 2 + pw;
  const py = 46, ph = drawHeight - py - 8;

  leftCircles = panelCircles(lx, pw, [[255,0,0],[0,255,0],[0,0,255]]);
  rightCircles = panelCircles(rx, pw, [[0,255,255],[255,0,255],[255,255,0]]);

  // LEFT: additive (light) on black
  noStroke(); fill(10); rect(lx, py, pw, ph, 8);
  blendMode(ADD);
  for (const c of leftCircles) { fill(c.c[0], c.c[1], c.c[2]); noStroke(); circle(c.x, c.y, c.r * 2); }
  blendMode(BLEND);

  // RIGHT: subtractive (paint) on white
  noStroke(); fill(255); stroke(220); rect(rx, py, pw, ph, 8);
  blendMode(MULTIPLY);
  for (const c of rightCircles) { fill(c.c[0], c.c[1], c.c[2]); noStroke(); circle(c.x, c.y, c.r * 2); }
  blendMode(BLEND);

  // emphasis border
  noFill(); strokeWeight(4); stroke(255, 196, 0);
  if (mode === 'Light') rect(lx - 2, py - 2, pw + 4, ph + 4, 9);
  else rect(rx - 2, py - 2, pw + 4, ph + 4, 9);

  // panel titles
  noStroke(); textSize(15); textAlign(CENTER, TOP);
  fill('black'); text('Additive (Light - LEDs)', lx + pw / 2, 22);
  text('Subtractive (Paint - Pigments)', rx + pw / 2, 22);

  // hover detection + tooltip
  hoverMsg = '';
  if (mouseY > py && mouseY < py + ph) {
    if (mouseX > lx && mouseX < lx + pw) hoverMsg = mixMessage(leftCircles, 'light');
    else if (mouseX > rx && mouseX < rx + pw) hoverMsg = mixMessage(rightCircles, 'paint');
  }

  // control label / tooltip
  noStroke(); fill('black'); textSize(13); textAlign(LEFT, CENTER);
  const note = hoverMsg ||
    (mode === 'Light' ? 'Light starts black; adding colors makes it brighter, up to white.'
                      : 'Paint starts white; each pigment subtracts light, mixing toward black.');
  text(note, 210, drawHeight + 20);
  textSize(defaultTextSize);
}

function mixMessage(circles, kind) {
  const inside = circles.map(c => dist(mouseX, mouseY, c.x, c.y) < c.r);
  const names = (kind === 'light') ? ['Red', 'Green', 'Blue'] : ['Cyan', 'Magenta', 'Yellow'];
  const hit = [];
  for (let i = 0; i < 3; i++) if (inside[i]) hit.push(i);
  if (hit.length === 0) return '';
  const word = (kind === 'light') ? 'light' : 'paint';
  if (hit.length === 1) return names[hit[0]] + ' ' + word;
  let result;
  if (kind === 'light') {
    if (hit.length === 3) result = 'White';
    else if (hit.includes(0) && hit.includes(1)) result = 'Yellow';
    else if (hit.includes(1) && hit.includes(2)) result = 'Cyan';
    else result = 'Magenta';
  } else {
    if (hit.length === 3) result = 'Black';
    else if (hit.includes(0) && hit.includes(1)) result = 'Blue';
    else if (hit.includes(1) && hit.includes(2)) result = 'Red';
    else result = 'Green';
  }
  return hit.map(i => names[i]).join(' + ') + ' ' + word + ' = ' + result;
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
