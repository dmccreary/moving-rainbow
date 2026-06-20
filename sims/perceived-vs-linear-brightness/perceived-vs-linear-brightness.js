// Perceived vs Linear Brightness - Moving Rainbow MicroSim (Chart.js)
// Two curves: what the LED does (linear) vs what your eye sees (perceived,
// gamma ~2.2). Drag the slider to see the gap. (Understand: why gamma.)
// CANVAS_HEIGHT: 380
document.addEventListener('DOMContentLoaded', function () {
  const GAMMA = 2.2;
  const xs = [];
  for (let x = 0; x <= 255; x += 5) xs.push(x);
  const linear = xs.map(x => ({ x, y: (x / 255) * 100 }));
  const perceived = xs.map(x => ({ x, y: Math.pow(x / 255, 1 / GAMMA) * 100 }));

  function perceivedAt(v) { return Math.pow(v / 255, 1 / GAMMA) * 100; }
  function linearAt(v) { return (v / 255) * 100; }

  const main = document.querySelector('main');
  main.innerHTML =
    '<style>' +
    '  #pb-wrap { font-family: Arial, Helvetica, sans-serif; max-width: 760px; margin: 0 auto; padding: 8px 12px; }' +
    '  #pb-wrap h3 { text-align: center; color: #1a3a6c; margin: 6px 0; }' +
    '  #chartbox { height: 280px; }' +
    '  #pb-controls { margin-top: 8px; display: flex; align-items: center; gap: 10px; flex-wrap: wrap; font-size: 14px; }' +
    '  #pb-controls input[type=range] { flex: 1; min-width: 160px; }' +
    '  #pb-readout { font-weight: 600; color: #642580; }' +
    '</style>' +
    '<div id="pb-wrap">' +
    '  <h3>Perceived vs. Linear LED Brightness</h3>' +
    '  <div id="chartbox"><canvas id="chart"></canvas></div>' +
    '  <div id="pb-controls">' +
    '    <label>LED value: <span id="pb-val">128</span></label>' +
    '    <input id="pb-slider" type="range" min="0" max="255" value="128" step="1">' +
    '    <span id="pb-readout"></span>' +
    '  </div>' +
    '</div>';

  const start = 128;
  const chart = new Chart(document.getElementById('chart'), {
    type: 'line',
    data: {
      datasets: [
        { label: 'Perceived (what your eye sees)', data: perceived, borderColor: '#642580',
          backgroundColor: '#642580', pointRadius: 0, tension: 0.2, borderWidth: 3 },
        { label: 'Linear (what the LED does)', data: linear, borderColor: '#41BAC1',
          backgroundColor: '#41BAC1', pointRadius: 0, borderDash: [6, 4], borderWidth: 3 },
        { label: 'The gap', data: [{ x: start, y: linearAt(start) }, { x: start, y: perceivedAt(start) }],
          borderColor: '#e8903a', backgroundColor: '#e8903a', pointRadius: 6, borderWidth: 2 },
      ],
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      interaction: { mode: 'nearest', intersect: false },
      scales: {
        x: { type: 'linear', min: 0, max: 255, title: { display: true, text: 'Linear LED value (0-255)' } },
        y: { min: 0, max: 100, title: { display: true, text: 'Perceived brightness (%)' } },
      },
      plugins: {
        legend: { position: 'bottom' },
        tooltip: { callbacks: {
          label: function (ctx) { return 'LED value: ' + Math.round(ctx.parsed.x) + ' -> brightness: ' + Math.round(ctx.parsed.y) + '%'; },
        } },
      },
    },
  });

  const slider = document.getElementById('pb-slider');
  function update() {
    const v = parseInt(slider.value, 10);
    document.getElementById('pb-val').textContent = v;
    const lin = linearAt(v), per = perceivedAt(v);
    chart.data.datasets[2].data = [{ x: v, y: lin }, { x: v, y: per }];
    chart.update('none');
    document.getElementById('pb-readout').textContent =
      'eye sees ' + Math.round(per) + '%, LED sends ' + Math.round(lin) + '% - gap ' + Math.round(per - lin) + '%';
  }
  slider.addEventListener('input', update);
  update();
});
