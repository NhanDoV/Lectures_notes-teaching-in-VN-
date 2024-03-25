## 1. Enhancing any specific pattern
If you want to enhance your text-input by any specificed pattern (like the hastag, url-link, number of emails or mobile, etc), 

| description | syntax (pattern) | regex.function | 
|-|-|-|
|find word starts with `x`|`r"^x"`|`re.findall(patt, test_string.lower())`|
|find word ended with `x` | `r"x$"` | `re.findall(patt, test_string.lower())`|
|matched a character `w` 3-5 times | `r"w{3,5}"` | `re.findall(patt, test_string.lower())`|
|matched these character `w, t, s` 3-5 times | `r"[wts]{3,5}"` | `re.findall(patt, test_string.lower())`|
|matched any digits more than 2 times | `r"\d{2,}"` | `re.findall(patt, test_string.lower())`|
|matched any words has at-least `digit` or `character`| `r"[A-Za-z0-9]+"` | 
|matched any words has all-characters are `uppercase` | `r"\b(?:[a-z]*[A-Z]){2}[a-zA-Z]*\b"` |
|matched if any words contained digits| `r"\d{1,}"`|
|matched if any string is non-digit | `r"\D{1,}"` |
|matched if `whitespace` | `r"\s{1,}"` |
|matched if `non-whitespace` | `r"\S{1,}"` |

