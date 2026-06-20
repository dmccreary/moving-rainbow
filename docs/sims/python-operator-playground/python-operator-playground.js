// Python Operator Playground - Moving Rainbow MicroSim
// Pick a category and operator, enter operands, and see the Python result
// plus a plain-English LED interpretation. Apply-level practice (L3).
// CANVAS_HEIGHT: 430
let canvasWidth = 760;
let drawHeight = 312;
let controlHeight = 118;
let canvasHeight = drawHeight + controlHeight;
let margin = 15;
let defaultTextSize = 16;

let tab = 'Math';
const mathOps  = ['+','-','*','/','//','%','**'];
const compOps  = ['==','!=','<','>','<=','>='];
const logicOps = ['and','or','not'];

let tabMath, tabComp, tabLogic, opSelect, leftInput, rightInput, leftBool, rightBool, revealButton;
let revealed = false;

const challenges = {
  Math:      {text:'A strip has 30 LEDs. A pixel is at position 47. Where does it appear? Try 47 % 30.', ans:'47 % 30 = 17'},
  Comparison:{text:'Red channel = 128, Blue channel = 255. Is red brighter? Try 128 > 255.', ans:'128 > 255 = False'},
  Logic:     {text:'Button A pressed (True), Button B not (False). Are BOTH pressed? Try True and False.', ans:'True and False = False'},
};

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));

  tabMath = createButton('Math');         tabMath.position(15, drawHeight + 8);  tabMath.mousePressed(() => setTab('Math'));
  tabComp = createButton('Comparison');   tabComp.position(75, drawHeight + 8);  tabComp.mousePressed(() => setTab('Comparison'));
  tabLogic = createButton('Logic');       tabLogic.position(185, drawHeight + 8); tabLogic.mousePressed(() => setTab('Logic'));

  leftInput = createInput('100', 'number');  leftInput.position(15, drawHeight + 46);  leftInput.size(70);
  rightInput = createInput('30', 'number');   rightInput.position(190, drawHeight + 46); rightInput.size(70);

  opSelect = createSelect(); opSelect.position(110, drawHeight + 46);

  leftBool = createSelect(); leftBool.position(15, drawHeight + 46);  leftBool.option('True'); leftBool.option('False');
  rightBool = createSelect(); rightBool.position(190, drawHeight + 46); rightBool.option('True'); rightBool.option('False');

  revealButton = createButton('Reveal Challenge Answer');
  revealButton.position(15, drawHeight + 84);
  revealButton.mousePressed(() => revealed = !revealed);

  setTab('Math');
  describe('A calculator where students apply Python math, comparison, and logic ' +
    'operators to LED-themed values and read the result interpretation.', LABEL);
}

function setTab(t) {
  tab = t; revealed = false;
  const ops = (t === 'Math') ? mathOps : (t === 'Comparison') ? compOps : logicOps;
  opSelect.elt.innerHTML = '';
  for (const o of ops) opSelect.option(o);
  const logic = (t === 'Logic');
  leftInput.elt.style.display = logic ? 'none' : '';
  rightInput.elt.style.display = logic ? 'none' : '';
  leftBool.elt.style.display = logic ? '' : 'none';
  rightBool.elt.style.display = logic ? '' : 'none';
}

function compute() {
  const op = opSelect.value();
  if (tab === 'Logic') {
    const a = leftBool.value() === 'True';
    const b = rightBool.value() === 'True';
    if (op === 'not') return {expr:'not ' + a, val: !a};
    const val = (op === 'and') ? (a && b) : (a || b);
    return {expr: a + ' ' + op + ' ' + b, val};
  }
  const a = parseFloat(leftInput.value()) || 0;
  const b = parseFloat(rightInput.value()) || 0;
  let val;
  if (tab === 'Math') {
    switch (op) {
      case '+': val = a + b; break;
      case '-': val = a - b; break;
      case '*': val = a * b; break;
      case '/': val = b !== 0 ? +(a / b).toFixed(3) : 'undefined (÷0)'; break;
      case '//': val = b !== 0 ? Math.floor(a / b) : 'undefined (÷0)'; break;
      case '%': val = b !== 0 ? ((a % b) + b) % b : 'undefined (÷0)'; break;
      case '**': val = Math.pow(a, b); break;
    }
  } else {
    switch (op) {
      case '==': val = a === b; break;
      case '!=': val = a !== b; break;
      case '<': val = a < b; break;
      case '>': val = a > b; break;
      case '<=': val = a <= b; break;
      case '>=': val = a >= b; break;
    }
  }
  return {expr: a + ' ' + op + ' ' + b, val};
}

