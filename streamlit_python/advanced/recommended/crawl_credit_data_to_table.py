import time, re
import pandas as pd
from IPython.display import display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Using selenium
chrome_options = Options()
chrome_options.add_argument('--disable-extensions')
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://www.vib.com.vn/vn/the-tin-dung")
df_general = pd.DataFrame({})
# Loop on the card-indexes
for idx in range(1, 11):
    card_name = chrome.find_element(By.XPATH, f'//*[@id="layoutContainers"]/div/div[5]/div[1]/section/div[2]/section/div/div[{idx}]/h3/a').text
    limit_fee = chrome.find_element(By.XPATH, f'//*[@id="layoutContainers"]/div/div[5]/div[1]/section/div[2]/section/div/div[{idx}]/div/div[2]/div[2]/p[1]').text
    main_fea = chrome.find_element(By.XPATH, f'//*[@id="layoutContainers"]/div/div[5]/div[1]/section/div[2]/section/div/div[{idx}]/div/div[2]/div[1]').text
    notes = chrome.find_element(By.XPATH, f'//*[@id="layoutContainers"]/div/div[5]/div[1]/section/div[2]/section/div/div[{idx}]/div/div[1]/div[2]').text
    avg_rt = chrome.find_element(By.XPATH, f'//*[@id="layoutContainers"]/div/div[5]/div[1]/section/div[2]/section/div/div[{idx}]/div/div[1]/div[4]/div[1]/div[2]').text
    n_users = chrome.find_element(By.XPATH, f'//*[@id="layoutContainers"]/div/div[5]/div[1]/section/div[2]/section/div/div[{idx}]/div/div[1]/div[5]/p').text
    # Append dataframe
    df_general = pd.concat([df_general,
                            pd.DataFrame({
                                'card_name': [card_name],
                                'hạn mức thẻ': [limit_fee],
                                'tính năng nổi bật': [main_fea.replace('\n', ' ')],
                                'average-rate': [avg_rt[:3]],
                                'số người đánh giá': [avg_rt[4:].replace("(", "").replace(")", "")],
                                'n-users': [n_users.replace(' lượt đăng ký', '')],
                                'category': [notes]
                            })
                            ], ignore_index=True)
    
    print(card_name, '\t', limit_fee, '\t', main_fea.replace('\n', ' '), '\n', notes, '\t', avg_rt, '\t', n_users)
print(df_general)
chrome.close()
print("Get general information finished")

init_url = ["https://www.vib.com.vn/vn/the-tin-dung/vib-cashback/bieu-phi-va-dieu-kien",            # 1. VIB Cash Back
            "https://www.vib.com.vn/vn/the-tin-dung/vib-premier-boundless/bieu-phi-va-dieu-kien",   # 2. VIB Premier Boundless
            "https://www.vib.com.vn/vn/the-tin-dung/vib-travel-elite/bieu-phi-va-dieu-kien",        # 3. VIB Travel Elite
            "https://www.vib.com.vn/vn/the-tin-dung/vib-reward-unlimited/bieu-phi-va-dieu-kien",    # 4. VIB Rewards Unlimited
            "https://www.vib.com.vn/vn/the-tin-dung/vib-family-link/bieu-phi-va-dieu-kien",         # 5. VIB Family Link
            "https://www.vib.com.vn/vn/the-tin-dung/vib-financial-free/bieu-phi-va-dieu-kien",      # 6. VIB Financial Free
            "https://www.vib.com.vn/vn/the-tin-dung/vib-lazcard/bieu-phi-va-dieu-kien",             # 7. VIB LazCard 
            "https://www.vib.com.vn/vn/the-tin-dung/vib-ivycard/bieu-phi-va-dieu-kien",             # 8. VIB IvyCard 
            "https://www.vib.com.vn/vn/the-tin-dung/vib-supercard/bieu-phi-va-dieu-kien",           # 9. VIB SuperCard
            "https://www.vib.com.vn/vn/the-tin-dung/vib-online-plus-2in1/bieu-phi-va-dieu-kien"     # 10. VIB Online Plus 2in1
            ]
