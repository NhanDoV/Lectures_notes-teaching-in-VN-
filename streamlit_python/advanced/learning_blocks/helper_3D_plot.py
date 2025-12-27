import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

pi = np.pi

def plot_3d(category, shape):
    if category == "Khối chóp":
        return pyramid_dispatch(shape)

    elif category == "Khối trụ":
        return cylinder_dispatch(shape)

    elif category == "Khối hộp":
        return box_dispatch(shape)

    elif category == "Khối nón":
        return cone_dispatch(shape)

    elif category == "Khối cầu":
        return sphere_plot(shape)

    else:
        raise ValueError(f"Unknown 3D category: {category}")

# ============================= KHỐI CHÓP ================================ #
def pyramid_plot(base_points, apex, title="Khối chóp"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    faces = []

    # ----- base face -----
    faces.append(base_points)

    # ----- side faces -----
    n = len(base_points)
    for i in range(n):
        p1 = base_points[i]
        p2 = base_points[(i + 1) % n]
        faces.append([p1, p2, apex])

    poly = Poly3DCollection(
        faces,
        facecolors="lightblue",
        edgecolors="k",
        alpha=0.85
    )

    ax.add_collection3d(poly)

    # ----- axis setup -----
    all_points = np.vstack([base_points, apex])
    max_range = (all_points.max(axis=0) - all_points.min(axis=0)).max() / 2
    mid = all_points.mean(axis=0)

    ax.set_xlim(mid[0] - max_range, mid[0] + max_range)
    ax.set_ylim(mid[1] - max_range, mid[1] + max_range)
    ax.set_zlim(0, mid[2] + 2 * max_range)

    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()
    ax.set_title(title)

    return fig

def tetrahedron_plot():
    base = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0.5, np.sqrt(3)/2, 0]
    ])
    apex = np.array([0.5, np.sqrt(3)/6, np.sqrt(6)/3])

    return pyramid_plot(base, apex, title="Tetrahedron")

def triangular_pyramid_plot():
    base = np.array([
        [-1, -0.5, 0],
        [1, -0.5, 0],
        [0, 1, 0]
    ])
    apex = np.array([0, 0, 1.5])

    return pyramid_plot(base, apex, title="Triangular pyramid")

def square_pyramid_plot():
    base = np.array([
        [-1, -1, 0],
        [1, -1, 0],
        [1, 1, 0],
        [-1, 1, 0]
    ])
    apex = np.array([0, 0, 2])

    return pyramid_plot(base, apex, title="Square pyramid")

def pyramid_dispatch(shape):
    if shape == "Tứ diện":
        return tetrahedron_plot()
    elif shape == "Chóp tam giác":
        return triangular_pyramid_plot()
    elif shape == "Chóp tứ giác":
        return square_pyramid_plot()
    else:
        raise ValueError("Unknown pyramid shape")

