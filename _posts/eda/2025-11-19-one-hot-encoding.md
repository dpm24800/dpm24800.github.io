---
layout: post
title: One-Hot Encoding (OHE)
description: 
# thumbnail: ../../../../assets/images/pandas/encoding-categorical-data.png
author: Dipak Pulami Magar
date:   2025-11-18 20:12:45 +0545
categories: pandas
status: published
---

- One-hot encoding in Pandas is a method to convert categorical data into a numerical format suitable for machine learning algorithms. 
- It transforms a categorical column into multiple binary columns, where each new column represents a unique category from the original column.

**How it works**:
- For each unique category in the original column, a new binary column is created.
- In a given row, if the original value matches the category represented by a new column, that new column will have a value of 1, and all other new columns for that row will have a value of 0.

Implementation with `pandas.get_dummies()`:

The `pandas.get_dummies()` function is the primary tool for one-hot encoding in Pandas.

Example:
```py
import pandas as pd

# Create a sample DataFrame
data = {'Fruit': ['Apple', 'Banana', 'Apple', 'Orange', 'Banana'],
        'Color': ['Red', 'Yellow', 'Green', 'Orange', 'Green']}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Perform one-hot encoding on the 'Fruit' column
df_encoded = pd.get_dummies(df, columns=['Fruit'])

print("\nDataFrame after one-hot encoding 'Fruit':")
print(df_encoded)

# Perform one-hot encoding on multiple columns with 'drop_first=True' to avoid multicollinearity
df_encoded_multi = pd.get_dummies(df, columns=['Fruit', 'Color'], drop_first=True)

print("\nDataFrame after one-hot encoding 'Fruit' and 'Color' with drop_first=True:")
print(df_encoded_multi)
```

**Explanation**:
- `pd.get_dummies(df, columns=['Fruit'])`: This line applies one-hot encoding to the 'Fruit' column. It creates new columns like 'Fruit\_Apple', 'Fruit\_Banana', and 'Fruit\_Orange', replacing the original 'Fruit' column.
- `drop_first=True`: This argument, when set to `True`, prevents multicollinearity by dropping the first category of each encoded column. For example, if you have 'Red', 'Green', 'Blue', it will create 'Green' and 'Blue' columns, and if both are 0, it implies 'Red'.

When to use it:
- When dealing with nominal categorical data (categories without inherent order, like colors, cities, etc.).
- When machine learning models require numerical input.

**Considerations**:
- **High Cardinality:** 
  One-hot encoding can lead to a large number of new columns if a categorical variable has many unique categories (high cardinality), potentially causing issues like the curse of dimensionality.

- **Multicollinearity:** 
By default, `get_dummies` creates a column for every unique category. For some models (e.g., linear regression), this can introduce multicollinearity. `drop_first=True` can mitigate this.



