import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import datetime
import pytz

# Tiêu đề cho ứng dụng
st.title("Ứng dụng Thanh Trượt Số")
page = st.sidebar.radio("Chọn trang", ("Trang 1", "Trang 2", "Trang 3"))
# Trang 1
if page == "Trang 1":
    st.subheader("Trang 1: Thanh trượt số và tính toán")
    st.text_area("Description", """ 
                 Chỗ này dùng công thức tính vui để ước lượng mức thu tổng tài sản mà bạn đã từng mong muốn dựa trên các con số bói toán đơn giản.
                 Bằng cách kéo chuột các con số bên dưới, bạn sẽ nhận được output tương ứng
                 """, height=150)    
    st.markdown("""
        <style>
        /* CSS cho các mục */
        .highlight-phone {
            background-color: #3A5B7C;  /* Màu xanh navy nhạt pha đậm */
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);  /* Đổ bóng nhẹ */
        }

        .highlight-time {
            background-color: #4C6C8B;  /* Màu xanh navy nhạt pha sáng hơn một chút */
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.25);  /* Đổ bóng nhẹ */
        }

        .highlight-age {
            background-color: #5F7E96;  /* Màu xanh xám nhạt hơn một chút */
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);  /* Đổ bóng mạnh hơn */
        }

        .highlight-income {
            background-color: #FF9E4F;  /* Màu cam nhạt */
            color: #fff;
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
            text-align: center;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);  /* Đổ bóng nhẹ */
        }

        /* Tạo khoảng cách giữa highlight-age và highlight-income */
        .highlight-age {
            margin-bottom: 50px;  /* Thêm khoảng cách dưới phần tử này */
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Hàm để định dạng số điện thoại
    def format_phone_number(number):
        # Chuyển số thành chuỗi và thêm dấu cách sau mỗi 3 chữ số
        return '{:,}'.format(number).replace(',', ' ')

    def format_timestamp(timestamp):
        # Chuyển đổi timestamp thành đối tượng datetime
        dt = datetime.datetime.utcfromtimestamp(timestamp)
        # Chuyển đổi múi giờ (ví dụ: chuyển sang GMT+7)
        tz = pytz.timezone('Asia/Ho_Chi_Minh')
        dt = pytz.utc.localize(dt).astimezone(tz)
        
        # Định dạng lại ngày tháng năm giờ phút giây
        return dt.strftime('%d-%m-%Y %H:%M:%S')

    # Giới hạn của thanh trượt từ 0 đến 1 tỷ
    number = st.slider("Chọn một số", min_value=0, max_value=9999999999, step=1)
    formatted_number = format_phone_number(number)
    # Hiển thị giá trị số điện thoại đã được định dạng
    # st.write(f"Số điện thoại bạn đã chọn là: 0 {formatted_number}")
    st.markdown(f'<div class="highlight-phone">Số điện thoại bạn đã chọn là: + 84 {formatted_number}</div>', unsafe_allow_html=True)
    
    # Cho thời gian
    timestamp = st.slider("Chọn mốc thời gian (số giây từ 01/01/1970)", min_value=0, max_value=9999999999, step=1)
    formatted_time = format_timestamp(timestamp)
    st.markdown(f'<div class="highlight-time">Ngày giờ bạn đã chọn là: {formatted_time}</div>', unsafe_allow_html=True)
    
    # age
    age_num = st.slider("Chọn một số", min_value=10, max_value=200, step=1)
    st.markdown(f'<div class="highlight-age">Tuổi bạn đã chọn là: {age_num}</div>', unsafe_allow_html=True)
    
    # income
    if number > timestamp:
        income = number * age_num / 29
    else:
        income = timestamp * age_num // 31
        
    st.markdown(f'<div class="highlight-income">Thu nhập của bạn đang mong muốn là: <br> $ {income:,.2f}</div>', unsafe_allow_html=True)
    
elif page == "Trang 2":
    st.markdown("""
        <style>
        /* Đổi độ rộng của container chính */
        .main .block-container {
            max-width: 1200px; /* Điều chỉnh độ rộng tối đa của giao diện */
            padding-top: 5rem;
            padding-bottom: 5rem;
        }
        </style>
    """, unsafe_allow_html=True)
        
    st.subheader("Trang 2: Ellipse by polar-coordinate")
    st.text_area("Description", """Polar coordinate hay tọa độ cực, một công thức mô tả ellipse tổng quát
                    ```
                        x = x0 + r*cos(theta)                        
                        y = y0 + R*sin(theta)
                    ```
                 """, height=150)
    
    def ellipse(r, R):
        t = np.linspace(0, 2 * np.pi, 101)  # Tăng độ chính xác
        x = R * np.cos(t)
        y = r * np.sin(t)
        return x, y

    def encode_color(color):
        # Chuyển số color thành giá trị thập lục phân với 6 ký tự
        return f"#{color:06X}"    

    # Tạo hai cột: Cột bên trái chứa thanh trượt, cột bên phải chứa hình vẽ
    col1, col2 = st.columns([1, 2])

    # Cột bên trái: Thanh trượt điều chỉnh bán kính của ellipse
    with col1:
        st.header("Chỉnh Sửa Bán Kính - màu")
        r = st.slider("Bán kính trục bé (r)", min_value=1, max_value=100, step=1, value=10)
        R = st.slider("Bán kính trục lớn (R)", min_value=1, max_value=100, step=1, value=30)
        color = st.slider("Mã màu đường viền", min_value=1, max_value=90000, step=1, value=5)

    # Cột bên phải: Hiển thị hình vẽ ellipse
    with col2:
        st.header("Result")
        
        # Vẽ ellipse bằng hàm ellipse()
        x, y = ellipse(r, R)
        color_hex = encode_color(color)
        
        # Sử dụng Matplotlib để vẽ ellipse
        fig, ax = plt.subplots()
        ax.plot(x, y, label="Ellipse", color=color_hex)
        ax.fill(x, y, 'skyblue', alpha=0.5)  # Tô màu nhẹ bên trong ellipse
        ax.set_aspect('equal', 'box')  # Đảm bảo tỉ lệ đúng
        ax.set_title("Hình Ellipse")
        ax.legend()

        # Hiển thị hình vẽ trong Streamlit
        st.pyplot(fig)

# Trang 3
elif page == "Trang 3":
    st.subheader("Trang 3: Change color-space of any image")
    st.text_area("Description", """Trang này cho phép bạn điều chỉnh các giá trị màu sắc của Red, Green và Blue và xem ngay sự thay đổi trên hình vuông mô phỏng không gian màu RGB. Hãy thử thay đổi giá trị của từng thanh trượt và quan sát kết quả.
                 """, height=80)    
    st.markdown("""
        <style>
        /* Đổi độ rộng của container chính */
        .main .block-container {
            max-width: 1000px; /* Điều chỉnh độ rộng tối đa của giao diện */
            padding-top: 5rem;
            padding-bottom: 5rem;
        }
        </style>
    """, unsafe_allow_html=True)
            
    def plot_color_squares(r, g, b):
        # Tạo một mảng 2D với 4 hình vuông nhỏ
        colors = np.array([[[r, 0, 0], [0, 0, b]],
                        [[0, g, 0], [r, b, g]]])

        # Vẽ hình vuông với các màu sắc
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.imshow(colors)
        ax.axis('off')  # Tắt trục toạ độ
        ax.set_title("RGB colors")

        # Hiển thị hình ảnh
        st.pyplot(fig)
    
    col1, col2 = st.columns([1, 2])
    with col1:    
        r = st.slider("Giá trị của kênh Red", min_value=0, max_value=255, step=1, value=255)
        b = st.slider("Giá trị của kênh Blue", min_value=0, max_value=255, step=1, value=255)
        g = st.slider("Giá trị của kênh Green", min_value=0, max_value=255, step=1, value=255)
    with col2:
        plot_color_squares(r, g, b)