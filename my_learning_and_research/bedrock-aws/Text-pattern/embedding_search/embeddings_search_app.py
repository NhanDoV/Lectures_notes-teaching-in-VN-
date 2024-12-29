import streamlit as st #all streamlit commands will be available through the "st" alias
import embeddings_search_lib as glib #reference to local lib script

st.set_page_config(page_title="Embeddings Search", layout="wide") #HTML title
st.title("Embeddings Search") #page title

input_text = st.text_input("Question about Amazon Bedrock:")
go_button = st.button("Go", type="primary") #display a primary button

if go_button: #code in this if block will be run when the button is clicked
    
    with st.spinner("Working..."): #show a spinner while the code in this with block runs
        response_content = glib.get_similarity_search_results(question=input_text)
        
        st.table(response_content) #using table so text will wrap
        
