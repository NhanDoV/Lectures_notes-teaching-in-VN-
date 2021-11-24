import re
import nltk
import string
import warnings
import itertools
import datefinder
import numpy as np
import pandas as pd
import seaborn as sns
from nltk import bigrams
from datetime import datetime
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
from collections import defaultdict
from spellchecker import SpellChecker    
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

warnings.filterwarnings("ignore")
#nltk.download(['punkt', 'wordnet'])
sns.set_theme(style = "darkgrid", 
                  rc = {"axes.spines.right": False, "axes.spines.top": False})

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

# /=================================================================================================\
def view_word_freq(word_list, show_info = True):
    """
        -------------------------------------------------------------------------------------------------------
          This function is used to view the frequencies (count) of word in each documents and the whole dataset
        -------------------------------------------------------------------------------------------------------
          Parameters:
        ----------------------
              word_list (list): list of sentences
          Returns:
        ----------------------
              dataframe contain the column of word_vocabularies with the indexes be the sentences in "word_list".
          Note. 
        ----------------------
              To save the results as a parameter, the number of words and sentences in your sample must be reasonable        
        |======================================================================================================
        | Example.
        | >>> corpus = ['this is the first document',
        |               'this document is the second document',
        |               'and this is the third one',
        |               'is this the first document?',
        |               'this Document is not yours..'
        |              ]
        | >>> view_word_freq(corpus)
        |*====================================================================================================
        ||There are 5 sentences in this corpus.
        ||====================================================================================================
        |*The number of the different words is 11, and ... they are:
        ||====================================================================================================
        |*	 1: and,
        |*	 2: document,
        |*	 3: first,
        |*	 4: is,
        |*	 5: not,
        |*	 6: one,
        |*	 7: second,
        |*	 8: the,
        |*	 9: third,
        |*	 10: this,
        |*	 11: yours,
        |  	 			 	and	document	first	is	not	one	second	the	third	this	yours
        | this is the first document		0	1		1	1	0	0	0	1	0	1	0
        | this document is the second document	0	2		0	1	0	0	1	1	0	1	0
        | and this is the third one 	 	1	0		0	1	0	1	0	1	1	1	0
        | is this the first document?	 	0	1		1	1	0	0	0	1	0	1	0
        | this Document is not yours..	 	0	1		0	1	1	0	0	0	0	1	1
        |======================================================================================================
    """
    cvect = CountVectorizer()
    X = cvect.fit_transform(word_list)

    if show_info == 1:
        print("*{}\n|There are {} sentences in this corpus.\n|{}".format(100*"=", X.shape[0], 100*"="))
        print("|The number of the different words is {}, and ... they are:\n|{}".format(X.shape[1], 100*"="))
        for idx, word in enumerate(cvect.get_feature_names()):
            print("*\t {}: {},".format(idx + 1, word))

    else:
        pass
    return pd.DataFrame(data = X.toarray(),
                        columns = cvect.get_feature_names(),
                        index = word_list 
                        )

# /=================================================================================================\
def view_Tfidf(word_list):
    """
        -------------------------------------------------------------------------------------------------------
          This function is used to compute the Tfidf of each word-vocabulary from each sentence in the corpus.
        -------------------------------------------------------------------------------------------------------
          Parameters
              word_list : list of sentences.
        ----------------------
          Returns
              dataframe of text(sentences) as indexes and columns is the tfidf of word_vocabulary
        ----------------------
          See also:
              view_word_freq
        -------------------------------------------------------------------------------------------------------
    """
    cvect = CountVectorizer()
    X_cvect = cvect.fit_transform(word_list)
    X_tfidf = TfidfTransformer().fit_transform(X_cvect)
     
    return pd.DataFrame(data = X_tfidf.toarray(),
                        columns = cvect.get_feature_names(),
                        index = word_list 
                        )

# /=================================================================================================\
def textdata_to_countvect(data, text_column):
    """
        Parameters
        --------------------
            - data (dataframe)
            - text_column : the column contained text in your dataframe
        Returns
        --------------------
            - dataset of text and its count_vectorizer
        See also
        --------------------
            - view_word_freq(word_list)
    """
    corpus = data[text_column].values.tolist()
    countvec_df = view_word_freq(corpus, show_info = False).reset_index().rename(columns = {'index': text_column})
    
    return countvec_df

