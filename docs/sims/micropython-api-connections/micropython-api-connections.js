// MicroPython API Connections - Moving Rainbow MicroSim (Mermaid)
// The Pico in the center, arrows to each component labeled with the
// MicroPython API used. Click a component to learn what its API does.
// CANVAS_HEIGHT: 680
document.addEventListener('DOMContentLoaded', function () {
  const info = {
    led:     '<b>NeoPixel strip.</b> <code>neopixel.NeoPixel(machine.Pin(0), n)</code> drives addressable LEDs on GP0. Covered in the NeoPixel chapters.',
    pwm:     '<b>Buzzer / Servo.</b> <code>machine.PWM(machine.Pin(p))</code> sends a pulse-width signal to make sound or move a servo. Covered in the electronics chapters.',
    photo:   '<b>Photoresistor.</b> <code>machine.ADC(machine.Pin(26))</code> reads an analog light level (0-65535). Covered in the sensors chapter.',
    btn:     '<b>Button.</b> <code>machine.Pin(15, machine.Pin.IN)</code> reads a digital on/off input. Covered in the input-devices chapter.',
    onboard: '<b>Built-in LED.</b> <code>machine.Pin(25, machine.Pin.OUT)</code> turns the onboard green LED on and off. Covered in the first lessons.',
    time:    '<b>Time / Delays.</b> <code>utime.sleep(seconds)</code> pauses the program so animations are visible. Used in every chapter.',
    rnd:     '<b>Random effects.</b> <code>urandom.randint(a, b)</code> picks random numbers for sparkle and noise effects. Covered in the animation chapters.',
  };

  const graph = [
    'flowchart LR',
    '  pico([Raspberry Pi Pico])',
    '  pico -->|neopixel.NeoPixel via Pin GP0| led[LED strip]',
    '  pico -->|machine.PWM via Pin| pwm[Buzzer / Servo]',
    '  pico -->|machine.ADC via Pin GP26| photo[Photoresistor]',
    '  pico -->|machine.Pin GP15 IN| btn[Button]',
    '  pico -->|machine.Pin 25 OUT| onboard[Built-in LED]',
    '  pico -->|utime.sleep| time[Time / Delays]',
    '  pico -->|urandom.randint| rnd[Random effects]',
    '  classDef hub fill:#642580,stroke:#4a1b60,color:#fff;',
    '  classDef gpio fill:#2b78e4,stroke:#1c4f99,color:#fff;',
    '  classDef pwm fill:#e8903a,stroke:#b56a18,color:#fff;',
    '  classDef adc fill:#2e8b57,stroke:#1c5a37,color:#fff;',
    '  classDef tim fill:#7030a0,stroke:#4a1f6a,color:#fff;',
    '  classDef rng fill:#d4ac0d,stroke:#9a7d09,color:#000;',
    '  class pico hub;',
    '  class led,btn,onboard gpio;',
    '  class pwm pwm;',
    '  class photo adc;',
    '  class time tim;',
    '  class rnd rng;',
  ].join('\n');

  const main = document.querySelector('main');
  main.innerHTML =
    '<style>' +
    '  #api-wrap { font-family: Arial, Helvetica, sans-serif; max-width: 940px; margin: 0 auto; padding: 8px 12px; }' +
    '  #api-wrap h3 { text-align: center; color: #1a3a6c; margin: 6px 0 10px; }' +
    '  #diagram { display: flex; justify-content: center; background: aliceblue; border: 1px solid silver; border-radius: 8px; padding: 12px; }' +
    '  #diagram .node { cursor: pointer; }' +
    '  #diagram .edgeLabel { background: #ffffff !important; padding: 1px 4px; border-radius: 3px; }' +
    '  #diagram .edgeLabel, #diagram .edgeLabel p, #diagram .edgeLabel span, #diagram .edgeLabel div { color: #333 !important; font-family: monospace; font-weight: 600; }' +
    '  #node-info { margin-top: 12px; background: #f1e8f8; border: 1px solid #d8c4ea; border-radius: 8px; padding: 12px 14px; font-size: 15px; line-height: 1.5; color: #222; }' +
    '  #node-info code { background: #efe6f7; padding: 1px 4px; border-radius: 3px; }' +
    '</style>' +
    '<div id="api-wrap">' +
    '  <h3>How the Pico Talks to Each Component</h3>' +
    '  <div id="diagram" class="mermaid">' + graph + '</div>' +
    '  <div id="node-info">Click any component to see the MicroPython API that controls it.</div>' +
    '</div>';

  mermaid.initialize({
    startOnLoad: false,
    securityLevel: 'loose',
    theme: 'base',
    themeVariables: { lineColor: '#555555', edgeLabelBackground: '#ffffff', fontSize: '14px' },
  });

  mermaid.run({ querySelector: '#diagram' }).then(function () {
    document.querySelectorAll('#diagram .node').forEach(function (node) {
      const m = node.id.match(/flowchart-([a-z]+)/);
      if (!m || !info[m[1]]) return;
      node.addEventListener('click', function () {
        document.getElementById('node-info').innerHTML = info[m[1]];
      });
    });
  });
});
