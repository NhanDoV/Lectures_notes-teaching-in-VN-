import scipy.stats as sts, numpy as np
import matplotlib.pyplot as plt, matplotlib.patches as patches
from matplotlib.patches import Arc, Wedge, FancyArrowPatch
import streamlit as st, seaborn as sns
import plotly.graph_objects as go
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

pi = np.pi
# =========================================================================================================================================== #
#                                                            FUNCTIONS OF CHART - ILLUSTRATION                                                #
# =========================================================================================================================================== #
#                                                               1. HINH HOC (minh hoa)                                                        #
# =========================================================================================================================================== #
def cube_inside_cube_plot():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), subplot_kw={'projection': '3d'}, gridspec_kw={'width_ratios': [2, 3]})

    # Left window (Cube and Octahedron)
    ax = axes[0]

    # Draw first cube
    vertices = [ (-1, -1, -1), ( 1, -1, -1), ( 1,  1, -1), (-1,  1, -1),
                (-1, -1,  1), ( 1, -1,  1), ( 1,  1,  1), (-1,  1,  1) 
            ]    
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Các cạnh của mặt dưới
        [4, 5], [5, 6], [6, 7], [7, 4],  # Các cạnh của mặt trên
        [0, 4], [1, 5], [2, 6], [3, 7]   # Các cạnh nối giữa mặt dưới và mặt trên
    ]

    for edge in edges:
        ax.plot([vertices[edge[0]][0], vertices[edge[1]][0]], 
                [vertices[edge[0]][1], vertices[edge[1]][1]], 
                [vertices[edge[0]][2], vertices[edge[1]][2]], color='blue')
            
    vertices_array = np.array(vertices)
    ax.scatter3D(vertices_array[:, 0], vertices_array[:, 1], vertices_array[:, 2], color='red')
    faces = [
        [0, 1, 2, 3],  # Mặt dưới
        [4, 5, 6, 7],  # Mặt trên
        [0, 1, 5, 4],  # Mặt trước
        [2, 3, 7, 6],  # Mặt sau
        [1, 2, 6, 5],  # Mặt phải
        [4, 7, 3, 0]   # Mặt trái
    ]    
    for face in faces:
        ax.add_collection3d(Poly3DCollection([np.array([vertices[vertice] for vertice in face])], 
                                            facecolors='cyan', linewidths=1, edgecolors='blue', alpha=.15))

    labels = ['A', 'B', 'C', 'D', 'A\'', 'B\'', 'C\'', 'D\'']
    for i, label in enumerate(labels):
        ax.text(vertices[i][0]*1.1, vertices[i][1]*1.1, vertices[i][2]*1.2, label, color='black', fontsize=12, fontweight='bold')


    # Vẽ khối thứ 2: octahedron
    vertices_octahedron = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)] 
    labels = [r'$I_1$', r'$I_2$', r'$I_3$', r'$I_4$', r'$I_5$', r'$I_6$']
    for i, label in enumerate(labels):
        ax.text(vertices_octahedron[i][0]*1.2, vertices_octahedron[i][1]*1.2, vertices_octahedron[i][2]*1.2, 
                label, color='blue', fontsize=10)  # Hiển thị văn bản đậm
    faces_octahedron = [
        [3, 4, 0],  # Mặt I4-I5-I1
        [3, 1, 5],  # Mặt I4-I2-I6
        [0, 1, 5],  # Mặt I4-I1-I6
        [0, 1, 4],  # Mặt I4-I2-I5
        [2, 4, 0],  # Mặt I3-I5-I1
        [2, 1, 5],  # Mặt I3-I2-I6
        [0, 2, 5],  # Mặt I3-I1-I6
        [0, 2, 4],  # Mặt I3-I2-I5
    ]

    # Vẽ các mặt của khối bát diện với màu xanh lá nhạt
    for face in faces_octahedron:
        ax.add_collection3d(Poly3DCollection([np.array([vertices_octahedron[vertice] for vertice in face])],
                                            facecolors='lightgreen', linestyle=':', linewidths=1, edgecolors='green', alpha=0.5))
    # Hiển thị các đỉnh
    vertices_octahedron_array = np.array(vertices_octahedron)
    ax.scatter3D(vertices_octahedron_array[:, 0], vertices_octahedron_array[:, 1], vertices_octahedron_array[:, 2], color='black')
    # Kết nối từ I4 đến các điểm I1, I2, I5, I6 bằng nét đứt

    edges_to_I4 = [0, 1, 4, 5]

    for idx, target in enumerate(edges_to_I4):
        ax.plot([vertices_octahedron[3][0], vertices_octahedron[target][0]], 
                [vertices_octahedron[3][1], vertices_octahedron[target][1]], 
                [vertices_octahedron[3][2], vertices_octahedron[target][2]], 
                color='green', linestyle='-', linewidth=2)  # Nét đứt màu xanh lá
        if idx in [0, 4]:
            ax.plot([vertices_octahedron[2][0], vertices_octahedron[target][0]], 
                    [vertices_octahedron[2][1], vertices_octahedron[target][1]], 
                    [vertices_octahedron[2][2], vertices_octahedron[target][2]], 
                    color='green', linestyle='-', linewidth=2)  # Nét đứt màu xanh lá
        else:
            ax.plot([vertices_octahedron[2][0], vertices_octahedron[target][0]], 
                    [vertices_octahedron[2][1], vertices_octahedron[target][1]], 
                    [vertices_octahedron[2][2], vertices_octahedron[target][2]], 
                    color='green', linestyle='--', linewidth=1)  # Nét đứt màu xanh lá
            
    ax.add_collection3d(Poly3DCollection([np.array([vertices_octahedron[vertice] for vertice in [1, 5, 0, 4]])],
                                        facecolors='red', linewidths=1, edgecolors='green', alpha=0.2))

    for i in range(len(edges_to_I4)):
        for j in range(i + 1, len(edges_to_I4)):
            ax.plot([vertices_octahedron[edges_to_I4[i]][0], vertices_octahedron[edges_to_I4[j]][0]], 
                [vertices_octahedron[edges_to_I4[i]][1], vertices_octahedron[edges_to_I4[j]][1]], 
                [vertices_octahedron[edges_to_I4[i]][2], vertices_octahedron[edges_to_I4[j]][2]], 
                color='red', linestyle=':', linewidth=2)  # Nét đứt (dotted line)
    ax.set_axis_off()

    ax2 = axes[1]
    vertices = np.array([
        [1, 0, 0],   # Đỉnh 1
        [-1, 0, 0],  # Đỉnh 2
        [0, 1, 0],   # Đỉnh 3
        [0, -1, 0],  # Đỉnh 4
        [0, 0, 1],   # Đỉnh 5 (chóp trên)
        [0, 0, -1]   # Đỉnh 6 (chóp dưới)
    ])

    # Các mặt của khối bát diện (8 mặt tam giác)
    faces = [
        [0, 2, 4], [0, 3, 4], [0, 1, 4], [1, 3, 4],  # Các mặt chóp trên
        [0, 2, 5], [0, 3, 5], [0, 1, 5], [1, 3, 5]   # Các mặt chóp dưới
    ]

    # Vẽ các mặt của khối bát diện vào ax2
    ax2.add_collection3d(Poly3DCollection([vertices[face] for face in faces], 
                                        facecolors='cyan', linestyle=':', linewidths=1, edgecolors='r', alpha=.25))
    vertices_cube = np.array([
        [ 1/3,  1/3,  1/3],
        [ 1/3, -1/3,  1/3],
        [-1/3, -1/3,  1/3],
        [-1/3,  1/3,  1/3],
        [ 1/3,  1/3, -1/3],
        [ 1/3, -1/3, -1/3],
        [-1/3, -1/3, -1/3],
        [-1/3,  1/3, -1/3]
    ])

    cube_faces = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 1, 5, 4],
        [2, 3, 7, 6],
        [0, 3, 7, 4],
        [1, 2, 6, 5]
    ]
    # Vẽ các mặt của hình lập phương (cube) bên trong
    for face in cube_faces:
        ax2.add_collection3d(Poly3DCollection([vertices_cube[face]], 
                                            facecolors='violet', linewidths=1, edgecolors='yellow', alpha=0.5))

    # Cài đặt giới hạn trục và tỷ lệ đồng đều
    centroids = np.array([np.mean(vertices[face], axis=0) for face in faces])
    cube_vertices = np.array(centroids)                        
    all_points = np.vstack([vertices, centroids, cube_vertices])

    # Tính phạm vi cực đại của tất cả các tọa độ
    x_min, y_min, z_min = np.min(all_points, axis=0)
    x_max, y_max, z_max = np.max(all_points, axis=0)

    # Tính chiều dài của chiều dài trục (để giữ tỷ lệ chính xác)
    max_range = max(x_max - x_min, y_max - y_min, z_max - z_min)

    # Cập nhật giới hạn trục sao cho hiển thị toàn bộ khối
    ax2.set_xlim([x_min - max_range * 0.1, x_max + max_range * 0.1])
    ax2.set_ylim([y_min - max_range * 0.1, y_max + max_range * 0.1])
    ax2.set_zlim([z_min - max_range * 0.1, z_max + max_range * 0.1])

    # Giữ tỷ lệ đồng đều cho các trục
    ax2.set_box_aspect([1, 1, 1])  # Giữ tỷ lệ đồng đều

    # Tắt hiển thị trục
    ax2.set_axis_off()
    
    return fig

def illustration_hinh_hoc_3_hard():
    AB, AC, BC = 45, 60, 75
    AH = AB*AC / BC
    BH = np.sqrt(AB**2 - AH**2)
    CH = BC - BH
    A, B, C, H, D, Da = ((0, AH), (-BH, 0), (CH, 0), (0, 0), (10, 16), (10, 0))
    fig, ax = plt.subplots()
    
    # Danh sách các điểm và nhãn
    points = {'A': A, 'B': B, 'C': C, 'H': H, 'D': D, 'D_a': Da}
    
    def distance_point_to_line(px, py, x1, y1, x2, y2):
        # Tính các hệ số của phương trình đường thẳng AB: A*x + B*y + C = 0
        A_line = y2 - y1
        B_line = x1 - x2
        C_line = x2 * y1 - y2 * x1

        # Tính tọa độ điểm vuông góc từ (px, py) đến đường thẳng
        denominator = A_line**2 + B_line**2
        xv = (B_line * (B_line * px - A_line * py) - A_line * C_line) / denominator
        yv = (A_line * (-B_line * px + A_line * py) - B_line * C_line) / denominator

        return (xv, yv)

    Db = distance_point_to_line(D[0], D[1], A[0], A[1], B[0], B[1])
    Dc = distance_point_to_line(D[0], D[1], A[0], A[1], C[0], C[1])
    
    # re defined
    points = {'A': A, 'B': B, 'C': C, 'H': H, 'D': D, 'D_a': Da, 'D_b': Db, 'D_c': Dc}
    
    # Vẽ các điểm và hiển thị tọa độ
    for label, point in points.items():
        ax.plot(*point, 'o', label=r"${label}$")  # Vẽ điểm
        ax.text(point[0], point[1], f"${label}$", fontsize=12, 
            verticalalignment='bottom' if label != 'A' else 'bottom',
            horizontalalignment='right' if label == 'A' else 'left')    # Hiển thị tọa độ
        
    ax.plot([A[0], B[0]], [A[1], B[1]], 'b-')
    ax.plot([A[0], C[0]], [A[1], C[1]], 'b-')
    ax.plot([B[0], C[0]], [B[1], C[1]], 'b-')

    ax.plot([D[0], Da[0]], [D[1], Da[1]], 'g:')
    ax.plot([D[0], Db[0]], [D[1], Db[1]], 'g:')
    ax.plot([D[0], Dc[0]], [D[1], Dc[1]], 'g:')
                            
    ax.plot([A[0], 0], [A[1], 0], 'r--')
    ax.set_axis_off()
    
    return fig

def illustration_hinh_hoc_2_medium():
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Các đỉnh của lập phương (các điểm trong không gian 3D)
    vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], 
                        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

    # Các mặt của lập phương (dùng chỉ số của các đỉnh)
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # Mặt dưới
        [vertices[4], vertices[5], vertices[6], vertices[7]],  # Mặt trên
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # Mặt phía trước
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # Mặt phía sau
        [vertices[0], vertices[3], vertices[7], vertices[4]],  # Mặt trái
        [vertices[1], vertices[2], vertices[6], vertices[5]]   # Mặt phải
    ]

    # Vẽ các mặt
    ax.add_collection3d(Poly3DCollection(faces, facecolors='skyblue', linewidths=0.5, edgecolors='g', alpha=.2))

    # Vẽ vết nứt
    ax.plot([0, 0], [1, 1], [0, 1], color='red', linestyle=':', linewidth=2)
    ax.plot([0, 0], [0, 1], [0, 0], color='red', linestyle=':', linewidth=2)
    ax.plot([0, 1], [1, 1], [0, 0], color='red', linestyle=':', linewidth=2)

    # Đặt tên cho các trục và các giới hạn
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])
    ax.set_axis_off()
    
    return fig

def illustration_hinh_hoc_1_medium():

    # Hàm tính trọng tâm của tam giác với 3 đỉnh
    def centroid(A, B, C):
        return (A + B + C) / 3

    # Định nghĩa các đỉnh của tứ diện
    A = np.array([1, 1, 1])
    B = np.array([1, -1, -1])
    C = np.array([-1, 1, -1])
    D = np.array([-1, -1, 1])

    # Tạo danh sách các mặt của tứ diện
    faces = [[A, B, C], [A, B, D], [A, C, D], [B, C, D]]

    # Tính các trọng tâm của mỗi mặt
    centroids = [centroid(f[0], f[1], f[2]) for f in faces]

    # Vẽ tứ diện và các trọng tâm
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ các mặt của tứ diện
    for face in faces:
        x = [v[0] for v in face]
        y = [v[1] for v in face]
        z = [v[2] for v in face]
        ax.plot_trisurf(x, y, z, color='cyan', alpha=0.3)

    # Vẽ các trọng tâm
    for centroid_point in centroids:
        ax.scatter(centroid_point[0], centroid_point[1], centroid_point[2], color='red', s=10)

    # Nối các trọng tâm bằng các đoạn thẳng đứt
    for i in range(len(centroids)):
        for j in range(i + 1, len(centroids)):
            ax.plot([centroids[i][0], centroids[j][0]],
                    [centroids[i][1], centroids[j][1]],
                    [centroids[i][2], centroids[j][2]], 'k--')

    points = {'A': A, 'B': B, 'C': C, 'D': D}
    centroid_points = {'M': centroids[0], 'N': centroids[1], 'P': centroids[2], 'Q': centroids[3]}

    # Hiển thị tên các điểm ngoài và các trọng tâm
    for label, point in points.items():
        ax.scatter(point[0], point[1], point[2], color='red', s=30)
        ax.text(point[0] + 0.1, point[1] + 0.1, point[2] + 0.2, label, fontsize=12, color='black')

    for label, centroid_point in centroid_points.items():
        ax.scatter(centroid_point[0], centroid_point[1], centroid_point[2], color='blue', s=10)
        ax.text(centroid_point[0] + 0.05, centroid_point[1]+ 0.05, centroid_point[2]+ 0.05, label, fontsize=12, color='black')                        
        
    # Thiết lập các labels cho trục
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_axis_off()
    
    return fig

