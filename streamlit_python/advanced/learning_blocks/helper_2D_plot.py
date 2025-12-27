import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from scipy.spatial import ConvexHull        # cho vẽ đa giác lồi

# Some global params
pi = np.pi

def plot_2d(category, shape):

    if category == "Tam giác":
        return triangle_plot(shape)
    
    elif category == "Tứ giác":
        return quad_plot(shape)
    
    elif category == "Đa giác":
        return random_polygon_plot(shape)
    
    elif category == "Hình tròn":
        return circle_plot(shape)
    
    else:
        raise ValueError("Unknown category")

# ======================= Quadrilateral's group ==============================
def gradient_fill_polygon(ax, vertices, cmap="Blues"):
    verts = np.array(vertices)
    x_min, y_min = verts.min(axis=0)
    x_max, y_max = verts.max(axis=0)

    n = 500
    x = np.linspace(x_min, x_max, n)
    y = np.linspace(y_min, y_max, n)
    X, Y = np.meshgrid(x, y)

    def dist_point_to_segment(px, py, x1, y1, x2, y2):
        vx, vy = x2 - x1, y2 - y1
        wx, wy = px - x1, py - y1
        c1 = vx * wx + vy * wy
        c2 = vx * vx + vy * vy
        t = np.clip(c1 / c2, 0, 1)
        proj_x = x1 + t * vx
        proj_y = y1 + t * vy
        return np.sqrt((px - proj_x)**2 + (py - proj_y)**2)

    # min distance tới mọi cạnh
    dist = np.full(X.shape, np.inf)
    for i in range(len(verts)):
        x1, y1 = verts[i]
        x2, y2 = verts[(i + 1) % len(verts)]
        d = dist_point_to_segment(X, Y, x1, y1, x2, y2)
        dist = np.minimum(dist, d)

    # mask ngoài polygon
    mask = Path(verts).contains_points(
        np.c_[X.ravel(), Y.ravel()]
    ).reshape(X.shape)

    dist[~mask] = np.nan
    dist /= np.nanmax(dist)

    ax.imshow(
        1 - dist,
        extent=(x_min, x_max, y_min, y_max),
        origin="lower",
        cmap=cmap,
        alpha=0.9
    )

def quad_plot(shape):
    fig, ax = plt.subplots()

    pad = 0.2  # padding quanh hình

    if shape == "Hình vuông":
        vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        color = "navy"
        cmap = "Blues"
        title = "Square"

    elif shape == "Hình chữ nhật":
        vertices = [(0, 0), (2, 0), (2, 1), (0, 1)]
        color = "darkgreen"
        cmap = "Greens"
        title = "Rectangle"

    elif shape == "Hình bình hành":
        vertices = [(0, 0), (2, 0), (2.6, 1), (0.6, 1)]
        color = "purple"
        cmap = "Purples"
        title = "Parallelogram"

    elif shape == "Hình thang cân":
        vertices = [(0.5, 0), (1.5, 0), (2, 1), (0, 1)]
        color = "darkorange"
        cmap = "Oranges"
        title = "Isosceles trapezoid"

    elif shape == "Hình thang":
        vertices = [(0.3, 0), (2.0, 0), (1.5, 1), (0, 1)]
        color = "brown"
        cmap = "Reds"
        title = "Trapezoid"

    elif shape == "Hình thang vuông":
        # đáy dưới nằm ngang, cạnh trái vuông góc
        vertices = [(0, 0), (2.0, 0), (1.5, 1), (0, 1)]
        color = "saddlebrown"
        cmap = "YlOrBr"
        title = "Right trapezoid"

    elif shape == "Hình thoi":
        # 4 cạnh bằng nhau, đối diện song song
        # tâm gần (0,0), đường chéo ngang dài hơn
        vertices = [(-1, 0), (0, 1.5), (1, 0), (0, -1.5)]
        color = "darkmagenta"
        cmap = "BuPu"
        title = "Rhombus"

    else:
        raise ValueError("Unknown quadrilateral")

    # Gradient fill
    gradient_fill_polygon(ax, vertices, cmap=cmap)

    # Boundary
    xs, ys = zip(*(vertices + [vertices[0]]))
    ax.plot(xs, ys, color=color, linewidth=2)

    # Padding theo bounding box đa giác
    xs_no_close, ys_no_close = zip(*vertices)
    xmin, xmax = min(xs_no_close), max(xs_no_close)
    ymin, ymax = min(ys_no_close), max(ys_no_close)

    x_range = xmax - xmin if xmax > xmin else 1
    y_range = ymax - ymin if ymax > ymin else 1

    ax.set_xlim(xmin - pad * x_range, xmax + pad * x_range)
    ax.set_ylim(ymin - pad * y_range, ymax + pad * y_range)

    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    ax.set_title(title, fontsize=10)

    return fig

