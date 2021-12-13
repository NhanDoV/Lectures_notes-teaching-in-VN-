## Theory
https://academy.dataiku.com/path/ml-practitioner/machine-learning-basics
## Practice
### Quiz 1. Create the Model
``` diff
@@ Question 1. What are some potential issues to look for when preparing a dataset for machine learning? (Select all that apply.) @@
```
- [x] **Columns that won't have any predictive power for the model**
- [x] **Raw dates that are not converted into numerical features**
- [x] **Data leakage**
- [x] **Data quality**

``` diff 
@@ Question 2. Data leakage happens when the model is trained using information that won't be available when the model is deployed to production.@@
```
- [x] **True. For a model to have a good performance, it must generalize well on unseen data Data leakage causes low generalization performance.**
- [ ] False. Data leakage refers to a feature that can be removed because it has little impact on the target.

``` diff
@@ Question 3. Building your machine learning model will happen in the Lab of DSS. The Lab is a place for both preliminary data preparation and machine learning model creation.@@
```
- [ ] False. The Lab is specifically designed for machine learning model creation and any data preparation must be performed outside of the Lab.
- [x] **True. While the Lab is where you build your machine learning model, you can also perform data preparation in the Lab with the option of deploying the script to the Flow.**

``` diff
@@ Question 4. Before building a model, you can prevent issues and improve the performance of your model by carefully exploring your training dataset.@@
```
- [ ] False. Most machine learning model performance issues are not attributed to the training dataset itself.
- [x] **True. You can use Dataiku DSS to explore your dataset to address common pitfalls before training your model.**

``` diff
@@ Question 5. What is the default sampling strategy DSS uses when training models? Select one. @@
```
- [ ] A random split, in which half of the records are fed into the train set.
- [x] **A random split, in which 80% of records are fed into the train set, and 20% are fed into the test set.**
- [ ] There is no default sampling strategy. The user must always select one.
- [ ] Two explicit extracts from the dataset are used, one for train, the other for test.

### Quiz 2: Evaluate the model.
``` diff
@@ Question 1. Which of the following are possible after training a model? (Select all that apply.)@@
```
- [x] **Compare different modeling sessions side-by-side.**
- [x] **Revert the model design back to a previous session.**
- [x] **View the most important variables or regression coefficients.**
- [x] **Find out how long it took to train the model.**

``` diff
@@ Question 2. When comparing model results in the Result tab, it is possible to select a different metric than the one you optimized for during training.@@
```
- [ ] False. To select another metric when comparing results, you would have to retrain the model using a different metric.
- [x] **True. In the Result tab, you can rank models according to another metric by selecting it from a drop-down list.**

### Quiz 3: Tune the model
``` diff
@@ Question 1. What are some reasons why you would want to generate polynomial features when building a model? (Select all that apply.)@@
```
- [x] Uncover new relationships between the features and the target.
- [ ] Reduce the resulting number of new features.
- [x] Improve the model's performance.

``` diff
@@ Question 2. When selecting features to train a model, Dataiku DSS will automatically detect and exclude a column that consists of unique identifiers.@@
```
- [ ] False. You must manually exclude features that you do not want to use to train the model.
- [x] True. DSS detects unique identifiers, such as Customer ID, and excludes them. You can also manually exclude any feature that you do not want to use to train the model.

``` diff
@@ Question 3. What types of columns can be processed as features in the Design Tab? (Select all that apply.)@@
```
- [x] Categorical
- [x] Text
- [x] Vector
- [x] Numerical
- [ ] Date

``` diff
@@ Question 4. The set of algorithms presented depends on the type of machine learning task you select, such as Prediction or Clustering.@@
```
- [x] True. DSS supports several algorithms and these algorithms depend on the machine learning task at stake.
- [ ] False. DSS displays all algorithms from which to choose regardles.

### Quiz 4. Explainable AI
``` diff
@@ Question 1. Consider a model to predict survival on the Titanic. Which model interpretation method would be used to answer a question such as, “Does the model perform similarly for male and female passengers?”@@
```
- [ ] Partial Dependence Plots
- [x] Subpopulation Analysis
- [ ] Individual Explanations
- [ ] Interactive Scoring

