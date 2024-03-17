import re
import string
import numpy as np
from wordcloud import STOPWORDS

def text_pre_processing(text):
    # Remove all stopwords
    text = re.compile(r'\b(' + r'|'.join(STOPWORDS) + r')\b\s*').sub(r'', text.lower())
    ## 1. Remove url_link & html
    remove_url = re.compile(r'https?://\S+|www\.\S+').sub(r'', text)
    remove_html = re.compile(r'<.*?>').sub(r'', remove_url)
    ## 2. Remove digits, tabs, new-lines
    remove_html = re.compile(r'[0-9]|\t|\n').sub(r'', remove_html)    
    ## 3. Remove Emojis
    remove_emo = re.compile(r'\d+(.*?)[\u263a-\U0001f645]').sub(r'', remove_html)
    words = re.sub(r"[^A-Za-z0-9\-]", " ", remove_emo).lower().split()    
    return ' '.join(words)

def regex_transform(data, text_col):
    """
        ===================================================================================================
        Parameters:
        -----------------
            - data (dataframe)
            - text_col : column that contained text-data to analysis
            - emoji_lang : choose the language to count the emoji in, default = "en" (ENG).
        See also:
        -----------------
            Python
                - wordcloud vs STOPWORDS
                - datefinder : https://pypi.org/project/datefinder/
                - re
                - string
                - emoji      : https://pypi.org/project/emoji/
        Returns
        -----------------
            This function is used to check the following table:
                ===================================================================================================
                *------------------------------------------------------------------------------------------*
                | Cases                                                | Examples (discriptions)           | 
                *------------------------------------------------------|-----------------------------------* 
                | number of hastags                                    | #memories                         |
                *------------------------------------------------------------------------------------------*
                | number of url_link and unique url in email, messages | http//:google.com                 |
                | or tweets / etc                                      | www.google.com                    |
                *------------------------------------------------------------------------------------------*
                | mention someone else`                                | @David                            |
                *------------------------------------------------------------------------------------------*
                | hour of day / day of week / or any mentioned-        | 2020-12-12                        |
                | timestamp when the email` or messages / tweets       | 21 Jun 2020                       |
                | was send / posted`                                   | etc                               |
                *------------------------------------------------------------------------------------------*
                | number of emojicon                                   | ":)", ":v", "=))", etc            |
                |                                                      | "\U000024C2-\U0001F251", etc                      
                *------------------------------------------------------------------------------------------*
                | number of capitalized words`                         | AbBa MoHameD                      |
                *------------------------------------------------------------------------------------------*
                | sum of all the character-lengths of word`            | len(word_splited)                 |
                *------------------------------------------------------------------------------------------*
                | number of words containing letters and numbers       | "128abc9*", "29Jun1998", etc.     |
                *------------------------------------------------------------------------------------------*
                | number of words containing only numbers or letters   | "12300 people...", etc.           |             
                *------------------------------------------------------------------------------------------*
                | max ratio of digit characters to all characters of   | max([len`(digit(word))            |
                | each word                                            |  / len(word) for word in words])  |
                *------------------------------------------------------------------------------------------*
                | max the charecter-lengths of all words.              | max([len(word) for word in words])|
                *------------------------------------------------------------------------------------------*
                | number of words in email, messages or tweets / etc.  | len(word.split())                 |
                *------------------------------------------------------------------------------------------*
                | max length of word                                   | max([len(w) for w in words])      |
                *------------------------------------------------------------------------------------------*
                | average length of word                               | mean([len(w) for w in words])     |
                *------------------------------------------------------------------------------------------*
                | number of punctuation                                |                                   | 
                *------------------------------------------------------------------------------------------*
    """      
    fs_emj = [":)", ":v", "=))", ":v", ":3", ":(", ":((", ":'("]          
    # 1. word_count
    data['wcount'] = data[text_col].apply(lambda x: len(str(x).split()))
    # 2. unique_word_count
    data['unq_wcount'] = data[text_col].apply(lambda x: len(set(str(x).split())))
    # 3. stop_word_count
    data['stop_word_count'] = data[text_col].apply(lambda x: len([w for w in str(x).lower().split() if w in STOPWORDS]))
    # 4. url_count
    data['url_count'] = data[text_col].apply(lambda x: len(re.findall(r"https|www|http", x)))
    # 5. average_word_length
    data['avg_wlen'] = data[text_col].apply(lambda x: np.mean([len(w) for w in str(x).split()]))
    # 6. char_count
    data['char_count'] = data[text_col].apply(lambda x: len(str(x)))
    # 7. punctuation_count
    punctuations = string.punctuation
    data['punct_count'] = data[text_col].apply(lambda x: len([c for c in str(x) if c in punctuations]))
    # 8. hashtag_count
    data['hastg_count'] = data[text_col].apply(lambda x: len([c for c in str(x) if c == '#']))
    # 9. mention_count
    data['mentn_count'] = data[text_col].apply(lambda x: len([c for c in str(x) if c == '@']))
    # 10. max length of word
    data['max_wlen'] = data[text_col].apply(lambda x: max([len(w) for w in str(x).split()]))
    # 11. count emoji
    data['emoji_cnt'] = data[text_col].apply(lambda x: len([c for c in str(x).split() if c in fs_emj]))
    data['emoji_cnt'] = data['emoji_cnt'] + data[text_col].apply(lambda x: len(re.compile(r'\d+(.*?)[\u263a-\U0001f645]').findall(x)))
    # 12.count the capital-words
    data['capt_cnt'] = data[text_col].apply(lambda x: sum(1 for c in x if c.isupper()))
    # 13. count the email
    data['email_cnt'] = data[text_col].apply(lambda x: len(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", x) ))
    # 15. count digits+characters
    data['char&num_cnt'] = data[text_col].apply(lambda x: len(re.findall(r"([A-Za-z]+[\d@]+[\w@]*|[\d@]+[A-Za-z]+[\w@]*)", x) )) - data['mentn_count']
    # 16. max ratio digits of word in each text
    data['max_digit_rate'] = data[text_col].apply(lambda x: max([len(re.findall(r"[0-9]", word) ) / 
                                                                 abs(len(word) - len(re.findall(r"[0-9]", word)))
                                                                    if 
                                                                         len(word) - len(re.findall(r"[0-9]", word)) != 0
                                                                    else 
                                                                         len(re.findall(r"[0-9]", word) ) 
                                                                for word in x
                                                                ])
                                                 )
    data['tab_newlines'] = data[text_col].apply(lambda x: len(re.findall(r"\t|\n", x)))
    return data