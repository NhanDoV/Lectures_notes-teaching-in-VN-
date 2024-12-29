import streamlit as st
import image_background_lib as glib

st.set_page_config(layout="wide", page_title="Image Background")
st.title("Image Background")
col1, col2, col3 = st.columns(3)

with col1:
    uploaded_file = st.file_uploader("Select an image", type=['png', 'jpg'])
    
    if uploaded_file:
        uploaded_image_preview = glib.get_bytesio_from_bytes(uploaded_file.getvalue())
        st.image(uploaded_image_preview)
    else:
        st.image("images/example.jpg")

with col2:
    st.subheader("Image parameters")
    mask_prompt = st.text_input("Object to keep:", value="A car", help="The mask text")
    prompt_text = st.text_area("Description including the object to keep and background to add:", value="Car at the beach", height=100, help="The prompt text")
    negative_prompt = st.text_input("What should not be in the background:", help="The negative prompt")
    outpainting_mode = st.radio("Outpainting mode:", ["DEFAULT", "PRECISE"], horizontal=True)
    generate_button = st.button("Generate", type="primary")

with col3:
    st.subheader("Result")
    if generate_button:
        if uploaded_file:
            image_bytes = uploaded_file.getvalue()
        else:
            image_bytes = glib.get_bytes_from_file("images/example.jpg")
        
        with st.spinner("Drawing..."):
            generated_image = glib.get_image_from_model(
                prompt_content=prompt_text, 
                image_bytes=image_bytes,
                mask_prompt=mask_prompt,
                negative_prompt=negative_prompt,
                outpainting_mode=outpainting_mode,
            )
        
        st.image(generated_image)
