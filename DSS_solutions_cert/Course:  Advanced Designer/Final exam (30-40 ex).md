``` diff
@@ Question 1. Which of the following statements about the Pivot recipe is false?@@
```
- [ ] Possible aggregations include: count, max, sum and average.
- [ ] Multiple columns can be defined as row identifiers.
- [x] If no row identifier columns are selected, there is a single row of output.
- [ ] Columns with over 20 categories cannot be selected as pivot columns.
- [ ] The schema of the output dataset cannot be computed until the first time a Pivot recipe is run.

``` diff
@@ Question 2. Use the Advanced Designer Certificate Assessment project to answer this question. If you removed stock_code as the Partitioning column from the Window recipe, could you still find the rolling average for each stock_code?@@
```
- [ ] No, removing these groupings changes what rows are included in the window frame.
- [ ] Yes, just interactively filter the output by stock_code.
- [x] It depends on the configuration of the Order column and Window frame.


``` diff
@@ Question 3. Imagine a Flow with more than 100 datasets and recipes. Which views are most likely to provide useful information for identifying the parts that take a long time to compute? Select two choices.@@
```
- [x] The “Count of records” view to identify the largest datasets in the Flow.
- [x] The “Last build” view to see which datasets were built recently.
- [ ] The “Connections” and “Recipe engines” views to see if connections and engines can be optimized for heavy-computation areas.
- [ ] The “Creation” view to see when objects were created.


``` diff
@@ Question 4. Which two settings are required in order to run a Top N recipe? Select two answers.@@
```
- [x] The number of top and/or bottom rows to display
- [ ] Statistics to compute for each row
- [ ] An explicit list of columns to retrieve
- [ ] The column to identify groups of rows
- [x] At least one column to sort by


``` diff
@@ Question 5. Use the Advanced Designer Certificate Assessment project to answer this question. You used the Schema Propagation tool to update the schema of the Distinct recipe's output. You could have also used a forced recursive rebuild to add the schema changes in the Prepare recipe to downstream datasets.@@
```
- [ ] True. The forced recursive build mode ensures not only the latest data, but also any schema updates from upstream datasets.
- [x] False. Schema propagation and dataset building are separate actions.


``` diff
@@ Question 6. Which of the following statements about plugins are true? Select three that apply.@@
```
- [x] A plugin that has been customized by a user can still receive future updates from the store.
- [x] Once a plugin is installed on an instance of Dataiku, it can be used in any project on the instance.
- [x] Any user (with any permission) can install plugins from the Dataiku plugin store.
- [ ] Plugins can contain multiple components, such as recipes or processors.
- [ ] A plugin's source code can be changed after installing it from the plugin store.


``` diff
@@ Question 7. Use the Advanced Designer Certificate Assessment project to answer this question. Why did the schema consistency check fail after updating the Prepare recipe?@@
```
- [ ] An expected column used in a recipe downstream was removed.
- [ ] The storage location of the output was changed.
- [x] The values in a column are different from what was expected after changing a Formula.
- [ ] The expected number of rows changed due to the removal of TEST rows.


``` diff
@@ Question 8. Which of the following statements is true of metrics and checks?@@
```
- [ ] Metrics and checks are always recomputed after a dataset is rebuilt.
- [ ] Metrics and checks are always used in conjunction with a scenario.
- [x] You can compute metrics and checks for each partition of a partitioned dataset.
- [ ] Metrics and checks are found on the Statistics tab of a dataset.
- [ ] Metrics can be computed for datasets, recipes, models, and managed folders.


``` diff
@@ Question 9. Which of the following Formulas correctly uses the substring function to retrieve only the last two characters of a string column named "my_column"?@@
```
- [ ] substring(my_column, 0, -2)
- [x] **substring(my_column, -2)**
- [ ] substring(my_column, 2, 0)
- [ ] substring(my_column, 2)


``` diff
@@ Question 10. Use the Advanced Designer Certificate Assessment project to answer this question. What was the average quantity for the stock item "84077" (World War 2 Gliders Asstd Designs) that was sold during the week of "2010-11-01"? Tip: Look in the Product-Centric-Flow using the Tag views. @@
```
- [ ] 12.04
- [ ] 89.14
- [x] 402.46
- [ ] 13.08
- [ ] 1006.56