def illustration_hinh_hoc_1_easy():
    AB, AC, BC = 6, 8 ,10
    AH = AB*AC / BC
    BH = np.sqrt(AB**2 - AH**2)
    CH = 10 - BH
    A, B, C, H = ((0, AH), (-BH, 0), (CH, 0), (0, 0))
    fig, ax = plt.subplots()
    
    # Danh sách các điểm và nhãn
    points = {'A': A, 'B': B, 'C': C, 'H': H}

    # Vẽ các điểm và hiển thị tọa độ
    for label, point in points.items():
        ax.plot(*point, 'o', label=r"${label}$")  # Vẽ điểm
        ax.text(point[0], point[1], f"${label}$", fontsize=12, 
            verticalalignment='bottom' if label != 'A' else 'bottom',
            horizontalalignment='right' if label == 'A' else 'left')    # Hiển thị tọa độ
        
    ax.plot([A[0], B[0]], [A[1], B[1]], 'b-')
    ax.plot([A[0], C[0]], [A[1], C[1]], 'b-')
    ax.plot([B[0], C[0]], [B[1], C[1]], 'b-')
    ax.plot([A[0], 0], [A[1], 0], 'r--')
    ax.set_axis_off()
    
    return fig
    
def illustration_hinh_hoc_2_hard():
    def plot_cone(ax, height, angle, num_points=100):
        # Tính bán kính đáy của hình nón
        radius = height * np.tan(angle)
        
        # Tạo lưới cho góc và chiều cao của hình nón
        z = np.linspace(0, height, num_points)  # Đỉnh ở trên, đáy dưới
        theta = np.linspace(0, 2*np.pi, num_points)
        
        # Tạo lưới 2 chiều cho tọa độ x và y
        Z, Theta = np.meshgrid(z, theta)
        R = radius * (1 - Z / height)  # Tỉ lệ bán kính từ đỉnh xuống đáy
        X = R * np.cos(Theta)
        Y = R * np.sin(Theta)
        
        # Lật ngược hình nón bằng cách đảo ngược trục Z
        Z = height - Z  # Đảo ngược trục Z (đỉnh hướng lên trên, đáy xuống dưới)
        
        # Vẽ mặt nón rỗng (không có mặt đáy) với màu sắc
        ax.plot_surface(X, Y, Z, color='b', alpha=0.5, rstride=20, cstride=20)  # Giảm độ chi tiết lưới để màu sắc dễ nhìn hơn
        
        R = 3.5
        ax.quiver(-R, -R, 8, 0, 0, 1, color='red', length=2, alpha=0.5)
        ax.quiver(-R, -R, 6, 0, 0, 1, color='red', length=2, alpha=0.4)    
        ax.quiver(-R, -R, 4, 0, 0, -1, color='red', length=2, alpha=0.4)    
        ax.quiver(-R, -R, 2, 0, 0, -1, color='red', length=2, alpha=0.5)
        ax.text(-R-1, -R, 5, r'height of cone: $h$', fontsize=9)

        ax.text(0, radius, height, r'water filled rate $k$', color='blue', alpha=0.8)
        ax.quiver(0, radius, height, -0.25, -0.25, -1, color='blue', length=1.0, alpha=0.5)
        ax.quiver(1, radius, height, 0, 0, -1, color='blue', length=1.0, alpha=0.5)
        
        ax.plot([0, radius], [0, 0], [height, 0], color='r', linestyle=':', lw=1)  # Đoạn thẳng tạo góc với trục Z
        ax.plot([0, 0], [0, 0], [height, 0], color='r', linestyle=':', lw=1)    
        ax.text(radius * -0.25, -1, height * 1.05, r'$\theta = \arctan \frac{1}{2}$', color='black', fontsize=12)  

        ax.plot([0, -R], [0, -R], [0, 0], color='violet', linestyle='--', lw=1)
        ax.plot([-R], [-R], [0], 'ro', alpha=0.3, markersize=3)
        ax.plot([-1, -R/2], [0, -R/2], [-1.5, 0], color='black', linestyle='-', lw=1, alpha=0.4)
        ax.text(-1, 0, -2, r"radius.cone: $R$", color='black', fontsize=10)

    def plot_random_point_on_cone(ax, height, angle, z_value, num_points=100):
        # Tính bán kính tương ứng với chiều cao z_value
        radius = height * np.tan(angle)
        R = radius * (1 - z_value / height)
        
        # Tính tọa độ của điểm trên mặt nón, chọn một góc ngẫu nhiên
        theta = 6.11331 # np.random.uniform(0, 2*np.pi)
        x = R * np.cos(theta)
        y = R * np.sin(theta)
        z = z_value  # Giá trị chiều cao của điểm trên mặt nón
        
        # Vẽ điểm trên đồ thị
        ax.plot([x, 3.5], [y, y], [z, z*1.2], color='violet', linestyle='--', lw=1)
        ax.text(3.5, y, z*1.2, 'spider', color='red', fontsize=12)
        ax.text(3, 3, 3, r"spider-speed = $u$", color='darkgreen', fontsize=10)
        
        ax.plot([x, x], [y, y], [0, z], color='blue', linestyle='--', alpha=0.75)
        ax.plot([0, 2*x], [0, y], [0, 0], color='violet', linestyle='--', alpha=0.5)        
        ax.text(2.5, 0, z/4, r'$h_0$', color='blue', fontsize=10)
        ax.plot([x], [y], [z], 'bo', alpha=0.6)  
        ax.plot([0], [0], [0], 'ro', alpha=0.3, markersize=3)
        
    # Khởi tạo đồ thị với DPI cao hơn
    fig = plt.figure(figsize=(8, 8), dpi=100)  # Tăng DPI tại đây
    ax = fig.add_subplot(111, projection='3d')

    # Tham số cho hình nón
    height = 10  # chiều cao hình nón
    angle = np.arctan(0.5)  # góc bán phương (arctan(0.5))

    # Vẽ hình nón ngược
    plot_cone(ax, height, angle)
    plot_random_point_on_cone(ax, height, angle, z_value=5)

    # Cài đặt hiển thị đồ thị
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([1, 1, 1])  # Giữ tỷ lệ đồng đều giữa các trục
    # ax.set_axis_off()

    return fig

def illustration_hinh_hoc_2_hard_projection():
    fig, ax = plt.subplots(1, 1, figsize=(10, 4), dpi=100)
    ax.plot([0, 6], [0, 0], color="darkblue", alpha=0.8)
    ax.plot([0, 0], [3, 0], color="darkblue", alpha=0.8)
    ax.plot([0, 6], [3, 0], color="darkblue", alpha=0.9)
    ax.text(0.1, 2.2, r"$ \theta = \arctan \frac{1}{2}$", color="blue", fontsize=10)
    ax.text(-0.5, 1.4, "$h$: height", color="darkgreen", fontsize=9)
    ax.text(2.8, 0.1, "$R$: radius", color="red", fontsize=10)

    arc = Arc((0, 3), 0.5, 0.5, angle=0, theta1=270, theta2=330, color="purple", linewidth=1)
    wedge = Wedge(center=(0, 3), r=0.45, theta1=270, theta2=332, facecolor="purple", edgecolor="black")
    ax.add_patch(wedge)
    ax.add_patch(arc)
    ax.set_axis_off()
    
    return fig

def rule_of_2015_exponent():
    fig, ax = plt.subplots(1, 2, figsize=(10, 4.5), dpi=100)
    ax[0].plot([0, 2], [2, 0], color='blue', lw=2)
    ax[0].plot([0, 2], [0, 2], color='blue', lw=2)
    ax[0].set_axis_off()
    ax[0].text(0.7, -0.25, "cycle 4 (for d in 1-4)")
    ax[0].text(0.92, 1.2, "$d=1$", color="red", fontsize=9)
    ax[0].text(0.88, 1.8, "$f^d_4 : 2015$", color="red", fontsize=12)
    ax[0].text(1.2, 1, "$d=2$", color="darkblue", fontsize=9)
    ax[0].text(1.7, 1, "$f^d_4 : 0225$", color="darkblue", fontsize=12)
    ax[0].text(0.92, 0.7, "$d=3$", color="darkgreen", fontsize=9)
    ax[0].text(0.88, 0.2, "$f^d_4 : 3375$", color="darkgreen", fontsize=12)
    ax[0].text(0.6, 1, "$d=4$", color="purple", fontsize=9)
    ax[0].text(0., 1, "$f^d_4 : 0625$", color="purple", fontsize=12)
    c1 = plt.Circle((1, 1), 1, fill=True, color='violet', alpha=0.3)
    ax[0].add_artist(c1)

    ax[1].plot([-2, 2], [0, 0], color='white', lw=1)
    ax[1].plot([0, 0], [-2, 2], color='blue', lw=2)
    ax[1].text(-0.7, -2.5, "cycle 2 (for $d \geq 5$)")
    ax[1].text(0.5, 0.5, '\t$d$ odd \n (e.g, 5,7,etc.)', color="darkblue", fontsize=9)
    ax[1].text(-1.5, -0.5, '$f^d_4 : 0625$', color="darkgreen", fontsize=12)
    ax[1].text(-1.5, 0.5, '\t$d$ even \n (e.g, 6,8,etc.)', color="darkgreen", fontsize=9)
    ax[1].text(0.5, -0.5, '$f^d_4 : 9325$', color="darkblue", fontsize=12)
    ax[1].set_axis_off()
    c2 = plt.Circle((0, 0), 1.5, fill=True, color='violet', alpha=0.3)
    ax[1].add_artist(c2)
    fig.suptitle("rule of the last 4 digits of 2015's exponent or \n $f^d_4 =$ last_4_digits of $2015^d$",y=1.1)
    
    return fig
    
# =========================================================================================================================================== #
#                                                               2. SO HOC (minh hoa)                                                          #  
# =========================================================================================================================================== #
def illustration_numeric_serial_1_easy():
    ns = list(np.linspace(2, 100, 99)) + [1e2, 1e3, 1e5, 1e10]
    an = [(1 - 1/n)**n for n in ns]
    fig, ax = plt.subplots()                     
    ax.plot(ns, an, label = r'$y=a_n$')
    ax.axhline(y=1/np.e, color='r', linestyle='--', label=r"$y = \dfrac{1}{e}$" ,linewidth=1)
    ax.set_xscale('log') 
    ax.set_xlabel("log(n)")
    ax.set_ylabel(r"$a_n = \left( 1 - \frac{1}{n} \right)^n$")                            
    ax.legend()
    
    return fig

def illustration_numeric_serial_1_medium():
    def my_func(n):
        n = int(n)
        S = np.sqrt(3)
        for _ in range(1, n):
            next_S = np.sqrt(3 * S)
            if abs(next_S - S) < 1e-6:  # Ngưỡng sai số đủ nhỏ (tùy chỉnh)
                break
            S = next_S
        return S
    
    ns = list(np.linspace(1, 20, 19))
    an = [my_func(n) for n in ns]
    fig, ax = plt.subplots()  
    ax.plot(ns, an, label=r"$y = a_n$")
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"$a_n = \sqrt{3 * \sqrt{3 * ... * \sqrt{3}}} $")
    ax.axhline(y=3, color='r', linestyle='--', label=r"$y=3$")
    ax.legend()
    
    return fig

def illustration_numeric_serial_1_hard():
    def my_func(n):
        n = int(n)
        S = 1 / 2
        for _ in range(1, n):
            next_S = 1 / (1 + S)
            # Nếu sự thay đổi giữa các giá trị quá nhỏ, dừng lại để tiết kiệm thời gian
            if abs(next_S - S) < 1e-6:  # Ngưỡng sai số đủ nhỏ (tùy chỉnh)
                break
            S = next_S
        return S
    
    ns = list(np.linspace(1, 20, 19))
    an = [my_func(n) for n in ns]
    fig, ax = plt.subplots()  
    ax.plot(ns, an, label=r"$y = a_n$")
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"$a_n = \frac{1}{1 + \frac{1}{1+\frac{1}{ 1 + \frac{1}{1 + ...} }}} $")
    ax.axhline(y=(-1 + np.sqrt(5)) / 2, color='r', linestyle='--', label=r"$y=\dfrac{-1+\sqrt{5}}{2}$")
    ax.legend()
    
    return fig
    
def illustration_numeric_serial_2_hard():
    def my_func(n):
        n = int(n)
        S = np.sqrt(3)  # Bắt đầu với giá trị căn bậc hai của 3
        for _ in range(1, n):
            next_S = np.sqrt(3 + S)
            # Nếu sự thay đổi giữa các giá trị quá nhỏ, dừng lại để tiết kiệm thời gian
            if abs(next_S - S) < 1e-6:  # Ngưỡng sai số đủ nhỏ (tùy chỉnh)
                break
            S = next_S
        return S
    
    ns = list(np.linspace(1, 400, 399))
    an = [my_func(n) for n in ns]
    fig, ax = plt.subplots()  
    log_ns = np.log(ns) / np.log(2)
    ax.plot(log_ns, an, label=r"$y = a_n$")
    ax.set_xlabel(r"$\log_2(n)$")
    ax.set_ylabel(r"$a_n = \sqrt{3 + \sqrt{3 + ... + \sqrt{3}}} $")
    ax.axhline(y=(1 + np.sqrt(13)) / 2, color='r', linestyle='--', label=r"$y=\dfrac{1+\sqrt{13}}{2}$")
    ax.legend()

    return fig

# =========================================================================================================================================== #
#                                                               3. LOGICAL (minh hoa)                                                         #  
# =========================================================================================================================================== #
def illustration_logical_1_easy():
    # Tạo hình trụ 3D
    def plot_cylinder(ax, radius, height, center, num_points=100):
        # Tạo các điểm trên mặt cắt ngang của hình trụ
        theta = np.linspace(0, 2*np.pi, num_points)
        z = np.linspace(-height/2, height/2, num_points) + center[2]
        
        # Tạo lưới 2 chiều cho các tọa độ x và y
        Z, Theta = np.meshgrid(z, theta)
        X = radius * np.cos(Theta) + center[0]
        Y = radius * np.sin(Theta) + center[1]
        
        # Vẽ hình trụ
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='cyan', alpha=0.3)

    # Vẽ dây xoắn
    def plot_twisted_wire(ax, radius, height, center, turns=10, num_points=400, color='r'):
        # Tạo đường xoắn ốc quanh hình trụ
        theta = np.linspace(0, 2*np.pi*turns, num_points)
        z = np.linspace(-height/2, height/2, num_points) + center[2]
        x = radius * np.cos(theta)  + center[0]
        y = radius * np.sin(theta)  + center[1]
        
        # Vẽ đường dây xoắn với màu sắc cho phép điều chỉnh
        ax.plot(x, y, z, color=color, linestyle="--", lw=1)
        
        # Trả về các giá trị điểm đầu và cuối của dây xoắn để đánh dấu
        return x[0], y[0], z[0], x[-1], y[-1], z[-1]

    # Khởi tạo đồ thị
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ hai ống hình trụ song song với đường kính nhỏ hơn
    r = 0.5
    plot_cylinder(ax, radius=r, height=10, center=(0, 0, 0))  # Hình trụ 1 với radius bé hơn
    #plot_cylinder(ax, radius=r, height=8, center=(4, 0, 0))  # Hình trụ 2 với radius bé hơn

    # Vẽ dây xoắn trên mỗi ống, mỗi dây có màu khác nhau và lấy các điểm đầu-cuối để highlight
    x1_start, y1_start, z1_start, x1_end, y1_end, z1_end = plot_twisted_wire(ax, radius=r, height=10, center=(0, 0, 0), turns=10, color='r')  # Dây xoắn 1 với màu đỏ
    x2_start, y2_start, z2_start, x2_end, y2_end, z2_end = plot_twisted_wire(ax, radius=r, height=8, center=(4, 0, 0), turns=8, color='black')   # Dây xoắn 2 với màu xanh lá

    # Highlight các điểm A, B, A', B' tại các đầu của đường xoắn ốc
    ax.plot(x1_start, y1_start, z1_start, 'bo', markersize=8)  # Điểm A
    ax.plot(x1_end, y1_end, z1_end, 'bo', markersize=8)  # Điểm A'
    ax.plot(x2_start, y2_start, z2_start, 'go', markersize=8)  # Điểm B
    ax.plot(x2_end, y2_end, z2_end, 'go', markersize=8)  # Điểm B'

    # Thêm nhãn ở mỗi đầu mỗi ống
    ax.text(0, 0, 6, 'A', fontsize=12, color='black', weight='bold')  # Nhãn cho ống 1
    ax.text(0, 0, -6, "A'", fontsize=12, color='black', weight='bold')  # Nhãn cho ống 1
    ax.text(4, 0, 5, 'B', fontsize=12, color='black', weight='bold')  # Nhãn cho ống 2
    ax.text(4, 0, -5, "B'", fontsize=12, color='black', weight='bold')  # Nhãn cho ống 2

    # Cài đặt hiển thị đồ thị
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_axis_off() 
    ax.set_box_aspect([1, 1, 1])

    return fig

