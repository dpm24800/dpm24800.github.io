---
layout: post
title: Feature Scaling
# description: 
# thumbnail: ../../../../assets/images/ml/feature-scaling.png
author: Dipak Pulami Magar
date:   2025-12-10 10:12:45 +0545
categories: ml
status: draft
---

Feature scaling is one of the most essential data preprocessing steps in machine learning. It ensures that numerical features are on a similar scale so models can learn efficiently and accurately.

In simple terms:

> *Feature scaling transforms numerical features so that they share a comparable range and distribution.*

Without scaling, many ML algorithms may perform poorly because they interpret larger values as more important—even when they’re not.

### Why Feature Scaling Is Important
**1. Prevents Dominance of Large-Range Features**  
For example, income (0–1,000,000) will dominate age (18–80) unless scaled.

**2. Speeds Up Gradient Descent**  
Models like logistic regression, neural networks, and SVM rely on optimization. Scaling makes convergence **faster and smoother**.

**3. Improves Model Accuracy**  
Models sensitive to distance (Euclidean/Manhattan) require scaling:
* KNN
* K-means
* SVM
* PCA

**4. Improves Numerical Stability**  
Large values can cause overflow or computation errors.


### **Algorithms That Require Feature Scaling**
Some ML models are **scale-sensitive**:

| Model Type               | Examples                                                | Scaling Needed? |
| ------------------------ | ------------------------------------------------------- | --------------- |
| Distance-based           | KNN, K-means, DBSCAN                                    | Required      |
| Gradient-based           | Logistic Regression, Linear Regression, Neural Networks | Required      |
| Margin-based             | SVM                                                     | Required      |
| Dimensionality Reduction | PCA, LDA                                                | Required      |

Models that are **scale-insensitive**:

| Model Type | Examples                               | Scaling Needed? |
| ---------- | -------------------------------------- | --------------- |
| Tree-based | Decision Trees, Random Forest, XGBoost | Not needed    |
| Rule-based | Naive Bayes                            | Not needed    |

## Types of Feature Scaling Techniques  
Feature scaling techniques fall into three broad categories:
1. Absolute Maximum Scaling (Max Abs Scaling)
2. Normalization (0–1 scaling)
3. Standardization (Z-score scaling/normalization)
  
<!-- 3. Robust Scalers (resistant to outliers) -->


###  1. Normalization (Min-Max Scaling)
Normalization rescales values to a range of **0 to 1**:

$$
x' = \frac{x - x_{min}}{x_{max} - x_{min}}
$$

**When to use**  
* When features must be bounded (0–1)
* For neural networks (especially sigmoid/tanh)
* For distance-based models like KNN and K-means

**Python Example**
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

**Advantages**  
* Maintains original distribution
* Simple and widely used

**Disadvantages**  
* Highly sensitive to outliers
  One extreme value can shrink all others.


### 2. Standardization (Z-score Scaling)

Standardization transforms data so that:

* Mean = 0
* Standard deviation = 1

$$
x' = \frac{x - \mu}{\sigma}
$$

**When to use**
* When the model assumes normally distributed variables
* For linear/ logistic regression
* For SVM and neural networks
* When there are outliers (mild)

**Python Example**
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

**Advantages**
* Not affected as much by outliers as Min-Max
* Works well in many ML models

**Disadvantages**
* Does not bound values in a fixed range
* Sensitive to extreme outliers


<!-- ### 3. Robust Scaling (Median and IQR Scaling)
RobustScaler uses **median and IQR** instead of mean and variance:

$$
x' = \frac{x - median}{IQR}
$$

**When to use**

* When the data has **many outliers**
* Financial data
* Sensor data
* Any real-world dataset with noise

**Python Example**
```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)
```

**Advantages**
* Very robust against outliers
* Good for skewed distributions

**Disadvantages**
* Does not bound values
* Does not assume normal distribution -->

---

# **Additional Scaling Techniques**

### **4. MaxAbs Scaling**

Scales values to range **-1 to 1**, preserving sparsity.

Formula:

$$
x' = \frac{x}{|x|_{max}}
$$

Used for:
* Text features
* Sparse data (TF–IDF)

```python
from sklearn.preprocessing import MaxAbsScaler
```

---

### **5. Unit Vector Scaling (Normalization by Euclidean Norm)**
Makes each row (sample) have magnitude = 1.

Used for:
* Text classification
* Cosine similarity tasks

<!-- ```python
from sklearn.preprocessing import Normalizer
``` -->

<!-- ## Feature Scaling and Outliers
Scaling does **not remove** outliers.
But some scalers break when outliers are present.

| Scaler         | Handles Outliers? | Notes                |
| -------------- | ----------------- | -------------------- |
| MinMaxScaler   | No                | Very sensitive       |
| StandardScaler | ⚠️                | Moderate sensitivity |
| RobustScaler   | Yes              | Best for outliers    |
| MaxAbs         | ⚠️                | Linearly affected    | -->


## **Feature Scaling in a Pipeline (Best Practice)**

Always scale **inside a pipeline**, not before splitting.

Avoid data leakage!

<!-- ```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipe.fit(X_train, y_train)
``` -->

## **Example: Comparing Scaling Techniques**

Imagine a dataset:

| Feature    | Range            | Issue                  |
| ---------- | ---------------- | ---------------------- |
| Age        | 18–80            | Small range            |
| Salary     | 10,000–1,000,000 | Dominates model        |
| Experience | 0–30             | Different distribution |

### Without scaling
KNN, SVM, logistic regression will heavily depend on **salary**.

### With scaling
All features contribute appropriately, improving:

* Accuracy
* Convergence speed
* Model balance

### Feature Scaling Mistakes (Avoid These!)
- Scaling **before train-test split** → leakage
  - Scale *after* splitting, inside pipeline
- Applying scaling to target variable
  - Do not scale `y` (except in regression with normalization)
- Using MinMaxScaler with outliers
  - Use RobustScaler instead
- Scaling categorical variables
  - Only scale **numerical** features

## **When NOT to Use Feature Scaling**
Scaling is not necessary when:
* You’re using tree-based models:
  * Random Forest
  * Decision Tree
  * XGBoost
  * CatBoost
  * LightGBM

These models split based on thresholds—not distances—so scaling doesn’t matter.

## **Conclusion**
Feature scaling is a critical preprocessing technique that:  
* Ensures fair contribution of all features
* Improves model accuracy
* Increases convergence speed
* Reduces numerical instability

Choosing the **right scaling method** depends on:
* The model you’re using
* The distribution of your data
* Presence of outliers
* Need for bounding or normalization
