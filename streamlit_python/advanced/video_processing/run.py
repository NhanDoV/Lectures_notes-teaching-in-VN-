import streamlit as st

st.set_page_config(
    page_title = "Video Processing",
    layout = "wide",
    initial_sidebar_state = "expanded",
)

# Load CSS
with open('helper/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)