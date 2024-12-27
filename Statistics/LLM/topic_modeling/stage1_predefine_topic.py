import time, warnings, logging
import pandas as pd
from topic_modeling import *
from datetime import datetime, timedelta

warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.info("Starting in process")
logger.info("#====================================================================================#")
logger.info("************************************ Step 1. ***************************************")

# Get today's date
today = datetime.today()

# Calculate the first day of the current month
first_day_of_month = today.replace(day=1)

# Set the lookback_date to the first day of the current month in 'YYYYMMDD' format
lookback_date = first_day_of_month.strftime('%Y%m%d')

# Calculate trunc_date_check_labeled as 12 months ago from the first day of the current month
twelve_months_ago = first_day_of_month - timedelta(days=365)
trunc_date_check_labeled = twelve_months_ago.strftime('%Y-%m-%d')

# Output the values
logger.info(f"lookback_date: {lookback_date}")
logger.info(f"trunc_date_check_labeled: {trunc_date_check_labeled}")

# Crawling
last_year_dt = str(int(lookback_date) - 10000)
lookback_date = datetime.strptime(lookback_date, '%Y%m%d').strftime("%Y-%m-%d")
last_year_dt = datetime.strptime(last_year_dt, '%Y%m%d').strftime("%Y-%m-%d")
next_targdate = datetime.strptime(lookback_date, '%Y-%m-%d') + timedelta(days=334)
next_targdate = next_targdate.strftime("%Y-%m-%d")

logger.info("/-------------------- Data from android is started to crawl ------------------------/")
t0 = time.time()
DATA_PATH = './data'
bank_array = ['tcb2']
rw_android_src_dict = {
                'tcb2':['com.vib.mytcb2','vi','vn'],
                'tcb2':['com.vib.mytcb2','en','us']
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
    time.sleep(10)
df_android_used = rawdf[['userName','content','at','score','bankapp','platform']]
df_android_used.rename(columns = {'userName':'username','content':'review','at':'date','score':'rating'}, 
                       inplace=True)

# Convert timetamps to string
df_android_used['date'] = df_android_used['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))
print(f"Process finished after {(time.time() - t0):.3f} seconds")
df_android_used.to_csv("temp_data/from_android.csv", index=False)
print(df_android_used.shape)
t0 = time.time()
rw_ios_src_dict = {
                   'tcb2':['bank-ver 2.0','vn','sth-here']
                  }

logger.info("/------------------- Data from iOS is started to crawl -------------------------/")
column = ['title','userName','isEdited','review','date','rating','developerResponse','bankapp','platform']
df_ios_rw = pd.DataFrame(columns = column)

get_review_in = bank_array #rw_ios_src_dict.keys()

for bankapp in get_review_in:
    iosrw_df = get_rwdata_ios(rw_ios_src_dict, bankapp) 
    iosrw_df['bankapp'] = bankapp
    iosrw_df['platform'] = 'ios'
    df_ios_rw = pd.concat([df_ios_rw, iosrw_df])  
    time.sleep(30)
    
#JUST RAW
df_ios_used = df_ios_rw[['userName','review','date','rating','bankapp','platform']]
df_ios_used.rename(columns = {'userName':'username'}, inplace=True)

# Convert timetamps to string
df_ios_used['date'] = df_ios_used['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))
logger.info(f"Process finished after {(time.time() - t0):.3f} seconds")
df_ios_used.to_csv('temp_data/from_ios.csv', index=False)
print(df_ios_used.shape)
df_ios_used.head(10)

logger.info("Crawl data from ios and android completed successfully!!!")
logger.info("#====================================================================================#")
logger.info("************************************ Step 2. ***************************************")
from topic_modeling import *

df_ard = pd.read_csv("temp_data/from_android.csv")
df_ios = pd.read_csv("temp_data/from_ios.csv")
df_ard['date'] = pd.to_datetime(df_ard['date'])
df_ios['date'] = pd.to_datetime(df_ios['date'])
print(df_ard.head())
print(df_ios.head())

ard_clean_df = transform_data(df_ard)
ios_clean_df = transform_data(df_ios)

ard_clean_df = transform_data(df_ard)[['date', 'text_cleaned', 'review', 'sentiment_values', 'rating']]
ard_clean_df['platform'] = 'android'
ios_clean_df = transform_data(df_ios)[['date', 'text_cleaned', 'review', 'sentiment_values', 'rating']]
ios_clean_df['platform'] = 'ios'
clean_df = pd.concat([ard_clean_df, ios_clean_df], axis=0, ignore_index=True)

temp_old = clean_df[clean_df['date'] <= trunc_date_check_labeled]
temp_old = topic_modeling(temp_old)
temp_old['topic'] = temp_old['colmax'].apply(topic_mapping)

temp_new = clean_df[clean_df['date'] >= trunc_date_check_labeled]
logger.info(f"Checking dimension:  current_data: {len(temp_old)} \t this_month_db: {len(temp_new)} \t")

logger.info("# This step needed to manual-review")
temp_new = topic_modeling(temp_new) # update some new key-words
temp_new['topic'] = temp_new['colmax'].apply(topic_mapping)
temp_new.to_excel('temp_data/new_logs.xlsx', index=False)

logger.info("Stage 1 completed successfully!!!")
print("#====================================================================================#")