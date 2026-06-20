// DRY Principle: Before & After - Moving Rainbow MicroSim
// Compare repeated code (Before DRY) with a refactor that uses a function
// (After DRY). Click a block to match it to its function call. Analyze (L4).
// CANVAS_HEIGHT: 470
let canvasWidth = 760;
let drawHeight = 420;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let margin = 12;
let defaultTextSize = 16;

let countButton, diffButton, bugButton;
let showCounts = false, showDiff = false, bugMode = false;
let hiBlock = -1, hiAllLeft = false, hiCall = -1;
let fixedCount = 0;

// Left "Before DRY": three 5-line blocks. Blocks 0 and 1 carry the bug
// (strip.write missing its parentheses).
const colorsTxt = ['(255, 0, 0)', '(0, 255, 0)', '(0, 0, 255)'];
const colorNames = ['red', 'green', 'blue'];
let leftLines = [];
function buildLeft() {
  leftLines = [];
  for (let b = 0; b < 3; b++) {
    leftLines.push({t:'# Turn all pixels ' + colorNames[b], block:b});
    leftLines.push({t:'for i in range(NUMBER_PIXELS):', block:b});
    leftLines.push({t:'    strip[i] = ' + colorsTxt[b], block:b});
    leftLines.push({t:'strip.write()', block:b, write:true, buggy:(b < 2), fixed:false});
    leftLines.push({t:'utime.sleep(0.5)', block:b});
  }
}
const rightLines = [
  {t:'def fill_color(strip, color):', kind:'func'},
  {t:'    for i in range(len(strip)):', kind:'func'},
  {t:'        strip[i] = color', kind:'func'},
  {t:'    strip.write()', kind:'func'},
  {t:'    utime.sleep(0.5)', kind:'func'},
  {t:'', kind:'blank'},
  {t:'fill_color(strip, (255, 0, 0))   # Red', kind:'call', call:0},
  {t:'fill_color(strip, (0, 255, 0))   # Green', kind:'call', call:1},
  {t:'fill_color(strip, (0, 0, 255))   # Blue', kind:'call', call:2},
];

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));
  buildLeft();

  countButton = createButton('Count Lines');
  countButton.position(10, drawHeight + 12);
  countButton.mousePressed(() => showCounts = !showCounts);

  diffButton = createButton("What's Different?");
  diffButton.position(110, drawHeight + 12);
  diffButton.mousePressed(() => showDiff = !showDiff);

  bugButton = createButton('Find the Bug');
  bugButton.position(240, drawHeight + 12);
  bugButton.mousePressed(() => { bugMode = !bugMode; });

  describe('Two code panels: repeated "Before DRY" code on the left and a ' +
    'refactored function-based "After DRY" version on the right, with click-to-match highlighting.', LABEL);
}

const lineH = 17, codeTop = 52, codeBoxTop = 44;
function leftY(i) { return codeTop + i * lineH; }
function rightY(i) { return codeTop + i * lineH; }

