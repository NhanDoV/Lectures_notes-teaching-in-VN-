# -*- coding: utf-8 -*-
#================================= Loading historical data ====================================#
import time
import warnings
import pandas as pd
from topic_modeling import *
from datetime import datetime, timedelta

warnings.filterwarnings("ignore")
t0 = time.time()
# Input transfered to calculate
# Thay đổi từng tháng, ví dụ ngày vận hành là 20 Sep 2024 thì lookback_date = 20231001 
lookback_date = '20240101'
year, month, day = f"{1+int(lookback_date[:4])}-{lookback_date[4:6]}-{lookback_date[6:]}".split("-")

# Preparing
last_year_dt = str(int(lookback_date) - 10000)
lookback_date = datetime.strptime(lookback_date, '%Y%m%d').strftime("%Y-%m-%d")
last_year_dt = datetime.strptime(last_year_dt, '%Y%m%d').strftime("%Y-%m-%d")
next_targdate = datetime.strptime(lookback_date, '%Y-%m-%d') + timedelta(days=334)
next_targdate = next_targdate.strftime("%Y-%m-%d")

#gpt_presaved_df = pd.read_excel("temp_data/topic_byGPT.xlsx")
gpt_presaved_df = pd.read_excel("temp_data/all_logs_byGPT.xlsx")
gpt_presaved_df['date'] = pd.to_datetime(gpt_presaved_df['date'])
print(f"Historical-data \n Lastest-timestamps : {gpt_presaved_df['date'].max()} \t first-timestamps: {gpt_presaved_df['date'].min()}")
print(gpt_presaved_df.head())

#================================= Loading news-logs from stage1 ================================#
new_logs_df = pd.concat([
        pd.read_csv("temp_data/from_ios.csv"),
        pd.read_csv("temp_data/from_android.csv")
    ]).reset_index(drop=True)
new_logs_df['date'] = pd.to_datetime(new_logs_df['date'])
new_logs_df = new_logs_df[new_logs_df['date'] > gpt_presaved_df['date'].max()].sort_values(by='date').reset_index(drop=True)
print(f"Newlogs-dataset after truncated the lastest-timestamp from the historical data: \
      \n Lastest timestamps {new_logs_df['date'].max()} \t first-timestamps: {new_logs_df['date'].min()}")
print(new_logs_df.head())

#================================= INITIALIZE Azure-OpenAI ====================================#
import json
from openai import AzureOpenAI

azure_client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
)
print("Azure client has been totally connected!!")