# =========================== Polygon's group ==============================
def random_polygon_plot(kind):
    fig, ax = plt.subplots()

    n = np.random.randint(5, 13)

    if kind == "Đa giác đều":
        vertices = regular_polygon(n)
        title = f"Regular polygon ({n} sides)"
        edge_color = "navy"
        cmap = "Blues"
    else:
        vertices = random_convex_polygon(n)
        title = f"Convex polygon ({n} sides)"
        edge_color = "darkred"
        cmap = "Reds"

    # Gradient fill
    gradient_fill_polygon(ax, vertices, cmap=cmap)

    # Boundary
    xs, ys = zip(*(vertices + [vertices[0]]))
    ax.plot(xs, ys, color=edge_color, linewidth=2)

    # Padding
    pad = 0.2
    xs_no_close, ys_no_close = zip(*vertices)
    xmin, xmax = min(xs_no_close), max(xs_no_close)
    ymin, ymax = min(ys_no_close), max(ys_no_close)

    x_range = xmax - xmin if xmax > xmin else 1
    y_range = ymax - ymin if ymax > ymin else 1

    ax.set_xlim(xmin - pad * x_range, xmax + pad * x_range)
    ax.set_ylim(ymin - pad * y_range, ymax + pad * y_range)

    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    ax.set_title(title, fontsize=10)
    return fig

def regular_polygon(n, radius=1.0):
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    return [(radius*np.cos(a), radius*np.sin(a)) for a in angles]  

def random_convex_polygon(n, radius=1.0):
    # sinh nhiều điểm random trong đĩa tròn
    m = max(3*n, 20)  # sinh dư ra
    angles = np.random.rand(m) * 2 * np.pi
    radii = radius * np.sqrt(np.random.rand(m))
    points = np.column_stack([radii * np.cos(angles), radii * np.sin(angles)])

    hull = ConvexHull(points)
    hull_points = points[hull.vertices]  # thứ tự các đỉnh trên hull

    # nếu hull có nhiều hơn n đỉnh thì lấy mẫu ngẫu nhiên n đỉnh,
    # vẫn giữ thứ tự vòng quanh
    if len(hull_points) > n:
        idx = np.linspace(0, len(hull_points)-1, n, dtype=int)
        hull_points = hull_points[idx]

    return [tuple(p) for p in hull_points]

# ========================= Triangle's group =================================
def gradient_fill_triangle(ax, vertices, cmap="Blues"):
    verts = np.array(vertices)
    x_min, y_min = verts.min(axis=0)
    x_max, y_max = verts.max(axis=0)

    n = 400
    x = np.linspace(x_min, x_max, n)
    y = np.linspace(y_min, y_max, n)
    X, Y = np.meshgrid(x, y)

    # Function tính khoảng cách điểm → cạnh
    def dist_point_to_line(px, py, x1, y1, x2, y2):
        return np.abs((y2 - y1)*px - (x2 - x1)*py + x2*y1 - y2*x1) / \
               np.sqrt((y2 - y1)**2 + (x2 - x1)**2)

    d1 = dist_point_to_line(X, Y, *verts[0], *verts[1])
    d2 = dist_point_to_line(X, Y, *verts[1], *verts[2])
    d3 = dist_point_to_line(X, Y, *verts[2], *verts[0])

    dist = np.minimum(np.minimum(d1, d2), d3)

    # Mask ngoài tam giác
    from matplotlib.path import Path
    mask = Path(verts).contains_points(
        np.c_[X.ravel(), Y.ravel()]
    ).reshape(X.shape)

    dist[~mask] = np.nan
    dist /= np.nanmax(dist)

    ax.imshow(
        1 - dist,
        extent=(x_min, x_max, y_min, y_max),
        origin="lower",
        cmap=cmap,
        alpha=0.9
    )

