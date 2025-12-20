---
layout: post
title:  Test x
description: 
thumbnail: /assets/images/matplotlib/right-skewed-histogram.png
author: Dipak Pulami Magar
date:   2025-12-19 16:12:45 +0545
categories: test pandas
status: published
---

## Section A: Multiple Choice Questions (12 x 0.5 = 6 marks)  
1. Which imputation method is most suitable for skewed numerical data?  
    a. Mean  
    **b. Median**  
    c. Mode  
    d. Zero  
2. `dropna(axis=1)` removes:  
    a. Rows with missing values  
    **b. Columns with missing values**  
    c. Only numeric missing values  
    d. Only categorical missing values  
3. One-hot encoding converts categories into:  
    a. Single integer  
    **b. Binary columns**  
    c. Probability values  
    d. Ranks  
4. Which encoding can cause dimensionality explosion?  
    a. Ordinal  
    b. Target  
    **c. One-hot**  
    d. Label  
5. Which plot best shows data distribution?  
    a. Line plot  
    b. Bar chart  
    **c. Histogram**  
    d. Heatmap  
6. A correlation value of 0 indicates:  
    a. Strong positive relation  
    b. Strong negative relation  
    **c. No linear relation**  
    d. Perfect relation  
7. Which method ensures every data point appears in test set exactly once?  
    a. Hold-out  
    b. Random split  
    **c. K-Fold**  
    d. Stratified split  
8. Normalization scales data between:  
    a. -1 and 1  
    **b. 0 and 1**  
    c. Mean 0, std 1  
    d. Any range  
9. Which scaler is sensitive to outliers?  
    a. StandardScaler  
    **b. MinMaxScaler**  
    c. RobustScaler  
    d. MaxAbsScaler  
10. Feature engineering improves:  
    a. Data size  
    **b. Model performance**  
    c. Data leakage  
    d. Missing values  
11. Suppose you have a column “Chest Pain Type” which features [‘Normal’, ‘Moderate’, and, ‘Severe’, what is the best way to encode it?  
    a. One Hot Encoding  
    b. Nominal Encoding  
    **c. Ordinal Encoding**  
    d. Frequency Based Encoding  
12. Which distribution does the following histogram is shown here:
![right-skewed-histogram]({{base.url}}/assets/images/matplotlib/right-skewed-histogram.png)  
    a. Left Skew  
    **b. Right Skew**    
    c. Normal  
    d. Uniform  

---

## Section B: Debug the Code (6 × 1 = 6 Marks)  
1. This code results in an Error. Why? Fix it.  
```py  
df.fillna(mean)  
```  
Correct:  
```  
df.fillna(df['column_name'].mean())  
```  
2. From this code snippet, debug the error:  
```py  
import pandas as pd  
import matplotlib.pyplot as plt  
  
### i. Loading the Dataset  
df pd.read_csv("adult.csv")  
  
### ii. Cheking the null values  
df.isna.sum()  
  
### iii. Checking the Bar Plot for Gender column  
gender_counts = df ['sex'].value_counts()  
  
# Extract categories and their counts  
categories gender_counts.index.tolist()  
counts gender_counts.values.tolist()  
  
#Plot using matplotlib  
plt.figure(figsize=(6,4))  
plt.plot(categories, counts)  
plt.title('Count of Each Gender')  
plt.xlabel('Gender')  
plt.ylabel('Count')  
  
### iv. Encode the Column Male with 1 and Female with 0:  
  
df ['gender'] = df ['gender'].rename({"Male": 1, "Female":0})  
```  

3. This code results in an Error. Why? Fix it.  
```
OneHotEncoder.fit_transform(data)
```

4. Why does unpacking throw an error?
```py
from sklearn.model_selection import train_test_split
X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2)
```
Debugged:
```py
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```
5. This code results in an Error. Why? Fix it.
```py
plt.hist(df)
```
Debugged:
```
plt.hist(df['numerical_column'])
```

---

## Section D: Coding Questions (2 × 2.5 = 5 Marks)  
1. Create a new feature `BMI` from `Weight` and `Height`, then select top 3 features using correlation.

Example dataset:

| Weight | Height | Age | BP  |
| ------ | ------ | --- | --- |
| 60     | 1.65   | 22  | 120 |
| 70     | 1.70   | 25  | 130 |
| 80     | 1.75   | 30  | 140 |
| 90     | 1.80   | 35  | 150 |

$$
{BMI} = \frac{\text{Weight (in kilograms)}}{\text{Height}^2 \text{ (in meters)}}
$$