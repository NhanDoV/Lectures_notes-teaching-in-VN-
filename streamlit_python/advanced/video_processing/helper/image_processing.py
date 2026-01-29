import cv2
import numpy as np

# ========================= 1. COLOR PROCESSING ============================
# ------------- 1.1. Replace channel-color by any pixel
def load_image_from_upload(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), 
                            dtype = np.uint8)
    img_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    return img_bgr

def replace_channel(img_bgr, channel_id, pixel_val):
    res = img_bgr.copy()
    res[:, :, channel_id] = pixel_val

    return res

def bgr_to_rgb(img_bgr):
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

def rgb_to_gray(img_rgb):
    return cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

def changing_channel_color_space(uploaded_file, channel_id, pixel_val):
    img_bgr = load_image_from_upload(uploaded_file)
    res_bgr = replace_channel(img_bgr, channel_id, pixel_val)

    return bgr_to_rgb(res_bgr)

# ------------- 1.2. HSV range
def hsv_mask(uploaded_file, lower, upper):
    img_bgr = load_image_from_upload(uploaded_file)
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)

    return mask

def hsv_mask_and_fill(uploaded_file, lower, upper, pixel_val):
    # Load image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Convert to HSV
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    lower = np.array(lower, dtype=np.uint8)
    upper = np.array(upper, dtype=np.uint8)

    # Create mask
    mask = cv2.inRange(hsv, lower, upper)

    # Fill pixels INSIDE mask (example: fill V channel)
    res_hsv = hsv.copy()
    res_hsv[mask > 0, 2] = pixel_val

    # Back to RGB
    res_bgr = cv2.cvtColor(res_hsv, cv2.COLOR_HSV2BGR)
    res_rgb = cv2.cvtColor(res_bgr, cv2.COLOR_BGR2RGB)

    return res_rgb, mask

def hsv_range_bar(h_range, width=360, height=40):
    bar = np.zeros((height, width, 3), dtype=np.uint8)

    for x in range(width):
        hue = int(179 * x / width)
        bar[:, x] = (hue, 255, 255)

    bar_bgr = cv2.cvtColor(bar, cv2.COLOR_HSV2BGR)
    bar_rgb = cv2.cvtColor(bar_bgr, cv2.COLOR_BGR2RGB)

    # Highlight selected range
    x1 = int(width * h_range[0] / 179)
    x2 = int(width * h_range[1] / 179)
    bar_rgb[:, :x1] //= 3
    bar_rgb[:, x2:] //= 3

    return bar_rgb

# ========================= 2. TRANSFORMATION ==================
# --------------- 2.1.
def get_img_dimension_from_bgr(img_bgr):
    h, w, _ = img_bgr.shape
    return h, w

def get_translation_img_from_bgr(img_bgr, x, y):
    rows, cols, _ = img_bgr.shape
    M = np.float32([
        [1, 0, x],
        [0, 1, y]
    ])
    res_bgr = cv2.warpAffine(img_bgr, M, (cols, rows))
    return bgr_to_rgb(res_bgr)

# --------------- 2.2.
def get_rotation_img(img_bgr, cx, cy, angle):
    
    height, width = img_bgr.shape[:2]
    center = (cx, cy)

    # Get the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
    
    # Perform the rotation
    rotated_image = cv2.warpAffine(img_bgr, rotation_matrix, (width, height))

    return bgr_to_rgb(rotated_image)

# --------------- 2.3.
def get_complement_pixel(img_bgr):
    return bgr_to_rgb(~img_bgr)

def color_bar(rgb, width=200, height=20):
    bar = np.ones((height, width, 3), dtype=np.uint8)
    bar[:] = rgb
    return bar

def get_pixel_rgb(img_bgr, x, y):
    b, g, r = img_bgr[y, x]
    return np.array([r, g, b], dtype = np.uint8)

def complement_rgb(rgb):
    return 255 - rgb

# ----------------- 2.4. Other transformations
import skimage.transform as skt

def sine_piecewise_transform(img_bgr, transform_type="sine_transform"):
    # BGR → RGB → float
    image = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) / 255.0

    rows, cols = image.shape[:2]

    src_cols = np.linspace(0, cols, 20)
    src_rows = np.linspace(0, rows, 10)
    src_rows, src_cols = np.meshgrid(src_rows, src_cols)
    src = np.dstack([src_cols.flat, src_rows.flat])[0]

    x = np.linspace(0, 3 * np.pi, src.shape[0])

    if transform_type == "sine_transform":
        dst_rows = src[:, 1] - np.sin(x) * 50
    elif transform_type == "cosine_transform":
        dst_rows = src[:, 1] - np.cos(x) * 50
    elif transform_type == "tan_transform":
        dst_rows = src[:, 1] - np.tan(x) * 50
    elif transform_type == "tanh_transform":
        dst_rows = src[:, 1] - np.tanh(x) * 50
    elif transform_type == "sinh_transform":
        dst_rows = src[:, 1] - np.sinh(x) * 50
    elif transform_type == "cosh_transform":
        dst_rows = src[:, 1] - np.cosh(x) * 50
    else:
        dst_rows = src[:, 1]

    dst_cols = src[:, 0]
    dst_rows = dst_rows * 1.5 - 1.5 * 50
    dst = np.vstack([dst_cols, dst_rows]).T

    tform = skt.PiecewiseAffineTransform()
    tform.estimate(src, dst)

    out_rows = int(rows - 1.5 * 50)
    out_cols = cols

    warped = skt.warp(
        image,
        tform,
        output_shape=(out_rows, out_cols)
    )

    # back to uint8 RGB
    warped_uint8 = (warped * 255).astype(np.uint8)

    return warped_uint8