def illustration_logical_2_easy():    
    fig, ax = plt.subplots(1, 3, figsize=(10, 4.5), gridspec_kw={'width_ratios': [4, 1, 1]}, dpi = 100)
    fig.suptitle("Minh họa các lượt đua",y=1.1)
    ax[0].set_axis_off()
    ax[0].set_xlim([-2, 6])
    ax[0].set_ylim([-1, 5])
    color_band = ['red', 'green', 'blue', 'purple', 'orange']
    ax[0].text(-2, 5.2, 'Group', fontweight='bold', color="darkblue")
    ax[0].text(-2, 2.2, 'rank', fontweight='bold', color="darkgreen")
    lanes = ['A', 'B', 'C', 'D', 'E']
    sublane = ['A2', 'A3', 'B1', 'B2', 'C1']
    rect = patches.Rectangle((-0.4, 3.6), 5, 1, linewidth=1, edgecolor='blue', facecolor='lime', alpha=0.2)
    ax[0].add_patch(rect)
    for x, lane in enumerate(lanes):
        ax[0].text(x, 5.1, f"{lane}",fontweight='bold', color="darkblue")
        for y in range(5):
            is_w = "white" if y == 0 else "black"
            ax[0].text(x-0.05, y, f"{lane}{5-y}", color = is_w)
            ax[0].text(-1, y, f"{5-y}",fontweight='bold', color="darkgreen")
            c = plt.Circle((x+0.1, y+0.1), 0.4, color=color_band[x], alpha= 1 / (y+1))
            ax[0].add_artist(c)
    ax[0].text(1, -0.75, '25-horses-encoded', fontsize=9)
    ax[0].set_title("Turn 1-5", y=1.1)

    rect2 = patches.Rectangle((-0.4, 3.6), 1.1, 1, linewidth=1, edgecolor='blue', facecolor='skyblue', alpha=0.25)
    rect3 = patches.Rectangle((-0.4, 3.6), 1.1, -4, linewidth=1, edgecolor='blue', facecolor='yellow', alpha=0.15)
    ax[1].add_patch(rect2)
    ax[1].add_patch(rect3)
    ax[1].set_xlim([-1, 1])
    ax[1].set_ylim([-1, 5])
    ax[1].text(0.7, 4, ' top1 \n final', color='red', fontsize=9, fontweight='bold')
    for x in range(5):
        ax[1].text(0, x, f"{lanes[5-x-1]}1")
        c = plt.Circle((0.15, x+0.1), 0.4, color=color_band[5-x-1], alpha= 1 / (y+1))
        ax[1].add_artist(c)    
    ax[1].set_axis_off()
    ax[1].set_title("Turn 6", y=1.1)

    ax[2].set_xlim([-1, 1])
    ax[2].set_ylim([-1, 5])
    rect4 = patches.Rectangle((-0.4, 4.6), 1.1, -5, linewidth=1, edgecolor='blue', facecolor='red', alpha=0.1)
    ax[2].add_patch(rect4)
    for x in range(5):
        ax[2].text(0, x, f"{sublane[5-x-1]}")
        c = plt.Circle((0.15, x+0.1), 0.4, color=color_band[x], alpha= 1 / (y+1))
        ax[2].add_artist(c)
    ax[2].set_axis_off()
    ax[2].set_title("Turn 7", y=1.1)
    
    return fig

def illustration_logical_1_medium():
    t_star = -(-1 + np.sqrt(5)) / 2
    times_list = [t_star, 0, 1, 2]
    snow_fall = [0, 0.7, 1.5, 2.25]
    coefficients = np.polyfit(times_list, snow_fall, 3)
    poly = np.poly1d(coefficients)
    x_range = np.linspace(t_star, 2, 100)
    speed = 1 / (x_range + 1)
    y_range = poly(x_range)
    x_range = np.linspace(t_star, 2, 100)
    alpha = 1.5585651909263851
    beta = 0.6180339887529622
    gamma = 0.7499999999923197 
    distance = np.log(beta + x_range[x_range > 0]) * alpha + gamma

    fig, ax = plt.subplots(1,1, figsize=(8, 5))
    ax.plot(x_range[x_range < 1], y_range[x_range < 1], 'red', linestyle='--', lw=1, label='snow-fall (cumulative)')
    ax.plot([1, 2], [1.5, 2.25], 'red', linestyle='--', lw=1)
    ax.plot(x_range, speed, 'blue', linestyle='--', lw=1, label='car-speed')
    ax.plot(x_range[x_range > 0.], distance, 'green', linestyle='-', lw=2, label='car-distance', alpha=0.6)
    ax.plot([-1, -1], [0, 3], linestyle='-', color='black', lw=1)
    ax.plot([-1, 2], [0, 0], linestyle='-', color='black', lw=1)
    for x, y, l in zip(times_list, snow_fall, [r'$t_0$', "midday (0pm)", "1pm", "2pm"]):
        color_text = "darkblue" if x != t_star else "purple"
        ax.text(x, -0.2, l, color=color_text, fontsize=9)
        if x > 0:
            ax.text(-1.1, y, f'$x_{x}$', color="darkblue", fontsize=9)
            ax.plot([x, x], [0, y], linestyle=":", color='green', lw=1)
            ax.plot([-1, x], [y, y], linestyle=":", color='green', lw=1)
            ax.plot([x], [y], 'go', markersize=5)

    ax.plot([0], [0], 'go', markersize=5)
    ax.text(-1.2, 0.1, '$x_0=0$', color="darkblue", fontsize=9)
    ax.text(-0.95, 1.75, '$x_1 - x_0 = 2(x_2 - x_1)$', fontsize=10)
    ax.text(2.25, -0.25, "time", color="darkgreen", fontsize=10)
    ax.text(t_star-0.1, -0.4, 'snow began', color="red", fontsize=9)
    ax.text(-0.06, -0.45, 'snow clearing car \n begins work', color='green', fontsize=8)
    ax.text(-1.2, 3.2, 'distance', color="darkgreen", fontsize=10)
    ax.text(-1.1, 3.05, '(miles)', color="darkgreen", fontsize=9)
    ax.legend(loc='upper right')
    ax.set_axis_off()
    
    return fig

def illustration_logical_2_medium():
    t_star = -(-1 + np.sqrt(5)) / 2
    times_list = [t_star, 0, 1, 2]
    snow_fall = [0, 0.7, 1.5, 2.25]
    coefficients = np.polyfit(times_list, snow_fall, 3)
    poly = np.poly1d(coefficients)
    x_range = np.linspace(t_star, 2, 100)
    speed = 1 / (x_range + 1)
    y_range = poly(x_range)
    x_range = np.linspace(t_star, 2, 100)
    alpha = 1.5585651909263851
    beta = 0.6180339887529622
    gamma = 0.7499999999923197 
    distance = np.log(beta + x_range[x_range > 0]) * alpha + gamma

    fig, ax = plt.subplots(1,1, figsize=(8, 5))
    ax.plot(x_range[x_range < 1], y_range[x_range < 1], 'red', linestyle='--', lw=1, label='snow-fall (cumulative)')
    ax.plot([1, 2], [1.5, 2.25], 'red', linestyle='--', lw=1)
    ax.plot(x_range, speed, 'blue', linestyle='--', lw=1, label='snowplow-speed')
    ax.plot(x_range[x_range > 0.], distance, 'green', linestyle='-', lw=2, label='snowplow-distance', alpha=0.6)
    ax.plot([-1, -1], [0, 3], linestyle='-', color='black', lw=1)
    ax.plot([-1, 2], [0, 0], linestyle='-', color='black', lw=1)
    for x, y, l in zip(times_list, snow_fall, [r'$t_0$', "8am", "9am", "10am"]):
        color_text = "darkblue" if x != t_star else "purple"
        ax.text(x, -0.2, l, color=color_text, fontsize=9)
        if x > 0:
            ax.text(-1.45, y, f'$x_{x} = {x+1}$ miles', color="darkblue", fontsize=9)
            ax.plot([x, x], [0, y], linestyle=":", color='green', lw=1)
            ax.plot([-1, x], [y, y], linestyle=":", color='green', lw=1)
            ax.plot([x], [y], 'go', markersize=5)

    ax.plot([0], [0], 'go', markersize=5)
    ax.text(-1.25, 0.1, '$x_0=0$', color="darkblue", fontsize=9)
    ax.text(2.25, -0.25, "time", color="darkgreen", fontsize=10)
    ax.text(t_star-0.1, -0.4, 'snow began', color="red", fontsize=9)
    ax.text(-0.1, -0.45, 'Homer Simpson had just started \n his own snowplow business', color='green', fontsize=8)
    ax.text(-1.2, 3.2, 'distance', color="darkgreen", fontsize=10)
    ax.text(-1.1, 3.05, '(miles)', color="darkgreen", fontsize=9)
    ax.legend(loc='upper right')
    ax.set_axis_off()

    return fig

def illustration_logical_1_hard():
    pass
# =========================================================================================================================================== #
#                                                            4. LUONG GIAC (minh hoa)                                                         #
# =========================================================================================================================================== #
def illustration_trigonometric_2_easy():
    fig = plt.figure(figsize=(10, 3), dpi=100)
    ax = fig.add_subplot(111)

    t = np.linspace(-10, 10, 1000)
    y = np.sin(np.pi * t)
    ax.plot(t, y)

    ax.plot([0, 6], [1/2, 1/2], 'red', linestyle=":", lw=1.2, alpha=0.5)
    ax.text(0.6, 1.1, r'$y=\sin \pi x$', color='blue')
    ax.text(4.5, 0.35, r'$y=\frac{1}{2}$', color='red')
    ax.plot([0, 6], [0, 0], 'black')

    ax.plot([2, 2], [-1, 1], 'g--')
    ax.text(1.9, 1.1, '$y=2$', color='green')
    ax.plot([3, 3], [-1, 1], 'g--')
    ax.text(3.2, 1.1, '$y=3$', color='green')

    ax.plot([13/6], [1/2], 'bo', markersize=5)
    ax.plot([17/6], [1/2], 'bo', markersize=5)
    ax.plot([13/6, 13/6], [1/2, 0], 'black', linestyle=":", lw=1)
    ax.plot([17/6, 17/6], [1/2, 0], 'black', linestyle=":", lw=1)
    ax.plot([13/6], [0], 'go', markersize=5)
    ax.plot([17/6], [0], 'go', markersize=5)
    ax.text(13/6, -0.25, '$x_1$', color='red')
    ax.text(17/6, -0.25, '$x_2$', color='red')

    ax.set_xlim(0, 5)
    ax.set_xlabel('$x$')
    ax.set_axis_off()
    plt.show()
    
    return fig

def illustration_trigonometric_1_medium():
    pi = np.pi
    def tan(t): return np.tan(t)

    x1 = np.linspace(pi/1000, 999*pi/2001, 200)
    x2 = np.linspace(pi/2 + pi/1000, 999*pi/1000, 200)
    labels = ['tan x', 'cot x', 'tan x + cot x']
    fig, axes = plt.subplots(1, 3, figsize=(12, 4), dpi=100, gridspec_kw={'width_ratios': [1, 1, 2]})
    for idx, ax in enumerate(axes):
        if idx != 2:
            ax.text(-0.25, -1, '$O$')   
            if idx == 0:
                y1 = [tan(t) for t in x1]
                y2 = [tan(t) for t in x2]
            elif idx == 1:
                y1 = [1/tan(t) for t in x1]
                y2 = [1/tan(t) for t in x2]
        else:
            ax.plot([0, pi], [2, 2], color='red', lw=1)
            ax.text(pi, 2.25, '$y=2$')
            ax.text(-0.15, -1, '$O$')
            ax.plot(pi/4, 2, 's', color='black', markersize=5)
            y1 = [tan(t) + 1/tan(t) for t in x1]
            y2 = [tan(t) + 1/tan(t) for t in x2]

        ax.plot(x1, y1, color='blue', label=labels[idx], lw=1, alpha=0.8)
        ax.plot(x2, y2, color='blue', lw=1, alpha=0.8)
        ax.plot([0, pi], [0, 0], color='black', lw=1)
        ax.plot([0, 0], [-10, 10], color='black', lw=1)
        ax.plot([pi/2, pi/2], [-10, 10], color='green', lw=1)
        ax.text(pi, -1, '$\pi$')
        ax.text(pi/2+0.2, 5, '$\dfrac{\pi}{2}$')
        ax.set_ylim([-10, 10])
        ax.set_axis_off()
        ax.legend()
        
    return fig

def illustration_trigonometric_1_hard():
    x = np.linspace(-3, 3, 201)
    sinh = np.sinh(x)
    cosh = np.cosh(x)

    fig, ax = plt.subplots(figsize=(4, 6), dpi=100)
    ax.plot(x, sinh, label='sinh x', linestyle='--', color='red')
    ax.plot(x, cosh, label='cosh x', color='blue')
    ax.plot([-pi, pi], [0, 0], color='black', lw=1)
    ax.plot([0, 0], [-12, 12], color='black', lw=1)

    ax.text(0.1, -1, '$O$')
    ax.text(3.15, 0, '$x$')
    ax.text(0, 12.5, '$y$')
    for x in range(-3, 4, 1):
        if x != 0:
            ax.text(x, -1, f"{x}", fontsize=9)
    for y in range(-12, 13, 2):
        if y != 0:
            ax.text(-0.5, y, f"{y}", fontsize=9)
    ax.legend(loc='lower right')
    ax.set_axis_off()
    
    return fig

# =========================================================================================================================================== #
#                                                             5. CALCULUS (minh hoa)                                                          #  
# =========================================================================================================================================== #
def illustration_Calculus_1_easy():
    fig, ax = plt.subplots(1, 1, figsize=(10, 3), dpi = 100)
    x = np.linspace(2, 100, 10001)
    y = 1 / (x*(x-1))
    ax.plot(x, y)
    ax.fill_between(x, y, color='skyblue', alpha=0.5)
    ax.plot([2, 2], [0, 1/2], linestyle="--", color='red', lw=1)
    ax.plot([100, 100], [0, 1/2], linestyle="--", color='red', lw=1)
    ax.plot([2, 100], [0, 0], linestyle="-", color='black', lw=1)
    ax.plot([2], [0], 'bo', markersize=3)
    ax.plot([2], [1/2], 'bo', markersize=3)
    ax.plot([100], [0], 'bo', markersize=3)

    ax.text(0, 0.55, r"$x=2$", fontsize=9)
    ax.text(100, 0.55, r"$x=n$", fontsize=9)
    ax.text(50, -0.05, r"$y=0$", fontsize=9)
    ax.text(5, 0.1, r"$y=\dfrac{1}{x(x-1)}$", fontsize=9)
    ax.set_axis_off()
    
    return fig
        
