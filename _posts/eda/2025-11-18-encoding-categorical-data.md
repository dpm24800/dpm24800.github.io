---
layout: post
title: Encoding Categorical Data
description: 
thumbnail: ../../../../assets/images/pandas/encoding-categorical-data.png
author: Dipak Pulami Magar
date:   2025-11-18 20:12:45 +0545
categories: pandas
status: published
---

Machine learning algorithms work primarily with **numerical data**. However, real-world datasets often contain **categorical variables**, such as:

* Gender: *Male, Female*
* Payment Method: *Credit Card, Cash, PayPal*
* Country: *Nepal, India, USA*
* Product Categories: *Electronics, Clothing, Grocery*

To use such data in ML, we must convert categorical values into **numeric form**.
This process is called **Categorical Encoding**.

## 1. Categorical Variables
Categorical variables represent groups or labels instead of numeric value. They are of two types:

**(a) Nominal (No order)**  
Examples:
* Colors: red, green, blue
* Cities
* Brands

**(b) Ordinal (Has meaningful order)**
Examples:
* Size: small < medium < large
* Education level: high school < bachelor < master < phd

Encoding depends on whether the category has **order**.

---

## 2. Why Do We Need Categorical Encoding?
Most ML algorithms **cannot work with strings**, e.g.:
* Linear Regression
* Logistic Regression
* SVM
* KNN
* Random Forest (works but performs better with numeric encoding)

Encoding helps to:
- Make data ML-ready
- Improve model performance
- Preserve or eliminate category order
- Reduce dimensionality (sometimes)

---

## 3. Types of Categorical Encoding
<!-- ## 3. Types of Categorical Encoding in Pandas & Scikit-Learn -->

We cover:
1. **Label Encoding**
2. **One-Hot Encoding (get_dummies)**
3. **Ordinal Encoding**


<!-- 3. **Binary Encoding**
1. **Frequency / Count Encoding**
2. **Target Encoding**
3. **Hash Encoding** (useful for high-cardinality data) -->

(Only the first two are built into pandas; others use custom logic or libraries.)

<center> - - - </center>

### 3.1. Ordinal Encoding
**Used**: when categories have a natural order OR when using tree models.

**Where NOT to use**
Not good for nominal categories like *red, blue, green*
→ ML models may assume **numeric order** (which is incorrect)

**Example Use Case**
* Customer satisfaction: *Poor < Average < Good < Excellent*
* T-shirt size: *S < M < L < XL*

**Code Example (Pandas + Scikit-Learn)**
```python
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

df = pd.DataFrame({
    "Size": ["M", "L", "S", "XL", "M"]
})

encoder = OrdinalEncoder(categories=[["S", "M", "L", "XL"]])
df["Size_encoded"] = encoder.fit_transform(df[["Size"]])
print(df)
```

### **Output**

| Size | Size_encoded |
| ---- | ------------ |
| M    | 1            |
| L    | 2            |
| S    | 0            |
| XL   | 3            |
| M    | 1            |

## 3.2. One-Hot Encoding (OHE)
- **Used when**: categories are nominal (no order).
- **Best for**: Logistic Regression, Linear Regression, Neural Nets.

**1. Using pandas.get_dummies()**

```python
import pandas as pd

df = pd.DataFrame({
    "Color": ["Red", "Blue", "Green", "Blue"]
})

df_ohe = pd.get_dummies(df, columns=["Color"])
print(df_ohe)
```

### Output

|   | Color_Blue | Color_Green | Color_Red |
| - | ---------- | ----------- | --------- |
| 0 | 0          | 0           | 1         |
| 1 | 1          | 0           | 0         |
| 2 | 0          | 1           | 0         |
| 3 | 1          | 0           | 0         |


**2. Using Scikit-Learn OneHotEncoder**

```python
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame({
    "City": ["Kathmandu", "Pokhara", "Biratnagar", "Pokhara"]
})

ohe = OneHotEncoder(sparse_output=False)
encoded = ohe.fit_transform(df[['City']])

df_ohe = pd.DataFrame(encoded, columns=ohe.get_feature_names_out())
print(df_ohe)
```

### **Problems with OHE**
- Creates many columns (curse of dimensionality)
- Not suitable for 1000+ unique categories (like product catalog)

## **3.3. Label Encoding**
**Used**: when converting categories into **integer labels** (0, 1, 2, …).
**Best for**: **Tree-based models** (Decision Tree, Random Forest, XGBoost).
**Not recommended for**: Linear models → they assume numeric order, which label encoding does **not** represent.

### **What It Does**
Label Encoding assigns a **unique integer** to each category:

| Category | Encoded |
| -------- | ------- |
| Apple    | 0       |
| Banana   | 1       |
| Mango    | 2       |

The order is **arbitrary**—it does *not* represent importance or ranking.

### **Where NOT to Use**
Avoid in **nominal categories** when using
* Linear Regression
* Logistic Regression
* Neural Networks

Because these models may think:
`Mango (2) > Banana (1) > Apple (0)` — which is incorrect.

### **Best Use Cases**
Works well when feeding into:
* Decision Tree
* Random Forest
* Gradient Boosting
* XGBoost / LightGBM
  (because these models **don’t assume order**)

Good when categories are large but you still need compact representation.

### **Code Example (Using Scikit-Learn LabelEncoder)**

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    "Fruit": ["Apple", "Banana", "Mango", "Banana", "Apple"]
})

