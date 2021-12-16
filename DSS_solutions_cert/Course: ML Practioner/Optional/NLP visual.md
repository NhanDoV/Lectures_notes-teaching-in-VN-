## Theory
[link]()

## Practices
### Quiz 1: Introduction to NLP.
``` diff
@@ Question 1. In NLP, what does it mean to treat the text as a “bag of words”?@@
```
- [x] **You divide the words in a text, ignoring grammar and word order, so the words can be counted or weighted.**
- [ ] You divide the words in a text, but maintain grammar and word order, before counting or weighting the words.
- [ ] None of these answers are correct.
- [ ] The “bag” here refers to the application of bootstrap aggregation (or bagging) to NLP models.

``` diff
@@ Question 2. Which of the following types of machine learning tasks best describes an effort to determine the main topics of discussion within a corpus of text when no topics are known?@@
```
- [ ] Multiclass classification
- [ ] Binary classification
- [x] **Clustering**
- [ ] Regression.

``` diff
@@ Question 3. The most advanced NLP use case is a binary classification task.@@
```
- [x] **False. Many kinds of machine learning tasks are possible within the domain of NLP, including clustering problems, for example.**
- [ ] True. Human language is too complex for more advanced use cases.

### Quiz 2. Preparing Text Data.
``` diff
@@ Question 1. In order to treat the words “apple” and “apples” as a single feature, which of the following steps would you apply?@@
```
- [ ] None of these.
- [ ] Text normalization
- [x] **Stemming**
- [ ] Stopwords removal

``` diff
@@ Question 2. Which of the following is NOT a consequence of normalizing a text?@@
```
- [ ] Punctuation is removed.
- [x] **Prefixes and suffixes of words are removed.**
- [ ] The case of all characters is now the same.
- [ ] Accents marks are removed.

``` diff
@@ Question 3. In order to remove punctuation from a column of text in Dataiku DSS, which of the following steps would you apply?@@
```
- [ ] Stemming
- [x] **Text normalization**
- [ ] Stopwords removal
- [ ] None of these.

### Quiz 3. Handling text features for ML.
``` diff
@@ Question 1. Which of the following text handling methods only creates an occurrence matrix for each word in the text column?@@
```
- [ ] TF-IDF vectorization
- [x] **Count vectorization**
- [ ] Term hashing + SVD (Tokenize, hash and apply SVD)
- [ ] Term hashing (Tokenize and hash)

``` diff
@@ Question 2. Fill in the blanks: When selecting features for a model, Dataiku DSS _________ text columns by default because they are ______ expensive in terms of memory.@@
```
- [ ] rejects; less
- [ ] includes; less
- [ ] includes; more
- [x]** rejects; more**

``` diff
@@ Question 3. When applying the “Tokenize and hash” method, each new hash column (or feature) represents an individual word.@@
```
- [ ] True. This makes term hashing a highly interpretable method.
- [x] **False. New features represent individual words only when you apply vectorization methods.**

### Final quiz
``` diff
@@ Question 1. Which of the following is generally the most scalable, but the least interpretable option for handling text features for ML? @@
```
- [ ] Count vectorization
- [x] Term hashing (Tokenize and hash) + SVD
- [ ] TF-IDF vectorization
- [ ] Term hashing (Tokenize and hash)

``` diff
@@ Question 2. When applying the “Tokenize, hash and apply SVD” method, which setting determines the number of final features to be derived from the text column?@@
```
- [ ] SVD limit
- [ ] Hash columns
- [ ] None of these
- [x] SVD components

``` diff
@@ Question 3. Why would it be a problem to have the words “apple” and “apples” treated as separate features? Select all that apply.@@
```
- [x] Increased computational burden
- [ ] For most use cases, it would actually be preferable to keep them separate.
- [x] Less concentrated information
- [x] Sparser features

``` diff
@@ Question 4. Using which of the following processors is it possible to create numeric features from natural language data? Select all that apply.@@
```
- [x] Count occurrences
- [x] Formula
- [x] Extract numbers
- [ ] Simplify text

``` diff
@@ Question 5. Which of the following options would NOT reduce the number of features resulting from a column of natural language?@@
```
- [ ] Removing stopwords.
- [ ] Applying stemming.
- [x] Including bigrams (2-grams) before vectorizing it.
- [ ] Normalizing the text.

```diff
@@ Question 6. Which of the following two options are generally considered the most interpretable, but the least scalable option for handling text features for ML? (Select two).@@
```
- [ ] Term hashing + SVD (Tokenize, hash and apply SVD)
- [x] TF-IDF vectorization
- [x] Count vectorization
- [ ] Term hashing (Tokenize and hash)

``` diff
@@ Question 7. Fill in the blanks: ________ vectorization is a good solution to build features taking into account the _______ of words in a text column. (Select two answers).@@
```
- [x] TF-IDF; rarity
- [x] Count; occurrences
- [ ] TF-IDF; occurrences
- [ ] Count; rarity

``` diff
@@ Question 8. Common machine learning algorithms, such as random forest or logistic regression, cannot be used for NLP tasks. @@
```
- [ ] True. The messy, unstructured nature of text data requires its own algorithms.
- [x] False. Text data is preprocessed differently, but many of the same familiar algorithms can also be used in NLP projects.
