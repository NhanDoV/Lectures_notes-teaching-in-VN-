## 1. Lan man, Hadoop and Spark
### Performance
- **Về tốc độ xử lý thì Spark nhanh hơn Hadoop**. `Spark` được cho là nhanh hơn `Hadoop` gấp `100 lần` khi chạy trên **`RAM`**, và gấp `10 lần` khi chạy trên **ổ cứng**. 
- Hơn nữa, người ta cho rằng `Spark` sắp xếp (sort) `100TB` dữ liệu nhanh gấp 3 lần `Hadoop` trong khi sử dụng ít hơn 10 lần số lượng hệ thống máy tính.
- Sở dĩ `Spark` nhanh là vì nó xử lý mọi thứ ở `RAM`. Nhờ xử lý ở bộ nhớ nên `Spark` cung cấp các phân tích dữ liệu thời gian thực cho các chiến dịch quảng cáo, `machine learning`, hay các trang web mạng xã hội.
- Tuy nhiên, khi `Spark` làm việc cùng các dịch vụ chia sẻ khác chạy trên `YARN` thì hiệu năng có thể giảm xuống. Điều đó có thể dẫn đến rò rỉ bộ nhớ trên `RAM`. `Hadoop` thì khác, nó dễ dàng xử lý vấn đề này. **Nếu người dùng có khuynh hướng xử lý hàng loạt (`batch process`) thì `Hadoop` lại hiệu quả hơn `Spark`**.

### Security
- Bảo mật của `Spark` đang được phát triển, hiện tại nó chỉ hỗ trợ xác thực mật khẩu (`password authentication`). Ngay cả trang web chính thức của `Apache Spark` cũng tuyên bố rằng, "Có rất nhiều loại mối quan tâm bảo mật khác nhau. Spark không nhất thiết phải bảo vệ chống lại tất cả mọi thứ".
- Mặt khác, `Hadoop` trang bị toàn bộ các mức độ bảo mật như `Hadoop Authentication`, `Hadoop Authorization`, `Hadoop Auditing`, and `Hadoop Encryption`. Tất cả các tính năng này liên kết với các dự án `Hadoop` bảo mật như `Knox Gateway` và `Sentry`.
- Vậy là ở **mặt bảo mật thì `Spark` kém bảo mật hơn `Hadoop`**. 

=> **Nếu có thể tích hợp `Spark` với `Hadoop` thì `Spark` có thể "mượn" các tính năng bảo mật của `Hadoop`**.

### Fee
Trước tiên, cả `Spark` và `Hadoop` đều là các `framework` mã nguồn mở (`open source`), nghĩa là nó miễn phí. Cả hai đều sử dụng các `server` chung, chạy trên `cloud`, và dường như chúng sử dụng các cầu hình phần cứng tương tự nhau.

| |`Apache Hadoop` | `Apache Spark`|
|-|-|-|
|CORE|4|8-16|
|Memmory|24 GB | 8 GB to hundreds of GB |
|DISKS| 4-6 one TB disk | 4-8 |
|Network|1 GB Ethernet all-to-all | 10 GB or more|

- `Spark` cần một lượng lớn `RAM` vì nó xử lý mọi thứ ở bộ nhớ. Đây là yếu tố ảnh hưởng đến chi phí vì giá thành của `RAM` cao hơn ổ đĩa. 
- Trong khi đó `Hadoop` bị ràng buộc bởi ổ đĩa, ổ đĩa thì rẻ hơn `RAM`. Tuy nhiên `Hadoop` thì cần nhiều hệ thống hơn để phân bổ ổ đĩa `I/O`.

Do vậy, khi nhu cầu của bạn là xử lý lượng lớn dữ liệu dạng lịch sử thì `Hadoop` là lựa chọn tốt vì dữ liệu dạng này cần lưu và có thể được xử lý trên ổ đĩa. Còn khi yêu cầu là xử lý dữ liệu thời gian thực thì `Spark` là lựa chọn tối ưu vì ta chỉ cần ít hệ thống cho sử lý cùng một lượng lớn dữ liệu với thời gian giảm nhiều lần hơn khi sử dụng `Hadoop`.

### Easy to use
Một trong những ưu điểm lớn nhất của Spark là tính dễ sử dụng. `Spark` có giao diện người dùng thân thiện. `Spark` cung cấp các `API` thân thiện cho `Scala` `Java`, `Python`, và `Spark SQL` (hay còn gọi là Shark). Việc `Spark` được xây dựng từ các khối đơn giản nó giúp ta tạo các hàm do người dùng xác định một cách dễ dàng.

