``` diff
@@ Question 1. What kind of insights does the Individual explanations tool give you?@@
```
- [ ] The number of records that were correctly predicted.
- [ ] How the predictions vary depending on a specific feature.
- xx] Which features were the most important in the prediction for a specific record.
- [ ] Statistics about the predictions, such as average and standard deviation.

``` diff
@@ Question 2. Which three of the following ML libraries you can leverage in DSS ?@@
```
- [ ] Champagne (Wine support for ML with Spark)
- [x] MLlib (Spark ML lib)
- [x] XGBoost
- [x] Sklearn

``` diff
@@ Question 3. Use the ML Practitioner Assessment project to answer this question. In the deployed model, which two of the following features contributed the least to the prediction?@@
```
- [ ] absences
- [x] Walc
- [x] Medu
- [ ] failures

``` diff
@@ Question 4. Which two of the following are benefits of using feature generation techniques? @@
```
- [ ] Reduced training time.
- [ ] Better handling of missing values.
- [x] Uncovering new relations between features and target.
- [x] Improved model performance.

``` diff
@@ Question 5. Use the ML Practitioner Assessment project to answer this question. Let's say a subject matter expert has analyzed a chart showing the proportion of students who repeat a grade to those who don't when considering the following factors: students whose travel time is 2 or more hours and whose number of absences is at least 8 repeat a grade. The subject matter expert has asserted that the proportion of students the model will predict as "repeated" will likely be more than 20%.@@
```
- [x] False. When analyzing schools_data, the percentage of repeated=1 is less than 20% of the records when traveltime is 2 or more hours and absences are equal to 8 or more.
- [ ] True. When analyzing schools_data, the percentage of repeated=1 is greater than 20% of the records when traveltime is 2 or more hours and absences are equal to 8 or more.

``` diff
@@ Question 6. The PCA card shows which three of the following?@@
```
- [ ] A cut-off value of 75% for the explained variance.
- [x] The principal component loading vectors as a heatmap.
- [x] Eigenvalues and their corresponding principal components.
- [x] The cumulative explained variance for each principal component.

``` diff
@@ Question 7. Which three of the following actions you can perform in the Design Tab of the Visual ML tool?@@
```
- [x] Choose how you want to split the data into the training set and testing set.
- [x] Customize the evaluation metric you want to optimize.
- [ ] Visualize the performance of your previous sessions to update your model.
- [x] Process your features (cleaning, feature generation, etc).

``` diff
@@ Question 8. Use the ML Practitioner Assessment project to answer this question. Classification models establish a certain probability as a threshold. In the Evaluate recipe, if the model assigns a probability to a record that is below the threshold, then what will the prediction for that record be?@@
```
- [x] 0 (grade not repeated)
- [ ] Missing value
- [ ] 1 (grade repeated)
- [ ] Unable to be determined

``` diff
@@ Question 9. When using a model to score a dataset, which three of the following options can be computed for the scored dataset?@@
```
- [x] The individual explanations (ie the most important features) for each prediction.
- [x] The probability associated with each class, for a classification task.
- [x] The output prediction value.
- [ ] The ML model and hyperparameters that have been used for this prediction.

``` diff
@@ Question 10. Use the ML Practitioner Assessment project to answer this question. Which school in the schools_data dataset has the highest median grade?@@
```
- [x] LT
- [ ] GP
- [ ] MS
- [ ] RC

``` diff
@@ Question 11. What are some reasons why you would want to generate polynomial features when building a model? (Choose two.)@@
```
- [x] Uncover new relationships between the features and the target.
- [x] Improve the model’s performance.
- [ ] Ensure that numerical features are properly rescaled.
- [ ] Reduce the resulting number of new features.

``` diff
@@ Question 12. What feature of DSS can help you detect differences in group-level performance?  For example, for a model that predicts student outcomes, you want to analyze the difference in model performance between girls and boys.@@
```
- [ ] Individual explanations
- [ ] Partial Dependence
- [x] Subpopulation Analysis
- [ ] Variable importance

``` diff
@@ Question 13. Use the ML Practitioner Assessment project to answer this question. Looking at the variable importance charts for the random forest model, which of the following features is the most important to the model?@@
```
- [ ] schoolsup
- [x] school is RC
- [ ] traveltime
- [ ] grade

