// Ripple Animation Simulator - Moving Rainbow MicroSim
// Press Pulse to send a brightness wave outward from the center. Decay and
// distance combine to shape the ripple. (Analyze: phase + distance.)
// CANVAS_HEIGHT: 310
let canvasWidth = 700;
let drawHeight = 190;
let controlHeight = 120;
let canvasHeight = drawHeight + controlHeight;
let margin = 15;
let defaultTextSize = 16;

const N = 20;
const CENTER = (N - 1) / 2;
let phase = 0;
let active = false;
let pulseButton, decaySlider, speedSlider, loopCheckbox;

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));

  pulseButton = createButton('Pulse');
  pulseButton.position(15, drawHeight + 10);
  pulseButton.mousePressed(() => { phase = 0; active = true; });

  loopCheckbox = createCheckbox('Loop', false);
  loopCheckbox.position(90, drawHeight + 12);

  decaySlider = createSlider(0.2, 0.9, 0.45, 0.05);
  decaySlider.position(130, drawHeight + 46);
  decaySlider.size(150);

  speedSlider = createSlider(1, 5, 2, 1);
  speedSlider.position(130, drawHeight + 80);
  speedSlider.size(150);

  describe('A 20-pixel strip where a brightness ripple expands outward from the ' +
    'center; sliders control how fast it moves and how quickly it fades.', LABEL);
}

function brightnessAt(d, decay) {
  let val = Math.cos((d - phase) * 0.6);
  if (val < 0) val = 0;
  const atten = Math.exp(-d * decay * 0.22);
  return val * atten;
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill(18); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  const decay = decaySlider.value(), sp = speedSlider.value();

  noStroke(); fill(220); textSize(15); textAlign(LEFT, TOP);
  text('Ripple from the center', margin, 12);

  const areaW = canvasWidth - 2 * margin;
  const spacing = areaW / N;
  const r = Math.min(spacing * 0.34, 16);
  const y = 96;
  let sampleD = Math.max(0, Math.round(phase));
  for (let i = 0; i < N; i++) {
    const x = margin + spacing * (i + 0.5);
    const d = Math.abs(i - CENTER);
    const b = active ? brightnessAt(d, decay) : 0.05;
    noStroke();
    if (b > 0.1) for (let g = 3; g >= 1; g--) { fill(80, 170, 255, 40 * b); circle(x, y, r * 2 + g * 6); }
    fill(60 * b + 20, 150 * b + 20, 255 * b + 20);
    stroke(60); strokeWeight(1); circle(x, y, r * 2);
    // center marker (just below the two middle pixels)
    if (i === 10) { noStroke(); fill(255); circle((x + (margin + spacing * (9 + 0.5))) / 2, y + r + 4, 5); }
  }

  // advance ripple
  if (active) {
    phase += 0.08 * sp;
    if (phase > N / 2 + 4) {
      if (loopCheckbox.checked()) phase = 0;
      else active = false;
    }
  }

  // formula
  const d = sampleD, b = brightnessAt(d, decay);
  noStroke(); fill('lightgreen'); textFont('monospace'); textSize(12); textAlign(LEFT, TOP);
  text('brightness = cos((dist - phase) * 0.6) = cos((' + d + ' - ' + phase.toFixed(1) + ') * 0.6) = ' + b.toFixed(2),
       margin, 156);
  textFont('sans-serif');

  // labels
  noStroke(); fill('black'); textSize(13); textAlign(LEFT, CENTER);
  text('Decay: ' + decay.toFixed(2), 15, drawHeight + 53);
  text('Speed: ' + sp, 15, drawHeight + 87);
  textSize(defaultTextSize);
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
