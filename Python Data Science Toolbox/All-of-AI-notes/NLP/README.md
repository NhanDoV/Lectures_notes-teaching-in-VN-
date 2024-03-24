## 1. Enhancing
[Reference](https://github.com/NhanDoV/Hackerank-test/blob/main/Mathematics/Regex_string/matching.ipynb)

| description | syntax (pattern) | regex.function | 
|-|-|-|
|find word starts with `x`|`r"^x"`|`re.findall(patt, test_string.lower())`|
|find word ended with `x` | `r"x$"` | `re.findall(patt, test_string.lower())`|
|matched a character `w` 3-5 times | `r"w{3,5}"` | `re.findall(patt, test_string.lower())`|
|matched these character `w, t, s` 3-5 times | `r"[wts]{3,5}"` | `re.findall(patt, test_string.lower())`|
|matched any digits more than 2 times | `r"\d{2,}"` | `re.findall(patt, test_string.lower())`


## 2. CountVect-Tfidf-Ngrams-GloVec-WordEmb

## 3. 