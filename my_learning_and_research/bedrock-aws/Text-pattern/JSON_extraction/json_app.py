import streamlit as st #all streamlit commands will be available through the "st" alias
import json_lib as glib #reference to local lib script

st.set_page_config(page_title="Text to JSON", layout="wide")  #set the page width wider to accommodate columns
st.title("Text to JSON")  #page title

col1, col2 = st.columns(2)  #create 2 columns
with col1: #everything in this with block will be placed in column 1
    st.subheader("Content") #subhead for this column
    
    input_text = st.text_area("Input text", height=500, label_visibility="collapsed")

    process_button = st.button("Run", type="primary") #display a primary button

with col2: #everything in this with block will be placed in column 2
    st.subheader("Result") #subhead for this column
    
    if process_button: #code in this if block will be run when the button is clicked
        with st.spinner("Running..."): #show a spinner while the code in this with block runs
            response_content = glib.get_json_response(input_content=input_text) #call the model through the supporting library
            
            st.json(response_content) #render JSON if there was no error
