## Mở đầu
Vanilla GAN Generator, sự khác biệt cơ bản giữa DCGANs vs VanillaGANs là ở

    * DCGANs có sử dụng deep-convolution
        (D): RELU activation được sử dụng trong Generator ở hầu hết các layers trừ layers-output sẽ dùng hàm Tanh, trong khi
        (G): Discriminator tất cả các layer đều sử dụng Leaky-ReLu làm activation function. 
    * Adam optimizer is used with a learning rate of 0.0002

Đây là mô hình GANs cơ bản nhất với 2 quá trình là Generator vs Discriminator
trong đó:

    * Generator sẽ phát sinh ra các fake-image
    * Discriminator sẽ tính xác suất của hình ảnh nhận được từ Generator rồi nhận diện nó là real hay fake
Cuối cùng, các phản hồi từ cả 2 quá trình sẽ được đo đạc bởi các loss function và do đó mục tiêu tối thiểu hóa các loss-function này
là mục tiêu sau cùng của Vanilla-GANs.  

## Ví dụ
Trong phần này ta có 2 ví dụ 
- MNIST digits: phát sinh các chữ số viết tay (dataloader sẽ được tải về từ MNIST với function `prepare_dataset`) 

- womanface / cartoon: dữ liệu sẽ được tải từ local với tham số `data_root`