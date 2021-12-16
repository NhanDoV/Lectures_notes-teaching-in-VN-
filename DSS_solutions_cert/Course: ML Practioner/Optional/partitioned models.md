## Theory
[link](https://academy.dataiku.com/path/ml-practitioner/partitioned-models)
## Practices
### Final quiz
``` diff
@@ Question 1. When interacting with the results of a partitioned model training session, it’s the same as interacting with the results of the overall (non-partitioned) model training session. The difference is:@@
```
- [x] **The partitioned model is an expert of only its “learning partition”**
- [ ] The partitioned model gives an approximate score
- [ ] The partitioned model does not give any specific details about its “learning partition”

``` diff
@@ Question 2. Seasons could impact purchasing patterns more in one subgroup of the dataset than another. Building a partitioned model on the subgroup could help in this case.@@
```
- [ ] False. Building a partitioned model could result in a better performing model only when you suspect the characteristics of the subgroups are mostly uniform.
- [x] **True. When you suspect the characteristics of subgroups of the dataset, such as countries, are dissimilar, then building a partitioned model could result in a better performing model.**

``` diff
@@ Question 3. Dataiku DSS displays the same performance summary for partitioned models as it does for non-partitioned models. @@
```
- [ ] True. DSS displays the performance summary for all model training sessions regardless of whether the model is partitioned or not.
- [x] **False. DSS does not display the performance summary for partitioned model training sessions because the display would be unreadable.**

``` diff
@@ Question 4. Partitioned models consist of training machine learning models over each partition of the dataset. @@
```
- [ ] False. Dataiku DSS trains one overall model regardless of the number of partitions.
- [x] **True. Dataiku DSS trains one model for each partition of the dataset (times the number of algorithms).**

``` diff
@@ Question 5. Partitioned models are a good solution when: (Choose two.)@@
```
- [x] **The subgroups associated with each partition have dissimilar behavior.**
- [ ] You want to establish a general/macro prediction strategy regarding all partitions.
- [ ] The subgroups associated with each partition have the same behavior.
- [x] **You want to establish a local/micro prediction strategy regarding each partition.**

``` diff
@@ Question 6. We can train a partitioned model if its source dataset is not partitioned.@@
```
- [ ] True. You can configure the design of a model to partition the training dataset for you if it is not already partitioned.
- [x] **False. You must first partition the dataset in the Settings tab of the dataset.**
