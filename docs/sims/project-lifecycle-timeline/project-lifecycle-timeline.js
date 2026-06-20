// Project Lifecycle Timeline - Moving Rainbow MicroSim (Mermaid Gantt)
// The six-week capstone, phase by phase. Click any bar to see that phase's
// success criteria. (Analyze: which phase is most at risk.)
// CANVAS_HEIGHT: 560
document.addEventListener('DOMContentLoaded', function () {
  const weekInfo = {
    1: '<b>Week 1 - Plan.</b> Success: a written proposal with the idea, the constraints, and the must-have modes listed.',
    2: '<b>Week 2 - Build MVP.</b> Success: the strip shows a basic animation driven by values in config.py.',
    3: '<b>Week 3 - Core features.</b> Success: the button cycles through all must-have modes, with a Git commit at each milestone.',
    4: '<b>Week 4 - Enhancements.</b> Success: should-have features and battery power work, with a polished feel.',
    5: '<b>Week 5 - Verify.</b> Success: the full test protocol passes and peer-review issues are fixed.',
    6: '<b>Week 6 - Present.</b> Success: a rehearsed demo and a completed capstone presentation.',
  };

  const graph = [
    'gantt',
    '  title Six-Week Capstone Project Timeline',
    '  dateFormat YYYY-MM-DD',
    '  axisFormat %b %d',
    '  section Week 1 Plan',
    '    Project ideation     :w1a, 2026-01-05, 2d',
    '    Constraint analysis  :w1b, after w1a, 2d',
    '    Proposal document    :w1c, after w1b, 3d',
    '  section Week 2 Build MVP',
    '    Circuit wiring       :w2a, 2026-01-12, 2d',
    '    Config.py setup      :w2b, after w2a, 2d',
    '    Basic animation      :w2c, after w2b, 3d',
    '  section Week 3 Core features',
    '    Button cycling       :w3a, 2026-01-19, 3d',
    '    All must-have modes  :w3b, after w3a, 3d',
    '    Git commit milestones:w3c, 2026-01-19, 6d',
    '  section Week 4 Enhancements',
    '    Should-have features :w4a, 2026-01-26, 3d',
    '    Battery integration  :w4b, after w4a, 2d',
    '    UX polish            :w4c, after w4b, 2d',
    '  section Week 5 Verify',
    '    Full testing         :w5a, 2026-02-02, 3d',
    '    Peer code review     :w5b, after w5a, 2d',
    '    Fix issues found     :w5c, after w5b, 2d',
    '  section Week 6 Present',
    '    Demo rehearsal       :w6a, 2026-02-09, 2d',
    '    Capstone presentation:w6b, after w6a, 2d',
    '    Peer feedback        :w6c, after w6b, 1d',
  ].join('\n');

  const main = document.querySelector('main');
  main.innerHTML =
    '<style>' +
    '  #pl-wrap { font-family: Arial, Helvetica, sans-serif; max-width: 920px; margin: 0 auto; padding: 8px 12px; }' +
    '  #pl-wrap h3 { text-align: center; color: #1a3a6c; margin: 6px 0; }' +
    '  #diagram { background: aliceblue; border: 1px solid silver; border-radius: 8px; padding: 8px; overflow-x: auto; }' +
    '  #diagram .task { cursor: pointer; }' +
    '  #node-info { margin-top: 12px; background: #f1e8f8; border: 1px solid #d8c4ea; border-radius: 8px; padding: 12px 14px; font-size: 15px; color: #222; }' +
    '</style>' +
    '<div id="pl-wrap">' +
    '  <h3>Six-Week Capstone Timeline</h3>' +
    '  <div id="diagram" class="mermaid">' + graph + '</div>' +
    '  <div id="node-info">Click any task bar to see the success criteria for that week.</div>' +
    '</div>';

  mermaid.initialize({
    startOnLoad: false, securityLevel: 'loose', theme: 'base',
    gantt: { barHeight: 18, barGap: 4, fontSize: 12 },
  });

  function weekFromId(id) {
    const m = id && id.match(/w(\d)/);
    return m ? m[1] : null;
  }

  mermaid.run({ querySelector: '#diagram' }).then(function () {
    // Gantt task bars carry their task id; text labels sit alongside.
    document.querySelectorAll('#diagram rect.task, #diagram .task, #diagram text.taskText, #diagram .taskTextOutsideRight, #diagram .taskTextOutsideLeft').forEach(function (el) {
      const wk = weekFromId(el.id) || weekFromId((el.className && el.className.baseVal) || '');
      const show = function () {
        // find a week number from this element's id or nearest task id
        let w = weekFromId(el.id);
        if (!w) { const t = el.textContent || ''; /* fall through */ }
        if (w && weekInfo[w]) document.getElementById('node-info').innerHTML = weekInfo[w];
      };
      el.style.cursor = 'pointer';
      el.addEventListener('click', show);
    });
    // Robust fallback: map by reading each task rect's id (w1a..w6c)
    document.querySelectorAll('#diagram rect').forEach(function (r) {
      const w = weekFromId(r.id);
      if (!w || !weekInfo[w]) return;
      r.style.cursor = 'pointer';
      r.addEventListener('click', function () { document.getElementById('node-info').innerHTML = weekInfo[w]; });
    });
  });
});
