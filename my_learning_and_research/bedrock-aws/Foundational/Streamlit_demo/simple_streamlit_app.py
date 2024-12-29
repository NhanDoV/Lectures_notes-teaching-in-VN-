import streamlit as st #all streamlit commands will be available through the "st" alias

st.set_page_config(page_title="Streamlit Demo") #HTML title
st.title("Streamlit Demo") #page title

color_text = st.text_input("What's your favorite color?") #display a text box
go_button = st.button("Go", type="primary") #display a primary button

if go_button: #code in this if block will be run when the button is clicked

    st.write(f"I like {color_text} too!") #display the response content
