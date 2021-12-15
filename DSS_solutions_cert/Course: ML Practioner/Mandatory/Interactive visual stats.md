## Theory
https://academy.dataiku.com/path/ml-practitioner/interactive-visual-statistics-1

## Practices
### Quiz 1: The Interactive Visual Statistics Interface.
``` diff
@@ Question 1: What is the default sampling method that is applied to the dataset in the worksheet?@@
```
- [ ] Last records
- [ ] Random
- [x] **First records**
- [ ] No sampling

``` diff
@@ Question 2: What card menu gives you the option to group your dataset by a specified variable, so that you can perform computations on each data subgroup?@@
```
- [ ] Sampling menu
- [x] **Split by menu**
- [ ] Configuration menu
- [ ] Group by menu

``` diff
@@ Question 3: Which of these options is not available in the Worksheet drop-down menu?@@
```
- [ ] Delete
- [x] **Publish**
- [ ] New Worksheet
- [ ] Rename

### Quiz 2: Univariate and Bivariate Analysis.
``` diff
@@Question 1: True or False. If I change the way that a variable “age” is used (from continuous to categorical) in a bivariate analysis card, by default, Dataiku will change the way that “age” is treated in other existing cards in the worksheet.@@
```
- [ ] True. Dataiku will update all the other existing cards in the worksheet that use “age” so that those cards also treat “age” as a categorical variable.
- [x] **False. Changing the way that a variable is used in one card will not affect how the same variable is used in another card of the worksheet.**

``` diff
@@ Question 2: True or False. A scatterplot of a dataset shows a factor variable on the x-axis and the response variable on the y-axis.@@
```
- [ ] False. The factor variable is plotted on the y-axis.
- [x] **True. The response variable is plotted on the y-axis.**

``` diff
@@ Question 3: In Dataiku, the character “A” next to a variable name indicates which kind of variable?@@
```
- [ ] A timestamp
- [x] **A categorical variable**
- [ ] None of the above
- [ ] A numerical variable

``` diff
@@ Question 4: When creating a bivariate analysis card in Dataiku DSS, you can select ______ variable(s) to use as the factor and _______ variable(s) to use as the response.@@
```
- [ ] “multiple” and “multiple”
- [x] **“multiple” and “a single”**
- [ ] “a single” and “multiple
- [ ] “a single” and “a single”.

### Quiz 3: Fit Curves and Distributions.
``` diff
@@ Question 1: Specifying smaller values for the X and Y relative bandwidth parameters has what effect on the KDE plot?@@
```
- [x] Less smoothing
- [ ] More smoothing
- [ ] Rotation by a given degree
- [ ] No effect

``` diff 
@@ Question 2: Which probability distribution function has a bell-shaped curve?@@
```
- [ ] Uniform
- [x] **Gaussian (normal)**
- [ ] Exponential
- [ ] Triangular

``` diff
@@ Question 3: DSS uses what kind of kernel for the 2-dimensional KDE plot?@@
```
- [ ] Uniform
- [ ] Triangular
- [ ] Beta
- [ ] Gaussian (normal)

``` diff
@@ Question 4: True or False: Observing points far from the identity line in a Q-Q plot indicates a good fit of the selected distribution to the data.@@
```
- [x] **False. Points far from the identity line indicate that the data could not come from the selected distribution.**
- [ ] True. Points far from the identity line indicate that the data could come from the selected distribution.

``` diff
@@ Question 5: When using a fit curve to model the relationship between variables, which option(s) require(s) you to specify a value for the degree?@@
```
- [ ] Both
- [ ] Isotonic
- [ ] None
- [x] Polynomial

### Quiz 4: Correlation Matrix.
``` diff
@@ Question 1: Correlation coefficient values can range from:@@
```
- [ ] 0 to 1
- [ ] -infinity to infinity
- [x] **-1 to 1**
- [ ] -1 to 0

``` diff
@@ Question 2: What options are available for configuring visualization of the correlation matrix in the card (Choose all that apply)?@@
```
- [x] Set a threshold
- [x] Show absolute values
- [x] Show values as text
- [x] Show values as colors

``` diff
@@ Question 3: Which of these are true about the properties of a correlation matrix (Choose all that apply)?@@
```
- [x] The matrix is square
- [x] The values on the diagonal equal 1
- [ ] The values on the diagonal equal 0
- [x] The matrix is symmetric

``` diff
@@ Question 4: True or False: Pearson’s coefficient can detect nonlinear monotonic relationships between variables.@@
```
- [ ] True. Pearson’s coefficient is robust and detects both linear and nonlinear relationships.
- [x] False. Pearson’s coefficient detects only linear relationships, but Spearman’s coefficient can detect nonlinear monotonic relationships.

### Quiz 5: Principal Component Analysis.
``` diff
@@ Question 1: True or False: The cumulative explained variance increases as you increase the number of principal components.@@
```
- [ ] False. Using fewer principal components increases the explained variance in the data.
- [x] True. Using more principal components increases the explained variance in the data.