Trong khi đó `Hadoop` được viết bằng `Java` và gay ra cho sự khó khăn trong việc viết chương trình không có chế độ tương tác. Mặc dù `Pig` (một công cụ bổ trợ) giúp lập trình dễ dàng hơn, nhưng nó cũng tốn thời gian để học cú pháp.

- Việc so sánh trên đã mang đến trong ta cảm giác `Spark` và `Hadoop` là "kẻ thù" của nhau. Vậy liệu rằng chúng có mối liên hệ kiểu hiệp lực nào không?
- Câu trả lời là có. Hệ sinh thái `Apache Hadoop` bao gồm `HDFS (Hadoop Distributed File System)`, `Apache Query`, và `HIVE`.

![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/24dc2a72-8eb4-4afe-8677-9ae3bd4316d8)

Hãy xem `Apache Spark` có thể sử dụng gì từ chúng?
### Integration Apache Spark vs HDFS
- Mục đích của `Apache Spark` là xử lý dữ liệu. Tuy nhiên, để xử lý dữ liệu, hệ thống cần dữ liệu đầu vào từ thiết bị lưu trữ. Và với mục đích này, `Spark` sử dụng `HDFS`. Đây không phải là lựa chọn duy nhất, nhưng là lựa chọn phổ biến nhất vì `Apache` là bộ não đằng sau cả hai.
### Mixture `Apache Hive` and `Apache Spark`
- `Apache Spark` và `Apache Hive` có tính tương thích cao, vì cùng nhau, chúng có thể giải quyết nhiều vấn đề của nghiệp vụ. 
- Chẳng hạn, giả sử rằng một doanh nghiệp đang phân tích hành vi của người tiêu dùng. Giờ đây, công ty sẽ cần thu thập dữ liệu từ nhiều nguồn khác nhau như mạng xã hội, bình luận, dữ liệu nhấp chuột, ứng dụng di động của khách hàng và nhiều hơn nữa. Tổ chức của bạn có thể sử dụng `HDFS` để lưu trữ dữ liệu và tổ `Apache Hive` làm cầu nối giữa `HDFS` và `Spark`.

## 2. Something must-known
### `YARN`: 
Đảm nhiệm việc quản lý tài nguyên (`resource management`) và lập kế hoạch (`job-scheduling`) /giám sát công việc (`monitoring`).
- `ResourceManager` là cơ quan có thẩm quyền cao nhất phân xử các tài nguyên giữa tất cả các ứng dụng trong hệ thống. Nó có hai thành phần: `Scheduler` và `ApplicationsManager`.
- `NodeManager` là tác nhân khung trên mỗi máy chịu trách nhiệm về `Containers`, giám sát việc sử dụng tài nguyên của chúng (cpu, bộ nhớ, đĩa, mạng) và báo cáo điều tương tự cho `ResourceManager/Scheduler`.

![Alt text](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/8bd72572-2fbc-4d76-99cd-72cbe4b5cdf2)

`ApplicationMaster` cho mỗi ứng dụng thương lượng các tài nguyên từ `ResourceManager` và làm việc với (các) `NodeManager` để thực thi và giám sát các `tasks`.
- `Scheduler` chịu trách nhiệm phân bổ tài nguyên cho các ứng dụng.
- `ApplicationsManager` chịu trách nhiệm chấp nhận các `job-submissions`, theo dõi trạng thái của chúng và theo dõi tiến độ.
  
### `Spark Core`
Đây là thành phần cốt lõi của `Apache Spark` và cung cấp các chức năng cơ bản để xử lý dữ liệu phân tán. Nó quản lý bộ nhớ, thiết lập lịch tác vụ và khôi phục lỗi.

### Spark SQL
`Spark SQL` cho phép truy vấn dữ liệu bằng ngôn ngữ `SQL` trên các tập dữ liệu lớn. Nó tích hợp với các cơ sở dữ liệu quan hệ và sử dụng tính năng phân tán của `Spark` để xử lý dữ liệu.

### Spark Streaming
Đây là một `module` cho phép xử lý dữ liệu trong thời gian thực. Spark Streaming chia nhỏ dữ liệu thành các microbatch và xử lý chúng thông qua `API` của `Spark`. Nó được sử dụng trong các ứng dụng như phân tích dữ liệu trực tuyến và giám sát hệ thống.

### Spark Mllib
Đây là thư viện `Machine Learning` tích hợp trong `Apache Spark`. `MLlib` cung cấp các thuật toán máy học phổ biến để xử lý dữ liệu lớn, bao gồm `regression`, `classification`, `clustering-segmentation`, lọc cộng tác và `dimension-reduction`.

