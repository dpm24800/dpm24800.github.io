---
layout: post
title: Gradient Boosting Machine (GBM)
description: A Complete Practical & Mathematical Guide
thumbnail: /assets/images/ml/supervised-learning/gradient-boosting-machine.png
author: Dipak Pulami Magar
date:   2026-02-02 10:12:45 +0545
categories: ml supervised-learning
status: draft
---

## 1. Introduction
**Gradient Boosting Machine (GBM)** is an ensemble learning technique that builds a **strong predictive model by sequentially adding weak learners**, usually decision trees.

Unlike bagging methods (like Random Forest), where trees are built independently, **GBM builds trees one after another**, and each new tree focuses on correcting the mistakes made by the previous model.

In practice, GBM is one of the foundations behind:

* XGBoost
* LightGBM
* CatBoost

Classical GBM refers to the original framework proposed by **Friedman (2001)**.

---

## 2. Core Idea of Gradient Boosting

At a high level:

> GBM performs **gradient descent in function space**.

Instead of optimizing parameters, we optimize a **model function**.

We build a model:

$$
F(x) = \sum_{m=1}^{M} \gamma_m h_m(x)
$$

Where:

* $$h_m(x)$$ = weak learner (usually a small decision tree)
* $$\gamma_m$$ = step size (weight)
* $$M$$ = number of boosting stages

---

## 3. Boosting vs Bagging (Important distinction)

| Aspect      | Random Forest (Bagging) | GBM (Boosting)                  |
| ----------- | ----------------------- | ------------------------------- |
| Training    | Parallel                | Sequential                      |
| Focus       | Reduce variance         | Reduce bias + variance          |
| Idea        | Many independent trees  | Each tree fixes previous errors |
| Overfitting | More robust by default  | Needs careful tuning            |

---

## 4. Mathematical Intuition of GBM

Let us formalize it.

We want to minimize a loss function:

$$
\min_{F} \sum_{i=1}^{n} L(y_i, F(x_i))
$$

We build the model in stages:

$$
F_0(x) = \arg\min_{\gamma} \sum_i L(y_i, \gamma)
$$

Then for stage (m):

$$
F_m(x) = F_{m-1}(x) + \nu \cdot h_m(x)
$$

Where:

* $$\nu$$ is the learning rate
* $$h_m(x)$$ is chosen to reduce the current loss

---

### The key step – pseudo residuals

We compute:

$$
r_{im} = - \left[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\right]*{F=F*{m-1}}
$$

These are called **pseudo-residuals**.

We train the next tree to predict these residuals.

---

## 5. Concrete Example (Regression, Squared Error)

Assume the loss:

$$
L(y, F(x)) = \frac{1}{2}(y - F(x))^2
$$

Then:

$$
\frac{\partial L}{\partial F(x)} = F(x) - y
$$

So:

$$
r_{im} = y_i - F_{m-1}(x_i)
$$

➡️ For squared error, **GBM reduces to fitting trees on ordinary residuals.**

This is why GBM feels intuitive for regression.

---

### Small numeric example

Suppose we have 5 samples and the target is **lpa**.

| iq  | cgpa | lpa |
| --- | ---- | --- |
| 90  | 8    | 3   |
| 100 | 7    | 4   |
| 110 | 6    | 8   |
| 120 | 9    | 6   |
| 80  | 5    | 3   |

---

#### Step 1 – initial model

For squared loss, the optimal constant model is the mean of the targets:

$$
F_0=\text{mean}(y)
=\frac{3+4+8+6+3}{5}=4.8
$$

Predictions:

```
[4.8, 4.8, 4.8, 4.8, 4.8]
```

Residuals (negative gradients):

| iq  | lpa | residual = y − F₀ |
| --- | --- | ----------------- |
| 90  | 3   | -1.8              |
| 100 | 4   | -0.8              |
| 110 | 8   | 3.2               |
| 120 | 6   | 1.2               |
| 80  | 3   | -1.8              |

We now fit the first regression tree $$m_1(x)$$ on

```
[-1.8, -0.8, 3.2, 1.2, -1.8]
```

Let the learning rate be

$$
\nu = 0.1
$$

Then

$$
F_1(x)=F_0+0.1,m_1(x)
$$

---

#### Step 2 – second model

Assuming (as in your board illustration) that the tree predicts the current residuals,

$$
\text{increment}_1 = 0.1,m_1(x)
$$

