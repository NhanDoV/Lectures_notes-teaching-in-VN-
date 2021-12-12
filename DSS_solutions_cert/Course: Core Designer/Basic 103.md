## Theory
https://academy.dataiku.com/path/core-designer/basics-103

## Practices
### Quiz 1. Enrich the Dataset.
``` diff
@@ Question 1: When using the Join recipe, what could you configure to match the datasets if Dataiku DSS does not automatically discover the join key?@@
```
- [ ] ~~Manually select columns in the Selected columns step of the Join recipe.~~
- [x] **Edit the Join Condition where you can select a join column from each dataset.**
- [ ] ~~Edit the Join Type and then DSS will auto discover the Join key.~~
- [ ] ~~Edit the schema of each dataset.~~
 
``` diff
@@ QQuestion 2: When choosing columns from two datasets to serve as the join key in a Join recipe, which of the following must be the same for each column?@@
```
- [ ] ~~The answer depends on the join type (left join vs. inner join, etc.)~~
- [x] **The storage type of the columns (unless auto cast has been enabled)**
- [ ] ~~The names of the columns~~
- [ ] ~~The number of missing values in the columns~~

``` diff
@@ Question 3: The primary use case for the Join recipe is to enrich one dataset with columns from another. What does DSS use to match values in both datasets?@@
```
- [x] **Key column**
- [ ] ~~Prepare step~~
- [ ] ~~Input dataset~~
- [ ] ~~Key value~~

### Quiz 2. Lab.
``` diff
@@ Question 1: Consider that you have created a visual analysis in the Lab. In the Script tab, you have added steps creating new columns in the dataset. If you save the script, return to the Flow and open the same dataset, will you find these newly-created columns?@@
```
- [x] **No, the new columns only exist in the visual analysis. The script would first need to be deployed to the Flow to find these columns.**
- [ ] ~~Yes, it is the same dataset, and so the columns must be there.~~

``` diff
@@ Question 2: Which of the following tools are found in the Lab? (Select all that apply.)@@
```
- [x] **Code Notebook**
- [ ] ~~Python Recipe~~
- [ ] ~~Prepare Recipe~~
- [x] **Visual Analysis**
 
``` diff
@@ Question 3: Which of the following statements concerning similarities between the Prepare recipe and the visual analysis are true? (Select all that apply.)@@
```
 Steps added to a Prepare Recipe and a visual analysis are immediately available in the Charts Tab.
 You can work interactively in a Prepare Recipe and a visual analysis because both operate on a sample of the dataset.
 Columns in a Prepare Recipe and a visual analysis have both storage type and meaning.
 You can use the same library of processors in both a Prepare Recipe and a visual analysis.
