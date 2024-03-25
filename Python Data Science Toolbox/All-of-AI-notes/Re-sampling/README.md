## 1. Sampling method
### Reminder: Sample vs population

| | Population | Sample |
|-|:-|-|
| **Definition** |- The **population** is the entire group that you want to draw conclusions about.| - The specific group of individuals that you will collect data from |
| | - Including all people or items with the characteristic one wishes to understand.|
| **Example** | - The population $\Omega = \lbrace 1,2,3,4,5,6 \rbrace$ | - A subset of $\Omega$ can be the even-numbers $\lbrace 2,4,6 \rbrace$ or 
| (Tossing a dice) | | prime-numbers $\lbrace 2,3,5 \rbrace$ |

- The population can be defined in terms of geographical location, age, income, and many other characteristics. It can be very broad or quite narrow: maybe you want to make inferences about the whole adult population of your country; maybe your research focuses on customers of a certain company, patients with a specific health condition, or students in a single school.
- It is important to carefully define your target population according to the purpose and practicalities of your project.
- If the population is very large, demographically mixed, and geographically dispersed, it might be difficult to gain access to a representative sample.

### 1.1. Probability sampling methods
- Probability sampling means that every member of the population has a chance of being selected.
- It is mainly used in quantitative research. If you want to produce results that are representative of the whole population, you need to use a probability sampling technique.

![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/e7a3510a-493d-4637-b246-eec1227ffb4e)


| Type | Definition & description | Example |
|-|:-|:-|
|`Simple random sampling`| - In a simple random sample, every member of the population has an equal chance of being selected. | You want to select a simple random sample of 100 employees of Company X. |
| | - Your sampling frame should include the whole population.| Then, you assign a number to every employee in the company database from 1 to 1000, and use a random number generator to select 100 numbers. |
| | - To conduct this type of sampling, you can use tools like random number generators or other techniques that are based entirely on chance. | |
| `Systematic sampling` |- Systematic sampling is similar to simple random sampling, but it is usually slightly easier to conduct. | All employees of the company are listed in alphabetical order. From the first 10 numbers, you randomly select a starting point: number 6. |
| | -  Every member of the population is listed with a number, but instead of randomly generating numbers, individuals are chosen at regular intervals. | Then, from number 6 onwards, every 10th person on the list is selected (6, 16, 26, 36, and so on), and you end up with a sample of 100 people. |
| `Stratified sampling` | - Involves dividing the population into subpopulations that may differ in important ways. | The company has 800 female employees and 200 male employees. |
| | - It allows you draw more precise conclusions by ensuring that every subgroup is properly represented in the sample.| You want to ensure that the sample reflects the gender balance of the company, so you sort the population into two strata based on gender. |
| | | Then you use random sampling on each group, selecting 80 women and 20 men, which gives you a representative sample of 100 people.|
| `Cluster sampling` | - It is also involves dividing the population into subgroups, but each subgroup should have similar characteristics to the whole sample. | The company has offices in 10 cities across the country (all with roughly the same number of employees in similar roles). | 
| | - Instead of sampling individuals from each subgroup, you randomly select entire subgroups.| You don’t have the capacity to travel to every office to collect your data, so you use random sampling to select 3 offices – these are your clusters.|

### 1.2. Non-probability sampling methods
- In a non-probability sample, individuals are selected based on non-random criteria, and not every individual has a chance of being included.
- This type of sample is easier and cheaper to access, but it has a higher risk of sampling bias, and you can’t use it to make valid statistical inferences about the whole population.
- Non-probability sampling techniques are often appropriate for exploratory and qualitative research. In these types of research, the aim is not to test a hypothesis about a broad population, but to develop an initial understanding of a small or under-researched population.
  
![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/61d177a9-991c-428b-be0b-67a7d6d3ec23)

