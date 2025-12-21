// =====================
// DATA
// =====================
const beforeNames = ["Others", "Lân", "Ly", "Lâm", "Tô", "Lu", "Ki"];
const beforeValues = [4, 13, 14, 15, 16, 17, 21];

const afterNames = ["Others", "Ki", "Lu", "Lân", "Ly", "Lâm", "Tô"];
const afterValues = [2, 2, 4, 5, 7, 10, 70];

// =====================
// TRACES
// =====================
const trace1 = {
    type: "bar",
    orientation: "h",
    x: beforeValues,
    y: beforeNames,
    text: beforeValues,
    textposition: "outside",
    marker: { color: "#1f77b4" },
    xaxis: "x1",
    yaxis: "y1",
    showlegend: false
};

const trace2 = {
    type: "bar",
    orientation: "h",
    x: afterValues,
    y: afterNames,
    text: afterValues,
    textposition: "outside",
    marker: { color: "#ff7f0e" },
    xaxis: "x2",
    yaxis: "y2",
    showlegend: false
};

// =====================
// LAYOUT
// =====================
const layout = {
    grid: { rows: 1, columns: 2, pattern: "independent" },
    height: 400,
    margin: { l: 60, r: 40, t: 40, b: 40 },
    
    paper_bgcolor: "rgba(0,0,0,0)",
    plot_bgcolor: "rgba(0,0,0,0)",
    font: { color: "#ffffff", size: 12 },

    xaxis1: { showgrid: false, zeroline: false },
    yaxis1: { automargin: true },
    xaxis2: { showgrid: false, zeroline: false },
    yaxis2: { automargin: true },

    annotations: [
        {
            text: "<b>Before 2025</b>",
            x: 0.20,
            y: 1.08,
            showarrow: false,
            xref: "paper",
            yref: "paper",
            font: { size: 14, color: "#ffffff" }
        },
        {
            text: "<b>After 2025</b>",
            x: 0.80,
            y: 1.08,
            showarrow: false,
            xref: "paper",
            yref: "paper",
            font: { size: 14, color: "#ffffff" }
        }
    ]
};

Plotly.newPlot("chart", [trace1, trace2], layout, { responsive: true });