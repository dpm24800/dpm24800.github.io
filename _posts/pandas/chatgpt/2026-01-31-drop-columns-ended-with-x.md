---
layout: post
title:  Drop all columns whose names end with X
author: Dipak Pulami Magar
date: 2026-01-31 10:12:45 +0545
categories: pandas extras
status: draft
---

Clean way to drop all columns whose names end with `_encoded`:

```python
df = df.drop(columns=df.filter(regex=r'_encoded$').columns)
```

✅ This drops every column like:

* `city_encoded`
* `gender_encoded`
* `category_encoded`

(but not `encoded_city` or `city_encoded_old`).

If you want a slightly simpler version:

```python
df = df.loc[:, ~df.columns.str.endswith('_encoded')]
```

Both are correct — I usually prefer the second one because it is very clear and fast.

Given you were recently working with `pd.get_dummies` and encoding, this is useful when you want to remove old encoded features before re-encoding again.