def illustration_Calculus_2_easy():
    fig, ax = plt.subplots(1, 1, figsize=(10, 3), dpi = 100)
    x = np.linspace(-2, 2, 10001)
    y = x * np.cos(x)
    ax.plot([-2, 2], [0, 0], color='black', lw=1)
    ax.plot([-2, -2], [-1, 1], color='green', lw=1)
    ax.plot([2, 2], [-1, 1], color='green', lw=1)
    ax.plot(x, y, lw=2, alpha=0.7)
    ax.fill_between(x[y > 0], y[y > 0], color='skyblue', alpha=0.5)
    ax.fill_between(x[y < 0], y[y < 0], color='red', alpha=0.2)
    ax.text(0, -0.25, '$O$')
    ax.text(-2.25, -0.2, '$x=-2$', fontsize=8)
    ax.text(2.05, 0.2, '$x=2$', fontsize=8)
    ax.text(0.8, 0.7, '$y= x \cos x$', fontsize=8)
    ax.set_axis_off()
    
    return fig

# =========================================================================================================================================== #
#                                                       6. XÁC SUẤT THỐNG KÊ (minh hoa)                                                       # 
# =========================================================================================================================================== #
def illustration_StatsnProba_1_easy():
    muy, sigma = 68, 5
    x = np.linspace(muy - 4*sigma, muy+4*sigma, 1000)
    pdf = sts.norm.pdf(x, loc=muy, scale=sigma)
    cdf = sts.norm.cdf(x, loc=muy, scale=sigma)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5), dpi=100)
    ax[0].plot(x, pdf, linestyle='-', lw=2)
    ax[0].set_ylim([-0.015, 0.09])
    ax[1].plot(x, cdf, linestyle='-', lw=2)
    ax[0].plot([muy, muy], [0, 0.08], color='green', lw=2)
    ax[1].plot([muy, muy], [0, 1], color='green', lw=1)
    ax[0].annotate('', xy=(muy+sigma, 0.04), xytext=(muy, 0.04),
                arrowprops=dict(facecolor='blue', edgecolor='red', arrowstyle='<->', lw=1))
    ax[0].annotate('', xy=(muy+4*sigma, -0.005), xytext=(muy, -0.005),
                arrowprops=dict(facecolor='blue', edgecolor='purple', arrowstyle='<->', lw=1))
    ax[0].annotate('', xy=(muy-4*sigma, -0.005), xytext=(muy, -0.005),
                arrowprops=dict(facecolor='blue', edgecolor='purple', arrowstyle='<->', lw=1))
    ax[0].text(muy+1/2, 0.035, r"$\sigma = 5$", color='red')
    ax[0].text(muy+1/2, 0.005, r'$x=\mu = 68$', color='green')
    ax[0].text(muy + 2*sigma, -0.01, r'$4\sigma$')
    ax[0].text(muy - 2*sigma, -0.01, r'$4\sigma$')
    ax[1].text(muy+1/2, 0.1, r'$x=\mu$')
    ax[0].set_title("pdf")
    ax[1].set_title("cdf")
    ax[0].plot([muy - 4*sigma, muy + 4*sigma], [0, 0], 'black', lw=1)
    ax[0].set_axis_off()
    ax[1].plot([78.27], [0.98], 'ro', markersize=5)
    ax[1].plot([muy - 4*sigma, muy+4*sigma], [0, 0], 'black', lw=1)
    ax[1].plot([muy - 4*sigma, muy+4*sigma], [1, 1], 'black', lw=1)
    ax[1].plot([muy - 4*sigma, muy-4*sigma], [0, 1], 'black', lw=1)
    ax[1].plot([muy - 4*sigma, muy+4*sigma], [0.98, 0.98], linestyle="--", color='red', lw=1)
    ax[1].plot([78.27, 78.27], [0.98, 0], linestyle=":", color='purple', lw=1)
    ax[1].text(88, 0.92, '$98\%$', color='red', fontsize=9)
    ax[1].text(79, 0.1, '$x = ?$', color='red', fontsize=9)
    for y in np.linspace(0, 1, 11):
        ax[1].text(muy - 5*sigma, y, f"{y:.1f}", fontsize=9)
    for x in np.linspace(muy-4*sigma, muy+4*sigma, 9):
        ax[1].text(x, -0.05, f"{int(x)}", fontsize=9)
    ax[1].set_axis_off()
    
    return fig

def illustration_StatsnProba_2_easy():
    # Parameters
    mean_height = 68
    std_height = 5
    mean_weight = 168
    std_weight = 25

    # Generate data for height and weight
    height_values = np.linspace(mean_height - 4*std_height, mean_height + 4*std_height, 100)
    weight_values = np.linspace(mean_weight - 4*std_weight, mean_weight + 4*std_weight, 100)

    # First plot: Normal distribution of height
    height_pdf = sts.norm.pdf(height_values, mean_height, std_height)

    # Second plot: Normal distribution of weight
    weight_pdf = sts.norm.pdf(weight_values, mean_weight, std_weight)

    # Create the figure
    fig, axs = plt.subplots(2, 2, figsize=(10, 10), dpi=100)
    axs = axs.ravel()

    def normal_dist_axes(ax, x, y, muy, sigma, label, color):
        idx = 1 if label == 'Height' else 2
        ax.plot(x, y, label=label, color=color)
        ax.fill_between(x, y, color=color, alpha=0.1)
        ax.set_title(label)
        ax.plot([muy, muy], [0, y.max()], color='red', lw=1)
        ax.plot([x.min(), x.max()], [0, 0], color='black', lw=1)
        ax.text(muy*1.02, y.max()/3, f"$\mu_{idx} = {muy}$",fontweight='bold', color="red", fontsize=9)
        ax.text(muy, -y.max()/12, f"$\mu_{idx}$", color="darkblue", fontsize=9, fontweight='bold')
        ax.text(muy*1.02, y.max()/4, f"$\sigma_{idx} = {sigma}$", color="green", fontsize=9, fontweight='bold')    
        ax.set_axis_off()
        return ax
        
    normal_dist_axes(axs[0], height_values, height_pdf, mean_height, std_height, label='Height', color='blue')
    normal_dist_axes(axs[1], weight_values, weight_pdf, mean_weight, std_weight, label='Weight', color='green')

    # 3-4 plot: Contour plot for joint distribution (correlation = 0.35)
    def make_normal_2d_dist(axes, mean_height, mean_weight, std_height, std_weight, correlation=0.35, addition_color='red'):
        # Generate bivariate normal distribution for correlation of 0.35
        mean = [mean_height, mean_weight]
        cov = [[std_height**2, correlation*std_height*std_weight],
            [correlation*std_height*std_weight, std_weight**2]]
        
        # Create a grid of points for the contour plot
        x, y = np.meshgrid(height_values, weight_values)
        pos = np.dstack((x, y))
        rv = np.random.multivariate_normal(mean, cov, size=5000)
        # Plot
        sns.kdeplot(x=rv[:, 0], y=rv[:, 1], cmap="Blues", fill=True, ax=axes, levels=10)
        axes.set_title(f'Joint Distribution (Correlation = {correlation})')
        axes.text(mean_height*0.92, 80,'Height (inches)', color='darkblue', fontsize=9)
        axes.text(45, 168,'Weight\n(pounds)', color='darkgreen', fontsize=9)
        axes.text(55, 244, r"$r_{1,2} = \frac{\sigma_{1,2}}{\sigma_1 \sigma_2} = %.2f$" % correlation, 
                color=addition_color, fontweight='bold', fontsize=12)
        arrow_h = FancyArrowPatch((50, 88), (82, 88), mutation_scale=15, arrowstyle='<|-|>', color='blue')
        arrow_w = FancyArrowPatch((51, 88), (51, 238), mutation_scale=15, arrowstyle='<|-|>', color='green')
        axes.add_patch(arrow_h)
        axes.add_patch(arrow_w)
        axes.set_axis_off()

        return axes
    make_normal_2d_dist(axs[2], mean_height, mean_weight, std_height, std_weight, correlation=0.35, addition_color='red')
    make_normal_2d_dist(axs[3], mean_height, mean_weight, std_height, std_weight, correlation=-0.5, addition_color='purple')
    
    return fig

def illustration_StatsnProba_3_easy():
    a, b = 0, 5
    x = np.linspace(a, b, 1000)
    y = ((b + a)/2)**2 - ((b + a)/2 - x)**2
    fig, ax = plt.subplots(1, 1, figsize=(4, 4), dpi=100)
    ax.plot(x, y)
    ax.plot([a, b], [0, 0], 'black', lw=1)
    ax.text(a, -0.5, '$a$')
    ax.text(b, -0.5, '$b$')
    ax.text(2, 6.6, r"$\mathbb{E}(X - \mathbb{E}X)^2$", color="blue", fontsize=12)
    ax.set_axis_off()
    
    return fig

def illustration_StatsnProba_4_easy():
    def make_normal_2d_dist(axes, muy_x=0, muy_y=10, std_x=0.25, std_y=2, correlation=0.35, x_note="X", y_note="Y", subtext="$\sigma_{X,Y} > 0$", sub_bg_col = 'Blues'):
        mean = [muy_x, muy_y]
        cov = [[std_x**2, correlation*std_x*std_y], [correlation*std_y*std_x, std_y**2]]
        
        x, y = np.meshgrid(np.linspace(muy_x - 3*std_x, muy_x + 3*std_x, 500), 
                        np.linspace(muy_y - 3*std_x, muy_y + 3*std_y, 1000))
        pos = np.dstack((x, y))
        x_min = x.min()
        y_min = muy_y - 3*std_y 
        rv = np.random.multivariate_normal(mean, cov, size=5000)
        sns.kdeplot(x=rv[:, 0], y=rv[:, 1], cmap=sub_bg_col, fill=True, ax=axes, levels=10)
        axes.set_title(f'Joint Distribution ({subtext})')
        temp_h = y_min * 0.98 if muy_x > 0 else y_min - 1
        axes.text(muy_x, temp_h, x_note, color='darkgreen', fontweight='bold', fontsize=9)
        axes.text(x_min*0.8, muy_y, y_note, color='darkblue', fontweight='bold', fontsize=9)
        arrow_h = FancyArrowPatch((x_min, muy_y - 3*std_y), (x_min, muy_y + 3*std_y), mutation_scale=15, arrowstyle='<|-|>', color='blue')
        arrow_w = FancyArrowPatch((muy_x - 3*std_x, y_min), (muy_x + 3*std_x, y_min), mutation_scale=15, arrowstyle='<|-|>', color='green')
        axes.add_patch(arrow_h)
        axes.add_patch(arrow_w)
        axes.set_axis_off()

        return axes

    fig, ax = plt.subplots(1, 2, figsize=(8, 4), dpi=100)
    ax[0] = make_normal_2d_dist(ax[0],  muy_x=0, muy_y=10, std_x=0.25, std_y=2, correlation=0.35, x_note="X", y_note="Y", subtext="$\sigma_{X,Y} > 0$", sub_bg_col="Purples")
    ax[1] = make_normal_2d_dist(ax[1],  muy_x=10, muy_y=5, std_x=2, std_y=0.2, correlation=-0.65, x_note="Y", y_note="Z", subtext="$\sigma_{Y,Z} < 0$", sub_bg_col="Oranges")    
    
    return fig

def illustration_StatsnProba_1_medium():
    fig, ax = plt.subplots(1, 1, figsize=(8, 4), dpi=100)
    ax.plot([-2, -2], [-0.2, 10], 'black', lw=1)
    ax.plot([10, 10], [-0.2, 10], 'black', lw=1)

    def sims(ax, text, y_coordinate):
        for idx, txt in enumerate(text):
            if idx > len(text) - 3:
                ax.text(idx, y_coordinate, txt, fontweight='bold', color="red", fontsize=9)        
            else:
                ax.text(idx, y_coordinate, txt, color='darkgreen', fontsize=10)

        return ax

    ax.plot([-2, 10], [-0.2, -0.2], 'black', linestyle="--", lw=1)
    ax = sims(ax, ["H", "H"], 0); ax.text(-1.9, 0, '2 flips')
    ax.plot([-2, 10], [0.75, 0.75], 'black', linestyle="--", lw=1)
    ax = sims(ax, ["T", "H", "H"], 1); ax.text(-1.9, 1, '3 flips')
    ax.plot([-2, 10], [1.75, 1.75], 'black', linestyle="--", lw=1)
    ax = sims(ax, ["H", "T", "H", "H"], 2); ax.text(-1.9, 2.44, '4 flips')
    ax = sims(ax, ["T", "T", "H", "H"], 2.75); 
    ax.plot([-2, 10], [3.3, 3.3], 'black', linestyle="--", lw=1)
    ax = sims(ax, ["T", "H", "T", "H", "H"], 3.5); ax.text(-1.9, 4.25, '5 flips')
    ax = sims(ax, ["H", "T", "T", "H", "H"], 4.25)
    ax = sims(ax, ["T", "T", "T", "H", "H"], 5)
    ax.plot([-2, 10], [5.75, 5.75], 'black', linestyle="--", lw=1)

    ax = sims(ax, ["H", "T", "H", "T", "H", "H"], 6); ax.text(-1.9, 7, '6 flips')
    ax = sims(ax, ["T", "T", "H", "T", "H", "H"], 6.75)
    ax = sims(ax, ["H", "T", "T", "T", "H", "H"], 7.5)
    ax = sims(ax, ["T", "T", "T", "T", "H", "H"], 8.25)

    ax.plot([-2, 10], [8.75, 8.75], 'black', linestyle="--", lw=1)
    ax.text(-1.9, 9.2, 'n flips')
    ax = sims(ax, ["..", "..", "..", "..", "..", "..", "..", "T", "H", "H"], 9.25)
    ax.plot([-2, 10], [10, 10], 'black', linestyle="-", lw=1)

    ax.set_axis_off()
    
    return fig

def illustration_StatsnProba_2_medium():
    def make_concave(axes, muy_x=0, muy_y=10, std_x=0.25, std_y=2, correlation=0.35, sub_bg_col = 'Blues', cave_name='E1', col='darkblue'):
        mean = [muy_x, muy_y]
        cov = [[std_x**2, correlation*std_x*std_y], [correlation*std_y*std_x, std_y**2]]
        
        x, y = np.meshgrid(np.linspace(muy_x - 3*std_x, muy_x + 3*std_x, 500), 
                        np.linspace(muy_y - 3*std_x, muy_y + 3*std_y, 1000))
        pos = np.dstack((x, y))
        rv = np.random.multivariate_normal(mean, cov, size=5000)
        sns.kdeplot(x=rv[:, 0], y=rv[:, 1], cmap=sub_bg_col, fill=True, ax=axes, levels=10)
        axes.text(muy_x, muy_y + 3.5*std_y, cave_name, color = col)
        axes.set_axis_off()

        return axes

    fig, ax = plt.subplots(1, 1, figsize=(8, 4), dpi=100)
    ax = make_concave(ax, muy_x=0, muy_y=2, std_x=0.35, std_y=2, correlation=0.35, sub_bg_col = 'Blues', cave_name='E1\n 1hour', col='darkblue')
    ax = make_concave(ax, muy_x=6, muy_y=5, std_x=0.81, std_y=3, correlation=-0.5, sub_bg_col = 'Greens', cave_name='E2\n 2hours', col='darkgreen')
    ax = make_concave(ax, muy_x=3, muy_y=-2, std_x=0.64, std_y=4, correlation=-0.15, sub_bg_col = 'Oranges', cave_name='E3\n 3hours', col='red')
    t = np.linspace(-np.pi, np.pi, 101)
    ax.plot(3 + np.cos(t)/5, -15 + np.sin(t) / 5, 'black')
    ax.text(2.5, -17, "you are here", fontsize=9)
    
    return fig