# Navigate to the desired URL
# for url in init_url:
#     chrome.get(url)
#     # get title
#     title = chrome.find_element(By.XPATH, '//*[@id="main-title-h1"]').text
#     tit = title.split('VIB')
#     print(f"Card: VIB {tit[1]}")
#     # Lãi suất áp dụng cho các giao dịch mua sắm
#     a = chrome.find_element(By.CLASS_NAME, 'desc table-2-colums').text
#     print(f"interest info: {a}")    
#     time.sleep(2)

# Using bs4
import requests, re
from bs4 import BeautifulSoup

pd.set_option('display.max_colwidth', 20)  # Tăng chiều rộng tối đa của cột
#pd.set_option('display.max_rows', None)     # Hiển thị tất cả các hàng
#pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột

def get_interest_info():
    
    interest_df = pd.DataFrame({})
    for url in init_url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()

        title = soup.title.string if soup.title else 'No title found'
        tit = title.split('VIB')
        print(f'Card: {tit[1]} \t response.code: {response}')
        
        # pattern để tìm kiếm các thông tin lãi suất
        matches_1 = re.findall(r'từ\s[\d\.]+%\sđến\s[\d\.]+%\/tháng', page_text.lower())
        matches_2 = re.findall(r'miễn\s+lãi\s+lên\s+đến\s+[\d]+\s+ngày', page_text.lower())
        matches_3 = re.findall(r'ngày đến hạn thanh toán của quý khách là \d+ ngày', page_text.lower())
                
        info1 = []
        info2 = []
        info3 = []        
        # In ra tất cả các kết quả
        for match1 in matches_1:
            info1.append(match1)
        for match3 in matches_3:
            info3.append(match3)
        for match2 in matches_2:
            info2.append(match2) 
        info1 = info1[:4]
        
        interest_df = pd.concat([interest_df, 
                                 pd.DataFrame({'card_name': [f"VIB{tit[1]}".split(" |")[0]],
                                               'số ngày miễn lãi': [info2[0]],
                                               'Lãi suất áp dụng cho các giao dịch mua sắm (sau khi hết miễn lãi) / tháng': [info1[0]],
                                               'Lãi suất áp dụng cho các giao dịch rút tiền': [info1[1]],
                                               'Lãi suất áp dụng cho các giao dịch rút/ứng tiền mặt qua máy POS tại chi nhánh/phòng giao dịch VIB': [info1[2]],
                                               'Lãi suất / tháng áp dụng cho các giao dịch trả góp tại Đơn vị chấp nhận thẻ bất kỳ': [info1[3]],
                                               'số ngày đến hạn thanh toán của Quý khách, tính từ sau ngày lập Bảng sao kê': [info3[0]]
                                               })], ignore_index=True)
    interest_df['card_name'] = interest_df['card_name'].replace({'VIB Financial Free I ': 'VIB Financial Free',
                                                                'VIB IvyCard': 'VIB Ivy Card',
                                                                'VIB Lazcard': 'VIB LazCard'
                                                                })
    return interest_df

