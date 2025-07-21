# MicroSim Template

<iframe src="main.html" height="400"></iframe>

<iframe src="main.html" height="400px" scrolling="no"></iframe>

<!--
![Image Name](./image.png){ width="400" }
-->

[Run the MicroSim](main.html){ .md-button .md-button--primary }
[Edit this MicroSim](https://editor.p5js.org/dmccreary/sketches/dJq4nTXE4)

## Sample iframe

```html
<iframe src="https://dmccreary.github.io/microsims/sims/name/main.html" height="400"  scrolling="no"></iframe>
```

## About this MicroSim

This MicroSim teaches us how to
specify the drawing of a static filled circle.

## Sample Prompt

!!! prompt
  Create a single file p5.js sketch.
  Draw a green circle on a 600x400 canvas with a radius of 200.

## Sample Response

```javascript
// canvas regions setup
// let canvasWidth = 750;
let drawHeight = 400;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let aspectRatio = 1.91; // Open Graph standard
let canvasWidth = canvasHeight * aspectRatio;
let radius = 200;

function setup() {
  const canvas = createCanvas(canvasWidth, canvasHeight);
  var mainElement = document.querySelector('main');
  canvas.parent(mainElement);
}

function draw() {
  // background of drawing region
  fill('aliceblue');
  rect(0, 0, canvasWidth, drawHeight);

  // background of controls
  fill('whitegray');
  rect(0, drawHeight, canvasWidth, controlHeight);
  circle(canvasWidth/2, canvasHeight/2, radius);
}
```

## Lesson Plan

### Grade Level, Subject and Topic

9th grade geometry. Circle and radius.

### Activities

#### Fill Color

Change the color in the prompt.  You
can specify any one of the [140 named colors](https://www.w3schools.com/tags/ref_colornames.asp).

#### Border Weight

Change the prompt to include a black border of
width 10.

#### Border Color

Change the prompt to make the border purple.

#### Change the Radius

Change the prompt to make the circle smaller
or larger by changing the radius from 10 to 200.

#### Change the Location

Change the prompt to move the circle to the left or right.

## References

* [Processing Wiki on Positioning Your Canvas](https://github.com/processing/p5.js/wiki/Positioning-your-canvas)