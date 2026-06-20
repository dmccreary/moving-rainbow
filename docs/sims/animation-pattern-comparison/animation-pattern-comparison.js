// Animation Pattern Comparison - Moving Rainbow MicroSim
// Six LED strips running six classic patterns at once. Match the moving
// pattern to its name and algorithm. (Analyze.)
// CANVAS_HEIGHT: 500
let canvasWidth = 700;
let drawHeight = 450;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let margin = 12;
let defaultTextSize = 16;

const N = 10;
let playing = true;
let t = 0;
let playButton, speedSlider;

const rows = [
  {name: 'Blink', desc: 'All pixels on, then all off.'},
  {name: 'Rainbow Static', desc: 'A fixed rainbow that holds still.'},
  {name: 'Moving Rainbow', desc: 'The rainbow scrolls along the strip.'},
  {name: 'Twinkle', desc: 'Random pixels sparkle on a dark strip.'},
  {name: 'Candle Flicker', desc: 'Warm colors wobble in brightness.'},
  {name: 'Random Colors', desc: 'Every pixel jumps to a random color.'},
];

let twinkle = new Array(N).fill(0);
let candle = new Array(N).fill(0.5);
let randomCols = [];

function hsv(h, s, v) {
  let c = v * s, x = c * (1 - Math.abs(((h / 60) % 2) - 1)), m = v - c;
  let r = 0, g = 0, b = 0;
  if (h < 60) { r = c; g = x; } else if (h < 120) { r = x; g = c; }
  else if (h < 180) { g = c; b = x; } else if (h < 240) { g = x; b = c; }
  else if (h < 300) { r = x; b = c; } else { r = c; b = x; }
  return [(r + m) * 255, (g + m) * 255, (b + m) * 255];
}

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));
  for (let i = 0; i < N; i++) randomCols.push(hsv(Math.random() * 360, 1, 1));

  playButton = createButton('Pause');
  playButton.position(15, drawHeight + 12);
  playButton.mousePressed(() => { playing = !playing; playButton.html(playing ? 'Pause' : 'Play'); });

  speedSlider = createSlider(1, 5, 3, 1);
  speedSlider.position(130, drawHeight + 15);
  speedSlider.size(160);

  describe('Six simulated LED strips running blink, static rainbow, moving rainbow, ' +
    'twinkle, candle flicker, and random color patterns side by side.', LABEL);
}

function updateStates(sp) {
  // twinkle: decay, occasional sparkle
  for (let i = 0; i < N; i++) {
    twinkle[i] *= 0.90;
    if (Math.random() < 0.02 * sp) twinkle[i] = 1;
  }
  // candle: random walk around mid brightness
  for (let i = 0; i < N; i++) {
    candle[i] += (Math.random() - 0.5) * 0.15 * sp;
    candle[i] = Math.max(0.35, Math.min(1, candle[i]));
  }
  // random colors: regenerate on an interval
  if (frameCount % Math.max(4, Math.round(24 / sp)) === 0) {
    for (let i = 0; i < N; i++) randomCols[i] = hsv(Math.random() * 360, 1, 1);
  }
}

function pixelColor(row, i, sp) {
  switch (row) {
    case 0: return (Math.floor(t / 30) % 2 === 0) ? [255, 220, 60] : [25, 25, 25];
    case 1: return hsv((i / N) * 360, 1, 1);
    case 2: return hsv((((i + t * 0.15) / N) * 360) % 360, 1, 1);
    case 3: { const b = twinkle[i]; return [180 * b + 10, 200 * b + 10, 255 * b + 10]; }
    case 4: { const b = candle[i]; return [255 * b, 120 * b, 20 * b]; }
    case 5: return randomCols[i];
  }
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill(20); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  const sp = speedSlider.value();
  if (playing) { t += sp; updateStates(sp); }

  const rowH = (drawHeight - 20) / rows.length;
  const stripX = 150, stripW = canvasWidth - stripX - 200;
  const spacing = stripW / N;
  const r = Math.min(spacing * 0.34, rowH * 0.28);

  for (let row = 0; row < rows.length; row++) {
    const cy = 22 + row * rowH + rowH / 2;
    // name
    noStroke(); fill(235); textSize(13); textAlign(LEFT, CENTER); text(rows[row].name, margin, cy);
    // pixels
    for (let i = 0; i < N; i++) {
      const x = stripX + spacing * (i + 0.5);
      const c = pixelColor(row, i, sp);
      noStroke(); fill(c[0], c[1], c[2]); stroke(60); strokeWeight(1); circle(x, cy, r * 2);
    }
    // description
    noStroke(); fill(160); textSize(11); textAlign(LEFT, CENTER);
    text(rows[row].desc, stripX + stripW + 14, cy);
  }

  noStroke(); fill('black'); textSize(13); textAlign(LEFT, CENTER);
  text('Speed: ' + sp, 300, drawHeight + 25);
  textSize(defaultTextSize);
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