# ============================== KHỐI TRỤ ================================ #
def prism_plot(base_points, height=2.0, title="Prism",
               facecolor="lightgreen", edgecolor="k"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    base = np.array(base_points)
    top = base.copy()
    top[:, 2] += height

    faces = []
    n = len(base)

    # ----- side faces -----
    for i in range(n):
        p1 = base[i]
        p2 = base[(i + 1) % n]
        p3 = top[(i + 1) % n]
        p4 = top[i]
        faces.append([p1, p2, p3, p4])

    # ----- bases -----
    faces.append(base)
    faces.append(top)

    poly = Poly3DCollection(
        faces,
        facecolors=facecolor,
        edgecolors=edgecolor,
        alpha=0.85
    )
    ax.add_collection3d(poly)

    # ----- scale -----
    all_pts = np.vstack([base, top])
    max_range = (all_pts.max(0) - all_pts.min(0)).max() / 2
    mid = all_pts.mean(0)

    ax.set_xlim(mid[0] - max_range, mid[0] + max_range)
    ax.set_ylim(mid[1] - max_range, mid[1] + max_range)
    ax.set_zlim(mid[2] - max_range, mid[2] + max_range)

    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()
    ax.set_title(title, fontsize=10)

    return fig

def circular_cylinder_plot(radius=1.0, height=2.0, n=50):
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    base = np.column_stack([
        radius * np.cos(theta),
        radius * np.sin(theta),
        np.zeros(n)
    ])

    # xanh dương cho hình trụ tròn
    return prism_plot(
        base,
        height,
        title="Circular cylinder",
        facecolor="#7fb3ff",   # light blue
        edgecolor="navy"
    )

def triangular_prism_plot(height=2.0):
    base = np.array([
        [-1, -0.6, 0],
        [ 1, -0.6, 0],
        [ 0,  1.0, 0]
    ])

    # xanh lá cho lăng trụ tam giác
    return prism_plot(
        base,
        height,
        title="Triangular prism",
        facecolor="#8ee08e",   # light green
        edgecolor="darkgreen"
    )

def cylinder_dispatch(shape):
    if shape == "Hình trụ đáy tròn":
        return circular_cylinder_plot()
    elif shape == "Hình lăng trụ tam giác":
        return triangular_prism_plot()
    else:
        raise ValueError("Unknown cylinder / prism type")

# ============================== KHỐI HỘP ================================ #
def box3d_plot(origin=(0, 0, 0), size=(2, 1.5, 1),
               title="Box", facecolor="lightcoral", edgecolor="k"):
    x0, y0, z0 = origin
    L, W, H = size

    # ----- 8 vertices -----
    V = np.array([
        [x0,   y0,   z0],
        [x0+L, y0,   z0],
        [x0+L, y0+W, z0],
        [x0,   y0+W, z0],
        [x0,   y0,   z0+H],
        [x0+L, y0,   z0+H],
        [x0+L, y0+W, z0+H],
        [x0,   y0+W, z0+H],
    ])

    # ----- faces -----
    faces = [
        [V[0], V[1], V[2], V[3]],  # bottom
        [V[4], V[5], V[6], V[7]],  # top
        [V[0], V[1], V[5], V[4]],  # front
        [V[1], V[2], V[6], V[5]],  # right
        [V[2], V[3], V[7], V[6]],  # back
        [V[3], V[0], V[4], V[7]],  # left
    ]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    poly = Poly3DCollection(
        faces,
        facecolors=facecolor,
        edgecolors=edgecolor,
        linewidths=1,
        alpha=0.85
    )
    ax.add_collection3d(poly)

    # ----- scaling -----
    max_range = max(L, W, H) / 2
    mid = V.mean(axis=0)

    ax.set_xlim(mid[0] - max_range, mid[0] + max_range)
    ax.set_ylim(mid[1] - max_range, mid[1] + max_range)
    ax.set_zlim(mid[2] - max_range, mid[2] + max_range)

    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()
    ax.set_title(title, fontsize=10)

    return fig

def rectangular_box_plot():
    # màu cam nhạt
    return box3d_plot(
        origin=(-1, -0.75, 0),
        size=(2.5, 1.5, 1),
        title="Rectangular box",
        facecolor="#ffb381",     # light orange
        edgecolor="saddlebrown"
    )

def cube_plot():
    # màu xanh dương nhạt
    return box3d_plot(
        origin=(-1, -1, -1),
        size=(2, 2, 2),
        title="Cube",
        facecolor="#88c9ff",     # light blue
        edgecolor="navy"
    )

def box_dispatch(shape):
    if shape == "Hình hộp chữ nhật":
        return rectangular_box_plot()
    elif shape == "Hình lập phương":
        return cube_plot()
    else:
        raise ValueError("Unknown box shape")

# ============================= KHỐI NÓN ================================= #
def cone_surface(r_bottom, r_top, height=3, n_theta=60, n_z=40):
    theta = np.linspace(0, 2*np.pi, n_theta)
    z = np.linspace(0, height, n_z)

    theta, z = np.meshgrid(theta, z)

    r = r_bottom + (r_top - r_bottom) * (z / height)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return x, y, z

def upright_cone_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    x, y, z = cone_surface(
        r_bottom=1.2,  # đáy
        r_top=0.0,     # đỉnh
        height=3
    )

    ax.plot_surface(x, y, z, cmap="Oranges", edgecolor="none", alpha=0.9)

    ax.set_title("Up-Right cone", fontsize=10)
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()

    return fig

def inverted_cone_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    x, y, z = cone_surface(
        r_bottom=1.2,
        r_top=0.0,
        height=3
    )

    z = -z 

    ax.plot_surface(
        x, y, z,
        cmap="Reds",      # upside-down cone
        edgecolor="none",
        alpha=0.9
    )

    ax.set_title("Inverted cone", fontsize=10)
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()

    return fig

def frustum_cone_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    x, y, z = cone_surface(
        r_bottom=1.4,
        r_top=0.6,
        height=2.5
    )

    ax.plot_surface(
        x, y, z,
        cmap="YlOrBr",    # frustum
        edgecolor="none",
        alpha=0.9
    )

    ax.set_title("Frustum of a cone", fontsize=10)
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()

    return fig

def cone_dispatch(shape):
    if shape == "Hình nón đứng":
        return upright_cone_plot()
    elif shape == "Hình nón úp":
        return inverted_cone_plot()
    elif shape == "Hình nón cụt (đứng)":
        return frustum_cone_plot()
    else:
        raise ValueError("Unknown cone shape")

# ============================== KHỐI CẦU ================================ #
def sphere_plot(shape):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # ===== parameters =====
    r = 1.0
    n_theta = 50
    n_phi = 50

    theta = np.linspace(0, pi, n_theta)
    phi = np.linspace(0, 2 * pi, n_phi)
    theta, phi = np.meshgrid(theta, phi)

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    if shape == "Hình cầu tiêu chuẩn":
        ax.plot_surface(
            x, y, z,
            cmap="Blues",
            edgecolor="none",
            alpha=0.9
        )
        # wireframe boundary
        ax.plot_wireframe(
            x, y, z,
            color="navy",
            linewidth=0.05
        )
        ax.set_title("Sphere", fontsize=10)

    elif shape == "Bán cầu":
        mask = z >= 0
        xm = np.where(mask, x, np.nan)
        ym = np.where(mask, y, np.nan)
        zm = np.where(mask, z, np.nan)

        ax.plot_surface(
            xm, ym, zm,
            cmap="Blues",
            edgecolor="none",
            alpha=0.9
        )
        ax.plot_wireframe(
            xm, ym, zm,
            color="navy",
            linewidth=0.02
        )
        ax.set_title("Hemisphere", fontsize=10)

    else:
        raise ValueError(f"Unknown sphere shape: {shape}")

    # aesthetics
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()

    return fig
