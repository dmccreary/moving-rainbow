// Problem-Solving Steps Flowchart - Moving Rainbow MicroSim (Mermaid)
// A vertical flowchart of the five problem-solving steps programmers use.
// Click any step to read a definition plus an LED-specific example.
// CANVAS_HEIGHT: 780
document.addEventListener('DOMContentLoaded', function () {
  const info = {
    step1: "<b>Understand the Problem.</b> Restate the problem in your own words before touching code. " +
           "<i>LED example: \"I need 30 LEDs to show a rainbow that scrolls right, one pixel per frame.\"</i>",
    step2: "<b>Plan Your Solution.</b> Write pseudocode or draw a flowchart before opening your editor. " +
           "<i>LED example: pseudocode listing how to calculate each pixel's color from its position.</i>",
    step3: "<b>Write the Code.</b> Translate your plan into Python one small, testable piece at a time. " +
           "<i>LED example: write just the loop that assigns a hue to each pixel index.</i>",
    step4: "<b>Test and Debug.</b> Run the program and compare the actual output to the expected output. " +
           "<i>LED example: the rainbow scrolls backward - trace the sign of the offset increment.</i>",
    step5: "<b>Reflect and Improve.</b> Ask: is the code readable? Can it be reused? What would you change? " +
           "<i>LED example: extract the hue formula into a named function for a later chapter.</i>",
  };

  const graph = [
    'flowchart TD',
    '  step1([Understand the Problem]) --> step2[Plan Your Solution]',
    '  step2 --> step3[Write the Code]',
    '  step3 --> step4{Does it work?}',
    '  step4 -- bug found --> step3',
    '  step4 -- it works! --> step5([Reflect and Improve])',
    '  step5 -- new challenge --> step1',
  ].join('\n');

  const main = document.querySelector('main');
  main.innerHTML =
    '<style>' +
    '  #ps-wrap { font-family: Arial, Helvetica, sans-serif; max-width: 900px; margin: 0 auto; padding: 8px 12px; }' +
    '  #ps-wrap h3 { text-align: center; color: #1a3a6c; margin: 6px 0 10px; }' +
    '  #diagram { display: flex; justify-content: center; background: aliceblue; border: 1px solid silver; border-radius: 8px; padding: 12px; }' +
    '  #diagram .node { cursor: pointer; }' +
    '  #diagram .edgeLabel { background: #ffffff !important; padding: 1px 4px; border-radius: 3px; }' +
    '  #diagram .edgeLabel, #diagram .edgeLabel p, #diagram .edgeLabel span, #diagram .edgeLabel div { color: #14787f !important; font-weight: 700; }' +
    '  #step-info { margin-top: 12px; background: #f1e8f8; border: 1px solid #d8c4ea; border-radius: 8px; padding: 12px 14px; font-size: 15px; line-height: 1.45; color: #222; }' +
    '</style>' +
    '<div id="ps-wrap">' +
    '  <h3>Five Problem-Solving Steps</h3>' +
    '  <div id="diagram" class="mermaid">' + graph + '</div>' +
    '  <div id="step-info">Click any step in the flowchart to learn more.</div>' +
    '</div>';

  mermaid.initialize({
    startOnLoad: false,
    securityLevel: 'loose',
    theme: 'base',
    themeVariables: {
      primaryColor: '#642580',
      primaryTextColor: '#ffffff',
      primaryBorderColor: '#4a1b60',
      lineColor: '#444444',
      edgeLabelBackground: '#ffffff',
      fontSize: '15px',
    },
  });

  mermaid.run({ querySelector: '#diagram' }).then(function () {
    document.querySelectorAll('#diagram .node').forEach(function (node) {
      const m = node.id.match(/(step\d)/);
      if (!m) return;
      const key = m[1];
      node.addEventListener('click', function () {
        document.getElementById('step-info').innerHTML = info[key];
      });
    });
  });
});
