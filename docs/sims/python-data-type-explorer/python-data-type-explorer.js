// Python Data Type Explorer - Moving Rainbow MicroSim
// See a Python value, predict its type, then reveal the answer with an LED
// example. Prediction-before-reveal supports retention at the Understand level.
// CANVAS_HEIGHT: 420
let canvasWidth = 760;
let drawHeight = 296;
let controlHeight = 124;
let canvasHeight = drawHeight + controlHeight;
let margin = 15;
let defaultTextSize = 16;

const TYPES = ['Integer','Float','String','Boolean','List','Tuple','None'];
const typeColors = {
  Integer:[80,150,235], Float:[0,180,200], String:[40,170,90], Boolean:[225,190,40],
  List:[232,144,58], Tuple:[140,70,200], None:[140,140,140]
};

const values = [
  {v:'42',              t:'Integer', why:'42 is a whole number with no decimal point.', led:'strip[0] = (255, 0, 0) - 255 is an integer color value.'},
  {v:'3.14',            t:'Float',   why:'3.14 has a decimal point, so it is a float.', led:'factor = 0.5 dims a color - floats allow fractions.'},
  {v:'"hello"',         t:'String',  why:'Text inside quotes is a string.',             led:'name = "Moving Rainbow" labels your project.'},
  {v:'True',            t:'Boolean', why:'True and False values are booleans.',         led:'is_on = True decides whether the strip lights up.'},
  {v:'[255, 0, 0]',     t:'List',    why:'Square brackets make a list - it can change.',led:'colors = [255, 0, 0] can be edited later.'},
  {v:'(128, 0, 200)',   t:'Tuple',   why:'Parentheses make a tuple - it cannot change.',led:'purple = (128, 0, 200) is a fixed RGB color.'},
  {v:'None',            t:'None',    why:'None means "no value yet".',                  led:'last_color = None before any pixel is set.'},
  {v:'0',               t:'Integer', why:'0 is a whole number.',                        led:'strip[0] is the first pixel - index 0.'},
  {v:'0.5',             t:'Float',   why:'0.5 has a decimal point.',                    led:'factor = 0.5 sets half brightness.'},
  {v:'"Moving Rainbow"',t:'String',  why:'Text in quotes is a string.',                 led:'title = "Moving Rainbow"'},
  {v:'False',           t:'Boolean', why:'False is a boolean.',                         led:'button_pressed = False until you press it.'},
  {v:'[1, 2, 3, 4, 5]', t:'List',    why:'Square brackets, changeable - a list.',       led:'pixels = [1, 2, 3, 4, 5] lists pixel indexes.'},
  {v:'(255, 255, 255)', t:'Tuple',   why:'Parentheses, fixed - a tuple.',               led:'white = (255, 255, 255) is full brightness.'},
  {v:'255',             t:'Integer', why:'255 is a whole number (the max color value).',led:'(255, 0, 0) - 255 is full red.'},
  {v:'""',              t:'String',  why:'Empty quotes are still a string.',            led:'message = "" starts with no text.'},
];

let order = [];
let pos = 0;            // position in order
let answered = false;
let selectedType = null;

let typeButtons = [], nextButton, shuffleButton;

function current() { return values[order[pos]]; }

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));
  order = values.map((_, i) => i);

  // 7 type buttons across two rows (4 + 3)
  for (let i = 0; i < TYPES.length; i++) {
    const b = createButton(TYPES[i]);
    const row = i < 4 ? 0 : 1;
    const col = i < 4 ? i : i - 4;
    b.position(15 + col * 95, drawHeight + 8 + row * 36);
    b.mousePressed(() => answer(TYPES[i]));
    typeButtons.push(b);
  }
  nextButton = createButton('Next Value');
  nextButton.position(15, drawHeight + 84);
  nextButton.mousePressed(next);

  shuffleButton = createButton('Shuffle');
  shuffleButton.position(120, drawHeight + 84);
  shuffleButton.mousePressed(shuffle);

  describe('A flashcard that shows a Python value; the student selects its data ' +
    'type and gets feedback with an LED programming example.', LABEL);
}

function answer(t) {
  if (answered) return;
  selectedType = t;
  answered = true;
  const correct = current().t;
  for (const b of typeButtons) {
    const lbl = b.html();
    if (lbl === correct) b.style('background-color', 'lightgreen');
    else if (lbl === t) b.style('background-color', '#ffc107');
  }
}

function clearButtonStyles() {
  for (const b of typeButtons) b.style('background-color', '');
}

function next() { pos = (pos + 1) % order.length; answered = false; selectedType = null; clearButtonStyles(); }
function shuffle() {
  for (let i = order.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [order[i], order[j]] = [order[j], order[i]]; }
  pos = 0; answered = false; selectedType = null; clearButtonStyles();
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill('aliceblue'); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  const cur = current();

  // progress
  noStroke(); fill('black'); textSize(13); textAlign(CENTER, TOP);
  text('Question ' + (pos + 1) + ' of ' + order.length, canvasWidth / 2, 12);

  // value card
  const cardW = Math.min(canvasWidth - 2 * margin, 360);
  const cardX = (canvasWidth - cardW) / 2, cardY = 36, cardH = 86;
  fill(30);
  if (answered) { stroke(typeColors[cur.t]); strokeWeight(4); } else { noStroke(); }
  rect(cardX, cardY, cardW, cardH, 12);
  noStroke(); fill(245); textFont('monospace'); textSize(30); textAlign(CENTER, CENTER);
  text(cur.v, canvasWidth / 2, cardY + cardH / 2);
  textFont('sans-serif');

  // feedback
  if (answered) {
    const correct = (selectedType === cur.t);
    const fy = 140, fh = 120;
    fill(correct ? [223,245,225] : [255,243,205]); stroke(correct ? [120,190,120] : [220,180,60]);
    rect(margin, fy, canvasWidth - 2 * margin, fh, 8);
    noStroke();
    fill(correct ? [25,110,40] : [150,100,10]);
    textSize(16); textAlign(LEFT, TOP);
    text(correct ? 'Correct! That is a ' + cur.t + '.' : 'Not quite - it is a ' + cur.t + '.', margin + 12, fy + 10);
    fill(40); textSize(13); textWrap(WORD);
    text('Why: ' + cur.why, margin + 12, fy + 38, canvasWidth - 2 * margin - 24);
    fill(20);
    text('LED example: ' + cur.led, margin + 12, fy + 76, canvasWidth - 2 * margin - 24);
  } else {
    noStroke(); fill(90); textSize(15); textAlign(CENTER, TOP);
    text('What type is this value? Pick a button below.', canvasWidth / 2, 150);
  }
  textSize(defaultTextSize); textAlign(LEFT, CENTER);
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
