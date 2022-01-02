## Theory
[link](https://academy.dataiku.com/path/advanced-designer/automation-course-1)

## Practices
### Quiz 1: Metrics & Checks.
``` diff
@@ Question 1. It is possible to use metrics and checks on partitioned DSS objects.@@
```
- [x] **True, you can use metrics and checks on each partition of the partitioned object.**
- [ ] False, you’ll have to unpartition the object in order to compute metrics and checks on it.

``` diff
@@ Question 2. Metrics can NOT be added to which of the following Flow items?@@
```
- [ ] Managed folders
- [x] **Recipes**
- [ ] Datasets
- [ ] Models

``` diff
@@ Question 3. In which of the following tabs of a dataset would a user be able to create a metric?@@
```
- [ ] Settings
- [ ] Statistics
- [ ] Explore
- [x] **Status**

### Quiz 2: Scenarios
``` diff
@@ Question 1. Which of the following are the two required components of a scenario? Select two.@@
```
- [ ] A reporter to send scenario information via several available channels
- [x] **A list of action(s) to run when a scenario launches**
- [ ] A code snippet to stop the scenario on certain conditions
- [x] **Trigger(s) that activate the scenario**

``` diff
@@ Question 2. Which of the following types of trigger would require custom code?@@
```
- [ ] Run when a dataset managed by Dataiku DSS changes.
- [ ] Run everyday at midnight.
- [ ] Run when another scenario finishes.
- [x] **None of these.**

``` diff
@@ Question 3. Which of the following is NOT a common use case of scenarios using the built-in options in Dataiku?@@
```
- [ ] Cleaning job logs weekly
- [ ] Running your flow daily when a change in a dataset is detected
- [x] **Automatically detecting the ML model features that need to be processed**
- [ ] Monitoring a ML model drift and retraining it

### Quiz 3: Custom Metrics, Checks & Scenarios.

### Final.

``` diff
@@ Question 1. In Dataiku DSS, metrics and checks can only be used in conjunction with scenarios.@@
```
- [ ] True. Without a scenario, metrics and checks have no value.
- [x] **False. Metrics and checks are often used to trigger actions in a scenario, but they exist independently.**

``` diff
@@ Question 2. Which of the following objects could you NOT use in a “Run checks” step of a scenario?@@
```
- [ ] Dataset
- [ ] Managed Folder
- [x] **Recipe**
- [ ] Model

``` diff 
@@ Question 3. After Dataiku DSS rebuilds a dataset, any metrics and checks belonging to that dataset are recomputed.@@
```
- [ ] Never true. Because they can be computationally-expensive, you must always explicitly choose to compute a metric.
- [x] **Sometimes true. It depends on whether you have chosen to auto-compute after build for that particular metric or check.**
- [ ] Always true. This is the value of metrics and checks.

``` diff
@@ Question 4. Which of the following is NOT an example of a metric?@@
```
- [ ] The number of files in a managed folder (e.g. 100)
- [ ] The most frequent values of a dataset column (e.g. "United States")
- [x] **Whether or not a column has more than some number of missing values (e.g. OK)**
- [ ] The accuracy of a machine learning model (e.g. 0.85)

``` diff
@@ Question 5. If a scenario has three different triggers, what needs to happen for the scenario to run?@@
```
- [ ] All of the triggers must be satisfied.
- [x] **Any one of the triggers must be activated.**
- [ ] A scenario can only have one trigger.
- [ ] At least two of the triggers must be activated.

``` diff
@@ Question 6. The “Last runs” tab of a scenario lists:@@
```
- [ ] Only successful runs of a scenario
- [ ] **All runs of a scenario**
- [ ] Only unsuccessful runs of a scenario

``` diff
@@ Question 7. Which of the following is NOT a valid status update for a check?@@
```
- [ ] ERROR
- [ ] OK
- [x] **N/A**
- [ ] WARNING

``` diff
@@ Question 8. Which of the following is NOT a valid messaging channel for a scenario reporter?@@
```
- [ ] Email
- [ ] Slack
- [ ] Microsoft Teams
- [x] **Jira**

``` diff
@@ Question 9. In order to launch a scenario when the number of records in a dataset stored in a SQL database has changed, which of the following triggers would be the first solution to try?@@
```
- [ ] Trigger on dataset change
- [ ] Trigger after scenario
- [x] **Trigger on SQL query change**
- [ ] Custom trigger (Python)

``` diff
@@ Question 10. Which of the following are the two required components of a scenario? Select two.@@
```
- [ ] A reporter to send scenario information via several available channels
- [ ] A code snippet to stop the scenario on certain conditions
- [x] **A list of action(s) to run when a scenario launches**
- [x] **Trigger(s) that activate the scenario.**
