Here is a **simple, clear, beginner-friendly explanation of Underfitting**:

---

# 🎯 **What is Underfitting?**

**Underfitting** happens when a machine learning model is **too simple** and cannot learn the real patterns in the data.

As a result:

* The model performs **poorly on training data**
* And also performs **poorly on test data**

👉 **The model neither memorizes nor understands — it learns too little.**

---

# 📘 Example (Easy to Understand)

Imagine you are preparing for exams:

* You study only 2–3 pages.
* You don’t understand the topic deeply.
* In the exam, you cannot answer most questions.

This is **underfitting** — not enough learning.

---

# 🧠 Technical Understanding

An underfitted model has:

* **Low training accuracy**
* **Low test accuracy**
* **High bias**
* **Oversimplified structure**

Examples:

* Using a **straight line** to fit data that actually curves
* Using too few features
* Too little training time

---

# 🖼 Visual Understanding

```
Underfitting:  model is too simple — misses patterns
Good Fit:     balanced — captures real patterns
Overfitting:  model is too complex — memorizes noise
```

---

# 🔍 How to Detect Underfitting?

Look for this pattern:

| Dataset  | Accuracy |
| -------- | -------- |
| Training | Low      |
| Testing  | Also low |

Both being low = **underfitting**.

---

# 🛠 How to Fix Underfitting?

### ✔ 1. Use a More Complex Model

* Try deeper models
* More parameters
* More powerful algorithms

### ✔ 2. Add More Features

* Feature engineering
* Use relevant columns

### ✔ 3. Train Longer

* Increase epochs in neural networks
* Allow model to learn enough

### ✔ 4. Reduce Regularization

* Too much regularization forces the model to be simple
* Reduce L1/L2 or dropout

---

# 🔧 Example in Python (Detecting Underfitting)

```python
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print("Train:", train_score)
print("Test:", test_score)
```

If both scores are **low**, your model is underfitting.

---

If you want, I can also explain:
👉 Underfitting vs Overfitting (table + graph)
👉 Bias-variance tradeoff
👉 Practical examples (classification, regression)
👉 How to fix in deep learning

Just tell me!
