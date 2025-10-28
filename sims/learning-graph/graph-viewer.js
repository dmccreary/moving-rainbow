function drawGraph() {
    // Fetch the graph data from the JSON file
    fetch('intelligent-textbooks.json')
      .then(response => response.json())
      .then(data => {
        // Extract nodes from the JSON data
        const nodes = new vis.DataSet(data.nodes);
  
        // Function to fix the x positions for foundation and goal groups after JSON load
        nodes.forEach(function (node) {
            if (node.group === "found") {
                // placement can't be done in a group
                node.x = -1400;
                node.fixed = { x: true, y: false }; // Fix x, but let y be adjusted by physics
                
            } else if (node.group === "goal") {
                node.x = 1400;
                node.fixed = { x: true, y: false }; // Fix x, but let y be adjusted by physics
            }
          });
  
        const edges = new vis.DataSet(data.edges);
  
        // Create a network
        const container = document.getElementById('mynetwork');
        const graphData = {
              nodes: nodes,
              edges: edges
        };
  
      // Network options
      // Configuration options
      var options = {
         physics: {
         enabled: true,
         solver: 'forceAtlas2Based',
         stabilization: {
           iterations: 1000,
           updateInterval: 25
        },
      },
      layout: {
        improvedLayout: false, // must use false if any pinned nodes
      },
      edges: {
          arrows: {
            to: {
              enabled: true, // all edges have an arrow on the "to"" side
              type: 'arrow' // Options: 'arrow', 'bar', 'circle', 'triangle'
            }
          },
          smooth: {
            type: 'continuous' // Smooth edges
          }
        },
      nodes: {
        shape: 'dot',
        size: 20,
        font: {
          size: 20,
          color: 'black'
        },
        borderWidth: 2,
        borderWidthSelected: 4
      },
      groups: {
        "found": {
           shape: "box", 
           color:{background:'red'},
           font: {color: "white"},
        },
        "term": {
           color:{background:'orange'},
        },
        "stand": {
           color:{background:'gold'},
        },
        "ui": {
           color:{background:'purple'},
        },
        "algorithms": {
           color:{background:'green'},
        },
        "similarity": {
           color:{background:'brown'},
        },
        "learning-theory": {
           color:{background:'green'},
        },
        "ai": {
           color:{background:'pink'},
        },
        "feed": {
           color:{background:'gray'},
        },
        "agents": {
           color:{background:'navy'},
        },
        goal: {
           shape: "star", 
           color:{background:'gold'}, 
           font: { size: 16 }
        }
    }
  };
  
    // Initialize the network
      const network = new vis.Network(container, graphData, options);
    })
    .catch(error => {
            console.error("Error loading or parsing graph-data.json:", error);
    });
  }

function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const mainContent = document.getElementById("main");
  const toggleButton = document.getElementById("toggle-button");

  if (sidebar.style.display === "none") {
    sidebar.style.display = "block";
    // toggleButton.textContent = "☰"; // Open icon
    toggleButton.innerHTML = "&#9776;"; // Hamburger menu icon (open state)

    mainContent.style.marginLeft = "auto"; // Restore margin
  } else {
    sidebar.style.display = "none";
    // toggleButton.textContent = "→"; // Collapse sidebar icon
    toggleButton.innerHTML = "&#8594;"; // Right arrow (collapsed state)
    mainContent.style.marginLeft = "0"; // Remove margin for full width
  }
}