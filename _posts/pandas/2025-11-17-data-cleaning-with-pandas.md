---
layout: post
title: Data Cleaning With Pandas
# description: A practical, example-driven tutorial for data science & machine learning
thumbnail: ../../../../assets/images/pandas/data-cleaning.png
author: Dipak Pulami Magar
date:   2025-11-17 17:12:45 +0545
categories: pandas
status: published
---

## **1. Introduction: What Is Data Cleaning?**
Data cleaning is the process of **detecting, correcting, or removing inaccurate, incomplete, corrupted, inconsistent, and irrelevant data** from a dataset.

In any data project—analytics, BI, ML, or AI—**clean data contributes ~80% of the model’s success**.
Without clean data, even the best model will fail.

### **Common Data Problems**
* Missing values
* Duplicate rows
* Outliers and impossible values
* Wrong data types
* Inconsistent formatting
* Noisy text (spaces, typos, casing issues)
* Categorical inconsistencies
* Mixed units (kg vs lbs)
* Irregular date formats

Pandas provides powerful tools to handle these problems.

---

# **2. Loading and Understanding Data With Pandas**

```python
import pandas as pd

df = pd.read_csv("sample.csv")
```

### **Preview Dataset**

```python
df.head()
df.tail()
df.sample(5)
```

### **Understand Structure**

```python
df.info()
df.describe(include='all')
df.shape
df.columns
```

### **Detect Data Types**
```python
df.dtypes
```

# **3. Handling Missing Data**
### **Identify Missing Values**
```python
df.isna().sum()
df.isnull().mean() * 100   # percentage
```

### **Remove Missing Data**
```python
df_clean = df.dropna()
df_clean = df.dropna(subset=['age', 'salary'])
df_clean = df.dropna(thresh=3)  # rows with at least 3 non-null values
```

### **Fill Missing Values**
#### **Fill with Mean / Median / Mode**
```python
df['age'] = df['age'].fillna(df['age'].mean())
df['salary'] = df['salary'].fillna(df['salary'].median())
df['gender'] = df['gender'].fillna(df['gender'].mode()[0])
```

#### **Forward & Backward Fill**
```python
df['sales'].fillna(method='ffill', inplace=True)
df['sales'].fillna(method='bfill', inplace=True)
```

#### **Fill using interpolation**
```python
df['temperature'] = df['temperature'].interpolate()
```

# **4. Handling Duplicates**
### **Check duplicates**
```python
df.duplicated().sum()
```

### **Remove duplicates**
```python
df = df.drop_duplicates()
```

### **Remove duplicates based on specific columns**
```python
df = df.drop_duplicates(subset=['name', 'date'])
```
<!-- 
# **5. Handling Outliers**
### **Detect Outliers: IQR Method**
```python
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1

df_no_outliers = df[
    (df['price'] >= Q1 - 1.5*IQR) &
    (df['price'] <= Q3 + 1.5*IQR)
]
```

### **Detect with Z-score**
```python
from scipy import stats
df['z'] = stats.zscore(df['price'])

df_no_out = df[df['z'].abs() < 3]
```

### **Cap Outliers**
```python
df['price'] = df['price'].clip(lower=df['price'].quantile(0.01),
                               upper=df['price'].quantile(0.99))
```

# **6. Fixing Incorrect Data Types**
### **Convert to numeric**
```python
df['age'] = pd.to_numeric(df['age'], errors='coerce')
```

### **Convert to integer**
```python
df['age'] = df['age'].astype('Int64')
```

### **Convert to datetime**
```python
df['date'] = pd.to_datetime(df['date'], errors='coerce')
```

### **Convert categorical**
```python
df['gender'] = df['gender'].astype('category')
```

# **7. Text & String Cleaning**
### **Basic Text Cleaning**
```python
df['name'] = df['name'].str.strip()
df['name'] = df['name'].str.lower()
df['name'] = df['name'].str.replace(r'[^a-zA-Z ]', '', regex=True)
```

