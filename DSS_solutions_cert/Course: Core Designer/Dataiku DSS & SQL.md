# 
### Theory
https://academy.dataiku.com/path/core-designer/dataiku-dss-sql-1
### Quiz 1. Move data to your database
Before moving on to the next course/lesson, take this short quiz to test your comprehension

```diff
@@ Question 1. Which statement is true when creating an SQL dataset in DSS? @@
``` 

- [x] The data is written both in the DSS local server and the database 
- [ ] The data is written in the local server only
- [ ] The data is written in the SQL database only
- [ ] The data is saved on your local computer
              
```diff 
@@ Question 2. When writing data to your SQL database, Dataiku DSS prompts you to write a “CREATE TABLE” query? @@
```
- [x] False 
- [ ] True 

```diff  
@@ Question 3. If a database connection has been set up in DSS, you can import data into DSS directly from the database without having to sync or prepare tables? @@
```
- [ ] False
- [x] True
             
### Quiz 2. SQL Recipe
```diff
@@ Question 1. The output of an SQL _______ can be stored using a different database connection than the input, but the output of an SQL _______ must be stored in the same database as the input. @@
``` 

| | | | |
|-|-|-|-|
|<ul><li> - [ ] notebook, query </li> | <ul><li> - [ ] script, query </li> |  <ul><li> - [x] query, script </li> |  <ul><li> - [ ] script,notebook </li> |

```diff  
@@ Question 2:  Which of the following cases is an acceptable use of the SQL Script? @@
```
- [ ] If the data types in a table are not natively handled by DSS
- [ ] If the SQL code makes use of ‘With’ commands that cannot be re-written
- [x] All of these
- [ ] None of these
  
```diff  
@@ Question 3:  The SQL query requires a primary SELECT statement that DSS can use to write the final INSERT INTO a table. @@
```
- [ ] False 
- [x] True 
  
### Quiz 3. In-Database Charts.
```diff  
@@ Question 1:  By default, DSS renders charts on a dataset using: @@
```
| | | | |
|-|-|-|-|
|<ul><li> - [ ] The first 100,000 rows </li> | <ul><li> - [ ] A random sample of 100,000 rows </li> |  <ul><li> - [x] The same sample used in the explore view </li> |  <ul><li> - [ ] The entire dataset </li> |
  
``` diff
@@ Question 2. What is the maximum number of records that you can display in a chart? @@
```
- [ ] It depends on the amount of memory available to your machine
- [x] It depends on the engine that you select
- [ ] 100,000 rows
- [ ] There is no limit, no matter the selected engine.
  
### Quiz 4. SQL recipe.
``` diff
@@ Question 1. An SQL Notebook can be linked to multiple SQL connections? @@
```
- [x] False. 
- [ ] True.

``` diff   
@@ Question 2. : An SQL Notebook is not represented by an icon in the flow? @@
```
- [ ] False.
- [x] True.
  
``` diff  
@@ Question 3. An SQL Notebook writes a query output as a new dataset in your SQL database? @@
```
- [x] False.
- [ ] True.
  
``` diff  
@@ Question . An SQL Notebook can list the tables generated in my project? @@
```
- [ ] False. 
- [x] True.

### Quiz final. 
``` diff 
@@ Question 1. The Sync recipe and the Prepare recipe are the only visual recipes that you can use to write data to an SQL database. @@
```
- [ ] True. Other visual recipes, such as the Group, Join, and Window recipes, allow you to write data only to a local filesystem.
- [x] False. Other visual recipes, such as the Group, Join, and Window recipes, also allow you to write data to an SQL database.
  
``` diff 
@@ Question 2.  An SQL notebook writes a query output as a new dataset in your SQL database. @@
```
- [ ] True.
- [x] False.
  
``` diff 
@@ Question 3.   When writing data from DSS to a database, you must specify the column names and storage types. @@
```
- [x] True. You must explicitly provide the table schema to the database.
- [ ] False. DSS provides the table schema to the database.
  
``` diff 
@@ Question 4. An SQL query requires a primary SELECT statement that DSS can use to write the final INSERT INTO a table. @@
``` 
- [x] True.
- [ ] False.
 
