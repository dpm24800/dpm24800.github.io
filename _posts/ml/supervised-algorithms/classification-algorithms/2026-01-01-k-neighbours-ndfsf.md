---
layout: post
title: K-Nearest Neighbors (KNN) Algorithm
# description: A Complete Guide
# thumbnail: /assets/images/ml/dfsfdfsdffier.png
author: Dipak Pulami Magar
date:   2026-01-14 08:12:45 +0545
categories: ml supervised classification
status: draft
---

## 1. Introduction
**K-Nearest Neighbors (KNN)** is a **supervised machine learning algorithm** used for:

* **Classification** (most common)
* **Regression**

It is a **non-parametric, instance-based (lazy learning)** algorithm, meaning:

* It does **not learn explicit parameters** during training
* It **stores the training data**
* Predictions are made **at runtime** using distance calculations

## 2. Intuition Behind KNN

> “Tell me who your neighbors are, and I’ll tell you who you are.”

* A new data point is classified based on the **majority class of its K closest neighbors**
* “Closeness” is measured using a **distance metric**

### Example intuition:
If most nearby points are **Class A**, the new point is likely **Class A**.

## 3. How KNN Works (Step-by-Step)
1. Choose the number of neighbors **K**
2. Compute distance between the test point and all training points
3. Select the **K nearest neighbors**
4. For classification → **majority vote**
5. For regression → **average of values**

## 4. Distance Metrics in KNN

### 4.1 Euclidean Distance (Most Common)

$$
d(x, y) = \sqrt{\sum_{i=1}^{n}(x_i - y_i)^2}
$$

### 4.2 Manhattan Distance

$$
d(x, y) = \sum_{i=1}^{n} |x_i - y_i|
$$

### 4.3 Minkowski Distance (Generalized)

$$
d(x, y) = \left( \sum_{i=1}^{n} |x_i - y_i|^p \right)^{1/p}
$$

* $$ p = 2 $$ → Euclidean
* $$ p = 1 $$ → Manhattan

## 5. Mathematical Example (Classification)

### Dataset

| Point | x | y | Class |
| ----- | - | - | ----- |
| A     | 1 | 2 | Red   |
| B     | 2 | 3 | Red   |
| C     | 3 | 3 | Blue  |
| D     | 6 | 5 | Blue  |
| E     | 7 | 7 | Blue  |

### Test Point:

$$
T = (3, 2)
$$

Let **K = 3**, Euclidean distance

### Step 1: Distance Calculation

$$
d(T, A) = \sqrt{(3-1)^2 + (2-2)^2} = \sqrt{4} = 2
$$

$$
d(T, B) = \sqrt{(3-2)^2 + (2-3)^2} = \sqrt{2} \approx 1.41
$$

$$
d(T, C) = \sqrt{(3-3)^2 + (2-3)^2} = \sqrt{1} = 1
$$

$$
d(T, D) = \sqrt{(3-6)^2 + (2-5)^2} = \sqrt{18} \approx 4.24
$$

$$
d(T, E) = \sqrt{(3-7)^2 + (2-7)^2} = \sqrt{41} \approx 6.40
$$

### Step 2: Choose 3 Nearest Neighbors

| Point | Distance | Class |
| ----- | -------- | ----- |
| C     | 1.00     | Blue  |
| B     | 1.41     | Red   |
| A     | 2.00     | Red   |

### Step 3: Majority Voting
* Red → 2
* Blue → 1

### Final Prediction:
$$
\boxed{\text{Red}}
$$

---

## 6. Choosing the Value of K
- Small K → **Overfitting**, sensitive to noise
- Large K → **Underfitting**, smoother decision boundary

### Rule of Thumb:

$$
K \approx \sqrt{n}
$$

Use **cross-validation** to find the optimal K.

## 7. Feature Scaling in KNN (Very Important ⚠️)
KNN is **distance-based**, so features must be scaled.

Example problem:
- Age: 18–60
- Salary: 20,000–1,000,000

Salary dominates distance ❌

### Common Scaling Methods:
- StandardScaler
- MinMaxScaler

## 8. KNN in Scikit-Learn (Classification Example)

```py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Example dataset
X = np.array([
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 5],
    [7, 7]
])

y = np.array(['Red', 'Red', 'Blue', 'Blue', 'Blue'])

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4 Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#.5 Train KNN Model
knn = KNeighborsClassifier(
    n_neighbors=3,
    metric='euclidean'
)

knn.fit(X_train, y_train)

# 6 Predictions & Evaluation
y_pred = knn.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
```

## 9. KNN for Regression (Brief)
```py
from sklearn.neighbors import KNeighborsRegressor

knn_reg = KNeighborsRegressor(n_neighbors=5)
knn_reg.fit(X_train, y_train)
predictions = knn_reg.predict(X_test)
```

Prediction = **average of nearest neighbors**

## 10. Advantages of KNN
- Simple and intuitive
- No training phase
- Works well with small datasets
- Flexible distance metrics

## 11. Disadvantages of KNN
- Computationally expensive
- Sensitive to noise
- Requires feature scaling
- Poor performance on large datasets

## 12. Applications of KNN
- Recommendation systems
- Image recognition
- Medical diagnosis
- Pattern recognition
- Fraud detection

## 13. Summary
* KNN is a **lazy, distance-based supervised algorithm**
* Works by **majority voting or averaging**
* **Scaling is critical**
* Performance depends heavily on **K and distance metric**

If you want, I can also provide:

* 📊 **Decision boundary visualization**
* 🔍 **How to choose best K using cross-validation**
* 🧠 **Comparison with Logistic Regression & SVM**
* 📝 **Interview questions on KNN**

Just tell me 👍
