## Theory

https://academy.dataiku.com/path/core-designer/integration-with-sql-databases-1
## Quiz
```diff
@@ Question 1. All SQL connections defined in Dataiku are read and write? @@
``` 
- [x] **False. The admin can define whether a connection is read-write or read-only in the connection settings.**
- [ ] ~~True, all users that have access to a connection can read and write to it.~~

```diff
@@ Question 2. What information does DSS require to create an SQL connection? @@
``` 
- [ ] ~~The database schema~~
- [ ] ~~All of these~~
- [x] **The database name, host, and port.**
- [ ] ~~The location of the JDBC driver~~

```diff
@@ Question 3. DSS has native support for all but one of these databases. @@
```
- [ ] ~~Redshift~~
- [ ] ~~Teradata~~
- [x] **Denodo**
- [ ] ~~Snowflake~~

```diff
@@ Question 4. Dataiku can leverage the SQL computation engine in all but one of these cases. @@
```
- [ ] ~~To execute SQL-based code recipes~~
- [x]  **To train a deep learning model**
- [ ] ~~To execute visual recipes~~
- [ ] ~~To render charts~~