### Reference
- [code](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/blob/master/Python%20Data%20Science%20Toolbox/All-of-AI-notes/NLP/some_cases_regex.py)
- [notebook](https://github.com/NhanDoV/Hackerank-test/blob/main/Mathematics/Regex_string/matching.ipynb)

## 2. CountVect-Tfidf-Ngrams-GloVec-WordEmb
### 2.1. CountVectorizer vs Tfidf
#### 2.1.1. CountVectorizer (Bag-of-words)
- This model converts text into fixed-length vectors by counting how many times each word appears.

```
      from sklearn.feature_extraction.text import CountVectorizer
      corpus = {} # your input list of sentences
      vectorizer = CountVectorizer(analyzer = 'word',
                                    ngram_range = (2, 2))
      X = vectorizer.fit_transform(corpus)
```

![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/9d9a3209-241d-4717-adeb-4c6facb253e3)

**Pros**
- Easy to implement
 
**Cons**
- Large documents may generate sparse vectors due to large sizes and excessive null values.
- Bag-of-words does not provide text meaning information, e.g, a sentence with different meanings might have the same vectors.

#### 2.1.2. Tfidf
`TFIDF` works by proportionally increasing the number of times a word appears in the document but is counterbalanced by the number of documents in which it is present. 
- Hence, words like ‘this’, ’are’ etc., that are commonly present in all the documents are not given a very high rank.
- However, a word that is present too many times in a few of the documents will be given a higher rank as it might be indicative of the context of the document.

```
      from sklearn.feature_extraction.text import TfidfVectorizer
      corpus = {} # your input list of sentences
      vectorizer = TfidfVectorizer(analyzer = 'word',
                                    ngram_range = (2, 2))
      X = vectorizer.fit_transform(corpus)
```

**Pros**
- Based on the product of `Term Frequency` and `Inverse Document Frequency` hence some words are zero and some words are non-zero depending on their frequency in the document and across all documents.

![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/6f72d15c-ab50-4f9d-9281-9c5587a69f4d)
  
**Cons**
- Doesn't incorporate contextual meaning.
- Based on frequency, not contextual.

#### 2.1.3. Ngrams
- `N-grams` are continuous sequences of words or symbols, or tokens in a document. In technical terms, they can be defined as the neighboring sequences of items in a document.
- For example in the sentence `I go to school` and `N-grams=2` we obtains `I go, go to, to school`

```
      from nltk.util import ngrams
      bigrams = ngrams(input_sentence.split(), 2)
```

**Pros**
- Useful for file type identification and text mining.
- N-gram analysis allows for the conversion of free text into numerical variables for statistical analysis.

**Cons**
- Computational resource demands and time consumption.
- Difficulty with larger n-gram datasets.
- Scalability issues with certain classifiers like `SVMs`.

#### 2.1.4. Important-params for both cases
- `max_features`: This parameter enables using only the `‘n’` most frequent words as features instead of all the words. An integer can be passed for this parameter.
- `stop_words`: You could remove the extremely common words like `‘this’, ’is’, ’are’` etc by using this parameter as the common words add little value to the model. We can set the parameter to `‘english’` to use a built-in list. We can also set this parameter to a custom list.
- `analyzer`: This parameter tells the model if the feature should be made of word `n-grams` or character `n-grams`. We can set it to be `‘word’`, `‘char’` or `‘char_wb’`. Option `‘char_wb’` creates character `n-grams` only from text inside word boundaries.
- `ngram_range`: An n-gram is a string of words in a row. We can set the ngram_range to be `(x,y)` where `x` is the minimum and `y` is the maximum size of the `n-grams` we want to include in the features. The default ngram_range is `(1,1)`.
- `min_df, max_df`: These refer to the minimum and maximum document frequency that a word/n-gram should have to be used as a feature. The frequency here refers to the proportion of documents. Both the parameters have to be set in the range of [0,1].
  
### 2.2. GloVec vs Word-Embedding
### 2.2.1. Word2Vec
- `Word2vec` is a technique in `NLP` for obtaining **vector representations of words**. These vectors capture information about the meaning of the word based on the surrounding words.
- Techique behinds: `Skip-grams` and `CBOW (Continuous Bag of Words)`

```
      from gensim.models import Word2Vec
      import gensim
      from nltk.tokenize import sent_tokenize, word_tokenize
      import warnings
      
      # Create CBOW model
      model1 = gensim.models.Word2Vec(data, min_count=1,
                                      vector_size=100, window=5)
      # Create Skip Gram model
      model2 = gensim.models.Word2Vec(data, min_count=1, vector_size=100,
                                      window=5, sg=1)    
```
  
**Pros**
- Improved performance compared to traditional bag-of-words features .
- Ability to learn from unlabeled data and reduce the dimension of the feature space .
- Better representation of specialized words in clinical text .
- Superior performance for medium-sized cohorts when using pre-trained domain-related embeddings .
- Potential for clinicians and healthcare workers to incorporate clinical text features in their own models and applications .

**Cons**
- Scaling to new languages requires new embedding matrices
- Inability to handle unknown or `OOV (Out-of-vocabulary) words`
- No shared representations at sub-word levels

### 2.2.2. GloVec
- `GloVe` is an unsupervised learning algorithm for obtaining vector representations for words.
- Training is performed on aggregated global word-word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space.

```
      from tensorflow.keras.preprocessing.text import Tokenizer
      
      text_dict = {'text', 'the', 'leader', 'prime', 'natural', 'language'}
      tokenizer = Tokenizer()
      tokenizer.fit_on_texts(text_dict)
      # matrix for vocab: word_index 50 dimensions
      embedding_dim = 50
      embedding_matrix_vocab = embedding_for_vocab(
                                                  '../glove.6B.50d.txt', tokenizer.word_index,
                                                   embedding_dim)
```

**Pros**
- Adds practical meaning to word vectors by considering word pair relationships.
- Enforces word vectors to capture sub-linear relationships in vector space.

**Cons**
- `GloVe word embeddings` have limitations in considering the order of words within their contexts . This lack of consideration for word order can affect the performance of GloVe on certain natural language tasks such as analogy completion and word similarity. 
- Additionally, the word pairs used in GloVe are extracted from a predefined local `context window`, which may result in limited and potentially semantically irrelevant word pairs . This limitation can impact the quality of the learned word embeddings.
- Furthermore, GloVe has been found to exhibit biases related to `gender`, `race`, and `religion`. These biases can be problematic in various applications.

### 2.2.3. FasText
- `FastText` is an extension of the Word to VEC framework that addresses the limitations associated with languages that have complex morphological structures.
- In `FastText`, words are broken down into their constituent character engrams, such as trigrams, four-grams, and five-grams. By utilizing these subword units, FastText is able to create vectors that capture the similarities and relationships within a word's morphological family.

In `Python`

```
      !pip install fasttext
      ------------------------------------
      import fasttext
      # Skipgram model :
      model = fasttext.train_unsupervised('data.txt', model='skipgram')
      
      # or, cbow model :
      model = fasttext.train_unsupervised('data.txt', model='cbow')
```

**Pros**
- `Capturing Morphological Similarities`: By breaking words into subword units, FastText captures the similarities and variations within a `word's morphological family`. This helps machines understand the shared properties and meanings of related words.
- `Enhanced Embeddings for Morphologically Rich Languages`: `FastText` greatly benefits languages with extensive morphological inflections, as it accounts for the forms and variations within words. This makes it suitable for a wide range of languages, including Finnish, Turkish, Arabic, and many Indian languages.

**Cons**
- `Increased Computational Complexity`: The inclusion of character-level information and subword units increases computational complexity compared to standard `Word2VEC` models. This can impact training and processing times, especially for larger Corpora.
- `Limited Application to Languages with Simplified Morphological Structures`: FastText's subword approach may provide less benefit for languages with simplified morphological structures, such as English. In such cases, simpler word embedding models may be more efficient.

### Reference
- [code](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/blob/master/Python%20Data%20Science%20Toolbox/All-of-AI-notes/NLP/some_cases_regex.py)
- [Word2Vec](https://aylien.com/blog/word-embeddings-and-their-challenges)
- [FastText](https://www.toolify.ai/gpts/exploring-word2vec-glove-and-fasttext-124900)

## 3. 