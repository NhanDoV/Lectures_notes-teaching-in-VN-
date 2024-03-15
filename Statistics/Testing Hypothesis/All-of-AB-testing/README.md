## 1. Mở đầu
`A/B testing` là một phương pháp nghiên cứu trải nghiệm người dùng dựa trên 2 biến thể `A`, `B`, trong đó
- `A` đại diện cho nhóm kiểm soát (hay còn gọi là `control_group`) là các biến thể không thể thay đổi (giữ nguyên trạng thái hiện tại của sản phẩm)
- `B` đại diện cho các biến thể có sự thay đổi.
  
Thực nghiệm này là một cách để so sánh hai phiên bản của một biến, thường bằng cách kiểm tra phản ứng của đối tượng đối với biến thể `A` so với biến thể `B`, và từ đó xác định xem biến thể nào có hiệu quả tốt hơn.

#### Mục đích
- Cải thiện `tỷ lệ chuyển đổi trang web` hay `chiến dịch tiếp thị`
- tiết kiệm chi phí / tăng doanh thu
- giảm tỷ lệ thoát trang / giảm sự bỏ qua các giỏ hàng.

Trong phần này, ngoại trừ các khái niệm thống kê thường dùng trực tiếp trong kiểm định như $p-$value, giả thuyết không (`null hypothesis`) thì ta cũng cần chú ý đến các khái niệm đặc thù khác như:

- tỷ lệ chuyển đổi (`conversion rate`) hay tỷ lệ nhấp (`CTR [click-through rate]`): là tỷ lệ người thực hiện các hành động trong tổng số người tham gia khảo sát.
- cỡ mẫu (`sample size`): trong một số trường hợp, ta cần xác định số người (số mẫu cần khảo sát) tối thiểu để thực nghiệm (trong 2 nhóm `control_group (A)` và `experiment_group` (hay `test_group (B)`).
- công cụ đánh giá (`metric`), là phương thức để tính toán khi thực hiện kiểm định.

**Reminders** (cho mọi bài toán kiểm định thống kê):

- $p-$ value: Về quan điểm thống kê, nó được định nghĩa bởi $P(H_0 | \text{unknown F})$, cụ thể ta có

| Đối thuyết | Công thức | Ý nghĩa |
|-|-|:-|
|$H_1:$ $\mu \neq \mu_0$ | $P(X \neq X_0$ given $H0) = 2*P(X < X0$ given $H0)$ | kiểm định với đối thuyết 2 phía |
|$H_1:$ $\mu > \mu_0$ | $P(X > X_0$ given H0)`| kiểm định với đối thuyết bên phải (`upper tailed`)|
|$H_1:$ $\mu < \mu_0$ | $P(X < X_0$ given H0)`| kiểm định với đối thuyết bên trái (`lower tailed`)|

- `Kiểm định giả thiết không (null hypothesis)` là lập luận bác bỏ một luận đề được thích nghi cho một kiểm định Thống kê. Về bản chất, một khẳng định được coi là hợp lệ nếu khẳng định đối lập của nó không thể thực hiện được.

#### Sample size
- **Baseline conversion rate (`B_rate`)**. là tỷ lệ chuyển đổi hiện tại của `nhóm control`.
- **Minimum Detectable Effect (`MDE`)** được hiểu là sự thay đổi nhỏ nhất trong số liệu mà thử nghiệm có thể phát hiện được một cách đáng tin cậy.

            * Ví dụ như khi thực hiện testing một chiến lược tiếp thị qua email mới (giả sử hình thức trước đó là qua TV),
              mục đích là tìm hiểu xem chiến lược mới này có thể tăng tỷ lệ mở email hay không?
            * Khi đó với các mức tăng như 5%, 10%, 1%, etc thì sample-size sẽ được xác định như thế nào?
Ta có 

$$ n = \dfrac{( z_{\alpha / 2} * \sqrt{ 2 * B_{\text{rate}} * (1-B_{\text{rate}})} + z_{1-\beta} * \sqrt{ B_{\text{rate}} * (1-B_{\text{rate}})+\text{MDE} * (1-\text{MDE}))})^2 }{( \text{MDE} - B_{\text{rate}} )^2} $$