encoder = LabelEncoder()
df["Fruit_encoded"] = encoder.fit_transform(df["Fruit"])

print(df)
```

**Output**

| Fruit  | Fruit_encoded |
| ------ | ------------- |
| Apple  | 0             |
| Banana | 1             |
| Mango  | 2             |
| Banana | 1             |
| Apple  | 0             |


<!-- ### **Reverse Mapping (Decoding Back)**

```python
encoder.inverse_transform([0, 1, 2])
```

Output:
`['Apple', 'Banana', 'Mango']` -->


### **Key Differences Between Label Encoding & Ordinal Encoding**

| Feature       | Label Encoding          | Ordinal Encoding       |
| ------------- | ----------------------- | ---------------------- |
| Purpose       | Assign arbitrary labels | Apply meaningful order |
| Order Meaning | No meaning              | Meaningful             |
| Good For      | Tree models             | Ordered features       |
| Example       | Apple → 0, Banana → 1   | Small < Medium < Large |

### **Potential Problems**
* **Introduces fake ordering** for models that assume number meaning.
* Cannot handle **unseen categories** unless configured separately.
* Can confuse linear models.

### **Real-World Use Cases**
* Encoding country names for tree models
* Converting product names before using XGBoost
* Encoding text labels in classification tasks (y-labels)

<!-- 
### 5.3. Frequency Encoding (Count Encoding)
** Replace category with frequency count.

**Real-World Use Case**
E-commerce product categories:
| Category | Count |
| -------- | ----- |
| Mobile   | 4000  |
| Laptop   | 2000  |
| Books    | 8000  |

**Code Example**

```python
df = pd.DataFrame({
    "Category": ["Mobile", "Laptop", "Mobile", "Books", "Books"]
})

freq = df["Category"].value_counts()

df["Category_freq"] = df["Category"].map(freq)
print(df)
```

### Output

| Category | Category_freq |
| -------- | ------------- |
| Mobile   | 2             |
| Laptop   | 1             |
| Mobile   | 2             |
| Books    | 2             |
| Books    | 2             |

### **Advantages**
Great for high-cardinality data
Keeps dataset small
Works well for tree models 


## 3.3. Target Encoding
Encode categories based on the mean of target variable.

Example: Predicting conversion rate of marketing channels.

| Channel    | Conversion Rate |
| ---------- | --------------- |
| Google Ads | 0.10            |
| Facebook   | 0.06            |
| TikTok     | 0.02            |


```python
df = pd.DataFrame({
    "Channel": ["Google Ads", "Facebook", "Google Ads", "TikTok"],
    "Converted": [1, 0, 1, 0]
})

target_mean = df.groupby("Channel")["Converted"].mean()

df["Channel_encoded"] = df["Channel"].map(target_mean)
print(df)
```

### **Use Case**
Fraud detection
Marketing model
Recommendation system

### 3.4. Binary Encoding**
(Using category_encoders library)

This combines hashing + OHE → reduces dimensionality.

Best for:
* High-cardinality columns (>100 categories)

Example:
* User countries
* Product SKUs
* Zip codes

```python
import category_encoders as ce
import pandas as pd

df = pd.DataFrame({
    "Country": ["Nepal", "India", "China", "Nepal", "USA"]
})

encoder = ce.BinaryEncoder(cols=["Country"])
df_bin = encoder.fit_transform(df)
print(df_bin)
```

### 3.5. Hashing Encoding
Used when category count is extremely large (10,000+).

```python
encoder = ce.HashingEncoder(cols=["Product"], n_components=8)
```

Fast
No need to store mapping
Great for big data, streaming data
Hash collisions possible

<!-- --- -->

<!-- # **10. Comparison of Encoding Methods**

| Method              | Best For                         | Pros                  | Cons                   |
| ------------------- | -------------------------------- | --------------------- | ---------------------- |
| **Label/Ordinal**   | Ordered categories               | Simple                | Wrong for nominal      |
| **One-Hot**         | Nominal data                     | Accurate, ML-friendly | Too many columns       |
| **Frequency**       | High-cardinality                 | Compact               | Loses category meaning |
| **Target Encoding** | Categorical → numeric prediction | Powerful              | Risk of leakage        |
| **Binary Encoding** | Many unique values               | Memory efficient      | Harder to interpret    |
| **Hash Encoding**   | Very large datasets              | Fast                  | Collision risk         | -->

<!-- 
## **11. Real-World Examples**
### **E-Commerce**
* Product category → One-hot
* Product brand (1000+ brands) → Binary encoding
* Product ID → Hash encoding
* Customer membership level → Ordinal encoding

### **Banking / Finance**
* Risk level → Ordinal
* Transaction type → One-hot
* Merchant category code (MCC ~400 categories) → Frequency encoding

### **Marketing**
* Channel performance → Target encoding
* Campaign type → One-hot

### **Healthcare**
* Patient condition stage (Stage I–IV) → Ordinal
* Symptoms (yes/no) → One-hot

---

## **12. Summary: When to Use What?**

**Use One-Hot Encoding when**
* Categorical values have no order
* Columns have < 20 unique categories

**Use Ordinal Encoding when**
* Categories have meaningful order

**Use Frequency Encoding when**
* Column has 50–5000 unique categories

**Use Target Encoding when**
* Building ML models with strong categorical impact
* Working with Kaggle-style datasets

**Use Binary/Hash Encoding when**
* Very high-cardinality columns (e.g., product IDs, URLs) -->