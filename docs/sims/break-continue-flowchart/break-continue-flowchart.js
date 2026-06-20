// Break vs Continue Flowchart - Moving Rainbow MicroSim (Mermaid)
// A for-loop cycle showing how break exits and continue skips. Click a node
// to read what it does. Break path = red, continue path = orange, body = green.
// CANVAS_HEIGHT: 1010
document.addEventListener('DOMContentLoaded', function () {
  const info = {
    start:  '<b>Start Loop.</b> Python begins the for loop and gets ready to walk through the range.',
    check:  '<b>i in range?</b> If there are still items left, keep looping; otherwise leave the loop.',
    cond:   '<b>Check condition.</b> Test something about this iteration before deciding what to do.',
    brk:    '<b>break?</b> <span style="color:#c0392b">break exits the loop entirely</span> - no more iterations run.',
    cont:   '<b>continue?</b> <span style="color:#d35400">continue skips to the next iteration</span> - the rest of the body is skipped.',
    body:   '<b>Run loop body.</b> This is where your animation code goes - set pixel colors, write the strip, sleep.',
    top:    '<b>Back to top.</b> Return to the range check and start the next iteration.',
    done:   '<b>Exit loop.</b> The loop is finished and the program continues after it.',
  };

  const graph = [
    'flowchart TD',
    '  start([Start Loop]) --> check{i in range?}',
    '  check -- no --> done([Exit loop])',
    '  check -- yes --> cond[Check condition]',
    '  cond --> brk{break?}',
    '  brk -- yes --> done',
    '  brk -- no --> cont{continue?}',
    '  cont -- yes --> top[Back to top]',
    '  cont -- no --> body[Run loop body]',
    '  body --> top',
    '  top --> check',
    '  classDef startEnd fill:#642580,stroke:#4a1b60,color:#fff;',
    '  classDef red fill:#c0392b,stroke:#7d2018,color:#fff;',
    '  classDef orange fill:#e8903a,stroke:#b56a18,color:#fff;',
    '  classDef green fill:#2e8b57,stroke:#1c5a37,color:#fff;',
    '  classDef normal fill:#41bac1,stroke:#2a8086,color:#fff;',
    '  class start startEnd;',
    '  class done red;',
    '  class check,cond,top normal;',
    '  class brk red;',
    '  class cont orange;',
    '  class body green;',
  ].join('\n');

  const main = document.querySelector('main');
  main.innerHTML =
    '<style>' +
    '  #bc-wrap { font-family: Arial, Helvetica, sans-serif; max-width: 900px; margin: 0 auto; padding: 8px 12px; }' +
    '  #bc-wrap h3 { text-align: center; color: #1a3a6c; margin: 6px 0 10px; }' +
    '  #diagram { display: flex; justify-content: center; background: aliceblue; border: 1px solid silver; border-radius: 8px; padding: 12px; }' +
    '  #diagram .node { cursor: pointer; }' +
    '  #diagram .edgeLabel { background: #ffffff !important; padding: 1px 4px; border-radius: 3px; }' +
    '  #diagram .edgeLabel, #diagram .edgeLabel p, #diagram .edgeLabel span, #diagram .edgeLabel div { color: #333 !important; font-weight: 700; }' +
    '  #node-info { margin-top: 12px; background: #f1e8f8; border: 1px solid #d8c4ea; border-radius: 8px; padding: 12px 14px; font-size: 15px; line-height: 1.45; color: #222; }' +
    '</style>' +
    '<div id="bc-wrap">' +
    '  <h3>break vs. continue in a for Loop</h3>' +
    '  <div id="diagram" class="mermaid">' + graph + '</div>' +
    '  <div id="node-info">Click any box to learn what it does. Red = break path, orange = continue path, green = loop body.</div>' +
    '</div>';

  mermaid.initialize({
    startOnLoad: false,
    securityLevel: 'loose',
    theme: 'base',
    themeVariables: { lineColor: '#444444', edgeLabelBackground: '#ffffff', fontSize: '15px' },
  });

  mermaid.run({ querySelector: '#diagram' }).then(function () {
    document.querySelectorAll('#diagram .node').forEach(function (node) {
      const m = node.id.match(/flowchart-([a-z]+)/);
      if (!m) return;
      const key = m[1];
      if (!info[key]) return;
      node.addEventListener('click', function () {
        document.getElementById('node-info').innerHTML = info[key];
      });
    });
  });
});