### **Fix Inconsistent Categories**
```python
df['city'] = df['city'].str.title()
df['city'].replace({'Ktm': 'Kathmandu', 'KTM': 'Kathmandu'}, inplace=True)
```

### **Extracting With Regex**
```python
df['year'] = df['text'].str.extract(r'(\d{4})')
```
--->

<!-- # **8. Handling Inconsistent Data** -->
# **5. Handling Inconsistent Data**
### **Detect impossible values**
```python
df[df['age'] < 0]
df[df['salary'] < 0]
df[df['height'] > 250]
```

### **Fix values**
```python
df.loc[df['age'] < 0, 'age'] = df['age'].median()
```

<!-- # **9. Feature Engineering** 
# **Feature Engineering**-->
### **Create new columns**
```python
df['total_price'] = df['quantity'] * df['unit_price']
```
<!--
### **Binning**
```python
df['age_group'] = pd.cut(df['age'], bins=[0,18,40,60,100],
                         labels=['Teen','Adult','Middle','Senior'])
```

### **Encoding categorical variables**
```python
df = pd.get_dummies(df, columns=['gender', 'city'])
```

### **Date features**
```python
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['weekday'] = df['date'].dt.day_name()
```
-->

<!-- # **10. Renaming Columns** -->
# **6. Renaming Columns**
### **Best practice**

```python
df.columns = df.columns.str.lower().str.replace(' ', '_')
```

### **Manual renaming**
```python
df.rename(columns={'Sale Price': 'sale_price'}, inplace=True)
```

<!--
# **11. Scaling & Normalization**
### **Min-Max Scaling**
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df[['salary_scaled']] = scaler.fit_transform(df[['salary']])
```

### **Standard Scaling**

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['salary_z']] = scaler.fit_transform(df[['salary']])
``` -->
<!-- 
---

# **12. End-to-End Example (Complete Walkthrough)**
### **Sample Dataset**

```python
data = {
    'name': ['Ram ', 'Shyam', 'Hari', None, 'SITA'],
    'age': ['25', '30', None, '40', '-5'],
    'salary': [20000, 25000, None, 40000, 15000],
    'city': ['ktm', 'KTM', 'pokhara', 'Biratnagar', None],
    'join_date': ['2020/01/01', '2021/05/03', None, '2019/12/15', '2021/01/20']
}

df = pd.DataFrame(data)
```

## **Step 1: Clean Text**

```python
df['name'] = df['name'].str.strip().str.title()
```

## **Step 2: Fix Data Types**

```python
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
```

## **Step 3: Handle Missing Values**

```python
df['age'] = df['age'].fillna(df['age'].median())
df['salary'] = df['salary'].fillna(df['salary'].median())
df['city'] = df['city'].fillna('Unknown')
```

## **Step 4: Correct Incorrect Values**

```python
df.loc[df['age'] < 0, 'age'] = df['age'].median()
```

## **Step 5: Fix Categorical Inconsistency**

```python
df['city'] = df['city'].str.title()
df['city'].replace({'Ktm': 'Kathmandu', 'Ktm ': 'Kathmandu', \
    'KTM': 'Kathmandu'}, inplace=True)
```

## **Step 6: Feature Engineering**

```python
df['year_joined'] = df['join_date'].dt.year
df['salary_lakh'] = df['salary'] / 100000
```

## **Result**

A clean dataset ready for:

* EDA
* Visualization
* Machine learning
* Storage -->

---

# **7. Summary & Best Practices**
<!-- **13. Summary & Best Practices**  -->

### **Data Cleaning Checklist**
* Understand data structure
* Handle missing values
* Fix data types
* Remove duplicates
* Address outliers
* Correct inconsistent values
* Clean text fields
* Standardize categories
* Engineer meaningful features

### **Best Practices**
* Clean **before** modeling
* Never drop data blindly
* Use visualizations to detect issues
* Automate cleaning for repeated tasks
* Document every step