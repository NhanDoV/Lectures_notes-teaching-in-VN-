In this topic we will discuss some techniques used in `data-wrangling`

## 1. Data pre-processing
### 1.1. Imputation (pre-processing)
Imputation deals with handling missing values in data. 
- **Categorical Imputation**: Missing categorical variables are generally replaced by the `most commonly occurring value in other records`
- **Numerical Imputation**: Depend on your dataset's scenario, the missing numerical values are generally replaced by the `mean, median, constants` of the corresponding value in other records.
- Other ways to do this include replacing missing values by picking the value from a `normal distribution` with the `mean/standard deviation` of the corresponding existing values or even replacing the missing value with an arbitrary value.
  
### 1.2. Discretization
This involves taking a set of data values and grouping sets of them together logically into bins (or buckets). The grouping of data can be done as follows:

- Grouping of **equal intervals** (split the age-groups into each equal-interval 0-20, 20-40, etc)
- Grouping based on **equal frequencies** (of observations in the bin)
- Grouping based on **decision tree sorting** (to establish a relationship with target)

```
      import pandas as pd
      # ******************************************************************
      df = pd.DataFrame({
                        'passenger_id': range(1, 301),
                        'age': np.random.randint(10, 88, 300)
                        })
      #================= by equal-interval
      df['age_group'] = pd.cut(df['age'].astype(int), 5)
      #================= by equal frequencies
      df['age_qcut_5'] = pd.qcut(df['age'], 5) # cut by quantiles
      #---------------------- display
      df.head()
      .....
           passenger_id  age      age_group     age_qcut_5
      0               1   45   (40.8, 56.2]   (44.0, 62.0]
      1               2   26   (25.4, 40.8]  (9.999, 28.0]
      2               3   85   (71.6, 87.0]   (74.2, 87.0]
      3               4   33   (25.4, 40.8]   (28.0, 44.0]
      4               5   64   (56.2, 71.6]   (62.0, 74.2]
      #=================== other
      import seaborn as sns
      df = sns.load_dataset("tips")
      df['weekday_type'] = np.where(df['day'].isin(['Sat', 'Sun']), 'weekend', 'weekday')
      #---------------------- display
      df.head()
      .....
           total_bill   tip     sex smoker   day    time  size weekday_type
      0         16.99  1.01  Female     No   Sun  Dinner     2      weekend
      1         10.34  1.66    Male     No   Sun  Dinner     3      weekend
      2         21.01  3.50    Male     No   Sun  Dinner     3      weekend
      3         23.68  3.31    Male     No   Sun  Dinner     2      weekend
      4         24.59  3.61  Female     No   Sun  Dinner     4      weekend
```

### 1.3. Categorical Encoding
This technique used to encode categorical features into numerical values, which are usually simpler for an algorithm to understand. `One hot encoding(OHE)`  is a popularly used technique of categorical encoding (only 0 and 1) and `LabelEncoder`

```
          import pandas as pd
          import numpy as np
          from sklearn.preprocessing import OneHotEncoder, LabelEncoder
          # ================================================
          df = pd.DataFrame({'fruit': np.random.choice(['apple', 'orange',
                                                        'pineaple', 'pear',
                                                        'grape', 'apricot'], 15)})
          df['fruit_enc'] = LabelEncoder().fit_transform(df['fruit'].to_numpy())
          #-------------------display
          df
          ....
                 fruit  fruit_enc
          0     orange          3
          1     orange          3
          2      grape          2
          3   pineaple          5
          4     orange          3
          5    apricot          1
          6    apricot          1
          7    apricot          1
          8      apple          0
          9    apricot          1
          10      pear          4
          11    orange          3
          12      pear          4
          13     apple          0
          14  pineaple          5
```

### 1.4. Enhancing
Include 
- `numerical`: for example, extract the values of date, month, etc from datetime, 

