### Mở đầu
`A/B testing` là một phương pháp nghiên cứu trải nghiệm người dùng dựa trên 2 biến thể `A`, `B`. Thực nghiệm này là một cách để so sánh hai phiên bản của một biến, thường bằng cách kiểm tra phản ứng của đối tượng đối với biến thể `A` so với biến thể `B`, và từ đó xác định xem biến thể nào có hiệu quả tốt hơn.

Trong phần này, ngoại trừ các khái niệm thống kê thường dùng trực tiếp trong kiểm định như $p-$value, giả thuyết không (`null hypothesis`) thì ta cũng cần chú ý đến các khái niệm đặc thù khác như:

- tỷ lệ chuyển đổi (`conversion rate`) hay tỷ lệ nhấp (`CTR [click-through rate]`): là tỷ lệ người thực hiện các hành động trong tổng số người tham gia khảo sát.
- cỡ mẫu (`sample size`): trong một số trường hợp `[Xem nó ở ví dụ 1.3]`, ta cần xác định số người (số mẫu cần khảo sát) tối thiểu để thực nghiệm (trong 2 nhóm `control_group` và `experiment_group` (hay test_group).
- công cụ đánh giá (`metric`), là phương thức để tính toán khi thực hiện kiểm định.

**Reminders** (cho mọi bài toán kiểm định thống kê):

- $p-$ value: Về quan điểm thống kê, nó được định nghĩa bởi $P(H_0 | \text{unknown F})$, cụ thể ta có

| Đối thuyết | Công thức | Ý nghĩa |
|-|-|:-|
|H1: \mu != \mu_0 | `P(X != X_0 given H0) = 2*P(X < X0 given H0)`| kiểm định với đối thuyết 2 phía |
|H1: \mu > \mu_0 | `P(X > X_0 given H0)`| kiểm định với đối thuyết bên phải (`upper tailed`)|
|H1: \mu < \mu_0 | `P(X < X_0 given H0)`| kiểm định với đối thuyết bên trái (`lower tailed`)|

- `Kiểm định giả thiết không (null hypothesis)` là lập luận bác bỏ một luận đề được thích nghi cho khoa học thống kê. Về bản chất, một khẳng định được coi là hợp lệ nếu khẳng định đối lập của nó không thể thực hiện được.

#### Sample size
- **Baseline conversion rate (B_rate)**. `Baseline conversion rate` is the current conversion rate of your `control_group` or existing product as it
- **Minimum Detectable Effect (MDE)** conversion rate lifted by the Absolute “Minimum Detectable Effect”, which means **B_rate + Abs(MDE)**. `MDE` is calculated by (`desired conversion rate lift`/`baseline conversion rate`)*100. The `MDE` talks about that marginal impact you want to detect. (The larger the MDE, the smaller the sample size needed to run your experiment)