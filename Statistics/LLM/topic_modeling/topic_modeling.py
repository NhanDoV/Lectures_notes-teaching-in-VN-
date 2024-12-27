# -*- coding: utf-8 -*-
# 1. Import basic libraries
import os
import pandas as pd
import numpy as np

# 2. Libraries supported to Topic-Segmented
import re, string
from datetime import date, datetime, timedelta

# 3. Basic visualization
import matplotlib.pyplot as plt
from IPython.display import display

# 5. Using in web-scraping
from google_play_scraper import Sort, reviews, app, reviews_all
from app_store_scraper import AppStore

# Android ===============================
def get_rwdata_android(rw_android_src_dict, bank_name):
    """Get raw data from android
    Args:
        rw_ios_src_dict (dict): dictionary of bank-info' (for e.g. {tcb2':['com.vib.mytcb2','vi','vn']})
        bankapp (str): name of app's banking (e.g. tpb2, vib2, tcb2)
    Returns:
        df: datafram of client's reviews / comments
    """
    Andreviews = reviews_all(
        rw_android_src_dict[bank_name][0],
        #'vn.com.techcombank.bb.app',
        sleep_milliseconds=0, # defaults to 0
        lang=rw_android_src_dict[bank_name][1], # defaults to 'en'
        country=rw_android_src_dict[bank_name][2], # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
    )
         
    Andreviews_df = pd.DataFrame(Andreviews) # Andreviews_df.to_csv('AndRaw_'+bank_name+'_'+str(today)+'.csv', index=False)
    print(f'{bank_name}: {Andreviews_df.shape}')
    return Andreviews_df
 
