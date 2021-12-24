## Theory
[link](https://academy.dataiku.com/path/advanced-designer/advanced-partitioning)

## Practices
### Quiz 1. Advanced Partitioning Concepts
``` diff
@@ Question 1. The Partition Redispatch feature is found in the Sync and Prepare recipes. When added to a non-partitioned dataset, the Partition Redispatch feature results in computing all possible partitions within the data, building all partitions at once, regardless of the string value we specify in the Recipe Run options.@@
```
- [ ] False: Targeting specific partition identifiers when redispatching a non-partitioned dataset helps Dataiku DSS improve the partition redispatch process.
- [x] **True: Targeting a specific partition when redispatching a non-partitioned dataset would not be useful.**

``` diff
@@ Question 2. One of the main uses of partitioned datasets is the ability to define partition-level dependencies in recipes.@@
```
- [x] **True. For a given recipe, partition dependencies allow you to compute which partition(s) of the input dataset are required to compute the requested partition(s) of the output dataset.**
- [ ] False. It is possible to define partition-level dependencies, but this must be configured in the dataset before adding the recipe.

``` diff
@@ Question 3. Which outcome is possible when adding a  Sync recipe to a non-partitioned dataset?@@
```
- [ ] Redispatch partitioning according to the values of the output columns.
- [ ] Collect partitioning according to the values of the input columns.
- [x] **Redispatch partitioning according to the values of the input columns.**
- [ ] Collect partitioning according to the values of the output columns.

``` diff
@@ Question 4. The purpose of partitioning in Dataiku DSS is to enable the processing of partitions in parallel.@@
```
- [x] **False: Practical use cases for partitioning include optimizing time-based computations in a Flow, and the creation of targeted features such as those used for a machine learning model.**
- [ ] True: The main use case for partitioning is processing of several partitions at once. For example, If we have transactional records that have been partitioned for the purpose of daily processing for multiple regions, we could use partitioning to process these at the same time in a Flow.

``` diff
@@ Question 5. The Dataiku DSS behavior while building a partitioned dataset can be described as "backwards partition dependency propagation." @@
```
- [ ] False. The activity execution starts at the beginning of the Flow computing the partition dependencies.
- [x] **True. The partition dependency computation starts with the requested output and then looks backward in the Flow.**

``` diff
@@ Question 6. What is the value of using partition redispatching in a Flow? (Select all that apply.)@@
```
- [x] **You can go from a non-partitioned dataset to a partitioned dataset.**
- [ ] You can go from a partitioned dataset to a non-partitioned dataset.
- [ ] You can synchronize partitions between inputs and outputs.
- [x] **You can partition a dataset in a Flow even when the input dataset's underlying structure does not have defined partitions.**

``` diff
@@ Question 7. Which of the following is true about partitioned dataset metrics? (Choose one.)@@
```
- [x] **Metrics can be computed on both the distinct partitions and the entire dataset.**
- [ ] Metrics can only be computed on the distinct data partitions.
- [ ] Metrics are not available when interacting with a partitioned dataset.
- [ ] Metrics can only be computed on the entire dataset.

``` diff
@@ Question 8. Which of the following statements are true about job activities when building partitioned datasets in Dataiku DSS? (Select all that apply.)@@
```
- [x] **A job can have more than one activity.**
- [ ] A job is always composed of a single activity.
- [ ] Activities start before the computation of partition dependencies.
- [x] **An activity is the run of a recipe on a specific partition.**

``` diff
@@ Question 9. Which of the following are true about partitioned datasets in DSS? (Select all that apply.)@@
```
- [ ] Multiple partitioning dimensions can not be activated on a single dataset.
- [x] **Computations such as Charts and Statistics can be performed on some or all partitions.**
- [x] **Multiple discrete dimensions can be activated on a single dataset.**
- [x] **The dataset sample can be configured to include some or all partitions.**

``` diff
@@ Question 10. Which of the following is not one of the three main elements making up the partition dependency computations in Dataiku DSS?@@
```
- [ ] The input partition identifier
- [ ] The partition dependency function type that maps the target partition identifier to the input partition identifier
- [x] **The recipe itself**
- [ ] The target partition identifier


### Quiz 2.  Partitioning in a Scenario
``` diff
@@ Question 1. Which of the following are ways scenarios can add value when building a Flow with partitioned datasets? (Select all that apply.)@@
```
- [x] Both the dataset and the target identifier can be specified either in a Sequence of Steps or a Custom Python Script
- [x] Use of a keyword, such as "PREVIOUS_DAY", in place of the target identifier
- [x] Scenario-level variables can be defined and then used to specify the target identifer, such as a date range or specific period of time.

```diff
@@ Question 2. In a scenario, we can  use keywords, such as "CURRENT_DAY",  to refresh a partition.@@
```
- [ ] False. The only way to automatically refresh a partition in a scenario is to use variables.
- [x] True. For example, The keyword "CURRENT_MONTH" can be used to specify the target identifier, which would compute the partition identifier corresponding to the current month.

### Final
``` diff
@@ Question 1. What is the value of using partition redispatching in a Flow? (Select all that apply.)@@
```
- [x] **You can go from a non-partitioned dataset to a partitioned dataset.**
- [ ] You can synchronize partitions between inputs and outputs.
- [ ] You can go from a partitioned dataset to a non-partitioned dataset.
- [x] **You can partition a dataset in a Flow even when the input dataset's underlying structure does not have defined partitions.**

``` diff
@@ Question 2. Which of the following are ways that partitioning can bring value to a Flow? (Select all that apply.)@@
```
- [x] Using scenarios to refresh partitions.
- [ ] Processing several partitions at once--in parallel.
- [x] Optimization of time-based computations, such as by day or month.
- [x] Targeting data processing on partition identifiers.

``` diff
@@ Question 3. What are some of the things you can do with a dataset partitioned by the time dimension value of "Day"? (Select all that apply.)@@
```
- [x] Create a visual chart on a specific range of days.
- [x] Compute metrics on one or more partitions.
- [x] Automatically build the previous day using a keyword in a scenario.
- [x] Automatically build the last seven days using a scenario.
- [x] Create a univariate analysis on a specific day.

``` diff
@@ Question 4. Which of the following is not one of the three main elements making up the partition dependency computations in Dataiku DSS?@@
```
- [ ] The input partition identifier
- [ ] The target partition identifier
- [ ] The partition dependency function type that maps the target partition identifier to the input partition identifier
- [x] The recipe itself

``` diff
@@ Question 5. Which of the following are true about partitioned datasets in DSS? (Select all that apply.)@@
```
- [ ] Multiple time dimensions can be activated on a single dataset.
- [x] Multiple discrete dimensions can be activated on a single dataset.
- [x] Computations can be performed on some or all partitions.
- [x] The dataset sample can be configured to include some or all partitions.

``` diff
@@ Question 6. Which of the following statements are true about job activities when building partitioned datasets in Dataiku DSS? (Select all that apply.)@@
```
- [x] **An activity is the run of a recipe on a specific partition.**
- [ ] Activities start before the computation of partition dependencies.
- [ ] A job is always composed of a single activity.
- [x] **A job can have more than one activity.**

``` diff
@@ Question 7. Which of the following is representative of one of the ways scenarios can add value when building a Flow with partitioned datasets?@@
```
- [ ] Both the dataset and the target identifier can be specified either in a Sequence of Steps or a Custom Python Script
- [ ] Scenario-level variables can be defined and then used to specify the target identifier, such as a date range or specific period of time.
- [ ] To add flexibility, variables can be defined and then used to build the partition identifier.
- [ ] Use of a keyword, such as "PREVIOUS_DAY", in place of the target identifier
- [x] All of these are true.

``` diff
@@ Question 8. Which of the following is true about partitioned dataset metrics? (Choose one.)@@
```
- [ ] Metrics are not available when interacting with a partitioned dataset.
- [ ] Metrics can only be computed on the distinct data partitions.
- [ ] Metrics can only be computed on the entire dataset.
- [x] Metrics can be computed on both the distinct partitions and the entire dataset.

``` diff
@@ Question 9. Which outcome is possible when adding a  Sync recipe to  a non-partitioned dataset?@@
```
- [ ] Collect partitioning according to the values of the output columns.
- [ ] Collect partitioning according to the values of the input columns.
- [ ] Redispatch partitioning according to the values of the output columns.
- [x] Redispatch partitioning according to the values of the input columns.