``` diff
@@ Question 14. To use Spearman's correlation in the correlation matrix card, what are some necessary steps to first perform on ordinal variables in your data?@@
```
- [ ] No special steps are ever required.
- [x] Map the categories to numbers, and treat the variables as numerical variables.
- [ ] Drop them from your dataset, as DSS cannot compute Spearman's correlation matrix when you have ordinal variables.
- [ ] Instead of Spearman's, you can compute Pearson's correlation matrix because it handles the ordinal variables as well.

``` diff
@@ Question 15. When using a bivariate analysis card in DSS, which one of the following statements is true?@@
```
- [x] You can choose one or more columns as factors and choose one response column in order to see how the response varies across values of each factor.
- [ ] You can choose one column as a factor and one or more response columns in order to see how each response varies across values of the factor.
- [ ] Bivariate analysis is not an option in the Statistics tab of a dataset.
- [ ] DSS automatically selects all the possible pairs of factors and responses and runs the analysis.

``` diff
@@ Question 16. Which three of the following are different ways you can process the missing values of your features? @@
```
- [ ] Drop the rows with missing value.
- [ ] Replace missing value by a constant value.
- [ ] Replace missing value by the average value or the most frequent value of the column.
- [x] Automatically drop columns that contains missing values.

``` diff
@@ Question 17. In the Results tab of an ML task after the models are trained, what does the score displayed for each model correspond to?@@
```
- [ ] Accuracy
- [ ] The score for the metric you decided to optimize for
- [ ] F1 Score
- [x] The score of the best performing metric among all the relevant ones

``` diff
@@ Question 18. Use the ML Practitioner Assessment project to answer this question. Which one of the following statements about the median grade, by number of past failures, in the schools_data dataset, is true?@@
```
- [ ] It seems to have a trend: the fewer failures a student had in the past, the higher the median grade.
- [x] It seems to have a trend: the fewer failures a student had in the past, the lower the median grade.
- [ ] The relationship has a U-shape: students with a moderate number of failures had a higher median grade, while students with very few or very many past failures had a lower median grade.
- [ ] It does not seem to have a trend here.

``` diff
@@ Question 19. Which of the following statements regarding adjustment methods is false?@@
```
- [ ] Adjustment methods are used for statistical tests that test multiple hypotheses at the same time.
- [ ] Adjustment methods will adjust the value of the observed p-value, and compare it to the pre-defined significance level.
- [x] Adjustment methods adjust the distribution of the population so that it resembles the normal distribution.
- [ ] Using adjustment methods can decrease the probability of making Type I errors (incorrectly rejecting the null hypothesis).

``` diff
@@ Question 20. You have a dataset about bank customers and credit cards defaults, and you want to build a ML model that will help you predict whether a new customer will default or not. What kind of ML task should you choose for this? @@
```
- [ ] Regression
- [ ] Clustering
- [x] Two-class classification
- [ ] Multiclass classification

``` diff
@@ Question 21. Which three of the following elements you can visualize in the Results Tab of an ML task, after the models are trained, but without clicking into individual models?@@
```
- [ ] The confusion matrix for each model
- [x] The amount of time to train each model
- [x] The performance of the model for different iterations of the gridsearch
- [x] The values of the hyperparameters for the best performing model

``` diff
@@ Question 22. Which of the following statements regarding p-values is false?@@
```
- [x] The smaller the p-value, the more confidence you can have in rejecting the null hypothesis H0.
- [ ] The p-value is the probability of observing a test statistic at least as extreme as the one computed from the sample, given that the null hypothesis is true.
- [ ] If a p-value is smaller than the significance level (alpha), this is evidence that the null hypothesis should be rejected.
- [ ] The p-value is the probability that the null hypothesis is true.

``` diff
@@ Question 23. What is the default behavior for splitting the training set and test set?@@
```
- [ ] DSS will perform a 5-fold cross validation.
- [ ] DSS will train on the whole sample available to maximize the training set available and test it on the same sample
- [ ] DSS will order the value using a time column and allocate the first half rows to training set and last half rows to test set.
- [x] DSS will perform a random split and allocate 80% of the data to the training set and 20% to the test set .

