---
layout: post
title: Cross Validation
# description: 
thumbnail: ../../../../assets/images/ml/cross-validation.png
author: Dipak Pulami Magar
date:   2025-12-09 11:12:45 +0545
categories: ml
status: draft
---

## Definition
Cross-validation (CV) is an advanced evaluation technique where the model is trained and tested **multiple times** using different splits.

Unlike hold-out (which uses only one split), CV reduces variance and gives a more reliable performance estimate.


### Use Cases of Cross-Validation
- **Small or medium datasets**:    
Uses every observation for training and testing.

- **When accuracy matters a lot**:  
Gives reliable model performance estimates.

- **Model selection & hyperparameter tuning**:  
Used with **GridSearchCV** and **RandomizedSearchCV**.

- **Detecting overfitting/underfitting**:  
CV scores show consistency across folds.

<!-- 
## **Example**:  Cross-Validation with GridSearchCV

```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import numpy as np

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])

model = SVC()

params = {'C': [0.1, 1, 10]}

grid = GridSearchCV(model, params, cv=3)
grid.fit(X, y)

print("Best Params:", grid.best_params_)
print("Best Score:", grid.best_score_)
``` -->

### Benefits of Cross-Validation
- **More reliable evaluation**:   
Uses multiple splits → more stable results.

- **Reduces overfitting risk**:   
Checks performance consistency across folds.

- **Uses dataset efficiently**:   
Each sample becomes both train and test at least once.

- **Standard in machine learning research**:   
Recommended for accuracy-sensitive tasks.

### Limitations of Cross-Validation
- **Computationally expensive**:   
Trains the model many times.

- **Not ideal for very big datasets**:  
Especially slow for deep learning.

- **Some models may not support CV easily**:  
(e.g., models requiring sequential data)

- **Complicated implementation for time-series data**: 
Careful handling needed to avoid data leakage.

### Train-Test Split vs Cross-Validation

| Aspect             | Train–Test Split / Hold-Out | Cross-Validation                          |
| ------------------ | --------------------------- | ----------------------------------------- |
| Number of splits   | 1                           | Many                                      |
| Speed              | Fast                        | Slow                                    |
| Accuracy stability | Fluctuates                  | Stable                                  |
| Best for           | Large datasets, quick tests | Small/medium datasets, serious evaluation |
| Data usage         | Limited                     | Full dataset is used                      |
| Risk of bias?      | High                        | Low                                       |

<!-- 
| Typical use        | Baseline testing            | Hyperparameter tuning, final evaluation   | -->


## Types of Cross-Validation

### 1. K-Fold Cross-Validation (Most Common)
The dataset is split into **K equal parts** (folds).
Process:
1. Train on K–1 folds
2. Test on the remaining fold
3. Repeat K times
4. Average all scores

Typical values: **K = 5 or 10**


<!-- **Python Example**:
```python
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([2, 4, 6, 8, 10, 12])

model = LinearRegression()
kf = KFold(n_splits=3)

scores = cross_val_score(model, X, y, cv=kf)
print("Scores:", scores)
print("Average Score:", scores.mean())
``` -->

**Use Cases**  
* When dataset is **small or medium-sized**
* For **model selection** and **hyperparameter tuning**
* When data is **not time-dependent**
* Good general-purpose evaluation method

<!-- **Example + Code**  
```python
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.random.rand(100, 5)
y = np.random.randint(0, 2, 100)

kf = KFold(n_splits=5, shuffle=True, random_state=42)
model = LogisticRegression()

scores = cross_val_score(model, X, y, cv=kf)
print(scores)
print("Average Score:", scores.mean())
``` -->

**Benefits**  
* Low bias, low-to-moderate variance
* Efficient use of data
* Works for both classification and regression
* Stable and widely used


**Limitations**  
* More computationally expensive than hold-out
* Must shuffle data properly
* Still not ideal for *time-series* data

### 2. Stratified K-Fold (For Classification)
Same as K-fold but keeps class ratios the *same* across folds.  
Used when data contains imbalanced classes.

**Use Cases**
* When the dataset is *imbalanced*
* Classification tasks where each fold must maintain *class proportions*
* Ensures fair evaluation of minority/majority classes

<!-- **Example + Code**  

```Python
From Sklearn.Model_Selection Import Stratifiedkfold, Cross_Val_Score
From Sklearn.Tree Import Decisiontreeclassifier

X = Np.Random.Rand(200, 4)
Y = [0]*160 + [1]*40   # Imbalanced Dataset

Skf = Stratifiedkfold(N_Splits=5, Shuffle=True, Random_State=42)
Model = Decisiontreeclassifier()

Scores = Cross_Val_Score(Model, X, Y, Cv=Skf)
Print(Scores)
``` -->

**Benefits**:     
* Preserves target class distribution
* Prevents folds with missing classes
* More reliable than normal K-fold for classification

**Limitations**:  
* Only works for classification
* Slightly slower due to stratification step


### 3. Leave-One-Out Cross-Validation (LOOCV)
<!-- Here you train a model on all data points except one, then test it on that single left-out point; this process repeats for every data point, creating 'n' models (where 'n' is total data points) to get an average error, providing an unbiased but computationally expensive performance estimate, ideal for small datasets.  -->

If dataset has *N samples*, then N folds.

Each iteration:
  * Train on N–1 samples
  * Test on 1 sample

Very accurate but *slow*.

**Use Cases**: 
* Very small datasets (e.g., less than 100 samples)
* When you want to use **almost all data for training**
* For sensitive scientific/statistical applications

<!-- 
**Example + Code**: 
```python
from sklearn.model_selection import LeaveOneOut, cross_val_score
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

loo = LeaveOneOut()
model = LinearRegression()

scores = cross_val_score(model, X, y, cv=loo)
print(scores)
print("Average Score:", scores.mean())
``` -->

**Benefits**:  
* Uses the maximum amount of data for training
* Very low bias
* Useful when dataset is too small for splitting

**Limitations**: 
* Extremely slow for large datasets
* High variance (since each test set is only 1 sample)
* Not practical for most ML problems


## K-Fold vs Stratified K-fold Vs LOOCV

| CV Type                        | Best For                  | Benefits            | Limitations             |
| ------------------------------ | ------------------------- | ------------------- | ----------------------- |
| **K-Fold**                     | General use               | Stable, widely used | Slow on big data        |
| **Stratified K-Fold**          | Imbalanced classification | Balanced folds      | Only for classification |
| **LOOCV**                      | Very small datasets       | Max training data   | Too slow                |

<!-- 
### 4. Repeated K-Fold
K-fold cross-validation **repeated multiple times** with different random splits.

Reduces variance even more.


### 5. Time Series Cross-Validation
Used when data has **temporal order**.
You cannot randomly shuffle time-based data.

Uses “expanding window” or “rolling window.” -->