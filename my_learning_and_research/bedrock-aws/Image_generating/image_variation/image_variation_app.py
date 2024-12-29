import streamlit as st
import image_variation_lib as glib

st.set_page_config(layout="wide", page_title="Image Variation")
st.title("Image Variation")

col1, col2, col3 = st.columns(3)

with col1:
    
    uploaded_file = st.file_uploader("Select an image", type=['png', 'jpg'])
    if uploaded_file:
        uploaded_image_preview = glib.get_bytesio_from_bytes(uploaded_file.getvalue())
        st.image(uploaded_image_preview)
    else:
        st.image("images/example.jpg")

with col2:
    prompt_text = st.text_input("How to vary the image:", value="A car on a brick road.", 
                                help="The prompt text")
    similarity_strength = st.slider("Similarity strength", 
                                    min_value=0.2, max_value=1.0, value=0.9, step=0.1, 
                                    help="How similar the generated image should be to the original image", format='%.1f')
    generate_button = st.button("Generate", type="primary")
    
with col3:

    if generate_button:
        
        if uploaded_file:
            image_bytes = uploaded_file.getvalue()
        else:
            image_bytes = glib.get_bytes_from_file("images/example.jpg")
        
        with st.spinner("Drawing..."):
            generated_image = glib.get_image_from_model(
                prompt_content=prompt_text,
                similarity_strength=similarity_strength,
                image_bytes=image_bytes,
            )
        
        st.image(generated_image)