``` diff
@@ Question 11. Use the Advanced Designer Certificate Assessment project to answer this question. Which object is NOT tagged as being "Skeleton Project"?@@
```
- [ ] Online_Retail_Distinct
- [ ] Product_Aggregated
- [ ] compute_Online_Retail_Stacked
- [x] **Online_Retail_Prepared**
- [ ] Stacked_Online_Retail


``` diff
@@ Question 12. Which one of the following is NOT a valid example of using variables in Dataiku?@@
```
- [ ] Create a global variable for an API key.
- [ ] Save the input of a Dataiku Application as a variable.
- [ ] Use the same variable in both visual and code recipes.
- [x] Define a project variable in one project and then use that variable in another project.
- [ ] Update project variables in a step of a scenario.


``` diff
@@ Question 13. Metrics and checks cannot be computed on which of the following objects?@@
```
- [x] Models
- [ ] Recipes
- [ ] Datasets
- [ ] Managed Folders


``` diff
@@ Question 14. Use the Advanced Designer Certificate Assessment project to answer this question. At what step in the "Initial Build" scenario, does the scenario fail?@@
```
- [ ] At Step #2, only a subset of the metric calculations can be performed.
- [x] At Step #5, the dataset to be built cannot be found.
- [ ] At Step #3, a check on column counts fails or cannot be evaluated.
- [ ] At Step #6, the project variable is not defined as a JSON object.
- [ ] At Step #1, the initial project is in an inconsistent state.


``` diff
@@ Question 15. Which of the following is NOT an example of a metric?@@
```
- [ ] The accuracy of a machine learning model
- [x] The minimum value of a column
- [ ] The most frequent values of a column
- [ ] Whether or not a column has more than three missing values
- [ ] The number of files in a folder


``` diff
@@ Question 16. Which of the following statements about the Window recipe is true?@@
```
- [x] In order to correctly compute the rank for each row, an Order column must be specified.
- [ ] If you define multiple windows, each window must be computed with the same Partitioning columns.
- [ ] In order for a Window recipe to work, all three Window definitions (Partitioning columns, Order columns, and Window frame) need to be activated.
- [ ] On the Aggregations step, you can compute custom aggregations with the DSS formula language.

``` diff
@@ Question 17. Which of the following are the two minimum required components for a functioning scenario? Select two.@@
```
- [ ] A reporter to send scenario information via several available channels.
- [ ] A code snippet to stop the scenario on certain conditions.
- [x] Trigger(s) that activate the scenario.
- [x] Metrics and checks defined for any dataset built by the scenario.
- [ ] A sequence of steps or a custom script to run when the scenario launches.


``` diff
@@ Question 18. In which of the following visual recipes is the Pre-filter step NOT available?@@
```
- [x] **Prepare**
- [ ] Window
- [ ] Group
- [ ] Pivot

``` diff
@@ Question 19. Use the Advanced Designer Certificate Assessment project to answer this question. Which of the following is NOT one of the ten most common product descriptions in the output to the Distinct recipe?@@
```
- [ ] White Hanging Heart T Light Holder
- [ ] Strawberry Ceramic Trinket Box
- [x] Regency Cakestand 3 Tier
- [ ] Rex Cash Carry Jumbo Shopper

``` diff
@@ Question 20. Use the Advanced Designer Certificate Assessment project to answer this question. From your calculations of the top 5 customers from each year, which customerid represented the third highest total revenue in 2009?@@
```
- [x] 15061
- [ ] 17450
- [ ] 13694
- [ ] 14191


``` diff
@@ Question 21. Your dataset contains the predicted revenue for five customers, where rows contain the values of 2565, 4398, 3571, 4432, and 5598. You have configured the Top N recipe to retrieve the top and bottom row and sort the data in descending order. Which of the following best represents the values in the output dataset?@@
```
- [ ] 4398, 5598
- [ ] 2565, 5598
- [ ] 5598, 4398
- [ ] 2565, 3571
- [x] 5598, 2565