def illustration_StatsnProba_4_hard():
    def gen_archer(ax, x_cen, y_cen, sublab = 'A', color='red'):
        col_map = color[0] + 'o'
        ax.text(x_cen, y_cen + 0.5, sublab, color=color)
        ax.plot([x_cen], [y_cen], col_map, markersize=10)
        ax.plot([x_cen, x_cen], [0, y_cen], color=color, linestyle="-.", lw=2)
        return ax
        
    fig, ax = plt.subplots(1, 2, figsize=(8, 4), dpi=100)
    ax[0].plot([0, 0], [0, 4.5], color="white", linestyle=":", lw=1)
    ax[0].plot([1.2, 6.3], [0, 0], color="white", linestyle=":", lw=1)
    ax[0] = gen_archer(ax[0], 1, 2, '$A_1$', 'green')
    ax[0] = gen_archer(ax[0], 0.5, 2.2, '$A_2$', 'blue')
    ax[0].plot(6, 1, 'o', color='orange', markersize=36, alpha=0.6)
    ax[0].plot(6, 1, 'o', color='pink', markersize=26)
    ax[0].plot(6, 1, 'o', color='violet', markersize=18)
    ax[0].plot(6, 1, 'o', color='purple', markersize=10)
    ax[0].plot(6, 1, 'ro', markersize=4)
    ax[0].text(5.75, 1.5, 'target', color='red', fontsize=9)
    ax[0].set_axis_off()

    t = np.linspace(-np.pi, np.pi, 101)
    for idx, col in enumerate(['red', 'purple', 'violet', 'pink', 'orange']):
        r = idx + 1
        x = r*np.cos(t)
        y = r*np.sin(t)    
        ax[1].plot(x, y, color=col, lw=2)
    ax[1].plot(0, 0, 'o', color='red')
    ax[1].text(0, -0.5, 'center', color='darkblue', fontsize=10)
    ax[1].text(-1, 1, '$r_1$')
    ax[1].text(3, 2, '$r_2$')
    ax[1].set_axis_off()
    
    return fig

# =========================================================================================================================================== #
#                                                                    Q + SOLUTION                                                             #
# =========================================================================================================================================== #
#                                                                   Questions                                                                 #
# =========================================================================================================================================== #
#                                                                HINH HOC (question)                                                          #
# =========================================================================================================================================== #
def question_hinh_hoc_1_easy():
    st.write("#### Câu 1.")
    st.write(r"Cho $\bigtriangleup ABC$ với $AB = 6, AC = 8$ và $BC = 10$, từ $A$ kẻ đường cao $AH$, tính $AH$")

def question_hinh_hoc_1_medium():
    st.write("#### Câu 1.")
    st.write(r"Cho hình tứ diện $ABCD$ với thể tích $V$, trên mỗi mặt của nó lấy một trọng tâm và các điểm này tạo được một khối thể tích $V'$, hỏi tỷ lệ $\frac{V'}{V}$")

def question_hinh_hoc_2_medium():
    st.write("#### Câu 2.")
    st.write("Một khối băng tan mà không thay đổi hình dạng với tốc độ đều 4 $cm^3$/phút. Tìm tốc độ thay đổi diện tích bề mặt của khối lập phương khi thể tích là 125 $cm^3$.")

def question_hinh_hoc_1_hard():
    st.write("#### Câu 1.")
    st.write("Cho hình lập phương với thể tích $V_a$, trên mỗi mặt của hình lập phương này ta lấy các tâm hình vuông nối lại, ta được một khối đa diện với thể tích $V_b$, từ khối đó ta lại làm tương tự và ta được $V_c = 1$, hỏi $V_a$ và $V_b$")
    
def question_hinh_hoc_2_hard():
    st.write("#### Câu 2.")
    st.write("Một hình nón rỗng với góc bán phương $\\arctan\\left( \\frac{1}{2} \\right)$ được cố định đầu đỉnh hướng xuống dưới, với trục của nó thẳng đứng và đang được điền nước với một tốc độ không đổi $k$. Một con nhện có thể chạy với tốc độ $u$ đang ngủ ở cuối một cái mạng, treo ở độ cao $h_0$ thẳng đứng trên đỉnh của nón. Tìm giá trị tối thiểu của $u$ theo $k$ và $h_0$ sao cho con nhện có thể thoát khỏi việc bị ướt, giả sử rằng nó bắt đầu chạy lên ngay khi nước chạm vào chân.")
    
def question_hinh_hoc_3_hard():
    st.write("#### Câu 3 (hình học + xác suất)")
    st.write(r"Cho tam giác $\bigtriangleup ABC$ độ dài 3 cạnh lần lượt là 45, 60, 75 và $D$ là 1 điểm ngẫu nhiên bên trong tam giác này, hãy tính kỳ vọng tổng khoảng cách 3 đường cao kẻ từ $D$ đến 3 cạnh của tam giác")

# =========================================================================================================================================== #
#                                                             LUONG GIAC (question)                                                           #
# =========================================================================================================================================== #
def question_trigonometric_1_easy():
    st.write("#### Câu 1.")
    st.write("Tính giá trị của: \n $\sin \dfrac{\pi}{6} + \sin \dfrac{\pi}{4} + \sin \dfrac{\pi}{3}$.")
    submit_button = st.button("See the answers")
    
    return submit_button

def question_trigonometric_1_medium():
    st.write("#### Câu 1.")
    st.write(r"Giải phương trình: $\tan(x) + \cot(x) = 2$, với $x \in [0, \pi]$.")
    submit_button = st.button("See the answers")
    
    return submit_button

def question_trigonometric_2_medium():
    st.write("#### Câu 2.")
    st.write(r"Tính giá trị của $ \displaystyle \sum_{k=1}^{n-1} \left( \sin \dfrac{k\pi}{2n} - \cos \dfrac{k\pi}{2n} \right)$ với $n \geq 2$")
    submit_button = st.button("See the answers")
    
    return submit_button

def question_trigonometric_2_easy():
    st.write("#### Câu 2.")
    st.write("Giải phương trình: $\sin \pi x = \dfrac{1}{2}$ với $x \in [2, 3]$.")
    submit_button = st.button("See the answers")

    return submit_button

def question_trigonometric_1_hard():
    st.write("#### Câu 1.")
    st.write("Phương trình sau có bao nhiêu nghiệm: $\sinh x = \cosh x$")
    submit_button = st.button("See the answers")

    return submit_button

# =========================================================================================================================================== #
#                                                                MA TRAN (question)                                                           #  
# =========================================================================================================================================== #
def question_matrix_1_easy():
    st.write("#### Câu 1.")
    st.write("Tìm định thức của ma trận sau")
    st.write(r"$$ A = \left( \begin{array}{ccc} 1 & 2 & 2 \\ 2 & 2 & 1 \\ 1 & 2 & 1 \end{array} \right) $$")
    submit_button = st.button("See the answers")

    return submit_button

def question_matrix_2_easy():
    st.write("#### Câu 2.")
    st.write("Tìm ma trận nghịch đảo của ma trận sau")
    st.write(r"$$ A = \left( \begin{array}{ccc} 1 & 2 & 2 \\ 2 & 2 & 1 \\ 1 & 2 & 1 \end{array} \right) $$")                            
    submit_button = st.button("See the answers")

    return submit_button

def question_matrix_1_medium():
    st.write("#### Câu 1.")
    st.write("3 phần tử trong một ma trận đối xứng $A$ là các biến ngẫu nhiên có phân phối đều $\mathcal{U}(-a, a)$, hỏi định thức $A$ là bao nhiêu")
    submit_button = st.button("See the answers")

    return submit_button

def question_matrix_2_medium():
    st.write("#### Câu 2.")
    st.write("If A is a skew-symmetric matrix, i.e. $A^T = -A$, then prove that $-A^2$ is symmetric and nonnegative definite matrix.")
    submit_button = st.button("See the answers")
    return submit_button
    
def question_matrix_1_hard():
    st.write("#### Câu 1.")
    st.write(r"Cho $A$ là một ma trận full-rank cấp $m \times n$ và $b \in \mathbb{R}^n$")
    st.write("Giả sử $m < n$, tìm $x \in \mathbb{R}^n$ sao cho $Ax = b$ và đảm bảo")
    st.write(r"$ \qquad x = \argmin_{x \in \mathbb{R}^n} \Vert x \Vert $")
    submit_button = st.button("See the answers")

    return submit_button

def question_matrix_2_hard():
    st.write("#### Câu 2.")
    st.write(r"Cho $A$ là một ma trận full-rank cấp $m \times n$ và $b \in \mathbb{R}^n$")
    st.write("Giả sử $m > n$, tìm $x \in \mathbb{R}^n$ sao cho:")
    st.write(r"$ \qquad x = \argmin_{x \in \mathbb{R}^n} \Vert Ax - b \Vert $")
    submit_button = st.button("See the answers")

    return submit_button

# =========================================================================================================================================== #
#                                                       XAC SUAT THONG KE (question)                                                          #  
# =========================================================================================================================================== #
def question_StatsnProba_1_easy():      
    st.write("#### Câu 1.")
    st.write("The height of men (in inches) in the US is approximately normally distributed with mean 68 inches and standard deviation of 5 inches.")
    st.write("A door frame manufacturer wants to build door frames such that only $2\%$ of all men have to duck their head when walking through the door. How high does the door frame need to be?")                 
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_2_easy():
    st.write("#### Câu 2.")
    st.write("The height of men (in inches) in the US is approximately normally distributed with mean 68 inches and standard deviation of 5 inches.")
    st.write("The weight of men in the US has mean 168 pounds with standard deviation 25 pounds. The correlation between weight and height is 0.35. What conclusions can you make if the correlation were -0.5? What is your best guess of a man’s height if you are told that he weighs 160 pounds?")
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_3_easy():
    st.write("#### Câu 3.")
    st.write("What is the maximal possible variance of a random variable taking value in the interval $[a, b]$")                        
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_4_easy():
    st.write("#### Câu 4.")
    st.write("Knowing that these co-variances $\sigma_{X, Y} > 0$ and $\sigma_{X, Z} < 0$, how can we conclude $\sigma_{Y, Z}$")
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_5_easy():
    st.write("#### Câu 5.")
    st.write(r"Suppose $X$ is a random variable with $\mathbb{E}[X^2] < 1$. What is the constant $c$ that minimizes $\mathbb{E}[(X - c)^2]$?")
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_1_medium():
    st.write("#### Câu 1.")
    st.write("What is the expected number of (fair) coin flips to get two consecutive heads?")
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_2_medium():
    st.write("#### Câu 2.")
    st.write("You are trapped in a dark cave with three indistinguishable exits on the walls. One of the exits takes you 3 hours to travel and takes you outside. One of the other exits takes 1 hour to travel and the other takes 2 hours, but both drop you back in the original cave through the ceiling, which is unreachable from the floor of the cave. You have no way of marking which exits you have attempted. What is the expected time it takes for you to get outside?")      
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_3_medium():
    st.write("#### Câu 3.")
    st.write("$a$ and $b$ are randomly chosen real numbers in the interval [0, 1], that is both $a$ and $b$ are standard uniform random variables. Find the probability that the quadratic equation $x^2 + ax + b = 0$ has real solutions.")
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_1_hard():
    st.write("#### Câu 1.")
    st.write("You have 1000 coins, one of which is faulty: it has a head on both sides. You randomly draw a coin, and, without examining it, toss it 10 times. As it happens, you get 10 heads in a row. What’s the probability that it’s the faulty one?")
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_2_hard():
    st.write("#### Câu 2.")
    st.write("If you repeatedly flip a coin whose probability of heads is p then what is the expected number of flips you need to do in order to get a head immediately followed by a tail?")
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_3_hard():
    st.write("#### Câu 3.")
    st.write("An ant and a blind spider are on opposite corners of a cube. The ant is stationary and the spider moves at random from one corner to another along the edges only. What is the expected number of turns before the spider reaches the ant?")
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_4_hard():
    st.write("#### Câu 4.")
    st.write("Two archers shoot at a target. The distance of each shot from the center of the target is uniformly distributed from 0 to 1, independently of the other shot. What is the PDF (probability density function) of the distance from the center for the winning shot?")
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_5_hard():
    st.write("#### Câu 5")
    st.write("A bug crawls along the edges of a regular tetrahedron ABCD with edges length 1. It starts at A and at each vertex chooses its next edge at random (so it has a $\dfrac{1}{3}$ chance of going back along the edge it came on, and a $\dfrac{1}{3}$ chance of going along each of the other two). Find the probability that after it has crawled a distance 7 it is again at A)")
    submit_button = st.button("See the answers")

    return submit_button

def question_StatsnProba_6_hard():
    st.write("#### Câu 6.")
    st.write("Let U be a uniform random variable on the interval (0, 1). For any continuous distribution function F define the random variable $X = F^{-1}(U)$. What is the distribution of X?")
    submit_button = st.button("See the answers")

    return submit_button

# ===========================================================================================================================================
#                                                          CALCULUS (question)                                                              # 
# ===========================================================================================================================================
def question_Calculus_1_easy():
    st.write("#### Câu 1.")
    st.write("Tính $ \displaystyle \int_{2}^{n} \dfrac{dx}{x(x-1)} $")
    submit_button = st.button("See the answers")

    return submit_button

def question_Calculus_2_easy():
    st.write("#### Câu 1.")
    st.write("Tính $ \displaystyle \int_{-2}^{2} x \cos x dx $")
    submit_button = st.button("See the answers")

    return submit_button

def question_Calculus_1_medium():
    st.write("#### Câu 1.")
    st.write("Tìm $x_t$ biết $x_0 = 1, x^{'}_0 = 1$ và")
    st.write("$\qquad x^{''}_t - 3 x^{'}_t + 2x_t = \sin t $")
    submit_button = st.button("See the answers")

    return submit_button

def question_Calculus_1_hard():
    st.write("#### Câu 1.")
    st.write("Cho phương trình $x^3 + y^3 = 3xy$, hãy xác định $\dfrac{dy}{dx}$")
    submit_button = st.button("See the answers")

    return submit_button

# =========================================================================================================================================== #
#                                                                   LOGICAL (question)                                                        #  
# =========================================================================================================================================== #
def question_logical_1_easy():
    st.write("#### Câu 1.")
    st.write("Có 2 sợi dây kim loại không đồng chất cũng không cùng chiều dài, biết rằng cả 2 sợi dây này đều cháy hết trong 1 giờ khi ta đốt một đầu của nó. Không thể gập sợi dây và chỉ dùng phương pháp đốt, làm thế nào để đo được đúng 45 phút")
    submit_button = st.button("See the answers")

    return submit_button

def question_logical_2_easy():
    st.write("#### Câu 2.")
    st.write("Biết rằng ta có 5 đường đua, mỗi đường đua chỉ được để tối đa 5 con ngựa và giả sử thể lực và tốc độ của chúng không thay đổi sau các lần đua. Hỏi ta cần ít nhất bao nhiêu lần đua để tìm ra 3 con ngựa nhanh nhất trong 25 con ngựa. ")
    submit_button = st.button("See the answers")

    return submit_button

def question_logical_1_medium():
    st.write("#### Câu 1")
    st.write("Snow starts falling sometime before midday. A snow clearing car begins work at midday, and the car's speed is reverse proportion to the time since the snow begain falling. The distance coverd by the snow car from midday until 1pm is double from 1pm to 2pm. When does the snow start?")
    submit_button = st.button("See the answers")

    return submit_button

def question_logical_2_medium():
    st.write("#### Câu 2")
    st.write("One morning, in Springfield, somewhere in the US, it started snowing at a heavy but constant rate. Homer Simpson had just started his own snowplow business. His snowplow started out at 8:00 A.M. At 9:00 A.M. it had gone 2 miles. By 10:00 A.M. it had gone 3 miles. Assuming that the snowplow removes a constant volume of snow per hour, determine the time at which it started snowing")
    submit_button = st.button("See the answers")

    return submit_button

def question_logical_1_hard():
    st.write("#### Câu 1.")
    st.write("What is the last 4 digits of $2015^{2013 ^ {2014} }$")
    submit_button = st.button("See the answers")
    
    return submit_button