```
      import pandas as pd
      df = pd.read_csv(...)
      df.head()
            +-------------------+------------+----+----+----+----+----+----+
            |                DOB|current_date|col3|col4|col5|col6|col7|col8|
            +-------------------+------------+----+----+----+----+----+----+
            |2019-08-25 13:30:00|  2024-03-19|    |    |    |    |    |    |
            |2023-10-06 05:12:11|  2024-03-19|    |    |    |    |    |    | 
            |2022-04-01 00:00:00|  2024-03-19|    |    |    |    |    |    |
            |2024-03-18 20:10:12|  2024-03-19|    |    |    |    |    |    |
            +-------------------+------------+----+----+----+----+----+----+    
      from feat_engr import *
      df = datetime_enhance(df, date_col='DOB', apply_on=['get_month', 'get_month_name', 'hour'])
      df.head()
            +-------------------+------------+---------+--------------+----+----+----+----+----+----+----+
            |                DOB|current_date|get_month|get_month_name|hour|col3|col4|col5|col6|col7|col8|
            +-------------------+------------+---------+--------------+----+----+----+----+----+----+----+
            |2019-08-25 13:30:00|  2024-03-19|       08|        August|  13|    |    |    |    |    |    |
            |2023-10-06 05:12:11|  2024-03-19|       10|       October|  05|    |    |    |    |    |    |
            |2022-04-01 00:00:00|  2024-03-19|       04|         April|  00|    |    |    |    |    |    |
            |2024-03-18 20:10:12|  2024-03-19|       03|         March|  20|    |    |    |    |    |    |
            +-------------------+------------+---------+--------------+----+----+----+----+----+----+----+         
```
  
- `text` ([read more - part1](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/tree/master/Python%20Data%20Science%20Toolbox/All-of-AI-notes/NLP))
- or even `feature creation`: involves deriving new features from existing ones. This can be done by simple mathematical operations such as aggregations to obtain the mean, median, mode, sum, or difference and even product of two values. Although derived directly from the given input data, these features can impact the performance when carefully chosen to relate to the target (as demonstrated later!)

### 1.5. Handling Outliers
Outliers are unusually high or low values in the dataset, which are unlikely to occur in normal scenarios. Since these outliers could adversely affect your prediction, they must be handled appropriately. The various methods of handling outliers include:

- **Removing**: The records containing outliers are removed from the distribution. However, the presence of outliers over multiple variables could result in losing out on a large portion of the datasheet with this method.
- **Replacing values**: The outliers could alternatively bed treated as missing values and replaced by using `appropriate imputation`.
- **Capping**: Capping the maximum and minimum values and replacing them with an arbitrary value or a value from a variable distribution.

### 1.6. Variable Transformations
Variable transformation techniques help with normalizing skewed data. One such popularly used transformation is the `logarithmic transformation`. 
- Logarithmic transformations operate to compress the larger numbers and relatively expand the smaller numbers. This, in turn, results in less skewed values, especially in the case of heavy-tailed distributions. Other variable transformations used include 
- [Square root](): $x' = \sqrt{x}$, and
- [Box-Cox transformations](https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_(Lane)/16%3A_Transformations/16.04%3A_Box-Cox_Transformations): The Box-Cox transformation of the variable $x$ is also indexed by $\lambda$ is defined by

![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/1752ab91-2a88-40ce-a89e-bac90e0f1c23)

which generalize the former two.

### 1.7. Data scaling
Feature scaling is done owing to the sensitivity of some machine learning algorithms to the scale of the input values. This technique of feature scaling is sometimes referred to as feature normalization. The commonly used scaling processes include:

- Min-Max Scaling: $x = \dfrac{x - x_{\min}}{x_{\max}- x_{\min}}$
- Standardization/Variance Scaling: $x = \dfrac{x - x.{\text{mean}}}{\text{Std}x}$
- Robust Scaling: $x = \dfrac{x - Q2}{IQR}$

### 1.8. Drop unnecessary data
- Drop the columns which contain IDs, Names, etc or contain a lot of null or missing values, or even column have low variance 
- Remove rows containing too-many (over 20%) null values
- Drop all the invalid-data

## 2. Dimension reduction (PCA - SVD - tSNE)
- Dimensionality reduction is required to remove the correlated variables and maximize the performance of the model
- Both **PCA (Principal Component Analysis)** and **t-SNE (t-Distributed Stochastic Neighbor Embedding)** are the dimensionality reduction techniques in Machine Learning and efficient tools for data exploration and visualization. In this article, we will compare both PCA and t-SNE. We will see the advantages and disadvantages / limitations of t-SNE over PCA.
### 2.1. T-SNE vs PCA
**Pros**
- `Handles Non Linear Data Efficiently`: PCA is a linear algorithm. It creates Principal Components which are the linear combinations of the existing features. So, it is not able to interpret complex polynomial relationships between features. So, if the relationship between the variables is nonlinear, it performs poorly. On the other hand, t-SNE works well on non-linear data. It is a very effective non-linear dimensionality reduction algorithm. 

      PCA tries to place dissimilar data points far apart in a lower dimension representation.
      But in order to represent high dimension data on low dimension, non-linear manifold, it is important that similar datapoints must be represented close together, which is not what PCA does.
      This is done efficiently by t-SNE. So, it can efficiently capture the structure of trickier manifolds in the dataset.

