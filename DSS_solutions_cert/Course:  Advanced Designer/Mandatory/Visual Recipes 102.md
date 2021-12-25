## Theory
[link](https://academy.dataiku.com/path/advanced-designer/visual-recipes-102)
## Practices
### Quiz 1. Common Steps in Recipes
``` diff
@@ Question 1. Imagine a Group recipe that computes the average order price for every unique customer in a dataset of retail transactions. Which of the following would you use to retain only rows of customers with an average order price higher than some value?@@
```
- [x] **Post-Filter**
- [ ] Computed Columns
- [ ] None of these.
- [ ] Pre-Filter

``` diff
@@ Question 2. Which of the following visual recipes DO NOT contain a Pre-filter step? Select two.@@
```
- [ ] Window recipe
- [x] **Sample/Filter recipe**
- [ ] Pivot recipe
- [x] **Prepare recipe**

``` diff
@@ Question 3. If the input dataset is stored in a SQL database, the Computed Columns step of a visual recipe (where this step is found) allows for the creation of new columns using:@@
```
- [x] **Both DSS Formulas and SQL Expressions**
- [ ] DSS Formulas Only
- [ ] SQL Expressions Only
- [ ] None of these.

### Quiz 2. Window Recipe
``` diff
@@ Question 1. Which of the following Window recipe components is NOT required to find the least expensive purchase per unique customer in a dataset of retail transactions?@@
```
- [ ] Partitioning column
- [x] Window frame
- [ ] Post-filter step
- [ ] Order column

``` diff
@@ Question 2. In order for a Window recipe to be valid, all three aspects of Window definition (Partitioning columns, Order columns, and Window frame) need to be activated. @@
```
- [x] False. All three are not necessarily required.
- [ ] True. If all three aspects are not needed, one should use a Group recipe.

``` diff
@@ Question 3. In the Window recipe, a window frame limited by the 10 preceding rows and 0 following rows will include how many rows? Assume this row is not one of the very first rows where the full window frame is not possible.@@
```
- [ ] Cannot be determined.
- [ ] 10
- [x] **11**
- [ ] 9

### Quiz 3. Advanced Formula & Regex.
``` diff
@@ Question 1. How can you access the value of a column as a string in a Formula expression when the column name contains spaces?@@
```
- [ ] Apply the substring() Formula function
- [ ] Write a Formula expression to normalize the column name
- [x] Apply the strval() Formula function
- [ ] Type the column name between double quotation marks

``` diff
@@ Question 2. Which of the following types of expressions could you use in a Formula step? Select all that apply.@@
```
- [x] String operations with functions like length(), substring(), and strval()
- [x] Common mathematical functions, such as round, sum and max
- [x] Comparison operators, such as >, <, >=, <=.
- [x] Conditional if-then statements

``` diff
@@ Question 3. Which of the following is the correct Formula for creating a column that outputs “True” if the value of a column called “Purchase Amount” is greater than 100, and “False” if it is less than or equal to 100?@@
```
- [ ] If(Purchase Amount > 100, "True", "False")
- [x] if(numval("Purchase Amount") > 100, "True", "False")
- [ ] if(strval("Purchase Amount") > 100, "True"), else("False")
- [ ] if(Purchase Amount > 100, "True"), else("False")

### Quiz 4. Pivot Recipe
``` diff
@@ Question 1. Which of the following does NOT describe a feature of the Pivot recipe?@@
```
- [ ] Possible aggregations include: count, max, sum and average
- [x] **Columns with over 20 categories cannot be selected as pivot columns**
- [ ] Multiple columns can be defined as group keys simultaneously
- [ ] It can use a Pre-filter or Computed Column step before the Pivot occurs.

``` diff
@@ Question 2. Which quantity does NOT need to be defined when creating a Pivot recipe? @@
```
- [ ] Aggregations
- [ ] Group key
- [x] **Order column**
- [ ] Pivot column

``` diff
@@ Question 3. Imagine new values are found in the pivoting column after having run the Pivot recipe, which is configured to NOT recompute the schema at each run. What will happen when the recipe is run again?@@
```
- [ ] The dataset rebuild will fail.
- [x] **The dataset will rebuild successfully without the new columns.**
- [ ] The dataset will rebuild successfully including the new columns.
- [ ] It depends if it is a recursive or a non-recursive build.

### Quiz 5. Top N Recipe
``` diff
@@ Question 1. Instead of a Top N recipe, you can always apply the interactive sort in the Explore tab to know the maximum or minimum value of a dataset column.@@
```
- [ ] True. This is actually easier than the Top N recipe.
- [x] False. This can only find the minimum or maximum value in the current sample.

``` diff
@@ Question 2. Which of the following need to be defined in order for the Top N recipe to work? Select two.@@
```
- [ ] The column to identify each group of rows by
- [x] The column to sort by
- [ ] The count of rows in its group
- [x] The number of top and/or bottom values to display

``` diff
@@ Question 3. The predicted revenue for a dataset of five customers is 2565, 4398, 3571, 4432, and 5598. You have configured the Top N recipe to retrieve the single top and bottom row and sorted the data according to predicted revenue in ascending order. From top to bottom, what are the values of the output dataset?@@
```
- [x] 2565; 5598
- [ ] 2565; 3571
- [ ] 5598; 2565
- [ ] 5598; 4398

### Final quiz
``` diff
@@ Question 1. Which of the following need to be defined in order for the Top N recipe to work? Select two.@@
```
- [ ] The count of rows in its group
- [x] **The column to sort by**
- [ ] The column to identify each group of rows by
- [x] **The number of top and/or bottom values to display**

``` diff
@@ Question 2. Imagine new values are found in the pivoting column after having run the Pivot recipe, which is configured to recompute the schema at each run. What will happen when the recipe is run again?@@
```
- [ ] It depends if it is a recursive or a non-recursive build.
- [ ] The dataset rebuild will fail.
- [ ] The dataset will rebuild successfully including the new columns.
- [x] **The dataset will rebuild successfully without the new columns.**

``` diff
@@ Question 3. Which of the following Window recipe components is NOT required to find the most recent purchase per unique merchant in a dataset of retail transactions?@@
```
- [ ] Order column
- [ ] Post-filter step
- [x] Window frame
- [ ] Partitioning column

``` diff
@@ Question 4. Which of the following are features of the Pivot recipe? Select two.@@
```
- [ ] It always recomputes the output schema when running.
- [ ] Multiple columns can be defined as group keys simultaneously
- [x] Possible aggregations include: count, max, sum and average
- [x] Both Pre-Filter and Post-Filter can be leveraged as steps in the Pivot recipe

``` diff
@@ Question 5. Imagine a Group recipe that computes the average order price for every unique customer in a dataset of retail transactions. Which of the following would you use to retain only rows of customers with an average order price higher than some value?@@
```
- [ ] Computed Columns
- [ ] Pre-Filter
- [x] **Post-Filter**
- [ ] None of these.

``` diff
@@ Question 6. Which of the following is the correct Formula for creating a column that outputs “True” if the value of a column called “Purchase Amount” is greater than 100, and “False” if it is less than or equal to 100?@@
```
- [ ] If(Purchase Amount > 100, "True", "False")
- [x] **if(numval("Purchase Amount") > 100, "True", "False")**
- [ ] if(strval("Purchase Amount") > 100, "True"), else("False")
- [ ] if(Purchase Amount > 100, "True"), else("False")

``` diff
@@ Question 7. Which of the following uses the correct syntax to call the value of a project variable named "my_var" in a Pre-filter step (to give one example)?@@
```
- [ ] !{my_var}
- [ ] $my_var
- [x] **${my_var}**
- [ ] $[my_var]

``` diff
@@ Question 8. 
In the Window recipe, a window frame limited by the 5 preceding rows and -1 following rows will include how many rows? Assume this row is not one of the very first rows where the full window frame is not possible.@@
```
- [ ] 4
- [x] 5
- [ ] Cannot be determined.
- [ ] 6

``` diff
@@ Question 9. To calculate the cumulative sum of a column using the Window recipe, what component(s) must be set in the Window definition step? Select all that apply.@@
```
- [x] Partitioning column
- [x] Order column
- [x] Post-filter
- [x] Window frame

``` diff
@@ Question 10. Many processors in the Prepare recipe allow you to use regular expression patterns. Which of the following does NOT?@@
```
- [ ] Filter rows on value
- [ ] Find and replace
- [x] **Simplify text**
- [ ] Extract with regular expression
