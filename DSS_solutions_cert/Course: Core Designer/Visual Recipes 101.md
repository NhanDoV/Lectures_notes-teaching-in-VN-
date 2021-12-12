# 
## Theory
https://academy.dataiku.com/path/core-designer/visual-recipes-overview-1

## Quiz final
```diff
@@ Question 1. The group keys of a Pivot Recipe determine which rows will be transformed into columns. @@
``` 
- [ ] ~~True. DSS uses the group key or keys and transforms them into columns.~~
- [x] False. The pivot column determines this; the group keys determine the row names.

```diff
@@ Question 2. You have two datasets and both contain a single column, customerID. Stacking the two datasets by the intersection of the input schemas would result in the same output dataset if you joined the two datasets using an inner join.@@
```
- [ ] ~~True. Stack by intersection of input schemas or joining using an inner join retrieves only the matching rows from both datasets.~~
- [x] **False. Stack by intersection of input schemas retrieves all rows of both datasets and stacks them. Joining using an inner join retrieves only the matching rows from both datasets.**

```diff
@@ Question 3. DSS automatically recognizes dates as strings so that you don’t have to parse them.@@
```

- [x] **If a column appears to be a Date column that has not yet been parsed, DSS recognizes it and suggests the Parse date processor.** [See Basic 102, question 2 checkpoints]
- [ ] ~~If a column appears to be a Date column, there is no need to parse it in order to use it as a Date column.~~

```diff
@@ Question 4. If a dataset of six rows with three distinct customers is grouped by customers, the output dataset will also contain six rows.@@
```
- [x] **False. The Group Recipe reduces the input dataset to the number of distinct values in the group key. For example, in the above scenario, the output dataset would only contain three rows.** [See Question 3. in Group the data Basic 102]
- [ ] ~~True. The Group Recipe keeps the original dimensions of the input dataset and appends the aggregations to the dataset.~~

```diff
@@ Question 5. Your dataset contains the predicted revenue for five customers, where rows contain the values of 2565, 4398, 3571, 4432, and 5598. You have configured the Top N recipe to retrieve the top and bottom row and sort the data in ascending order. Which of the following best represents the output dataset?@@
```
- [x] 2565; 5598
- [ ] ~~5598; 2565~~
- [ ] ~~5598; 4398~~
- [ ] ~~2565; 3571.~~

```diff
@@ Question 6. Which of the following does not describe a feature of the DSS Pivot Recipe?@@
```
- [ ] ~~Multiple columns can be defined as group keys simultaneously~~
- [x] Columns with over 20 categories cannot be selected as pivot columns
- [ ] ~~Possible aggregations include: count, max, sum and average.~~

```diff
@@ Question 7. Which of the following is not a valid splitting method in DSS?@@
```
- [ ] ~~Map values on a single column~~
- [x] Split on dataset name
- [ ] ~~Dispatch based on percentiles of sorted data.~~

```diff
@@ Question 8. Which of the following is not a stacking method in DSS?@@
```
- [ ] ~~Manual remapping~~
- [x] **Alphabetical column order**
- [ ] ~~Intersection of input schemas~~

```diff
@@ Question 9. Which of the following actions would result in a new output dataset?@@
```
- [ ] ~~Configuring a visual recipe without running it~~
- [x] Running a visual recipe
- [ ] ~~Running a recipe never results in a new output dataset~~
- [ ] ~~Adding a step to an existing Prepare Recipe.~~

```diff
@@ Question 10. Which of the following types of  expressions could you use in a Formula step? (Select all that apply.)@@
```
- [x] Conditional if-then statements
- [x] Comparison operators, such as >, <, >=, <=
- [x] String operations with functions like contains(), length(), and startsWith()
- [x] Tests for missing values, such as isBlank() or isNULL()
- [x] Common mathematical functions, such as round, sum and max.

```diff
@@ Question 11. Which quantity does not need to be defined when creating a Pivot Recipe?@@
```
- [ ] ~~Pivot Column~~~~
- [x] Window
- [ ] ~~Aggregations~~
- [ ] ~~Group key~~
