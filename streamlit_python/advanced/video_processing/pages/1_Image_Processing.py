import streamlit as st
from helper.image_processing import *

# List of options
IMG_OPTIONS = {
    "Color-space": [
        "Replace color of channel",
        "Replace color of detected-range"
    ],
    "Transformation": [
        "Translation",
        "Rotation",
        "Complement image",
        "Sine/Cosine curve",
        "Blurring",
        "Denoising"
    ],
    "Funny Application": [
        "KMeans cartoonize",
        "Sketch - edge detection",
        "Eigen factor cartoonize",
    ]
}

st.title("🏠 Labotary of Image Processing")
# Load CSS
with open('./helper/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

params, _, results = st.columns([1, 0.1, 5])
with params:
    # --- Row 1: Dimension ---
    method = st.selectbox("Chọn phương thức", IMG_OPTIONS.keys())

    # --- Row 2: Category ---
    categories = list(IMG_OPTIONS[method])
    category = st.selectbox("Chọn nhóm", categories)

    # --- Row 3: Params & Results:
    if method == "Color-space":
        if category == "Replace color of channel":
            CHANNEL_MAP = {"Blue": 0, "Green": 1, "Red": 2}
            channel_name = st.selectbox("Channel", CHANNEL_MAP.keys())
            channel_id = CHANNEL_MAP[channel_name]
            pixel_val = st.number_input("Input pixel value", 
                                        min_value = 0, max_value = 255, value = 128)
            with results:
                c1, _, c2 = st.columns([5, 0.1, 5])
                with c1:
                    st.subheader("Input")
                    img_file = st.file_uploader("Upload your image", type = ["jpg", "png"], key = "replace_channel")
                    if img_file:
                        st.image(img_file, caption="Original")

                with c2:
                    st.subheader("Output")
                    if img_file:
                        st.markdown("#### Logs")
                        st.json({
                            "channel selected": channel_name,
                            "pixel fill in": pixel_val
                        })

                        st.markdown("#### Result")
                        res_rgb = changing_channel_color_space(img_file, channel_id, pixel_val)
                        st.image(res_rgb, caption="Processed")

        else:
            st.subheader("HSV color filtering")

            h_range = st.slider("Hue range", 0, 179, (35, 85))
            s_range = st.slider("Saturation range", 0, 255, (50, 255))
            v_range = st.slider("Value range", 0, 255, (50, 255))

            clr_range = {
                "lower": (h_range[0], s_range[0], v_range[0]),
                "upper": (h_range[1], s_range[1], v_range[1])
            }

            # pixel val to replace the HSV-range
            pixel_val = st.number_input("Input pixel value", 
                                        min_value = 0, max_value = 255, value = 128)

            with results:
                c1, _, c2 = st.columns([5, 0.1, 5])
                with c1:
                    st.subheader("Input")
                    img_file = st.file_uploader("Upload your image", type = ["jpg", "png"], 
                                                key = "hsv_filter")
                    if img_file:
                        st.image(img_file, caption="Original")

                    with c2:
                        st.subheader("Output")
                        if img_file:
                            # Row 1. Display a horizontal-bar of hsv range (instead of the json)
                            st.write("##### Color range selected")
                            hsv_bar = hsv_range_bar(h_range)
                            st.image(hsv_bar, width = 'stretch')

                            # Row 2. display the output which filled
                            st.markdown("##### Result")
                            res_rgb, mask = hsv_mask_and_fill(img_file, clr_range["lower"], clr_range["upper"], pixel_val)
                            st.image(res_rgb, caption="Processed")

    elif method == "Transformation":
        if category == "Translation":
            with results:
                c1, _, c2 = st.columns([5, 0.1, 5])
                with c1:
                    st.subheader("Input")
                    img_file = st.file_uploader("Upload your image", type = ["jpg", "png"], 
                                                key = "translation")
                    if img_file:
                        st.image(img_file, caption="Original")

                    with c2:
                        st.subheader("Output")
                        if img_file:
                            img_bgr = load_image_from_upload(img_file)
                            h, w = get_img_dimension_from_bgr(img_bgr)
                            st.write(f"**Image dimension:** `height`: {h}, `width`: {w}")
                            c21, c22 = st.columns(2)
                            with c21:
                                tx = st.number_input("tx", min_value = -w, max_value = w, value = w // 3,
                                                     help = "moved left (if tx < 0) or right")
                            with c22:
                                ty = st.number_input("ty", min_value = -h, max_value = h, value = h // 4)
                            st.write("#### Result")
                            res = get_translation_img_from_bgr(img_bgr, tx, ty)
                            st.image(res, caption = "Translated")

        elif category == "Rotation":
            with params:
                angle = st.number_input("rotation angle",
                                        min_value = -180, max_value = 180, value = 45)
            with results:
                c1, _, c2 = st.columns([5, 0.1, 5])
                with c1:
                    st.subheader("Input")
                    img_file = st.file_uploader("Upload your image", type = ["jpg", "png"], 
                                                key = "rotation")
                    if img_file:
                        st.image(img_file, caption = "Original")
                        img_bgr = load_image_from_upload(img_file)
                        h, w = get_img_dimension_from_bgr(img_bgr)
                        with c2:
                            st.subheader("Output")
                            
                            c21, c22 = st.columns(2)
                            with c21:
                                cx = st.number_input("cx", min_value = 0, max_value = w, value = w // 2, help = "x-center")
                            with c22:
                                cy = st.number_input("cy", min_value = 0, max_value = h, value = h // 2, help = "y-center")

                            if img_file:
                                st.write("#### Result")
                                res = get_rotation_img(img_bgr, cx, cy, angle)
                                st.image(res, caption = "Rotated")

        elif category == "Complement image":
            with results:
                c1, _, c2 = st.columns([5, 0.1, 5])
                with c1:
                    st.subheader("Input")
                    img_file = st.file_uploader("Upload your image", type = ["jpg", "png"], 
                                                key = "translation")
                    if img_file:
                        st.image(img_file, caption = "Original")

                        with c2:
                            st.subheader("Output")
                            st.write("##### Demo")
                            # Pick pixel
                            with params:
                                st.write("--------------")
                                st.markdown("##### Pick a pixel to see demo")
                                img_bgr = load_image_from_upload(img_file)
                                h, w, _ = img_bgr.shape
                                x = st.number_input("x", 0, w - 1, w // 2)
                                y = st.number_input("y", 0, h - 1, h // 2)

                            # Original pixel
                            rgb = get_pixel_rgb(img_bgr, x, y)
                            comp_rgb = complement_rgb(rgb)

                            c21, c22 = st.columns(2)
                            with c21:
                                st.caption(f"Original pixel RGB: {rgb.astype(int).tolist()}")
                                st.image(color_bar(rgb))

                            with c22:
                                st.caption(f"Complementary pixel RGB: {comp_rgb.astype(int).tolist()}")
                                st.image(color_bar(comp_rgb))

                            st.write("##### Result")
                            res = get_complement_pixel(img_bgr)
                            st.image(res, caption = "Complementary pixel")

        elif category == "Sine/Cosine curve":
            trans_method = st.selectbox("Transformation type",
                                            [
                                                "sine_transform",
                                                "cosine_transform",
                                                "tan_transform",
                                                "tanh_transform",
                                                "sinh_transform",
                                                "cosh_transform"
                                            ])
            with results:
                c1, _, c2 = st.columns([5, 0.1, 5])
                with c1:
                    st.subheader("Input")
                    img_file = st.file_uploader("Upload your image", type = ["jpg", "png"], 
                                                key = "affine-transformation")
                    if img_file:
                        st.image(img_file, caption = "Original")

                        with c2:
                            st.subheader("Output")
                            if img_file:
                                img_bgr = load_image_from_upload(img_file)

                                st.markdown("##### Transform info")
                                st.json({
                                    "method": trans_method,
                                    "grid": '20 x 10',
                                })

                                res = sine_piecewise_transform(
                                    img_bgr,
                                    transform_type = trans_method
                                )

                                st.markdown("##### Result")
                                st.image(res, caption="Piecewise Affine Transform")

        elif category == "Blurring":
            with params:
                blur_method = st.selectbox("bluring method", ["Gaussian", "Median", "Bilateral"])
                ksize = st.slider("Kernel size", 3, 31, 7, step=2)
                sigma = st.slider("Sigma", 0.0, 10.0, 0.0)

            with results:
                c1, _, c2 = st.columns([5, 0.1, 5])

                with c1:
                    st.subheader("Input")
                    img_file = st.file_uploader("Upload your image", type=["jpg", "png"], key="blur")

                    if img_file:
                        st.image(img_file, caption="Original")

                with c2:
                    st.subheader("Output")

                    if img_file:
                        img_bgr = load_image_from_upload(img_file)

                        st.markdown("**Logs**")
                        st.json({
                                "method": blur_method,
                                "kernel_size": ksize,
                                "sigma": sigma
                            })

                        res_bgr = apply_blur(img_bgr, blur_method, ksize, sigma)
                        st.write("**Results**")
                        res_rgb = bgr_to_rgb(res_bgr)
                        st.image(res_rgb, caption = f"{blur_method} Blur")

        else: # "Denoising"
            with params:
                add_or_remove = st.selectbox("You wanna", ["Denoising", "Adding noise"])
                noise_sigma = st.slider("White noise sigma", 0.0, 20.0, 5.0)
                blur_sigma = st.slider("Blur sigma (PSF)", 0.5, 5.0, 2.0)
                ksize = st.slider("Kernel size", 3, 31, 15, step=2)

            with results:
                c1, _, c2 = st.columns([5, 0.1, 5])

                with c1:
                    st.subheader("Input")
                    img_file = st.file_uploader("Upload your image", type=["jpg", "png"])

                    if img_file:
                        st.image(img_file, caption="Original")

                with c2:
                    st.subheader("Output")

                    if img_file:
                        # ---- Load & preprocess
                        img_bgr = load_image_from_upload(img_file)
                        img_rgb = bgr_to_rgb(img_bgr)
                        img_gray = rgb_to_gray(img_rgb) / 255.0

                        # ---- Blur
                        psf = gaussian_psf(ksize, blur_sigma)
                        blurred = cv2.filter2D(img_gray, -1, psf)

                        # ---- Add noise
                        noisy = add_white_gaussian_noise(blurred, noise_sigma)

                        if add_or_remove == "Adding noise":
                            st.markdown("##### Noisy image")
                            st.image(noisy, clamp=True)

                        else:  # Denoising (Wiener)
                            restored = wiener_deconvolution(
                                noisy,
                                psf,
                                noise_sigma
                            )

                            c21, c22 = st.columns(2)

                            with c21:
                                st.caption("Noisy")
                                st.image(noisy, clamp=True)

                            with c22:
                                st.caption("After Wiener Deconvolution")
                                st.image(restored, clamp=True)

                        st.markdown("##### Logs")
                        st.json({
                            "mode": add_or_remove,
                            "noise_sigma": noise_sigma,
                            "blur_sigma": blur_sigma,
                            "kernel_size": ksize
                        })

    else:   # Application
        if category == "KMeans cartoonize":
            with results:
                c1, _, c2 = st.columns([5, 0.2, 5])
                with c1:
                    st.subheader("Input")
                    img_file = st.file_uploader("Upload your image", type=["jpg", "png"], key="segmentation")

                    if img_file:
                        img_bgr = load_image_from_upload(img_file)
                        st.image( img_bgr[:, :, ::-1], caption="Original (RGB)")

                with c2:
                    st.write("#### Output")
                    with params:
                        st.write("**Parameters**")
                        color_space = st.selectbox("Color space for clustering", ["RGB", "HSV", "LAB"])                    
                        nb_clusters = st.slider("Number of clusters (K)", 
                                                min_value=2, max_value=12, value=4)
                        normalize = st.checkbox("Normalize pixel values", value=True)

                    if img_file:
                        with st.spinner("Running KMeans segmentation..."):
                            seg_img, label_map = get_kmeans_segments(
                                img_bgr,
                                nb_clusters=nb_clusters,
                                color_space=color_space,
                                normalize=normalize
                            )

                        with st.expander("Debug / Info"):
                            st.write("Label map shape:", label_map.shape)
                            st.write("Unique clusters:", list(set(label_map.flatten())))

                        st.write("#### Result")
                        st.image( seg_img, caption=f"KMeans Segmentation (K={nb_clusters}, {color_space})")

        elif category == "Sketch - edge detection":
            edge_method = st.selectbox(
                "Edge detection method",
                ["Sobel", "Laplacian", "Canny"]
            )

            with results:
                c1, _, c2 = st.columns([5, 0.2, 5])

                # ---------- INPUT ----------
                with c1:
                    st.subheader("Input")
                    img_file = st.file_uploader(
                        "Upload your image",
                        type=["jpg", "png"],
                        key="edge"
                    )

                    if img_file:
                        gray = load_gray_from_upload(img_file)
                        st.image(gray, caption="Grayscale input")

                # ---------- OUTPUT ----------
                with c2:
                    st.subheader("Output")

                    if img_file:

                        if edge_method in ["Sobel", "Laplacian"]:
                            ksize = st.slider(
                                "Kernel size",
                                min_value=3,
                                max_value=7,
                                step=2,
                                value=3
                            )

                        if edge_method == "Canny":
                            t1, t2 = st.slider(
                                "Thresholds",
                                0, 255, (50, 150)
                            )

                        if edge_method == "Sobel":
                            edge = sobel_edge(gray, ksize)

                        elif edge_method == "Laplacian":
                            edge = laplacian_edge(gray, ksize)

                        else:
                            edge = canny_edge(gray, t1, t2)

                        st.image(edge, caption=f"{edge_method} edge map")

        else :          # "Eigen factor cartoonize",
            with params:
                st.write("#### Parameters")
                t1, t2 = st.slider("Canny thresholds", 0, 255, (50, 150))
                bilateral_d = st.slider("Bilateral d", 5, 15, 9, step=2)
                sigma_color = st.slider("Sigma Color", 10, 150, 75)
                sigma_space = st.slider("Sigma Space", 10, 150, 75)

            with results:
                c1, _, c2 = st.columns([5, 0.2, 5])

                with c1:
                    st.subheader("Input")
                    img_file = st.file_uploader(
                        "Upload your image",
                        type=["jpg", "png"],
                        key="cartoon"
                    )

                    if img_file:
                        img_bgr = load_image_from_upload(img_file)
                        st.image(img_bgr[:, :, ::-1], caption="Original")

                with c2:
                    st.subheader("Output")
                    if img_file:
                        res = eigen_cartoonize(
                            img_bgr,
                            bilateral_d,
                            sigma_color,
                            sigma_space,
                            t1, t2
                        )
                        st.image(res, caption="Eigen-factor Cartoonize")