```diff
@@ Question 2. Which model interpretation method could you use to compare predictions for different passenger profiles and how changing inputs like ticket class, fare, gender, etc. affects the predicted probability of survival?@@
```
- [ ] Partial Dependence Plots
- [ ] Subpopulation Analysis
- [ ] Individual Explanations
- [x] Interactive Scoring

``` diff
@@ Question 3. Which of the following model interpretation methods lets you quickly get feature contributions for the most extreme predictions, making it easier to communicate the reasons for a specific prediction to business users, and check for any potential biases in the model?@@
```
- [ ] Partial Dependence Plots
- [ ] Subpopulation Analysis
- [x] Individual Explanations
- [ ] Interactive Scoring

``` diff
@@ Question 4. Which model interpretation method is used to determine if a model performs the same across different groups of interest (subgroups)?@@
```
- [ ] Partial Dependence Plots
- [x] Subpopulation Analysis
- [ ] Individual Explanations
- [ ] Interactive Scoring

``` diff
@@ Question 5. What is the name of the model interpretation plot that allows you to understand how a particular feature affects the model’s predictions? @@
```
- [xx] Partial Dependence Plots
- [ ] Subpopulation Analysis
- [ ] Individual Explanations
- [ ] Interactive Scoring

### Final quiz
``` diff
@@ Question 1. Before building a model, you can prevent issues and improve the performance of your model by carefully exploring your training dataset.@@
```
- [ ] False. Most machine learning model performance issues are not attributed to the training dataset itself.
- [x] True. You can use Dataiku DSS to explore your dataset to address common pitfalls before training your model.

```diff
@@ Question 2. Which of the following is not possible after training a model and reviewing the results in the Result tab? (Choose one.)@@
```
- [ ] View the most important variables or regression coefficients.
- [ ] Compare different modeling sessions side-by-side.
- [ ] Revert the model design back to a previous session.
- [x] Combine two modeling sessions.
- [ ] Find out how long it took to train the model.

```diff
@@ Question 3. Which of the following model interpretation methods lets you quickly get feature contributions for the most extreme predictions, making it easier to communicate the reasons for a specific prediction to business users, and check for any potential biases in the model?@@
```
- [ ] Partial Dependence Plots
- [ ] None of these
- [ ] Subpopulation Analysis
- [x] Individual Prediction Explanations

``` diff
@@ Question 4. Which model interpretation method is used to determine if a model performs the same across different groups of interest (subgroups)?@@
```
- [ ] None of these
- [x] Subpopulation Analysis
- [ ] Partial Dependence Plots
- [ ] Individual Prediction Explanations

``` diff
@@ Question 5. What is the name of the model interpretation plot that allows you to understand how a particular feature affects the model’s predictions?@@
```
- [x] Partial Dependence Plots
- [ ] Individual Prediction Explanations
- [ ] None of these
- [ ] Subpopulation Analysis

``` diff 
@@ Question 6. What types of columns can be processed as features in the Design tab? (Select all that apply.)@@
```
- [ ] Lasso
- [ ] Categorical
- [ ] Vector
- [ ] Text
- [ ] Numerical

``` diff
@@ Question 7. The set of algorithms presented depends on the type of machine learning task you select, such as Prediction or Clustering.@@
```
- [ ] False. DSS displays all algorithms from which to choose regardless of the machine learning task at stake.
- [x] True. DSS supports several algorithms and these algorithms depend on the machine learning task at stake.

``` diff
@@ Question 8. Consider a model to predict survival on the Titanic. Which model interpretation method would be used to answer a question such as, “How do survival prediction rates (what the model is trying to predict) differ across a particular feature like age?”@@
```
- [x] Partial Dependence Plots
- [ ] Subpopulation Analysis
- [ ] Individual Prediction Explanations
- [ ] None of these

``` diff
@@ Question 9. Consider a model to predict survival on the Titanic. Which model interpretation method would be used to answer a question such as, “Does the model perform similarly for male and female passengers?”@@
```
- [ ] Individual Explanations
- [x] Subpopulation Analysis
- [ ] Interactive Scoring
- [ ] Partial Dependence Plot

``` diff
@@ Question 10. When comparing model results in the Result tab, it is possible to select a different metric than the one you optimized for during training.@@
```
- [ ] False. To select another metric when comparing results, you would have to retrain the model using a different metric.
- [x] True. In the Result tab, you could rank models according to any available metric, even though selecting another metric may not be the best possible metric for the model’s design.
