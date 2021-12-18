## Theory
https://academy.dataiku.com/path/ml-practitioner/time-series-basics-1
## Practices
### Quiz 1: Introduction to Time Series. 
```diff
@@ Question 1: True or False: Entries in a time series dataset are time-dependent, and they can be arranged in random order.@@
```
- [ ] True. The data entries must have a record of time, and they do not have to be in sequential order.
- [x] **False. The order of the data entries must be sequential with time.**
``` diff
@@ Question 2: True or False: Time series data is typically equispaced but can also be irregularly-spaced.@@
```
- [x] **True. Raw time series data can be irregularly-spaced and would need to be processed before it can be used in analysis.**
- [ ] False. If the data is irregularly-spaced, then it is not a time series.
``` diff
@@ Question 3: Which of these are examples of time series data? (Choose all that apply)@@
```
- [x] Hourly measurements of your blood pressure and pulse
- [x] The daily change of a stock price in 2018
- [ ] The average temperature of Paris for the month of June
- [ ] The online credit card transaction data of 1000 customers at noon on Friday.

### Quiz 2: Time Series Data Types and Formats. 
``` diff
@@ Question 1: Which of these is an example of multivariate time series data?@@
```
- [ ] Weights of four strangers measured over six months
- [x] Yearly measurements of Kate’s weight and Kate’s height
- [ ] Yearly measurements of Kate’s weight and Jon’s height
- [ ] Yearly measurements of Kate’s height
``` diff
@@ Question 2: True or False: If a dataset consists of multiple time series — Mike’s monthly weights in one column and Kate’s monthly weights in another column, then the dataset is in the long format.@@
```
- [ ] True. The long format stores the individual time series in separate columns.
- [x] **False. In the long format, the weights for both Mike and Kate will be stored in the same column.**
``` diff
@@ Question 3: Which of these is an example of multiple time series data?@@
```
- [ ] Hourly measurements of Kate’s blood pressure and pulse
- [ ] Yearly measurements of Kate’s weight and height
- [ ] Yearly measurements of Kate’s height
- [x] **Monthly weight measurements for 30 patients.**

### Quiz 3: Components.
``` diff
@@ Question 1: Which of these is an example of a cycle in a time series?@@
```
- [ ] The increase in sales of gift cards every December
- [x] **The number of lynx trapped over the past 50 years in northwest Canada shows repetitions occuring with varying frequencies and lasting different periods.**
- [ ] A country’s population plunged due to the outbreak of a deadly virus.
- [ ] The number of tourists in a city increases every September because of the annual jazz festival.
``` diff
@@ Question 2: Which of these is an example of seasonality in a time series?@@
```
- [x] **The increase in sales of gift cards every December**
- [ ] A decrease in house sales during a recession
- [ ] An increase in oil price due to a war in the Middle East
- [ ] The steady growth of China’s population since 1960
``` diff
@@ Question 3: True or False: A trend is a non-repeating long-term direction of the time series data, and it either increases or decreases.@@
```
- [ ] True. The trend can only increase or decrease.
- [x] **False. The trend can also be horizontal; neither increasing or decreasing.**

### Quiz 4. Objective
``` diff
@@ Question 1: By plotting time series data, you can do the following (Choose two):@@
```
- [x] **Obtain high-level observations of its components**
- [ ] Extend the time series to predict its future values
- [x] **Spot potential outliers**
- [ ] Model the behavior of the time series
``` diff
@@ Question 2: Plotting a time series is very useful for obtaining a ________ overview and observing its main _________.@@
```
- [x] **“high level” and “components”**
- [ ] “low level” and “slope”
- [ ] “low level” and “components”
- [ ] “high level” and “slope”
``` diff
@@ Question 3: The objectives of time series analysis fall into these categories:@@
```
- [ ] Decomposition, explanatory, regression, forecasting
- [ ] Descriptive, regression, forecasting, control
- [x] **Descriptive, explanatory, forecasting, control**
- [ ] Decomposition, explanatory, regression, control.

### Final
``` diff
@@ Question 1: Which of these is an example of univariate time series data?@@
```
- [x] Daily electricity consumption of one household for the month of June
- [ ] Quarterly values of the GDP for France and Germany
- [ ] Hourly measurements of your blood pressure and pulse
- [ ] T-shirt sizes for thirty students
``` diff
@@ Question 2: True or False: When storing multiple time series in the long format, we must include an additional column of identifiers.@@
```
- [x] True. The identifier column is necessary so that we can tell which rows belong to which time series.
- [ ] False. The long format is compact, therefore no additional column is needed.
``` diff
@@ Question 3: Which of these is not a component of time series data?@@
```
- [x] Horizon
- [ ] Cycle
- [ ] Trend
- [ ] Seasonality
``` diff
@@ Question 4: True or False: The phases of recovery, prosperity, recession, and depression in a business form a seasonal pattern.@@
```
- [ ] True. These phases form a seasonal pattern, occurring in predictable time intervals.
- [x] **False. These phases form a cyclical pattern that occurs in unpredictable time intervals.**
``` diff
@@ Question 5: How should you decide on the right level of granularity for your time series data?@@
```
- [x] **The granularity level depends on data availability and the purpose of your analysis**
- [ ] The more granular, the better
- [ ] The granularity doesn’t really matter for an analysis
- [ ] The less granular the better
``` diff
@@ Question 6: True or False: To start recording Jon’s monthly weight in a table that already contains Mike’s and Kate’s monthly weights, I must add a new column for Jon. This means that my time series data is in the wide format.@@
```
- [ ] False. By adding a new column, the table will get bigger, therefore the data is in the long format.
- [x] **True. In the wide format, weights for each individual are in separate columns.**
``` diff
@@ Question 7: Which of these are examples of time series data? (Choose all that apply)@@
```
- [x] **The daily change of a stock price in 2020**
- [x] **The hourly temperature measurements of Paris on Sunday**
- [ ] The online credit card transaction data of 1000 customers at noon on Friday
- [ ] A survey from 100 customers about a restaurant service
``` diff
@@ Question 8: The objectives of time series analysis fall into these categories:@@
```
- [x] **Descriptive, explanatory, forecasting, control**
- [ ] Descriptive, regression, forecasting, control
- [ ] Decomposition, explanatory, regression, control
- [ ] Decomposition, explanatory, regression, forecasting
``` diff
@@ Question 9: In an additive model, a time series is modeled as a sum of its components. Therefore the magnitude of its seasonality tends to increase over time.@@
```
- [x] **False. Because the time series is modeled as a sum of its components, the magnitude of its seasonality tends to stay constant.**
- [ ] True. The magnitude of the seasonality tends to increase over time because of a cumulative effect when you sum the components.
``` diff
@@ Question 10: True or False: When the goal of a time series analysis is “control,” we use observed values to predict future time series values.@@
```
- [ ] True. Predicting future values is the goal of control.
- [x] **False. Predicting future values is the goal of forecasting.**
