// Transistor Circuit Diagrams - Moving Rainbow MicroSim
// Tab 1: a transistor switch you turn on/off. Tab 2: the same circuit driven
// by PWM duty cycle. Click parts for notes. (Apply: trace current, predict LED.)
// CANVAS_HEIGHT: 400
let canvasWidth = 700;
let drawHeight = 350;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let margin = 15;
let defaultTextSize = 16;

let tab = 'switch';
let tabSwitch, tabPwm, gpioButton, dutySlider;
let gpioHigh = false;
let selected = '';
let hotspots = [];

const notes = {
  r1: '1 kΩ resistor: limits the base current to about 2 mA - just enough to switch the transistor.',
  r2: '220 Ω resistor: limits the LED current to about 14 mA so the LED is bright but safe.',
  q: '2N2222 NPN transistor: a small Base current lets a larger current flow from Collector to Emitter.',
  led: 'LED: lights up when the transistor is on and current can flow to ground.',
};

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));

  tabSwitch = createButton('Transistor Switch');
  tabSwitch.position(15, drawHeight + 12);
  tabSwitch.mousePressed(() => { tab = 'switch'; selected = ''; });

  tabPwm = createButton('PWM Dimmer');
  tabPwm.position(155, drawHeight + 12);
  tabPwm.mousePressed(() => { tab = 'pwm'; selected = ''; });

  gpioButton = createButton('GP0: LOW');
  gpioButton.position(300, drawHeight + 12);
  gpioButton.mousePressed(() => { gpioHigh = !gpioHigh; gpioButton.html('GP0: ' + (gpioHigh ? 'HIGH' : 'LOW')); });

  dutySlider = createSlider(0, 100, 50, 1);
  dutySlider.position(360, drawHeight + 15);
  dutySlider.size(150);

  describe('A transistor driver schematic. In switch mode a GP0 toggle turns the ' +
    'LED on or off; in PWM mode a duty-cycle slider dims it.', LABEL);
}

