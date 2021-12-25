## Theory
[link](https://academy.dataiku.com/path/advanced-designer/variables-101)
## Practice
```diff
@@ Question 1. The only way to set & update project variables is to go to the project variable page and edit it. @@
```
- [x] False, variables can be set and updated via steps in scenarios or code and be fully automated.
- [ ] True, it is a manual operation.

``` diff
@@ Question 2. One variable is used in three visual recipes of a Flow. After manually changing the value of that variable, you rebuild the entire Flow. The new value of the variable will be used in _________________.@@
```
- [x] all three recipes
- [ ] the first (most upstream) recipe only
- [ ] the last (furthest downstream) recipe only.

``` diff
@@ Question 3. In which of the following Dataiku DSS objects can you use variables? (Select all that apply.)@@
```
- [x] Scenarios
- [x] Webapps
- [x] Visual recipes
- [x] Code recipes
- [x] Dataiku Applications.

``` diff
@@ Question 4. Project variables are project-dependent and cannot be called from other projects on the Dataiku DSS instance. @@
```
- [ ] False. A project variable is defined at the global level and can be used by any project on the Dataiku DSS instance.
- [x] True. Project variables are only available to a specific project, while global variables are available to the entire Dataiku DSS instance.

``` diff
@@ Question 5. Variables in Dataiku DSS are defined as JSON objects. Which of the following demonstrates the correct syntax for the name of a variable?@@
```
- [ ] {my_var}
- [x] "my_var"
- [ ] my_var
- [ ] 'my_var'
