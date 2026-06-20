// Variable Scope Explorer - Moving Rainbow MicroSim
// Click a variable name in the program to see whether it is global or local,
// where it lives, and why. Classify-on-click pattern (Understand L2).
// CANVAS_HEIGHT: 430
let canvasWidth = 760;
let drawHeight = 380;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let margin = 12;
let defaultTextSize = 16;

let globalsButton, localsButton;
let selectedVar = null;
let flashMode = null, flashUntil = 0;
let charW = 8;

const code = [
  'NUM_PIXELS = 30          # global',
  'BRIGHTNESS = 0.8         # global',
  '',
  'def fill_color(strip, color):',
  '    scaled = scale_color(color, BRIGHTNESS)',
  '    for i in range(NUM_PIXELS):',
  '        strip[i] = scaled',
  '    strip.write()',
  '',
  'def scale_color(color, factor):',
  '    r = int(color[0] * factor)',
  '    g = int(color[1] * factor)',
  '    b = int(color[2] * factor)',
  '    return (r, g, b)',
  '',
  'fill_color(strip, (255, 0, 0))',
];

const varInfo = {
  NUM_PIXELS: {scope:'GLOBAL', zone:null, expl:'Defined at module level - visible everywhere in the program.'},
  BRIGHTNESS: {scope:'GLOBAL', zone:null, expl:'Defined at module level - visible everywhere in the program.'},
  strip:      {scope:'LOCAL',  zone:'fill', expl:'A parameter of fill_color - created when fill_color is called.'},
  color:      {scope:'LOCAL',  zone:'both', expl:'A parameter inside a function. Each function has its OWN color - they do not share.'},
  scaled:     {scope:'LOCAL',  zone:'fill', expl:'Created inside fill_color. Python deletes it when the function ends.'},
  i:          {scope:'LOCAL',  zone:'fill', expl:'The loop variable, local to fill_color\'s for loop.'},
  factor:     {scope:'LOCAL',  zone:'scale', expl:'A parameter of scale_color.'},
  r:          {scope:'LOCAL',  zone:'scale', expl:'Created inside scale_color; gone when it returns.'},
  g:          {scope:'LOCAL',  zone:'scale', expl:'Created inside scale_color; gone when it returns.'},
  b:          {scope:'LOCAL',  zone:'scale', expl:'Created inside scale_color; gone when it returns.'},
};

let tokens = [];   // {line, col, len, name}
function buildTokens() {
  tokens = [];
  for (let li = 0; li < code.length; li++) {
    const text = code[li].split('#')[0];   // ignore comments
    for (const name of Object.keys(varInfo)) {
      const re = new RegExp('\\b' + name + '\\b', 'g');
      let m;
      while ((m = re.exec(text)) !== null) tokens.push({line: li, col: m.index, len: name.length, name});
    }
  }
}

const codeTop = 50, lineH = 19;

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));
  buildTokens();

  globalsButton = createButton('Highlight all globals');
  globalsButton.position(10, drawHeight + 12);
  globalsButton.mousePressed(() => { flashMode = 'global'; flashUntil = millis() + 1500; });

  localsButton = createButton('Highlight all locals');
  localsButton.position(170, drawHeight + 12);
  localsButton.mousePressed(() => { flashMode = 'local'; flashUntil = millis() + 1500; });

  describe('A Python program with two functions where students click variable ' +
    'names to learn whether each is global or local and which scope zone it lives in.', LABEL);
}

