## Theory
[link](https://academy.dataiku.com/path/developer/r-users)

## Practices
``` diff
@@ Question 1. Which of the following functions from the DSS R API can be used in conjunction with a managed folder where the data source is stored non-locally? Select two choices.@@
```
- [x] **dkuManagedFolderUploadPath()**
- [ ] dkuManagedFolderPath()
- [ ] dkuManagedFolder()
- [x] **dkuManagedFolderDownloadPath()**

``` diff
@@ Question 2. If a DSS project has an R Markdown report, a Shiny webapp, and R notebooks, these objects must all share the same R code environment.@@
```
- [ ] True. Every project must have one single code environment.
- [x] **False. Objects in the same project can have their own code environments.**

``` diff
@@ Question 3. To use the DSS R API outside of Dataiku, you’ll need to install the dataiku package through _______. You _________ need an API key.@@
```
- [ ] CRAN / won’t
- [ ] CRAN / will
- [x] **the DSS instance / will**
- [ ] the DSS instance / won’t

``` diff
@@ Question 4. Which line of code saves a ggplot object named "gg" as a static insight titled "my-ggplot"?@@
```
- [ ] dkuSaveInsight("my-ggplot", gg)
- [ ] dkuSaveGgplotInsight(gg, "my-ggplot")
- [x] **dkuSaveGgplotInsight("my-ggplot", gg)**
- [ ] dkuSaveInsight("ggplot", "my-ggplot", gg)

``` diff
@@ Question 5. To find a visual alternative to string processing functions found in the stringr package, which of the following recipes would be the best place to look?@@
```
- [ ] Sync recipe
- [ ] String recipe
- [ ] Stack recipe
- [x] **Prepare recipe**

``` diff
@@ Question 6. Which of the following DSS actions cannot be performed using the RStudio Desktop integration?@@
```
- [ ] Edit and save back the contents of an R recipe.
- [ ] **Write a DSS dataset output of an R recipe.**
- [ ] Save a ggplot object as a static insight.
- [ ] Read a DSS dataset into memory as a dataframe.

``` diff
@@ Question 7. Every R recipe ______ have ________ input(s) and output(s), which may be dataset(s) or folder(s).@@
```
- [ ] must / a single
- [x] **can / multiple**
- [ ] can / a single
- [ ] must / multiple

``` diff
@@ Question 8. To import code from another project on the DSS instance, add the project key to the "__________________" name in the "________________" file.@@
```
- [ ] importRLibrariesFromProjects, external-libraries.R
- [ ] importProjectLibraries, external-project-libraries.json
- [x] **importLibrariesFromProjects, external-libraries.json**
- [ ] importLibraries, external-libraries.json

``` diff
@@ Question 9. To import a function named my_function() from a file called "my_file.R" into an R notebook within DSS, which of the following lines of code would you use (in addition to library(dataiku))?@@
```
- [ ] library(my_file)
- [x] **dkuSourceLibR("my_file.R")**
- [ ] load("my_file.R")
- [ ] dkuSourceLibR("my_function")

``` diff
@@ Question 10. Imagine a global project variable called "my_var". An R notebook includes the line vars <- dkuGetProjectVariables(). Which of the following lines prints the value of "my_var"?@@
```
- [ ] vars$local$my_var
- [x] **vars$standard$my_var**
- [ ] vars$my_var
- [ ] vars$global$my_var
