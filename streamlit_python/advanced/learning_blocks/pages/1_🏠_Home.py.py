import streamlit as st
from helper_2D_plot import plot_2d
from helper_3D_plot import plot_3d

# List of shapes
SHAPES = {
    "2D": {
        "Tam giác": [\
            "Tam giác thường",
            "Tam giác vuông",
            "Tam giác cân",
            "Tam giác đều",
            "Tam giác vuông cân",
        ],
        "Tứ giác": [
            "Hình vuông",
            "Hình chữ nhật",
            "Hình bình hành",
            "Hình thang",
            "Hình thang vuông",
            "Hình thoi",
            "Hình thang cân",
        ],
        "Đa giác": [
            "Đa giác đều",
            "Đa giác lồi",
        ],
        "Hình tròn": [
            "Hình tròn (tiêu chuẩn)",
            "Bán nguyệt",
            "Hình vành khăn",
        ],
    },
    "3D": {
        "Khối chóp": [
            "Tứ diện",
            "Chóp tam giác",
            "Chóp tứ giác",
        ],
        "Khối trụ": [
            "Hình trụ đáy tròn",
            "Hình lăng trụ tam giác",
        ],
        "Khối hộp": [
            "Hình hộp chữ nhật",
            "Hình lập phương",
        ],
        "Khối nón": [
            "Hình nón cụt (đứng)",
            "Hình nón đứng",
            "Hình nón úp",
        ],
        "Khối cầu": [
            "Hình cầu tiêu chuẩn",
            "Bán cầu"
        ]
    }
}

st.title("🏠 Home - Mô phỏng hình khối vui nhộn")
# Load CSS
with open('./style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

params, results = st.columns([5, 2])
with params:
    # --- Row 1: Dimension ---        
    dimension = st.selectbox(
        "Chọn hình / khối",
        ["2D", "3D"],
        format_func=lambda x: "Hình (2D)" if x == "2D" else "Khối (3D)"
    )

    # --- Row 2: Category ---
    categories = list(SHAPES[dimension].keys())
    category = st.selectbox(
        "Chọn nhóm",
        categories
    )

    # --- Row 3: Specific shape ---
    shapes = SHAPES[dimension][category]
    sel_block = st.selectbox(
        "Chọn hình cụ thể",
        shapes
    )

    # ======================== processing logic ==============================#
    if dimension == "2D":
        fig = plot_2d(category = category, shape = sel_block)
    else:
        fig = plot_3d(category = category, shape = sel_block)

# =========================== outut =======================================
with results:
    st.pyplot(fig)
    st.success(f"Bạn đã chọn: {dimension} → {category} → {sel_block}")