``` diff
@@ Question 2: Which of the following are typical use cases for PCA (Choose three)?@@
```
- [x] Feature processing
- [ ] Regularization
- [x] Representing data in a reduced dimension
- [x] Visualizing data

``` diff
@@ Question 3: True or False: The PCA card in Dataiku DSS works on numerical variables only.@@
```
- [x] True. Only numerical variables can be used in PCA transformation.
- [ ] False. PCA can also transform categorical variables in a meaningful way.

``` diff
@@ Question 4: True or False: For a 2-dimensional scatter plot in the directions of the first two principal component axes, the first principal component shows the largest variation.@@
```
- [ ] False. The variation is always smallest in the direction of the first principal component.
- [x] True. The variation is always largest in the direction of the first principal component.

``` diff
@@ Question 5: The goal of PCA is to represent data in directions that maximize the existing ________ in the data.@@
```
- [x] variations
- [ ] correlations
- [ ] features
- [ ] skewness

### Quiz 6. Statistical Testing
``` diff
@@ Question 1: What number determines how rare an event must be for us to reject the null hypothesis?@@
```
- [ ] p value
- [ ] Test statistic value
- [x] Significance level (alpha)
- [ ] Hypothesized value

``` diff
@@ Question 2: The adjustment methods reduce the probability of making type I errors when making multiple comparisons, by adjusting the observed p-value and comparing it to the ________ .@@
```
- [ ] Confidence interval
- [ ] Sample mean
- [x] pre-specified significance level
- [ ] Number of comparisons

``` diff
@@ Question 3: True or False. If p is greater than the significance level (alpha), DSS will accept the null hypothesis.@@
```
- x] False; p greater than alpha indicates that the test is inconclusive.
- [ ] True; p greater than alpha indicates that the null hypothesis is definitely true.

``` diff
@@ Question 4: Using a grouping variable, you can split your data into groups that are guaranteed to be _____________ .@@
```
- [ ] Correlated
- [x] Disjoint
- [ ] Independent
- [ ] Uncorrelated

``` diff
@@ Question 5: Which of these options is not a way that Dataiku DSS categorizes hypothesis tests?@@
```
- [ ] Location test
- [ ] N-sample test
- [] Inferential test
- [ ] Categorical test

``` diff
@@ Question 6: When you perform a hypothesis test in Dataiku DSS, you can find information about the underlying assumptions for the test by clicking this element in the test card:@@
```
- [ ] Split by menu
- [ ] Configuration menu
- [ ] Gear icon
- [x] Question icon in the card header.

### Final
``` diff
@@ Question 1: Specifying smaller values for the X and Y relative bandwidth parameters has what effect on the KDE plot?@@
```
- [ ] More smoothing
- [ ] Rotation by a given degree
- [x] Less smoothing
- [ ] No effect

``` diff
@@ Question 2: When performing two-sample tests in Dataiku DSS, you specify _______ test variable(s) and a grouping variable with two groups.@@
```
- [x] one
- [ ] multiple
- [ ] two

``` diff
@@ Question 3: What do we call a test that considers more than two populations with independent random samples that are used to make inferences?@@
```
- [x] An N-sample test
- [ ] None of these
- [ ] A two-sample test
- [ ] A one-sample test

``` diff
@@ Question 4: For a _________ test, you specify a numerical test variable and a grouping variable with multiple modalities.@@
```
- [ ] Two-sample test
- [ ] One-sample test
- [ ] Categorical test
- [x] N-sample test

``` diff
@@ Question 5: Which of these are true about the properties of a correlation matrix (Choose all that apply)?@@
```
- [x] The values on the diagonal equal 1
- [x] The matrix is symmetric
- [ ] The values on the diagonal equal 0
- [x] The matrix is square

``` diff
@@ Question 6: In Dataiku DSS, the character “#” next to a variable name indicates which kind of variable? @@
```
- [ ] A categorical variable
- [x] A numerical variable
- [ ] A currency
- [ ] A time stamp

``` diff
@@ Question 7: Which of these options are possible values for the adjustment method parameter in a Pairwise Median Mood Test? (Select all that apply)@@
```
- [ ] Parzen
- [x] Bonferroni
- [x] Holm-Bonferroni
- [ ] Rosenblatt

``` diff
@@ Question 8: True or False. If p is less than or equal to the significance level (alpha), DSS will reject the null hypothesis.@@
```
- [x] True; p less than or equal to alpha is sufficient for rejecting the null hypothesis.
- [ ]  False; p less than or equal to alpha is not sufficient to reject the null hypothesis.

``` diff
@@ Question 9: To group your dataset by a specified variable so that a statistics card can perform computations on each data subgroup, you can use the _______________ card menu.@@
```
- [ ] Sampling menu
- [ ] Configuration menu
- [x] Split by menu
- [ ] Group by menu

``` diff
@@ Question 10: True or False: The cumulative explained variance increases as you increase the number of principal components.@@
```
- [ ] False. Using fewer principal components increases the explained variance in the data.
- [x] True. Using more principal components increases the explained variance in the data.