| Type | Definition & description | Example |
|-|:-|:-|
|`Convenience sampling`| - A convenience sample simply includes the individuals who happen to be most accessible to the researcher. | You are researching opinions about student support services in your university, |
|| - This is an easy and inexpensive way to gather initial data,.| so after each of your classes, you ask your fellow students to complete a survey on the topic. |
|| - but there is no way to tell if the sample is representative of the population, so it can’t produce generalizable results| This is a convenient way to gather data, but as you only surveyed students taking the same classes as you at the same level, the sample is not representative of all the students at your university.|
|`Voluntary response sampling`| - Similar to a convenience sample, a voluntary response sample is mainly based on ease of access.|You send out the survey to all students at your university and a lot of students decide to complete it. |
|| - Instead of the researcher choosing participants and directly contacting them, people volunteer themselves (e.g. by responding to a public online survey).|This can certainly give you some insight into the topic, but the people who responded are more likely to be those who have strong opinions about the student support services,|
|| - Voluntary response samples are always at least somewhat biased, as some people will inherently be more likely to volunteer than others.| so you can’t be sure that their opinions are representative of all students.|
|`Purposive sampling`| - This type of sampling involves the researcher using their judgement to select a sample that is most useful to the purposes of the research.|You want to know more about the opinions and experiences of disabled students at your university, |
|| - It is often used in qualitative research, where the researcher wants to gain detailed knowledge about a specific phenomenon rather than make statistical inferences.| so you purposefully select a number of students with different support needs in order to gather a varied range of data on their experiences with student services.|
|` Snowball sampling`| - If the population is hard to access, snowball sampling can be used to recruit participants via other participants.|You are researching experiences of homelessness in your city. Since there is no list of all homeless people in the city, probability sampling isn’t possible. |
|| -  The number of people you have access to “snowballs” as you get in contact with more people.|You meet one person who agrees to participate in the research, and she puts you in contact with other homeless people that she knows in the area.|

## 2. Upsampling vs downsampling
We use it when the data we gather will be heavily imbalanced
## 2.1. Definition
### 2.1.1. Upsampling
- This is a procedure where synthetically generated data points (corresponding to minority class) are injected into the dataset. After this process, the counts of both labels are almost the same.
- This equalization procedure prevents the model from inclining towards the majority class. Furthermore, the interaction(boundary line)between the target classes remains unaltered. And also, the upsampling mechanism introduces bias into the system because of the additional information.
- We also have the other oversampling methods like `'ADASYN', 'BorderlineSMOTE', 'KMeansSMOTE', 'RandomOverSampler', 'SMOTE', 'SMOTEN', 'SMOTENC', 'SVMSMOTE'`
- Some `Oversampling methods`:

      ADASYN (Adaptive synthetic sampling approach for imbalanced learning):
                          Reducing the bias introduced by the class imbalance and then
                          Adaptively shifting the classification decision boundary toward the difficult examples
      SMOTE (Synthetic Minority Oversampling Technique):
                          Works based on the KNearestNeighbours algorithm, synthetically generating data points that fall in the proximity of the already existing outnumbered group.
                          The input records should not contain any null values when applying this approach.
      RandomOverSampler : Object to over-sample the minority class(es) by picking samples at random with replacement.
                          The bootstrap can be generated in a smoothed manner.
      
![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/a3e07bb8-48a3-4bc8-9a55-394fcbdcb9e1)

### 2.1.2. Downsampling
- This is a mechanism that reduces the count of training samples falling under the majority class. 
- As it helps to even up the counts of target categories. By removing the collected data, we tend to lose so much valuable information.

### 2.2.1. In tablular data
**Example (oversampling)**
  
```
      import imblearn
      import numpy as np
      from imblearn.over_sampling import SMOTENC
      from sklearn.datasets import make_classification
      from collections import Counter
      X, y = make_classification(n_samples=1000, n_classes=6, n_informative=10)
      y = np.random.choice([1,2,3,4,6,9], size=1000, p=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05])
      print("initial distribution")
      print(Counter(y))
      oversample = SMOTENC(categorical_features=[1,2,3,4,6,9], 
                           random_state = 100)
      X, y = oversample.fit_resample(X, y)
      print("current distribution")
      print(Counter(y))
      .......
      initial distribution
      Counter({1: 503, 2: 196, 3: 104, 4: 99, 6: 54, 9: 44})

      current distribution
      Counter({1: 503, 2: 503, 4: 503, 3: 503, 6: 503, 9: 503})
```

**Example (undersampling)**
```
      from imblearn.under_sampling import TomekLinks, NearMiss
      
      X, y = make_classification(n_samples=10000, n_classes=6, n_informative=10)
      y = np.random.choice([1,2,3,4,6,9], size=10000, p=[0.92, 0.02, 0.01, 0.01, 0.02, 0.02])
      print("initial distribution")
      print(Counter(y))
      undersample = NearMiss()
      X, y  = undersample.fit_resample(X, y)
      print("current distribution")
      print(Counter(y))
      .....
      initial distribution
      Counter({1: 9144, 6: 236, 2: 212, 9: 202, 3: 110, 4: 96})

      current distribution
      Counter({1: 96, 2: 96, 3: 96, 4: 96, 6: 96, 9: 96})
```
### 2.2.2 In computer vision or sound-processing, 
- In case you want to enhance / oversampling your images, you can consider `data-augmentation`, the various image transformations include scaling, cropping, flipping, padding, rotation, Brightness, contrast, and saturation level changes. By doing so, with just a single image, a humongous image dataset can be created.
- But incase you want to up-scaling or down-scaling image like this, you can refers the other [section]()
  