| iq  | res1 | pred2 = 0.1·m₁(x) | res2  |
| --- | ---- | ----------------- | ----- |
| 90  | -1.8 | -0.18             | -1.62 |
| 100 | -0.8 | -0.08             | -0.72 |
| 110 | 3.2  | 0.32              | 2.88  |
| 120 | 1.2  | 0.12              | 1.08  |
| 80  | -1.8 | -0.18             | -1.62 |

Now fit the second tree $$m_2(x)$$ on

```
[-1.62, -0.72, 2.88, 1.08, -1.62]
```

and update

$$
F_2(x)=F_1(x)+0.1,m_2(x)
$$

---

#### Step 3 – third model

$$
\text{increment}_2 = 0.1,m_2(x)
$$

| iq  | res2  | pred3  | res3   |
| --- | ----- | ------ | ------ |
| 90  | -1.62 | -0.162 | -1.458 |
| 100 | -0.72 | -0.072 | -0.648 |
| 110 | 2.88  | 0.288  | 2.592  |
| 120 | 1.08  | 0.108  | 0.972  |
| 80  | -1.62 | -0.162 | -1.458 |

Fit $$m_3(x)$$ on

```
[-1.458, -0.648, 2.592, 0.972, -1.458]
```

and

$$
F_3(x)=F_2(x)+0.1,m_3(x)
$$

---

#### Step 4 – fourth model

$$
\text{increment}_3 = 0.1,m_3(x)
$$

| iq  | res3   | pred4   | res4    |
| --- | ------ | ------- | ------- |
| 90  | -1.458 | -0.1458 | -1.3122 |
| 100 | -0.648 | -0.0648 | -0.5832 |
| 110 | 2.592  | 0.2592  | 2.3328  |
| 120 | 0.972  | 0.0972  | 0.8748  |
| 80  | -1.458 | -0.1458 | -1.3122 |

Fit $$m_4(x)$$ on

```
[-1.3122, -0.5832, 2.3328, 0.8748, -1.3122]
```

and

$$
F_4(x)=F_3(x)+0.1,m_4(x)
$$

---

#### Step 5 – fifth model

$$
\text{increment}_4 = 0.1,m_4(x)
$$

| iq  | res4    | pred5    | res5     |
| --- | ------- | -------- | -------- |
| 90  | -1.3122 | -0.13122 | -1.18098 |
| 100 | -0.5832 | -0.05832 | -0.52488 |
| 110 | 2.3328  | 0.23328  | 2.09952  |
| 120 | 0.8748  | 0.08748  | 0.78732  |
| 80  | -1.3122 | -0.13122 | -1.18098 |

Fit $$m_5(x)$$ on

```
[-1.18098, -0.52488, 2.09952, 0.78732, -1.18098]
```

and

$$
F_5(x)=F_4(x)+0.1,m_5(x)
$$

---

#### Final boosted model

With 5 estimators and learning rate 0.1, the Gradient Boosting model is

$$
F(x)
====

4.8
+0.1,m_1(x)
+0.1,m_2(x)
+0.1,m_3(x)
+0.1,m_4(x)
+0.1,m_5(x)
$$

And the process continues.

This is the exact mechanism of GBM.

---

## 6. Why is it called “Gradient” Boosting?

Because the pseudo-residuals are:

$$
-\nabla_{F(x)} L(y, F(x))
$$

We are following the **negative gradient direction of the loss**.

So:

> GBM = Gradient descent in model space.

---

## 7. Algorithm (Regression GBM)

1. Initialize:

$$
F_0(x) = \arg\min_{\gamma} \sum_i L(y_i, \gamma)
$$

2. For m = 1 to M:

   * Compute pseudo-residuals
   * Fit a regression tree to residuals
   * Find optimal step size
   * Update model

---

## 8. Important Hyperparameters (scikit-learn GBM)
Below are the most important ones you will tune in practice.

1. **n_estimators** 
   - Number of boosting stages.
     * Large → more expressive
     * Too large → overfitting if learning rate is high

2. **learning_rate** 
   - Shrinkage parameter.
   - Controls how much each tree contributes.
   - Typical values:
     - 0.01 – 0.1
   - Lower learning rate → need more trees.

3. **max_depth** 
   - Depth of each individual tree.
   - Controls interaction order.
     - 1 → decision stumps (very weak learners)
     - 3–6 → commonly used

<!-- ### 8.4 min_samples_split / min_samples_leaf

Regularization through tree structure.

Helps control overfitting.

---

