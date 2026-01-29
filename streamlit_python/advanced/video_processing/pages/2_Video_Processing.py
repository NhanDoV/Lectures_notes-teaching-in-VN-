import streamlit as st
import tempfile
from helper.video_processing import *

st.subheader("Video Processing")

video_file = st.file_uploader(
    "Upload video",
    type=["mp4", "avi", "mov"]
)

if video_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(video_file.read())
        video_path = tmp.name

    cap, fps, w, h, total = read_video(video_path)
    info = video_info(fps, total)
    st.json(info)

    operation = st.selectbox(
        "Operation",
        ["Invert video (reverse timeline)", "Grayscale video"]
    )

    out_path = video_path + "_out.mp4"
    writer = write_video(out_path, fps, w, h)

    if st.button("Run"):
        if operation == "Invert video (reverse timeline)":
            invert_video_frames(cap, writer)

        else:
            apply_frame_transform(cap, writer, to_grayscale)

        cap.release()
        writer.release()

        st.success("Done processing!")

        st.video(out_path)