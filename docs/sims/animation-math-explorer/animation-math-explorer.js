// Animation Math Explorer - Moving Rainbow MicroSim (Chart.js)
// Three tabs - Sine Wave, Linear Interpolation, Exponential Decay - each with
// a live chart and a moving dot. Match the math to the LED effect. (Analyze.)
// CANVAS_HEIGHT: 430
document.addEventListener('DOMContentLoaded', function () {
  let tab = 'sine';
  let frame = 0;

  const main = document.querySelector('main');
  main.innerHTML =
    '<style>' +
    '  #am-wrap { font-family: Arial, Helvetica, sans-serif; max-width: 760px; margin: 0 auto; padding: 8px 12px; }' +
    '  #am-wrap h3 { text-align: center; color: #1a3a6c; margin: 6px 0; }' +
    '  #am-tabs { display: flex; gap: 6px; justify-content: center; margin-bottom: 8px; }' +
    '  #am-tabs button { padding: 6px 12px; border: 1px solid #bbb; background: #eee; border-radius: 6px; cursor: pointer; font-size: 13px; }' +
    '  #am-tabs button.active { background: #2b78e4; color: #fff; border-color: #1c4f99; }' +
    '  #chartbox { height: 270px; }' +
    '  #am-controls { margin-top: 8px; font-size: 14px; min-height: 28px; }' +
    '  #am-controls label { margin-right: 6px; }' +
    '  #am-controls input[type=range] { vertical-align: middle; }' +
    '  #am-readout { text-align: center; font-weight: 600; color: #642580; margin-top: 4px; }' +
    '</style>' +
    '<div id="am-wrap">' +
    '  <h3>Animation Math Explorer</h3>' +
    '  <div id="am-tabs">' +
    '    <button data-tab="sine" class="active">Sine Wave</button>' +
    '    <button data-tab="linear">Linear Interpolation</button>' +
    '    <button data-tab="exp">Exponential Decay</button>' +
    '  </div>' +
    '  <div id="chartbox"><canvas id="chart"></canvas></div>' +
    '  <div id="am-controls"></div>' +
    '  <div id="am-readout"></div>' +
    '</div>';

  // sliders (created once, shown per tab)
  const ctr = document.getElementById('am-controls');
  function setControls(html) { ctr.innerHTML = html; }

  let speed = 0.2, aVal = 0, bVal = 255, decay = 0.95;

  function curveFunc(f) {
    if (tab === 'sine') return 127.5 + 127.5 * Math.sin(f * speed);
    if (tab === 'linear') return aVal + (bVal - aVal) * (f / 100);
    return 255 * Math.pow(decay, f);
  }
  function curveData() { const d = []; for (let f = 0; f <= 100; f++) d.push({ x: f, y: curveFunc(f) }); return d; }

  const chart = new Chart(document.getElementById('chart'), {
    type: 'line',
    data: {
      datasets: [
        { label: 'value', data: curveData(), borderColor: '#642580', pointRadius: 0, borderWidth: 3, tension: 0.2 },
        { label: 'now', data: [{ x: 0, y: curveFunc(0) }], borderColor: '#e8903a', backgroundColor: '#e8903a', pointRadius: 7, showLine: false },
      ],
    },
    options: {
      responsive: true, maintainAspectRatio: false, animation: false,
      scales: {
        x: { type: 'linear', min: 0, max: 100, title: { display: true, text: 'Frame number' } },
        y: { min: 0, max: 255, title: { display: true, text: 'Brightness (0-255)' } },
      },
      plugins: { legend: { display: false } },
    },
  });

  function rebuild() { chart.data.datasets[0].data = curveData(); chart.update('none'); }

  function renderControls() {
    if (tab === 'sine') {
      setControls('<label>Speed (step size): <span id="v">' + speed.toFixed(2) + '</span></label>' +
        '<input id="s" type="range" min="0.05" max="0.4" step="0.01" value="' + speed + '">');
      document.getElementById('s').addEventListener('input', e => { speed = parseFloat(e.target.value); document.getElementById('v').textContent = speed.toFixed(2); rebuild(); });
    } else if (tab === 'linear') {
      setControls('<label>a (start): <span id="va">' + aVal + '</span></label>' +
        '<input id="sa" type="range" min="0" max="255" step="1" value="' + aVal + '"> ' +
        '<label>b (end): <span id="vb">' + bVal + '</span></label>' +
        '<input id="sb" type="range" min="0" max="255" step="1" value="' + bVal + '">');
      document.getElementById('sa').addEventListener('input', e => { aVal = parseInt(e.target.value); document.getElementById('va').textContent = aVal; rebuild(); });
      document.getElementById('sb').addEventListener('input', e => { bVal = parseInt(e.target.value); document.getElementById('vb').textContent = bVal; rebuild(); });
    } else {
      setControls('<label>Decay factor: <span id="vd">' + decay.toFixed(2) + '</span></label>' +
        '<input id="sd" type="range" min="0.7" max="0.99" step="0.01" value="' + decay + '">');
      document.getElementById('sd').addEventListener('input', e => { decay = parseFloat(e.target.value); document.getElementById('vd').textContent = decay.toFixed(2); rebuild(); });
    }
  }

  document.querySelectorAll('#am-tabs button').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('#am-tabs button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      tab = btn.dataset.tab; frame = 0; renderControls(); rebuild();
    });
  });

  renderControls();
  setInterval(function () {
    frame = (frame + 1) % 101;
    const y = curveFunc(frame);
    chart.data.datasets[1].data = [{ x: frame, y }];
    chart.update('none');
    document.getElementById('am-readout').textContent = 'frame ' + frame + '  ->  brightness ' + Math.round(y);
  }, 60);
});
