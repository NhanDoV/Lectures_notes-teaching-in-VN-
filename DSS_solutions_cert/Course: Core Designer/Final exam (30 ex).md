``` diff
@@ Question 1. Use the CO2 Emissions project to answer this question. How many records are in the original Urbanization_GDP_and_Population source dataset? @@
```

- [ ] 197
- [ ] 96224
- [x] 41859
- [ ] 245

``` diff
@@ Question 2. The Lab is a place to experiment before committing an analysis to your data pipeline in the Flow.  Which of the following are examples of how you can incorporate Lab work into the Flow? (Select two.) @@
```
- [ ] Deploy analysis done in a statistics worksheet to the Flow.
- [x] Deploy the Script from a Visual Analysis as a Prepare recipe.
- [x] Deploy a chart created in a Visual Analysis as output.
- [ ] Deploy a notebook as a code recipe.

``` diff
@@ Question 3. Use the CO2 Emissions project to answer this question. In the dataset that aggregates (averages) across the years 2008-2012, what is the median of the GDP per capita column? @@
```
- [ ] 7875.2
- [x] 36710.7
- [ ] 7442.5
- [ ] 70946.9

``` diff
@@ Question 4. The Formula processor in the Prepare recipe can be used to create a new column from a complex expression.  What language is used to write these expressions?@@
```
- [ ] R
- [ ] Excel
- [x] Dataiku’s spreadsheet-like formula language
- [ ] Python

```diff
@@ Question 5. Use the CO2 Emissions project to answer this question. In the univariate analysis on the prepared dataset, the median meat supply in kg per capita is lowest for which year? (Hint: The notation [2001,2002) refers to the year 2001)@@
```
- [x] 2011
- [ ] 2010
- [ ] 2009
- [ ] 2008

``` diff
@@ Question 6. You can perform univariate, bivariate, and principal components analysis in which tab of a dataset?@@
```
- [ ] Charts
- [x] Statistics
- [ ] Summary
- [ ] Explore

``` diff 
@@ Question 7. What is the name of the Dataiku DSS feature that you use to organize items such as datasets, recipes, models, discussions, and dashboards? @@
```
- [ ] Workspace
- [ ] Flow
- [x] Project
- [ ] Block

``` diff
@@ Question 8. A Prepare recipe's Script can have many steps.  Which of the following is the best option to make it easier for a coworker to understand the workflow within a Script of many steps? @@
```
- [ ] Choose processors that complete multiple operations in a single step.
- [ ] Organize individual steps into Groups of steps within the Script.
- [ ] Divide the steps into multiple Prepare recipes.
- [x] None of the other options.

``` diff
@@ Question 9. According to the Value Proposition of Dataiku, by automating both design and production to reduce repetitive work and maximize quality, Dataiku helps organizations to: @@
```
- [ ] Streamline the path to production
- [x] **Govern AI projects at scale**
- [ ] Centralize AI initiatives from data to impact
- [ ] Unify diverse teams working on AI

``` diff
@@ Question 10. Which of the following cannot be changed once it is created in Dataiku DSS?@@
```
- [ ] Project Description
- [ ] Project Folder Name
- [x] Project ID
- [ ] Project Name

``` diff
@@ Question 11. According to the Value Proposition of Dataiku, Dataiku enables teams to centralize AI initiatives from data to impact so that they can accomplish these. (Choose three.) @@
```
- [x] Unify business, data, and IT teams to work together on AI projects
- [ ] Code applications that perform extraordinary tasks
- [x] Upskill business analysts with visual tools that empower them to work with data
- [x] Provide a single place for developing, testing, and putting projects into production.

``` diff
@@ Question 12. Which of the following represent ways to find outliers in the values in the column of a dataset? (Choose three.)@@
```
- [ ] Schema
- [ ] Charts tab
- [x] Analyze window
- [ ] Statistics tab

``` diff
@@ Question 13. When in the Explore tab of a dataset with default settings, actions like sorting and filtering return fast results. What property of DSS makes this possible?@@
```
- [ ] Proprietary algorithms
- [x] A powerful DSS server
- [ ] Connections to powerful computation engines
- [ ] These actions are performed on only a sample of the dataset.

``` diff
@@ Question 14. Which tab on the project homepage shows a high-level overview of user contributions to a project?@@
```
- [ ] Activity
- [x] Summary
- [ ] Metrics
- [ ] Changes

``` diff
@@ Question 15. You are working with two datasets.  One contains listings of Homes_For_Sale and the other contains a listing of Realtors for which you have contact information. You want to create a new dataset that contains only the homes for sale that also have a realtor for whom you have contact information. How can you accomplish this in the Join recipe?@@
```
- [x] A Cross join type with Homes_For_Sale on the left.
- [ ] A Left join type with Realtors on the left.
- [ ] An Inner join type.
- [ ] A Left join type with Homes_For_Sale on the left.

