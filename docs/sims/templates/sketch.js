<<<<<<< HEAD
// MicroSim Template for 2D geometry with region drawing parameters
// the width of the entire canvas
let canvasWidth = 600;
// The top drawing region above the interactive controls
let drawHeight = 400;
// control region height
let controlHeight = 50;
// The total hight of both the drawing region height + the control region height
let canvasHeight = drawHeight + controlHeight;
// margin around the active plotting region
let margin = 25;
// larger text so students in the back of the room can read the labels
let defaultTextSize = 16;

function setup {
    const canvas = createCanvas(canvasWidth, canvasHeight);
    // canvas.parent('canvas-container');
    var mainElement = document.querySelector('main');
    canvas.parent(mainElement);
    textSize(defaultTextSize);

    // create a new slider at th bottom of the canvas
    mySlider = createSlider(0, 100, 50, 1);
    mySlider.position(sliderLeftMargin, drawHeight + 30);
    mySlider.size(canvasWidth - 2*margin); 
}

function draw() {
    // make the background drawing region a very light blue
    fill('aliceblue');
    rect(0, 0, canvasWidth, drawHeight);
    // make the background of the controls area white
    fill('white')
    rect(0, drawHeight, canvasWidth, controlHeight);

    // get the updated slider value
    val = mySlider.value();

    // put your custom code here
    
    // draw label and value
    text("MySlider: " +  val, 10, drawHeight + 25)
=======
// global variables for width and height
let containerWidth; // calculated by container upon resize
let containerHeight = 200; // fixed height on page

function setup() {
    // Create a canvas to match the parent container's size
    updateCanvasSize();
    const canvas = createCanvas(containerWidth, containerHeight);
    canvas.parent(document.querySelector('main'));
    /* canvas.parent('p5-container'); */
    noLoop(); // Stop the draw loop since we'll redraw only on resize
}

function draw() {
  background('aliceblue');
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
  redraw();
}

function updateCanvasSize() {
    // Get the exact dimensions of the container
    const container = document.querySelector('main').getBoundingClientRect();
    containerWidth = Math.floor(container.width);  // Avoid fractional pixels
>>>>>>> fca05a3e66c92aa31c23acb1d85d21069fd37346
}