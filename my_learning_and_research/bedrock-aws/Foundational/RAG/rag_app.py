
import streamlit as st #all streamlit commands will be available through the "st" alias
import rag_lib as glib #reference to local lib script

st.set_page_config(page_title="Retrieval-Augmented Generation") #HTML title
st.title("Retrieval-Augmented Generation") #page title
input_text = st.text_area("Input text", label_visibility="collapsed") #display a multiline text box with no label
go_button = st.button("Go", type="primary") #display a primary button

if go_button: #code in this if block will be run when the button is clicked
    
    with st.spinner("Working..."): #show a spinner while the code in this with block runs
        response_content, search_results = glib.get_rag_response(question=input_text) #call the model through the supporting library
        
        st.write(response_content) #display the response content
        
        with st.expander("See search results"):
            st.table(search_results)
