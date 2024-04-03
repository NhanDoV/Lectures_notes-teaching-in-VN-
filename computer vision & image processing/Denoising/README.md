## 1. Tạo hình ảnh có nhiễu
### 1.1. Tải một hình bất kỳ
```
import cv2
import numpy as np
import matplotlib.pyplot as plt
from noise_preprocessing import *

img_normal = cv2.imread(r"\Nhan_pro\Data\computer_vision_data\fig3.jpg", 0)
plt.figure(figsize = (10, 6))
plt.imshow(img_normal, 'gray')
plt.show()
```

![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/2b32731b-64a1-4420-bca2-78b2af171917)

### 1.2. Các nhiễu với các variance(of noise) khác nhau
```
noise_show(img_normal, [4, 9, 12, 16, 25, 30], 3, (24, 21))
```
![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/b355ff78-9f87-427e-b5e5-c5e06fbff2d0)

Như vậy ta thấy rằng mật độ nhiễu của hình tỷ lệ thuận với độ tăng của các variance

### 1.3. Lấy một hình có noise bất kỳ khác
```
org_img_1 = cv2.imread(r"\Nhan_pro\Data\computer_vision_data\noise_img1.jpg")
plt.figure(figsize = (15, 8))
plt.imshow(org_img_1, 'gray')
plt.title('original image')
plt.show()
```
![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/cddea28e-e939-4e84-8ee7-faf0684a8006)

```
s, h, k = 7, 40, 14 
DN_img_1 = cv2.fastNlMeansDenoising(org_img_1, h, h, 7, 21)
DN_img_2 = cv2.GaussianBlur(org_img_1, (s, s), 2*k)
DN_img_3 = cv2.GaussianBlur(DN_img_1, (s, s), 2*k)
DN_img_4 = cv2.fastNlMeansDenoising(DN_img_2, h, h, 7, 21)

plt.figure(figsize = (24, 18))

plt.subplot(221), plt.imshow(DN_img_1, 'gray')
plt.title('Denoise image using fastNlMeansDenoising:\n template_WindowSize = 7, search_WindowSize = 21')
plt.xlabel('filter strength = %s'%(h))

plt.subplot(222), plt.imshow(DN_img_2, 'gray')
plt.title('Denoise image using: Gaussian bluring \n (sigma_X, sigma_Y) = (%s, %s), ksize = %s'%(s, s, k))

plt.subplot(223), plt.imshow(DN_img_3, 'gray')
plt.title('Denoise image by:\n GaussianBlur(fastNlMeansDenoising(img))')

plt.subplot(224), plt.imshow(DN_img_4, 'gray')
plt.title('Denoise image by:\n fastNlMeansDenoising(GaussianBlur(img))')

plt.show()
```
![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/9aa8e20e-9529-41b1-9071-6f18565755a8)

- Tương tự nhưng cho một hình có nhiễu khác, ta được

![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/b1a3b4c5-e701-45c3-af27-1909b74d3a95)

## 2. Ảnh hưởng của các tham số đến việc xử lý nhiễu
### 2.1. filter_strength

We can guess the `sigma` (must be `odd`) of `random_noise` is too large, such as 49, 
- we put the `filter strength` is about `40` for using `cv2.fastNlMeansDenoising`
- and `sigma = 7` `ksize = 14` for using `cv2.GaussianBlur`

```
filter_strength_vary_show(org_img_1, [10, 20, 30, 40, 50, 60], 3, (20, 20))
```
![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/25fa3f61-95f3-4ab2-ae48-facbdaaa20b8)
hoặc
![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/b247e341-3ca0-4f34-bde4-6c783b86dc07)

Việc tăng `filter_strength` sẽ giúp việc giảm các nhiễu này tốt hơn

### 2.2. TemplateWindowSize
Khi xem xét `TemplateWindowSize` ảnh hưởng như thế nào đến việc giảm nhiễu thì ta sẽ cố định đồng thời các tham số khác như `filter_strength`
```
template_WindowSize_vary_show(org_img_1, [3, 7, 37, 121], 2, (20, 20))
```
![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/a8dfde7b-9db9-4cfe-9021-476b009ba9bf)
hoặc
![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/c46dca8a-7a54-4a87-b6f1-0ace549993df)
Như vậy, việc lạm dụng tăng giá trị `TemplateWindowSize` có thể sẽ dẫn đến hình ảnh bị nhòa đi

### 2.3. SearchWindowSize
```
search_WindowSize_vary_show(org_img_1, [14, 21, 35, 91], 2, (20, 16))
```
![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/2254d344-8fc2-4631-a987-5e4c193a96e3)
hoặc
![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/fd0b1dbf-98a1-4838-a687-b42c345f3131)

### 2.4. Sigma
```
sigma_gaussianblur_vary_show(org_img_1, [(5, 5), (5, 7), (7,5), (7, 7), (15, 7), (15, 15)], 3, (20, 16))
```
![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/00997f6b-2f3d-49b9-9ee0-5768e3fb1df0)

hoặc

![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/ba493fd5-6b4f-4df0-9c66-ffcd7d0394b3)

## 3. Cho hình ảnh trắng-đen
Tương tự như trên nhưng ta có điều chỉnh như sau
```
org_img_1 = cv2.imread(r"\Nhan_pro\Data\computer_vision_data\noise_img1.jpg", 0)
plt.figure(figsize = (15, 8))
plt.imshow(org_img_1, 'gray')
plt.title('original image')
plt.show()
```
![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/3eb1a0ec-a1c3-4c31-8e37-0f8ab5be1e83)
Tiếp theo ta cũng sẽ thấy ảnh hưởng của các tham số đến việc giảm nhiễu tương tự như cho phần trên (với ảnh màu)
### 3.1. filter_strength

![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/182a212f-ff58-4080-afeb-1c54f9c6fb39)


### 3.2. TemplateWindowSize

![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/e03b5c2d-9e51-4d81-bb63-3e5fc072f70c)


### 3.3. SearchWindowSize

![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/044e931f-4170-419c-a632-4bc76b9b4195)

### 3.4. Sigma

![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/3cd5efe6-ffea-440a-af3d-67980c224f6c)

### 3.5. ksize

![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/1b8c8db5-b7d1-4c74-b4c0-1d39f4e6c959)

![image](https://github.com/NhanDoV/Cycle-GANs/assets/60571509/e205b34c-27d3-4a09-93c0-46a8364045e0)
