// Function Call Step-Through - Moving Rainbow MicroSim
// Trace a function call step by step: into the function, through each line,
// across the return, and back to the caller. Step-through, not autoplay (L2).
// CANVAS_HEIGHT: 410
let canvasWidth = 760;
let drawHeight = 360;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let margin = 12;
let defaultTextSize = 16;

let nextButton, prevButton, restartButton;
let step = 0;   // 0..6 -> displayed as Step 1..7

const callerCode = [
  'dim = scale_color((255, 0, 0), 0.5)',
  'print(dim)',
];
const funcCode = [
  'def scale_color(color, factor):',
  '    r = int(color[0] * factor)',
  '    g = int(color[1] * factor)',
  '    b = int(color[2] * factor)',
  '    return (r, g, b)',
];

const steps = [
  {panel:'caller', line:0, label:'Caller', expl:'Python reads scale_color((255,0,0), 0.5) and prepares to jump into the function.',
   vars:{}, ret:null},
  {panel:'func', line:0, label:'Enter function', expl:'Parameters are bound to the arguments.',
   vars:{color:'(255, 0, 0)', factor:'0.5'}, ret:null},
  {panel:'func', line:1, label:'Compute r', expl:'r = int(255 * 0.5) = 127',
   vars:{color:'(255, 0, 0)', factor:'0.5', r:'127'}, ret:null},
  {panel:'func', line:2, label:'Compute g', expl:'g = int(0 * 0.5) = 0',
   vars:{color:'(255, 0, 0)', factor:'0.5', r:'127', g:'0'}, ret:null},
  {panel:'func', line:3, label:'Compute b', expl:'b = int(0 * 0.5) = 0',
   vars:{color:'(255, 0, 0)', factor:'0.5', r:'127', g:'0', b:'0'}, ret:null},
  {panel:'func', line:4, label:'Return', expl:'return (127, 0, 0) - the function exits and sends this tuple back.',
   vars:{color:'(255, 0, 0)', factor:'0.5', r:'127', g:'0', b:'0'}, ret:'(127, 0, 0)'},
  {panel:'caller', line:1, label:'Back in caller', expl:'dim = (127, 0, 0); print(dim) shows (127, 0, 0).',
   vars:{dim:'(127, 0, 0)'}, ret:'(127, 0, 0)'},
];

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));

  prevButton = createButton('Previous');
  prevButton.position(10, drawHeight + 12);
  prevButton.mousePressed(() => { if (step > 0) step--; });

  nextButton = createButton('Next Step');
  nextButton.position(95, drawHeight + 12);
  nextButton.mousePressed(() => { if (step < steps.length - 1) step++; });

  restartButton = createButton('Restart');
  restartButton.position(190, drawHeight + 12);
  restartButton.mousePressed(() => step = 0);

  describe('A step-through tracer of a scale_color function call showing the active ' +
    'line, current variable values, and the return value at each of seven steps.', LABEL);
}

function draw() {
  updateCanvasSize();
  const splitX = Math.max(canvasWidth * 0.55, 320);
  const s = steps[step];

  noStroke();
  fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);
  fill('aliceblue'); stroke('silver'); rect(0, 0, splitX, drawHeight);

  // function panel tint when execution is inside it
  if (s.panel === 'func') { noStroke(); fill(225, 235, 255); rect(0, 196, splitX, drawHeight - 196); }
  noStroke(); fill(60); textSize(13); textAlign(LEFT, TOP);
  text('Caller code', margin, 12);
  text('Function body' + (s.panel === 'func' ? '  (inside)' : ''), margin, 188);

  drawCodeBlock(callerCode, 36, s.panel === 'caller' ? s.line : -1);
  drawCodeBlock(funcCode, 212, s.panel === 'func' ? s.line : -1);

  drawInspector(splitX);

  noStroke(); fill('black'); textSize(13); textAlign(LEFT, CENTER);
  text('Step ' + (step + 1) + ' of ' + steps.length, 270, drawHeight + 25);
  textSize(defaultTextSize);
}

function drawCodeBlock(lines, top, activeLine) {
  textFont('monospace'); textSize(13); textAlign(LEFT, TOP);
  for (let i = 0; i < lines.length; i++) {
    const y = top + i * 22;
    if (i === activeLine) {
      noStroke(); fill(255, 240, 130); rect(margin + 18, y - 2, 999, 20, 3);
      fill('red'); textSize(15); text('→', margin, y - 2); textSize(13);
    }
    noStroke();
    fill(lines[i].trim().startsWith('def') ? '#2b78e4' : 30);
    text(lines[i], margin + 22, y);
  }
  textFont('sans-serif');
}

function drawInspector(splitX) {
  const s = steps[step];
  const px = splitX + 12, pw = canvasWidth - splitX - 24;
  noStroke(); fill('white'); stroke('silver'); rect(splitX, 0, canvasWidth - splitX, drawHeight);
  noStroke(); fill(20); textSize(15); textAlign(LEFT, TOP);
  text('State Inspector', px, 14);
  fill(70); textSize(13);
  text('Step ' + (step + 1) + ' of 7: ' + s.label, px, 40);

  // variable table
  fill(20); textSize(13); text('Variables now:', px, 70);
  let y = 92;
  const keys = Object.keys(s.vars);
  if (keys.length === 0) { fill(120); text('(none yet)', px + 6, y); y += 20; }
  for (const k of keys) {
    noStroke(); fill(245); stroke(210); rect(px, y - 2, pw, 20, 3);
    noStroke(); fill('#7030a0'); textFont('monospace');
    text(k, px + 6, y); fill(40); text('= ' + s.vars[k], px + 60, y);
    textFont('sans-serif'); y += 24;
  }

  y += 6;
  fill(20); text('Return value:', px, y); y += 20;
  noStroke(); fill(s.ret ? [223,245,225] : [240,240,240]); stroke(180); rect(px, y - 2, pw, 22, 3);
  noStroke(); fill(s.ret ? [25,110,40] : 130); textFont('monospace');
  text(s.ret ? s.ret : '(blank until return)', px + 6, y);
  textFont('sans-serif'); y += 34;

  fill(20); textSize(13); text('What happens:', px, y); y += 18;
  fill(60); textWrap(WORD); text(s.expl, px, y, pw);
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
