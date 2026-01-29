import plotly.graph_objects as go
import numpy as np

pi = np.pi

def generate_xy_linear_segment(a = 1, b = 1):
    # Original data: y = ax + b
    x_full = np.linspace(0, 1, 50)
    y_full = a * x_full + b

    return x_full, y_full

def generate_xy_circle(x0 = 0, y0 = 0, r = 1, R = 2):
    # Generate xy by polar-coordinate
    t = np.linspace(0, 2*pi, 201)
    x_full = x0 + R * np.cos(t)
    y_full = y0 + r * np.sin(t)

    return x_full, y_full

def generate_xy_heart():
    t = np.linspace(0, 2*pi, 201)
    
    # Parametric equation
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    
    # Scaling
    x = x / 16 * 5
    y = y / 13 * 5
    
    return x, y

def generate_xy_spiral(a = 0.1, n_round = 5):
    """
        
    """
    phi = (1 + np.sqrt(5)) / 2                  # golden ratio
    b = np.log(phi) / (np.pi / 2)               # growth factor
    
    theta = np.linspace(0, n_round * np.pi, 201)
    rho = a * np.exp(b * theta)

    x_full = rho * np.cos(theta)
    y_full = rho * np.sin(theta)    

    return x_full, y_full

def generate_xy_stars(inner_scale: float = 0.4, out_radius: float = 2.1, n_wings: int = 4):
    R = out_radius
    r = inner_scale * out_radius

    if n_wings % 2:
        t = np.linspace(0, 2*pi, n_wings*2, endpoint=False)
    else:
        t = np.linspace(-pi, pi, n_wings*2, endpoint=False)

    radius = np.where(np.arange(len(t)) % 2 == 0, R, r)
    x = radius * np.cos(t)
    y = radius * np.sin(t)
    
    # CLOSE the polygon by repeating the first point
    x_closed = np.concatenate([x, x[:1]])
    y_closed = np.concatenate([y, y[:1]])

    return x_closed, y_closed

def generate_xy_flowers(x0: float = 0, y0: float = 0, r_x: float = 0.6, r_y: float = 0.8, 
                        N: int = 20, core_tp: str = "cosine"):
    """
        Draw a generalized “flower” curve using cosine or sine modulation.

        Args:
            x0, y0 : float
                Center shift of the flower.
            r_x, r_y : float
                Amplitude in x and y directions.
            N : int
                Number of petals (frequency of modulation).
            core_tp : {"cosine", "sine"}
                Defines the modulation base function.

        Notes:
            - Uses modified polar-form equations.
            - Produces symmetric flower-like shapes.    
    """
    t = np.linspace(0, 2*pi, 501)
    # if core is cosine in the polar-coordinate
    if core_tp == "cosine":
        x = np.cos(t)*(x0 + r_x * np.cos(N * t))
        y = np.sin(t)*(y0 + r_y * np.cos(N * t))
    else:
        x = np.cos(t)*(x0 + r_x * np.sin(N * t))
        y = np.sin(t)*(y0 + r_y * np.sin(N * t))

    return x, y

def create_cumulative_animation_frames(x_full, y_full, marker_color='red', line_color='blue'):
    """
        Tạo list frames cho animation cumulative (điểm + đường nối dần dần)
        - x_full, y_full: mảng numpy đầy đủ tọa độ
        - Trả về: list[go.Frame]
    """
    frames = []
    for i in range(1, len(x_full) + 1):
        frames.append(go.Frame(
            data=[
                go.Scatter(
                    x=x_full[:i],
                    y=y_full[:i],
                    mode='markers',
                    marker=dict(size=10, color=marker_color, opacity=0.9)
                ),
                go.Scatter(
                    x=x_full[:i],
                    y=y_full[:i],
                    mode='lines',
                    line=dict(color=line_color, width=4)
                )
            ],
            name=str(i)
        ))
    return frames

def create_animated_figure(
    x_full, y_full,
    title="Cumulative Drawing Animation",
    xlim=None, ylim=None,
    marker_color='red', line_color='blue',
    duration = 30,  # ms mỗi frame
    width = 800, height=600,
    show_grid=True
):
    """
        Tạo figure Plotly hoàn chỉnh với animation cumulative
        - xlim, ylim: tuple (min, max) hoặc None → tự tính
    """
    if xlim is None:
        xlim = (x_full.min() - 0.1 * (x_full.max() - x_full.min()),
                x_full.max() + 0.1 * (x_full.max() - x_full.min()))
    if ylim is None:
        ylim = (y_full.min() - 0.1 * (y_full.max() - y_full.min()),
                y_full.max() + 0.1 * (y_full.max() - y_full.min()))

    frames = create_cumulative_animation_frames(x_full, y_full, marker_color, line_color)

    # Figure ban đầu: chỉ điểm đầu + đoạn đầu
    fig = go.Figure(
        data=[
            go.Scatter(x=[x_full[0]], y=[y_full[0]], mode='markers',
                       marker=dict(size=10, color=marker_color)),
            go.Scatter(x=[x_full[0]], y=[y_full[0]], mode='lines',
                       line=dict(color=line_color, width=4))
        ],
        layout = go.Layout(
            title = title,
            xaxis = dict(range=xlim, gridcolor='lightgray' if show_grid else None),
            yaxis = dict(range=ylim, gridcolor='lightgray' if show_grid else None,
                       scaleanchor="x", scaleratio=1),  # giữ tỷ lệ 1:1 nếu muốn
            width = width,
            height = height,
            paper_bgcolor = 'rgba(255,255,255,0.9)',
            plot_bgcolor = 'white',
            font = dict(color = 'black'),
            updatemenus=[{
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": duration, "redraw": True}, "fromcurrent": True}],
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate"}],
                        "label": "Pause",
                        "method": "animate"
                    }
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": False,
                "type": "buttons",
                "x": 0.1,
                "y": 0
            }],
            showlegend=False,
            margin=dict(l=40, r=40, t=60, b=40)
        ),
        frames=frames
    )

    return fig