def pre_processing_interest_data(interest_df):
    interest_df['số ngày miễn lãi'] = interest_df['số ngày miễn lãi'].apply(lambda x: re.search(r'miễn\s+lãi\s+lên\s+đến\s+(\d+)\s+ngày', x, re.IGNORECASE).group(1))
    interest_df['số ngày đến hạn thanh toán của Quý khách, tính từ sau ngày lập Bảng sao kê'] = interest_df['số ngày đến hạn thanh toán của Quý khách, tính từ sau ngày lập Bảng sao kê'].apply(lambda x: re.search(r'ngày\s+đến\s+hạn\s+thanh\s+toán\s+của\s+quý\s+khách\s+là\s+(\d+)\s+ngày', x, re.IGNORECASE).group(1))
    interest_df['Lãi suất tối thiểu áp dụng cho các giao dịch mua sắm (sau khi hết miễn lãi) / tháng'] = interest_df['Lãi suất áp dụng cho các giao dịch mua sắm (sau khi hết miễn lãi) / tháng'].apply(lambda x: re.findall(r'(\d+\.\d+)%', x)[0])
    interest_df['Lãi suất tối đa áp dụng cho các giao dịch mua sắm (sau khi hết miễn lãi) / tháng'] = interest_df['Lãi suất áp dụng cho các giao dịch mua sắm (sau khi hết miễn lãi) / tháng'].apply(lambda x: re.findall(r'(\d+\.\d+)%', x)[1])
    interest_df['Lãi suất tối thiểu áp dụng cho các giao dịch rút tiền'] = interest_df['Lãi suất áp dụng cho các giao dịch rút tiền'].apply(lambda x: re.findall(r'(\d+\.\d+)%', x)[0])
    interest_df['Lãi suất tối đa áp dụng cho các giao dịch rút tiền'] = interest_df['Lãi suất áp dụng cho các giao dịch rút tiền'].apply(lambda x: re.findall(r'(\d+\.\d+)%', x)[1])
    interest_df['Lãi suất tối thiểu áp dụng cho các giao dịch rút/ứng tiền mặt qua máy POS tại chi nhánh/phòng giao dịch VIB'] = interest_df['Lãi suất áp dụng cho các giao dịch rút/ứng tiền mặt qua máy POS tại chi nhánh/phòng giao dịch VIB'].apply(lambda x: re.findall(r'(\d+\.\d+)%', x)[0])
    interest_df['Lãi suất tối đa áp dụng cho các giao dịch rút/ứng tiền mặt qua máy POS tại chi nhánh/phòng giao dịch VIB'] = interest_df['Lãi suất áp dụng cho các giao dịch rút/ứng tiền mặt qua máy POS tại chi nhánh/phòng giao dịch VIB'].apply(lambda x: re.findall(r'(\d+(\.\d+)?)%', x)[-1][0])
    interest_df['Lãi suất tối thiểu / tháng áp dụng cho các giao dịch trả góp tại Đơn vị chấp nhận thẻ bất kỳ'] = interest_df['Lãi suất / tháng áp dụng cho các giao dịch trả góp tại Đơn vị chấp nhận thẻ bất kỳ'].apply(lambda x: re.findall(r'(\d+\.\d+)%', x)[0])
    interest_df['Lãi suất tối đa / tháng áp dụng cho các giao dịch trả góp tại Đơn vị chấp nhận thẻ bất kỳ'] = interest_df['Lãi suất / tháng áp dụng cho các giao dịch trả góp tại Đơn vị chấp nhận thẻ bất kỳ'].apply(lambda x: re.findall(r'(\d+(\.\d+)?)%', x)[-1][0])
                    
    return interest_df.drop(columns=['Lãi suất áp dụng cho các giao dịch mua sắm (sau khi hết miễn lãi) / tháng', 
                                     'Lãi suất áp dụng cho các giao dịch rút tiền',
                                     'Lãi suất áp dụng cho các giao dịch rút/ứng tiền mặt qua máy POS tại chi nhánh/phòng giao dịch VIB',
                                     'Lãi suất / tháng áp dụng cho các giao dịch trả góp tại Đơn vị chấp nhận thẻ bất kỳ'
                                     ])

interest_df = get_interest_info()
interest_df = pre_processing_interest_data(interest_df)
display(interest_df)

