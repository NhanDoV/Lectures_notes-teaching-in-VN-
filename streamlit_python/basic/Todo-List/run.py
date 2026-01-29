import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="To-do list",
    page_icon="📝",
    layout="centered"
)

# =========================
# BACKGROUND STYLE (OK, CSS NÀY VẪN ĂN)
# =========================
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 20% 80%, rgba(120,119,198,0.3), transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255,119,198,0.3), transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(120,219,255,0.3), transparent 50%),
                linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    background-size: 100% 100%;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.title("📝 To-do list")

# =========================
# SESSION STATE
# =========================
# Initialize session state - THÊM TASK MẶC ĐỊNH
if "todos" not in st.session_state:
    st.session_state.todos = [
        {"task": "Địzt đàn bà thằng TôLâm", "done": True},
        {"task": "Bán TôLâm cho Trump địt", "done": False},
        {"task": "Địzt mẹ Tập Cận Bình", "done": True},
        {"task": "Cho TôLâm ăn cứt", "done": True},
        {"task": "Địt vợ tụi CSGT", "done": True},
        {"task": "Bán clip địt vợ bọn CSGT", "done": False}
    ]

# Add new task
col1, col2 = st.columns([7, 1])
with col1:
    new_task = st.text_input(label = " ", 
                             placeholder = "Add to-do item", 
                             label_visibility = "collapsed")
with col2:
    if st.button("➕ Add"):
        if new_task.strip():
            st.session_state.todos.append(
                {
                    "task": new_task.strip(), 
                    "done": False
                }
            )

st.divider()

# Display tasks
for i, todo in enumerate(st.session_state.todos):
    col1, col2 = st.columns([10, 1])
    with col1:
        todo["done"] = st.checkbox(
            todo["task"], value=todo["done"], key=f"todo_{i}"
        )
    with col2:
        if st.button("🗑️", key=f"delete_{i}"):
            st.session_state.todos.pop(i)
            st.rerun()

st.divider()
_, c, _ = st.columns([1,1,1])
with c:
    if st.button("🧹 Delete all checked"):
        st.session_state.todos = [
            t for t in st.session_state.todos if not t["done"]
        ]
        st.rerun()