```diff
@@ Question 24. Use the ML Practitioner Assessment project to answer this question. Looking at the validation_scored dataset, the model achieves the highest correct prediction rate for which school?@@
```
- [ ] RC
- [x] MS
- [ ] LT
- [ ] GP

``` diff
@@ Question 25. Which three of the following things can you do with a model that has been deployed in the Flow?@@
```
- [ ] Use the model to score an unlabeled dataset.
- [x] Modify the model, by doing some further feature engineering for instance, in order to improve the model.
- [x] Package and deploy the model as an API to make real-time predictions.
- [x] Evaluate the model against a labeled test dataset.

``` diff
@@ Question 26. Which of the following is not a possible way to categorize statistical tests?@@
```
- [ ] Location tests vs. distribution tests.
- [ ] Descriptive tests vs. inferential tests.
- [x] 1-sample tests vs. 2-sample tests.
- [ ] Parametric tests vs. non-parametric tests.

``` diff
@@ Question 27. Which two of these statements are true regarding the active version of the model?@@
```
- [ ] The active version of the model is always the most recently deployed model.
- [ ] You can not retrain a model that has been activated.
- [x] You can deploy several versions of a model and roll back and activate a previous version of the model.
- [x] The active version of the model is the version of the model used when running the Retrain, Score or Evaluate recipes.

``` diff
@@ Question 28. Use the ML Practitioner Assessment project to answer this question. Looking at the partial dependence plots for the studytime feature on the logistic regression model, which one of the following statements is true?@@
```
- [x] It seems to have a trend: the more time a student studies, the lower the probability of repeating a grade.
- [ ] The relationship has a U-shape: students who spend a moderate amount of time studying had a lower probability of repeating a grade, while students with very few or very many hours studying had a higher probability of repeating a grade.
- [ ] It seems to have a trend: the less time a student studies, the lower the probability of repeating a grade.
- [ ] It does not seem to have a trend here.

``` diff
@@ Question 29. Use the ML Practitioner Assessment project to answer this question. In the confusion matrix for the Random forest model, if you increase the cut-off threshold, which of the following measures increase?  Select the one that applies.@@
```
- [ ] Recall
- [ ] Accuracy
- [x] Precision
- [ ] F1-Score

``` diff
@@ Question 30. When doing hypothesis testing, it is needed to have a null hypothesis H0, and an alternative hypothesis H1. What does H0 correspond to?@@
```
- [ ] The null hypothesis H0 is the hypothesis that the parameter that we want to test is equal to zero.
- [ ] The null hypothesis H0 is the hypothesis that the distribution we want to test is normally distributed, which is a required assumption to be able to perform some tests.
- [ ] The null hypothesis H0 is the hypothesis that p-value is equal to zero.
- [x] The null hypothesis H0 is a statement about the population that we assume to be true unless testing proves otherwise.

``` diff
@@ Question 31. After building a machine learning model, Dataiku DSS generates a number of visualizations and statistical summaries to understand the model. Which of the following charts will be found in the model report for both classification and clustering tasks?@@
```
- [x] Variables importance
- [ ] Cluster profiles
- [ ] Confusion matrix
- [ ] ROC Curve

``` diff
@@ Question 32. What kind of columns can be used as inputs to the PCA card?@@
```
- [x] Only numerical variables.
- [ ] Any kind of variables (numerical, categorical, text, dates, vectors...).
- [ ] Only categorical variables.
- [ ] Both numerical and categorical variables.

``` diff
@@ Question 33. Which two of the following statements are true about the PCA card heatmap?@@
```
- [ ] The darker a cell color, the weaker the relationship between the column and the principal component.
- [x] A blue color means the column has a negative relationship with the component.
- [x] The darker a cell color, the stronger the relationship between the column and the principal component.
- [ ] A blue color means the column has a positive relationship with the component.

``` diff
@@ Question 34. Using the Variables importance summary shown below, which of these features appears to be least important?@@
```
- [ ] Distance traveled by the cab during the trip, in kilometers.
- [ ] The difference in latitude from the pickup point to the drop-off point.
- [ ] The hour of the pickup time.
- [x] The distance of the drop-off point from LaGuardia Airport.

 ``` diff
 @@ Question 35.@@
 ```

21 / 30
