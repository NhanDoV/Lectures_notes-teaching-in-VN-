## Theory
https://academy.dataiku.com/path/core-designer/basics-102/

## Practices
### Quiz 1: Prepare Your Data.

``` diff
@@ Question 1: Which of the following is not true of the processing logic in DSS?@@
```
- [ ] ~~It is separate from datasets.~~
- [x] **When the underlying storage infrastructure of the dataset changes, it impacts the processing logic found in the recipes of a Flow.**
- [ ] ~~Coders can define their own processing logic in a code recipe.~~
- [ ] ~~Keeping processing logic in recipes allows you to see a clear data lineage in a project from the imported data to the output dataset.~~

``` diff
@@ Question 2: What are some ways you can add steps to the script in a Prepare Recipe? (Select all that apply.)@@
```
- [x] **Drag columns to adjust their order**
- [x] **Add a step directly from the processor library**
- [x] **Select suggested steps from a column’s context menu**
- [x] **Add steps through the Analyze window**
 
``` diff
@@ Question 3: Once a step has been added to a Prepare recipe script, DSS immediately applies that step to the full input dataset.@@
```
- [x] **False. The step is immediately applied to the current dataset sample, allowing for immediate visual feedback. The step is not applied to the full input dataset until the recipe is run.**
- [ ] ~~True. The step is immediately applied to the full input dataset, but you can disable the step preview if it takes too long.~~
 
``` diff
@@ Question 4: Which of the following types of expressions could you use in a Dataiku Formula step? Select all that apply@@
```
- [x] **Comparison operators: >, <, >=, <=**
- [x] **Common mathematical functions: round, sum, max**
- [x] **Logical operators: AND, OR**
- [x] **Tests for missing values: isBlank(), isNULL()**

``` diff
@@ Question 5: DSS automatically recognizes dates as strings so that you don’t have to parse them.@@
```
- [x] **False. If a column appears to be a Date column that has not yet been parsed, DSS recognizes it and suggests the "Parse date" processor.**
- [ ] ~~True. If a column appears to be a Date column, there is no need to parse it in order to use it as a Date column.~~

### Quiz 2. Interactive Visual Statistics.

``` diff
@@ Question 1:  What is the default sampling method that is applied to the dataset in the worksheet?@@
```
- [x] **First records**
- [ ] ~~Last records~~
- [ ] ~~Random~~
- [ ] ~~No sampling~~

``` diff
@@ Question 2: Which of these options is not available in the Worksheet drop-down menu?@@
```
- [x] **Publish**
- [ ] ~~Rename~~
- [ ] ~~New Worksheet~~
- [ ] ~~Delete~~

``` diff
@@ Question 3: What card menu gives you the option to group your dataset by a specified variable, so that you can perform computations on each data subgroup?@@
```
- [ ] ~~Sampling menu~~
- [ ] ~~Group by menu~~
- [ ] ~~Configuration menu~~
- [x] **Split by menu**

### Quiz 3. Group the Data.

``` diff
@@ Question 1: What are the two components used to configure the Group recipe?@@
```
- [ ] ~~Input and output datasets~~
- [x] **Group key and aggregations**
- [ ] ~~Key columns and filters~~
- [ ] ~~Aggregations and column headings~~
 
``` diff
@@ Question 2: Although the Group recipe allows you to select an unlimited number of aggregations, you may only select one column as the group key.@@
```
- [ ] ~~True. In the Group recipe, only one column can serve as the group key at a time. You can open a code notebook to group by more than one column at a time.~~
- [x] **False. When initiating a Group recipe, you must first choose one column to group by. However, on the following Group step, it is possible to add more columns to the group key.**

``` diff
@@ Question 3: If a dataset of six rows with three distinct customers is grouped by customers, the output dataset will also contain six rows.@@
```
- [ ] ~~True. The Group recipe keeps the original dimensions of the input dataset and appends the aggregations to the dataset.~~
- [x] **False. The Group recipe reduces the input dataset to the number of distinct values in the group key. For example, in the above scenario, the output dataset would only contain three rows.**

### Quiz 4. Explore the flow

``` diff
@@ Question 1:  Which of the following statements are true about tags in the Flow? (Choose three.)@@
```
- [x] **Tags can help you interpret the Flow.**
- [ ] ~~Tags must be applied to two or more objects and cannot be applied to a single object in the Flow.~~
- [x] **When there are too many objects on screen, you can select to view parts of the Flow using tags.**
- [x] **Tags can be based on attributes such as creator, purpose, and status.**

``` diff
@@ Question 2: Which of the following statements are true of computation in Dataiku DSS? (Select all that apply.)@@
```
- [x] **The Dataiku DSS computation strategies aim to reduce the cost of computation.**
- [x] **Dataiku can perform computations using either the DSS engine or an external engine that has been configured.**
- [x] **When adding transformation steps to a recipe, you’re actually working with a sample of the dataset.**

``` diff
@@ Question 3: Once a user makes changes to a dataset downstream in a Flow, they can choose to dynamically rebuild dependent items upstream or downstream.@@
```
- [x] **True. Dataiku DSS is aware of the relationships and dependencies between datasets in a project.**
- [ ] ~~False. Dataiku DSS does not have an awareness of the relationships and dependencies between datasets in a project.~~

### Final & summary

``` diff
@@ Question 1:  When creating interactive statistics, all cards have a configuration menu that includes options for doing all but this:@@
```
- [x] **View Python Code**
- [ ] ~~Publish~~
- [ ] ~~View JSON Code~~
- [ ] ~~Duplicate~~
 
``` diff
@@ Question 2: DSS automatically recognizes dates as strings so that you don’t have to parse them.@@
```
- [ ] ~~True. If a column appears to be a Date column, there is no need to parse it in order to use it as a Date column.~~
- [x] **False. If a column appears to be a Date column that has not yet been parsed, DSS recognizes it and suggests the Parse date processor.**

``` diff
@@ Question 3:  When creating a recipe: (Choose three.)@@
```
- [x] **The user selects the input dataset and the output dataset**
- [ ] ~~The input dataset can be outside the Flow~~
- [x] **The user can tell DSS where to store the output data**
- [x] **The user can create a visual recipe or a code recipe**
 
``` diff
@@ Question 4:  What are some of the ways you can help project collaborators understand and become familiar with your project? (Select all that apply.)@@
```
- [x] **Use short simple titles for the project’s name**
- [x] **Add a wiki page**
- [x] **Create and use tags**
- [x] **Adopt a dataset naming convention**

``` diff
@@ Question 5: In this course, we learned that computation in Dataiku can take four main forms. Which of the following computation forms uses container execution:@@
```
- [ ] ~~In Database~~
- [ ] ~~In DSS Engine~~
- [ ] ~~On a Hadoop or Spark Cluster~~
- [x] **In Kubernetes or Docker**