# /=================================================================================================\
def textdata_to_TFIDF(data, text_column):
    """
        Parameters
        --------------------
            - data (dataframe)
            - text_column : the column contained text in your dataframe
        Returns
        --------------------
            - dataset of text and its count_vectorizer
        See also
        --------------------
            - view_word_freq(word_list)
    """
    corpus = data[text_column].values.tolist()
    tfidf_df = view_Tfidf(corpus).reset_index().rename(columns = {'index': text_column})
    
    return tfidf_df

# /=================================================================================================\
def count_date(x):
    try:
        res=len(list(datefinder.find_dates( x )))
    except TypeError:
        pass
    else:
        return res
# /=================================================================================================\
def view_url_emoij_etc(data, text_col, emoji_lang = 'en'):
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
    # Extract emoji_icon_list
    import emoji
    emojis = [emj for emj, _ in emoji.UNICODE_EMOJI[emoji_lang].items()]        
    fs_emj = [":)", ":v", "=))", ":v", ":3", ":(", ":((", ":'("]
               
    # 1. word_count
    data['wcount'] = data[text_col].apply(lambda x: len(str(x).split()))

    # 2. unique_word_count
    data['unq_wcount'] = data[text_col].apply(lambda x: len(set(str(x).split())))

    # 3. stop_word_count
    data['stop_word_count'] = data[text_col].apply(lambda x: len([w for w in str(x).lower().split() if w in STOPWORDS]))

    # 4. url_count
    data['url_count'] = data[text_col].apply(lambda x: len([w for w in str(x).lower().split() 
                                                                    if 'http' in w 
                                                                        or 'https' in w
                                                                        or 'www' in w
                                                           ]))

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
    data['emoji_cnt'] = data[text_col].apply(lambda x: len([c for c in str(x).split() if c in emojis or c in fs_emj])) 
    
    # 12.count the capital-words
    data['capt_cnt'] = data[text_col].apply(lambda x: sum(1 for c in x if c.isupper()))
    
    # 13. count the email
    data['email_cnt'] = data[text_col].apply(lambda x: len(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", x) ))
    
    # 14. count the timestamps mentioned
    data['time_cnt'] = data[text_col].apply(lambda x: count_date(x) )
    
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
    
    return data

# /=================================================================================================\
def basic_clean_text(str_input, show_all = False):
    """
        This function used to clean the input_strings then return the list of words.
    """
    ## 1. Remove all the email
    emails = ''.join(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", str_input))
    rmv_str_input = str_input.replace(emails, "")
    date_list = list(datefinder.find_dates(rmv_str_input))
    if len(date_list) > 0:
        date_list = date_list[0].strftime("%d/%m/%Y")
        rmv_str_input = rmv_str_input.replace(date_list, rmv_str_input)
    else:
        date_list = date_list
    
    ## 2. Remove url_link
    url_list = ''.join(re.findall(r'https?://\S+|www\.\S+', rmv_str_input))
    remove_url = re.compile(r'https?://\S+|www\.\S+').sub(r'', rmv_str_input)
    
    ## 3. Remove html_link
    remove_html = re.compile(r'<.*?>').sub(r'', remove_url)
            
    ## 4. Remove Emojis
    remove_emo = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE).sub(r'', remove_html)
    
    words = re.sub(r"[^A-Za-z0-9\-]", " ", remove_emo).lower().split()    
            
    ## 5. spell_correction & drop punctuation
    spell = SpellChecker()
    words = [spell.correction(word) for word in words if word not in string.punctuation]    
    if show_all == 1:
        print("{}\nInitial input strings: '{}'.\n{}\nWord-list fter cleansing: '{}\n{}'".format(120*"=", str_input, 
                                                                                        120*"=", words, 
                                                                                        120*"="))
        print("Email detected: {}\n{}\nurl_link detected: {}\n{}\nThe first timestamp detected: {}\n{}".format(emails, 120*"=", 
                                                                                                     url_list, 120*"=",
                                                                                                     date_list, 120*"="
                                                                                                    ))
    else:
        pass;
        
    return words

# /=================================================================================================\
def generate_ngrams(text, n_gram = 1):
    """
        This function create the word_list as N-grams in your input_text
        --------------------------
        Parameters:
        --------------------------
            - text (str): input strings
            - ngram (int) must be 1 (unigram), 2(bi-grams), 3(tri-grams)
        Example
        --------------------------
        >>> init_text = "\U0001F600-\U0001F64F heallo, haev a godo jbo, todyao is 29Jun2021 !PlesAe Visit https://google.com.vn and contact abc2083181@yahoo.com"
            ['😀-🙏',
             'heallo,',
             'haev',
             'godo',
             'jbo,',
             'todyao',
             '29jun2021',
             '!plesae',
             'visit',
             'https://google.com.vn',
             'contact',
             'abc2083181@yahoo.com']
    """
    token = [token for token in text.lower().split(' ') if token != '' if token not in STOPWORDS]
    ngrams = zip(*[token[i:] for i in range(n_gram)])
    return [' '.join(ngram) for ngram in ngrams]

# /=================================================================================================\
def get_N_grams(data, text_col, target_col, positive_value, n_gram):
    """
        This function returns 2 datasets of N_grams
            - The first one contain the positive value meaning from the target-column
            - The last one .............negative
        Parameters
        ---------------------------
            - data (dataframe)
            - target_col : the target column
            - positive_value : the value in the target column that had a positive-meaning
            - n_gram (int)
    """     
    mask = (data[target_col] == positive_value)
    positive_N_grams = defaultdict(int)
    negative_N_grams = defaultdict(int)

    for text in data[mask][text_col]:
        for word in generate_ngrams(text, n_gram=n_gram):
            positive_N_grams[word] += 1

    for text in data[~mask][text_col]:
        for word in generate_ngrams(text, n_gram=n_gram):
            negative_N_grams[word] += 1

    df_positive_N_grams = pd.DataFrame(sorted(positive_N_grams.items(), key=lambda x: x[1])[::-1])
    df_negative_N_grams = pd.DataFrame(sorted(negative_N_grams.items(), key=lambda x: x[1])[::-1])
    
    return df_positive_N_grams, df_negative_N_grams

# /=================================================================================================\
def N_grams_data_show(data, text_col, target_col, positive_value, n_gram, topN_words):
    """
        Show the comparison of N-grams on the binary-group of text-classification
    """
    if n_gram == 1:
        n_gr_vl = "unigram"
    elif n_gram == 2:
        n_gr_vl = "bigram"
    elif n_gram == 3:
        n_gr_vl = "trigram"
    else:
        ValueError("the number of N-grams must be in [1, 2, 3]!!...")
        
    df_positive_N_grams, df_negative_N_grams = get_N_grams(data, text_col, target_col, positive_value, n_gram)
    
    fig, axes = plt.subplots(ncols=2, figsize=(18, 2*topN_words//5), dpi=100)
    plt.tight_layout()

    sns.barplot(y = df_positive_N_grams[0].values[: topN_words], 
                x = df_positive_N_grams[1].values[: topN_words], 
                ax = axes[0], 
                color="MediumBlue"#"Blues_d"
               )
    sns.barplot(y = df_negative_N_grams[0].values[: topN_words], 
                x = df_negative_N_grams[1].values[: topN_words], 
                ax = axes[1], 
                color="SpringGreen")

    for i in range(2):
        axes[i].spines['right'].set_visible(False)
        axes[i].set_xlabel('count')
        axes[i].set_ylabel('')
        axes[i].tick_params(axis='x', labelsize=10)
        axes[i].tick_params(axis='y', labelsize=10)
        for p in axes[i].patches:
            cnt = p.get_width()
            cnt = np.where(np.isnan(cnt), 0, cnt) 
            axes[i].annotate(cnt, 
                             xy = (int(p.get_width() * 2/3) + 0.5, p.get_y() + p.get_height() / 2),
                             color = 'white',
                             bbox = dict(boxstyle = 'round,pad=0.3',
                                        fc = 'violet', 
                                        alpha=0.3
                                       ),
                             size = 10
                            )

    axes[0].set_title(f'Top {topN_words} {positive_value} most common.{n_gr_vl}', fontsize=11)
    axes[1].set_title(f'Top {topN_words} non-{positive_value} most common.{n_gr_vl}', fontsize=11)

    plt.show()
    
# /=================================================================================================\
def generate_co_occurrence_matrix(corpus):
    """
        This function is used to generate the co-occurence matrix
        **************************
        Definition.
        --------------------------
             - Co-occurrence matrix, is a symmetric square matrix, each row or column will be the vector representing 
            the corresponding word; it is measuring co-occurrences of features within a user-defined context.

             - The context can be defined as a document or a window within a collection of documents, with an optional 
            vector of weights applied to the co-occurrence counts.
                
        **************************
        See also
        ---------------------------
            - Co-occurrence matrix
            - A context window
    """
    vocab = set(corpus)
    vocab = list(vocab)
    vocab_index = {word: i for i, word in enumerate(vocab)}
 
    # Create bigrams from all words in corpus
    bi_grams = list(bigrams(corpus))
 
    # Frequency distribution of bigrams ((word1, word2), num_occurrences)
    bigram_freq = nltk.FreqDist(bi_grams).most_common(len(bi_grams))
 
    # Initialise co-occurrence matrix
    # co_occurrence_matrix[current][previous]
    co_occurrence_matrix = np.zeros((len(vocab), len(vocab)))
 
    # Loop through the bigrams taking the current and previous word,
    # and the number of occurrences of the bigram.
    for bigram in bigram_freq:
        
        current = bigram[0][1]   # row 1 ([0]); col 2 ([1]) of the first set in the 2D-set
        previous = bigram[0][0]  # row 1, col 1

        # the values in the 2nd set
        count = bigram[1]        
        
        # get position
        pos_current = vocab_index[current]  
        pos_previous = vocab_index[previous]
        
        # put the value into the matrix
        co_occurrence_matrix[pos_current][pos_previous] = count
    
    # create matrix
    co_occurrence_matrix = np.matrix(co_occurrence_matrix)
    
    return co_occurrence_matrix, vocab_index

# /=================================================================================================\
def get_co_occurence_matrix(list_words):
    """
        This function is used to create the co-occurence matrix from the list of words
    """
    lst_of_lst_words = [basic_clean_text(text) for text in list_words]
    
    # List-itertool
    draft_data = list(itertools.chain.from_iterable(lst_of_lst_words))
    matrix, vocab_index = generate_co_occurrence_matrix(draft_data)

    data_matrix = pd.DataFrame(data = matrix, 
                               index = vocab_index,
                               columns = vocab_index)
    return data_matrix

# /=================================================================================================\
def metafeature_view(data, text_col, clf_col, obs_val = 'real_spam'):
    """
    
    """
    encode_data = view_url_emoij_etc(data, text_col)
    METAFEATURES = list(encode_data.columns[-16:])

    DISASTER_TWEETS = encode_data[clf_col] ==  obs_val
    n_rows = len(METAFEATURES) + 1
    fig, axes = plt.subplots(ncols=2, nrows=n_rows, figsize=(20, int(n_rows*3.75)), dpi=100)
    for i, feature in enumerate(METAFEATURES):
        n_distinct = len(encode_data[feature].unique())
        if n_distinct > 25:
            sns.distplot(encode_data.loc[~DISASTER_TWEETS][feature], label='Non-spam', ax=axes[i][0], color='green')
            sns.distplot(encode_data.loc[DISASTER_TWEETS][feature], label='Real-spam', ax=axes[i][0], color='red')            
            sns.boxplot(y = feature, x = 'target', data = encode_data, 
                         palette="Set3", ax=axes[i][1])
            axes[i][0].legend()    

        else:
            sns.countplot(hue=clf_col, x = feature, data=encode_data, 
                          palette="Set3", ax=axes[i][0]);
            sns.boxplot(y = feature, x = 'target', data = encode_data, 
                         palette="Set3", ax=axes[i][1])
        
        for j in range(2):
            axes[i][j].set_xlabel('')
            axes[i][j].tick_params(axis='x', labelsize=10)
            axes[i][j].tick_params(axis='y', labelsize=10)
            if j == 0:
                axes[i][j].set_title(f'{feature}-distribution in Training Set', fontsize=11)
            else:
                axes[i][j].set_title(f'{feature}-boxplot in Training Set', fontsize=11)
    labels = encode_data.groupby(clf_col).count()[feature].index
    sizes = list(encode_data.groupby(clf_col).count()[feature].values)
    axes[n_rows-1][0].pie(sizes, explode = (0, 0.1), 
                          labels = labels, autopct = '%1.1f%%',
                          shadow = True, startangle = 90)
    sns.countplot(x = clf_col, data = encode_data, ax = axes[n_rows-1][1])
    
    plt.show()
    
# /=================================================================================================\
def col_view(tweet, cate_col = 'keyword', target_col = 'target'):
    """
    
    """
    fig = plt.figure(figsize=(8, 60), dpi=100)
    tweet['target_mean'] = tweet.groupby(target_col)[cate_col].transform('count')
    sns.countplot(y = tweet.sort_values(by = 'target_mean', ascending = False)[cate_col],
                  hue = tweet.sort_values(by = 'target_mean', ascending = False)[target_col])

    plt .tick_params(axis = 'x', labelsize = 12)
    plt.tick_params(axis = 'y', labelsize = 10)
    plt.legend(loc=1)
    plt.title('Target Distribution in {}'.format(cate_col))
    plt.show()

# /=================================================================================================\
def advanced_view(data, text_col, clf_col):
    """
    
    """
    fig, ax = plt.subplots(1, 1, figsize = (20, 10))
    
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    
    encode_data = view_url_emoij_etc(data, text_col)
    METAFEATURES = list(encode_data.columns[-16:]) 
    str_cols = encode_data.drop(columns = [text_col, clf_col]).columns[encode_data.drop(columns = [text_col, clf_col]).dtypes == 'object']
    n_rows = len(str_cols)
    df = encode_data.copy()
    df[clf_col] = le.fit_transform(df[clf_col])
    df = df[[clf_col] + METAFEATURES]
    sns.heatmap(df.corr(), annot=True, ax = ax)
    plt.show()
    
# /=================================================================================================\
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# /=================================================================================================\
def NLP_get_pca_data(data, id_col, text_col, target_col, n_pc = 200):
    """
    
    """
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import PCA, TruncatedSVD
    
    tfidf_vect = TfidfVectorizer(tokenizer = tokenize)
    y = data[[id_col, target_col]]

    pca = TruncatedSVD(n_pc)
    
    tfidf_X = tfidf_vect.fit(data[text_col]).transform(data[text_col])
    pca.fit_transform(tfidf_X)
    
    X_pca = pd.DataFrame(data = pca.fit_transform(tfidf_X),
                         columns = ['PC_{}'.format(k) for k in range(n_pc)]
                        )
    
    print(X_pca.shape, pca.explained_variance_ratio_.sum())
    
    return pd.concat([y, X_pca], axis = 1)

# /=================================================================================================\
from tensorflow import keras
from tensorflow.keras import layers
from keras import layers
from keras.models import Sequential
from keras.layers import Flatten
from keras.layers import Dense, Dropout, Activation, Conv1D, GlobalMaxPooling1D, MaxPooling1D, GlobalAveragePooling1D
from keras.layers.embeddings import Embedding
from keras.preprocessing.text import one_hot
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.callbacks import ModelCheckpoint, EarlyStopping

def load_word_embedding(data, text_col, clf_col, vocab_size, max_length):
    
    
    y = data[clf_col]
    encoded_docs = [one_hot(d, vocab_size) for d in list(data[text_col])]
    padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')

    x_train, x_test, y_train, y_test = train_test_split(padded_docs, y, test_size = 0.3, 
                                                        stratify = y, random_state = 42)
    
    return vocab_size, max_length, x_train, x_test, y_train, y_test

# /=================================================================================================\
def word_embedding_CNN(vocab_size, max_length, x_train, x_test, y_train, y_test, saved_path,  epochs = 10, batch_size = 32, verbose = 2):
    """
    """
    # = load_word_embedding(data, text_col, clf_col, vocab_size, max_length) 
    model = Sequential()
    model.add(Embedding(vocab_size, 128, input_length=max_length))
    model.add(GlobalAveragePooling1D())
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['acc'])
    print(model.summary())
    
    checkpointer = ModelCheckpoint(filepath = saved_path, 
                                   verbose = 1, save_best_only = True)
    history = model.fit(x_train, y_train, 
                        epochs = epochs, batch_size = batch_size,
                        callbacks = [checkpointer],
                        verbose = verbose, validation_data = (x_test, y_test))
    
    return model, history

# /=================================================================================================\
def WEmbedding_plot(history):
    """
    
    """
    
    fig, ax1 = plt.subplots(2,1,figsize = (20, 7))
    def plot_type(ax, history, ptype = 'loss'):
        ax1 = ax
        color = 'tab:red'
        ax1.set_xlabel('n_epochs')
        ax1.set_ylabel('train_{}'.format(ptype), color=color)
        y = history.history[ptype]
        x = [1+k for k in range(len(y))]
        ax1.plot(x, y, color=color)
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.set_title("train_{} and val_{} on Embedding model via each epoch".format(ptype, ptype))
        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

        color = 'tab:green'
        ax2.set_ylabel("val_{}".format(ptype), color=color)  # we already handled the x-label with ax1
        z = history.history["val_{}".format(ptype)]
        ax2.plot(x, z, color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()  # otherwise the right y-label is slightly clipped

    plot_type(ax1[0], history, ptype = 'loss')
    plot_type(ax1[1], history, ptype = 'acc')
    
# /=================================================================================================\
from sklearn.metrics import classification_report, precision_score, recall_score, roc_auc_score, f1_score, log_loss

def WEmbedding_acc(model, history, x_test, y_test, cls0_name = 'no-spam', cls1_name = 'spam'):
    """

    """

    clf_names = [cls0_name, cls1_name]    
    y_pred = [0 if t < 0.5 else 1 for t in model.predict(x_test).ravel()]

    print(classification_report(y_test, y_pred,  digits=4, target_names = clf_names)) 

    return pd.DataFrame({
                          'ROC_AUC': roc_auc_score(y_test, y_pred),
                          'accuracy': (y_pred == y_test).sum() / len(y_test),
                          'f1_score': [{clf_names[k] : round(f1_score(y_test, y_pred, average=None)[k], 4) for k in range(2)}],
                          'precison': [{clf_names[k] : round(precision_score(y_test, y_pred, average = None)[k], 4) for k in range(2)}],
                          'recall': [{clf_names[k] : round(recall_score(y_test, y_pred, average = None)[k], 4) for k in range(2)}],
                          'log_loss(cross-entropy)': min(history.history["val_loss"]),
                          'n_features': x_test.shape[1],
                          'best_param': str(model.to_json())
                         },
                            index = ['avg_score_k_split']
                        )

# /=================================================================================================\
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense, Dropout, LSTM, Bidirectional
def LSTM_model(x_train, y_train, x_test, y_test, n_lstm, vocab_size, max_length, saved_path, epochs = 10, batch_size = 32, verbose = 2):
    """
    
    """
    lstm_model = Sequential()
    lstm_model.add(Embedding(vocab_size, 128, input_length=max_length))
    lstm_model.add(LSTM(n_lstm, dropout=0.1, return_sequences=True))
    lstm_model.add(LSTM(n_lstm, dropout=0.1, return_sequences=True))
    lstm_model.add(Flatten())
    lstm_model.add(Dense(1, activation='sigmoid'))


    lstm_model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics=['acc'])
    
    print(lstm_model.summary())

    checkpointer = EarlyStopping(monitor='val_loss', patience=3)
    
    lstm_history = lstm_model.fit(x_train, y_train, 
                                    epochs = epochs, batch_size = batch_size,
                                    callbacks = [checkpointer],
                                    verbose = verbose, validation_data = (x_test, y_test))
    
    return lstm_model, lstm_history

# /=================================================================================================\
def Bi_LSTM(x_train, y_train, x_test, y_test, n_lstm, vocab_size, max_length, saved_path, epochs = 10, batch_size = 32, verbose = 2):
    """
    
    """
    bi_LSTM_model = Sequential()
    bi_LSTM_model.add(Embedding(vocab_size, 128, input_length=max_length))
    bi_LSTM_model.add(Bidirectional(LSTM(n_lstm, dropout=0.1, return_sequences=True)))
    bi_LSTM_model.add(Dropout(0.1))
    bi_LSTM_model.add(Flatten())
    bi_LSTM_model.add(Dense(1, activation='sigmoid'))
    
    bi_LSTM_model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics=['acc'])
    
    checkpointer = EarlyStopping(monitor='val_loss', patience=3)
    
    bi_LSTM_history = bi_LSTM_model.fit(x_train, y_train, 
                                        epochs = epochs, batch_size = batch_size,
                                        callbacks = [checkpointer],
                                        verbose = verbose, validation_data = (x_test, y_test))
    
    return bi_LSTM_model, bi_LSTM_history