### GraphX
`GraphX` là một `module` cho phép xử lý cấu trúc đồ thị phân tán. Nó cung cấp các cấu trúc dữ liệu như `RDD`, `VertexRDD` và `EdgeRDD` để thực hiện tính toán trên đồ thị.

### Driver Program: 
Đây là chương trình chính của `Spark Application`. Nó chạy trên một `node` trong `cluster` và quản lý quá trình xử lý trên toàn bộ `cluster`. `Driver Program` tạo và quản lý `Spark Context`.

### Spark Context: 
`Spark Context` là một đối tượng quan trọng trong `Spark`. Nó đại diện cho kết nối với một `Spark cluster` và bao gồm các chức năng cơ bản như `quản lý bộ nhớ`, `lập lịch tác vụ` và `khôi phục lỗi`.

### Cluster Manager: 
`Cluster Manager` giúp quản lý và phân phối tài nguyên trên các `node` trong `cluster`. Nó quản lý việc phân phối và giám sát quá trình xử lý trên các `node` để đảm bảo hiệu suất và độ tin cậy.

### `Executors`: 
Là các tiến trình chạy trên các `worker nodes` trong `cluster`. Chúng được quản lý bởi `driver program` để thực hiện các tác vụ xử lý dữ liệu. Mỗi `executor` có thể chứa nhiều nhiệm vụ được giao để thực hiện.

### Resilient Distributed Datasets (RDDs): 
`RDDs` là cấu trúc dữ liệu cốt lõi trong `Spark`. Chúng là tập hợp dữ liệu phân tán và bất biến có thể được xử lý song song trên nhiều node. `RDDs` được tạo trong `Spark Context`, được phân phối trên các `worker nodes` và được lưu trữ trong `bộ nhớ cache` để tăng hiệu suất.

## 3. How to optimize executor on sparks

