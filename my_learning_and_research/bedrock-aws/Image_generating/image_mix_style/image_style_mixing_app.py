import streamlit as st
import image_style_mixing_lib as glib

st.set_page_config(layout="wide", page_title="Image Style Mixing")
st.title("Image Style Mixing")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Image One")    
    uploaded_file1 = st.file_uploader("Select image 1", type=['png', 'jpg'])
    
    if uploaded_file1:
        uploaded_image_preview = glib.get_bytesio_from_bytes(uploaded_file1.getvalue())
        st.image(uploaded_image_preview)
    else:
        st.image("images/art_example.png")

with col2:
    st.subheader("Image Two")
    
    uploaded_file2 = st.file_uploader("Select image 2", type=['png', 'jpg'])
    
    if uploaded_file2:
        uploaded_image_preview = glib.get_bytesio_from_bytes(uploaded_file2.getvalue())
        st.image(uploaded_image_preview)
    else:
        st.image("images/cat_example.png")

with col3:  
    st.subheader("Options")

    prompt_text = st.text_input("Brief description of the target image:", 
                                value="a cat using art style", help="The prompt text")
    similarity_strength = st.slider("Similarity strength", min_value=0.2, max_value=1.0, value=0.9, step=0.1, 
                                    help="How similar the generated image should be to the original image", format='%.1f')
    generate_button = st.button("Generate", type="primary")    

with col4:
    st.subheader("Result")

    if generate_button:

        if uploaded_file1:
            image_bytes1 = uploaded_file1.getvalue()
        else:
            image_bytes1 = glib.get_bytes_from_file("images/art_example.png")
            
        if uploaded_file2:
            image_bytes2 = uploaded_file2.getvalue()
        else:
            image_bytes2 = glib.get_bytes_from_file("images/cat_example.png")
                
        with st.spinner("Drawing..."):
            generated_image = glib.get_image_from_model(
                prompt_content=prompt_text,
                similarity_strength=float(similarity_strength),
                image_bytes1=image_bytes1,
                image_bytes2=image_bytes2,
            )
        
        st.image(generated_image)