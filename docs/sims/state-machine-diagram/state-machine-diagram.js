// State Machine Diagram - Moving Rainbow MicroSim (Mermaid)
// A three-mode state machine. Press Animate to step through the cycle; the
// current mode highlights. Click a mode to see what it does. (Understand.)
// CANVAS_HEIGHT: 440
document.addEventListener('DOMContentLoaded', function () {
  let current = 0;

  const info = {
    Mode0: '<b>Mode 0 - Red.</b> Every pixel glows a steady red.',
    Mode1: '<b>Mode 1 - Green.</b> A green comet chases along the strip.',
    Mode2: '<b>Mode 2 - Blue.</b> A slow blue breathing pulse.',
  };

  const main = document.querySelector('main');
  main.innerHTML =
    '<style>' +
    '  #sm-wrap { font-family: Arial, Helvetica, sans-serif; max-width: 820px; margin: 0 auto; padding: 8px 12px; }' +
    '  #sm-wrap h3 { text-align: center; color: #1a3a6c; margin: 6px 0; }' +
    '  #sm-bar { text-align: center; margin-bottom: 8px; }' +
    '  #sm-bar button { padding: 6px 14px; border: 1px solid #1c4f99; background: #2b78e4; color: #fff; border-radius: 6px; cursor: pointer; font-size: 14px; }' +
    '  #diagram { display: flex; justify-content: center; background: aliceblue; border: 1px solid silver; border-radius: 8px; padding: 12px; min-height: 180px; }' +
    '  #diagram .statediagram-state { cursor: pointer; }' +
    '  #node-info { margin-top: 12px; background: #f1e8f8; border: 1px solid #d8c4ea; border-radius: 8px; padding: 12px 14px; font-size: 15px; color: #222; }' +
    '</style>' +
    '<div id="sm-wrap">' +
    '  <h3>Three-Mode State Machine</h3>' +
    '  <div id="sm-bar"><button id="sm-animate">Animate (next state)</button></div>' +
    '  <div id="diagram" class="mermaid"></div>' +
    '  <div id="node-info">Press Animate to advance. Click a mode to see what its LED animation does.</div>' +
    '</div>';

  mermaid.initialize({
    startOnLoad: false, securityLevel: 'loose', theme: 'base',
    themeVariables: { lineColor: '#444', fontSize: '15px' },
  });

  function source(cur) {
    return [
      'stateDiagram-v2', '  direction LR',
      '  Mode0 : Mode 0 - Red', '  Mode1 : Mode 1 - Green', '  Mode2 : Mode 2 - Blue',
      '  [*] --> Mode0',
      '  Mode0 --> Mode1 : button pressed (debounced)',
      '  Mode1 --> Mode2 : button pressed (debounced)',
      '  Mode2 --> Mode0 : button pressed (debounced)',
      '  classDef current fill:#ffd23f,stroke:#caa400,color:#000,stroke-width:3px',
      '  class Mode' + cur + ' current',
    ].join('\n');
  }

  async function render() {
    const div = document.getElementById('diagram');
    div.removeAttribute('data-processed');
    div.innerHTML = source(current);
    await mermaid.run({ nodes: [div] });
    div.querySelectorAll('.statediagram-state, g.node').forEach(function (node) {
      const txt = (node.textContent || '');
      let key = null;
      if (txt.indexOf('Mode 0') >= 0) key = 'Mode0';
      else if (txt.indexOf('Mode 1') >= 0) key = 'Mode1';
      else if (txt.indexOf('Mode 2') >= 0) key = 'Mode2';
      if (!key) return;
      node.style.cursor = 'pointer';
      node.addEventListener('click', function () {
        document.getElementById('node-info').innerHTML = info[key];
      });
    });
  }

  document.getElementById('sm-animate').addEventListener('click', function () {
    current = (current + 1) % 3;
    document.getElementById('node-info').innerHTML =
      'Transitioned to <b>Mode ' + current + '</b>. ' + info['Mode' + current];
    render();
  });

  render();
});
