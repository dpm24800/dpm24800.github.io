
# **2. Stratified K-Fold Cross-Validation**



---

---

# **3. Leave-One-Out Cross-Validation (LOOCV)**

## 

---

---

# **4. Leave-P-Out Cross-Validation (LPOCV)**

## **Use Cases**

* When you want a very detailed evaluation
* Good for small datasets
* Can measure model sensitivity to removing specific “p” samples
* Used sometimes in research

---

## **Example + Code**

(*p = 2 in this example*)

```python
from sklearn.model_selection import LeavePOut
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X = np.random.rand(10, 2)
y = np.random.randint(0, 2, 10)

lpo = LeavePOut(p=2)
model = KNeighborsClassifier()

for train_index, test_index in lpo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
```

---

## **Benefits**

* Extremely thorough testing
* Useful for validating stability of the model
* Very informative for small datasets

---

## **Limitations**

* Testing all combinations is **combinatorially expensive**
* Not scalable at all for moderate or large datasets

---

---

# **5. Repeated K-Fold Cross-Validation**

## **Use Cases**

* When dataset is small and K-fold alone has high variance
* Used when highly stable evaluation is required
* Great for unreliable/noisy datasets

---

## **Example + Code**

```python
from sklearn.model_selection import RepeatedKFold, cross_val_score
from sklearn.svm import SVC
import numpy as np

X = np.random.rand(200, 5)
y = np.random.randint(0, 2, 200)

rkf = RepeatedKFold(n_splits=5, n_repeats=5, random_state=42)
model = SVC()

scores = cross_val_score(model, X, y, cv=rkf)
print(scores.mean())
```

---

## **Benefits**

* Very stable performance estimation
* Averages over many random splits
* Better than plain K-fold when data is noisy

---

## **Limitations**

* Slow (K-fold * number of repeats)
* Can be overkill for large datasets

---

---

# **6. Repeated Stratified K-Fold**

## **Use Cases**

* Imbalanced classification
* When stability and fairness are required
* Popular in competitions and research

---

## **Example + Code**

```python
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.random.rand(300, 6)
y = [0]*240 + [1]*60

rskf = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=42)
model = RandomForestClassifier()

scores = cross_val_score(model, X, y, cv=rskf)
print(scores.mean())
```

---

## **Benefits**

* Combines benefits of stratification + repeated splits
* Very low bias and variance
* Most reliable CV for imbalanced data

---

## **Limitations**

* Computation-heavy
* Not suitable for large datasets

---

---

# **7. Time-Series Cross-Validation / Rolling Window CV**

## **Use Cases**

* Stock price prediction
* Weather forecasting
* Sales forecasting
* Any time-dependent dataset

Time series **must not be randomly shuffled**.

---

## **Example + Code**

```python
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.arange(100).reshape(-1, 1)
y = X.ravel() + np.random.randn(100)

tscv = TimeSeriesSplit(n_splits=5)
model = LinearRegression()

for train_index, test_index in tscv.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
```

---

## **Benefits**

* Respects time order
* No data leakage
* Works perfectly for sequential data
* Mimics real-world forecasting

---

## **Limitations**

* Less training data in early folds
* Cannot shuffle data
* More biased than standard K-fold

---

---

# 🎯 **Final Summary Table**

| CV Type                        | Best For                  | Benefits            | Limitations             |
| ------------------------------ | ------------------------- | ------------------- | ----------------------- |
| **K-Fold**                     | General use               | Stable, widely used | Slow on big data        |
| **Stratified K-Fold**          | Imbalanced classification | Balanced folds      | Only for classification |
| **LOOCV**                      | Very small datasets       | Max training data   | Too slow                |
| **LPO**                        | Research, tiny data       | Very thorough       | Combinatorial explosion |
| **Repeated K-Fold**            | Noisy datasets            | Very stable         | Slow                    |
| **Repeated Stratified K-Fold** | Imbalanced + noisy        | Most reliable CV    | Slowest                 |
| **Time Series CV**             | Forecasting               | No leakage          | Cannot shuffle          |

---

If you want, I can also prepare:

A **diagram** of each CV type
A **side-by-side comparison PDF**
**Interview questions** from this topic
**Python notebook-style explanation**

Just tell me!
