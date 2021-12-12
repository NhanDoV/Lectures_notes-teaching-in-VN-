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