trong đó 
- $z_{\alpha / 2}$ là phân vị mức $\alpha / 2$
- $\alpha$: mức ý nghĩa hoặc tỷ lệ dương tính giả [`Significance level` (False positive)]
- $1-\beta$: là độ mạnh của kiểm định mà hiệu quả của nó là tối thiểu [`statistical power` (minimum effect)]

Như vậy, **`MDE` càng bé thì thử nghiệm sẽ càng phát hiện được những thay đổi tinh tế hơn** tuy nhiên `sample-size` cũng sẽ lớn hơn.

#### Bài toán
            Tỷ lệ chuyển đổi hiện tại của một trang web hoặc kênh trước khi thực hiện bất kỳ thay đổi nào đối với nó. 
            Hãy xem xét mục tiêu của chúng tôi là thay đổi vị trí của nút "thêm vào giỏ hàng" và tỷ lệ chuyển đổi hiện tại của chúng tôi, 
            - Số người dùng đến trang web của bạn là 4000 và 
            - Số người dùng nhấp vào nút 'thêm vào giỏ hàng' là 800.

khi đó
- Tỷ lệ chuyển đổi cơ sở cho Biến thể đối chứng `A` $B_{\text{rate}}$ là: `20%` (chia tỷ lệ nhấp chuột này (`800`) cho tổng số người dùng (`4000`) sẽ cung cấp cho bạn tỷ lệ chuyển đổi cơ bản ở đây sẽ là `20%`)
- Tỷ lệ chuyển đổi **dự kiến (kỳ vọng)** cho Biến thể thử nghiệm `B` $R_\text{mde}$ là: `22%`

và ta tìm được $n = 6347$, khi đó cho 2 biến thể $A, B$ ta cần đến $2n = 12694$ quan sát cho cả hai. Tiếp tục chia con số này cho tổng số khách truy cập mỗi ngày là 4000 (tham khảo phần chuyển đổi cơ sở) trong trường hợp của chúng tôi, sẽ cho chúng tôi số ngày thử nghiệm sẽ chạy là khoảng 6.3 ngày.

## 2. Quy trình thực hiện
- **`B1. Xác định mục tiêu cụ thể`**. Có thể là

            "tỷ lệ đăng ký"
            "thời gian truy cập"
            "tỷ lệ chuyển đổi trên trang sản phẩm"
- **`B2. Lên kế hoạch test trên 2 biến thể`**, Ta cũng cần hiểu rõ bối cảnh của doanh nghiệp, bài toán và sản phẩm
- **`B3. Thiết kế kiểm định và tạo biến thể`**. Ở bước này, ta cần xác định được

            null hypothesis
            metric nào cần dùng để thực hiện
            sample-size, và từ đó suy ra testing-time
- **`B4. Triển khai test và theo dõi KQ`**
- **`B5. Báo cáo, phân tích KQ và đưa tra KL và đánh giá`** để từ đó quyết định biến thể nào sẽ dùng để triển khai
- **`B6. Triển khai và theo dõi các biến thể được chọn`** Xem biến thể mới có hoạt động tốt hơn và ổn định hay không, có cần phải thực hiện một thử nghiệm A/B testing nào khác nữa hay không? (Biết điểm dừng để đưa ra quyết định)

#### Cách đọc kết quả
- **Đo lường và kiểm tra các chỉ số mục tiêu**

            Tùy thuộc vào mục đích và mục tiêu của bạn khi thực hiện A/B Testing, có thể có nhiều chỉ số mục tiêu khác nhau để đánh giá hiệu quả của thử nghiệm.
            Điều quan trọng là bạn phải quyết định trước những chỉ số mục tiêu mà bạn muốn đo lường và theo dõi để đánh giá hiệu quả của thử nghiệm của mình.
- **So sánh với tỷ lệ chuyển đổi**

            Để đánh giá hiệu quả của chúng. Tỷ lệ chuyển đổi được xác định bằng tỷ lệ giữa số lượt chuyển đổi và tổng số lượt thử nghiệm.
            Biến thể nào có tỉ lệ chuyển đổi cao hơn là biến thể tối ưu hơn.
