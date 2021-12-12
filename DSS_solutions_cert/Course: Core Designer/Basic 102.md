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
