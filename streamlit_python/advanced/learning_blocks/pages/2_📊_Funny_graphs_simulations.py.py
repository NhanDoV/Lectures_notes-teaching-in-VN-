import streamlit as st
from helper_simulation import *

st.title("📊 Funny Graphs Simulations")
# Load CSS (nếu cần)
with open('./style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

params, results = st.columns([3, 2])

with params:
    path_sims = st.selectbox("Chọn kiểu hình học",
                             [
                                 "Tròn / Ellipse",
                                 "Đoạn thẳng",
                                 "Trái tim",
                                 "Vòng xoắn ốc",
                                 "Ngôi sao",
                                 "Cánh hoa",
                             ])

    # Tùy chỉnh params theo từng loại
    if path_sims == "Tròn / Ellipse":
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            x0 = st.number_input("x0 (tâm)", value=0.0, step=0.1)
        with c2:
            y0 = st.number_input("y0 (tâm)", value=0.0, step=0.1)
        with c3:
            R = st.number_input("R (bán kính ngang)", value=2.0, min_value=0.1, step=0.1)
        with c4:
            r = st.number_input("r (bán kính dọc)", value=1.0, min_value=0.1, step=0.1)
        x_full, y_full = generate_xy_circle(x0, y0, r, R)

    elif path_sims == "Đoạn thẳng":
        c1, c2 = st.columns(2)
        with c1:
            a = st.number_input("a (độ dốc)", value=1.0, step=0.1)
        with c2:
            b = st.number_input("b (chặn y)", value=1.0, step=0.1)
        x_full, y_full = generate_xy_linear_segment(a, b)

    elif path_sims == "Trái tim":
        st.info("Công thức trái tim cổ điển (parametric) – không cần chỉnh nhiều")
        scale = st.slider("Kích thước tổng thể", 1.0, 10.0, 5.0, step=0.5, help="Scale lên/xuống toàn bộ hình")
        # Vì hàm generate_xy_heart đã scale x5 rồi, ta scale thêm nếu cần
        x_full, y_full = generate_xy_heart()
        x_full *= (scale / 5)
        y_full *= (scale / 5)

    elif path_sims == "Vòng xoắn ốc":
        c1, c2 = st.columns(2)
        with c1:
            a = st.slider("a (scale ban đầu)", 0.01, 1.0, 0.1, step=0.01, help="Giá trị nhỏ để xoắn từ tâm")
        with c2:
            n_round = st.slider("Số vòng quay", 3, 15, 8, step=1)
        x_full, y_full = generate_xy_spiral(a=a, n_round=n_round)

    elif path_sims == "Ngôi sao":
        c1, c2, c3 = st.columns(3)
        with c1:
            n_wings = st.slider("Số cánh", 4, 12, 5, step=1)
        with c2:
            out_radius = st.number_input("Bán kính ngoài", value=2.1, min_value=0.5, step=0.1)
        with c3:
            inner_scale = st.slider("Tỷ lệ trong/ngoài", 0.2, 0.8, 0.4, step=0.05, help="Nhỏ hơn → cánh nhọn hơn")
        x_full, y_full = generate_xy_stars(inner_scale=inner_scale, out_radius=out_radius, n_wings=n_wings)

    elif path_sims == "Cánh hoa":
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            N = st.slider("Số cánh hoa", 4, 30, 12, step=1)
        with c2:
            r_x = st.number_input("r_x (chiều ngang cánh)", value=0.6, min_value=0.1, step=0.05)
        with c3:
            r_y = st.number_input("r_y (chiều dọc cánh)", value=0.8, min_value=0.1, step=0.05)
        with c4:
            core_tp = st.selectbox("Loại lõi", ["cosine", "sine"])
        x_full, y_full = generate_xy_flowers(r_x=r_x, r_y=r_y, N=N, core_tp=core_tp)

with results:
    if 'x_full' in locals() and 'y_full' in locals():
        # Tùy chỉnh màu sắc theo kiểu hình (tùy chọn, cho vui)
        color_map = {
            "Tròn / Ellipse": ("cyan", "purple"),
            "Đoạn thẳng": ("red", "blue"),
            "Trái tim": ("pink", "red"),
            "Vòng xoắn ốc": ("orange", "gold"),
            "Ngôi sao": ("yellow", "gold"),
            "Cánh hoa": ("violet", "magenta")
        }
        marker_c, line_c = color_map.get(path_sims, ("red", "blue"))

        fig = create_animated_figure(
            x_full, y_full,
            title=f"Animation: {path_sims}",
            marker_color=marker_c,
            line_color=line_c,
            duration=60,  # có thể để slider nếu muốn
            width=700,
            height=700    # vuông để đẹp hơn với hầu hết hình
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Chọn kiểu hình để bắt đầu animation!")