- **Tạo các phân đoạn công chúng (audience segmentation) để tìm thêm insight**

            Chia người dùng thành các nhóm khác nhau dựa trên các thuộc tính và đặc điểm cụ thể và kiểm tra hiệu quả của các biến thể A/B testing đối với mỗi nhóm này.
            Từ đó, ta có thể đo lường hiệu quả của các biến thể A/B testing đối với từng nhóm.
            Điều này sẽ giúp bạn tìm ra những thông tin mới và đưa ra quyết định tối ưu hóa tốt hơn.

#### Một số lưu ý khi tiến hành thực hiện
- Bên cạnh việc `sample-size` của 2 nhóm $A, B$ phải bằng nhau thì ta cũng phải đảm bảo rằng các quan sát ở các nhóm phải đảm bảo tính ngẫu nhiên 
- Ngoài ra nếu `sample-size` quá nhỏ thì kết quả kiểm định sẽ có độ tin cậy thấp còn nếu quá lớn sẽ tốn nhiều thời gian và chi phí
- Phải đảm bảo quy trình testing được diễn ra trong một thời điểm của chiến dịch, tránh việc nó diễn ra ở những nút giao thời điểm mà nhân tố thời vụ (seasonality) tác động đến
- Yêu cầu phản hồi từ người dùng thực (`user feedback`) là một yếu tố quan trọng khi triển khai `A/B Testing`. Hoạt động này giúp bạn đánh giá hiệu quả của chiến dịch từ góc độ của người dùng thực, từ đó ta có thể hiểu được về cảm nhận, trải nghiệm và phản hồi của người dùng đối với các biến thể của chiến dịch.
- Nếu có điều kiện, hãy tiến hành testing cho `mobile` và `desktop` riêng biệt
- **Nên tiến hành ở những khách hàng tiềm năng mới**, tuy nhiên để xác định đúng `khách hàng tiềm năng` đòi hỏi các giả định và thuật toán phải tốt
  
#### Một số việc nên tránh
- **Không nên kết luận quá sớm với kết quả**. Kết luận khi mới test 1 lần hoặc test trong 1 đến 2 ngày kết quả này sẽ không chính xác.
- **Đừng để linh cảm chi phối kết quả**.

          * Dữ liệu hành vi người dùng và dữ liệu khảo sát khách hàng có thể bị xung đột vì một số phương pháp khảo sát trong quá trình lấy mẫu,
            vì vậy cần giữ cho việc thu thập và sử dụng dữ liệu là tách biệt, độc lập của nhau.
          * Đôi lúc, sẽ có những phân khúc hành vi / tâm lý mới của khách hàng (và đặc biệt là nhân tố seasonality) nên không được đi theo `"lối mòn tư duy"`!
          * Lấy ý kiến từ nhiều nguồn là rất quan trọng để đảm bảo rằng quyết định cuối cùng của bạn là đúng và tối ưu hóa hiệu quả của trang web của bạn
            Hơn nữa, nó sẽ cung cấp góc nhìn (hành vi / tâm lý) của người dùng đa dạng hơn

- **Sample size** không đều giữa các biến thể, hoặc nếu bằng thì cả 2 lại quá bé hoặc quá lớn
- Again, **không được có sự sai lệch về thời gian thực hiện**

#### Các lỗi thường gặp
- **Công cụ testing bị lỗi** Ví dụ kết nối internet, cập nhật lại trình duyệt, khi đó cần phải liên hệ với nhà cung cấp dịch vụ để được hỗ trợ, sửa lỗi hoặc cung cấp giải pháp thay thế.
- **Ngừng test khi đã đạt kết quả**. Không nên ngừng test khi đã đạt kết quả mà cần xác định tiêu chí rõ ràng trước khi ngừng thử nghiệm.
- **Chỉ tập trung vào chuyển đổi**. Cần tập trung thêm đến `tốc độ tải trang, khả năng tiếp cận, số lượng truy cập, giá trị đơn hàng trung bình` để giúp tối ưu hóa và nâng cao trải nghiệm người dùng, giảm tỷ lệ thoát trang và tăng doanh thu 
- **Chỉ chú tâm tới thay đổi những thứ nhỏ nhặt** (tiêu đề, nội dung, hình ảnh, bố cục, etc) mà bỏ qua việc thay đổi mô hình kinh doanh, giao diện người dùng hoặc chức năng của trang web