function draw() {
  updateCanvasSize();
  const gap = canvasWidth * 0.04;
  const panelW = (canvasWidth - 2 * margin - gap) / 2;
  const leftX = margin, rightX = margin + panelW + gap;

  noStroke();
  fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);
  fill('aliceblue'); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);

  // panel headers
  noStroke(); fill('black'); textSize(15); textAlign(LEFT, TOP);
  text('Before DRY' + (showCounts ? '  (15 lines)' : ''), leftX + 4, 14);
  text('After DRY' + (showCounts ? '  (9 lines)' : ''), rightX + 4, 14);

  // panel backgrounds
  fill(40); noStroke(); rect(leftX, codeBoxTop, panelW, 15 * lineH + 14, 6);
  rect(rightX, codeBoxTop, panelW, rightLines.length * lineH + 14, 6);

  // left code
  textFont('monospace'); textSize(12); textAlign(LEFT, TOP);
  for (let i = 0; i < leftLines.length; i++) {
    const ln = leftLines[i], y = leftY(i);
    const lit = hiAllLeft || hiBlock === ln.block;
    if (lit) { noStroke(); fill(232, 144, 58, 70); rect(leftX + 2, y - 1, panelW - 4, lineH, 3); }
    const buggyNow = bugMode && ln.buggy && !ln.fixed;
    noStroke();
    fill(buggyNow ? 'tomato' : (ln.t.startsWith('#') ? 140 : 230));
    let shown = ln.t;
    if (ln.write && ln.buggy && !ln.fixed) shown = 'strip.write';   // missing ()
    text(shown, leftX + 6, y + 1);
  }

  // right code
  for (let i = 0; i < rightLines.length; i++) {
    const ln = rightLines[i], y = rightY(i);
    const lit = (ln.kind === 'call' && ln.call === hiCall) || (ln.kind === 'func' && hiAllLeft);
    if (lit) { noStroke(); fill(232, 144, 58, 70); rect(rightX + 2, y - 1, panelW - 4, lineH, 3); }
    noStroke();
    fill(ln.t.trim().startsWith('#') || ln.t.includes('#') ? 160 : (ln.kind === 'call' ? 130 : 230));
    text(ln.t, rightX + 6, y + 1);
  }
  textFont('sans-serif');

  // explanation / bug status
  const ey = codeBoxTop + 15 * lineH + 22;
  if (showDiff) {
    noStroke(); fill(255, 255, 255, 235); stroke(180);
    rect(margin, ey, canvasWidth - 2 * margin, 64, 8);
    noStroke(); fill(20); textSize(12); textAlign(LEFT, TOP); textWrap(WORD);
    text('The three blocks are identical except for the color value. Moving the shared code ' +
         'into fill_color() and making color a parameter cuts 15 lines to 9. A bug in the loop ' +
         'now lives in one place instead of three.', margin + 10, ey + 8, canvasWidth - 2 * margin - 20);
  }
  if (bugMode) {
    noStroke(); fill(20); textSize(13); textAlign(LEFT, TOP);
    const msg = (fixedCount >= 2)
      ? 'Fixed ' + fixedCount + ' / 2. With DRY, this bug would exist in ONE place - the function body.'
      : 'Find the Bug: click each "strip.write" missing its ()  -  fixed ' + fixedCount + ' / 2';
    text(msg, margin, drawHeight - 22);
  }

  noStroke(); fill('black'); textSize(12); textAlign(LEFT, CENTER);
  text('Click a left block to match its call; click the function body to match all.', 350, drawHeight + 25);
  textSize(defaultTextSize);
}

function mousePressed() {
  const gap = canvasWidth * 0.04;
  const panelW = (canvasWidth - 2 * margin - gap) / 2;
  const leftX = margin, rightX = margin + panelW + gap;

  // left lines
  if (mouseX > leftX && mouseX < leftX + panelW) {
    for (let i = 0; i < leftLines.length; i++) {
      const y = leftY(i);
      if (mouseY > y - 1 && mouseY < y + lineH) {
        const ln = leftLines[i];
        if (bugMode && ln.buggy && !ln.fixed) { ln.fixed = true; fixedCount++; return; }
        hiBlock = ln.block; hiAllLeft = false; hiCall = ln.block; return;
      }
    }
  }
  // right lines
  if (mouseX > rightX && mouseX < rightX + panelW) {
    for (let i = 0; i < rightLines.length; i++) {
      const y = rightY(i);
      if (mouseY > y - 1 && mouseY < y + lineH) {
        const ln = rightLines[i];
        if (ln.kind === 'func') { hiAllLeft = true; hiBlock = -1; hiCall = -1; }
        else if (ln.kind === 'call') { hiCall = ln.call; hiBlock = ln.call; hiAllLeft = false; }
        return;
      }
    }
  }
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
