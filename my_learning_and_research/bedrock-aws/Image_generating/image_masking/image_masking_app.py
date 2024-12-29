import streamlit as st
import image_masking_lib as glib


st.set_page_config(layout="wide", page_title="Image Masking")
st.title("Image Masking")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Image")
    uploaded_image_file = st.file_uploader("Select an image", type=['png', 'jpg'])
    if uploaded_image_file:
        uploaded_image_preview = glib.get_bytesio_from_bytes(uploaded_image_file.getvalue())
        st.image(uploaded_image_preview)
    else:
        st.image("images/desk1.jpg")
    
    
with col2:
    st.subheader("Mask")
    masking_mode = st.radio("Masking mode:", ["Image", "Prompt"], horizontal=True)
    if masking_mode == 'Image':
        uploaded_mask_file = st.file_uploader("Select an image mask", type=['png', 'jpg'])
        if uploaded_mask_file:
            uploaded_mask_preview = glib.get_bytesio_from_bytes(uploaded_mask_file.getvalue())
            st.image(uploaded_mask_preview)
        else:
            st.image("images/mask1.png")
    else:
        mask_prompt = st.text_input("Item to mask:", help="The item to replace (if inpainting), or keep (if outpainting).")
    
        
with col3:
    st.subheader("Result")
    prompt_text = st.text_area("Prompt text:", height=100, help="The prompt text")
    painting_mode = st.radio("Painting mode:", ["INPAINTING", "OUTPAINTING"])
    generate_button = st.button("Generate", type="primary")
    if generate_button:
        with st.spinner("Drawing..."):
            
            if uploaded_image_file:
                image_bytes = uploaded_image_file.getvalue()
            else:
                image_bytes = glib.get_bytes_from_file("images/desk1.jpg")
            
            if masking_mode == 'Image':
                if uploaded_mask_file:
                    mask_bytes = uploaded_mask_file.getvalue()
                else:
                    mask_bytes = glib.get_bytes_from_file("images/mask1.png")
                
                generated_image = glib.get_image_from_model(
                    prompt_content=prompt_text, 
                    image_bytes=image_bytes,
                    masking_mode=masking_mode,
                    mask_bytes=mask_bytes,
                    painting_mode=painting_mode
                )
            else:
                generated_image = glib.get_image_from_model(
                    prompt_content=prompt_text, 
                    image_bytes=image_bytes,
                    masking_mode=masking_mode,
                    mask_prompt=mask_prompt,
                    painting_mode=painting_mode
                )
            
        
        st.image(generated_image)