def chat(client, message_content):
    pre_defined_message = f"""
                            Please provide the following details for each user review. The context of the story is that you are using the MyVib service.
                                1. Onboarding_issues: Lỗi đăng ký tài khoản mới trên ứng dụng mobile banking (ngân hàng di động) là tinhg huống người dùng không thể hoàn tất quá trình tạo tài khoản mới trên ứng dụng của ngân hàng, Các lỗi này có thể xảy ra do nhiều nguyên nhân như: Sai thông tin cá nhân, thông tin không khớp với hệ thống, kết nối mạng không ổn định, lỗi xác thực OTP, lỗi từ phía máy chủ, ứng dụng không tương thích, số điện thoại đã được sử dụng, quá trình xác minh danh tính gặp sự cố. Dưới đây là list các keywords:
                                    ['đăng ký, không thành công, mở mới, tên đăng nhập, online, trực tuyến, khóa, mở tài khoản online, user]
                                2. Login_issues: 'Lỗi khi đăng nhập ứng dụng Mobile Banking là tình huống người đúng không thể đăng nhập vào ứng dụng của ngân hàng. Có thể xảy ra vì nhiều lý do khác nhau như: sai thông tin đăng nhập (username và password), tài khoản bị khóa, không nhận được mã OTP, lỗi kết nối mạng, phiên bản ứng dụng lỗi, lỗi hệ thống hoặc bảo trì hệ thống, thiết bị không tương thích, lỗi bảo mật trên thiết bị, lỗi liên quan đến sinh trắc học, lỗi thời gian trên thiết bị không chính xác,... If the reviews contains one of these keywords
                                    [mật khẩu, thiết bị, đăng nhập, tên đăng nhập, đăng xuất, quên pass, lỗi login, thông tin không hợp lệ, cập nhật phiên bản, xóa app, tải lại]
                                3. UI_UX_issues: Lỗi UI/UX trên ứng dụng mobile banking là các vấn đề ảnh hưởng đến cách người dùng tương tác và trải nghiệm với ứng dụng, từ giao diện hiển thị đến sự tiện lợi khi sử dụng. keywords gồm:
                                    ['giao diện, đẹp, xấu, thân thiện, chán, không xem, ẩn, hiện, số tiền, thấy, không thể hiện, đầy đủ thông tin, lộn xộn, sử dụng, hiển thị, số tiền, bố trí, bố cục, thao tác, trải nghiệm, người dùng, thiết kế, UI, UX, khó sử dụng, font chữ to, nhỏ, kích cỡ, màu sắc, phiên bản, hình nền]
                                4. eKYC_NFC: lỗi định danh căn cước công dân, quét NFC, hoặc xác thực gương mặt hay có liên quan đến sinh trắc học
                                    [căn cước mới, thẻ căn cước, căn cước, sinh trắc học, cập nhật, chụp, CCCD, mở mới, giấy tờ cá nhân (cmnd hoặc cccd), không hợp lệ, xác thực, chính chủ, chụp hình, NFC, khuôn mặt, xác minh, rõ ràng, chip, mờ,  chụp ảnh, ảnh chụp, nhòe, không rõ, định danh, Face ID, hình ảnh]
                                5. card_issue: Lỗi về thẻ credit (thẻ tín dụng) và debit (thẻ ghi nợ) trên ứng dụng ngân hàng là những sự cố xảy ra trong quá trình quản lý, thực hiện giao dịch hoặc sử dụng thẻ qua ứng dụng di động của ngân hàng. Các lỗi này có thể liên quan đến việc kiểm tra số dư, thực hiện thanh toán, chuyển tiền, hoặc quản lý các tính năng bảo mật của thẻ. Các lỗi về thẻ thường gặp là: Lỗi kết nối thẻ, lỗi khi kiểm tra số dư, lỗi thanh toán hoặc giao dịch bị từ chối, lỗi xác thực OTP, lỗi khóa thẻ hoặc tạm ngừng thẻ không thành công, lỗi giao dịch quốc tế, lỗi tính năng hoàn tiền và trả góp, lỗi thông tin giao dịch không khớp, lỗi về phí và lãi suất thẻ tín dụng, lỗi bảo mật và gian lận thẻ,
                                    ['hủy thẻ, phí dịch vụ, phí thường niên, phí, điều kiện, hoàn tiền, thanh toán thẻ, chậm, phí trễ hạn, trễ, thẻ, rút tiền, lộ thông tin, truy thu, kích hoạt, mất tiền, lừa, trừ tiền, mở thẻ, đóng thẻ, hạn mức, dư nợ, quá hạn, điểm thưởng, trả góp, POS, ATM, credit, debit, định danh, cư trú, thẻ tín dụng, kích hoạt, nợ xấu, sao kê]
                                6. promotion_claims: Khiếu nại về khuyến mãi trên ứng dụng ngân hàng là việc khách hàng phản ánh hoặc yêu cầu giải quyết các vấn đề liên quan đến việc không nhận được khuyến mãi, ưu đãi như đã quảng bá hoặc do các sai sót trong quá trình nhận ưu đãi khi sử dụng dịch vụ trên ứng dụng ngân hàng. Những khiếu nại này có thể bao gồm các vấn đề về mã khuyến mãi, chương trình hoàn tiền, tích điểm, giảm giá, hoặc các ưu đãi dành cho chủ thẻ và khách hàng đăng ký qua ứng dụng. Các loại khiếu nại thường gặp: không nhận được ưu đãi sau khi giao dịch thành công, mãi khuyến mãi không hiệu lực, chương trình khuyến mãi không rõ ràng, gây hiểu nhầm, không được tích điểm hoặc nhận quà tặng, lỗi hệ thống dẫn đến mất quyền nhận ưu đãi, chương trình khuyến mãi hết hạn hoặc thay đổi mà không thông báo,
                                    [gọi điện, lừa đảo, ưu đãi, quảng cáo, sai sự thật, push, giảm giá, voucher, hoàn tiền, khuyến mãi]
                                7. spam_notifications: Khiếu nại về việc nhận quá nhiều thông báo trên ứng dụng ngân hàng là việc khách hàng phản ánh về tình trạng nhận được quá nhiều thông báo không cần thiết hoặc không mong muốn từ ứng dụng ngân hàng. Các thông báo này có thể là thông tin về giao dịch, quảng cáo, khuyến mãi, hoặc các tin tức khác. Việc nhận thông báo quá nhiều có thể gây phiền toái và làm gián đoạn trải nghiệm người dùng. Các tình huống liên quan đến khiếu nại về thông báo như: nhận thông báo khuyến mãi liên tục, thông báo giao dịch không cần thiết, thông báo tin tức và cập nhật dịch vụ thường xuyên, không có tùy chọn tắt hoặc quản lý thông báo, thông báo xuất hiện vào thời điểm không hợp lý. 
                                    [thông báo, push, spam, làm phiền, nhiễu]
                                8. support_call_center: Các khiếu nại về dịch vụ Call Center của ngân hàng thường liên quan đến chất lượng dịch vụ khách hàng qua điện thoại mà ngân hàng cung cấp. Những khiếu nại này có thể phản ánh sự không hài lòng về khả năng hỗ trợ, thái độ nhân viên, thời gian phản hồi, hoặc việc xử lý vấn đề của khách hàng. Những khiếu nại phổ biến liên quan đến dịch vụ Call Center của ngân hàng: Thời gian chờ quá lâu, tổng đài viên không đủ kiến thức chuyên môn, thái độ nhân viên không tốt, không giải quyết được vấn đề, chuyển máy nhiều lần, hệ thống trả lời tự động phức tạp, không hỗ trợ ngoài giờ hành chính, bị ngắt kết nối khi đang chờ, không bảo mật thông tin, không hỗ trợ ngôn ngữ khác, phí cuộc gọi cao,
                                    [chăm sóc khách hàng, nhân viên, tận tình, phục vụ, tư vấn viên, liên lạc, tổng đài, gọi, nhiệt tình, dịch vụ, cskh, hotline, thái độ, feedback, dịch vụ]
                                9. Transaction_transfer_issues: Lỗi khi chuyển tiền trên ứng dụng ngân hàng là các vấn đề phát sinh trong quá trình thực hiện giao dịch chuyển tiền từ tài khoản của khách hàng qua ứng dụng ngân hàng. Những lỗi này có thể khiến giao dịch không thành công hoặc bị trì hoãn, ảnh hưởng đến trải nghiệm của khách hàng. Những lỗi phổ biến khi chuyển tiền: Lỗi kết nối mạng, lỗi hệ thống ngân hàng, lỗi nhập sai thông tin người nhận, tài khoản người nhận không hợp lệ, hạn mức chuyển tiền vượt quá, lỗi xác thực OTP, tài khoản không đủ số dư, lỗi bảo trì hoặc cập nhật ứng dụng,...
                                    [ck, chuyển khoản, chuyển, thông tin chuyển khoản, hiển thị, thanh toán, tra soát, chuyển đi, chuyển tiền, mã QR, người nhận, thông tin chủ tài khoản, thành công, thụ hưởng, chuyển nhanh, ngân hàng khác, hạn mức, giao dịch thất bại]
                                10. App_Bug: Bug trên ứng dụng ngân hàng là những lỗi hoặc sự cố xảy ra trong quá trình sử dụng ứng dụng ngân hàng điện tử, khiến ứng dụng hoạt động không đúng như mong đợi hoặc gây ra những kết quả không chính xác. Bug có thể ảnh hưởng đến trải nghiệm người dùng, bảo mật, hoặc tính chính xác của các dịch vụ như chuyển tiền, thanh toán, tra cứu thông tin, và các chức năng khác. Các loại bug phổ biến như: bug chức năng, bug trải nghiệm người dùng, bug bảo mật, bug hiệu suất, bug tương thích, bug kết nối,... dưới đây là các từ khóa
                                    [mã qr, không quét, gián đoạn, cập nhật, lỗi, fix, update, xóa, tải lại, gián đoạn, không xác định, bug, fix, thất bại, lag, nâng cấp, treo app không load được, load chậm,nâng cấp hệ thống, không có tài khoản nguồn, bảo trì]
                                11. OTP_issues: Lỗi OTP khi sử dụng ứng dụng ngân hàng là những sự cố liên quan đến việc nhận và sử dụng mã OTP (One-Time Password - mật khẩu một lần) để xác thực giao dịch hoặc đăng nhập trên ứng dụng ngân hàng. OTP là một yếu tố quan trọng trong quy trình bảo mật để ngăn chặn truy cập trái phép và bảo vệ tài khoản người dùng. Tuy nhiên, các lỗi liên quan đến OTP có thể gây ra sự chậm trễ hoặc thậm chí ngăn cản việc hoàn thành giao dịch. Một số lỗi OTP phổ biến là: Không nhận được mã OTP, mã OTP bị trễ hoặc hết hạn, nhập sai mã OTP, OTP bị từ chối khi xác thực giao dịch, lỗi hệ thống OTP ngân hàng, lỗi OTP khi chuyển vùng quốc tế, lỗi OTP khi thiết bị bị mất hoặc thay đổi, ...
                                    [an toàn, đảm bảo, xác thực OTP, bảo mật, thông tin, người dùng, làm phiền, moi móc, riêng tư, lộ thông tin, bán thông tin, số điện thoại lạ, lừa đảo, che tài khoản, mã otp, smart otp]
                                12. account_error: Lỗi về tài khoản trên ứng dụng ngân hàng đề cập đến các sự cố hoặc vấn đề liên quan đến tài khoản của người dùng trong ứng dụng ngân hàng điện tử. Những lỗi này có thể ảnh hưởng đến khả năng truy cập tài khoản, thực hiện giao dịch, hoặc quản lý thông tin cá nhân. Một số loại lỗi về tài khoản phổ biến: tài khoản bị khóa hoặc tạm ngưng, không nhận được thông báo giao dịch, lỗi khi liên kết tài khoản, giao dịch bị từ chối hoặc không thành công, không thể truy cập vào lịch sử giao dịch tài khoản, lỗi chuyển tiền giữa các tài khoản, ...
                                    [số dư, cập nhật, biến động, tiền gửi, tài khoản, nhận tiền, lãi, tiết kiệm, biến động số dư chậm, email thông báo phát sinh giao dịch chậm, cập nhật số dư]
                                13. payment_issues: Lỗi khi thanh toán hóa đơn hoặc nạp tiền trên ứng dụng ngân hàng là những sự cố phát sinh trong quá trình thực hiện các giao dịch thanh toán hóa đơn hoặc nạp tiền vào tài khoản ví hoặc nạp tiền điện thoại qua ứng dụng ngân hàng điện tử. Những lỗi này có thể ảnh hưởng đến khả năng thanh toán đúng hạn và tạo ra sự bất tiện cho người dùng. 
                                    [bill, hóa đơn, thanh toán, điện, nước, quét mã QR, thanh toán trực tuyến, online, Internet/ADSL, học phí]    
                                14. Tranx_claim_MyVIB: Lỗi khi tra soát giao dịch trên ứng dụng ngân hàng đề cập đến các vấn đề phát sinh trong quá trình người dùng muốn tra soát, kiểm tra các giao dịch tài chính đã thực hiện qua ứng dụng ngân hàng. Một số loại lỗi phổ biến khi tra soát giao dịch: không tìm thấy giao dịch để tra soát, thông tin giao dịch không chính xác, giao dịch bị trùng lặp, không thể tra soát giao dịch, thời gian nhận kết quả tra soát quá lâu, không nhận được kết quả tra soát, ....
                                    [không tra soát được , bị trừ tiền, không thành công, kết quả tra soát, hoàn tiền, chuyển khoản, quá hạn tra soát]
                                15. security_issues: Lỗi bảo mật đối với ứng dụng ngân hàng là những sự cố, lỗ hổng, hoặc thiếu sót trong các biện pháp bảo mật của ứng dụng ngân hàng điện tử, có thể dẫn đến việc thông tin người dùng bị rò rỉ, tài khoản bị truy cập trái phép, hoặc các giao dịch gian lận. Những lỗi bảo mật này có thể ảnh hưởng nghiêm trọng đến sự an toàn của dữ liệu tài chính và cá nhân của người dùng. Một số loại lỗi bảo mật phổ biến: Lỗ hỏng bảo mật trong mã nguồn, thiếu mã hóa dữ liệu, xác thực yếu, lỗi xác thực và phân quyền, thiếu chính sách bảo mật rõ ràng, rò rỉ dữ liệu từ bên thứ ba, bảo mật yếu trên thiết bị di động, tấn công từ phía nội bộ,...
                                    [an toàn, đảm bảo, bảo mật thông tin, người dùng, làm phiền, moi móc, riêng tư, lộ thông tin, bán thông tin, số điện thoại lạ, lừa đảo, che tài khoản]
                                16. Product issues: Khiếu nại về chính sách sản phẩm của ngân hàng thường liên quan đến các vấn đề mà khách hàng gặp phải khi sử dụng các dịch vụ và sản phẩm tài chính như vay, bảo hiểm, biểu phí, lãi suất,... 
                                    [vay, biểu phí ngân hàng, lãi suất, bảo hiểm]
                                17. received_money_issue: Lỗi khi nhận tiền về tài khoản của VIB. Lỗi khi KH claim đã ghi nhận ở ngân hàng chuyển nhưng không ghi nhận số dư tại VIB,

                                18. Undefined_topic: if the review didnt belongs to any pre-defined topics

                            The output must be in a json dictionary, for example
                            
                            EX1.text = "Giảm 50% thanh toán hóa đơn và cái nào cũng báo không tìm thấy nợ cước =))", then
                                output = {{
                                    'express_words': ['cái nào cũng báo không tìm thấy nợ cước'],
                                    'topic_found': ['payment_issues'],
                                    'negative_words': {{}},                                                                                                    
                                    'keywords_found': ['hóa đơn', 'thanh toán', 'nợ cước'],
                                    'conclusion_topic': 'payment_issues',
                                    'n_toxic_words': 0,
                                    'sentiment-score': -0.26216151
                                }}
                            EX2. text = "ngân hàng gì làm ăn như cc, chuển khoản cả chục lần rồi mà méo chuyển. hơn nữa cái app làm đéo làm lz gì suốt ngày toàn quảng cáo mấy cái nhảm nhí xàm cak. Thanh toán hóa đơn internet hoài không được, app nhảm lz"
                                output = {{
                                    'express_words': ['làm ăn như cc', 'chuển khoản cả chục lần', 'méo chuyển', 'làm đéo làm lz gì suốt ngày toàn quảng cáo mấy cái nhảm nhí xàm cak', 'app nhảm lz'],
                                    'topic_found': ['Transaction_transfer_issues', 'payment_issues', 'promotion_claims'],
                                    'negative_words': {{
                                            'promotion_claims': [đéo, lz, nhảm nhí, xàm cak],
                                            'payment_issues': [nhảm loz],
                                            'Transaction_transfer_issues': [như cc, méo chuyển]
                                        }},                                                                              
                                    'keywords_found': ['chuyển khoản', 'méo chuyển', 'quảng cáo', 'thanh toán', 'hóa đơn internet'],
                                    'conclusion_topic': 'promotion_claims',
                                    'n_toxic_words': 7,
                                    'sentiment-score': -0.9851441189
                                }}
                            ......................................................................
                            Explaination the conclusion_topic at EX2
                                câu trên đề cập đến nhiều topic nhưng
                                    * promotion_claims chỉ gồm đoạn 'hơn nữa cái app làm đéo làm lz gì suốt ngày toàn quảng cáo mấy cái nhảm nhí xàm cak' có độ dài gồm 20 chữ với 4 từ chửi tục hay negative words (đéo, lz, nhảm nhí, xàm cak)
                                    * payment_issues là đoạn cuối 'Thanh toán hóa đơn internet hoài không được, app nhảm lz' với độ dài 11 và chỉ có 1 từ chửi tục (nhảm loz)
                                    * Transaction_transfer_issues là đoạn đầu tiên 'ngân hàng gì làm ăn như cc, chuển khoản cả chục lần rồi mà méo chuyển' với độ dài 16 và chỉ có 2 negative words (như cc, méo chuyển)
                                sentiment-score nằm trong khoảng (-1, 1) và nên là một số thực, tùy thuộc vào số từ negative tìm được và độ dài câu review mà ta sẽ đánh giá chỉ số này 
                            ...................................................................
                            Dont print out the explaination
                            EX 3. text = "OK" or "Ok", then
                                {{
                                    'express_words' : [],
                                    'topic_found': [],
                                    'negative_words': {{}},
                                    'keywords_found': [],
                                    'conclusion_topic': 'These reviews are positive',
                                    'n_toxic_words': 0,
                                    'sentiment-score': 0.7
                                }}
                            EX 4. text = "Good", then
                                {{
                                    'express_words' : [],
                                    'topic_found': [],
                                    'negative_words': {{}},
                                    'keywords_found': [],
                                    'conclusion_topic': 'These reviews are positive',
                                    'n_toxic_words': 0,
                                    'sentiment-score': 0.8
                                }}
                            EX 5. text = "Excellent" or "Great", then
                                {{
                                    'express_words' : [],
                                    'topic_found': [],
                                    'negative_words': {{}},
                                    'keywords_found': [],
                                    'conclusion_topic': 'These reviews are positive',
                                    'n_toxic_words': 0,
                                    'sentiment-score': 0.9
                                }}
                            EX 6, text = "Cài về vào đăng ký thì ko gửi mã ko hiểu kiểu gì", then
                                {{
                                    'express_words' : ['ko gửi mã', 'ko hiểu kiểu gì'],
                                    'topic_found': ['Onboarding_issues', 'OTP_issues],
                                    'negative_words': {{}},
                                    'keywords_found': ['đăng ký', 'cài về', 'gửi mã'],
                                    'conclusion_topic': 'OTP_issues',
                                    'n_toxic_words': 0,
                                    'sentiment-score': -0.1                                    
                                }}                  
                            Trong EX 6, tuy có 2 topic_found với trọng số như nhau thì lúc này dựa trên semantic, ta sẽ đưa nó vào nhóm "OTP_issues"
                            .........
                            EX 7, text = "Trải nghiệm quá tệ, xác thực cccd mãi chẳng được, muốn lấy lại cái Mã chuyển tiền mà báo lỗi Otp suốt, nói chung ngân hàng này không mạnh về chuyển đổi số", then
                            {{
                                'express_words': ['trải nghiệm quá tệ', 'xác thực cccd mãi chẳng được', 'muốn lấy lại cái Mã chuyển tiền mà báo lỗi Otp suốt', 
                                                'ngân hàng này không mạnh về chuyển đổi số'], 
                                'topic_found': ['eKYC_NFC', 'OTP_issues', 'Transaction_transfer_issues'], 
                                'negative_words': {{'eKYC_NFC': ['trải nghiệm quá tệ', 'xác thực cccd mãi chẳng được'], 
                                                    'OTP_issues': ['báo lỗi Otp suốt'], 
                                                    'Transaction_transfer_issues': ['không mạnh về chuyển đổi số']}}, 
                                'keywords_found': ['xác thực', 'cccd', 'mã chuyển tiền', 'Otp'], 
                                'conclusion_topic': 'eKYC_NFC', 
                                'n_toxic_words': 3, 
                                'sentiment-score': -0.6
                            }}
                            EX 8. text = "Trải nghiệm tòi tệ cho dịch vụ của NN", then
                                {{
                                    'conclusion_topic': 'Undefined_topic',
                                    'express_words': ['trải nghiệm tòi tệ'],
                                    'keywords_found': ['trải nghiệm'],
                                    'n_toxic_words': 1,
                                    'negative_words': {{'Undefined_topic': ['trải nghiệm tòi tệ']}},
                                    'sentiment-score': -0.5,
                                    'topic_found': ['Undefined_topic']
                                }}
                            ...............
                            Giải thích cho EX 8, các review mang tính chất chung chung, không rõ ràng hoặc không đề cập và không liên quan đến một trong các chủ đề khác sẽ được gán là Undefined_topic. UI_UX không liên quan trong trường hợp này
                            ..................................................................
                            Cuối cùng, lưu ý rằng tất cả các giá trị về key trong output bắt buộc phải có, value có thể để là 0 hoặc empty
                            .................................................................
                            Now, you will get the user-review                                           
                            {message_content}
                            """

    response = client.chat.completions.create(
        model="intbot-prod-gpt-4o",
        messages=[{"role":"system","content": pre_defined_message}, 
                  {"role":"user","content":"---\nYOUR_QUESTION\nOutput:\n"}],
        temperature=0.2,
        max_tokens=512,
        top_p=0.9,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    json_string =  response.choices[0].message.content.replace('\n"','"').replace('\n}','}')
    cleaned_json_string = json_string.replace('```json\n', '').replace('```', '')

    return json.loads(cleaned_json_string)

#================================= Append new detected-terms ====================================#
print("Appended new-logs finished sucessfully!!!")
new_logs_df.to_excel("temp_data/new_logs_by_GPT.xlsx", index=False)
print("New-logs by chatgpt has been writen successfully !!!")

import ast
import pprint
pp = pprint.PrettyPrinter(indent=4)

all_logs = pd.concat([gpt_presaved_df, new_logs_df]).reset_index(drop=True)
redindexes = all_logs[(all_logs['date'] >= '2024-12-01') & (all_logs['rating'] <= 3)].index
for idx in redindexes:    
    inp_txt = all_logs.loc[idx, 'review']
    perc = 100 * (idx + 1) / len(redindexes)
    print(f"Process-to {perc:.2f}% \t date: {all_logs.loc[idx, 'date']} \t input: {inp_txt} ")
    try:
        res_dict = chat(azure_client, inp_txt.replace('\n', ''))
        print(f"output: {res_dict} \n conclusion_topic: {res_dict['conclusion_topic']} \t sentiment-score: {res_dict['sentiment-score']}")        
        all_logs.loc[idx, 'all_logs'] = pp.pformat(ast.literal_eval(str(res_dict)))
        all_logs.loc[idx, 'negative_words'] = pp.pformat(ast.literal_eval(str(res_dict['negative_words'])))
        all_logs.loc[idx, 'n_toxic_words'] = res_dict['n_toxic_words']
        all_logs.loc[idx, 'conclusion_topic'] = res_dict['conclusion_topic']
        all_logs.loc[idx, 'sentiment-score'] = res_dict['sentiment-score']
        all_logs.loc[idx, 'keywords_found'] = str(res_dict['keywords_found'])
        all_logs.loc[idx, 'topic_found'] = str(res_dict['topic_found'])
    except:
        print(f"{idx}: \t {inp_txt}")
    print(69*"=")

all_logs.loc[(all_logs['rating'] <= 3) 
             & (all_logs['conclusion_topic'] == 'These reviews are positive'), 
            'conclusion_topic'
            ] = 'Undefined_topic'
        
all_logs['conclusion_topic'] = all_logs['conclusion_topic'].replace({
    'Product issues' : 'Product_issues',
    'login_issues': 'Login_issues',
    'onboarding_issues': 'Onboarding_issues'
})

all_logs['date'] = pd.to_datetime(all_logs['date'])
col_list = ['date', 'review', 'conclusion_topic', 'rating', 'n_toxic_words', 'platform']

ios_rate_12m = all_logs.loc[(all_logs['date'] > '2024-12-01') & (all_logs['platform'] == 'ios'), 'rating'].mean().round(3)
adr_rate_12m = all_logs.loc[(all_logs['date'] > '2024-12-01') & (all_logs['platform'] == 'android'), 'rating'].mean().round(3)
adr_rate_all = all_logs.loc[all_logs['platform'] == 'android', 'rating'].mean().round(3)
ios_rate_all = all_logs.loc[all_logs['platform'] == 'ios', 'rating'].mean().round(3)
n_ios = len(all_logs[all_logs['platform'] == 'ios'])
n_adr = len(all_logs[all_logs['platform'] == 'android'])

print(f"""
    iOS: 
        avg_rate_12m: {ios_rate_12m} \t avg_rate_all-time: {ios_rate_all}, \t n_reviews: {n_ios}
    Android
        avg_rate_12m: {adr_rate_12m} \t avg_rate_all-time: {adr_rate_all}, \t n_reviews: {n_adr}
    """
)

def fill_missed_topic(df):
    
    # Tạo các DataFrame con cho 'this-year' và 'this-month'
    df_year = df[df['type'] == 'this-year']
    df_month = df[df['type'] == 'this-month']

    # Tìm các topic có trong 'this-year' nhưng thiếu trong 'this-month'
    topics_year = set(df_year['conclusion_topic'])
    topics_month = set(df_month['conclusion_topic'])

    missing_topics = topics_year - topics_month

    # Tạo DataFrame mới cho các dòng thiếu
    missing_rows = df_year[df_year['conclusion_topic'].isin(missing_topics)]
    missing_rows['type'] = 'this-month'

    # Đặt giá trị cho các cột khác là 0 trong các dòng mới
    missing_rows = missing_rows.copy()
    missing_rows[['review', 'text_length', 'n_toxic_words']] = 0

    # Gộp DataFrame hiện tại với các dòng thiếu
    df_combined = pd.concat([df, missing_rows], ignore_index=True)

    # Tạo cột phụ để sắp xếp theo type trước
    df_combined['type_order'] = df_combined['type'].apply(lambda x: 0 if x == 'this-year' else 1)

    # Sắp xếp lại dữ liệu
    df_combined = df_combined.sort_values(by=['type_order', 'conclusion_topic'])

    # Xóa cột phụ
    df_combined = df_combined.drop(columns=['type_order'])
    
    return df_combined

path = f'temp_data/gpt_output/{year}/{month}/excel_supplement_docs/'
for idx, platf in enumerate(['android', 'ios']):
    df_this_year = all_logs.loc[(all_logs['date'] >= lookback_date)&(all_logs['platform'] == platf), col_list]
    df_last_year = all_logs.loc[(all_logs['date'] < lookback_date) & (all_logs['date'] >= last_year_dt)&(all_logs['platform'] == platf), col_list]
    df_this_year['ym'] = df_this_year['date'].dt.strftime("%Y-%m")
    df_last_year['month'] = df_last_year['date'].dt.strftime("%m")

    df_this_year['rate_type'] = df_this_year['rating'].apply(lambda x: 'pos' if x > 3 else ('neg' if x < 3 else 'neu'))
    sheet2_df = pd.concat([pd.pivot_table(df_this_year, index='ym', columns='rate_type', values='rating', aggfunc='count'),
                        df_this_year.groupby('ym')['rating'].mean()], axis=1)
    ser = df_last_year.groupby('month')['rating'].mean()
    for ym in sheet2_df.index:
        month = ym.split("-")[1]
        sheet2_df.loc[ym, 'rating_last_year'] = ser.loc[month]
    create_folder(f'{path}/Sheet{idx+2}')
    sheet2_df.to_excel(f'{path}/Sheet{idx+2}/{platf}_barline.xlsx')
    print(sheet2_df.T)
    
for idx, platf in enumerate(['android', 'ios']):    
    all_logs['sentiment-status'] = all_logs['rating'].apply(lambda x: 'positive' if x > 3 else 'negative')
    all_logs['month_year'] = all_logs['date'].apply(lambda x: x.strftime('%Y-%m'))
    temp_ios = all_logs[(all_logs['date'] >= lookback_date)&(all_logs['platform'] == platf)]    
    ser = temp_ios[(temp_ios['date'] >= lookback_date)&(temp_ios['platform'] == platf)].groupby('month_year')['n_toxic_words'].sum()
    temp_ios = pd.pivot_table(temp_ios, index='sentiment-status', columns='month_year', values='sentiment-score', aggfunc='mean').T
    temp_ios['total_negative_words'] = ser
    temp_ios.to_excel(f'{path}/Sheet{idx+2}/{platf}_scoresline.xlsx')
    print(temp_ios.T)


titles = ['this-month', 'all-time', 'last-12-month']
data = [
    all_logs.loc[all_logs['date'] >= next_targdate, col_list],
    all_logs.loc[:, col_list],
    all_logs.loc[all_logs['date'] >= lookback_date, col_list]
]
sheet1_df = pd.DataFrame({})

for platf in ['android', 'ios']:
    for tit, df in zip(titles, data):
        temp = df.loc[df['platform'] == platf, 'rating'].value_counts().sort_index()
        sheet1_df.loc[f"{tit}_{platf}", 'note'] = tit
        #print(platf, tit, 'rate =',[int(temp.loc[idx]) for idx in range(1, 6)])
        for idx in range(1, 6):
            try:
                temp.loc[idx]
                sheet1_df.loc[f"{tit}_{platf}", f'rate={idx}'] = temp.loc[idx]
            except:
                sheet1_df.loc[f"{tit}_{platf}", f'rate={idx}'] = 0
            
sheet1_df.index = sheet1_df.index.map(lambda x: x.split("_")[-1])
sheet1_df[sheet1_df.columns[1:]] = sheet1_df[sheet1_df.columns[1:]].astype(int)
create_folder(f'{path}/Sheet1')
create_folder(f'{path}/Sheet2')
create_folder(f'{path}/Sheet3')

sheet1_df.to_excel(f'{path}/Sheet1/sheet1_smr.xlsx')
print(sheet1_df)

platf = 'android'
for idx, platf in enumerate(['android', 'ios']):
    # Filter by this-month (next-targdate) or this-year (lookback-date)
    data = [all_logs.loc[(all_logs['date'] >= lookback_date)&(all_logs['platform'] == platf), col_list],
            all_logs.loc[(all_logs['date'] >= next_targdate)&(all_logs['platform'] == platf), col_list]
            ]
    sheet2_df = pd.DataFrame({})
    for tit, df in zip(['this-year', 'this-month'], data):
        df['text_length'] = df['review'].apply(lambda x: len(x.split(" ")))
        temp = df[df['rating'] < 3]
        temp = temp.groupby(['platform', 'conclusion_topic']).agg({'review': 'count', 
                                                                   'text_length': 'mean',
                                                                   'n_toxic_words': 'mean'
                                                                }).reset_index()
        if tit == 'this-month':                
            temp['text_length'] = temp['text_length'].apply(lambda x: np.log2(x + 1))
        temp['type'] = tit
        sheet2_df = pd.concat([sheet2_df, temp]) 
    sheet2_df = fill_missed_topic(sheet2_df)
    sheet2_df.to_excel(f'{path}/Sheet{idx+2}/{platf}_radar.xlsx', index=False)
    
for idx, platf in enumerate(['android', 'ios']):
    print(f"Platform: {platf} \n {100*'-'}")
    temp = all_logs[(all_logs['date'] >= lookback_date)&(all_logs['platform'] == platf)&(all_logs['rating'] < 3)]
    print('Count (rate < 3)')
    t1 = pd.pivot_table(temp, index='conclusion_topic', columns='month_year', values='review', aggfunc='count')
    t1['note'] = 'Count (rate < 3)'
    print('Avg (rate < 3)')
    t2 = pd.pivot_table(temp, index='conclusion_topic', columns='month_year', values='rating', aggfunc='mean')
    t2['note'] = 'Avg (rate < 3)'    
    print('Avg(sentiment-score| knowing that rate < 3)')
    temp['text_length'] = temp['review'].apply(lambda x: len(x.split(" ")))
    print(temp['sentiment-score'].min())
    t3 = pd.pivot_table(temp, index='conclusion_topic', columns='month_year', values='sentiment-score', aggfunc='mean')    
    t3['note'] = 'Avg(sentiment-score| knowing that rate < 3)'
    t = pd.concat([t1, t2, t3], axis=0)
    t.to_excel(f'{path}/Sheet{idx+2}/{platf}_agg_stacked.xlsx')
    print(100*'=')
    print(t)
    
all_logs[all_logs['date'] >= '2024-08-01'].drop(columns=['bankapp', 'sentiment-status']).to_excel("temp_data/all_logs_byGPT_lastest.xlsx",index=False)
all_logs.drop(columns=['bankapp', 'sentiment-status']).to_excel("temp_data/all_logs_byGPT.xlsx",index=False)
print(f"All process finished after {(time.time() - t0):.2f} seconds !!!!!")
print("Done!!!")