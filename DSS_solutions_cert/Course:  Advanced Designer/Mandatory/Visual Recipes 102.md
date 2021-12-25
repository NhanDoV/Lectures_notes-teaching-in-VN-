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

