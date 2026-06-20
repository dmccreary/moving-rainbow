// Brightness Envelope Comparison - Moving Rainbow MicroSim (Chart.js)
// Four tabs - Heartbeat, Comet Tail, Larson Scanner, Sine Breathing - each
// showing its brightness envelope plus a live strip. (Analyze the shape.)
// CANVAS_HEIGHT: 460
document.addEventListener('DOMContentLoaded', function () {
  let tab = 'heartbeat';
  let ph = 0;
  let cometHead = 20, larsonWidth = 4;
  const STRIP = 30;

  const main = document.querySelector('main');
  main.innerHTML =
    '<style>' +
    '  #be-wrap { font-family: Arial, Helvetica, sans-serif; max-width: 760px; margin: 0 auto; padding: 8px 12px; }' +
    '  #be-wrap h3 { text-align: center; color: #1a3a6c; margin: 6px 0; }' +
    '  #be-tabs { display: flex; gap: 6px; justify-content: center; flex-wrap: wrap; margin-bottom: 8px; }' +
    '  #be-tabs button { padding: 6px 12px; border: 1px solid #bbb; background: #eee; border-radius: 6px; cursor: pointer; font-size: 13px; }' +
    '  #be-tabs button.active { background: #2b78e4; color: #fff; border-color: #1c4f99; }' +
    '  #chartbox { height: 230px; }' +
    '  #be-strip { display: flex; gap: 2px; margin: 10px 0 6px; height: 22px; }' +
    '  #be-strip div { flex: 1; border-radius: 3px; background: #111; }' +
    '  #be-controls { font-size: 14px; min-height: 26px; text-align: center; }' +
    '</style>' +
    '<div id="be-wrap">' +
    '  <h3>Brightness Envelope Comparison</h3>' +
    '  <div id="be-tabs">' +
    '    <button data-tab="heartbeat" class="active">Heartbeat</button>' +
    '    <button data-tab="comet">Comet Tail</button>' +
    '    <button data-tab="larson">Larson Scanner</button>' +
    '    <button data-tab="breathing">Sine Breathing</button>' +
    '  </div>' +
    '  <div id="chartbox"><canvas id="chart"></canvas></div>' +
    '  <div id="be-strip"></div>' +
    '  <div id="be-controls"></div>' +
    '</div>';

  // build strip cells
  const strip = document.getElementById('be-strip');
  for (let i = 0; i < STRIP; i++) strip.appendChild(document.createElement('div'));
  const cells = strip.querySelectorAll('div');

  function gauss(t, mu, sig) { return Math.exp(-((t - mu) * (t - mu)) / (2 * sig * sig)); }

  // brightness 0-255 at envelope coordinate
  function heartbeat(t) { return 255 * (gauss(t, 6, 1.4) + 0.85 * gauss(t, 18, 1.4)); }
  function comet(i, head) { return i <= head ? 255 * Math.exp(-(head - i) * 0.30) : 0; }
  function larson(i, c, w) { return 255 * Math.max(0, 1 - Math.abs(i - c) / w); }
  function breathing(t) { return 127.5 + 127.5 * Math.sin(t * 0.105); }

  // axis config + curve per tab
  function isTimeTab() { return tab === 'heartbeat' || tab === 'breathing'; }
  function xMax() { return tab === 'heartbeat' ? 60 : isTimeTab() ? 60 : STRIP - 1; }
  function curveData() {
    const d = [];
    const xm = xMax();
    for (let x = 0; x <= xm; x++) {
      let y;
      if (tab === 'heartbeat') y = heartbeat(x);
      else if (tab === 'breathing') y = breathing(x);
      else if (tab === 'comet') y = comet(x, cometHead);
      else y = larson(x, larsonCenter(), larsonWidth);
      d.push({ x, y });
    }
    return d;
  }
  function larsonCenter() { const tri = Math.abs(((ph * 0.4) % (2 * (STRIP - 1))) - (STRIP - 1)); return (STRIP - 1) - tri; }

  const chart = new Chart(document.getElementById('chart'), {
    type: 'line',
    data: { datasets: [
      { label: 'envelope', data: curveData(), borderColor: '#642580', pointRadius: 0, borderWidth: 3, tension: 0.25 },
      { label: 'now', data: [], borderColor: '#e8903a', backgroundColor: '#e8903a', pointRadius: 7, showLine: false },
    ] },
    options: {
      responsive: true, maintainAspectRatio: false, animation: false,
      scales: {
        x: { type: 'linear', min: 0, max: 60, title: { display: true, text: 'time' } },
        y: { min: 0, max: 260, title: { display: true, text: 'Brightness (0-255)' } },
      },
      plugins: { legend: { display: false } },
    },
  });

  function setAxis() {
    chart.options.scales.x.max = xMax();
    chart.options.scales.x.title.text = isTimeTab() ? 'time step' : 'pixel index';
  }

  function renderControls() {
    const c = document.getElementById('be-controls');
    if (tab === 'comet') {
      c.innerHTML = '<label>Head position: <span id="vh">' + cometHead + '</span></label> ' +
        '<input id="sh" type="range" min="0" max="29" value="' + cometHead + '">';
      document.getElementById('sh').addEventListener('input', e => { cometHead = parseInt(e.target.value); document.getElementById('vh').textContent = cometHead; });
    } else if (tab === 'larson') {
      c.innerHTML = '<label>Peak width: <span id="vw">' + larsonWidth + '</span></label> ' +
        '<input id="sw" type="range" min="1" max="10" value="' + larsonWidth + '">';
      document.getElementById('sw').addEventListener('input', e => { larsonWidth = parseInt(e.target.value); document.getElementById('vw').textContent = larsonWidth; });
    } else if (tab === 'breathing') {
      c.innerHTML = 'Peak at the top, trough at the bottom, half-way in between - a smooth breath.';
    } else {
      c.innerHTML = 'Two quick beats, then a long rest - just like a heartbeat.';
    }
  }

  function tabColor(b) {
    if (tab === 'heartbeat') return 'rgb(' + Math.round(255 * b) + ',' + Math.round(40 * b) + ',' + Math.round(40 * b) + ')';
    if (tab === 'comet') return 'rgb(' + Math.round(120 * b + 10) + ',' + Math.round(200 * b + 10) + ',' + Math.round(255 * b) + ')';
    if (tab === 'larson') return 'rgb(' + Math.round(255 * b) + ',' + Math.round(20 * b) + ',' + Math.round(20 * b) + ')';
    return 'rgb(' + Math.round(60 * b + 10) + ',' + Math.round(120 * b + 10) + ',' + Math.round(255 * b) + ')';
  }

  document.querySelectorAll('#be-tabs button').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('#be-tabs button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      tab = btn.dataset.tab; ph = 0; setAxis(); renderControls();
    });
  });

  renderControls(); setAxis();

  setInterval(function () {
    ph += 1;
    chart.data.datasets[0].data = curveData();

    // strip + moving dot
    if (tab === 'heartbeat') {
      const t = (ph * 0.5) % 60, b = heartbeat(t) / 255;
      for (const cell of cells) cell.style.background = tabColor(Math.min(1, b));
      chart.data.datasets[1].data = [{ x: t, y: heartbeat(t) }];
    } else if (tab === 'breathing') {
      const t = (ph * 0.5) % 60, b = breathing(t) / 255;
      for (const cell of cells) cell.style.background = tabColor(b);
      chart.data.datasets[1].data = [{ x: t, y: breathing(t) }];
    } else if (tab === 'comet') {
      for (let i = 0; i < STRIP; i++) cells[i].style.background = tabColor(comet(i, cometHead) / 255);
      chart.data.datasets[1].data = [{ x: cometHead, y: comet(cometHead, cometHead) }];
    } else {
      const c = larsonCenter();
      for (let i = 0; i < STRIP; i++) cells[i].style.background = tabColor(larson(i, c, larsonWidth) / 255);
      chart.data.datasets[1].data = [{ x: c, y: 255 }];
    }
    chart.update('none');
  }, 60);
});
