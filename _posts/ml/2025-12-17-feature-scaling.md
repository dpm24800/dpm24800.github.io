---
layout: post
title: Feature Scaling
# description: 
thumbnail: /assets/images/ml/feature-scaling.png
author: Dipak Pulami Magar
date:   2025-12-17 3:12:45 +0545
categories: ml
status: draft
---
- Feature scaling in machine learning is a crucial preprocessing step that transforms numerical features to a common scale (like 0-1 or mean=0, std=1) to prevent features with larger ranges (e.g., income) from dominating those with smaller ranges (e.g., age), ensuring algorithms treat all features equally, converge faster (like neural networks), and distance-based models (like KNN) perform accurately. 
- Common methods include Normalization (Min-Max Scaling) and Standardization (Z-score), applied after splitting data into training/test sets, fitting only on training data. 

## Why it's important: 
- **Prevents feature dominance**: Algorithms sensitive to magnitude (e.g., KNN, K-Means, SVM, Neural Networks) can overemphasize features with larger values.
- **Speeds up convergence**: Gradient descent-based models converge much faster with scaled features.
- **Improves model performance**: Ensures all features contribute meaningfully, leading to better accuracy and interpretability. 

## Common Techniques: 
### Normalization (Min-Max Scaling):  
Rescales data to a fixed range, usually [0].  

Formula:  
$$X_{scaled}=\frac{X-X_{min}}{X_{max}-X_{min}}$$

### Standardization (Z-Score Normalization): 
Rescales data to have a mean ($$\mu$$) of 0 and a standard deviation ($$\sigma$$) of 1.

Formula:
$$X_{scaled}=\frac{X-\mu }{\sigma }$$


### Robust Scaling:  
Uses percentiles, making it less sensitive to outliers. 

## When to use it: 
- Distance-based algorithms: KNN, K-Means, SVM, PCA.
- **Gradient descent-based algorithms**: Linear Regression, Logistic Regression, Neural Networks (for faster convergence). 

When not to use (or use with care): 
- **Tree-based models**: Decision Trees, Random Forests, XGBoost are generally insensitive to feature scaling because they split data based on thresholds, not distances. 

## How to apply: 
1. **Split** data into training and testing sets.
2. **Fit** the scaler *only* on the training data (e.g., `scaler.fit(X_train)`).
3. **Transform** both the training and testing data using the fitted scaler (e.g., `scaler.transform(X_train)`, `scaler.transform(X_test)`).