### 8.5 subsample

Fraction of samples used per tree.

If < 1.0 → **Stochastic Gradient Boosting**

Helps:

* reduce variance
* improve generalization

---

### 8.6 max_features

Number of features used when splitting.

Adds randomness similar to Random Forest.

---

### 8.7 loss

For regression:

* 'squared_error'
* 'absolute_error'
* 'huber'
* 'quantile'

For classification:

* 'log_loss' -->

---

## 9. Advantages of GBM

1. **Very strong predictive performance**  
GBM is usually stronger than:
   * single trees
   * linear models
   * bagging-based ensembles

2. **Flexible loss functions**  
You can optimize:  
   * MSE
   * MAE
   * Huber
   * quantile loss
   * log-loss

3. **Handles complex non-linear relationships**  
Excellent at capturing: 
   * feature interactions
   * threshold effects
   * non-linear patterns

1. **Works well on structured / tabular data**  
Still one of the strongest baselines for tabular problems.

## 10. Disadvantages of GBM
1. **Sensitive to hyperparameters**:  
Bad tuning can lead to:
   * severe overfitting
   * very slow training

2. **Training is slow**:  
Trees are built sequentially → no easy parallelization.

3. **Less robust to noisy labels**  
Because every tree tries to fit residuals, noise can be amplified.

4. **Harder to interpret**  
Compared to:  
   * linear models
   * single decision trees

5. **Memory and compute heavy**  
Especially when:
   * many trees
   * deep trees

---

## 11. GBM vs XGBoost / LightGBM (Short note)

Classical GBM:

* greedy CART trees
* no second-order derivatives
* no advanced regularization

Modern libraries add:

* second order optimization
* regularization
* histogram splits
* leaf-wise growth

But the **mathematical backbone is still GBM**.

---

## 12. Python Implementation (Regression – scikit-learn)

Since you recently worked on **burnout_score regression**, below is a clean template suitable for your workflow.

```python
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.ensemble import GradientBoostingRegressor

# -----------------------------------
# Example: assume df already exists
# target: burnout_score
# -----------------------------------

df = pd.read_csv("clean.csv")

X = df.drop(columns=['burnout_score'])
y = df['burnout_score']

# if categorical features exist
X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

gbm = GradientBoostingRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=3,
    min_samples_leaf=5,
    subsample=0.8,
    max_features=None,
    loss='squared_error',
    random_state=42
)

gbm.fit(X_train, y_train)

y_train_pred = gbm.predict(X_train)
y_test_pred = gbm.predict(X_test)

print("Train RMSE:", np.sqrt(mean_squared_error(y_train, y_train_pred)))
print("Test  RMSE:", np.sqrt(mean_squared_error(y_test, y_test_pred)))
print("Test R2:", r2_score(y_test, y_test_pred))
```

---

## 13. Hyperparameter tuning (GridSearch example)

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators": [200, 400],
    "learning_rate": [0.05, 0.1],
    "max_depth": [2, 3, 4],
    "min_samples_leaf": [3, 5, 10],
    "subsample": [0.7, 0.9]
}

gbm = GradientBoostingRegressor(random_state=42)

grid = GridSearchCV(
    gbm,
    param_grid,
    cv=5,
    scoring="neg_root_mean_squared_error",
    n_jobs=-1
)

grid.fit(X_train, y_train)

print("Best params:", grid.best_params_)

best_model = grid.best_estimator_

y_test_pred = best_model.predict(X_test)

print("Test RMSE:", np.sqrt(mean_squared_error(y_test, y_test_pred)))
print("Test R2:", r2_score(y_test, y_test_pred))
```

---

## 14. Important practical tuning strategy (Senior tip)

A reliable tuning sequence:

1. Fix a small `learning_rate` (0.05 or 0.03)
2. Tune:

   * `max_depth`
   * `min_samples_leaf`
3. Tune:

   * `subsample`
4. Increase `n_estimators` until validation stops improving

Do **not** tune everything at once.

---

## 15. Summary
Gradient Boosting Machine is:
* an additive model
* trained by functional gradient descent
* extremely powerful on structured data
* but sensitive to tuning and noise

The essential idea is:

> Fit a tree to the negative gradient of the loss at each step and add it to the current model.

This simple idea is what eventually evolved into XGBoost and LightGBM.

<!-- ---

If you want, in your next message I can extend this blog with a **classification GBM version (log-loss math + example)** so you have both regression and classification theory in one place for your notes. -->