# =========================================================================================================================================== #
#                                                                   SO HOC (question)                                                         #  
# =========================================================================================================================================== #
def question_numeric_serial_1_easy():
    st.write("#### Câu 1.")
    st.write(r"Cho $a_n = \left( 1 - \frac{1}{n} \right)^n$")
    st.write(r"Tính $a_n$ khi $n \to \infty$ hay $\lim_{n \to \infty} a_n$")
    submit_button = st.button("See the answers")

    return submit_button

def question_numeric_serial_1_medium():
    st.write("#### Câu 1.")
    st.write(r"Cho $a_n = \underset{n \text{ times of the root-squared}}{\underbrace{\sqrt{3 * \sqrt{3 * ... * \sqrt{3}}}}}$")
    st.write(r"Tính $a_n$ khi $n \to \infty$ hay $\lim_{n \to \infty} a_n$")
    submit_button = st.button("See the answers")
    
    return submit_button

def question_numeric_serial_1_hard():
    st.write("#### Câu 1.")
    st.write(r"Cho $a_n = \frac{1}{1 + \frac{1}{1+\frac{1}{ 1 + \frac{1}{1 + ...} }}}$")
    st.write(r"Tính $a_n$ khi $n \to \infty$ hay $\lim_{n \to \infty} a_n$")
    submit_button = st.button("See the answers")

    return submit_button

def question_numeric_serial_2_hard():
    st.write("#### Câu 2.")
    st.write(r"Cho $a_n = \underset{n \text{ times of the root-squared}}{\underbrace{\sqrt{3 + \sqrt{3 + ... + \sqrt{3}}}}}$")
    st.write(r"Tính $a_n$ khi $n \to \infty$ hay $\lim_{n \to \infty} a_n$")
    submit_button = st.button("See the answers")
    
    return submit_button

# =========================================================================================================================================== #
#                                                                   ALGO (question)                                                           #  
# =========================================================================================================================================== #
def question_algorithm_1_easy():
    st.write("#### Câu 1.")
    st.write("Cho đoạn script sau:")
    st.markdown("```\nsum = 0\nfor n in range(1, 100)\n    if n odd:\n        sum = sum + n\n    else:\n        sum = sum - 2```")
    st.write("Hỏi `sum` bằng bao nhiêu?")
    submit_button = st.button("See the answers")
    
    return submit_button
    
# =========================================================================================================================================== #
#                                                                    Solutions                                                                #
# =========================================================================================================================================== #
#                                                            XAC SUAT THONG KE (solution)                                                     #  
# =========================================================================================================================================== #
def solution_StatsnProba_1_easy():
    st.write("#### Answers")
    st.write("To find the height corresponding to the top 98%, we first need to find the Z-score that corresponds to the 98th percentile of the normal distribution. The Z-score for the 98th percentile can be found using a standard normal table or a calculator.")   
    st.write(r"For any normal distribution $Z \sim \mathcal{N}(\mu, \sigma)$ where $\mu = 68$ and $\sigma = 5$, then the 98th percentile is approximately")
    st.write(r"$\qquad \qquad z_{0.98} \approx 2.054$")
    st.write("and the height of the door frame is")
    st.write(r"$ \qquad \qquad \sigma z_{0.98} + \mu \approx 78.27$")

def solution_StatsnProba_2_easy():
    st.write("#### Answers")
    st.write("Đặt:")
    st.write(r"$\qquad \mu_1, \sigma_1$ tương ứng với kỳ vọng và độ lệch chuẩn của chiều cao")
    st.write(r"$\qquad \mu_2, \sigma_2$ tương ứng cho kỳ vọng và độ lệch chuẩn của cân nặng")
    st.write("$\diamond$ Khi đó, với $r = 0.35$ và $w_h = 160$ pounds, ta có")
    st.write(r"$\quad \qquad \qquad \sigma_{1, 2} = r_{1, 2} \times \sigma_1 \times \sigma_2 = 43.75$")
    st.write("và")
    st.write(r"$\qquad \qquad \begin{array}{ccc} \hat{h} &=& \mu_1 + \dfrac{\sigma_{1, 2}}{\sigma_1^2} (w_h - \mu_2) \\ \\ &=& 68 + \dfrac{43.75}{25^2} (160 - 168) &\approx & 67.44 \end{array}$")
    st.write("$\diamond$ Tương tự với $r = -0.5$, ta có")
    st.write(r"$\quad \qquad \qquad \sigma_{1, 2} = r_{1, 2} \times \sigma_1 \times \sigma_2 = -37.5$")
    st.write("và")
    st.write(r"$\qquad \qquad \begin{array}{ccc} \hat{h} &=& \mu_1 + \dfrac{\sigma_{1, 2}}{\sigma_1^2} (w_h - \mu_2) \\ \\ &=& 68 + \dfrac{-37.5}{25^2} (160 - 168) &\approx & 68.48 \end{array}$")    

def solution_StatsnProba_3_easy_additional():
    st.write("Tổng quát, với $n$ điểm $x_1, \ldots, x_n \in (a, b)$")
    st.write(r"$\qquad \mathcal{L}(x, \lambda, p) = \sum_{k=1}^n p_k (x_k - c)^2 + \lambda ( \sum_{k=1}^n p_k - 1)$")
    st.write("Do đó,")
    st.write(r"$ \qquad \qquad \left\lbrace \begin{array}{ccl} c &=& \displaystyle \sum_{k=1}^n p_k x_k \\ \\ \lambda &=& -(c - x_k)^2 \quad \forall k  \end{array} \right.$")
    st.write("tức là")
    st.write("$\qquad \qquad |x_1 - c| = |x_2 - c| = \ldots = |x_n - c|$")
    st.write(r"tương đương $c = \frac{1}{n}\sum_{k=1}^n x_k$ và $\text{Var} X = \frac{1}{n}\sum_{k=1}^n (x_k - c)^2$")
    
def solution_StatsnProba_3_easy():
    st.write("#### Answers")
    st.write("Nhận xét:")
    st.write("$\qquad \diamond$ Biến ngẫu nhiên chỉ nhận 2 giá trị trên khoảng (a, b) sẽ có phương sai cao hơn khi nhận nhiều giá trị hơn.")
    st.write("$\qquad \diamond$ Với biến ngẫu nhiên chỉ nhận 2 giá trị, giả sử")
    st.write("$\qquad \qquad \qquad P(X=a) = p_a $ và $P(X = b) = p_b$")
    st.write("$\qquad \qquad$ Khi đó,")
    st.write(r"$\qquad \qquad \quad $ Var $X := \mathbb{E}(X - \mathbb{E}X)^2 \leq \mathbb{E}(X - c)^2 $")
    st.write("$\qquad$ trong đó $c \in (a, b)$, do $X$ nhận giá trị trên $(a, b)$. Không mất tính tổng quát, ")
    st.write(r"$\qquad \qquad \qquad c := \mathbb{E} X = a p_a + b p_b $")
    st.write("$\qquad \qquad$ Mặt khác,")
    st.write(r"$\qquad \qquad \qquad \text{Var} X = p_a (a - c)^2 + p_b ( b - c)^2 $")
    st.write(r"$\qquad \qquad$ Với $p_a + p_b = 1$, khi đó $\text{Var} X \to \max$ khi và chỉ khi")
    st.write(r"$\qquad \qquad \qquad \qquad \begin{array}{ccc} \frac{d \mathcal{L}}{d p_a} = 0 & \frac{d \mathcal{L}}{d p_b} = 0 & \frac{d \mathcal{L}}{d c} = 0\end{array}$")
    st.write("$\qquad \qquad$ trong đó $\mathcal{L} := \mathcal{L}(\lambda, p_a, p_b, c)$ với")
    st.write(r"$\qquad \qquad \quad \mathcal{L} = p_a (a - c)^2 + p_b ( b - c)^2 + \lambda (p_a + p_b - 1) $")
    st.write(r"$\qquad \qquad$ dễ thấy rằng cặp $\frac{d \mathcal{L}}{d p_a} = 0 $ và $\frac{d \mathcal{L}}{d p_b} = 0 $ suy ra")
    st.write(r"$\qquad \qquad \quad \left( \lambda + (a - c)^2 \right) = 0$ và $\left( \lambda + (b - c)^2 \right) = 0$")
    st.write(r"$\qquad \qquad \qquad \begin{array}{cccc} \Leftrightarrow & (a-c)^2 - (b-c)^2 &=& 0 \\ \\ \Leftrightarrow & a^2 - b^2 - 2c(a-b) &=&0 \end{array} $")
    st.write(r"$\qquad \qquad$ dẫn đến $c = \dfrac{a + b}{2},$ tuần tự ta tìm được")
    st.write("$\qquad \qquad \qquad \qquad p_a = p_b = \dfrac{1}{2}$ và $c = \dfrac{a+b}{2}$")
    st.write("$\qquad \qquad$ Như vây, phương sai đạt cực đại tại")
    st.write(r"$\qquad \qquad \qquad \qquad \quad \text{Var} X = \dfrac{(b-a)^2}{4}$")    

def solution_StatsnProba_4_easy():
    st.write("#### Answers")
    st.write("Từ các giả thiết trên, ta thấy rằng")
    st.write(r"$\qquad \diamond X, Y$ là `tương quan thuận (positively correlated)`")
    st.write(r"$\qquad \diamond Y, Z$ là `tương quan nghịch (negatively correlated)`")
    st.write("Do đó, ")
    st.write(r"$\qquad \bullet X$ tăng thì $Y$ tăng nhưng $Z$ lại giảm")
    st.write(r"$\qquad \bullet X$ giảm thì $Y$ giảm nhưng $Z$ lại tăng")
    st.write("Vì vậy, $X, Z$ là tương quan nghịch nên")
    st.write(r"$\qquad \qquad \qquad \qquad \qquad \sigma_{X, Z} < 0$")

def solution_StatsnProba_5_easy():
    st.write("#### Answers")
    st.write("Đặt")
    st.write(r"$\qquad \qquad \qquad f(c) = \mathbb{E}(X - c)^2$")
    st.write("khi đó,")
    st.write(r"$\qquad \qquad f(c) = \mathbb{E}X^2 - 2c\mathbb{E}X + c^2$")
    st.write("Dễ thấy rằng $f(c) > 0$ và $f$ là một hàm lồi nên cực tiểu xảy ra khi và chỉ khi")
    st.write(r"$\qquad \begin{array}{cccccc} \dfrac{df}{dc} &=& 0 &\Leftrightarrow & \dfrac{d}{dc} \left( \mathbb{E}X^2 - 2c \mathbb{E}X + c^2 \right) & = & 0 \\ \\ &&& \Rightarrow & -2 \mathbb{E}X + 2c &=& 0 \\ &&& \Rightarrow & c &=& \mathbb{E}X \end{array} $")

def solution_StatsnProba_1_medium():
    st.write("#### Answers")

def solution_StatsnProba_2_medium():
    st.write("#### Answers")

def solution_StatsnProba_4_hard():
    st.write("#### Answers")                            
    st.write("Đặt $r_1, r_2$")

# =========================================================================================================================================== #
#                                                               CALCULUS (solution)                                                           #  
# =========================================================================================================================================== #
def solution_Calculus_1_easy():
    st.write("#### Answers")
    st.write(r"$\forall n \geq 2$, ta có")
    st.write(r" $ \begin{array}{ccc} \displaystyle \int_2^n \dfrac{dx}{x(x-1)} &=& \displaystyle \int_2^n \left( \dfrac{1}{x-1} - \dfrac{1}{x} \right) dx \\ \\ &=& \left. \ln \left( \dfrac{x-1}{x} \right) \right| _{x=2}^{x=n} \\ \\ &=& \ln \left( \frac{n-1}{n} \right) - \ln \frac{1}{2} \\ \\ &=& \ln \frac{2(n-1)}{n} \end{array} $ ")

def solution_Calculus_2_easy():
    st.write("#### Answers")
    st.write("Dễ thấy rằng $x \cos x$ là hàm lẻ nên tích phân trên miền đối xứng sẽ bằng 0.")

def solution_Calculus_1_medium():
    st.write("#### Answers")
    st.write("Bài toán này là dạng PTVP không thuần nhất, ở dạng thuần nhất thì nó sẽ được đưa về phương trình đặc trưng với")
    st.write(r"$\qquad \qquad r^2 - 3r + 2 = 0 \Leftrightarrow r = \lbrace 1, 2 \rbrace $")
    st.write("do đó, nghiệm tổng quát của nó khi thuần nhất sẽ có dạng")
    st.write(r"$ \qquad \qquad x_t = c_1 e^t + c_2 e^{2t} $")
    st.write("Do đây là dạng không thuần nhất, nên")
    st.write(r"$ \qquad \qquad x_t = c_1 e^t + c_2 e^{2t} + c_3 \sin t + c_4 \cos t$")
    st.write("Trong đó, phần $z_t = c_3 \sin t + c_4 \cos t$ được gọi là nghiệm đặc trưng (cho dạng không thuần nhất), và")
    st.write(r"$ \begin{array}{ccl} z_t'' - 3z_t' + 2z_t = \sin t & \Leftrightarrow & (-c_4 - 3c_3 + 2c_4) \cos t + \\  & & + (-c_3 + 3c_4 + 2c_3) \sin t = \sin t \\ \\ & \Leftrightarrow & \left[ \begin{array}{ccc} -3c_3 + c_4 &=& 0 \\ c_3 + 3c_4 &=& 1 \end{array} \right. \\ \\ & \Leftrightarrow & \left\lbrace \begin{array}{ccc} c_3 &=& \frac{1}{10} \\ \\ c_4 &=& \frac{3}{10} \end{array} \right. \end{array}  $")  
    st.write(r"Như vậy, $x_t = c_1 e^t + c_2 e^{2t} + \frac{1}{10} \sin t + \frac{3}{10} \cos t$, kết hợp với cặp điều kiện đầu, ta được")
    st.write(r"$ \left[ \begin{array}{ccl} x_t &=& 0 \\ x_t' &=& 1 \end{array} \right. \Leftrightarrow \left[ \begin{array}{ccl} c_1 + c_2 + \frac{3}{10} &=& 0 \\ \\ c_1 + 2c_2 - \frac{3}{10} &=& 1 \end{array} \right. \Leftrightarrow \left[ \begin{array}{ccc} c_1 &=& -\frac{19}{10} \\ c_2 &=& \frac{8}{5} \end{array} \right. $")
    st.write("Do đó,")
    st.write(r"$\qquad x_t = -\frac{19}{10}e^t + \frac{8}{5} e^{2t} - \frac{1}{10} \sin t + \frac{3}{10} \cos t $")

# =========================================================================================================================================== #
#                                                                SO HOC (solution)                                                            #
# =========================================================================================================================================== #
def solution_numeric_serial_2_hard():
    st.write("#### Answers")
    st.write(r"Ta thấy rằng : $ a_n^2 = 3 + a_n, \qquad \forall n $ với $a_n > 0$")
    st.write("Do đó")
    st.write(r"$a_n = \dfrac{1+\sqrt{13}}{2} \approx 2.308 $")
  
def solution_numeric_serial_1_hard():
    st.write("#### Answers")
    st.write(r"Ta thấy rằng : $ a_n \left( 1 + a_n \right) = 1, \qquad \forall n $ với $a_n \in (0, 1)$")
    st.write("Do đó")
    st.write(r"$a_n = \dfrac{-1+\sqrt{5}}{2} \approx 2.308 $")

def solution_numeric_serial_1_medium():
    st.write("#### Answers")
    st.write(r"Ta thấy rằng : $ a_n^2 = 3 * a_n, \qquad \forall n $ với $a_n > 0$")
    st.write("Do đó")
    st.write(r"$a_n = 3 $")

def solution_numeric_serial_1_easy():
    st.write("#### Answers")
    st.write(r"Chú ý công thức tổng quát: $$  \left( 1 + \frac{c}{n} \right)^n \to e^{c} $$")
    st.write(r"Do đó, $a_n \to \dfrac{1}{e} \approx 0.3678 $")