## 3. FAQ
#### `A/B Testing` có thực sự quan trọng không?
- Có! Việc thực hiện này giúp người dùng đánh giá hiệu quả của các thay đổi trên trang web. 
- Thông qua `A/B Testing`, người dùng có thể kiểm tra và so sánh nhiều biến thể khác nhau của trang web hoặc ứng dụng, từ đó lựa chọn ra các loại biến thể tốt hơn và tiếp tục tối ưu hóa.
- `A/B Testing` giúp ứng dụng khoa học và quá trình lặp lại liên tục để tối ưu hóa trải nghiệm người dùng.

#### Khi nào thì nên triển khai `A/B testing`?
Đây là một phương pháp quan trọng để tối ưu hóa trang web, nhưng không phải trong tất cả các trường hợp đều nên triển khai. Dưới đây là một số trường hợp nên triển khai:
- **Mới triển khai trang web:** Khi bạn mới phát triển một trang web mới hoặc một hệ thống trang web mới, `A/B Testing` sẽ giúp bạn đánh giá và cải thiện các yếu tố của trang web để tăng tỷ lệ chuyển đổi.
- **Tần suất truy cập trang web thấp:** Khi lượng truy cập của trang web của bạn thấp, `A/B Testing` có thể giúp bạn xác định những yếu tố cần tối ưu để tăng tần suất truy cập và tỷ lệ chuyển đổi.
- **Cải thiện tỷ lệ chuyển đổi:** Khi bạn muốn cải thiện tỷ lệ chuyển đổi của trang web của mình, `A/B Testing` sẽ giúp bạn xác định những biến thể hoặc yếu tố của trang web có thể tăng tỷ lệ chuyển đổi.
- **Thời gian và tiền bạc có hạn:** A/B Testing là một phương pháp tối ưu hóa có thể tiết kiệm thời gian và tiền bạc của bạn so với việc thay đổi hoàn toàn trang web.
- **Cải thiện trải nghiệm người dùng:** Khi bạn muốn cải thiện trải nghiệm người dùng trên trang web của mình, `A/B Testing` sẽ giúp bạn đánh giá và cải thiện các yếu tố giao diện, định dạng, nội dung, vv.

#### Sau khi có kết quả `A/B Testing` thì nên làm gì?
Sau khi đã thực hiện `A/B Testing` và thu thập dữ liệu, bạn nên chú ý đến các bước sau để sử dụng kết quả:
- **Bước 1: Phân tích kết quả**: Hãy phân tích kết quả `A/B Testing` để xác định sự khác biệt giữa các biến thể và đánh giá việc cải thiện của các biến thể đối với mục tiêu của bạn.
- **Bước 2: Đưa ra quyết định**: Dựa trên kết quả của `A/B Testing`, bạn cần đưa ra **quyết định về biến thể nào** sẽ được áp dụng vào trang web hoặc sản phẩm của bạn.
- **Bước 3: Ghi nhận và học hỏi**: Hãy ghi nhận các kết quả `A/B Testing` để có thể học hỏi từ các thí nghiệm trước. Điều này sẽ giúp bạn tiếp cận với các thí nghiệm A/B tiếp theo một cách tốt hơn.
- **Bước 4: Thực hiện `thí nghiệm tiếp theo`**: Nếu biến thể `A/B testing` hiện tại không cải thiện hiệu quả của trang web hoặc sản phẩm của bạn, hãy xem xét thực hiện các thí nghiệm mới để tìm ra một cách tối ưu hóa tốt hơn.
  
## Tham khảo
  - [A/B testing wikipedia](https://en.wikipedia.org/wiki/A/B_testing)
  - [Quy trình triển khai A/B testing](https://mona.media/ab-testing/?fbclid=IwAR1UzmItivBHDSaDU4_EtV0MTJ5RUVOL6QjdPX-CxwtJM7cbyzlhl9XQW2M)
  - [MDE và sample-size](https://pulse/sample-sizing-ab-testing-jatin-shrivastava#:~:text=MDE%20or%20Minimum%20Detectable%20Effect,experiment%20to%20be%20adequately%20powered.)