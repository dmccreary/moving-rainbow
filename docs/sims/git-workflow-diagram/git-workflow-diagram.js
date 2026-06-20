// Git Workflow Diagram - Moving Rainbow MicroSim (Mermaid)
// The three places Git stores your work - your computer, the local repo, and
// GitHub - and the commands that move data between them. Click a box. (Understand.)
// CANVAS_HEIGHT: 430
document.addEventListener('DOMContentLoaded', function () {
  const info = {
    edit:    '<b>Edit code in Thonny.</b> Your working files live on your computer. Nothing is saved to Git yet.',
    add:     '<b>git add &lt;files&gt;</b> - stage the changes you want to include in the next commit.',
    stage:   '<b>Staging Area.</b> A holding zone listing exactly what will go into the next commit.',
    commits: "<b>git commit -m '...'</b> - save a snapshot to your local commit history with a message.",
    remote:  '<b>GitHub repository.</b> The cloud copy. <code>git push</code> uploads commits; <code>git pull</code> downloads them.',
    other:   '<b>git clone &lt;url&gt;</b> - copy the entire repository onto another computer.',
  };

  const graph = [
    'flowchart LR',
    '  subgraph PC[Your Computer]',
    '    direction TB',
    '    edit[Edit code in Thonny] --> add[git add files]',
    '    add --> stage[Staging Area]',
    '  end',
    '  subgraph LOCAL[Local Git Repo]',
    '    direction TB',
    '    commits[Local commit history]',
    '  end',
    '  subgraph CLOUD[GitHub Cloud]',
    '    direction TB',
    '    remote[GitHub repository]',
    '    other[Another computer]',
    '  end',
    "  stage -->|git commit -m '...'| commits",
    '  commits -->|git push| remote',
    '  remote -.->|git pull| commits',
    '  remote -.->|git clone| other',
    '  classDef act fill:#2b78e4,stroke:#1c4f99,color:#fff;',
    '  classDef store fill:#642580,stroke:#4a1b60,color:#fff;',
    '  classDef faded fill:#cccccc,stroke:#999,color:#333;',
    '  class edit,add act;',
    '  class stage,commits,remote store;',
    '  class other faded;',
  ].join('\n');

  const main = document.querySelector('main');
  main.innerHTML =
    '<style>' +
    '  #git-wrap { font-family: Arial, Helvetica, sans-serif; max-width: 920px; margin: 0 auto; padding: 8px 12px; }' +
    '  #git-wrap h3 { text-align: center; color: #1a3a6c; margin: 6px 0; }' +
    '  #diagram { display: flex; justify-content: center; background: aliceblue; border: 1px solid silver; border-radius: 8px; padding: 12px; }' +
    '  #diagram .node { cursor: pointer; }' +
    '  #diagram .edgeLabel { background: #ffffff !important; padding: 1px 4px; border-radius: 3px; }' +
    '  #diagram .edgeLabel, #diagram .edgeLabel p, #diagram .edgeLabel span, #diagram .edgeLabel div { color: #333 !important; font-family: monospace; font-weight: 700; }' +
    '  #node-info { margin-top: 12px; background: #f1e8f8; border: 1px solid #d8c4ea; border-radius: 8px; padding: 12px 14px; font-size: 15px; color: #222; }' +
    '  #node-info code { background: #efe6f7; padding: 1px 4px; border-radius: 3px; }' +
    '</style>' +
    '<div id="git-wrap">' +
    '  <h3>Where Git Stores Your Work</h3>' +
    '  <div id="diagram" class="mermaid">' + graph + '</div>' +
    '  <div id="node-info">Three places hold your code: your computer, the local repo, and GitHub. Click a box to see the command.</div>' +
    '</div>';

  mermaid.initialize({
    startOnLoad: false, securityLevel: 'loose', theme: 'base',
    themeVariables: { lineColor: '#555', edgeLabelBackground: '#ffffff', fontSize: '14px' },
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
