## Theory
[link](https://academy.dataiku.com/path/developer/code-in-dataiku-dss)

## Practices
### Quiz 1: Code Notebooks
``` diff
@@ Question 1. Python notebooks can only be created from a dataset’s Lab menu.@@
```
- [ ] True. Each notebook is associated with a single dataset.
- [x] **False. Python notebooks can be created either directly from the Notebooks menu or from a dataset's Lab menu.**

``` diff
@@ Question 2. When using SQL notebooks in Dataiku DSS, it is best to write all queries in a single query cell.@@
```
- [ ] True. This ensures easier maintenance.
- [x] **False. It's best to keep each query in a separate cell, so that you can easily edit them interactively without impacting the other queries.**

``` diff
@@ Question 3. Which of the following are types of code notebooks enabled in Dataiku DSS? (Select all that apply.)@@
```
- [x] **Python**
- [x] **SQL**
- [ ] JavaScript
- [x] **R
- [x] **Scala**

``` diff 
@@ Question 4. In which of the following ways can a user kill a Jupyter notebook kernel?@@
```
- [ ] From the Notebooks menu, by selecting to "Unload" the notebook.
- [ ] If they are an administrator, from the Administration menu > Monitoring > Running background tasks.
- [ ] From the Macros menu, by configuring the dedicated "Kill Jupyter sessions" macro.
- [ ] Programmatically, using the Dataiku public API.
- [x] **All of these methods are valid.**

### Quiz 2: Code Recipes.
``` diff
@@ Question 1. To which of the options below does the following statement apply: Dataiku DSS allows for a two-way interaction between code recipes, which can be edited as code notebooks, and notebooks which can be deployed as recipes.@@
```
- [ ] Python or R recipes and Jupyter notebooks
- [ ] SQL recipes and SQL notebooks
- [x] **Both of these**

``` diff
@@ Question 2. Which of the following is NOT a Dataiku DSS code recipe?@@
```
- [ ] Spark R
- [ ] Impala
- [x] **Pivot**
- [ ] Hive

``` diff
@@ Question 3. Which of the following statements about code recipes are FALSE? Select all that apply.@@
```
- [ ] Code recipes are a type of Dataiku DSS recipe which executes a piece of user-defined code.
- [x] **Code recipes are represented by yellow circles in the Flow.**
- [x] **In order to create a code recipe, the user always needs to define the input dataset first.**
- [ ] Users can easily move between exploratory work in code notebooks and deploying it in a recipe, or vice versa.

### Quiz 3: 
``` diff
@@ Question 1. To change the code environment in a Jupyter notebook, one needs to:@@
```
- [ ] Deploy the notebook as a code recipe, and then change the environment from the Advanced tab.
- [x] **Change the Jupyter kernel.**
- [ ] Neither of these; Jupyter notebooks don't use code environments.

``` diff
@@ Question 2. For which of the following code languages are code environments available in Dataiku DSS? Select all that apply.@@
```
- [ ] SQL
- [x] **Python**
- [x] **R**
- [ ] Scala

``` diff
@@ Question 3. Which of the following is the recommended deployment type to use when creating a new code environment in Dataiku DSS?@@
```
- [ ] As a named external Conda environment.
- [ ] As a non-managed path.
- [x] **As a managed environment by Dataiku DSS.**

### Quiz 4: External IDE Integrations.
``` diff
@@ Question 1. Which of the following are Dataiku DSS objects that users can interact with via Dataiku's integrations with external IDEs? Select all that apply.@@
```
- [x] **Webapps**
- [ ] Visual recipes
- [x] **Plugins**
- [ ] Other Dataiku DSS users
- [x] **Code recipes**

``` diff
@@ Question 2. Which of the following are external IDEs that Dataiku DSS integrates with? Select all that apply.@@
```
- [x] **RStudio**
- [x] **PyCharm**
- [x] **Sublime**
- [x] **VS Code**

``` diff
@@ Question 3. To connect your instance of Dataiku DSS to an external IDE, you need to contact an administrator to generate a personal API key.@@
```
- [ ] True. This is an important security measure.
- [x] **False. You can create it yourself from your profile page.**

### Final quiz.
``` diff
@@ Question 1. Only administrators can create, edit, and set code environments in Dataiku DSS.@@
```
- [ ] True, only administrators have these privileges and they cannot assign them to other users.
- [x] **False. The administrator(s) of a DSS instance can authorize users to create, modify, and use code environments.**

``` diff
@@ Question 2. Which of the following code notebook types in Dataiku DSS allow you to run jobs on Spark?@@
```
- [ ] SQL notebooks
- [x] **Both SQL and all available Jupyter notebooks**
- [ ] All Jupyter notebooks
- [ ] Only Python Jupyter notebooks

``` diff
@@ Question 3. With an IDE integration, you can edit, locally run, and debug code within the IDE, and then save your code back to Dataiku DSS.@@
```
- [ ] False, IDEs can only be used to edit code, not run it.
- [x] **True, IDE integrations make all of these operations possible.**

``` diff
@@ Question 4. True or False: when creating a new recipe, Dataiku DSS auto-fills the recipe code editor with starter code.@@
```
- [x] **True, most recipes contain a set of pre-written code and comments that are meant to help the user get started.**
- [ ] False, when creating a new recipe, the code editor is always blank in order to allow users to start from scratch.

``` diff
@@ Question 5. Which of the following are benefits of using code notebooks? Select all that apply.@@
```
- [x] **They allow you to experiment with code.**
- [x] **They combine code, text, and visualizations in a single document.**
- [x] **They allow you to make your work more transparent.**
- [ ] They are the only way to write code in Dataiku DSS.
