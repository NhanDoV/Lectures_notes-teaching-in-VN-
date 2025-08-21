import streamlit as st

# ======= Title of the page =======
st.set_page_config(layout="wide")
# st.title("🧮 DVN_App Searching Math")
st.markdown("""
    <p style='
        color: red;
        font-size: 36px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 25px;
    '>🧮 DVN_App Searching Math</p>
""", unsafe_allow_html=True)

home, math = st.tabs(("**HOME**", "**MFF[Math-Fact-Fun]**"))

with home:
    st.markdown("""
        <p style='
            color: green;
            font-size: 26px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
        '>Homepage</p>
    """, unsafe_allow_html=True)
    _, c, _ = st.columns([3,19,4])
    with c:
        st.image("images/home_cover.png", use_container_width =True)
    st.markdown("""
        <p style='
            color: blue;
            font-size: 16px;
            margin-top: 12px;
            margin-bottom: 10px;
        '> ⬇️ Below is list of all questions 📥 (scroll down to see more question or you can type `Ctrl + F` to find text 🔍) </p>
    """, unsafe_allow_html=True)
    # st.write("Cell `A54` (id = 53) vs `A79` (id = 78) has been used, replace another question later")
    from libs.home import *
    make_table()

with math:
    from libs.mff import *
    st.markdown("""
        <p style='
            color: green;
            font-size: 26px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
        '>Fact & Fun</p>
    """, unsafe_allow_html=True)    
    c1, c2 = st.columns([3, 2])
    with c1:
        # Select main topic
        with c1: main_topic = st.selectbox("Choose main topic", list(topic_dict.keys()))
        # Select sub-topic (category)
        with c2: category = st.selectbox("Select category", topic_dict[main_topic])
    show_hand(category) 