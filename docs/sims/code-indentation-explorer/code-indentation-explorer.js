// Code Indentation Explorer - Moving Rainbow MicroSim
// Click a line to see which block it belongs to, then "Check Indentation"
// to color every line green (correct) or red (error).
// CANVAS_HEIGHT: 440
let canvasWidth = 760;
let drawHeight = 390;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let margin = 12;
let defaultTextSize = 16;

let checkButton, fixButton, nextButton;
let exampleIndex = 0;
let selectedLine = -1;
let checked = false;
let showFix = false;

// Each line: text shown, indent level (for the colored bar), ok flag, error note,
// and (for error lines) the corrected text.
const examples = [
  { name: 'Correct: a single if block', lines: [
    {t:'is_on = True',            lvl:0, ok:true,  err:''},
    {t:'if is_on:',               lvl:0, ok:true,  err:''},
    {t:'    print("LED is on")',  lvl:1, ok:true,  err:''},
    {t:'    print("Glowing!")',   lvl:1, ok:true,  err:''},
    {t:'print("Outside the if")', lvl:0, ok:true,  err:''},
  ]},
  { name: 'Error: missing indentation', lines: [
    {t:'brightness = 100',        lvl:0, ok:true,  err:''},
    {t:'if brightness > 50:',     lvl:0, ok:true,  err:''},
    {t:'print("Bright!")',        lvl:0, ok:false, err:'Should be indented 4 spaces - it belongs inside the if block.', fix:'    print("Bright!")'},
  ]},
  { name: 'Correct: nested blocks', lines: [
    {t:'for i in range(30):',         lvl:0, ok:true, err:''},
    {t:'    if i % 2 == 0:',          lvl:1, ok:true, err:''},
    {t:'        print("Even:", i)',   lvl:2, ok:true, err:''},
    {t:'    print("Pixel:", i)',      lvl:1, ok:true, err:''},
  ]},
  { name: 'Error: inconsistent indentation', lines: [
    {t:'for i in range(5):',          lvl:0, ok:true,  err:''},
    {t:'    print(i)',                lvl:1, ok:true,  err:''},
    {t:'      print("extra spaces")', lvl:2, ok:false, err:'6 spaces instead of 4 - indentation must be consistent.', fix:'    print("extra spaces")'},
  ]},
];

const lvlColors = [[255,255,255],[80,150,235],[232,144,58]];

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));

  checkButton = createButton('Check Indentation');
  checkButton.position(10, drawHeight + 12);
  checkButton.mousePressed(() => { checked = true; });

  fixButton = createButton('Show Fix');
  fixButton.position(150, drawHeight + 12);
  fixButton.mousePressed(() => { showFix = !showFix; });

  nextButton = createButton('Next Example');
  nextButton.position(245, drawHeight + 12);
  nextButton.mousePressed(() => {
    exampleIndex = (exampleIndex + 1) % examples.length;
    selectedLine = -1; checked = false; showFix = false;
  });

  describe('A Python code snippet on the left where students click lines to see ' +
    'block membership and check whether each line is correctly indented.', LABEL);
}

function draw() {
  updateCanvasSize();
  const splitX = Math.max(canvasWidth * 0.58, 320);

  noStroke();
  fill('white');  rect(0, drawHeight, canvasWidth, controlHeight);
  fill('aliceblue'); stroke('silver'); rect(0, 0, splitX, drawHeight);
  fill('white'); rect(splitX, 0, canvasWidth - splitX, drawHeight);

  drawCode(splitX);
  drawFeedback(splitX);

  noStroke();
  fill('black'); textSize(13); textAlign(LEFT, CENTER);
  text('Example ' + (exampleIndex + 1) + ' of ' + examples.length, 360, drawHeight + 25);
  textSize(defaultTextSize);
}

function lineGeom() {
  return { x0: margin + 34, y0: 56, h: 30 };
}

function drawCode(splitX) {
  const ex = examples[exampleIndex];
  noStroke();
  fill('black'); textSize(15); textAlign(LEFT, TOP);
  text(ex.name, margin, 14);

  // dark code background
  const g = lineGeom();
  const codeTop = g.y0 - 6;
  const codeH = ex.lines.length * g.h + 12;
  fill(40); stroke(70); rect(margin, codeTop, splitX - 2 * margin, codeH, 6);

  textFont('monospace');
  textSize(14);
  for (let i = 0; i < ex.lines.length; i++) {
    const ln = ex.lines[i];
    const y = g.y0 + i * g.h;
    // selection / verdict border
    if (selectedLine === i) { noFill(); stroke('yellow'); strokeWeight(2); rect(margin + 28, y - 2, splitX - 2 * margin - 32, g.h - 4, 4); }
    if (checked) {
      noFill(); stroke(ln.ok ? 'limegreen' : 'red'); strokeWeight(2);
      rect(margin + 28, y - 2, splitX - 2 * margin - 32, g.h - 4, 4);
    }
    // indentation-level bar
    const c = lvlColors[Math.min(ln.lvl, 2)];
    noStroke(); fill(c[0], c[1], c[2]); rect(margin + 26, y - 2, 4, g.h - 4);
    // line number
    fill(150); textAlign(RIGHT, TOP); text(i + 1, margin + 20, y + 3);
    // code text
    const shown = (showFix && ln.fix) ? ln.fix : ln.t;
    fill(showFix && ln.fix ? 'lightgreen' : 230);
    textAlign(LEFT, TOP); text(shown, margin + 34, y + 3);
  }
  textFont('sans-serif');
  textSize(defaultTextSize);
}

function drawFeedback(splitX) {
  const ex = examples[exampleIndex];
  const px = splitX + 12;
  noStroke();
  fill(20); textSize(15); textAlign(LEFT, TOP);
  text('Feedback', px, 16);
  textSize(13); fill(60);
  let y = 46;

  if (selectedLine >= 0) {
    const ln = ex.lines[selectedLine];
    fill(20); text('Line ' + (selectedLine + 1) + ':', px, y); y += 20;
    fill(60); textWrap(WORD);
    text('Indentation level ' + ln.lvl +
         (ln.lvl === 0 ? ' - module level (no indent).' :
          ln.lvl === 1 ? ' - one block deep (4 spaces).' :
                         ' - two blocks deep (8 spaces).'),
         px, y, canvasWidth - splitX - 24); y += 50;
  } else {
    fill(110); text('Click a code line to see its block membership.', px, y);
    y += 40;
  }

  if (checked) {
    fill(20); textSize(13); text('Check results:', px, y); y += 20;
    for (let i = 0; i < ex.lines.length; i++) {
      const ln = ex.lines[i];
      fill(ln.ok ? 'green' : 'red');
      textWrap(WORD);
      const msg = ln.ok ? 'Line ' + (i + 1) + ': correct'
                        : 'Line ' + (i + 1) + ': ' + ln.err;
      text(msg, px, y, canvasWidth - splitX - 24);
      y += ln.ok ? 18 : 38;
    }
  }
  textSize(defaultTextSize);
}

function mousePressed() {
  const ex = examples[exampleIndex];
  const g = lineGeom();
  const splitX = Math.max(canvasWidth * 0.58, 320);
  if (mouseX > margin && mouseX < splitX - margin) {
    for (let i = 0; i < ex.lines.length; i++) {
      const y = g.y0 + i * g.h;
      if (mouseY > y - 2 && mouseY < y + g.h - 2) { selectedLine = i; return; }
    }
  }
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