def triangle_plot(shape):
    fig, ax = plt.subplots()

    pad = 0.2  # padding chung cho mọi loại tam giác

    if shape == "Tam giác đều":
        h = np.sqrt(3) / 2
        vertices = [(-0.5, 0), (0.5, 0), (0, h)]

        # Gradient fill - xanh dương
        gradient_fill_triangle(ax, vertices, cmap="Blues")

        xs, ys = zip(*(vertices + [vertices[0]]))
        ax.plot(xs, ys, color="navy", linewidth=2)
        ax.set_title("Equilateral triangle", fontsize=10)

    elif shape == "Tam giác vuông":
        vertices = [(0, 5), (12, 0), (0, 0)]

        # Gradient fill - xanh lá
        gradient_fill_triangle(ax, vertices, cmap="Greens")

        xs, ys = zip(*(vertices + [vertices[0]]))
        ax.plot(xs, ys, color="darkgreen", linewidth=2)
        ax.set_title("Right triangle", fontsize=10)

    elif shape == "Tam giác vuông cân":
        vertices = [(0, 0), (1, 1), (2, 0)]

        # Gradient fill - cam
        gradient_fill_triangle(ax, vertices, cmap="Oranges")

        xs, ys = zip(*(vertices + [vertices[0]]))
        ax.plot(xs, ys, color="darkorange", linewidth=2)
        ax.set_title("Isosceles right triangle", fontsize=10)

    elif shape == "Tam giác cân":
        vertices = [(0, 0), (1, 2.2), (2, 0)]

        # Gradient fill - tím
        gradient_fill_triangle(ax, vertices, cmap="Purples")

        xs, ys = zip(*(vertices + [vertices[0]]))
        ax.plot(xs, ys, color="indigo", linewidth=2)
        ax.set_title("Isosceles triangle", fontsize=10)

    else:
        vertices = [(0, 0), (2.5, 1), (1.8, 0)]

        # Gradient fill - đỏ
        gradient_fill_triangle(ax, vertices, cmap="Reds")

        xs, ys = zip(*(vertices + [vertices[0]]))
        ax.plot(xs, ys, color="darkred", linewidth=2)
        ax.set_title("Scalene triangle", fontsize=10)

    # Apply padding theo bounding box của tam giác
    xs_no_close, ys_no_close = zip(*vertices)
    xmin, xmax = min(xs_no_close), max(xs_no_close)
    ymin, ymax = min(ys_no_close), max(ys_no_close)

    x_range = xmax - xmin if xmax > xmin else 1
    y_range = ymax - ymin if ymax > ymin else 1

    ax.set_xlim(xmin - pad * x_range, xmax + pad * x_range)
    ax.set_ylim(ymin - pad * y_range, ymax + pad * y_range)

    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    return fig

# ========================== Circle's group ==================================
def radial_gradient_circle(ax, r=1.0, cmap="Blues"):
    n = 400
    x = np.linspace(-r, r, n)
    y = np.linspace(-r, r, n)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)

    gradient = np.clip(R / r, 0, 1)
    gradient[R > r] = np.nan  # mask ngoài hình tròn

    ax.imshow(
        gradient,
        extent=(-r, r, -r, r),
        origin="lower",
        cmap=cmap,
        alpha=0.9
    )

def circle_plot(shape):
    fig, ax = plt.subplots()

    if shape == "Hình tròn (tiêu chuẩn)":
        r = 1.0
        t = np.linspace(0, 2 * pi, 1000)
        radial_gradient_circle(ax, r=r, cmap="Blues")
        ax.plot(r*np.cos(t), r*np.sin(t), color="navy", linewidth=2)
        ax.set_title("Circle", fontsize=10)

        pad = 0.1                       # thụt hình vô trong
        ax.set_xlim(-1 - pad, 1 + pad)
        ax.set_ylim(-1 - pad, 1 + pad)

    elif shape == "Bán nguyệt":
        r = 1.0
        t = np.linspace(0, pi, 1000)
        radial_gradient_circle(ax, r=r, cmap="Greens")
        ax.set_ylim(0, r)
        ax.plot(r*np.cos(t), r*np.sin(t), color="darkgreen", linewidth=2)
        ax.plot([-r, r], [0, 0], color="darkgreen", linewidth=2)
        ax.set_title("Semicircle", fontsize=12)

        pad = 0.1
        ax.set_xlim(-1 - pad, 1 + pad)
        ax.set_ylim(0, 1 + pad)

    elif shape == "Hình vành khăn":
        r1, r2 = 1.0, 0.6
        t = np.linspace(0, 2 * pi, 1000)
        radial_gradient_circle(ax, r=r1, cmap="Oranges")
        circle = plt.Circle((0, 0), r2, color="white", zorder=10)
        ax.add_patch(circle)
        ax.plot(r1*np.cos(t), r1*np.sin(t), color="darkorange", linewidth=2)
        ax.plot(r2*np.cos(t), r2*np.sin(t), color="darkorange", linewidth=2)
        ax.set_title("Annulus", fontsize=10)

        pad = 0.05
        ax.set_xlim(-1 - pad, 1 + pad)
        ax.set_ylim(-1 - pad, 1 + pad)

    ax.set_aspect("equal")
    ax.axis("off")
    return fig