# =========================================================================================================================================== #    
#                                                                HINH HOC (solution)                                                          #
# =========================================================================================================================================== #
def solution_hinh_hoc_1_medium():    
    st.write("#### Answers")
    st.write("Trên các mặt $(ABC), (ABD), (BCD), (ACD)$ lần lượt lấy các điểm $M, N, Q, P$, khi đó ta dễ dàng có được dạng tọa độ tổng quát")
    st.write(r"$\qquad M \left( \dfrac{x_A + x_B + x_C}{3}, \dfrac{y_A + y_B + y_C}{3}, \dfrac{z_A + z_B + z_C}{3} \right)$")
    st.write("Tương tự")
    st.write(r"$\qquad N \left( \dfrac{x_A + x_B + x_D}{3}, \dfrac{y_A + y_B + y_D}{3}, \dfrac{z_A + z_B + z_D}{3} \right)$")                            
    st.write("Suy ra: ")
    st.write(r"$\begin{array}{ccl} \overrightarrow{MN} &=& \left( x_N - x_M, y_N - y_M, z_N - z_M \right) \\ &=& \left( \dfrac{x_D - x_C}{3}, \dfrac{y_D - y_C}{3}, \dfrac{z_D - z_C}{3} \right) = \dfrac{1}{3}\overrightarrow{CD} \end{array}$")
    st.write("Do đó")
    st.write(r"$ \qquad \qquad \dfrac{PM}{AD} = \dfrac{PQ}{AB} = \dfrac{NQ}{AC} = \dfrac{MN}{CD} = \dfrac{1}{3} $")
    st.write("Vậy $\dfrac{V_{ABCD}}{V_{MNPQ}} = \dfrac{1}{27}$")

def solution_hinh_hoc_2_medium():
    st.write("#### Answers")
    st.write("Đặt $V_t, S_t$ lần lượt là thể tích và diện tích bề mặt của khối băng tại thời điểm $t$, ta thấy rằng :")
    st.write("$\qquad \diamond \; dV_t = -4 cm^3 /$min là tốc độ ta của khối băng")
    st.write("$\qquad \diamond \; V_0 = 125 cm^3$ là thể tích ban đầu của khối băng (cạnh $5 cm$)")
    st.write("Theo công thức đạo hàm của hàm số hợp, ta có")
    st.write(r"$\quad \qquad \dfrac{dS}{dt} = \dfrac{dS}{dV} \times \dfrac{dV}{dt} = -4 \dfrac{dS}{dV} $")
    st.write("Lại có $S = 6a^2$ với $a$ là cạnh của hình lập phương nên")
    st.write(r"$\qquad \qquad \qquad S = 6 V^{2/3} \Rightarrow \dfrac{dS}{dV} = 4V^{-1/3}$")
    st.write("Do đó,")
    st.write("$\qquad \quad \qquad \dfrac{dS}{dt} = 16 V^{-1/3} = \dfrac{16}{ \sqrt[3]{125} } = 3.2 cm^3/$ min")
        
def solution_hinh_hoc_1_easy():
    st.write("#### Answers")
    st.write("Dễ thấy rằng đây là tam giác vuông tại $A$ với cạnh huyền $BC$, do đó")
    st.write(r"$BC = \dfrac{AB \cdot AC}{BC} = 4.8$")
    
def solution_hinh_hoc_1_hard():
    st.write("#### Answers")    
    st.write("Lấy các đỉnh $I_1 - I_6$ là các đỉnh của khối bát diện (2 hình chóp đáy hình vuông ghép lại) với thể tích $V_b$ cũng đồng thời là tâm trên 6 mặt của khối lập phương $V_a$ này, giả sử")
    st.write("$\qquad I_1(0, -a, 0) \in (A'B'BA)$ và $I_2(0, a, 0) \in (D'C'CD)$")
    st.write("$\qquad I_3(0, 0, -a) \in (ABCD)$ và $I_4(0, 0, a) \in (A'B'C'D')$")
    st.write("$\qquad I_5(-a, 0, 0) \in (A'D'DA)$ và $I_6(a, 0, 0) \in (B'C'CB)$")
    st.write("Đặt $O_1 - O_8$ lần lượt là 8 trọng tâm tương ứng trên khối bát diện này, giả sử")
    st.write(r"$\qquad O_1\left( \dfrac{a}{3}, \dfrac{-a}{3}, \dfrac{a}{3} \right) \in \left( I_4 I_1 I_6 \right)$ và $O_2 \left( \dfrac{a}{3}, \dfrac{-a}{3}, \dfrac{-a}{3} \right) \in \left( I_3 I_1 I_6 \right)$")
    st.write("Do đó,")
    st.write(r"$\qquad \overrightarrow{O_1 O_2} = \dfrac{1}{3} \overrightarrow{B'B} = \dfrac{1}{3} \overrightarrow{A'A} = \ldots = \dfrac{1}{3} \overrightarrow{D'D}$")
    st.write("Như vậy,")
    st.write(" $\qquad V_c = \dfrac{1}{27} V_a$ và do đó $V_a = 27$")
    st.write(r"$ \qquad \begin{array}{ccl} V_b &=& 2 V_{I_4 (I_2 I_6 I_1 I_5)} \\  &=& 2 \left( \dfrac{h S_{(I_2 I_6 I_1 I_5)}} {3} \right) \\ &=& \dfrac{2 a * a (a\sqrt{2})^2}{3} = \dfrac{8\sqrt{2}a^3}{3} \end{array}$")
    st.write("Chú ý rằng, $h = d_{(I_4, (I_2 I_6 I_1 I_5))} = a$ và $(I_2 I_6 I_1 I_5)$ là đáy hình vuông với cạnh $I_1 I_6 = a\sqrt{2}$")

def solution_hinh_hoc_2_hard():
    st.write("#### Answers")
    st.write(r"Từ các giả thiết về góc bán phương, ta được $\dfrac{h}{R} = \tan \theta = \dfrac{1}{2}$ hay $R=2h$")
    st.write("Với $h, R$ lần lượt là chiều cao và bán kính của nón, ta có")
    st.write(r"$\qquad \quad \qquad \qquad V = \dfrac{1}{3} \pi R^2 h = \dfrac{\pi}{3} 4 h^3$")
    st.write("và")
    st.write(r"$\qquad \quad \qquad \dfrac{dV}{dt} = \dfrac{4\pi}{3} \dfrac{d}{dt} \left( h^3_t \right) = 4\pi h^2 \times \dfrac{dh}{dt}$")
    st.write("Do đó, ")
    st.write(r"$\qquad \qquad \qquad \qquad \dfrac{dh}{dt} = \dfrac{1}{4 \pi h^2} \dfrac{dV}{dt}$")
    st.write("Mặt khác, nước được đổ vào với tốc độ không đổi $k$, tức là $k = \dfrac{dV}{dt}$, nên")
    st.write(r"$\qquad \quad \qquad \qquad \qquad \dfrac{dh}{dt} = \dfrac{k}{4 \pi h^2}$")
    st.write(r"Để con nhện không bị ướt, tốc độ chạy của nó phải đủ lớn để nó có thể chạy lên và thoát khỏi nước trước khi nước đạt đến độ cao $h_0$. Thời gian để nước dâng từ độ cao $0$ đến độ cao $h_0$ là:")
    st.write(r"$\qquad \qquad t_{\text{escape}} = \displaystyle \int_{0}^{h_0} \dfrac{dt}{dh} = \int_0^{h_0} \dfrac{4\pi}{k} h^2 dh = \dfrac{4\pi h_0^3}{3k}$")
    st.write("Do đó, tốc độ tối thiểu $u$ mà con nhện cần để thoát là")
    st.write(r"$\qquad \quad \qquad \qquad u \geq \dfrac{h_0}{t_{\text{escape}}} = \dfrac{3k}{4\pi h_0^2}$")
    
def solution_hinh_hoc_3_hard():
    st.write("#### Answers")
    st.write(r"Dễ thấy rằng $\bigtriangleup ABC$ là một tam giác vuông. Không mất tính tổng quát, ta giả sử nó vuông tại $A$ với $ AB=45, AC=60 $, do đó")
    st.write(r"$\qquad \qquad S_{\bigtriangleup ABC} = \dfrac{1}{2} AB . AC = 1350 $")
    st.write("Đặt $h_a, h_b, h_c$ là các khoảng cách từ $D$ đến các cạnh $BC, AC, AB$ của tam giác, khi đó ta cần tính")
    st.write(r"$ \qquad \qquad \mathbb{E} \left( h_a + h_b + h_c \right) $")
    st.write("Ta có:")
    st.write(r"$\quad \mathbb{E} h_a = \mathbb{E} \left( \lbrace D \in \bigtriangleup ABC, D \in h_a: h_a \perp BC \rbrace \right) = \frac{2S}{BC} = 18$")
    st.write(r"$\quad \mathbb{E} h_b = \mathbb{E} \left( \lbrace D \in \bigtriangleup ABC, D \in h_b: h_b \perp AC \rbrace \right) = \frac{2S}{AC} = 22.5$")
    st.write(r"$\quad \mathbb{E} h_c = \mathbb{E} \left( \lbrace D \in \bigtriangleup ABC, D \in h_c: h_c \perp AB \rbrace \right) = \frac{2S}{AB} = 30$")                                                        
    st.write(r"Như vậy, $\mathbb{E} \left( h_a + h_b + h_c \right) = 70.5$")
    


def additional_explaination():
    st.write(r"Có thể lấy các đỉnh hình lập phương $ABCD A'B'C'D'$ này có dạng $\left( \pm a, \pm a, \pm a \right)$")
    st.write('Không mất tính tổng quát, giả sử:')                        
    st.write(r"$A(-a, -a, -a), B( a, -a, -a), C( a,  a, -a), D(-a,  a, -a)$")
    st.write(r"$A'(-a, -a,  a), B'(a, -a,  a), C'( a,  a,  a), D'(-a,  a,  a)$")                        

# =========================================================================================================================================== #
#                                                               LUONG GIAC (solution)                                                         #  
# =========================================================================================================================================== #
def solution_trigonometric_1_easy():
    st.write("#### Answers")
    st.write("Dễ thấy:")
    st.write(r"$ \qquad \sin \dfrac{\pi}{6} + \sin \dfrac{\pi}{4} + \sin \dfrac{\pi}{3} = \dfrac{1}{2} \left( 1 + \sqrt{2} + \sqrt{3} \right) $")

def solution_trigonometric_2_easy():
    st.write("#### Answers")
    st.write(r"Dễ thấy rằng $\sin \pi x = \dfrac{1}{2}$ nên $ \left[ \begin{array}{ccc} \pi x &=& \frac{\pi}{6} + k2\pi \\ \pi x &=& \frac{5\pi}{6} + k2 \pi \end{array} \right.$")
    st.write("Kết hợp với điều kiện $x \in [2, 3]$, do đó")
    st.write(r"$\qquad \qquad x = \left \lbrace \dfrac{13}{6}, \dfrac{17}{6} \right \rbrace $")    

def solution_trigonometric_1_medium():
    st.write("#### Answers")
    st.write(r"Với điều kiện đề bài, miền xác định bài toán sẽ là $x \in \left(0, \frac{\pi}{2} \right) \cup \left( \frac{\pi}{2}, \pi \right) $")
    st.write(r"Đặt $u = \tan x$, khi đó $\cot x = u^{-1}$ với $u \neq 0$")
    st.write(r"Khi đó, $u = 1$ và $x = \arctan 1$")
    st.write("Kết hợp với điều kiện đầu bài, ta được $x = \dfrac{\pi}{4}$")

def solution_trigonometric_2_medium():
    st.write("#### Answers")
    st.write("Dễ thấy rằng")
    st.write(r"$ \qquad \sin \dfrac{k \pi}{2n} = \cos \left( \dfrac{\pi}{2} - \dfrac{k \pi}{2n} \right) = \cos \left( \dfrac{ (n - k - 1) \pi}{2n} \right), \qquad \forall n$")
    st.write("Do đó,")
    st.write(r"$ \begin{array}{ccc} \displaystyle \sum_{k=1}^{n} \left( \sin \dfrac{k \pi}{2n} - \cos \dfrac{k \pi}{2n}  \right) &=& \displaystyle \sum_{k=1}^{n} \left( \cos \left( \dfrac{(n - k - 1) \pi}{2n} \right) - \cos \dfrac{k \pi}{2n} \right) \\ &=& \displaystyle \sum_{k=1}^{n} \left( \cos \dfrac{(n - k - 1) \pi}{2n} - \cos \dfrac{k \pi}{2n} \right) \\ &=& 0 \end{array} $")

def solution_trigonometric_1_hard():
    st.write("#### Answers")
    st.write("Ta thấy rằng:")
    st.write(r"$\qquad \sinh x = \dfrac{e^x - e^{-x}}{2}$")
    st.write("và")
    st.write(r"$\qquad \cosh x = \dfrac{e^x + e^{-x}}{2}$")
    st.write("Vậy,")
    st.write(r"$ \qquad \begin{array}{lccl} & \sinh x &=& \cosh x \\ \\ \Leftrightarrow & \dfrac{e^x - e^{-x}}{2} &=& \dfrac{e^x + e^{-x}}{2} \\ \\ \Leftrightarrow & e^{-x} &=& 0 \end{array}$")
    st.write("Do đó, phương trình trên là vô nghiệm")

# =========================================================================================================================================== #
#                                                                    MA TRAN (solution)                                                       #  
# =========================================================================================================================================== #
def solution_matrix_1_easy():
    st.write("#### Answers")
    st.write('**Cách 1.** Thực hiện biến đổi sơ cấp, ta được')
    st.write(r"$ \qquad \left( \begin{array}{ccl} 1&2&2 \\ 2&2&1 \\ 1&2&1 \end{array} \right) \underset{d_3:d_3 -d_1}{\overset{d_2: d_2 - 2d_1}{\longrightarrow }} \left( \begin{array}{ccl} 1&2&2 \\ 0&-2&-3 \\ 0&0&-1 \end{array} \right) $")
    st.write("Do đó, $\det A = 2$")
    st.write('**Cách 2.** Tính các định thức cấp con trên hàng / cột, tổng quát với')
    st.write(r"$\qquad \qquad A = \left( a_{i, j} \right)_{1 \leq i,j \leq n}$")
    st.write("khi đó,")
    st.write(r"$ \begin{array}{ccl} \det A &=& \displaystyle  \sum_{j=1}^{n} (-1)^{i+j} a_{ij} \cdot \text{det}(A_{ij}) \\ &=& a_{11} \cdot \left \Vert \begin{matrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{matrix} \right\Vert - a_{12} \cdot \left\Vert \begin{matrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{matrix} \right\Vert + a_{13} \cdot \left\Vert \begin{matrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{matrix} \right\Vert \\ &=& 1 \cdot \left \Vert \begin{matrix} 2&1 \\ 2&1 \end{matrix} \right\Vert - 2 \cdot \left \Vert \begin{matrix} 2&1 \\ 1&1 \end{matrix} \right\Vert + 2 \cdot \left \Vert \begin{matrix} 2&2 \\ 1&2 \end{matrix} \right\Vert \\ &=& 2 \end{array} $")