``` diff
@@ Question 22. The output to a Window recipe will have the same number of rows as its input dataset.@@
```
- [ ] It cannot be known without knowing the kinds of aggregations included.
- [ ] Always true. This is the key differentiator between Group and Window recipes.
- [ ] False. The number of rows depends on the number of groups in the partitioning column.
- [x] Sometimes true. If a pre- or post-filter step is used, the number of rows may be different.


``` diff
@@ Question 23. Use the Advanced Designer Certificate Assessment project to answer this question. After retaining only records with a quantity greater than or equal to 2000 units, what was the 4 week rolling average on total quantity sold for the stock item 84077 on 2010-11-29?@@
```
- [ ] 3809
- [ ] 3097.5
- [ ] 3318.38
- [x] 3732.75

``` diff
@@ Question 24. Use the Advanced Designer Certificate Assessment project to answer this question. The Group recipe that creates the Product_Aggregated Dataset uses a Post-filter step to remove products with low quantities of sales. It would have been more efficient to use a Pre-filter step.@@
```
- [ ] True. These rows could be removed before the Group operation.
- [ ] Both options are exactly the same.
- [x] False. The column used as the filter condition is only created in the Group step.


``` diff
@@ Question 25. Which of the following is the correct Formula expression for creating a column that outputs “True” if the number of characters in a column called “Free Text Response” is greater than 50, and otherwise “False”?@@
```
- [ ] if(length(strval("Free Text Response")) > 50, "False", "True")
- [ ] if(length(numval("Free Text Response")) > 50, "True", "False")
- [x] **if(length(strval("Free Text Response")) > 50, "True", "False")**
- [ ] if(length("Free Text Response") > 50, "True", "False")


``` diff
@@ Question 26. Use the Advanced Designer Certificate Assessment project to answer this question. For stock item 22197, what was the largest gap in days between any two weeks of qualifying purchases in the windowed output?@@
```
- [ ] 14
- [ ] 182
- [x] 84
- [ ] 7

``` diff
@@ Question 27. Which of the following statements are true of scenarios? Select two that apply.@@
```
- [ ] Only projects with Python recipes in the Flow can have scenarios that execute custom Python code.
- [ ] Custom code is required for a scenario that triggers when a dataset managed by DSS changes.
- [ ] In order for a scenario with multiple triggers to run, all of the triggers must be satisfied.
- [x] To launch a scenario when there are changes in a SQL database, you should use the "Trigger on a SQL query change".
- [x] The "Last runs" tab of a scenario will list all runs of a scenario.



``` diff
@@ Question 28. The schema consistency check CANNOT detect changes in which of the following?@@
```
- [ ] Column names
- [ ] Column storage types
- [ ] The number of columns in a dataset
- [x] Column values


``` diff
@@ Question 29. What two settings are the absolute minimum requirement in order to run a Pivot recipe? Select two answers.@@
```
- [x] Pivot column
- [ ] Row identifier column
- [ ] Custom aggregations
- [x] At least one aggregation to populate the pivoted columns


``` diff
@@ Question 30. Which of the following types of components can a single plugin contain?@@
```
- [ ] Webapps
- [ ] Datasets
- [ ] Recipes
- [x] All of these are valid components.
- [ ] Processors


16/30
``` diff
@@ Question 31. Use the Advanced Designer Certificate Assessment project to answer this question. What are the two most popular colors among product descriptions according to the word cloud on the distinct dataset? Select two.@@
```
- [ ] Red
- [x] Pink
- [ ] Blue
- [ ] White
- [x] Black

``` diff
@@ Question 32. The ___________ recipe offers a Computed Columns step to create a new column with a ___________. Assuming the input dataset is SQL-based, select two choices that are true.@@
```
- [x] Window, SQL expression
- [ ] Split, Python code
- [x] Group, DSS Formula
- [ ] Prepare, DSS Formula

``` diff
@@ Question 33. A smart recursive build is a safe way to ensure schema changes have been propagated throughout the Flow.@@
```
- [ ] You need to use the schema propagation tool instead.
- [x] Yes, this will take care of it with the minimal amount of computation.
- [ ] A simple non-recursive build will do it!
- [ ] You need a forced recursive build if there are schema changes.