# ----------------- 2.5. Bluring
import cv2

def apply_blur(img_bgr, method, ksize, sigma):
    """
        method: 'Gaussian' | 'Median' | 'Bilateral'
        ksize: odd integer
        sigma: float (used for Gaussian & Bilateral)
    """

    if method == "Gaussian":
        k = (ksize, ksize)
        return cv2.GaussianBlur(img_bgr, k, sigmaX=sigma)

    elif method == "Median":
        # MedianBlur chỉ nhận ksize (odd)
        return cv2.medianBlur(img_bgr, ksize)

    elif method == "Bilateral":
        # d = diameter of pixel neighborhood
        d = ksize
        sigmaColor = sigma * 25 if sigma > 0 else 75
        sigmaSpace = sigma * 25 if sigma > 0 else 75
        return cv2.bilateralFilter(
            img_bgr,
            d=d,
            sigmaColor=sigmaColor,
            sigmaSpace=sigmaSpace
        )

    else:

        return img_bgr

# ------------------ 2.6. DENOISING
def add_white_gaussian_noise(img, sigma):
    """
        img: float image in [0,1]
        sigma: noise std (0–10 typical)
    """
    noise = np.random.normal(0, sigma / 255.0, img.shape)
    noisy = img + noise
    return np.clip(noisy, 0, 1)

def gaussian_psf(ksize, sigma):
    ax = np.arange(-ksize // 2 + 1., ksize // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2. * sigma**2))
    kernel /= np.sum(kernel)
    return kernel

def psf_to_otf(psf, shape):
    """
        Convert PSF to OTF for FFT
    """
    otf = np.zeros(shape)
    psf_shape = psf.shape
    otf[:psf_shape[0], :psf_shape[1]] = psf
    otf = np.roll(otf, -psf_shape[0] // 2, axis=0)
    otf = np.roll(otf, -psf_shape[1] // 2, axis=1)
    return np.fft.fft2(otf)

def wiener_deconvolution(img, psf, noise_sigma):
    """
        img: degraded image (float, [0,1])
        psf: blur kernel
        noise_sigma: assumed noise std
    """
    img_fft = np.fft.fft2(img)
    H = psf_to_otf(psf, img.shape)
    H_conj = np.conj(H)

    K = (noise_sigma / 255.0) ** 2  # noise power

    wiener_filter = H_conj / (np.abs(H)**2 + K)
    result_fft = wiener_filter * img_fft
    result = np.real(np.fft.ifft2(result_fft))

    return np.clip(result, 0, 1)

# =================================
from sklearn.cluster import KMeans

def convert_color_space(img_bgr, color_space):
    if color_space == "RGB":
        return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    elif color_space == "HSV":
        return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    elif color_space == "LAB":
        return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
    else:
        return img_bgr
    
def get_kmeans_segments(img_bgr, nb_clusters=4, color_space="RGB", normalize=True, random_state = 42):
    """
        Parameters
        ----------
        img_bgr : np.ndarray
            Input image in BGR format
        nb_clusters : int
            Number of KMeans clusters
        color_space : str
            RGB | HSV | LAB
        normalize : bool
            Normalize pixel values before clustering
        random_state : int
            Reproducibility

        Returns
        -------
        seg_rgb : np.ndarray
            Segmented image in RGB
        label_map : np.ndarray
            Cluster index per pixel
    """

    # Convert color space for clustering
    img_cs = convert_color_space(img_bgr, color_space)

    h, w, c = img_cs.shape
    X = img_cs.reshape((-1, c)).astype(np.float32)

    if normalize:
        X /= 255.0

    kmeans = KMeans(
        n_clusters=int(nb_clusters),
        random_state=random_state,
        n_init=10
    )
    labels = kmeans.fit_predict(X)

    centers = kmeans.cluster_centers_
    if normalize:
        centers = (centers * 255).astype(np.uint8)
    else:
        centers = centers.astype(np.uint8)

    segmented = centers[labels]
    segmented = segmented.reshape((h, w, c))

    # Always return RGB for displaying
    if color_space == "RGB":
        seg_rgb = segmented
    else:
        seg_rgb = cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB)

    label_map = labels.reshape((h, w))

    return seg_rgb, label_map

# -----

def load_gray_from_upload(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    return gray


def sobel_edge(gray, ksize=3):
    gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
    gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)
    mag = cv2.magnitude(gx, gy)
    mag = np.uint8(255 * mag / np.max(mag))
    return mag


def laplacian_edge(gray, ksize=3):
    lap = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
    lap = np.uint8(np.absolute(lap))
    return lap


def canny_edge(gray, t1=50, t2=150):
    return cv2.Canny(gray, t1, t2)

# ----------- 2.3.
def eigen_cartoonize(img_bgr, bilateral_d=9, sigma_color=75, sigma_space=75, edge_thresh1=50, edge_thresh2=150):
    # 1. Smooth colors but preserve edges
    smooth = cv2.bilateralFilter(
        img_bgr,
        d=bilateral_d,
        sigmaColor=sigma_color,
        sigmaSpace=sigma_space
    )

    # 2. Edge detection
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, edge_thresh1, edge_thresh2)

    # 3. Make edge mask
    edge_inv = cv2.bitwise_not(edges)
    edge_inv = cv2.cvtColor(edge_inv, cv2.COLOR_GRAY2BGR)

    # 4. Combine
    cartoon = cv2.bitwise_and(smooth, edge_inv)

    return cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)