def get_fees_info():
    
    fees_df = pd.DataFrame({})
    for idx, url in enumerate(init_url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()

        title = soup.title.string if soup.title else 'No title found'
        tit = title.split('VIB')
        print(f'Card: {tit[1]} \t response.code: {response}')

        # Patterns để tìm kiếm thông tin các khoản phí 
        matches_1 = re.findall(r'(\d{1,3}(\.\d{3})*) VNĐ/thẻ/thiết kế (tiêu chuẩn|đặc biệt)', page_text)
        matches_2 = page_text.split('Phí đóng thẻ')[1].split('Phí rút tiền dư có từ Thẻ tín dụng')[0].replace('\n', ' ')
        
        if idx != 6:
            main_fee = None
            sub_fee = ""
        # nếu là LazCard
        else:
            main_fee = "599.000 VNĐ "
            sub_fee = "299.000 VNĐ "
        try:
            rows = page_text.split('Phí thường niên thẻ chính')[1].split('Phí ứng/rút tiền mặt')[0].replace('\n', ' ')
            rows = f"Phí thường niên thẻ chính: {rows}"
            main_fee = rows.split('Phí thường niên thẻ phụ')[0]
            sub_fee = f"{rows.split('Phí thường niên thẻ phụ')[1]}"
            c = (main_fee, sub_fee)
        except:
            main_fee = main_fee if main_fee != None else ""
            sub_fee = sub_fee if sub_fee != None else ""
            c = (main_fee, sub_fee)
            
        del main_fee, sub_fee        
        info1 = []
        if len(matches_1) == 0:
            info1.append(('null', 'null'))
        else:
            for match1 in matches_1:
                info1.append(match1)   
        
        fees_df = pd.concat([fees_df, 
                             pd.DataFrame({'card_name': [f"VIB{tit[1]}".split(" |")[0]],
                                        'Phí phát hành (áp dụng thiết kế hình ảnh in trên thẻ tiêu chuẩn)': [info1[0][0] if info1[0][0] != 'null' else 'null'],
                                        'Phí phát hành (áp dụng thiết kế hình ảnh in trên thẻ đặc biệt)': [info1[1][0] if len(info1) > 1 and info1[1][0] != 'null' else 'null'],
                                        'Phí thường niên thẻ chính': c[0].replace('Phí thường niên thẻ chính: ', ''),
                                        'Phí thường niên thẻ phụ': c[1],
                                        'phí đóng thẻ': [re.search(r'(\d{1,3}(?:\.\d{3})*)\s*(VNĐ)', matches_2).group(0)]
                            })], ignore_index=True)
    
    fees_df['miễn phí thường niên năm đầu (thẻ chính)'] = fees_df['Phí thường niên thẻ chính'].apply(lambda x: True if ' Năm đầu tiên: 0 ' in x else False)
    fees_df['miễn phí thường niên năm đầu (thẻ phụ)'] = fees_df['Phí thường niên thẻ phụ'].apply(lambda x: True if ' Năm đầu tiên: 0 ' in x else False)
    fees_df['Thẻ chính miễn phí nếu phát sinh tổng giao dịch thanh toán tại POS/Internet đạt tối thiểu 12 triệu trong năm liền trước'] = fees_df['Phí thường niên thẻ chính'].apply(lambda x: True if ' Miễn phí nếu phát sinh tổng giao dịch thanh toán tại POS/Internet đạt tối thiểu 12 triệu trong năm liền trước' in x else False)
    fees_df['Thẻ phụ miễn phí nếu phát sinh tổng giao dịch thanh toán tại POS/Internet đạt tối thiểu 12 triệu trong năm liền trước'] = fees_df['Phí thường niên thẻ phụ'].apply(lambda x: True if ' Miễn phí nếu phát sinh tổng giao dịch thanh toán tại POS/Internet đạt tối thiểu 12 triệu trong năm liền trước' in x else False)    
    fees_df['Phí thường niên thẻ chính (phát hành trước 27/04/2024)']
    fees_df['Phí thường niên thẻ chính'] = fees_df['Phí thường niên thẻ chính'].apply(lambda x: x.replace(' Năm đầu tiên: 0 			Các năm tiếp theo: ', '').replace('VNĐ 			Miễn phí nếu phát sinh tổng giao dịch thanh toán tại POS/Internet đạt tối thiểu 12 triệu trong năm liền trước (giao dịch đã ghi nhận vào sao kê)   ', ''))
    fees_df['Phí thường niên thẻ phụ'] = fees_df['Phí thường niên thẻ phụ'].apply(lambda x: x.replace(' Năm đầu tiên: 0 			Các năm tiếp theo: ', '').replace('VNĐ 			Miễn phí nếu phát sinh tổng giao dịch thanh toán tại POS/Internet đạt tối thiểu 12 triệu trong năm liền trước (giao dịch đã ghi nhận vào sao kê)   ', ''))    
    fees_df['card_name'] = fees_df['card_name'].replace({'VIB Financial Free I ': 'VIB Financial Free',
                                                        'VIB IvyCard': 'VIB Ivy Card',
                                                        'VIB Lazcard': 'VIB LazCard'
                                                        })
        
    return fees_df
        
fees_df = get_fees_info()
display(fees_df)

def get_eligibility_info():
    
    elig_df = pd.DataFrame({})
    for idx, url in enumerate(init_url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()

        title = soup.title.string if soup.title else 'No title found'
        tit = title.split('VIB')
        print(f'Card: {tit[1]} \t response.code: {response}')

        # find conditions
        age_text = page_text.lower().split("độ tuổi")[1].split("các yêu cầu khác")[0]
        
        elig_df = pd.concat([elig_df, 
                             pd.DataFrame({'card_name': [f"VIB{tit[1]}".split(" |")[0]],
                                           'all-text': [age_text.lower()],
                            })], ignore_index=True)
        
    elig_df['card_name'] = elig_df['card_name'].replace({'VIB Financial Free I ': 'VIB Financial Free',
                                                        'VIB IvyCard': 'VIB Ivy Card',
                                                        'VIB Lazcard': 'VIB LazCard'
                                                        })
            
    return elig_df

def pre_processingeligibility_data(elig_df):
    elig_df['độ tuổi'] = elig_df['all-text'].apply(lambda x: x.split("thu nhập")[0])
    elig_df['tín dụng'] = elig_df['all-text'].apply(lambda x: x.split("lịch sử tín dụng")[1].replace('\n', ' '))
    elig_df['thu nhập'] = elig_df.apply(lambda r: r['all-text'].replace(r['độ tuổi'], '').replace(r['tín dụng'], '').replace('thu nhập\n', ''), axis=1)
    elig_df = elig_df.drop(columns=['all-text'])
    print("Step 1. extract column from web finished")
    print(elig_df)
    elig_df['độ tuổi (chủ thẻ chính)'] = elig_df['độ tuổi'].apply(lambda x: x.split("\n")[1].replace('chủ thẻ chính: ', ''))
    elig_df['độ tuổi (chủ thẻ phụ)'] = elig_df['độ tuổi'].apply(lambda x: x.split("\n")[2].replace('chủ thẻ phụ: ', '').replace('\t', ''))
    elig_df['tín dụng (số năm không nợ xấu)'] = elig_df['tín dụng'].apply(lambda x: re.search(r"\d{1,2}", x).group(0))
    elig_df['tín dụng (số năm không nợ xấu)'] = elig_df['tín dụng (số năm không nợ xấu)'].apply(lambda x: x.replace('0', ''))
    elig_df['thu nhập trung bình tối thiểu 3 tháng gần nhất'] = elig_df['thu nhập'].fillna("").apply(lambda x: re.search(r"\d{1,2}", x.replace("3", "")).group(0) if x != "" else "")    
    elig_df['thu nhập trung bình tối thiểu 3 tháng gần nhất'] = elig_df['thu nhập trung bình tối thiểu 3 tháng gần nhất'].apply(lambda x: f"{x}000000" if x != "" else "")
    elig_df = elig_df.drop(columns=['độ tuổi', 'tín dụng', 'thu nhập'])
    print("Step 2. finished")
    return elig_df
      
elig_df = get_eligibility_info()
elig_df = pre_processingeligibility_data(elig_df)
display(elig_df)

def merging_dataframe():
    print("Thông tin chung", df_general.shape)
    print("Lãi suất", interest_df.shape)
    print("Các phí", fees_df.shape)    
    print("Điều kiện", elig_df.shape)    
    final_df = df_general.merge(interest_df, on = 'card_name', how='left')
    print("1")
    display(final_df)
    print("2")
    final_df = final_df.merge(fees_df, on="card_name", how="left")
    display(final_df)    
    final_df = final_df.merge(elig_df, on = 'card_name', how='left')
    print("3")
    final_df['hạn mức thẻ'] = final_df['hạn mức thẻ'].apply(lambda x: x.replace('Hạn mức lên đến ', ' ').replace(' đồng', '')
                                                            .replace(' triệu', '000000').replace(' tỷ', '000000000'))
    final_df['tính năng nổi bật'] = final_df['tính năng nổi bật'].apply(lambda x: x.lower().replace('tính năng nổi bật ', ''))
    final_df.to_excel("all_credit_cards.xlsx", index=False)
    display(final_df)
    
merging_dataframe()