def solution_matrix_2_easy():
    st.write("#### Answers")
    st.write("Lại áp dụng kỹ thuật biến đổi sơ cấp")
    st.write(r"$ \begin{array}{rcl} [A | I] &=& \left[\begin{array}{ccc|ccc} 1 & 2 & 2 & 1 & 0 & 0 \\ 2 & 2 & 1 & 0 & 1 & 0 \\ 1 & 2 & 1 & 0 & 0 & 1 \end{array}\right] \\ \\ &=& \left[\begin{array}{ccc|ccc} 1 & 2 & 2 & 1 & 0 & 0 \\ 0 & -2 & -3 & -2 & 1 & 0 \\ 0 & 0 & -1 & -1 & 0 & 1 \end{array}\right] \\ \\ &=& \left[\begin{array}{ccc|ccc} 1 & 2 & 2 & 1 & 0 & 0 \\ 0 & 1 & \frac{3}{2} & 1 & -\frac{1}{2} & 0 \\ 0 & 0 & 1 & 1 & 0 & -1 \end{array}\right] \\ \\ &=& \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & 3 & -1 & 2 \\ 0 & 1 & 0 & 1 & -\frac{1}{2} & \frac{3}{2} \\ 0 & 0 & 1 & 1 & 0 & -1 \end{array}\right] \\ \\ &=& \left[I | A^{-1} \right] \end{array} $")    
    st.write("Do đó,")
    st.write(r"$\qquad \qquad  A^{-1} = \left[\begin{array}{ccc} 3 & -1 & 2 \\ 1 & -\frac{1}{2} & \frac{3}{2} \\ 1 & 0 & -1 \end{array}\right]$")

def solution_matrix_1_medium():
    st.write("#### Answers")
    st.write("Vì $A$ là ma trận đối xứng, nên")
    st.write("$ \qquad \qquad \det A = X_{1,1} X_{2,2} - X_{1, 2}^2 $")
    st.write(r"trong đó, $X_{1,1}, X_{1,2}, X_{2,2} \sim \mathcal{U}(-a, a)$")
    st.write("Do đó,")
    st.write(r"$\qquad \mathbb{E} \det A = \mathbb{E}(X_{1,1} X_{2, 2}) - \mathbb{E} X_{1,2}^2$")
    st.write("Hơn nữa, do các biến ngẫu nhiên này là độc lập, nên")
    st.write(r"$\qquad \begin{array}{ccl} \mathbb{E} \det A &=& \mathbb{E}X_{1,1} \mathbb{E} X_{2, 2} - \mathbb{E} X_{1,2}^2 \\ &=& \left( \mathbb{E} Z \right)^2 - \mathbb{E} \left( Z^2 \right) \\ &=& - \dfrac{a^2}{3} \end{array} $")
    st.write("trong đó, $Z \sim \mathcal{U}(-a, a) $")

def solution_matrix_2_medium():
    st.write("#### Answers")
    st.write("$\diamond$ We have $-A^2$ is symmetric, indeed")
    st.write(r"$\quad \begin{array}{cclll} (-A^2)^T &=& (-A \cdot A)^T &=& A^T \cdot (-A)^T \\ &&&=& -A \cdot (A^T)^T \\ &&&=& -A \cdot A \\ &&&=& -A^2 \end{array}$")
    st.write(r"Moreover, for all $w \in \mathbb{R}^n$, we have")
    st.write(r"$\qquad \begin{array}{ccl} w^T (-A^2) w &=& w^T \cdot \left( (-A) \cdot A \right) \cdot w \\ &=& w^T \cdot \left( A^T \cdot A \right) \cdot w \\ &=& (A w)^T (Aw) \\ &\geq& 0 \end{array}$")
    st.write("$\diamond$ Hence, $-A^2$ is non-negative define")
            
def solution_matrix_1_hard():
    st.write("#### Answers")
    st.write(r"The problem becomes: $\left\lbrace \begin{array}{cclr} Ax &=& b & \text{(constraints)} \\ \Vert x \Vert &=& \displaystyle \sum_{k=1}^n x_k^2 \to \min & \text{(objective)} \end{array} \right.$")
    st.write("By Larrange's multiplier, we let")
    st.write(r"$\qquad F(x) = F(x_1, \ldots, x_n) = Ax - b$, and")
    st.write(r"$\qquad \Phi(x) = \Phi(x_1, \ldots, x_n) = x^T x $")
    st.write("then, we need to minimize ")
    st.write(r"$\qquad \mathcal{L}(x, \lambda) = \Phi(x) + \lambda F(x) = x^T x + \lambda^T (Ax - b)$")
    st.write("We have")
    st.write(r"$\left\lbrace \begin{array}{ccl} \frac{d \mathcal{L}}{d\lambda} &=& 0 \\ \\ \frac{d \mathcal{L}}{dx} &=& 0 \end{array} \right. \Leftrightarrow \left\lbrace \begin{array}{ccl} Ax - b &=& 0 \\ 2x^T + \lambda^T A &=& 0 \end{array} \right. \Rightarrow \left\lbrace \begin{array}{ccl} Ax &=& b \\ \\ x^T &=& -\frac{\lambda^T A}{2} \end{array} \right. $")
    st.write("Hence, we obtain")
    st.write(r"$\qquad \qquad \qquad x = -\frac{1}{2} A^T \lambda$")
    st.write("and,")
    st.write(r"$\qquad A \left( -\frac{1}{2} A^T \lambda \right) = b \Leftrightarrow -(A A^T) \lambda = 2b$, since $AA^T$ is invertible matrix, hence")
    st.write(r"$\qquad \qquad \qquad \lambda = - (AA^T)^{-1} 2b $")
    st.write("and,")
    st.write(r"$\qquad \qquad \begin{array}{cccc} x &=& -\frac{1}{2} A^T \left( -(A A^T)^{-1} 2b \right) &=& A^T (A A^T)^{-1} b \end{array} $")

def solution_matrix_2_hard():
    st.write("#### Answers")
    st.write("Consider")
    st.write(r"$\qquad \mathcal{L}(x) = \Vert Ax - b \Vert^2 = (A x - b)^T (A x - b) $")
    st.write("Hence,")
    st.write(r"$\qquad \begin{array}{ccl} \dfrac{d \mathcal{L}}{dx} &=& \dfrac{d}{dx} \left[ x^T (A^T A) x - b^T (A x) - (A x)^T b + b^T b \right] \\ \\ &=& 2 x^T (A^T A) - 2b^T A \end{array}$")
    st.write(r"Since $A_{m \times n}$ is full-rank (with $m > n$) hence $(A^T A)$ is invertible and")
    st.write(r"$\qquad \qquad \begin{array}{ccl} \dfrac{d \mathcal{L}}{dx} = 0 & \Rightarrow & x^T = b^TA(A^T A)^{-1} \end{array} $")
    
# =========================================================================================================================================== #
#                                                                   LOGICAL (solution)                                                        #
# =========================================================================================================================================== #
def solution_logical_1_easy():
    st.write("#### Answers")
    st.write("Giả sử ta có 2 sợi dây $a$ và $b$ như hình với 4 đầu dây $(a): A, A'$ và $(b): B, B'$")
    st.write("$\diamond$ Đầu tiên, ta đốt 3 đầu của 2 sợi dây, giả sử là $A, A'$ và $B$. khi đó, sau 30 phút thì")
    st.write(r"$\qquad \text{Dây} (a)$ sẽ cháy hết do ta đã đốt cả 2 đầu cùng lúc")
    st.write(r"$\qquad \text{Dây} (b)$ sẽ cháy đến 1 đoạn bất kỳ, lúc này nó chỉ còn 30 phút nữa là hết")
    st.write("$\diamond $ Lúc này, ta lại đốt đầu $B'$ còn lại, khi đó dây $(b)$ sẽ cháy hết trong 15 phút còn lại")
    st.write("Như vậy, tổng thời gian của ta là 45 phút")        

def solution_logical_2_easy():
    st.write("#### Answers")
    st.write("Như hình minh họa bên trái, ta đặt thành 5 lane chạy $A,B,C,D,E$ và mỗi lane có 5 con ngựa. Đầu tiên ta sẽ tổ chức cho cả 5 lane này cùng chạy và giả sử kết quả thu được như hình bên trái. Lúc này ta đã sử dụng 5 lượt")
    st.write("Tiếp theo, lấy 5 con ngựa đứng đầu ở 5 lượt đầu tiên và ta cho nó chạy ở lượt 6. Giả sử con nhanh nhất ở lượt này là $A1$ và các con theo sau như hình bên trái, khi đó nó cũng là con ngựa nhanh nhất chung cuộc. Để chọn ra 2 con ngựa nhanh thứ 2 và 3 chung cuộc, ta có các phân tích sau:")
    st.write("$\qquad \diamond$ Lane $D$ và $E$ góp mặt thứ 4 và 5 ở `turn 6` (với đại diện $D1, E1$) nên chúng không thể ở top3 chung cuộc,  nên ta sẽ loại cả 10 con ngựa ở 2 lane này")
    st.write("$\qquad \diamond$ Với 2 vị trí tiếp theo ở `turn 6` sau khi đã loại $A1$ và 10 con ngựa trong 2 lane $D, E$ thì ta sẽ có các khả năng")
    st.write(r"$\qquad \quad \bullet \; A2, A3$ sẽ là các con ngựa cần tìm do lượt đầu nó chỉ sau mỗi $A1$")
    st.write(r"$\qquad \quad \bullet \; B1, B2$ sẽ là các con ngựa cần tìm do `turn6` $B1$ chỉ sau mỗi $A1$")
    st.write(r"$\qquad \quad \bullet \; C1$ cũng có khả năng do `turn6` $C1$ xếp sau $A1$ và $B1$")
    st.write(r"$\qquad \quad \bullet$ những con còn lại không có khả năng")
    st.write("Do đó, `turn 7` sẽ là cuộc đua của 5 con ngựa $A2, A3, B1, B2, C1$ để tìm 2 con nhanh nhất còn lại")
            
def solution_logical_1_medium():
    st.write("#### Answers")
    st.write("From the second sentence, we obtain the car-speed")
    st.write(r"$\qquad \qquad s_t = \alpha t^{-1}, \qquad \forall t > 0$")
    st.write(r"where $\alpha > 0$ is a constant of proportionality and $t$ is the time elapsed since snow began. Hence, for any timestamp $t_1, t_2$, we have")
    st.write(r"$ \qquad \begin{array}{ccccl} d(t_1, t_2) &=& \text{distance} (t_1, t_2) &=& \displaystyle \int_{t_1}^{t_2} s_t dt \\ \\ & & & = & \alpha \ln \frac{t_2}{t_1} \qquad \forall t_2 \geq t_1 \end{array} $")
    st.write("By assumption the distance covered by the snow car from midday until 1pm is double from 1pm to 2pm, we obtain")
    st.write("$\qquad \qquad d(t_0, t_0 + 1) = 2 d(t_0 + 1, t_0 + 2)$")
    st.write("where $t_0 > 0$ is the amount of time it's been snowing for at midday. So,")
    st.write(r"$ \qquad \begin{array}{cccl} & \alpha \ln \frac{1 + t_0}{t_0} & = & 2 \alpha \ln \frac{t_0 + 2}{t_0 + 1} \\ \\ \Leftrightarrow & \frac{t_0 + 1}{t_0} &=& \left( \frac{t_0 + 2}{t_0 + 1} \right)^2 \end{array}$")
    st.write(r"Combining with $t_0 > 0$, we obtain:")
    st.write(r"$\qquad t_0 = \frac{-1 + \sqrt{5}}{2} \approx 0.618 \approx 37.08$ minutes")
    st.write("Therefore, it is about 37.08 minutes before midday, approximate 11 h 22 ")

def solution_logical_2_medium():
    st.write("#### Answers")
    st.write("Let")
    st.write("$\qquad V_t, x_t, t_0$ respectively be the Volume of snowfall, distance that the snowplow has gone after $t$ hours, the time before the snowfall began and,")
    st.write("$\qquad k$ is the constant rate of the snowfall")
    st.write("$\qquad r$ is the constant rate of the snowplow")
    st.write("We have")
    st.write(r"$\qquad \begin{array}{ccc} dV_t = k & V_t(t_0) = 0 & V_t dx_t = r \\ x_{t_0} = 0 & x_{t_0 + 1} = 2 & x_{t_0 + 2} = 3 \end{array}$")      
    st.write("So")
    st.write(r"$\qquad dx_t = \dfrac{r}{V_t} = \dfrac{r}{k(t - t_0)} \Rightarrow x_t = \dfrac{r}{k} \ln (t - t_0) + c$")
    st.write("where $c$ is any constant, We also have")
    st.write(r"$\qquad \begin{array}{cccc} & x_{t_0+1} - x_{t_0} &=& 2(x_{t_0 +2} - x_{t_0 + 1}) \\ \Leftrightarrow & \ln \left( \frac{1 + t_0}{t_0} \right) & = & 2 \ln \left( \frac{2 + t_0}{t_0 + 2} \right)^2 \end{array} $")
    st.write(r"Therefore $t_0  = \dfrac{-1+\sqrt{5}}{2} \approx 0.618 \approx 37.08$ minutes")
    st.write("Hence, the snowfall started at 7h23 in the morning!")
                                    
def solution_logical_1_hard():
    st.write("#### Answers")
    st.write("$\quad$ Ta thấy bài toán lớn là xác định 4 số hạng cuối trong biểu thức $2015^d$,")
    st.write(r"với $d = 2013^{2014}$")
    st.write("Lúc này, chú ý rằng quy luật của $2015^d$ trong hình minh họa bên trái,")
    st.write(r"$\forall d > 4$ và $d \, \not \vdots \, 2$, ta có")
    st.write(r"$\qquad \qquad F_4^d (2015^d) := \text{last-4-digits-of-}2015^d = 3375$")
    st.write("Với $d:= 2013^{2014} $ thì $d > 4$ và $d$ là số lẻ, do đó" )
    st.write(r"$\qquad \qquad F_4^d (2015^{2013^{2014}}) = 3375 $")

#================================================ Define illustration card-banking ================================================ #
def get_chart_avg(credits_card_data):
    ext_df = credits_card_data[['card_name', 'average-rate']]
    ext_df['average-rate'] = ext_df['average-rate'].astype(float)
    ext_df = ext_df.sort_values(by='average-rate', ascending=True)        
    fig = go.Figure(data=[go.Bar( y=ext_df['card_name'], x=ext_df['average-rate'], text=ext_df['average-rate'], textposition='auto', orientation='h')])
    fig.update_layout(
        title="Average Ratings of Credit Cards",
        yaxis_title="Card Name", xaxis_title="Average Rate",
        template="plotly_dark"
    )
    return fig    

def get_chart_cnt(credits_card_data):
    ext_df = credits_card_data[['card_name', 'n-users']]
    ext_df['n-users'] = ext_df['n-users'].apply(lambda x: str(x).replace('.', '')).astype(int)
    ext_df = ext_df.sort_values(by='n-users', ascending=True)        
    fig = go.Figure(data=[go.Bar( y=ext_df['card_name'], x=ext_df['n-users'], text=ext_df['n-users'], textposition='auto', orientation='h')])
    fig.update_layout(
        title="Number registrations of Credit Cards",
        yaxis_title="Card Name", xaxis_title="n-registrations",
        template="plotly_dark"
    )        
    return fig

#====================================================== Define quiz_num ===================================================== #
def get_quiz_num(math_topic, levels):
    if math_topic == "Hình học":
        if levels == "Dễ":
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 11)))
        elif levels == "Trung bình":
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 21)))
        else:
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 41)))
    elif math_topic == "Phương trình lượng giác":
        if levels == "Dễ":
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 11)))
        elif levels == "Trung bình":
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 21)))
        else:
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 41)))
    elif math_topic == "Tập hợp - chuỗi số - hàm số":
        if levels == "Dễ":
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 11)))
        elif levels == "Trung bình":
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 21)))
        else:
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 41)))
    elif math_topic == "Ma trận":
        if levels == "Dễ":
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 11)))
        elif levels == "Trung bình":
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 21)))
        else:
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 41)))
    elif math_topic == "Xác suất Thống kê":
        if levels == "Dễ":
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 11)))
        elif levels == "Trung bình":
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 21)))
        else:
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 41)))
    else:
        if levels == "Dễ":
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 11)))
        elif levels == "Trung bình":
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 21)))
        else:
            quiz_num = st.selectbox("chọn câu", (f"câu {idx}" for idx in range(1, 41)))      
            
    return quiz_num