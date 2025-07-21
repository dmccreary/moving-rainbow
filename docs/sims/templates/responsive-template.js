// MicroSim p5.js responsive template
// Use this template to create a responsive p5.js sketch that fills its parent container
// The sketch will resize the canvas with automatically when the container is resized

// global variables for width and height
let containerWidth; // this values is calculated by container upon init and changed on resize
let containerHeight = 400; // fixed height on page determined by MicroSim author
// the width of the entire canvas
let canvasWidth = containerHeight;
// The top drawing region above the interactive controls
let drawHeight = 400;
// control region height
let controlHeight = 50;
// The total hight of both the drawing region height + the control region height
let canvasHeight = drawHeight + controlHeight;
// margin around the active plotting region
let margin = 25;
let sliderLeftMargin = 105;
// larger text so students in the back of the room can read the labels
let defaultTextSize = 16;

function setup() {
    // get the container dimensions
    updateCanvasSize();
    // Create a canvas to match the parent container's width and height
    const canvas = createCanvas(containerWidth, containerHeight);
    var mainElement = document.querySelector('main');
    canvas.parent(mainElement);
    /* canvas.parent('p5-container'); */
    noLoop(); // Stop the draw loop since we'll redraw only on resize
}

function draw() {
  // Draw light gray outlines of the draw and controls regions
  stroke('silver');
  strokeWeight(1);
  // Draw the drawing area background in light blue
  fill('aliceblue');
  rect(0,0, canvasWidth, drawHeight);
  // Draw the controls area background in white
  fill('white');
  rect(0,drawHeight, canvasWidth, controlHeight);
  fill('black');
  textSize(36);
  textAlign(CENTER, CENTER);

  // Display container dimensions
  text(`Width: ${containerWidth}px\nHeight: ${containerHeight}px`, width / 2, height / 2);
}

function windowResized() {
  // Update canvas size when the container resizes
  updateCanvasSize();
  resizeCanvas(containerWidth, containerHeight);
  // resize any sliders here to match the new canvasWidth
  // speedSlider.size(canvasWidth - sliderLeftMargin - 15);
  redraw();
}

function updateCanvasSize() {
  // Get the width of the <main> element
  const container = document.querySelector('main').getBoundingClientRect();
  containerWidth = Math.floor(container.width);  // Avoid fractional pixels
  // set the canvas width to the container width
  canvasWidth = containerWidth;
}