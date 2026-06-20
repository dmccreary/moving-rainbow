// For Loop List Iteration - Moving Rainbow MicroSim
// A loop cursor steps through a list of three colors, one per click, showing
// that the for loop gives the loop variable a new value each time. (Remember)
// CANVAS_HEIGHT: 280
let canvasWidth = 600;
let drawHeight = 230;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let margin = 15;
let defaultTextSize = 16;

let nextButton, resetButton;
let idx = 0;
const colors = [[255, 0, 0], [0, 255, 0], [0, 0, 255]];
const labels = ['(255, 0, 0)', '(0, 255, 0)', '(0, 0, 255)'];

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));

  nextButton = createButton('Next Step');
  nextButton.position(10, drawHeight + 12);
  nextButton.mousePressed(() => { if (idx < colors.length - 1) idx++; });

  resetButton = createButton('Reset');
  resetButton.position(100, drawHeight + 12);
  resetButton.mousePressed(() => idx = 0);

  describe('Three colored boxes representing a list; a loop cursor highlights each ' +
    'box in turn and shows the loop variable value and iteration number.', LABEL);
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill('aliceblue'); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  noStroke(); fill('black'); textSize(18); textAlign(CENTER, TOP);
  text('for color in colors:', canvasWidth / 2, 14);

  const n = colors.length;
  const boxW = Math.min(120, (canvasWidth - 2 * margin) / n - 16);
  const gap = 24;
  const totalW = n * boxW + (n - 1) * gap;
  const startX = (canvasWidth - totalW) / 2;
  const boxY = 54, boxH = 58;

  for (let i = 0; i < n; i++) {
    const x = startX + i * (boxW + gap);
    // cursor arrow above current box
    if (i === idx) {
      fill('black'); noStroke();
      triangle(x + boxW / 2 - 10, boxY - 24, x + boxW / 2 + 10, boxY - 24, x + boxW / 2, boxY - 8);
    }
    fill(colors[i][0], colors[i][1], colors[i][2]);
    stroke(i === idx ? 'black' : 'silver'); strokeWeight(i === idx ? 4 : 1);
    rect(x, boxY, boxW, boxH, 8);
    noStroke();
    fill(255); textSize(11); textAlign(CENTER, TOP);
    text('index ' + i, x + boxW / 2, boxY + 6);
    fill(40); textSize(13); textAlign(CENTER, TOP);
    text(labels[i], x + boxW / 2, boxY + boxH + 8);
  }

  // status
  noStroke(); fill('black'); textSize(16); textAlign(CENTER, TOP);
  text('Iteration ' + (idx + 1) + ' of ' + n + '   ->   color = ' + labels[idx], canvasWidth / 2, 158);

  fill(70); textSize(13);
  text('The for loop gives color a new value each time.', canvasWidth / 2, 196);

  noStroke(); fill('black'); textSize(13); textAlign(LEFT, CENTER);
  text('Step ' + (idx + 1) + ' / ' + n, 170, drawHeight + 25);
  textSize(defaultTextSize);
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