- `Preserves Local and Global Structure`: t-SNE is capable to preserve local and global structure of the data. This means, roughly, that points which are close to one another in the high-dimensional dataset, will tend to be close to one another in the low dimension. On the other hand, PCA finds new dimensions that explain most of the variance in the data. So, it cares relatively little about local neighbors unlike t-SNE.

**Cons**
- Computationally Complex: t-SNE involves a lot of calculations and computations because it computes pairwise conditional probabilities for each data point and tries to minimize the sum of the difference of the probabilities in higher and lower dimensions.

        “Since t-SNE scales quadratically in the number of objects N, its applicability is limited to data sets with only a few thousand input objects;
        beyond that, learning becomes too slow to be practical (and the memory requirements become too large)”.
        
        t-SNE has a quadratic time and space complexity in the number of data points.
        This makes it particularly slow, computationally quite heavy and resource draining while applying it to datasets comprising of more than 10,000 observations. 

#### Use both PCA and t-SNE: 
Solution of the above problem is to use both PCA and t-SNE in conjunction. So, if you have thousands of features in a dataset, don't use t-SNE for dimensionality reduction in the first step. First use PCA to reduce the dimensions to a reasonable number of features and then run t-SNE to further reduce the dimensionality.

- Non-deterministic: Sometimes different runs with same hyper parameters may produce different results. So, you won't get exactly the same output each time you run it, though the results are likely to be similar.

- Requires Hyperparameter Tuning: t-SNE involves hyperparameters to be tuned unlike PCA (does not have any hyperparameter). Handing hyperparameters incorrectly may lead to unwanted results.

- Noisy Patterns: Patterns may be found in random noise as well, so multiple runs of the algorithm with different sets of hyperparameter must be checked before deciding if a pattern exists in the data.

### 2.2. Important-params

            PCA                                                              T-SNE
            n_components                                                      n_components
            svd_solver:{‘auto’, ‘full’, ‘arpack’, ‘randomized’}               learning_rate
                                                                              n_iter (default 1000) / n_iter_without_progress (default 300)
                                                                              metric (’euclidean’/ ’precomputed’) / method: {‘barnes_hut’, ‘exact’}
```
        from sklearn.decomposition import PCA
        
        df = sns.load_dataset("iris")
        df = df.drop(columns='species')
        pca = PCA(n_components=3, svd_solver='full')
        pca_df = pd.DataFrame(pca.fit_transform(df), columns=['PC1', 'PC2', 'PC3'])
        pca_df.head()
        ....
                  PC1       PC2       PC3
        0   -2.684126  0.319397 -0.027915
        1   -2.714142 -0.177001 -0.210464
        2   -2.888991 -0.144949  0.017900
        3   -2.745343 -0.318299  0.031559
        4   -2.728717  0.326755  0.090079
        #========================= using TSNE 
        from sklearn.manifold import TSNE
        import seaborn as sns
        import pandas as pd
        
        df = sns.load_dataset("iris")
        df = df.drop(columns='species')
        tsne = TSNE(n_components=3, learning_rate='auto', init='random', 
                    perplexity=3, n_iter=500, n_iter_without_progress=100,
                    metric='euclidean', method='exact'
                    )
        tsne_df = pd.DataFrame(tsne.fit_transform(df.to_numpy()), columns=['tsne_1', 'tsne_2', 'tsne_3'])
        tsne_df.head()
        .....
                tsne_1     tsne_2     tsne_3
        0     7.941830 -20.041439  10.733975
        1     1.523185   7.113355  44.816097
        2    -3.798206   9.286362  14.683980
        3    -3.915818   2.862830  23.132486
        4     9.670996 -13.806034   5.404904
```
## 3. Data Wrangling 
### 3.1. Feature engineering
Like what we mentioned in the first section

### 3.2. Train-test split
We should not use the entire dataset to train a model. We should keep aside around 20% of data to test the accuracy of the model. So, usually we maintain a ratio of 80:20 (or `70:30 | 75:25`) between training and testing datasets.

#### Reference
- [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
- [t-SNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)
- [code](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/tree/master/Python%20Data%20Science%20Toolbox/All-of-AI-notes/Feature-engineering)