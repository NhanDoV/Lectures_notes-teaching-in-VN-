## Theory
https://academy.dataiku.com/path/ml-practitioner/scoring-basics
## Practices
### Quiz 1: Deploy the Model
``` diff
@@ Question 1. In order to deploy a model, you can click on the training dataset in the Flow and add a Train recipe from the Actions sidebar.@@
```
- [x] **False. You can only initiate a Train recipe by choosing a model from the Lab to deploy.**
- [ ] True. Look beneath the plugin recipes.

``` diff
@@ Question 2. Before scoring a model in DSS, you first need to deploy the model from the __________ to the _________.@@
```
- [x] **Lab; Flow**
- [ ] Neither. It’s an optional step.
- [ ] Flow; Lab

``` diff
@@ Question 3. What is the output of a Train recipe?@@
```
- [x] **A saved model**
- [ ] A scored dataset
- [ ] A new model training session

### Quiz 2: Scoring Data.
``` diff
@@ Question 1. Which of the following are inputs to a Score recipe? Select two.@@
```
- [x] **A saved model**
- [x] **Data to be scored**
- [ ] Model hyperparameters
- [ ] Training data

```diff
@@ Question 2. Which of the following could a Score recipe NOT add to its output dataset?@@
```
- [ ] Class probabilities
- [ ] Explanations
- [x] **Confidence intervals**
- [ ] Predictions

``` diff
@@ Question 3. The output of which of the following recipes is a scored dataset?@@
```
- [x] **Score**
- [ ] Train
- [ ] Deploy
- [ ] Cluster

### Quiz 3: Model Lifecycle Management.
``` diff
@@ Question 1. After retraining a model deployed in the Flow, the newly trained model becomes the active version.@@
```
- [x] **By default this is true, but you can also change the settings to manually choose when to activate a new version.**
- [ ] Always true. The model trained on the latest data must be better.
- [ ] Never true. The best performing model automatically becomes the new version.

``` diff
@@ Question 2. After retraining a model deployed in the Flow, which other models are also retrained?@@
```
- [ ] It depends on what recipe settings you have selected.
- [x] **Only the model deployed in the Flow**
- [ ] All other models in the same visual analysis
- [ ] All other models in the same training session.

``` diff
@@ Question 3. The purpose of which kind of dataset, also known as a hold-out set, is to provide an unbiased evaluation of model fit?@@
```
- [ ] Scoring set
- [ ] Training set
- [x] **Validation set**
- [ ] Testing set

### Final / summary
``` diff
@@ Question 1. The output of which of the following recipes is a scored dataset? Select all that apply.@@
```
- [ ] Train
- [x] Predict
- [x] Score
- [ ] Deploy

``` diff
@@ Question 2. In the page showing the versions of a saved model, the metric displayed to the right of a model name is in reference to which of the following datasets?@@
```
- [ ] The unlabelled set
- [ ] The train set
- [x] The test set
- [ ] The validation set

``` diff
@@ Question 3. Deploying a model from the Lab adds which of the following two items to the Flow? Select two.@@
```
- [ ] A scored dataset
- [x] A Train recipe
- [ ] A Score recipe
- [x] A saved model

``` diff
@@ Question 4. Which of the following are inputs to the Evaluate recipe? Select all that apply.@@
```
- [x] A labelled dataset
- [ ] A visual analysis
- [x] A deployed prediction model
- [ ] Data to be scored

``` diff
@@ Question 5. In which of the following ways can a saved model NOT be used?@@
```
- [ ] An input to a Train recipe
- [ ] An input to a Score recipe
- [ ] Deployed as an API
- [x] An input to an Evaluate recipe

``` diff
@@ Question 6. Which of the following are outputs to the Evaluate recipe? Select all that apply.@@
```
- [ ] A chart of variable importance
- [ ] A new active version of the model
- [x] A dataset of model metrics
- [x] A scored dataset

``` diff
@@ Question 7. The data used to train the model and the data to be scored by the model must have the same schema. In this scenario, both datasets contain the same columns.@@
```
- [ ] False. Any missing features in the data to be scored will be dropped from the model before scoring.
- [x] True. DSS will throw an error on the Score recipe dialog if the schemas do not match.

``` diff
@@ Question 8. What is the difference between a Score recipe and a Predict recipe?@@
```
- [ ] A Score recipe handles classification tasks, but the Predict recipe is for regression tasks.
- [x] They are the exact same operation. The only difference is whether a dataset or a model is selected first from the Flow.
- [ ] They have different inputs: data to score for a Score recipe and a saved model for a Predict recipe.
