import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Data
df1 = pd.DataFrame({
    "Dog's name": ["Ki", "Lu", "Tô", "Lâm", "Ly", "Lân", "Others"],
    "percentage": [21, 17, 16, 15, 14, 13, 4]
}).set_index("Dog's name").sort_values(by="percentage")

df2 = pd.DataFrame({
    "Dog's name": ["Tô", "Lâm", "Ly", "Lân", "Lu", "Ki", "Others"],
    "percentage": [70, 10, 7, 5, 4, 2, 2]
}).set_index("Dog's name").sort_values(by="percentage")

# Subplots
fig = make_subplots(
    rows = 1, cols = 2,
    subplot_titles = ("Before 2025", "After 2025"),
    shared_yaxes = False
)

# Plot df1
fig.add_trace(
    go.Bar(
        x = df1["percentage"],
        y = df1.index,
        orientation = "h",
        text = df1["percentage"],
        textposition = "outside",
        showlegend = False
    ),
    row = 1, col = 1
)

# Plot df2
fig.add_trace(
    go.Bar(
        x = df2["percentage"],
        y = df2.index,
        orientation = "h",
        text = df2["percentage"],
        textposition = "outside",
        showlegend = False
    ),
    row = 1, col = 2
)

# Layout tuning
fig.update_layout(
    height = 350,
    width = 1000,
    margin = dict(l = 40, 
                  r = 40, 
                  t = 40, 
                  b = 40),
    template = "plotly_white"
)

fig.show()