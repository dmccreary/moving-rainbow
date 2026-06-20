// HSV Color Explorer - Moving Rainbow MicroSim
// Move the Hue, Saturation, and Value sliders to see how each changes the
// output color and where it sits on the color wheel. (Understand HSV.)
// CANVAS_HEIGHT: 390
let canvasWidth = 700;
let drawHeight = 260;
let controlHeight = 130;
let canvasHeight = drawHeight + controlHeight;
let margin = 15;
let defaultTextSize = 16;
let sliderLeftMargin = 150;

let hSlider, sSlider, vSlider;
let wheelGfx;
const WHEEL_D = 180;

function hsvToRgb(h, s, v) {
  let c = v * s, x = c * (1 - Math.abs(((h / 60) % 2) - 1)), m = v - c;
  let r = 0, g = 0, b = 0;
  if (h < 60) { r = c; g = x; } else if (h < 120) { r = x; g = c; }
  else if (h < 180) { g = c; b = x; } else if (h < 240) { g = x; b = c; }
  else if (h < 300) { r = x; b = c; } else { r = c; b = x; }
  return [Math.round((r + m) * 255), Math.round((g + m) * 255), Math.round((b + m) * 255)];
}

function buildWheel() {
  wheelGfx = createGraphics(WHEEL_D, WHEEL_D);
  // Force 1:1 pixel density so the direct pixels[] indexing below is correct
  // on Retina/HiDPI displays (otherwise the buffer is 2x and the wheel renders
  // as two squished copies).
  wheelGfx.pixelDensity(1);
  wheelGfx.loadPixels();
  const R = WHEEL_D / 2;
  for (let y = 0; y < WHEEL_D; y++) {
    for (let x = 0; x < WHEEL_D; x++) {
      const dx = x - R, dy = y - R, r = Math.sqrt(dx * dx + dy * dy);
      const idx = 4 * (y * WHEEL_D + x);
      if (r <= R) {
        let ang = Math.atan2(dy, dx) * 180 / Math.PI; if (ang < 0) ang += 360;
        const rgb = hsvToRgb(ang, r / R, 1);
        wheelGfx.pixels[idx] = rgb[0]; wheelGfx.pixels[idx + 1] = rgb[1];
        wheelGfx.pixels[idx + 2] = rgb[2]; wheelGfx.pixels[idx + 3] = 255;
      } else {
        wheelGfx.pixels[idx + 3] = 0;
      }
    }
  }
  wheelGfx.updatePixels();
}

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));
  buildWheel();

  hSlider = createSlider(0, 360, 180, 1);
  hSlider.position(sliderLeftMargin, drawHeight + 15);
  hSlider.size(canvasWidth - sliderLeftMargin - margin);

  sSlider = createSlider(0, 1, 1, 0.01);
  sSlider.position(sliderLeftMargin, drawHeight + 50);
  sSlider.size(canvasWidth - sliderLeftMargin - margin);

  vSlider = createSlider(0, 1, 1, 0.01);
  vSlider.position(sliderLeftMargin, drawHeight + 85);
  vSlider.size(canvasWidth - sliderLeftMargin - margin);

  describe('A color explorer with hue, saturation, and value sliders, a large color ' +
    'swatch, the RGB tuple, and a color wheel with a dot tracking the current color.', LABEL);
}

function draw() {
  updateCanvasSize();
  noStroke();
  fill('aliceblue'); stroke('silver'); rect(0, 0, canvasWidth, drawHeight);
  noStroke(); fill('white'); rect(0, drawHeight, canvasWidth, controlHeight);

  const H = hSlider.value(), S = sSlider.value(), V = vSlider.value();
  const rgb = hsvToRgb(H, S, V);

  noStroke(); fill('black'); textSize(18); textAlign(LEFT, TOP);
  text('HSV Color Explorer', margin, 12);

  // big color swatch
  const swX = margin + 20, swY = 48, swR = 74;
  stroke(180); strokeWeight(1); fill(rgb[0], rgb[1], rgb[2]); circle(swX + swR, swY + swR, swR * 2);
  noStroke(); fill('black'); textSize(15); textAlign(LEFT, TOP);
  text('RGB: (' + rgb[0] + ', ' + rgb[1] + ', ' + rgb[2] + ')', swX, swY + swR * 2 + 6);
  textSize(12); fill(80);
  text('HSV: (' + H + ', ' + S.toFixed(2) + ', ' + V.toFixed(2) + ')', swX, swY + swR * 2 + 28);

  // color wheel (anchored to the right edge, vertically centered with the swatch)
  const R = WHEEL_D / 2;
  const wx = canvasWidth - WHEEL_D - 60, wy = 36;
  const cx = wx + R, cy = wy + R;
  image(wheelGfx, wx, wy);
  // value dimming overlay
  noStroke(); fill(0, (1 - V) * 255); circle(cx, cy, WHEEL_D);
  // dot
  const ang = H * Math.PI / 180, rr = S * R;
  const dotX = cx + Math.cos(ang) * rr, dotY = cy + Math.sin(ang) * rr;
  stroke('white'); strokeWeight(2); fill(rgb[0], rgb[1], rgb[2]); circle(dotX, dotY, 16);
  noStroke(); fill(70); textSize(11); textAlign(CENTER, TOP); text('color wheel (angle = hue, radius = saturation)', cx, wy + WHEEL_D + 4);

  // slider labels
  noStroke(); fill('black'); textSize(14); textAlign(LEFT, CENTER);
  text('Hue (H): ' + H, 12, drawHeight + 22);
  text('Saturation (S): ' + S.toFixed(2), 12, drawHeight + 57);
  text('Value (V): ' + V.toFixed(2), 12, drawHeight + 92);
  textSize(defaultTextSize);
}

function windowResized() {
  updateCanvasSize();
  resizeCanvas(canvasWidth, canvasHeight);
  hSlider.size(canvasWidth - sliderLeftMargin - margin);
  sSlider.size(canvasWidth - sliderLeftMargin - margin);
  vSlider.size(canvasWidth - sliderLeftMargin - margin);
}
function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) canvasWidth = container.offsetWidth;
}