``` diff
@@ Question 16. Consider the CO2 Emissions project. The Urbanization_GDP_and_Population dataset includes columns for "Population" and "GDP per capita". Which of the following recipe options would allow you to create a new column in the output dataset that represents the total GDP for each country (row)?  (Choose two). Hint: total GDP = GDP per capita * population @@
```
- [x] The Formula processor in a Prepare recipe
- [ ] Distinct recipe
- [x] Code recipe
- [ ] Join recipe

``` diff
@@ Question 17. In order to join more than two datasets with only visual recipes, which of the following solutions is correct and why?@@
```
- [ ] It is not possible to join more than two datasets at a time with the Join recipe. Perform multiple Join recipes instead.
- [x] Although only two datasets can be added in the Join recipe creation dialog, more datasets can be added on the Join step.
- [ ] Provided it is a left join, a single Join processor of the Prepare recipe is capable of joining more than two datasets at a time.
- [ ] None of these.

``` diff
@@ Question 18. Use the CO2 Emissions project to answer this question. What country has the 5th highest CO2 emissions per capita for the year 2010? (Hint: You can use options from the context menu of the column headers since the entire data fits in the dataset sample)
@@
```
- [ ] Trinidad and Tobago
- [ ] Bahrain
- [x] Luxembourg
- [ ] Saudi Arabia

``` diff
@@ Question 19. Consider the CO2 Emissions project. Imagine the CO2_and_Oil dataset is recorded by month instead of by year. For each observation of a country, there is a column storing the month (such as January) and a column storing the year (such as 2012). What visual recipe could be used to aggregate the data into yearly totals?@@
```
- [x] Group
- [ ] Stack
- [ ] Prepare
- [ ] Join

``` diff
@@ Question 20. Consider the CO2 Emissions project. Which of these visual recipes can NOT be used to restrict the datasets in the project to the years 2008-2012?@@
```
- [ ] A Sample/Filter recipe
- [ ] The pre-filter step of a Join recipe
- [ ] A filter processor in a Prepare recipe
- [x] A Sync recipe

``` diff
@@ Question 21. Use the CO2 Emissions project to answer this question. In the dataset that aggregates (averages) across the years 2008-2012, which country has the highest average meat production per capita for the years 2008-2012?  (Hint: You can use one of the options from the context menu of the column header since the entire data fits in the dataset sample) @@
```
- [ ] Spain
- [ ] Argentina
- [x] Australia
- [ ] Denmark

 ``` diff
 @@ Question 22. Which of the following are true of sampling in DSS? (Choose three.)@@
```
- [x] The default sampling method is to take a random sample, to ensure that the sample is representative of the full dataset.
- [x] Sampling settings are configurable.
- [ ] Sampling enables users to work interactively with huge datasets.
- [x] When preparing your dataset or building a chart, DSS uses a sample of the dataset, by default.

``` diff
@@ Question 23. According to the Value Proposition of Dataiku, Dataiku can help organizations take a ____________ approach to AI.@@
```
- [ ] Coding-oriented
- [ ] Design-oriented
- [ ] Individualized
- [x] **Systemized**

``` diff
@@ Question 24. Use the CO2 Emissions project to answer this question. In the dataset that aggregates (averages) across the years 2008-2012, which country has the lowest average percentage of urbanization?  (only considering countries with a non-null/non-zero average percentage urbanization)@@
```
- [ ] Solomon Islands
- [x] Burundi
- [ ] Kenya
- [ ] Nepal

``` diff
@@ Question 25. Use the CO2 Emissions project to answer this question. In the Entity column of the CO2_and_Oil source dataset, what percentage of the rows in the default sample are marked red (NOK) for having an invalid meaning?@@
```
- [ ] 16%
- [ ] 82%
- [ ] 0%
- [x] 4%

``` diff
@@ Question 26. Use the CO2 Emissions project to answer this question. In the dataset that aggregates (averages) across the years 2008-2012, which column has the highest Spearman correlation value with per-capita CO2 emissions?@@
```
- [ ] Oil production per capita
- [ ] Egg production per capita
- [ ] Percent of population living in urban areas
- [x] GDP per capita

``` diff
@@ Question 27. By default, when browsing a dataset in its Explore tab, what are you viewing?@@
```
- [ ] 5,000 random records
- [ ] The full dataset
- [ ] The first million records
- [x] The first 10,000 records

``` diff 
@@ Question 28. Which of these is not one of the available card types in a statistics worksheet?@@
```
- [ ] Principal Component Analysis
- [ ] Statistical tests
- [x] Covariance matrix
- [ ] Univariate analysis.

``` diff
@@ Question 29. You are working with a dataset of retail orders, and want to enrich that dataset with columns (from another dataset) that contain information about the customers who placed each order.  Which of the following recipes can you use to accomplish this?@@
```
- [ ] Stack
- [ ] Window
- [ ] Group
- [x] Join

``` diff
@@ Question 30. According to the Value Proposition of Dataiku, the task of delivering value from AI at scale requires that organizations master the tensions existing between all of these, EXCEPT:@@
```
- [ ] individual and the collective
- [ ] the mundane and the moonshot
- [ ] rationality and creativity
- [x] **technology and business**
