import streamlit as st #all streamlit commands will be available through the "st" alias
import csv_lib as glib #reference to local lib script

st.set_page_config(page_title="Text to CSV", layout="wide")  #set the page width wider to accommodate columns
st.title("Text to CSV")  #page title


st.subheader("Content") #subhead for this column
input_text = st.text_area("Input text", height=200, label_visibility="collapsed")
process_button = st.button("Run", type="primary") #display a primary button

st.subheader("Result") #subhead for this column

if process_button: #code in this if block will be run when the button is clicked
    with st.spinner("Running..."): #show a spinner while the code in this with block runs
        response_data_frame, response_csv = glib.get_csv_response(input_content=input_text) #call the model through the supporting library
        st.table(response_data_frame)
        st.markdown("#### Raw CSV")
        st.text(response_csv)
        