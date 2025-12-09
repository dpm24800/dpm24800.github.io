
In pandas, `df.describe()` behaves differently for object (string) columns.
By default: `df.describe()` only summarizes numeric columns.
To get describe() for object/string columns, do this:

```py
df.describe(include=['object']) # Describe only object columns
df.describe(include='object') # Describe only object columns
df.describe(include='all') # Describe all columns (numeric + object)
```

### What it shows for object columns
For each string/object column, you get:

| Statistic  | Meaning                    |
| ---------- | -------------------------- |
| **count**  | Number of non-null entries |
| **unique** | Number of unique values    |
| **top**    | Most frequent value        |
| **freq**   | Frequency of top value     |
