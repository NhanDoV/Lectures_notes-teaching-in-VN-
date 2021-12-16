## Theory
[link](https://academy.dataiku.com/path/ml-practitioner/intro-to-machine-learning-ml)
## Practice
### Quiz 1: Introductory Concepts.
``` diff
@@ Question 1:  True or False: In a supervised learning task, learning occurs when labeled data is used to create a mapping of input features to unknown outputs.@@
```
- [ ] True. The input features represent the labeled data.
- [x] **False. The very existence of labeled data is what makes the learning “supervised” but the outputs are known rather than unknown.**

``` diff
@@ Question 2: True or False: A machine learning algorithm is not explicitly programmed, instead its learning is based on the way humans learn.@@
```
- [x] **True. A machine learning algorithm learns from patterns, historical records, and events.**
- [ ] False. A machine learning algorithm must be explicitly programmed using conditional statements, such as, “If, Then, Else” rules.

``` diff
@@ Question 3: Which of the following is an accurate description of the benefit of machine learning over traditional programming? (Choose one.)@@
```
- [ ] Algorithms require fewer hours of programming but more lines of code.
- [ ] Algorithms require more hours of programming but fewer lines of code.
- [x] **Algorithms can improve their learning over time without being explicitly programmed.**

### Quiz 2: Predictive Modeling.
``` diff
@@ Question 1: True or False: An overfit model cannot apply what it has learned to new data because it has memorized the training dataset.@@
```
- [ ] False. An overfit model cannot apply what it has learned to new data because the training dataset did not provide enough information.
- [x] True. Overfitting happens when a model fits the training dataset too well. It memorizes that dataset and does not learn the relationship between the inputs and outputs.
``` diff
@@ Question 2: If we wanted to predict a distinct or continuous value, such as an exam score, what type of prediction problem would we be solving?@@
```
- [ ] Clustering
- [x] **Regression**
- [ ] Classification
``` diff
@@ Question 3: A confusion matrix can be used to determine the optimal threshold when training a classification model. Note: the threshold in this context is the cutoff point between what the model classifies as true and what is classifies as false.@@
```
- [ ] False. A confusion matrix helps to visualize the performance of a classification model, but creating the matrix does not depend on the threshold used with the model.
- [x] **True. A confusion matrix shows the correct and incorrect predictions made by the model at a specific threshold.**
``` diff
@@ Question 4: A set of rules that define how a model makes predictions are called the model parameters. Which of the following is not an example of these rules? (Choose one.)@@
```
- [x] **Hyperparameter optimization**
- [ ] An equation
- [ ] A decision tree
- [ ] Many decision trees
``` diff
@@ Question 5: True or False: The difference between supervised and unsupervised learning is that supervised learning uses labeled data while unsupervised learning uses unlabeled data.@@
```
 - [ ] False. In supervised learning, a machine learning practitioner uses unlabeled data as input. In unsupervised learning, a machine learning practitioner uses labeled data as input.
- [x] **True. In supervised learning, a machine learning practitioner uses labeled data as input. In unsupervised learning, a machine learning practitioner uses unlabeled data as input.**
``` diff
@@ Question 6: Which of the following can be used evaluate the performance of a regression model? (Choose one.)@@
```
- [ ] True positive rate
- [ ] ROC/AUC
- [x] R-Squared
- [ ] Confusion matrix
 
 ### Quiz 3: Prediction: Regression.
 ``` diff
@@ Question 1: In the regression equation, where the equation of the best fitting line is MIN (SUM(y - ŷ)2), what does ŷ (y-hat) represent?@@
```
- [ ] The predicted value of "x" (the independent variable).
- [ ] The predicted value of "x" (the dependent variable).
- [ ] The predicted value of "y" (the independent variable).
- [x] The predicted value of "y" (the dependent variable).
``` diff
@@ Question 2: True or False: In linear regression, where the equation that models the data set is y = mx + b, b is the point where the line crosses the y axis.@@
```
- [ ] False: "b" is the slope of the line.
- [x] True: "b" is the "y-intercept".
``` diff
@@ Question 3: True or False: If we are predicting a continuous quantity, we would use a regression algorithm instead of a classification algorithm.@@
```
- [x] True: Classification is about predicting a discrete class label while regression is about predicting a continuous quantity.
- [ ] False: Regression is about predicting a discrete class label while regression is about predicting a continuous quantity.

### Quiz 4. Prediction: Classification.
``` diff
@@ Question 1: Which of the following machine learning algorithms cannot be used in both classification and regression problems? (Choose two.)@@
```
- [ ] Decision trees
- [ ] Random forest
- [x] **Logistic regression**
- [x] **Linear regression**
``` diff
@@ Question 2: In binary classification, a decision node in a decision tree is labeled with either an input feature, or a "yes/no" question.@@
```
- [ ] False. A "yes/no" question in a decision tree is represented as a leaf of the tree rather than a node of the tree.
- [x] **True. A decision node in a decision tree is also known as a feature.**

### Quiz 5: Clustering.
``` diff
@@ Question 1: True or False: One difference between K-means and hierarchical clustering is in hierarchical clustering, we don't arbitrarily select the initial value of "K".@@
```
- [x] **True. In hierarchical clustering, we aim to first understand the relationship between the clusters visually, and then determine the number of clusters, or hierarchy level, that best portrays the different groupings.**
- [ ] False. In hierarchical clustering, we aim to set K to an optimal number, creating just the right number of clusters, where adding more clusters would no longer provide a sufficient decrease in variation.
``` diff
@@ Question 2: How does an unsupervised machine learning algorithm work?@@
```
- [ ] By finding the relationship between the features and the resulting outcome.
- [ ] By finding the relationship between the input and output variables.
- [ ] By using labeled data for which class labels represent outcomes.
- [x] **By inferring underlying patterns from an unlabeled dataset (clustering).**

### Final.
``` diff
@@ Question 1: Which of the following algorithms could be used to predict a continuous quantity. (Choose two)@@
```
- [x] **Multiple linear regression**
- [ ] Logistic regression
- [x] **Linear regression**
``` diff
@@ Question 2: True or False. One difference between K-means and hierarchical clustering is that hierarchical clustering does not require us to select an initial value for the number of clusters, while K-means clustering does.@@
```
- [ ] False. In hierarchical clustering, we aim to first set an optimal value for the number of clusters so that we know where adding more clusters would no longer provide a sufficient decrease in variation.
- [x] **True. In hierarchical clustering, we aim to first understand the relationship between the clusters visually, and then determine the number of clusters, or hierarchy level, that best portrays the different groupings.**
``` diff
@@ Question 3: Model parameters can be thought of as a set of rules that define how a model makes predictions. Which of the following is not an example of these rules? (Choose one.)@@
```
- [ ] Many decision trees
- [x] **Hyperparameter optimization**
- [ ] An equation
- [ ] A decision tree
``` diff
@@ Question 4: How does an unsupervised machine learning algorithm work?@@
```
- [ ] By using labeled data for which class labels represent outcomes.
- [ ] By finding the relationship between the input and output variables.
- [ ] **By inferring underlying patterns from an unlabeled dataset (clustering).**
- [ ] By finding the relationship between the features and the resulting outcome.
``` diff
@@ Question 5: If we wanted to predict a distinct or continuous value, such as an exam score, what type of prediction problem would we be solving?@@
```
- [ ] Clustering
- [ ] Classification
- [x] **Regression**
``` diff
@@ Question 6: In binary classification, a decision node in a decision tree is labeled with either an input feature, or a "yes/no" question.@@
```
- [x] **True. A decision node in a decision tree is also known as a feature.**
- [ ] False. A "yes/no" question in a decision tree is represented as a leaf of the tree rather than a node of the tree.
``` diff
@@ Question 7: Which of the following is a tool or metric used to evaluate a regression model:@@
```
- [ ] Confusion matrix
- [ ] True positive rate
- [x] R-Squared
- [ ] ROC/AUC
``` diff
@@ Question 8: Let’s say we have a linear regression algorithm where the equation of the line on the graph is y=mx+b. Which of the following correctly describes this line?@@
```
- [ ] Curvy line
- [x] **Straight line**
- [ ] Non-linear
- [ ] Sigmoid function
``` diff
@@ Question 9: Which of the following machine learning algorithms cannot be used in both classification and regression problems?
```
- [ ] Random forest
- [x] **Logistic regression**
- [ ] Decision trees
