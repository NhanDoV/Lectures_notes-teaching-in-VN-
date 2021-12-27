## Theory
[link](https://academy.dataiku.com/path/advanced-designer/flow-views-actions)

## Practices
### Quiz 1. Flow Views
``` diff
@@ Question 1. The “Partitions count” view shows you the number of partitions in a partitioned dataset, whether the partitions have been built or not. @@
```
- [ ] True. This view displays all the partitions that could potentially be built.
- [x] **False. This view allows you to see the number of partitions only for partitions that have already been built.**

``` diff
@@ Question 2. Which of the options below can NOT be seen from the View menu of the Flow? @@
```
- [ ] File size
- [x] **Column count**
- [ ] Partitioning schemes
- [ ] Count of records

``` diff
@@ Question 3. Imagine a Flow that takes several hours to build. Which two actions would be the most efficient for identifying the parts where optimization efforts would have the greatest impact? (Select two).@@
```
- [ ] Click "Build All" from the Flow, and then check how long it took for each activity in the Jobs menu.
- [ ] Open each recipe, click "RUN", and record how long it takes.
- [x] **Use the "Connections" and "Recipe engines" views to see if connections and engines can be optimized.**
- [x] **Use the "Count of records" and "File size" views to get an idea about which parts of the Flow contain large datasets.**

### Quiz 2: Flow action.
``` diff
@@ Question 1. When you change a dataset’s connection, the dataset contains its existing data and does NOT need to be rebuilt.@@
```
- [x] **False. Changing the dataset connection transfers its schema; the resulting dataset is empty and would need to be rebuilt.**
- [ ] True. Changing the dataset connection does not require rebuilding the dataset.

``` diff
@@ Question 2. A ‘non-recursive’ build is the default option for building a dataset in the Flow.@@
```
- [x] **True. The default option is to build only the dataset by running the parent recipe.**
- [ ] False. The default option is to recursively build the dataset and any outdated dependencies.

``` diff
@@ Question 3. When you perform a forced recursive build on a dataset in your Flow, a required upstream dataset will NOT be rebuilt if the ‘rebuild-behavior’ setting of the upstream dataset is ‘write-protected’.@@
```
- [x] **True. A forced recursive rebuild cannot override the read-only behavior of a ‘write-protected’ dataset.**
- [ ] False. A forced recursive rebuild will override the read-only behavior of a ‘write-protected’ dataset

``` diff
@@ Question 4. Schema consistency checks are automatically performed when rebuilding a dataset from which of the following?@@
```
- [x] **A recipe’s editor screen**
- [ ] The dataset’s Actions menu
- [ ] A scheduled job in a scenario
- [ ] The Flow

``` diff
@@ Question 5. By default, the Schema Propagation tool detects all downstream recipes that require schema updates.@@
```
- [ ] True. The Schema Propagation tool can detect outdated schemas for the output of any recipe.
- [x] **False. The Schema Propagation tool cannot detect outdated output dataset schemas for some recipes without first running them. For example, code recipes, or a Pivot recipe.**

### Final
``` diff
@@ Question 1. Which of the options below can be seen from the View menu of the Flow?@@
```
- [ ] Recipe engines
- [ ] Tags
- [x] **All of these**
- [ ] Dataset connections

``` diff
@@ Question 2. When you perform a forced recursive build on a dataset in your flow, a required upstream dataset will NOT be rebuilt if... (choose three)@@
```
- [x] **The 'rebuild-behavior' setting of the upstream dataset is ‘explicit’.**
- [x] **The ‘rebuild-behavior’ setting of the upstream dataset is ‘write-protected’.**
- [ ] The data in the upstream dataset is up-to-date.
- [x] **The upstream dataset is shared from a different source project.**

``` diff
@@ Question 3. Which of the following changes CANNOT be detected by a schema consistency check?@@
```
- [ ] Change in a column’s storage type
- [ ] Change in the number of columns in a dataset
- [x] **Change in a column’s inferred meaning**
- [ ] Change in column name

``` diff
@@ Question 4. True or false: When your flow includes a shared dataset from another project, the shared dataset must be re-built from its source project.@@
```
- [x] **True. The shared dataset must be rebuilt from the Flow where it was created.**
- [ ] False. If a forced recursive build from your flow requires a re-build of the shared dataset, it will be rebuilt.

``` diff
@@ Question 5. True or false: When you copy a recipe to an existing project or a new project, the recipe’s input dataset will be shared between the source and destination projects. @@
```
- [x] **True. Both the recipe and its input dataset will be shared.**
- [ ] False. Only the recipe will be shared.

``` diff
@@ Question 6. For which of the following recipes can the Schema Propagation tool detect an outdated output schema without having to first run the recipe?@@
```
- [ ] Python recipe
- [x] **Prepare recipe**
- [ ] R recipe
- [ ] Pivot recipe

``` diff
@@ Question 7. When performing a recursive build of a dataset, which of these is NOT a valid option that you can choose from?@@
```
- [ ] Smart reconstruction
- [x] **Flow outputs reachable from here**
- [ ] Missing data only
- [ ] Forced recursive rebuild

``` diff
@@ Question 8. When you duplicate a code recipe for the purpose of applying it to a different input dataset, you only need to choose the desired input dataset in the dialog for copying the recipe.@@
```
- [ ] True. DSS automatically changes the code in the recipe to reflect the new input dataset’s name.
- [x] **False. You must also manually change the input dataset’s name inside your code to the configured input.**

``` diff
@@ Question 9. Imagine a Flow with more than 100 datasets and recipes. Which Flow view would provide you useful information for identifying the parts that take a long time to compute? Choose two.@@
```
- [ ] The “Last build” view to see which datasets were built recently. These must be the fast ones to build.
- [x] **The “Connections” and “Recipe engines” views to see if connections and engines can be optimized for heavy-computation areas.**
- [ ] The “Creation” view to see when objects were created. Older objects always take longer to build.
- [x] **The “Count of records” view to identify the largest datasets in the Flow.**

``` diff
@@ Question 10. If you take action from a destination project to stop sharing a dataset that is connected to a recipe, the dataset gets deleted from the flow of the destination project.@@
```
- [ ] True. Because the dataset is no longer needed in the destination project.
- [x] **False. You will only lose access to open the dataset in the destination project.**
