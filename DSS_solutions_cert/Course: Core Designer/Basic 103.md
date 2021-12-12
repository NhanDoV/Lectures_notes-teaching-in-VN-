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
- [ ] ~~Steps added to a Prepare Recipe and a visual analysis are immediately available in the Charts Tab.~~
- [x] **You can work interactively in a Prepare Recipe and a visual analysis because both operate on a sample of the dataset.**
- [ ] ~~Columns in a Prepare Recipe and a visual analysis have both storage type and meaning.~~
- [x] **You can use the same library of processors in both a Prepare Recipe and a visual analysis.**

### Quiz 3: Reporting Tools.
``` diff
@@ Question :When a dashboard is marked as "private", it can only be seen by the dashboard creator.@@
```
- [x] **False. A "private" dashboard is private to those who have the correct permissions. Setting it to "public" makes it accessible from the DSS homepage of these same users.**
- [ ] ~~True. Set the dashboard to "public" in order for other project collaborators to see it.~~

``` diff
@@ Question 2: Both R Markdown reports and dashboards can be downloaded as part of automation scenarios.@@
```
- [x] **True. R Markdown reports can be downloaded in a wide variety of formats, and dashboards can be exported as PDF or PNG files.**
- [ ] ~~False. R Markdown reports can be included in automation scenarios (since they are just code), but dashboards must be downloaded manually as they can contain a wide variety of insights.~~
 
``` diff
@@ Question 3: A user who only has the permission to “Read dashboards” will be able to see the source objects of only the insights included in the dashboard -- not all DSS objects in the project.@@
```
- [x] **False. To see any source objects in the project, that user would also need the permission to “Read project content”.**
- [ ] ~~True. If, for example, a dataset is used as a source object in the dashboard, that user would be able to see its content.~~

### Final quiz / summary
``` diff
@@ Question 1:  Which of these are valid reasons for preparing data in a visual analysis instead of directly building a Prepare recipe in the Flow? Choose two.@@
```
- [ ] ~~I want to use a larger library of processors found only in the visual analysis.~~
- [ ] ~~I have access to better collaboration features like commenting steps, discussions, etc in the visual analysis.~~
- [x] **I want to visualize the data in the Charts tab as soon as I’ve added a step without having to build the dataset from a Prepare recipe first.**
- [x] **I want to experiment with preparing the data without overcrowding the Flow in production.**

``` diff
@@ Question 2: Which of the following cannot be included in a DSS dashboard?@@
```
- [ ] ~~Dataset~~
- [ ] ~~Web app~~
- [x] **Recipe**
- [ ] ~~Managed folder~~
 
``` diff
@@ Question 3: Joining two datasets with the Join recipe changes the input datasets.@@
```
- [x] **False. The recipe produces one new output dataset, but the inputs remain the same.**
- [ ] ~~True. Once the datasets are joined into one new dataset, and the original inputs no longer exist.~~

``` diff
@@ Question 4: The primary use case for the Join recipe is to enrich one dataset with columns from another. What is the name of the element that DSS uses to match values in both datasets?@@
```
- [ ] ~~Prepare step~~
- [x] **Key column**
- [ ] ~~Input dataset~~
- [ ] ~~Key value~~
 
``` diff
@@ Question 5: When using the Join recipe, you can only select one column to serve as the join key.@@
```
- [ ] ~~True. A code recipe, such as a SQL recipe, is needed in order to join datasets on multiple columns.~~
- [x] **False. On the Join step, you have full control over the Join conditions, including all columns serving as the key.**

``` diff
@@ Question 6: When choosing columns from two datasets to serve as the join key in a Join recipe, which of the following must be the same for each column?@@
```
- [ ] ~~The answer depends on the join type (left join vs. inner join, etc.)~~
- [ ] ~~The names of the columns~~
- [ ] ~~The number of missing values in the columns~~
- [x] **The storage type of the columns (unless auto cast has been enabled)**

``` diff
@@ Question 7: If you wanted to start building machine learning models in DSS from a visual interface, where would you go?@@
```
- [ ] ~~None of these. All modeling in DSS requires coding on the part of the user.~~
- [ ] ~~A predict or cluster recipe in the Flow (depending on the type of ML task)~~
- [x] ** A visual analysis in the Lab**
 
``` diff
@@ Question 8: In order to join more than two datasets using the Join recipe, which of the following solutions is correct?@@
```
- [x] ** Although only two datasets can be added in the Join recipe creation dialog, more datasets can be added on the Join step.**
- [ ] ~~It is not possible to join more than two datasets at a time with the Join recipe. Perform multiple Join recipes instead.~~

``` diff
@@ Question 9: When a dashboard is marked as "public", only DSS users with the correct permissions can find it on their DSS homepage.@@
```
- [x] **True. For a “public” dashboard to be accessible from the DSS homepage of users, they still need to have the correct permissions.**
- [ ] ~~False. When a dashboard is public, any project collaborator can find it on their DSS homepage.~~
