## Theory
https://academy.dataiku.com/path/core-designer/basics-101
## Practices
### Quiz 1. Create the project
``` diff
@@ Question 1: The Dataiku DSS homepage is your command center for all work on a specific activity.@@
```
- [x] **False. The Project is the command center for all your work on a specific activity.**
- [ ] ~~True. As the command center, you can even view recent user activity on the Dataiku DSS homepage.~~

``` diff
@@ Question 2: DSS is built for collaboration across the data team. When returning to a project, which of the following tabs on the project homepage would be the best place to visit for a high-level overview of user contributions to a project? @@
```
- [ ] ~~Metrics~~
- [ ] ~~Changes~~
- [ ] ~~Summary~~
- [x] **Activity**

``` diff
@@ Question 3:  search bar at the top of every Dataiku DSS screen searches across several sources that include the following (choose three).@@
```
- [x]  The catalog
- [ ] ~~The Dataiku Community~~
- [x]  Screens and settings within the product
- [x]  Recent items

### Quiz 2. Create the dataset.
``` diff
@@ Question 1: If a user has the right to read and write content for a particular project, then that user must also have the right to manage the data connections in that project.@@
```
- [x]  **False. Only those with admin permissions have access to connection settings such as credentials, security settings, naming rules, and usage parameters.**
- [ ] ~~True. As a collaborative platform, Dataiku DSS enables all users to manage connections.~~

``` diff
@@ Question 2: You can read, write, visualize, and manipulate datasets within DSS using the same methods.@@ 
```
- [ ] ~~False. How you interact with a dataset in Dataiku DSS depends on its underlying storage infrastructure.~~
- [x]  **True. Dataiku DSS allows you to interact with all kinds of datasets in the same manner.**

``` diff
@@ Question 3: Which of the following kinds of datasets can be used as a dataset that you can read, write, visualize, and transform in DSS?@@
```
- [ ] ~~An Amazon S3 bucket~~
- [x]  **All of these options**
- [ ] ~~An uploaded Excel spreadsheet~~
- [ ] ~~A folder of data files on a Hadoop cluster~~

### Quiz 3. Explore dataset
``` diff
@@ Question 1: To find outliers in the values in the column of a dataset, you must use the Charts tab.@@
```
- [x] **False: You can access the Analyze window of a column to view summary statistics and outliers.**
- [ ] ~~True: To find outliers in the values, you must create a chart.~~
``` diff
@@ Question 2: When designing the Flow, such as when using a Prepare recipe script to change the storage type or meaning of a column, Dataiku DSS asks if you want to update the schema.@@
```
- [x] **True. This is because the output dataset’s schema changes as you apply changes to the columns.**
- [ ] ~~False. Only changes to a column’s storage type will prompt DSS to ask if you want to update the schema.~~
``` diff
@@ Question 3: The default sampling method is First records.@@
```
- [x] **True. "First records" takes the first N rows of the dataset and is very fast. This may be a very biased view of the dataset and users should consider changing the sampling method based on their use case.**
- [ ] ~~False. The default sampling method is "No sampling" which takes all data from the dataset.~~

``` diff
@@ Question 4: When you import a CSV file, Dataiku DSS sets the storage type of the columns to String. @@
```
- [ ] ~~False, DSS can read the columns of a CSV file as other than text and sets the storage types accordingly.~~
- [x] **True, the storage type of all columns in a CSV file are read as text in DSS and are therefore set to storage type, String.**

### Final quiz.

``` diff
@@ Question 1: According to the Value Proposition of Dataiku, by providing the capabilities for managing operational risks and ensuring legal and regulatory compliance, Dataiku helps organizations to:@@
```
- [ ] ~~Unify diverse teams working on AI~~
- [ ] ~~Centralize AI initiatives from data to impact~~
- [ ] ~~Streamline the path to production~~
- [x] **Govern AI projects at scale**

``` diff
@@ Question 2: You can use Charts to zoom in on different time periods of a dataset in order to explore them and even change the aggregated date interval.@@
``` 
- [ ] ~~False: The ability to zoom in on different time periods is not found in the Charts tab.~~
- [x] **True: One of the features available in Charts is the ability to zoom in on different time periods.**

``` diff
@@ Question 3: According to the Value Proposition of Dataiku, Dataiku can help organizations take a ____________ approach to AI.@@
```
- [x] **Systemized**
- [ ] ~~Coding-oriented~~
- [ ] ~~Design-oriented~~
- [ ] ~~Individualized~~

``` diff
@@ Question 4: Which of the following are true of sampling in DSS? (Choose two).@@
```
- [x] **Sampling settings are configurable.**
- [ ] ~~When preparing a dataset or building a chart, Dataiku uses all the rows of the dataset by default.~~
- [ ] ~~Sampling enables users to work interactively with huge datasets.~~

``` diff
@@ Question 5: All these are examples of column storage types in Dataiku, EXCEPT?@@
```
- [ ] ~~TFloat~~
- [ ] ~~TInteger~~
- [x] **Name**
- [ ] ~~TBoolean~~
 
``` diff
@@ Question 6: To find outliers in the values in the column of a dataset, you must use the Charts tab.@@
```
- [ ] ~~True: You must create a chart.~~
- [x] **False: You can use the Analyze window.**
 
``` diff
@@ Question 7:  If you wanted to configure Dataiku DSS to automatically detect columns containing values that represent a company's departments, which of the following DSS features could you use?@@
```
- [ ] ~~Storage type~~
- [x] **Meaning**
- [ ] ~~This is not possible in Dataiku DSS.~~
 
``` diff
@@ Question 8: According to the Value Proposition of Dataiku, the task of delivering value from AI at scale requires that organizations master the tensions existing between all of these, EXCEPT:@@
```
- [ ] ~~rationality and creativity~~
- [x] **technology and business**
- [ ] ~~individual and the collective~~
- [ ] ~~the mundane and the moonshot~~

``` diff
@@ Question 9:  Using tags in your project can help collaborators to find it easily.@@
```
- [x] **True. Tagging a project is one way to prepare it for collaboration with others.**
- [ ] ~~False. Tagging is only useful for organizing a project. It doesn't make the project discoverable to collaborators.~~

``` diff
@@ Question 10: Dataiku DSS makes it possible for users to collaborate in real-time.@@
```
- [x] **True. When users collaborate in DSS they are doing so in real-time through a web browser.**
- [ ] ~~False. Dataiku DSS is installed locally, on each user’s desktop, and there is no shared server where users can collaborate in real-time.~~
