// Ohm's Law Calculator - Moving Rainbow MicroSim
// Pick which value to solve for, enter the other two, and read the worked
// formula plus the power it uses. (Apply Ohm's Law for any unknown.)
// CANVAS_HEIGHT: 360
let canvasWidth = 700;
let drawHeight = 290;
let controlHeight = 70;
let canvasHeight = drawHeight + controlHeight;
let margin = 15;
let defaultTextSize = 16;

let solveSelect, inputA, inputB;
let highlight = '';

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));

  solveSelect = createSelect();
  solveSelect.position(120, drawHeight + 12);
  solveSelect.option('I (current)');
  solveSelect.option('V (voltage)');
  solveSelect.option('R (resistance)');
  solveSelect.changed(relabel);

  inputA = createInput('5', 'number');  inputA.position(120, drawHeight + 44); inputA.size(70);
  inputB = createInput('220', 'number'); inputB.position(300, drawHeight + 44); inputB.size(70);

  describe('An Ohm\'s Law triangle (V, I, R) where the student picks the unknown, ' +
    'enters two values, and sees the worked formula and the power used.', LABEL);
}

function relabel() { /* defaults kept; labels drawn in draw() */ }

function solved() {
  const mode = solveSelect.value();
  const a = parseFloat(inputA.value()) || 0;
  const b = parseFloat(inputB.value()) || 0;
  let V, I, R, formula;
  if (mode.startsWith('I')) {        // a=V, b=R
    V = a; R = b; I = R !== 0 ? V / R : 0;
    formula = 'I = V / R = ' + V + ' / ' + R + ' = ' + I.toFixed(4) + ' A = ' + Math.round(I * 1000) + ' mA';
  } else if (mode.startsWith('V')) { // a=I, b=R
    I = a; R = b; V = I * R;
    formula = 'V = I * R = ' + I + ' * ' + R + ' = ' + V.toFixed(2) + ' V';
  } else {                            // a=V, b=I
    V = a; I = b; R = I !== 0 ? V / I : 0;
    formula = 'R = V / I = ' + V + ' / ' + I + ' = ' + R.toFixed(1) + ' ohms';
  }
  const P = V * I;
  return { V, I, R, formula, power: 'P = V * I = ' + V.toFixed(2) + ' * ' + I.toFixed(4) + ' = ' + P.toFixed(3) + ' W' };
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill('aliceblue'); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  const s = solved();
  noStroke(); fill('black'); textSize(18); textAlign(LEFT, TOP);
  text("Ohm's Law Calculator", margin, 12);

  // triangle
  const tx = 120, ty = 60, tw = 180, th = 150;
  stroke(90); strokeWeight(2); noFill();
  triangle(tx + tw / 2, ty, tx, ty + th, tx + tw, ty + th);
  stroke(150); line(tx + 18, ty + th / 2, tx + tw - 18, ty + th / 2);  // V over (I R)
  // circles
  drawNode('V', tx + tw / 2, ty + th * 0.28, s.V.toFixed(1), solveSelect.value().startsWith('V'));
  drawNode('I', tx + tw * 0.30, ty + th * 0.72, (s.I * 1000).toFixed(0) + 'mA', solveSelect.value().startsWith('I'));
  drawNode('R', tx + tw * 0.70, ty + th * 0.72, s.R.toFixed(0) + 'Ω', solveSelect.value().startsWith('R'));

  // formulas
  const fx = 340, fw = canvasWidth - fx - margin;
  noStroke(); fill(235, 240, 252); stroke(150, 180, 230); rect(fx, 70, fw, 56, 8);
  noStroke(); fill(20, 60, 130); textFont('monospace'); textSize(15); textAlign(LEFT, CENTER); textWrap(WORD);
  text(s.formula, fx + 12, 98, fw - 24);
  noStroke(); fill(252, 248, 227); stroke(220, 200, 120); rect(fx, 140, fw, 56, 8);
  noStroke(); fill(120, 90, 10);
  text(s.power, fx + 12, 168, fw - 24);
  textFont('sans-serif');

  noStroke(); fill(90); textSize(12); textAlign(LEFT, TOP);
  text('V = volts,  I = amps,  R = ohms.  23 mA is a typical NeoPixel-driver current.', margin, drawHeight - 22);

  // control labels
  noStroke(); fill('black'); textSize(13); textAlign(LEFT, CENTER);
  text('Solve for:', 15, drawHeight + 22);
  const mode = solveSelect.value();
  text(mode.startsWith('I') ? 'V (volts):' : mode.startsWith('V') ? 'I (amps):' : 'V (volts):', 15, drawHeight + 54);
  text(mode.startsWith('R') ? 'I (amps):' : 'R (ohms):', 210, drawHeight + 54);
  textSize(defaultTextSize);
}

function drawNode(label, x, y, val, active) {
  noStroke(); fill(active ? color(255, 210, 90) : color(255)); stroke(active ? 'darkorange' : 'silver'); strokeWeight(2);
  circle(x, y, 52);
  noStroke(); fill('black'); textSize(18); textAlign(CENTER, CENTER); text(label, x, y - 6);
  fill(60); textSize(11); text(val, x, y + 12);
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