function ledFactor() {
  if (tab === 'switch') return gpioHigh ? 1 : 0;
  return dutySlider.value() / 100;
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill('aliceblue'); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  // tab highlight
  tabSwitch.style('background-color', tab === 'switch' ? '#2b78e4' : '');
  tabSwitch.style('color', tab === 'switch' ? 'white' : '');
  tabPwm.style('background-color', tab === 'pwm' ? '#2b78e4' : '');
  tabPwm.style('color', tab === 'pwm' ? 'white' : '');
  gpioButton.style('display', tab === 'switch' ? '' : 'none');
  dutySlider.style('display', tab === 'pwm' ? '' : 'none');

  const f = ledFactor();
  const on = f > 0.01;

  noStroke(); fill('black'); textSize(17); textAlign(LEFT, TOP);
  text(tab === 'switch' ? 'Transistor Switch' : 'PWM Dimmer', margin, 12);

  // layout coordinates
  const railTop = 70, railBot = 310;
  const gp0x = 70, qx = 360, ledX = 360, topRailY = railTop;
  hotspots = [];

  stroke(on ? color(60, 200, 90) : color(120)); strokeWeight(on ? 4 : 2);
  // +5V rail
  stroke(180, 60, 60); strokeWeight(3); line(ledX - 120, topRailY, ledX + 120, topRailY);
  noStroke(); fill(180, 60, 60); textSize(13); textAlign(LEFT, CENTER); text('+5V', ledX + 124, topRailY);

  // LED (triangle + bar) from +5V down
  const ledY = 120;
  stroke(on ? color(60, 200, 90) : 120); strokeWeight(on ? 4 : 2);
  line(ledX, topRailY, ledX, ledY - 14);
  noStroke();
  const lr = 200 * f + 40, lg = 60 * f + 30, lb = 30;
  fill(on ? color(255, 230, 120) : color(120)); if (on) for (let g = 3; g >= 1; g--) { fill(255, 230, 120, 50 * f); circle(ledX, ledY, 30 + g * 6); }
  fill(on ? color(255, 220, 90) : color(150)); stroke(80); strokeWeight(1);
  triangle(ledX - 10, ledY - 10, ledX + 10, ledY - 10, ledX, ledY + 8); rect(ledX - 11, ledY + 8, 22, 3);
  hotspots.push({ x: ledX - 14, y: ledY - 14, w: 28, h: 30, key: 'led' });

  // 220 ohm resistor below LED to collector
  const r2y = ledY + 40;
  stroke(on ? color(60, 200, 90) : 120); strokeWeight(on ? 4 : 2); line(ledX, ledY + 12, ledX, r2y - 12);
  noStroke(); fill(225, 200, 120); stroke(150); rect(ledX - 16, r2y - 12, 32, 24, 3);
  noStroke(); fill(40); textSize(11); textAlign(LEFT, CENTER); text('220Ω', ledX + 22, r2y);
  hotspots.push({ x: ledX - 16, y: r2y - 12, w: 32, h: 24, key: 'r2' });

  // transistor body
  const qy = 220;
  stroke(on ? color(60, 200, 90) : 120); strokeWeight(on ? 4 : 2); line(ledX, r2y + 12, qx, qy - 26);
  noStroke(); fill(60); circle(qx, qy, 46);
  noStroke(); fill(230); textSize(10); textAlign(CENTER, CENTER); text('Q', qx, qy);
  fill(40); textAlign(LEFT, CENTER); text('C', qx + 6, qy - 22); text('E', qx + 6, qy + 22); text('B', qx - 30, qy);
  hotspots.push({ x: qx - 23, y: qy - 23, w: 46, h: 46, key: 'q' });

  // base resistor 1k from GP0
  stroke(on ? color(230, 200, 60) : 120); strokeWeight(on ? 4 : 2); line(gp0x + 40, qy, qx - 23, qy);
  noStroke(); fill(225, 200, 120); stroke(150); rect(gp0x + 70, qy - 12, 32, 24, 3);
  noStroke(); fill(40); textSize(11); textAlign(CENTER, BOTTOM); text('1kΩ', gp0x + 86, qy - 14);
  hotspots.push({ x: gp0x + 70, y: qy - 12, w: 32, h: 24, key: 'r1' });
  // GP0 node
  noStroke(); fill(on && tab === 'switch' ? color(60, 200, 90) : (on ? color(230, 200, 60) : color(150)));
  rect(gp0x - 10, qy - 12, 46, 24, 4);
  fill('white'); textSize(11); textAlign(CENTER, CENTER); text('GP0', gp0x + 13, qy);

  // emitter to GND
  stroke(on ? color(60, 200, 90) : 120); strokeWeight(on ? 4 : 2); line(qx, qy + 23, qx, railBot);
  stroke(40); strokeWeight(3); line(qx - 40, railBot, qx + 40, railBot);
  line(qx - 26, railBot + 8, qx + 26, railBot + 8); line(qx - 12, railBot + 16, qx + 12, railBot + 16);
  noStroke(); fill(40); textSize(12); textAlign(LEFT, CENTER); text('GND', qx + 46, railBot + 4);

  // status
  noStroke(); fill(on ? color(20, 130, 50) : color(140)); textSize(14); textAlign(RIGHT, TOP);
  text(tab === 'switch' ? (on ? 'GP0 HIGH -> LED ON' : 'GP0 LOW -> LED OFF')
                        : ('Duty ' + dutySlider.value() + '% -> brightness ' + Math.round(f * 100) + '%'),
       canvasWidth - margin, 16);

  drawCard();

  noStroke(); fill('black'); textSize(12); textAlign(LEFT, CENTER);
  text(tab === 'switch' ? 'Toggle GP0 to switch the LED. Click a part for details.'
                        : 'Drag the duty cycle to dim the LED. Click a part for details.',
       tab === 'switch' ? 410 : 520, drawHeight + 25);
  textSize(defaultTextSize);
}

function drawCard() {
  if (!selected) return;
  const cw = 250, cx0 = margin, cy = 250;
  noStroke(); fill(255, 255, 255, 240); stroke(120); rect(cx0, cy, cw, 80, 8);
  noStroke(); fill(20); textSize(12); textAlign(LEFT, TOP); textWrap(WORD);
  text(notes[selected], cx0 + 10, cy + 10, cw - 20);
}

function mousePressed() {
  for (const h of hotspots) {
    if (mouseX > h.x && mouseX < h.x + h.w && mouseY > h.y && mouseY < h.y + h.h) { selected = h.key; return; }
  }
  selected = '';
}

function windowResized() { updateCanvasSize(); resizeCanvas(canvasWidth, canvasHeight); }
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