function draw() {
  updateCanvasSize();
  const splitX = Math.max(canvasWidth * 0.58, 320);

  noStroke();
  fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);
  fill(38); stroke('silver'); rect(0, 0, splitX, drawHeight);
  fill('white'); rect(splitX, 0, canvasWidth - splitX, drawHeight);

  if (flashMode && millis() > flashUntil) flashMode = null;

  // code
  textFont('monospace'); textSize(13); textAlign(LEFT, TOP);
  charW = textWidth('m');
  const x0 = margin;
  for (let li = 0; li < code.length; li++) {
    noStroke(); fill(code[li].includes('#') ? 150 : 220);
    text(code[li], x0, codeTop + li * lineH);
  }
  // highlight tokens
  for (const tk of tokens) {
    const info = varInfo[tk.name];
    const flashHit = flashMode && info.scope.toLowerCase() === flashMode;
    const selHit = (selectedVar === tk.name);
    if (!flashHit && !selHit) continue;
    const x = x0 + tk.col * charW, y = codeTop + tk.line * lineH;
    noStroke();
    fill(flashHit ? (flashMode === 'global' ? [255,235,90,180] : [120,170,255,160]) : [255,235,90,200]);
    rect(x - 1, y - 1, tk.len * charW + 2, 17, 3);
    fill(20); text(tk.name, x, y);
  }
  textFont('sans-serif');

  drawInspector(splitX);

  noStroke(); fill('black'); textSize(12); textAlign(LEFT, CENTER);
  text('Click any variable name in the code on the left.', 330, drawHeight + 25);
  textSize(defaultTextSize);
}

function drawInspector(splitX) {
  const px = splitX + 12, pw = canvasWidth - splitX - 24;
  noStroke(); fill(20); textSize(15); textAlign(LEFT, TOP);
  text('Scope Inspector', px, 14);

  if (selectedVar) {
    const info = varInfo[selectedVar];
    const isGlobal = info.scope === 'GLOBAL';
    fill('#7030a0'); textFont('monospace'); textSize(16);
    text(selectedVar, px, 40); textFont('sans-serif');
    fill(isGlobal ? [25,110,40] : [30,90,170]); textSize(14);
    text(info.scope + (isGlobal ? '' : ' - ' + (info.zone === 'scale' ? 'scale_color()' : info.zone === 'fill' ? 'fill_color()' : 'a function')), px, 64);
    fill(60); textSize(12); textWrap(WORD); text(info.expl, px, 88, pw);
  } else {
    fill(110); textSize(13); text('Click a variable to inspect its scope.', px, 44);
  }

  // nested scope diagram
  const dy = 150, dh = drawHeight - dy - 16;
  noStroke(); fill(245); stroke(120); rect(px, dy, pw, dh, 6);
  noStroke(); fill(80); textSize(11); textAlign(LEFT, TOP); text('Program (global scope)', px + 8, dy + 6);

  const innerW = (pw - 30) / 2, innerY = dy + 28, innerH = dh - 64;
  // fill_color box (blue), scale_color box (orange)
  const sel = selectedVar ? varInfo[selectedVar] : null;
  noStroke();
  fill(sel && (sel.zone === 'fill' || sel.zone === 'both') ? [200,225,255] : [225,235,250]); stroke(90,130,200);
  rect(px + 10, innerY, innerW, innerH, 5);
  fill(sel && (sel.zone === 'scale' || sel.zone === 'both') ? [255,225,195] : [250,235,220]); stroke(210,150,80);
  rect(px + 20 + innerW, innerY, innerW, innerH, 5);
  noStroke(); fill(40,80,150); textSize(10); text('fill_color', px + 16, innerY + 5);
  fill(160,90,30); text('scale_color', px + 26 + innerW, innerY + 5);

  // place selected var label in its box
  if (selectedVar) {
    fill(20); textFont('monospace'); textSize(13); textAlign(CENTER, CENTER);
    if (sel.scope === 'GLOBAL') text(selectedVar, px + pw / 2, dy + 18);
    else if (sel.zone === 'fill') text(selectedVar, px + 10 + innerW / 2, innerY + innerH / 2);
    else if (sel.zone === 'scale') text(selectedVar, px + 20 + innerW * 1.5, innerY + innerH / 2);
    else { text(selectedVar, px + 10 + innerW / 2, innerY + innerH / 2); text(selectedVar, px + 20 + innerW * 1.5, innerY + innerH / 2); }
    textFont('sans-serif'); textAlign(LEFT, TOP);
  }
}

function mousePressed() {
  textFont('monospace'); textSize(13);
  const cw = textWidth('m');
  textFont('sans-serif');
  const x0 = margin;
  for (const tk of tokens) {
    const x = x0 + tk.col * cw, y = codeTop + tk.line * lineH;
    if (mouseX > x - 1 && mouseX < x + tk.len * cw + 2 && mouseY > y - 1 && mouseY < y + 17) {
      selectedVar = tk.name; return;
    }
  }
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
