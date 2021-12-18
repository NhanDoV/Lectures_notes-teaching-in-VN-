## Theory
[link](https://academy.dataiku.com/path/ml-practitioner/time-series-preparation-1)
## Practices
### Quiz 1: Time Series Preparation.
``` diff
@@ Question 1: If a dataset containing three independent time series is stored in long format, what is the minimum number of columns it could possibly have?@@
```
- [ ] 6
- [ ] 5
- [x] **3**
- [ ] 4
``` diff
@@ Question 2: If a dataset containing three independent time series is stored in wide format, what is the minimum number of columns it could possibly have?@@
```
- [x] **4**
- [ ] 6
- [ ] 5
- [ ] 3
``` diff
@@ Question 3: If a dataset has two values or measurements for the same timestamp in the same time series, what will Dataiku DSS do when trying to apply a recipe from the Time Series Preparation plugin?@@
```
- [ ] Retain only the row with the value closest to the mean of the two nearest timestamps.
- [x] **Throw an error complaining about duplicate timestamps.**
- [ ] Produce an error before a dataset such as this could be created.
- [ ] Warn the user that the time series is not valid, but complete execution as normal.

### Quiz 2: Resampling
``` diff
@@ Question 1: Is it possible in the Resampling recipe to equispace the timestamps of a time series without interpolating missing values?@@
```
- [x] **Yes. Choose “Don’t interpolate” as the interpolation method.**
- [ ] No. You can choose a constant value like 0, but there has to be some new value.
``` diff
@@ Question 2: The process of inferring values between two timestamps is known as:@@
```
- [ ] Equispacing
- [ ] Resampling
- [ ] Extrapolation
- [x] **Interpolation**
``` diff
@@ Question 3: Which of the following methods can be used for interpolation in the Resampling recipe? (Choose one answer).@@
```
- [x] **Any of these**
- [ ] Replace the missing timestamp by the previous point
- [ ] Fit a linear polynomial line between existing points to complete the missing timestamps
- [ ] Replace the missing points by the average value of nearest neighbors
``` diff
@@ Question 4: The Resampling recipe from the Time Series Preparation plugin can be helpful when you have time series data with missing and/or irregular time intervals.@@
```
- [ ] False. The Resampling recipe requires the input data to already have equispaced timestamps.
- [x] **True. The Resampling recipe transforms the input data into equispaced intervals, while also applying any interpolation method.**

### Quiz 3: Interval Extraction. 
``` diff
@@ Question 1: In the output dataset of an Interval Extraction recipe, the integers in the “interval_id” column will always be strictly increasing (i.e. they never decrease).@@
```
- [x] **Sometimes true. This is true for a single independent time series, but likely not true if there are multiple independent time series in the dataset.**
- [ ] Never true. Interval IDs start at an arbitrarily large number and decrease by 1 for each interval.
- [ ] Always true. Interval IDs start at 0 and increase by 1 for each interval.
``` diff
@@ Question 2: In the Interval Extraction recipe, the minimal segment duration parameter must always be greater or equal than the acceptable deviation parameter.@@
```
- [x] **Always false. There are no limitations on these values in relationship to each other.**
- [ ] Sometimes true. It depends on whether the data is in long format.
- [ ] Always true. Dataiku DSS would throw an error if so.
``` diff
@@ Question 3: In the Interval Extraction recipe, if the first valid timestamp in a daily time series is “2020-10-01” and the last valid timestamp is “2020-10-02”, how long is the duration in days?@@
```
- [ ] More information is needed to answer.
- [ ] 2
- [ ] 0
- [x] **1**

### Quiz 4: Windowing
``` diff
@@ Question 1: Imagine the 100th row in a single time series of 200 daily, regularly-spaced, timestamps. You have set a causal window frame with a width of 7 days. You configure the time series Windowing recipe to exclude both bounds. How many values are in the window frame when calculating a sum?@@
```
- [ ] 8
- [ ] 7
- [ ] 5
- [x] **6**
``` diff
@@ Question 2: For a particular row in a time series of all positive values, the sum resulting from a rectangular window frame is 100. For that same row, what must be true about the sum of a triangular window frame if no other window parameters are changed?@@
```
- [ ] Equal to 100
- [ ] More information is required.
- [ ] Greater than 100
- [x] **Less than or equal to 100**
``` diff
@@ Question 3: Imagine the 100th row in a single time series of 200 daily, regularly-spaced, timestamps. You have set a non-causal window frame with a width of 8 days using the time series Windowing recipe. How many of the timestamps included in the window frame would be greater than the current timestamp of that row?@@
```
- [ ] 2
- [ ] **3**
- [ ] 4
- [ ] 0

### Quiz 5: Extrema Extraction.
``` diff
@@ Question 1: Which of the following use cases are good candidates for the Extrema Extraction recipe? (Choose two.)@@
```
- [x] **Having the time series of product sales, explore the week leading to peak sales.**
- [ ] Having the time series of a stock price, we could predict its extremum values.
- [x] **Having the time series of an engine’s rotation speed, investigate what happened around a breakdown.**
- [ ] Having the time series of temperature data, smooth trends with the extracted extrema.
``` diff
@@ Question 2: Imagine a dataset of three independent time series (i.e., long format with 3 categories) is fed to the Extrema Extraction recipe. If there are no duplicate values among extrema, how many rows are in the output dataset?@@
```
- [ ] 6
- [ ] 1
- [ ] Not enough information to answer.
- [x] **3**
``` diff
@@ Question 3: The Extrema Extraction recipe can build a window frame around which of the following points in a time series? (Choose two.)@@
```
- [x] **Global minimum**
- [x] **Global maximum**
- [ ] Local minimum
- [ ] Local maximum

### Final
``` diff
@@ Question 1. For an input dataset containing multiple time series, which of the following is REQUIRED in order to apply the Resampling recipe? Select all that apply.@@
```
- [x] Long format
- [ ] No more than one measurement for each timestamp in a time series
- [x] A parsed date column
- [x] Wide format

``` diff
@@ Question 2. Which recipe of the Time Series Preparation plugin would be best suited to smooth the data in order to reduce noise and volatility? @@
```
- [ ] Resampling
- [x] Windowing
- [ ] Extrema Extraction
- [ ] Interval Extraction

``` diff
@@ Question 3. Which of the following factors determine the number of rows in the output dataset of an Extrema Extraction recipe? (Choose two.) @@
```
- [x] The extremum chosen (global maximum or minimum)
- [ ] The number of independent time series in the dataset
- [x] The width of the window frame
- [ ] The number of duplicate extrema values

``` diff
@@ Question 4. In order to ensure that every interval has at least seven days, which parameter of the Interval Extraction recipe would you adjust?@@
```
- [ ] Maximum valid value
- [ ] Acceptable deviation
- [ ] Minimal valid value
- [x] Minimal segment duration

``` diff
@@ Question 5. Which recipe of the Time Series Preparation plugin would be best suited to transform data occurring in irregular intervals into equispaced data?@@
```
- [ ] Windowing
- [ ] Extrema Extraction
- [x] **Resampling**
- [ ] Interval Extraction

``` diff
@@ Question 6. An output row of the Interval Extraction recipe that is assigned an interval ID of 6 is guaranteed to have an earlier timestamp than a row assigned an interval ID of 5.@@
```
- [ ] True. Interval IDs start at 0 and increase by 1 for each interval moving down time-ordered rows.
- [x] False. If the dataset contains multiple independent time series, this is not necessarily the case

``` diff
@@ Question 7. Imagine the 100th row in a single time series of 200 daily, regularly-spaced, timestamps. You set the window frame of the visual Window recipe to limit 2 preceding rows “before” and limit 0 following rows “after”. Which of the following options in the time series Windowing recipe would include the same values at the aggregation step? (Choose two).@@
```
- [ ] Non-causal, rectangular window with a width of 2 days
- [x] Causal, rectangular window with a width of 2 days, including both bounds
- [x] Causal, rectangular window with a width of 3 days, including only the right bound
- [ ] Causal, rectangular window with a width of 3 days, including only the left bound

``` diff
@@ Question 8. Which recipe of the Time Series Preparation plugin would be best suited to identify periods where a time series is within a given range under certain conditions?@@
```
- [ ] Windowing
- [x] **Interval Extraction**
- [ ] Resampling
- [ ] Extrema Extraction

``` diff
@@ Question 9. If you wanted your interval assignment to be flexible enough to account for time series volatility, which Interval Extraction recipe parameter would you most likely use?@@
```
- [ ] Minimal valid value
- [ ] Maximum valid value
- [ ] Acceptable deviation
- [x] Minimal segment duration

``` diff
@@ Question 10. Before using any of the other recipes in the Time Series Preparation Plugin, you first MUST use the Resampling recipe in order to equispace the timestamps.@@
```
- [x] False. Other recipes in the plugin may run successfully without being equispaced, but it can lead to unexpected behavior and so is not recommended.
- [ ] True. Recipes like time series windowing will fail if the data is not equispaced.

``` diff
@@ Question 11. If the maximum valid value in an Interval Extraction recipe is 100, and you wanted to assign a row with a value of 200 to an interval ID, you must set the acceptable deviation to 100.@@
```
- [ ] True. In this case, an acceptable deviation of 100 would push the effective maximum valid value to 200.
- [x] **False. The acceptable deviation accommodates deviations in time-- not in the magnitude of values.**

``` diff 
@@ Question 12. Setting the extrapolation method in the Resampling recipe enables you to extrapolate estimates for a fixed number of timestamps before the first timestamp or after the last timestamp in the dataset.@@
```
- [ ] True. For example, if the earliest timestamp in the dataset is March 1, you can extrapolate estimates for the last week of February.
- [x] **False. If there are multiple time series in the dataset, setting the extrapolation method allows you to stretch the length of shorter time series to match that of the longest.**