def save_rawdata(type_p = 'android'):
    """Save the rawdata with respect to Android of iOS
    Args:
        type_p (str, optional): platform type to crawl. Defaults to 'android'
    Returns:
        _type_: _description_
    """
    import time
    
    type_p = type_p.lower()
    bank_array = ['tcb2']
    if type_p == 'android':
        rw_android_src_dict = {
                       'tcb2':['com.vib.mytcb2','vi','vn']
                       }        
        # get Android review
        column = ['reviewId','userName','userImage','content','score','thumbsUpCount','reviewCreatedVersion',
                  'at','replyContent','repliedAt','bankapp','platform']
        rawdf = pd.DataFrame(columns = column)
        get_review_in = bank_array
        for bank_name in get_review_in:
            Andrw_df = get_rwdata_android(rw_android_src_dict, bank_name)   
            Andrw_df['bankapp'] = bank_name
            Andrw_df['platform'] = 'android'
            rawdf = pd.concat([rawdf, Andrw_df])
            time.sleep(2)
        df_android_used = rawdf[['userName','content','at','score','bankapp','platform']]
        df_android_used.rename(columns = {'userName':'username','content':'review','at':'date','score':'rating'}, inplace=True)

        # Convert timetamps to string
        df_android_used['date'] = df_android_used['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))
        df_android_used.to_csv("customer_segmentation/notebook_preprocessing/data/from_android.csv", index=False)
        
    else:
        pass

    print("Your data has been crawled successfully!!!")
    
# iOS =================================
def get_rwdata_ios(rw_ios_src_dict, bankapp):
    """Get raw data from iOS
    Args:
        rw_ios_src_dict (dict): dictionary of bank-info' (for e.g. {'vib2':['MyVIB 2.0','vn','1626624790']})
        bankapp (str): name of app's banking (e.g. vib2)
    Returns:
        df: datafram of client's reviews / comments
    """
    appStore = AppStore(country=rw_ios_src_dict[bankapp][1], app_name=rw_ios_src_dict[bankapp][0], 
                        app_id=int(rw_ios_src_dict[bankapp][2])) #Techcombank Mobile
    print(f'{bankapp}: AppStore(country=\'{rw_ios_src_dict[bankapp][1]}\', \
          app_name=\'{rw_ios_src_dict[bankapp][0]}\', app_id=\'{int(rw_ios_src_dict[bankapp][2])}\')')
    appStore.review()    
   
    df = pd.DataFrame(np.array(appStore.reviews),columns=['review'])
    df = df.join(pd.DataFrame(df.pop('review').tolist()))
    print(f'{bankapp}: {df.shape}')
    
    return df


def transform_data(data):
    """Transform input_data
    Args:
        data (df): Input dataframe (iOS or android)
    """
    clean_data = data.copy()
    # Positive (rating > 3) will be assigned to 1
    clean_data['sentiment_values'] = clean_data['rating'].apply(lambda x: -1 if x < 3 else (1 if x > 3 else 0))
    clean_data['text_cleaned'] = clean_data['review'].apply(basic_text_cleaning)
    
    return clean_data

def basic_text_cleaning(text):
    """Remove digits, vietnamese_common_stopwords
    Args:
        text (str): văn bản chưa qua xử lý 
    Returns:
        text (str): văn bản đã qua xử lý
    """
    text = text.lower()
    
    def translate(text, conversion_dict, before=None):
        """
        Translate words from a text using a conversion dictionary

        Arguments:
            text: the text to be translated
            conversion_dict: the conversion dictionary
            before: a function to transform the input
            (by default it will to a lowercase)
        """
        # if empty:
        if not text: return text
        # preliminary transformation:
        before = before or str.lower
        t = before(text)
        for key, value in conversion_dict.items():
            t = t.replace(key, value)
        return t
    
    # remove số
    text = text.replace('2.0', 'myvib')
    pattern = r'\b\d+(\.\d+)?k\b'
    # Replace matched patterns with 'money'
    text = re.sub(pattern, 'money', text)
    text = re.sub(r'[0-9]+', '', text)
    
    # remove enter-space
    text = text.replace("\n", ' ')
    text = text.replace("\t", ' ')
    
    # remove punctuation    
    for _ in string.punctuation:
        text = text.replace(_, ' ')
    # đổi tên + chỉnh lỗi chính tả
    dict_text = {
                'ngân hàng': 'ngân_hàng',
                'sms banking': 'sms_banking',                
                'banks': 'bank',
                'chuyen': 'chuyển',
                'tài khoảng': 'tài_khoản',
                'thẻ ngân_hàng': 'thẻ_ngân_hàng',
                'biets': 'biết',
                'không biet': 'không biết',
                'ứng dung': 'ứng dụng',
                'biét': 'biết',
                'ngta': 'người_ta',
                'nâg': 'nâng',
                'phaỉ': 'phải',
                'boỏ': 'bỏ',
                'bii': 'bị',
                'mạt khẩu': 'mật_khẩu',
                'đc': 'được',
                'xuôngd': 'xuống',
                'nma': 'nhưng_mà',
                'bg': 'bây_giờ',
                'nvnh': 'nhân_viên ngân_hàng',
                'trl' : 'trả_lời',
                'ứng dụng': 'ứng dụng',
                'khách hàng': 'khách_hàng',
                'application': 'app',
                'update': 'cập_nhật',
                'cập nhật': 'cập_nhật',
                'dự an': 'dự_án',
                'dự án': 'dự_án',
                ' khong ': ' không ',
                'cccd': 'căn_cước_công_dân',
                'thẻ căn_cước_công_dân': 'thẻ_căn_cước_công_dân',
                'hình thẻ': 'hình_thẻ',
                'sinh học': 'sinh_học',
                'sinh trắc': 'sinh_trắc',
                'chuyển tiền': 'chuyển_tiền',
                'việc chuyển_tiền': 'việc_chuyển_tiền',
                'hệ thống': 'hệ_thống',
                'tiêu dùng': 'tiêu_dùng',
                'người tiêu_dùng': 'người_tiêu_dùng',
                'tóm lại': 'tóm_lại',
                'ko': 'không',
                'tài khoản': 'tài_khoản',
                'bill': 'hóa_đơn',
                'hóa đơn': 'hóa_đơn',
                'cty': 'công_ty',
                'nhân viên': 'nhân_viên',
                'tạo tk': 'tạo tài_khoản',
                'thẻ bh': 'thẻ_bảo_hiểm',
                'account': 'tài_khoản',
                'saving account': 'tài_khoản tiết_kiệm',                
                'acc': 'tài_khoản',
                'androi': 'android',
                'androidd': 'android',
                'bug': 'lỗi',
                'giao diện': 'giao_diện',
                # thẻ
                'mở thẻ': 'mở_thẻ',
                'đóng thẻ': 'đóng_thẻ',
                'khóa thẻ': 'khóa_thẻ',
                'hủy thẻ': 'hủy_thẻ',
                'thẻ tín_dụng': 'thẻ_tín_dụng',
                'thông_tin thẻ': 'thông_tin_thẻ',                
                'số dư': 'số_dư',
                'thông báo': 'thông_báo',
                'thông_báo rác': 'thông_báo_rác',
                'thông_báo ck': 'thông_báo chuyển_khoản',
                'tin tưỡng': 'tin_tưởng',
                'đề ngị': 'đề_nghị',
                '₫': 'không',
                'cskh': 'chăm_sóc_khách_hàng',
                'nt fange': 'nhắn tin',
                'ứg dụng': 'ứng dụng',
                'ads': 'quảng cáo',
                'cụ thể': 'cụ_thể',
                'notification': 'thông_báo',
                'turn off': 'tắt',
                'messages': 'tin_nhắn',
                'tin nhắn': 'tin_nhắn',
                'but': 'nhưng',
                'still':' vẫn',
                'receive': 'nhận được',
                'stuffs': 'lộn xộn',
                'about': 'về',
                'actually': 'chính xác',
                'all': 'tất cả',
                'great': 'tuyệt',
                'unactive': 'vô hiệu hóa',
                'active': 'kích hoạt',
                'good': 'tốt',
                'accrued interest amount': 'tài_khoản tích_lũy',
                'accrued': 'tích_lũy',
                'ứng dụng cụ': 'ứng_dụng cũ',
                'ứng đụng': 'ứng_dụng',
                'ứng như': 'ứng_dụng như',
                'phien ban': 'phiên_bản',
                'phiên bản': 'phiên_bản',
                'ăn cướp': 'ăn_cướp',
                'cai lui': 'cải lùi',
                'so voi': 'so với',
                'đơn điệu': 'đơn_điệu',
                'màn hình': 'màn_hình',
                'banh kinh': 'banking',
                'sms banh kinh': 'sms_banking',
                'chuyển khoản': 'chuyển_khoản',
                'banhking': 'banking', 
                'bankking': 'banking', 
                'bankning': 'banking',
                'hống hách': 'hống_hách',
                'bạn bè': 'bạn_bè',
                'điện thoại': 'điện_thoại',
                'cam on cac ban rat nhieu': 'cám_ơn các_bạn rất_nhiều',
                'sốp': 'shop',
                'dk roi': 'được rồi',
                'quyét mặt': 'quét mặt',
                'ntnao': 'như thế nào',
                'thời gian': 'thời_gian',
                'mâý': 'mấy',
                'bjt': 'biết',
                'biêt': 'biết',
                'chêeeeeeeee': 'chê',
                'chổ': 'chỗ',
                'chữa': 'chửa',
                'cmmd': 'chửi_tục', 
                'tổng đài': 'tổng_đài', 
                'liên lạc': 'liên_lạc', 
                'liên hệ': 'liên_hệ',
                'cmnl': 'chửi_tục',
                'ccccccc': 'chửi_tục',
                'cdb': 'chửi_tục',
                'cdcm': 'chửi_tục',
                'cđb': 'chửi_tục',
                'cdclmmmmm': 'chửi_tục',
                'content': 'nội_dung',
                'csdl': 'cơ_sở dữ_liệu',
                'gương mặt': 'gương_mặt',
                'cặk': 'chửi_tục',
                'cặt': 'chửi_tục',
                'djt': 'chửi_tục', 
                'dki': 'đăng_ký', 
                'dkm': 'chửi_tục', 
                'dme': 'chửi_tục', 
                'dmm': 'chửi_tục', 
                'dmvib': 'chửi_tục',
                'dởm': 'chửi_tục',
                'dứoi': 'dưới',
                'gdich': 'giao_dịch',
                'giao dịch': 'giao_dịch',
                'gthieu': 'giới thiệu',
                'gth': 'giới thiệu', 
                'hayyyyb': 'hay', 
                'hayyyyy': 'hay',
                'hãi': 'chửi_tục',
                'hãm': 'chửi_tục',
                'cải thiện': 'cải_thiện',
                'giới thiệu': 'giới_thiệu',
                'chương trình': 'chương_trình', 
                'phần thưởng': 'phần_thưởng',
                'hỗ trợ': 'hỗ_trợ',
                'bảo mật': 'bảo_mật',
                'khuôn mặt': 'khuôn_mặt',
                'quảng cáo': 'quảng_cáo',
                'trách nhiệm': 'trách_nhiệm',
                'kết nối': 'kết_nối', 
                'máy chủ': 'máy_chủ',
                'tín dụng': 'tín_dụng', 
                'cắt cổ': 'cắt_cổ', 
                'trả góp': 'trả_góp',
                'gián đoạn': 'gián_đoạn', 
                'đăng nhập': 'đăng_nhập',
                'dag nhap': 'đăng_nhập',
                'dang nhap': 'đăng_nhập',
                'tiet kiem': 'tiết_kiệm',
                'thoi gian': 'thời_gian',
                'hạn mức': 'hạn_mức', 
                'ưu đãi': 'ưu_đãi',
                'tỉ lệ': 'tỉ_lệ',
                'tỷ lệ': 'tỷ_lệ',
                'mua sắm': 'mua_sắm',
                'cong suc': 'công_sức',
                'xác thực': 'xác_thực',
                'sao kê': 'sao_kê',
                'online':' trực_tuyến',
                'smart otp': 'smart_otp',
                'tính năng bảo mật': 'tính_năng_bảo_mật',
                'user': 'người_dùng',
                'người dùng': 'người_dùng',
                'trả nghiênm': 'trải_nghiệm',
                'trai nghiem': 'trải_nghiệm',
                'trải nghiệm': 'trải_nghiệm',
                'không có': 'không_có',
                'bố đời': 'bố_đời',
                'hoàn phí': 'hoàn_phí',
                'biểu phí':'biểu_phí',
                'đóng phí': 'đóng_phí',
                'không nghe máy': 'không_nghe_máy',
                'kích hoaht': 'kích_hoạt',
                'làm lộ': 'làm_lộ',
                'bán thông tin': 'bán_thông_tin',
                'tài chính đen': 'tài_chính_đen',
                'tín dụng đen': 'tín_dụng_đen',
                'cho vay': 'cho_vay',
                'nặng lãi': 'nặng_lãi',
                'dung lg': 'dung_lượng',
                'dung lượng': 'dung_lượng',
                'gửi tiền': 'gửi_tiền',
                'mất tiền': 'mất_tiền',
                'rút tiền': 'rút_tiền',
                'nuốt tiền': 'nuốt_tiền',
                'hình nền': 'hình_nền',
                'rối mắt': 'rối_mắt',
                'khó nhìn': 'khó_nhìn',
                'hoàn tiền': 'hoàn_tiền',
                ' quét mã ': ' quét_mã ',
                'chạy lòng vòng': 'chạy_lòng_vòng',
                'đăng kí': 'đăng_ký',
                'đăng ký': 'đăng_ký',
                'phần mềm': 'phần_mềm',
                'bảo hiểm': 'bảo_hiểm',
                'dữ liệu': 'dữ_liệu',
                'thông tin': 'thông_tin',
                'tư vấn': 'tư_vấn',
                'tín dụng': 'tín_dụng',
                'thẻ tín dụng': 'thẻ_tín_dụng',
                'tính năng': 'tính_năng',
                'chức năng': 'chức_năng',
                'nâng cấp': 'nâng_cấp',
                'bộ nhớ': 'bộ_nhớ',
                'hiển thị': 'hiển_thị',
                'rườm rà': 'rườm_rà',
                'bắt mắt': 'bắt_mắt',
                'thiết kế': 'thiết_kế',
                'trực quan': 'trực_quan',
                'màu mè': 'màu_mè',
                'nói chuyện': 'nói_chuyện',
                'giọng điệu': 'giọng_điệu',
                'phiền nhiễu': 'phiền_nhiễu',
                'cuộc gọi': 'cuộc_gọi',
                'liên tục': 'liên_tục',
                'khủng bố': 'khủng_bố',
                }
    text = translate(text, dict_text)   
    text = translate(text, {
                'uy tín': 'uy_tín',                
                'làm phiền': 'làm_phiền',
                'lừa dân': 'lừa_dân',
                'lừa đảo': 'lừa_đảo',
                'tổ chức': 'tổ_chức',
                'thanh toán': 'thanh_toán',
                'nhận diện': 'nhận_diện',
                'cập nhập': 'cập_nhật',
                'tối ưu': 'tối_ưu',
                'ứng dụng': 'ứng_dụng',
                'lừa dối': 'lừa_dối',
                'bảo trì': 'bảo_trì',
                'giam tiền': 'giam_tiền',
                'không đầy đủ': 'không_đầy_đủ',
                'làm rõ': 'làm_rõ',
                'quét chip': 'quét_chip',
                'ma pin': 'mã_pin',
                'mã pin': 'mã_pin',
                'điện nước': 'điện_nước',
                'trừ tiền': 'trừ_tiền',
                'ct không được': 'chuyển_tiền không_được',
                'không hiện': 'không_hiện',
                'sơ sài': 'sơ_sài',
                'font chữ': 'font_chữ',
                'stk khác': 'tài_khoản khác',
                'tk khác': 'tài_khoản khác',
                'ăn lời': 'ăn_lời',
                'bán thông_tin': 'bán_thông_tin',
                'không minh bạch': 'không_minh_bạch',
                'bản cũ': 'bản_cũ',
                'cbnv': 'cán_bộ nhân_viên',
                'cap nhật': 'cập_nhật',
                'xuôngd': 'xuống',
                'bị tính phí': 'bị_tính_phí',
                'gia hạn thẻ': 'gia_hạn_thẻ',
                'ngân hangd': 'ngân_hàng',
                'pgd': 'phòng_giao_dịch',
                'gdich': 'giao_dịch',
                'gd': 'giao_dịch',
                'dịch vụ': 'dịch_vụ',
                'chất lượng': 'chất_lượng',
                'câu giờ': 'câu_giờ',
                'thành toán': 'thanh_toán',
                'đang ký': 'đăng_ký',
                'đang nhập': 'đăng_nhập',
                'dang nhập': 'đăng_nhập',
                'phản ánh': 'phản_ánh',
                'trợ lý ảo': 'trợ_lý_ảo',
                'đkien': 'điều_kiện',
                'đki': 'đăng_ký',
                ' vao đc': ' vào_được',
                ' vao dc': ' vào_được',                             
                ' vao ': ' vào ',
                ' không vào ': ' không_vào ',
                'vào được ': 'vào_được',
                'không vào được': ' không_vào_được ',
                'gian dối': 'gian_dối',
                ' phí thường niên': ' phí_thường_niên ',
                'mật khẩu': 'mật_khẩu',
                'nhập mật vô': 'nhập mật_khẩu vô',
                'cách phục vụ': 'cách_phục_vụ',
                'tin tưởng': 'tin_tưởng',
                'nhập mã': 'nhập_mã',
                'log in': 'login',
                'tải về': 'tải_về',
                'gửi mã': 'gửi_mã',
                'đăng xuất': 'đăng_xuất',
                'chỗ liên kết': 'chỗ_liên_kết',
                'xỏ mũi': 'xỏ_mũi',
                'mập mờ': 'mập_mờ',
                'nang cấp': 'nâng_cấp',
                'trễ hạn': 'trễ_hạn',
                'chậm trễ': 'chậm_trễ',
                'nghe máy': 'nghe_máy',
                'hút máu': 'hút_máu',
                'định danh': 'định_danh',
                'huỷ thẻ': 'hủy_thẻ',
                'xác minh': 'xác_minh', 
                'nhân trắc': 'nhân_trắc',
                ' trả lời ': ' trả_lời ',
                ' nhắn_tin ': ' nhắn_tin ',
                'tham nhũng': 'tham_nhũng',
                'lộng hành': 'lộng_hành',
                'tự ý': 'tự_ý'
    })
    
    # remove một số từ stopwords trong VI
    removed_list = ['a', 'ae', 'ace', 'iem', 'đc', 'đi', 'ah', 'ak', 'album', 'chet', 'chánn','chèn', 'dknhs', 'hanh', 'hap',
                    'alo', 'bye', 'ar', 'dc', 'sẻ', 't', 'yc', 'appo', 'mám', 'buff', 'checkhôngut', 'chx', 'conin', 'deu', 'haz', 'hcf',
                    'beware', 'nc', 'abc', 'abcz', 'ai','buoc', 'asap','bar','biế', 'chai', 'cham', 'chao', 'chuản', 'dau', 'dcu', 'hieu',
                    'abcd', 'saoaf', 'bn', 'bh', 'roof', 'đx', 'ad', 'adm', 'baby', 'baen', 'choá', 'choán', 'chup', 'chuyene', 'hó',
                    'boỏ','dk','lolllllllllolololololl', 'tt','tao','haizzz', 'acb', 'chương', 'chải', 'chảo', 'dan',
                    'hoaht','is', 'it', 'ji', 'jk', 'ib', 'icon', 'nx','kg', 'kh', 'khacd', 'chực', 'ckang', 'cứoc', 'giẻ', 
                    'khieensal', 'lm', 'ln', 'logo', 'biệ', 'bla', 'bm', 'bot', 'bthg', 'coid', 'cois',' cũg', 'cũmg', 'khuên',
                    'ms','mj', 'mk', 'mn','ngta', 'vvv', 'vs', 'nn', 'bàng', 'bày', 'bá', 'cp', 'cqq', 'cảu', 'cảy', 'giấc', 
                    'nv', 'nyc', 'nâg', 'nân','pban', 'pc', 'phaỉ', 'h_h', 'haha', 'bươc', 'cuc', 'cunc', 'cungz', 'giọt', 'giỏ',
                    'biets', 'ﾟθ', 'va', 'báy', 'bâyh', 'bãi', 'bét', 'bưa', 'bưc', 'câph', 'câpn', 'diên', 'diều', 'giốg',
                    'xuôngd', 'bíai', 'bít', 'bòi', 'bòn', 'bấmbàiviếtcó', 'cọc', 'cồn', 'dong', 'doạ', 'dươc', 'dườm',
                    'caì', 'cbnv', 'cgv', 'ds', 'dug', 'dx', 'dãy', 'dè', 'dì', 'dò', 'dòg', 'dõm', 'dùg', 'dăng', 'dũng', 'dơ',
                    'dảo', 'dầy', 'dẩn', 'dẫ', 'dẫm', 'dập', 'dật', 'dố', 'dồ', 'dợ', 'dử', 'fải', 'giay', 'gio', 'gioa', 'hangd',
                    'giữi', 'giựt', 'gmai', 'goih', 'goole', 'goài', 'gq', 'gào', 'gí', 'gôd', 'gôôd', 'găm', 'gập', 'gờ', 'gửu', 'gữi',
                    'hoá', 'hoả', 'hoẹ', 'hpk', 'hqua', 'htai', 'htc', 'huykk', 'huệ', 'hy', 'hz', 'hànb', 'háng', 'hân', 'hât', 'hã',
                    'hôg', 'hú', 'hăn', 'hđh', 'hưu', 'hưỡng',  'idepo', 'if', 'iic', 'im', 'imo', 'ips', 'iqiyi', 'ir', 'jdheg', 'jdlobhl', 
                    'jnuslj', 'job', 'jok', 'jook', 'kha', 'khac', 'khach', 'khoãng', 'khoảv', 'khoẻ', 'khu', 'khung', 'khuu', 'khuông', 'khuất',
                    'kháck', 'khôngbe', 'khôngiachỉ', 'khôngản', 'khônng', 'khầu', 'khỏa', 'khống', 'khổ', 'ki', 'kich', 'kick', 'kiem', 'kiep',
                    'kiên', 'kiến', 'kiếp', 'kiễm', 'kkk', 'kkkk', 'ktien',  'ky', 'kèn', 'kèo', 'két', 'mạc', 'mạch', 'mạt', 'mả', 'mấ',
                    'nguyen', 'nguyenvanhoan', 'nguyễn', 'ngy', 'ngẽn', 'ngục', 'ngửi', 'ngữ', 'nhah', 'nham', 'nhang', 'nhiet', 'nhièu', 'nhiêig',
                    'nhnn', 'nhoe', 'nhoè', 'nhqt', 'nhue', 'nhuộm', 'nháo', 'nhát', 'nhã', 'nhì', 'nhìm', 'nhòe', 'nhưg', 'nhấp', 'nhần', 'nhậl', 'nhắt', 
                    'nhặp', 'nhặt', 'nhẽo', 'nhị', 'ni', 'nic', 'niê', 'non', 'nuôi', 'nuột', 'ny', 'náy', 'nâp', 'ngâng', 'ngâu', 
                    ] 
    
    removed_list = '|'.join(removed_list)
    regex = re.compile(r'\b('+removed_list+r')\b', flags=re.IGNORECASE)
    text = regex.sub(" ", text)
        
    return text #ViTokenizer.tokenize(text)

def returncolname(row, colnames):
    """
    Returns the column name corresponding to the maximum value in a row.
    Args:
        row (pd.Series): A row of numerical values.
        colnames (list): List of column names corresponding to the row values.
    Returns:
        str: The column name with the maximum value in the row.
    """    
    return colnames[np.argmax(row.values)]

def topic_modeling(clean_df):
    """
    Analyzes text data to classify topics and normalize topic scores based on predefined vocabularies (this is the first version)
    Parameters:
        clean_df (DataFrame): A pandas DataFrame containing a column 'text_cleaned' with preprocessed text data
                              and a column 'rating' representing user ratings.
    Returns:
        DataFrame: A modified DataFrame with new columns corresponding to normalized topic scores and 
                   the most prominent topic ('colmax') for each text entry.
    Description:
        The function uses predefined vocabularies to detect topics in the cleaned text data and assigns 
        scores based on the frequency of topic-specific terms. Topics include:
        - 'ekyc': Related to electronic know-your-customer processes.
        - 'trans': Related to transactions and financial operations.
        - 'card': Related to credit/debit card issues.
        - 'apperr': Related to application errors or bugs.
        - 'applag': Related to slow or lagging application performance.
        - 'applogin': Related to login/logout or password issues.
        - 'ui_err': Related to user interface design or usability concerns.
        - 'otp_qr': Related to OTP (one-time password) or QR code issues.
        - 'spam': Related to spam messages or advertisements.
        - 'fraud': Related to fraudulent activities or scams.
        - 'staff': Related to staff behavior or customer service.
        - 'nfc': Related to NFC (near-field communication) technology.
        Additional Calculations:
        - A 'total_score' column is computed as the sum of topic scores for normalization.
        - The 'colmax' column identifies the most prominent topic based on normalized scores.
        - Entries with no prominent topics and low ratings are labeled as 'Undefined'.
        - Entries with no prominent topics and high ratings are labeled as 'Good_review'.
    Example:
        # Assuming clean_df contains 'text_cleaned' and 'rating' columns:
        result_df = topic_modeling2(clean_df)
    Notes:
        - The function modifies and returns a copy of the input DataFrame.
        - If none of the predefined terms are found in the text, the topic is labeled as 'Undefined' 
          for low-rated reviews or 'Good_review' for high-rated reviews.
    """    
    card_vocab = ['thẻ_tín_dụng', 'mở_thẻ', 'hạn_mức', 'thẻ', 'debit', 'thẻ_ngân_hàng', 'bị_tính_phí', 'gia_hạn_thẻ',
                'đóng_thẻ', 'khóa_thẻ', 'hủy_thẻ', 'biểu_phí', 'đóng_phí', 'phí_thường_niên', 'trễ_hạn']

    app_err_vocab = ['tính_năng_bảo_mật', 'nâng_cấp', 'cập_nhật', 'lỗi', 'bộ_nhớ', 'dung_lượng', 'phiên_bản', 'ver',
                    'ứng_dụng', 'app', 'ap', 'appl', 'myvib', 'phần_mềm', 'chức_năng', 'tính_năng', 'hiển_thị', 'dịch_vụ',
                    'rườm_rà', 'số_dư', 'tối_ưu', 'bảo_trì', 'appp', 'không_hiện', 'bản_cũ', 'tài_khoản', 'trải_nghiệm', 
                    'chất_lượng', 'trợ_lý_ảo', 'deploy', 'phiên_bản_cũ', 'chương_trình', 'sms_banking',
                    'hệ_thống', 'lucky', 'chỗ_liên_kết', 'áp', 'event'
                    ]  # procedure|virt-asist|other-features/program

    login_vocab = ['đăng_nhập', 'phiên_bản', 'ứng_dụng', 'văng', 'app', 'ap', 'appl', 'myvib', 'áp', 'phần_mềm', 'login', 'đăng_xuất', 'lỗi', 'timeout', 'nhập',
                'ver', 'hệ_thống', 'đăng_ký', 'không_vào', 'không_vào_được', 'vao_dc', 'mật_khẩu', 'phiên_bản', 'bản_cũ', 'tải_về', 'tài_khoản', 'sập', 'tạo'
                ] # login|logout|register|passwords

    ui_vocab = ['giao_diện', 'màn_hình', 'rối_mắt', 'bắt_mắt', 'thiết_kế', 'trực_quan', 'màu_mè', 'ứng_dụng', 'chức_năng', 'font_chữ',
                'app', 'ap', 'appl', 'myvib', 'phần_mềm', 'hình_nền', 'khó_nhìn', 'ui', 'đơn_điệu', 'appp', 'sơ_sài', 'áp']

    app_slow_vocab = ['ứng_dụng', 'app', 'ap', 'appl', 'myvib', 'phần_mềm', 'lag', 'chậm', 'giật', 'đơ', 'chạy_lòng_vòng',
                    'gián_đoạn', 'loading', 'appp', 'load', 'lâu', 'quay', 'treo', 'kết_nối', 'đợi', 'chờ']

    staff_vocab = ['chăm_sóc_khách_hàng', 'nhân_viên', 'tư_vấn', 'tổng_đài', 'nói_chuyện', 'hống_hách', 'bố_đời', 'câu_giờ', 'nhắn_tin',
                'giọng_điệu', 'không_nghe_máy', 'hotline', 'liên_hệ', 'phản_ánh', 'cách_phục_vụ', 'gọi', 'nghe_máy', 'trả_lời']

    spam_mes = ['tin_nhắn', 'quảng_cáo', 'phiền_nhiễu', 'cuộc_gọi', 'nhiều', 'liên_tục', 'spam', 'khủng_bố', 'làm_phiền', 
                'thông_báo_rác', 'không_có']

    fraud_vocab = ['bảo_mật', 'lừa_đảo', 'bán_thông_tin', 'tài_chính_đen', 'tín_dụng_đen', 'tổ_chức', 'cho_vay', 'không_đầy_đủ', 'xỏ_mũi',
                'nặng_lãi', 'lãi_suất', 'ăn_cắp', 'ưu_đãi', 'bạn_bè', 'người_thân', 'lãi', 'lừa_dối', 'làm_rõ', 'cắt_cổ', 'ăn_cướp',
                'ăn_lời', 'uy_tín', 'lừa_dân', 'không_minh_bạch', 'lừa', 'gian_dối', 'bịp', 'tin_tưởng', 'mập_mờ', 'hút_máu', 'tham_nhũng',
                'lộng_hành', 'tự_ý'
                ]

    trans_vocab = ['giao_dịch', 'chuyển_tiền', 'rút_tiền', 'gửi_tiền', 'atm', 'nuốt_tiền', 'mất_tiền', 'tài_khoản', 'điện_nước', 'tiền',
                'thanh_toán', 'hóa_đơn', 'hoàn_tiền', 'chức_năng', 'cashback', 'số_dư', 'giam_tiền', 'chuyển', 'trừ_tiền', 'stk',
                'bị_tính_phí', 'hạn_mức', 'chuyển_khoản', 'nạp', 'rút', 'tiền', 'phí', 'app', 'money'
                ]

    ekyc_vocab = ['sinh_trắc', 'gương_mặt', 'khuôn_mặt', 'mặt', 'faceid', 'chức_năng', 'nhận_diện', 'xác_thực', 'chụp', 'vneid',
                'cập_nhật', 'định_danh', 'căn_cước_công_dân', 'kyc', 'ekyc', 'eye', 'xác_minh', 'nhân_trắc', 'sth']

    otp_qr_vocab = ['qr', 'quét_mã', 'otp', 'mã_pin', 'smart_otp', 'nhập_mã', 'gửi_mã', 'lỗi', 
                    'app', 'ap', 'appl'] # Code_Scaning
    nfc_vocab = ['nfc', 'quét_chip']

    #======================== Topic naming
    temp = clean_df.copy()
    temp['ekyc'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in ekyc_vocab]) / len(x.split(" ")))
    temp['trans'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in trans_vocab]) / len(x.split(" ")))
    temp['card'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in card_vocab]) / len(x.split(" ")))
    temp['apperr'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in app_err_vocab]) / len(x.split(" ")))
    temp['applag'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in app_slow_vocab]) / len(x.split(" ")))
    temp['applogin'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in login_vocab]) / len(x.split(" ")))
    temp['ui_err'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in ui_vocab]) / len(x.split(" ")))
    temp['otp_qr'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in otp_qr_vocab]) / len(x.split(" ")))
    temp['spam'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in spam_mes]) / len(x.split(" ")))
    temp['fraud'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in fraud_vocab]) / (len(x.split(" ")) - 0.05))
    temp['staff'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in staff_vocab]) / len(x.split(" ")))
    temp['nfc'] = temp['text_cleaned'].apply(lambda x: 1 if any(t for t in x.split(" ") if t in nfc_vocab) else 0)

    #==========================
    cols = ['ekyc', 'nfc', 'trans', 'card', 'apperr', 'applag', 'applogin', 'ui_err', 'otp_qr', 'spam', 'fraud', 'staff']
    temp['total_score'] = temp[cols].sum(axis=1).apply(lambda x: 1 if x == 0 else x)
    mask = (temp[cols].max(axis=1) == 0)& (temp.rating <= 3)
    mask_p = (temp[cols].max(axis=1) == 0)& (temp.rating > 3)
    for col in cols:        
        temp.loc[:, col] = temp.loc[:, col] / temp.loc[:, 'total_score']
    temp['colmax'] = temp.apply(lambda x: returncolname(x[cols], cols), axis=1)
    temp.loc[mask, 'colmax'] = 'Undefined'
    temp.loc[mask_p, 'colmax'] = 'Good_review'
    
    return temp.drop(columns='total_score')

