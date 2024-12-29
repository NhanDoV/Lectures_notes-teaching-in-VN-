import streamlit as st #all streamlit commands will be available through the "st" alias
import text_lib as glib #reference to local lib script

st.set_page_config(page_title="Text to Text") #HTML title
st.title("Text to Text") #page title

input_text = st.text_area("Input text", label_visibility="collapsed") #display a multiline text box with no label
go_button = st.button("Go", type="primary") #display a primary button


if go_button: #code in this if block will be run when the button is clicked    
    with st.spinner("Working..."): #show a spinner while the code in this with block runs
        response_content = glib.get_text_response(input_content=input_text) #call the model through the supporting library        
        st.write(response_content) #display the response content        