function ledNote(op, val) {
  if (op === '%') return 'On a strip, position % count wraps a pixel index back into range.';
  if (op === '//') return 'Integer division splits LEDs into equal groups with no remainder.';
  if (op === '**') return 'Powers scale brightness curves (gamma) quickly.';
  if (op === '>' || op === '<' || op === '>=' || op === '<=' || op === '==' || op === '!=')
    return (val === true) ? 'This comparison is True, so an if-statement would run its block.'
                          : 'This comparison is False, so an if-statement would skip its block.';
  if (op === 'and' || op === 'or' || op === 'not')
    return 'Logic combines button or sensor states to decide what the LEDs do.';
  return 'Math operators compute color channels, positions, and timing for LEDs.';
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill('aliceblue'); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  // highlight active tab
  for (const [b, name] of [[tabMath,'Math'],[tabComp,'Comparison'],[tabLogic,'Logic']])
    b.style('background-color', tab === name ? '#2b78e4' : '');
  for (const [b, name] of [[tabMath,'Math'],[tabComp,'Comparison'],[tabLogic,'Logic']])
    b.style('color', tab === name ? 'white' : '');

  noStroke(); fill('black'); textSize(18); textAlign(LEFT, TOP);
  text('Operator Playground - ' + tab, margin, 12);

  const r = compute();
  const op = opSelect.value();

  // operator badge
  fill(235); stroke(180); rect(canvasWidth/2 - 36, 50, 72, 56, 10);
  noStroke(); fill(40); textSize(34); textAlign(CENTER, CENTER);
  text(op, canvasWidth/2, 78);

  // expression + result
  noStroke(); textAlign(CENTER, TOP);
  fill(60); textSize(18); text(r.expr + ' =', canvasWidth/2, 120);
  const isBool = (typeof r.val === 'boolean');
  fill(isBool ? (r.val ? 'green' : 'red') : '#2b78e4');
  textSize(44); text(String(r.val), canvasWidth/2, 146);

  // LED interpretation
  noStroke(); fill(252, 248, 227); stroke(220, 200, 120);
  rect(margin, 206, canvasWidth - 2*margin, 44, 8);
  noStroke(); fill(120, 90, 10); textSize(13); textAlign(LEFT, CENTER); textWrap(WORD);
  text('LED interpretation: ' + ledNote(op, r.val), margin + 10, 228, canvasWidth - 2*margin - 20);

  // challenge
  fill(235, 240, 252); stroke(150, 180, 230);
  rect(margin, 256, canvasWidth - 2*margin, 48, 8);
  noStroke(); fill(20, 60, 130); textSize(13); textAlign(LEFT, TOP); textWrap(WORD);
  const ch = challenges[tab];
  text('Challenge: ' + ch.text + (revealed ? '   Answer: ' + ch.ans : ''),
       margin + 10, 263, canvasWidth - 2*margin - 20);

  // control labels
  noStroke(); fill('black'); textSize(12); textAlign(LEFT, CENTER);
  text(tab === 'Logic' ? 'A' : 'left', 15, drawHeight + 40);
  text('op', 110, drawHeight + 40);
  text(tab === 'Logic' ? 'B' : 'right', 190, drawHeight + 40);
  textSize(defaultTextSize);
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