def topic_mapping(text):
    """
    Maps a topic identifier to a detailed title.
    Args:
        text (str): Topic identifier.
    Returns:
        str: Mapped title with a detailed description.
    """
    label_dict = {
        'trans': 'Transaction|Payments-transfer|Charge&Recharge', 
        'ui_err':'Bad_UI(bad-interface| difficult-to-use)', 
        'card': 'Card_issue (cannot-activate/remove_card)',
        'ekyc': 'eKYC(face_scanning)',
        'staff' : 'Supporting_staff(cannot connect to the switch-board, bad attitude)', 
        'applag': 'App_slow_lag', 
        'applogin': 'App_cannot(login|logout|register|password)',
        'apperr': 'App_error_Complaint(procedure|virtual-asisitant|program-complaint|other-features)',  
        'otp_qr': '(OTP|QR)_scanning_code_issues',
        'spam': 'Spam_Notification (message|adv|etc)', 
        'fraud': 'Loan-interest|Fraud|De-fraud|', 
        'nfc': 'NFC-issues',
        'Undefined': 'UndefinedTopic(Not-complaint-the-specified-object)',
        'Good_review': 'These reviews are positive'
    }
    return label_dict[text]

def topic_modeling2(clean_df):
    """
    Analyzes text data to classify topics and normalize topic scores based on predefined vocabularies.
    Parameters:
        clean_df (DataFrame): A pandas DataFrame containing a column 'text_cleaned' with preprocessed text data
                              and a column 'rating' representing user ratings.
    Returns:
        DataFrame: A modified DataFrame with new columns corresponding to normalized topic scores and 
                   the most prominent topic ('colmax') for each text entry.
    Description:
        The function uses predefined vocabularies to detect topics in the cleaned text data and assigns 
        scores based on the frequency of topic-specific terms. Topics include:
        - 'ekyc': Related to electronic know-your-customer processes.
        - 'trans': Related to transactions and financial operations.
        - 'card': Related to credit/debit card issues.
        - 'apperr': Related to application errors or bugs.
        - 'applag': Related to slow or lagging application performance.
        - 'applogin': Related to login/logout or password issues.
        - 'ui_err': Related to user interface design or usability concerns.
        - 'otp_qr': Related to OTP (one-time password) or QR code issues.
        - 'spam': Related to spam messages or advertisements.
        - 'fraud': Related to fraudulent activities or scams.
        - 'staff': Related to staff behavior or customer service.
        - 'nfc': Related to NFC (near-field communication) technology.
        Additional Calculations:
        - A 'total_score' column is computed as the sum of topic scores for normalization.
        - The 'colmax' column identifies the most prominent topic based on normalized scores.
        - Entries with no prominent topics and low ratings are labeled as 'Undefined'.
        - Entries with no prominent topics and high ratings are labeled as 'Good_review'.
    Example:
        # Assuming clean_df contains 'text_cleaned' and 'rating' columns:
        result_df = topic_modeling2(clean_df)
    Notes:
        - The function modifies and returns a copy of the input DataFrame.
        - If none of the predefined terms are found in the text, the topic is labeled as 'Undefined' 
          for low-rated reviews or 'Good_review' for high-rated reviews.
    """
    # Vocabulary definitions
    card_vocab = ['thẻ_tín_dụng', 'mở_thẻ', 'hạn_mức', 'thẻ', 'debit', 'thẻ_ngân_hàng', 'bị_tính_phí', 'gia_hạn_thẻ',
                  'đóng_thẻ', 'khóa_thẻ', 'hủy_thẻ', 'biểu_phí', 'đóng_phí', 'phí_thường_niên', 'trễ_hạn']
    app_err_vocab = ['tính_năng_bảo_mật', 'nâng_cấp', 'cập_nhật', 'lỗi', 'bộ_nhớ', 'dung_lượng', 'phiên_bản', 'ver',
                     'ứng_dụng', 'app', 'ap', 'appl', 'myvib', 'phần_mềm', 'chức_năng', 'tính_năng', 'hiển_thị',
                     'dịch_vụ', 'rườm_rà', 'số_dư', 'tối_ưu', 'bảo_trì', 'appp', 'không_hiện', 'bản_cũ', 'tài_khoản',
                     'trải_nghiệm', 'chất_lượng', 'trợ_lý_ảo', 'deploy', 'phiên_bản_cũ', 'chương_trình', 'sms_banking',
                     'hệ_thống', 'lucky', 'chỗ_liên_kết', 'áp', 'event']
    login_vocab = ['đăng_nhập', 'phiên_bản', 'ứng_dụng', 'văng', 'app', 'ap', 'appl', 'myvib', 'áp', 'phần_mềm', 'login',
                   'đăng_xuất', 'lỗi', 'timeout', 'nhập', 'ver', 'hệ_thống', 'đăng_ký', 'không_vào', 'không_vào_được',
                   'vao_dc', 'mật_khẩu', 'bản_cũ', 'tải_về', 'tài_khoản', 'sập', 'tạo']
    ui_vocab = ['giao_diện', 'màn_hình', 'rối_mắt', 'bắt_mắt', 'thiết_kế', 'trực_quan', 'màu_mè', 'ứng_dụng', 'chức_năng',
                'font_chữ', 'app', 'ap', 'appl', 'myvib', 'phần_mềm', 'hình_nền', 'khó_nhìn', 'ui', 'đơn_điệu', 'appp',
                'sơ_sài', 'áp']
    app_slow_vocab = ['ứng_dụng', 'app', 'ap', 'appl', 'myvib', 'phần_mềm', 'lag', 'chậm', 'giật', 'đơ', 'chạy_lòng_vòng',
                      'gián_đoạn', 'loading', 'appp', 'load', 'lâu', 'quay', 'treo', 'kết_nối', 'đợi', 'chờ']
    staff_vocab = ['chăm_sóc_khách_hàng', 'nhân_viên', 'tư_vấn', 'tổng_đài', 'nói_chuyện', 'hống_hách', 'bố_đời', 'câu_giờ',
                   'nhắn_tin', 'giọng_điệu', 'không_nghe_máy', 'hotline', 'liên_hệ', 'phản_ánh', 'cách_phục_vụ', 'gọi',
                   'nghe_máy', 'trả_lời']
    spam_mes = ['tin_nhắn', 'quảng_cáo', 'phiền_nhiễu', 'cuộc_gọi', 'nhiều', 'liên_tục', 'spam', 'khủng_bố', 'làm_phiền',
                'thông_báo_rác', 'không_có']
    fraud_vocab = ['bảo_mật', 'lừa_đảo', 'bán_thông_tin', 'tài_chính_đen', 'tín_dụng_đen', 'tổ_chức', 'cho_vay',
                   'không_đầy_đủ', 'xỏ_mũi', 'nặng_lãi', 'lãi_suất', 'ăn_cắp', 'ưu_đãi', 'bạn_bè', 'người_thân', 'lãi',
                   'lừa_dối', 'làm_rõ', 'cắt_cổ', 'ăn_cướp', 'ăn_lời', 'uy_tín', 'lừa_dân', 'không_minh_bạch', 'lừa',
                   'gian_dối', 'bịp', 'tin_tưởng', 'mập_mờ', 'hút_máu', 'tham_nhũng', 'lộng_hành', 'tự_ý', 'vay']
    trans_vocab = ['giao_dịch', 'chuyển_tiền', 'rút_tiền', 'gửi_tiền', 'atm', 'nuốt_tiền', 'mất_tiền', 'tài_khoản',
                   'điện_nước', 'tiền', 'thanh_toán', 'hóa_đơn', 'hoàn_tiền', 'chức_năng', 'cashback', 'số_dư', 'giam_tiền',
                   'chuyển', 'trừ_tiền', 'stk', 'bị_tính_phí', 'hạn_mức', 'chuyển_khoản', 'nạp', 'rút', 'tiền', 'phí',
                   'app', 'money']
    ekyc_vocab = ['sinh_trắc', 'gương_mặt', 'khuôn_mặt', 'mặt', 'faceid', 'chức_năng', 'nhận_diện', 'xác_thực', 'chụp',
                  'vneid', 'cập_nhật', 'định_danh', 'căn_cước_công_dân', 'kyc', 'ekyc', 'eye', 'xác_minh', 'nhân_trắc',
                  'sth']
    otp_qr_vocab = ['qr', 'quét_mã', 'otp', 'mã_pin', 'smart_otp', 'nhập_mã', 'gửi_mã', 'lỗi', 'app', 'ap', 'appl']
    nfc_vocab = ['nfc', 'quét_chip']

    # Process the DataFrame and calculate topic scores
    temp = clean_df.copy()
    temp['ekyc'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in ekyc_vocab]) / len(x.split(" ")))
    temp['trans'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in trans_vocab]) / len(x.split(" ")))
    temp['card'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in card_vocab]) / len(x.split(" ")))
    temp['apperr'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in app_err_vocab]) / len(x.split(" ")))
    temp['applag'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in app_slow_vocab]) / len(x.split(" ")))
    temp['applogin'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in login_vocab]) / len(x.split(" ")))
    temp['ui_err'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in ui_vocab]) / len(x.split(" ")))
    temp['otp_qr'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in otp_qr_vocab]) / len(x.split(" ")))
    temp['spam'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in spam_mes]) / len(x.split(" ")))
    temp['fraud'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in fraud_vocab]) / (len(x.split(" ")) - 0.05))
    temp['staff'] = temp['text_cleaned'].apply(lambda x: len([t for t in x.split(" ") if t in staff_vocab]) / len(x.split(" ")))
    temp['nfc'] = temp['text_cleaned'].apply(lambda x: 1 if any(t for t in x.split(" ") if t in nfc_vocab) else 0)

    # Normalize scores and determine the most prominent topic
    cols = ['ekyc', 'nfc', 'trans', 'card', 'apperr', 'applag', 'applogin', 'ui_err', 'otp_qr', 'spam', 'fraud', 'staff']
    temp['total_score'] = temp[cols].sum(axis=1).apply(lambda x: 1 if x == 0 else x)
    mask = (temp[cols].max(axis=1) == 0) & (temp.rating <= 3)
    mask_p = (temp[cols].max(axis=1) == 0) & (temp.rating > 3)
    for col in cols:
        temp.loc[:, col] = temp.loc[:, col] / temp.loc[:, 'total_score']
    temp['colmax'] = temp.apply(lambda x: returncolname(x[cols], cols), axis=1)
    temp.loc[mask, 'colmax'] = 'Undefined'
    temp.loc[mask_p, 'colmax'] = 'Good_review'

    return temp.drop(columns='total_score')

def create_folder(path):
    """
    Creates a folder at the specified path if it does not already exist.
    Parameters:
        path (str): The path where the folder should be created.
    Behavior:
        - If the folder does not exist, it creates the folder and prints a success message.
        - If the folder already exists, it prints a message indicating so.
        - If an error occurs during folder creation, it catches the exception and prints an error message.
    """
    try:
        # Kiểm tra xem thư mục đã tồn tại chưa
        if not os.path.exists(path):
            # Tạo thư mục
            os.makedirs(path)
            print(f"Thư mục '{path}' đã được tạo thành công.")
        else:
            print(f"Thư mục '{path}' đã tồn tại.")
    except Exception as e:
        # Xử lý ngoại lệ nếu có lỗi xảy ra
        print(f"Có lỗi xảy ra khi tạo thư mục: {e}")