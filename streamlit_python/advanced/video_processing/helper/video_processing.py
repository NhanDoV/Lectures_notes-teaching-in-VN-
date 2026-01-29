import cv2
import subprocess

# ======================== I/O
def read_video(path):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        raise IOError("Cannot open video")

    fps = cap.get(cv2.CAP_PROP_FPS)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    return cap, fps, w, h, total


def write_video(path, fps, w, h):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    return cv2.VideoWriter(path, fourcc, fps, (w, h))

# ====================== TRANSFORM
def to_grayscale(frame_bgr):
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


def invert_frame(frame_bgr):
    return 255 - frame_bgr

# ====================== 
def invert_video_frames(cap, writer):
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    for frame in reversed(frames):
        writer.write(frame)


def apply_frame_transform(cap, writer, transform_fn):
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        writer.write(transform_fn(frame))

def video_info(fps, total_frames):
    duration = total_frames / fps
    return {
        "fps": fps,
        "frames": total_frames,
        "duration_sec": round(duration, 2)
    }