![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/016a84cd-bd4c-465b-8d8a-3bebd1337e9b)

### 2.2.3. In NLP
- In case you want to enhance / oversampling your input-text, you can consider `translation, dropping some word are not importance, etc`

#### Reference
- [ref 1](https://www.kaggle.com/discussions/general/262007)
- [ref 2](https://www.slideshare.net/slideshow/implementation-of-upsampling-downsampling/251957761)

## 3. Resampling: Boostraping - Jacknife
Resampling methods - an extremely useful class of statistical data analysis techniques which are closely related to the concept of statistical simulation. They have wide applications in areas like model validation, uncertainty estimation and significance testing.
#### Why resample?
At a very basic level, resampling methods are quite attractive due to their simplicity. They are conceptually quite simple to implement and are applicable to complex estimators. 

For example, there's a statistical formula for estimating the confidence interval of a population mean, but how about the confidence interval for the 35th percentile of the population distribution? 

- Resampling methods easily allow such estimations. In general, resampling methods don't make any strict assumptions regarding the distribution of the data. 
- The drawback of using resampling methods, of course, is that they tend to be computationally expensive.
- However, with the advent of more powerful computers, this has become less of an issue in recent years. Let's look at the three major types of resampling methods.

#### Types of resampling methods
Generally speaking, there are three broad types of resampling methods.
>- **Bootstrap resampling** is the most common type of resampling method. Here we sample from the dataset repeatedly but with **replacement**.
>- **Jackknife resampling** is very similar to bootstrapping, except that there is no random sampling. Instead, one or more observations from the original dataset are systematically excluded in creating new datasets. Jackknife resampling methods are quite useful for estimating the bias and variance of estimators. Although jackknife methods were developed before bootstrapping, they can be seen as a linear approximation of bootstrapping. 
>- Finally, we have **permutation testing**, which involves switching the labels in the dataset.

### Example to understand Boostrap vs Jacknife
Suppose you've received a large shipment of [Easter eggs](https://en.wikipedia.org/wiki/Easter_egg) and are interested in determining the average weight of each egg for quality control. 
>- You have access to a small sample of 10 eggs. You weigh these eggs and find 4 that weigh 20g, 3 that weigh 70g and 3 others weighing 50g, 90g and 80g respectively.
>- From this sample, you can easily calculate the `mean of 51`, `standard deviation of 27`, `standard error of 8.53` and then multiply this standard error by 1.96 to get the `95% confidence interval` between `34.27` and `67.73`. 
>- This gives us what we want, doesn't it? We went from a sample distribution to a population distribution. However, there are hidden assumptions in this calculation.
>- First of all, we *`assumed that the distribution of weights is normal`*. 

In addition, we assumed that the confidence interval was symmetric. Both of these might not be reasonable assumptions. So what do we do?

#### Bootstrapping Easter eggs
>- One approach is to take a bootstrapped sample by *`sampling with replacement from the original sample`*. In our case, this means that each of the `10` eggs have an equal probability of being picked. 
>- And since it `with replacement`, each egg has an equal probability of being picked subsequently as well. Here are some bootstrapped samples drawn from the `original sample`.
>- Notice how some egg weights appear more often that they do in the original sample. After drawing multiple bootstrap samples, we can calculate the mean weight for each of these samples.

![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/555caa18-0ed8-482a-8589-37ac1386913c)

**Bootstrapped distribution**

>- Using `5000 iterations`, I get a mean weight of `50.8g` with a `95%` confidence interval between `35` and `67.03`. 
>- Notice that the `CI (confidence interval)` is not symmetric. Although this result isn't hugely different from the original calculation, it does serve to illustrate the power of the bootstrap.
>- One thing to keep in mind is that the reliability of the bootstrap is dependent on the original sample being a reasonable representation of the population.

#### Jackknife resampling
Next, we turn our attention to jackknife resampling. The jackknife estimation process was developed before bootstrapping but is quite similar. John Tukey proposed the name `jackknife` because he saw this procedure as a quick tool that could be applied to a variety of problems. 
>- It is particularly useful when the underlying distribution of the data is unknown. 
>- Just like bootstrapping, you create multiple samples from the original dataset and calculate your statistic for each of the samples.

![image](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/assets/60571509/c7cebd5e-031e-4844-9b98-70e4dd184039)

#### Reference
- [sampling method - my-github](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/blob/master/Statistics/Sampling%20%26%20Resampling/Sampling/introduction-to-sampling-methods.ipynb)
- [resampling method - my-github](https://github.com/NhanDoV/Lectures_notes-teaching-in-VN-/blob/master/Statistics/Sampling%20%26%20Resampling/Resampling/Resampling_methods.ipynb)