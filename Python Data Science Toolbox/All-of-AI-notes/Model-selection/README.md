Here we only focus on tabular-data, the images / sound / etc will be represented in the other section likes [Computer-Vision](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/tree/master/Python%20Data%20Science%20Toolbox/All-of-AI-notes/Computer-Vision) or [Generative-model](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/tree/master/Python%20Data%20Science%20Toolbox/All-of-AI-notes/Generative_model)

## 1. ANOVA in Linear-regression
- Analysis of variance (ANOVA) is a powerful statistical technique. 
- Null hypothesis: all means are equal

```
      import statsmodels.api as sm
      from statsmodels.formula.api import ols
```

## 2. Feature importance
- Feature importance is a step in building a machine learning model that involves calculating the score for all input features in a model to establish the importance of each feature in the decision-making process. 
- The higher the score for a feature, the larger effect it has on the model to predict a certain variable.

### Why it is important
- **DATA COMPREHENSION** Building a model is one thing, but understanding the data that goes into the model is another. Like a correlation matrix, feature importance allows you to understand the relationship between the features and the target variable. It also helps you understand what features are irrelevant for the model.
- **MODEL IMPROVEMENT** When training your model, you can use the scores calculated from feature importance to reduce the dimensionality of the model. The higher scores are usually kept and the lower scores are deleted as they are not important for the model. This simplifies the model and speeds up the model’s working, ultimately improving the performance of the model.
- **MODEL INTERPRETABILITY**: Feature importance is also useful for interpreting and communicating your model to other stakeholders. By calculating scores for each feature, you can determine which features attribute the most to the predictive power of your model.

### Which ML algorithms used it
- RandomForest
- ExtraTrees
- XGB
- LGBM
- AdaBoost

### Flow to compute
- Calculate the mean squared error with the original values.
- Shuffle the values for the features and make predictions.
- Calculate the mean squared error with the shuffled values.
- Compare the difference between them.
- Sort the differences in descending order to get features with most to least importance.

## 3. Bagging-Boosting models
Bagging and Boosting are two types of Ensemble Learning. These two decrease the variance of a single estimate as they combine several estimates from different models. So the result may be a model with higher stability. Let’s understand these two terms in a glimpse.

- Bagging:
>- It is a homogeneous weak learners’ model that learns from each other independently in parallel and combines them for determining the model average.
>- Bootstrap Aggregating, also known as bagging, is a machine learning ensemble meta-algorithm designed to improve the stability and accuracy of machine learning algorithms used in statistical classification and regression. It decreases the variance and helps to avoid overfitting. It is usually applied to decision tree methods. Bagging is a special case of the model averaging approach.
#### Implementation Steps of Bagging

        Step 1: Multiple subsets are created from the original data set with equal tuples, selecting observations with replacement.
        Step 2: A base model is created on each of these subsets.
        Step 3: Each model is learned in parallel with each training set and independent of each other.
        Step 4: The final predictions are determined by combining the predictions from all the models.

![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/0687ab2d-6e17-417e-a8b5-13875f74c8a1)

- Boosting:
>- It is also a homogeneous weak learners’ model but works differently from Bagging. In this model, learners learn sequentially and adaptively to improve model predictions of a learning algorithm.
>- Boosting is an ensemble modeling technique that attempts to build a strong classifier from the number of weak classifiers. It is done by building a model by using weak models in series.
>- Firstly, a model is built from the training data. Then the second model is built which tries to correct the errors present in the first model.
>- This procedure is continued and models are added until either the complete training data set is predicted correctly or the maximum number of models is added.
#### Algorithm:

    1. Initialise the dataset and assign equal weight to each of the data point.
    2. Provide this as input to the model and identify the wrongly classified data points.
    3. Increase the weight of the wrongly classified data points and decrease the weights of correctly classified data points. And then normalize the weights of all data points.
    4. if (got required results)
        Goto step 5
      else
        Goto step 2
    5. End

![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/42bbed6a-ee56-41f5-9f37-a1cd0e697699)

#### Comparison
![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/be42687d-ea4e-42dd-a6b1-b0e5e3e87404)

## 4. All of clustering models

![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/7b0fc5de-0488-44bf-873c-1558294147f6)

## 5. All of time-series models
### 5.1. Stationery testing
- A stationary time series is one whose statistical properties do not depend on the time at which the series is observed.18 Thus, time series with trends, or with seasonality, are not stationary — the trend and seasonality will affect the value of the time series at different times. On the other hand, a white noise series is stationary — it does not matter when you observe it, it should look much the same at any point in time.
- In this case we can consider any models like `ARIMA` and `SARIMAX`

### 5.2. Denoising
- Savitzky–Golay filter
- Convolution
- Rolling average