![Alt text](https://editor.analyticsvidhya.com/uploads/79196image2.png)

Có ba thứ chính cần chú ý để định cấu hình `Spark Jobs` của bạn trên `cluster`: 
– `number of executors`, 
- `executor memory`, and
- `number of cores`. 

Mỗi `executor` là một tiến trình `JVM (Java Virtual Machine)` được khởi chạy cho ứng dụng `Sparks` trên một `node` trong khi lõi là đơn vị tính toán cơ bản của `CPU` hoặc các tác vụ đồng thời mà người thực thi có thể chạy.

Mỗi `node` có thể có nhiều `executors` và `cores`. Tất cả các tính toán đều yêu cầu một lượng bộ nhớ nhất định để hoàn thành các tác vụ này.

Bạn có thể suy nghĩ nhiều hơn về số lượng `cores` mà bạn có nhiều `nhiệm vụ đồng thời (concurrent tasks)` hơn mà bạn có thể thực hiện tại một thời điểm nhất định. Mặc dù hệ tư tưởng này hoạt động nhưng có một hạn chế đối với nó.

- Người ta quan sát thấy rằng nhiều ứng dụng spark có **hơn 5 tác vụ đồng thời là chưa tối ưu và hoạt động kém**. Con số này đến từ khả năng của `executor` chứ không phải từ số lượng `cores` của hệ thống.
- Vì vậy, con số $5$ vẫn giữ nguyên ngay cả khi bạn có nhiều lõi hơn trong máy của mình. Vì vậy, đặt giá trị này thành $5$ để có thông lượng `HDFS` tốt (bằng cách đặt `lõi thực thi` là $5$ trong khi gửi `ứng dụng Spark`) là một ý tưởng hay.

>> $\diamond$ Khi bạn chạy các ứng dụng spark bằng `Cluster Manager`, sẽ có một số trình nền `Hadoop` chạy trong nền như `name node`, `data node`, `trình theo dõi công việc (job tracker)` và `trình theo dõi tác vụ (task tracker)` (tất cả chúng đều có một công việc cụ thể để thực hiện mà bạn nên đọc). Vì vậy, trong khi chỉ định `num-executors`, bạn cần đảm bảo rằng bạn dành đủ số `core` (`~1` lõi cho mỗi `node`) để các daemon này chạy **smoothly**.

>> $\diamond$ Ngoài ra, bạn sẽ phải để lại ít nhất `executor` cho `Application Manager` để điều phối nguồn tài nguyên từ `Resource Manager`. Bạn cũng sẽ phải chỉ định một số bộ nhớ thực thi để bù đắp cho bộ nhớ trên cho một số tác vụ linh tinh khác. Tài liệu cho thấy việc gán nó cho khoảng `7-10%` bộ nhớ thực thi là một lựa chọn tốt tuy nhiên không nên quá thấp.

>>>> Ví dụ: giả sử bạn đang làm việc trên một `10 nodes cluster` với `16 cores per node` và `64 GB RAM trên mỗi node`. Bạn có thể chỉ định `5 cores cho mỗi executor` và để lại `1 core cho mỗi node` cho các trình nền `Hadoop`. Vì vậy, bây giờ bạn có `15 là số cores có sẵn trên mỗi node`. Vì bạn có `10 node` nên `tổng số cores` có sẵn sẽ là `10×15 = 150`.

>>>> Lúc này 

                    Số executors có sẵn = (tổng số cores)/ (cores per executor) = 150 / 5 = 30, 
            
>>>>  nhưng bạn sẽ phải để lại `ít nhất 1 executor` cho `Application Manager` do đó `số executors sẽ là 29`.

>>>> Nhưng vì ta có `10 nodes`, do đó `3 (30/10) executors cho mỗi node`.

>>>> Vậy `memory cho mỗi executor` will be `memory per node/executors per node = 64 / 3 around 21GB`. 

>>>> Loại bỏ thêm `7% (~3 GB) as memory overhead`, ta được `18 (21-3) GB per executor as memory`, do đó:

                        executor-cores 5, –num-executors 29, –executor-memory 18 GB.

Like this, you can work out the math for assigning `these parameters`. Although do note that this is just one of the ways to assign these parameters, it may happen that your job may get tuned at different values but the important point to note here is to have a structured way to think about tuning these values rather than shooting in the dark.

### Avoid Long Lineage
`Spark` cung cấp hai loại hoạt động: `Actions` and `Transformations`.
- `Transformations` (eg. `map`, `filter`, `groupBy`, etc.) xây dựng một `new RDD/DataFrame` từ cái trước đó, trong khi đó
- `Actions` (e.g. `head`, `show`, `write`, etc.) tính toán kết quả dựa trên `RDD/DataFrame` và trả kết quả đó về chương trình trình điều khiển hoặc lưu nó vào hệ thống lưu trữ bên ngoài. `Spark` thực hiện tất cả các thao tác này một cách lười biếng.

`Lazy evaluation` in `spark` có nghĩa là việc thực thi thực tế không xảy ra cho đến khi một hành động được kích hoạt (`triggered`). Mọi lệnh `transform` chạy trên `Spark` `DataFrame` hoặc `RDD` đều được lưu trữ vào `lineage graph`.

Không nên xâu chuỗi nhiều phép biến đổi trong một dòng, đặc biệt khi bạn muốn xử lý khối lượng dữ liệu khổng lồ với tài nguyên tối thiểu. Thay vào đó, hãy phá vỡ dòng bằng cách ghi các kết quả trung gian vào `HDFS` (tốt nhất là ở HDFS chứ không phải ở bộ nhớ ngoài như `S3` vì việc ghi vào bộ nhớ ngoài có thể chậm hơn).

### Broadcasting 
Khi một biến cần được chia sẻ giữa những người thực thi trong `Spark`, biến đó có thể được khai báo là biến phát sóng. Lưu ý rằng các biến phát sóng có bản chất chỉ đọc. `Broadcast variables (các biến phát sóng)` đặc biệt hữu ích trong trường hợp các kết nối bị lệch. 

Ví dụ: nếu bạn đang cố gắng nối hai `tables`, một trong số đó rất nhỏ và bảng kia rất lớn, thì việc phát bảng nhỏ hơn qua các trình thực thi của `workers nodes` để tránh `network overhead` là điều hợp lý.

![Alt text](https://editor.analyticsvidhya.com/uploads/86120image3.png)


### Partitioning your DataSet
Mặc dù `Spark` chọn các giá trị mặc định hợp lý và hợp lý cho dữ liệu của bạn, nhưng nếu `Spark job` của bạn hết bộ nhớ hoặc chạy chậm thì có thể có lỗi do phân vùng kém.

Nếu tập dữ liệu của bạn lớn, bạn có thể thử `phân vùng lại (repartitioning)` thành số lượng lớn hơn để cho phép thực hiện song song hơn trong công việc của bạn.
- Một dấu hiệu rõ ràng cho điều này là nếu trong `Spark UI` bạn không có nhiều `tasks` nhưng mỗi `task` lại hoàn thành rất chậm.
- Mặt khác, nếu bạn không có nhiều dữ liệu và có rất nhiều phân vùng thì việc có quá nhiều phân vùng cũng có thể khiến `job` của bạn bị chậm. Bạn có thể phân vùng lại thành một số nhỏ hơn bằng phương pháp hợp nhất thay vì phương pháp phân vùng lại vì nó nhanh hơn và sẽ cố gắng kết hợp các phân vùng trên cùng một máy thay vì xáo trộn lại dữ liệu của bạn.
  
![Alt text](https://editor.analyticsvidhya.com/uploads/70797image4.png)


### Columnar File Formats
- `Spark` sử dụng khái niệm `Predicate Push Down` để tối ưu hóa kế hoạch thực hiện của bạn.
  
>>> Ví dụ: nếu bạn xây dựng một `large Spark job` nhưng chỉ định một bộ lọc ở cuối chỉ yêu cầu chúng tôi tìm nạp một hàng từ dữ liệu nguồn của mình, thì cách hiệu quả nhất để thực hiện việc này là truy cập vào một bản ghi duy nhất mà bạn cần. `Spark` sẽ thực sự tối ưu hóa điều này cho bạn bằng cách tự động đẩy bộ lọc xuống.

- `Columnar File Formats` lưu trữ dữ liệu được phân vùng theo cả hàng và cột. Điều này làm cho việc truy cập dữ liệu nhanh hơn nhiều. Chúng tương thích hơn nhiều trong việc sử dụng hiệu quả sức mạnh của `Predicate Push Down` và được thiết kế để hoạt động với `MapReduce framework`.

>>> Một số ví dụ về `Columnar File Formats` là `Parquet`, `ORC` hoặc `Cột hàng được tối ưu hóa`, v.v.
>>> 
>>> Sử dụng `parquet format` bất cứ khi nào có thể để đọc và ghi tệp vào `HDFS` hoặc `S3`, vì nó hoạt động tốt với `Spark`.

### Use DataFrames/Datasets instead of RDDs :
`Bộ dữ liệu phân tán linh hoạt (Resilient Distributed Dataset)` hoặc `RDD` là bản tóm tắt cơ bản trong `Spark`.

- `RDD` là một cách `có khả năng chịu lỗi` để lưu trữ `unstructured data` và xử lý dữ liệu đó trong `Sparks` theo cách phân tán (`distributed manner`). Trong các phiên bản cũ hơn của `Spark`, dữ liệu nhất thiết phải được lưu trữ dưới dạng `RDD` và sau đó được xử lý, tuy nhiên, các phiên bản `Spark` mới hơn sử dụng `API DataFrame` nơi dữ liệu được lưu trữ dưới dạng `DataFrames` hoặc `Datasets`.
  
- `DataFrame` là một tập hợp dữ liệu phân tán được sắp xếp thành các cột được đặt tên, rất giống `DataFrames` trong `R/Python`. `Dataframe` nhanh hơn nhiều so với `RDD` vì nó có `metadata` (một số thông tin về dữ liệu) được liên kết với nó, điều này cho phép `Spark` tối ưu hóa kế hoạch truy vấn của nó. Vì những người tạo ra `Spark` khuyến khích sử dụng `DataFrames` vì tối ưu hóa nội bộ nên bạn nên thử sử dụng nó thay vì `RDD`.

![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/5c1cddee-7974-4789-9be0-c9b034cbcd01)

|Features|	RDD|	Dataframe|
|-|-|-|
|Version|	Spark 1.0|	Spark 1.3|
|Representation of data|	Distributed data elements	|Data elements are organized in columns|
|Formats of data|	Structured and unstructured	|Structured and semi-structured|
|Sources of data|	Various	|Various|
|Compile-time| type safety|	Available	Unavailable|
|Optimization|	No built-in engine for optimization	| Catalyst optimizer for optimization |
|Serialization|	Use Java serialization	| Serialization occurs in memory |
|Lazy Evaluation|	Yes |	Yes |

## 4. Long table vs wide table
Xem hình minh họa sau

![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/ec616243-9368-4d56-b95d-fab46aea9622)

|Type|`wide format`| `long format` |
|-|-|-|
|Mô tả|chứa nhiều giá trị không lặp lại trên cùng một cột| chứa nhiều gia trị lặp lại trên một cột |
|Khi nào nên dùng|phân tích dữ liệu thì thông thường| tạo biểu đồ phân tích phức tạp|

## 5. Reference
- [Hadoop overview](https://colab.research.google.com/github/pnavaro/big-data/blob/master/notebooks/13-Hadoop.ipynb#scrollTo=fdGIjLjASEn1)
- [RDD vs DataFrame](https://algoscale.com/blog/apache-spark-rdd-vs-dataframe/)
