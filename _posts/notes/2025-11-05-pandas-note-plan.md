---
layout: post
title:  "Pandas – note plan"
author: Dipak Pulami Magar
date: 2025-11-05 10:12:45 +0545
categories: note-plans
status: draft
---
## Table of Contents
[1. Introduction to Pandas](#1-introduction-to-pandas)  
[2. The Fundamental/Core Data Structures](#2-the-fundamentalcore-data-structures)   
[3. Data Input and Output (I/O) Operations](#3-data-input-and-output-io-operations)    
[4. Initial Data Inspection and Summary (Statistics) ](#4-basicinitial-data-inspection-and-summary-statistics)  
[5. Data Selection, Indexing](#5-data-selection--indexing-and-subsetting)  
[6. Data Cleaning preprocessing](#6-data-cleaning--preprocessingpreparation)  
[7. Data Transformation and Manipulation](#7-data-transformation-and-manipulation)  
[8. Data Aggregation and Grouping](#8-data-aggregation--grouping)  
[9. Combining, merging, and concatination](#9-combining-merging-joining-and-concatenating-dataframesdatasets-data-manipulation)  
[12. Working with Time Series](#12-working-with-time-series-and-categorical-datatime-series-analysis)  
[15. Visualization with Pandas](#15-visualization-with-pandas)

---

## 1. Introduction to Pandas
### What is Pandas 
  * Definition: 
    * A fast, powerful, and flexible open-source data analysis and manipulation library for Python.
    * Built on top of NumPy.
### Key features and benefits/advantages
  - History and development
### Key uses: why it’s used/primary use cases
  * Data cleaning, transformation, data manipulation, 
  * analysis, and visualization preparation.
* **Comparison with NumPy**
  * Relation to **NumPy** (Pandas is built on top of NumPy).
  * Comparison with other libraries (e.g., NumPy, Polars)
  * Overview of Pandas ecosystem (relation to NumPy, Matplotlib, etc.)

* Installation and Import: (using pip, conda)
  * `pip install pandas`:
  * `import pandas as pd`: 

- Pandas data structures overview (`Series` vs/& `DataFrame`)
  * Data structures in Pandas: `Series` and `DataFrame`

---

## 2. The Fundamental/Core Data Structures
### 2.1. (Pandas) Series:
  * One-dimensional labeled array.
  * Creating Series: 
    * from lists, dictionaries, NumPy arrays, scalar values
  * Anatomy: Index and Values.
  * Key attributes: 
    * `.index`: 
    * `.values`: 
    * `.dtype`: 
    * `.name`: 
    * shape
  +++  
  - Indexing and index objects
  - Vectorized operations
  - Boolean indexing with Series
  - Handling missing values in Series

* Indexes and Labels
* Accessing elements (`.loc[]`, `.iloc[]`, slicing)
* Operations on Series
  * Arithmetic, comparison, and broadcasting

* Useful Series methods
  * `head()`: 
  * `tail()`: 
  * `describe()`: 
  * `value_counts()`: 
  * `unique()`: 
  * `nunique()`: 
  * `map()`: 
  * `apply()`: 

* Handling missing values in Series 
  * `isna()`: 
  * `fillna()`: 
  * `dropna()`: 

### 2.2. (Pandas) DataFrame:
* Two-dimensional labeled data structure (like a spreadsheet or SQL table).

* Creating DataFrames from:
  - From dicts
  - from dict of Series/lists, 
  - list of dicts, List of dictionaries
  - NumPy arrays, 
  - from a file (e.g., CSV, Excel).CSV/Excel files
  - Dictionaries of lists/Series
  - External databases

* DataFrame Anatomy: DataFrame structure:
  * Index
  * Columns, 
  * and Data.

* Key/Essential attributes: 
  * `.index`: 
  * `.columns`: 
  * `.axes`:
  * `.dtypes`: 
  * `.shape`: 
  * `.size`: 
  - `.ndim`: 
  - `.values`:  
- Essential methods:
  - `.info()`: 
  - `.describe()`:
  - `.head()`: 
  - `.tail()`: 
  - `.sample()`: 

---

## 3. Data Input and Output: (I/O) Operations
### 3.1. Reading data: from various sources/formats
* `pd.read_csv()`: # key parameters: sep, header, index_col, usecols, dtype; Parameters like sep, header, index_col, dtype
* `pd.read_excel()`: # sheet_name, engine; from Excel; Sheet selection, multi-sheet handling
* `pd.read_json()`: # orient, lines; from JSON; Orientation options
* `pd.read_html()`: # web scraping; HTML tables
* `pd.read_sql()`: # sql, con; Queries, connections;  SQLAlchemy engine |
* `pd.read_clipboard()`: from Clipboard; Clipboard
* `pd.read_table()`: from Flat Files??
* `read_fwf`: 
* From URLs.
* Parquet, HDF5, Feather, and other efficient formats

* Important Parameters for reading:
  - `index_col`: 
  - `header`: 
  - `usecols`: 
  - `parse_dates`: 
  - `sep`: 
  - `dtype`:  
  - `nrows`: 

### 3.2. Writing Data: to files
* `df.to_csv()`:  # index=False, header, encoding; (important: `index=False`); Parameters like index, header, mode
* `df.to_excel()`: # `sheet_name`, `index`; 
* `ExcelWriter`: Multi-sheet writing with ExcelWriter
* `df.to_sql()`: writing to a database; Handling if_exists, chunksize;  SQLAlchemy engine
* `df.to_json()`: # `orient`; Orientation (split, records, etc.)
* `df.to_parquet()`: # efficient storage; efficient binary format, highly recommended for large datasets.

* Key **parameters** for writing:
  * `index=False`:
  * `header=False`:
  * `sheet_name`):
  * `mode`
* Handling large datasets: Chunking, iterators
* Parameters for performance and memory optimization

---

## 4. Basic/Initial Data Inspection and Summary (Statistics)
* **Initial Review:** Checking basic info: Viewing data: 
  * `df.head()`:  
  * `df.tail()`:
  * `df.sample()`: sampling; see random parts of your data

  * `df.info()`: comprehensive overview; Concise summary: 
    * (data types, entries, columns, Dtype/Data types, non-null counts, memory usage).
  * `df.describe()`: 
    * Summary statistics for numerical columns; (include/exclude parameters)
    * Descriptive statistics (count, mean, std, min, max, quartiles).

  * `df.value_counts()`: column value counts
  * `df.shape`: Dimensions of the DataFrame.
  * `df.columns`: List of column names.
  * `df.index`: 
  * `df.axes`: 
  * `df.shape`: Shape
  * `df.size`: size
  * `df.memory_usage()`: memory consumption

* **Data Types:**
  * `df.dtypes`: Data types of each column; checking types
  * `.astype()`: converting types
  * Understanding common Pandas dtypes 
    * (`int64`, `float64`, `object`, `category`, etc.).

---

## 5. Data Selection & Indexing, Subsetting/Slicing and Filtering
*This is a critical section. Understand the difference between `[]`, `.loc[]`, and `.iloc[]`.*
* **Basic Selection:**
    * Selecting columns (as Series and as a DataFrame subset).
    * Selecting rows using list slicing (`df[10:20]`).
* **Label-based Indexing:**
    * Using **`.loc[]`** (selection by labels/names for rows and columns).
    * Conditional/Boolean filtering (e.g., `df[df['Age'] > 25]`).
* **Position-based Indexing:**
    * Using **`.iloc[]`** (selection by integer position for rows and columns).
* **Advanced Indexing:**
    * Setting, resetting, and modifying the index: `.set_index()`, `.reset_index()`.
    * Working with **MultiIndex** (Hierarchical Indexing).
---

* Accessing data
  * Selecting columns (`df['col']`), rows (`.loc[]`, `.iloc[]`), slices

* Copying vs referencing (`copy(deep=True)`)

### Column Selection: selecting columns
- `df.columns`: Column attributes
- `df['column_name']`: Single column as Series
- `df[['column_name']]`: Single column as DataFrame
- `df[['col1', 'col2']]`: Multiple columns
- `.rename(columns={})`: Renaming columns

### Row Selection: selecting rows
#### By label/index: `.loc[]` (label-based indexing)
- `df.loc['index_label']`: Single row
- `df.loc[['label1', 'label2']]`: Multiple rows
* `df.loc['label1/start':'label3/end']` (inclusive!): Slicing with labels

#### By integer position: (position-based indexing)`.iloc[]` 
  - `df.iloc[0]`: Single row: 
  - `df.iloc[[0, 2, 4]]`: Multiple rows: 
  - `df.iloc[0:5]`: Slicing with index-position (exclusive of the stop index)

#### Boolean Indexing/Filtering Data/Conditional selection 
- Single condition
  - `df[df['col'] > value]`: 
    - `df[df['age'] > 30]`: 
    - `df.loc[df['age'] > 30]`:
* Multi-condition filtering with `&`, `|`, `~`:
* Boolean indexing with multiple conditions (`&`, `|`, `~`).
  - `(df['age'] > 30) & (df['city'] == 'NYC')`: Multiple conditions
- `.isin()` method
* Using `.isin([list])`.
- `.query()` method for complex filtering
  * Using `.query()` method.

- Boolean indexing with multiple categories
* Using `.str` methods for text filtering.

### Combined Selection/Selecting Subsets (of Rows and Columns)/Subsetting
- `df.loc[row_labels, col_labels]`:
  - `df.loc[3,'weight']`
  - `df.loc[3,'weight'] = 50` # changing its value
- `df.iloc[row_positions, col_positions]`:
  - `df.iloc[]
  - `df.iloc[3,'weight'] = 50` 


* Using `.loc[]`: 
  * `df.loc[rows_selection, columns_selection]`
    * `df.loc[df['age'] > 25, ['name', 'city']]`
* Using `.iloc[]`: 
  * `df.iloc[row_indices, column_indices]`
  * `df.iloc[3, 3]`
  * `df.iloc[3, 3] = 50` # change values of [3,3] to 50
  * Example: `df.iloc[0:5, [1, 3]]`

- `df.at[]` and `df.iat[]` for scalar access
* `isin()`, `between()`, `where()`, `mask()`

---

## 6. Data Cleaning & Preprocessing: Preparation
### 6.1. Handling Missing Data: [done]
- Detecting/identifying/checking missing values/data:
  - `.isna()`: 
  - `.isnull()`:
  - `.notna()`: 
  - `.notnull()`: 
- Counting: 
  - `.isnull().sum()`: Count of missing values per column.
  - `.isnull().mean()`: 
- Dropping missing values: 
  - `.dropna()`: 
    - (axis, how, thresh, subset)
    - (how='any'/'all', axis, thresh, subset)
    - (rows/columns, parameters like `how='all'`, `subset`).
- Filling missing values: 
  - `.fillna()`:
    - e.g. `df.fillna(0)`, `df['balance'].fillna(df['balance'].mean())` 
    - (value, method='ffill'/'bfill', limit) ; 
    - (ffill/bfill, interpolation) 
    - (with a scalar, mean/median/mode, or forward fill `ffill` and backward fill `bfill`)
- Interpolation: 
  - `.interpolate()`: (method, limit_direction)
- Dropping or filling NaNs conditionally

### 6.2. Handling Duplicates/duplicate data: [done]
- `df.duplicated()`: Detecting/identifying duplicates:
  - (subset, keep)
- `df.duplicated().sum()`: Counting duplicates
- `df.drop_duplicates()`: Removing/dropping duplicates
  - (subset, keep='first'/'last'/False)

### 6.3. Column Operations: Adding, Renaming/modifying and Dropping  
- **Adding columns**: [done]
  - `df['new'] = values`:
  - `df['new_col'] = ...`: Add [done]
  - `df.assign()`: Adding columns: 
    * `df.assign(new_col=...)`: Add

- **Renaming columns**: `.rename()` [done]
  * `df.rename(columns={'old':'new', 'old':'new'})`: 
  * `df.rename({'make':'make1', 'model':'model1'}, axis=1)`

- **Dropping columns/index**: `df.drop()`
  - `df.drop(columns=[])`: 
  * `df.drop(columns=['col1', 'col2'])`:
  * `df.drop(['col1'], axis=1)`:
    * `df.drop(columns={'full_name', 'balance'})` #
    * `df.drop(['name'])` ??

- **Modifying data/values:**
  * `.replace()`: replacing values
    * `df['l_name'] = df['l_name'].replace({'Tamang':'Lama', np.nan: 'Nepali'})` --->
    * `df['priority'] = df['priority'].replace({'yes': True, 'no': False})`
  * `.map()`: mapping values
    * `df['l_name'] = df['l_name'].replace({'Tamang':'Lama', np.nan: 'Nepali'})`
    * `df['priority'] = df['priority'].replace({'yes': True, 'no': False})`

### 6.4 Index/Row Operations: [done]
- **Adding an Index**: #Adding new index/row in pandas
  - `df.loc['k'] = ['rabbit', 4, 2, 'yes']`
  - Adding multiple indexes: using `.concat()`

- **Rename index(s)/row(s)**
  - `df.rename({2:20, 3:30})` # rename index 2 and 3 to 20 and 30
  - `df.rename({2:20, 3:30}, axis=0)` # same thing, axis is optional/dual
  - `df.rename({'a':'A', 'b':'B'})`
  - `df.rename(index={2:20, 3:30})`
  
- **Drop index(s)/row(s)**:
  - `df.drop(4)`: 
  - `df.drop(5, axis=0)` # axis=0, optional/default
  - `df.drop([6, 7, 8], axis=0)`
  - `df.drop('k', axis=0)`
  - `df.drop(['c', 'd', 'e'], axis=0)`

- **Changing a Value**: 
  - `df.loc['f', 'age'] = 1.5`

* Handling outliers

### Data Type Conversion/Changing Data Types: See basic/initial
- `.astype()` - basic type conversion; for simple conversions (e.g., `df['col'].astype('int32')`)
- `pd.to_numeric()` - with error handling; more robust, handles errors (`errors='coerce'`)
- `pd.to_datetime()` - date parsing; convert to datetime.
- `pd.to_timedelta()`: 
- `infer_objects()` - smart type inference

### String Operations
- String accessor: `.str`
- Common methods:
  - Case: 
    - `str.lower()`, 
    - `str.upper()`, 
    - `stritle()`
  - Searching: 
    - `str.contains()`, 
    - `str.startswith()`, 
    - `str.endswith()`
  - Manipulation: 
    - `str.replace()`, 
    - `str.strip()`, 
    - `str.split()`, 
    - `str.extract()`
  - Information: 
    - `.len()`, 
    - `.find()`

---

## 7. Data Transformation and Manipulation

### 7.1. Sorting
- Sorting by index:
  - `.sort_index()` (ascending, inplace)ascending, na_position)
- Sorting by values: ascending, na_position)
  - `.sort_values()` (by, ascending, na_position)
  - `df3 = df.sort_values('visits')` # default: ascending=True
  - `df2 = df.sort_values('age', ascending=False)`
  - `df.sort_values(by=['col1', 'col2'], ascending=[False, True])` (multiple columns)
    - `df4 = df.sort_values(by=['age', 'visits'], ascending=[False, True])` # can be more than two
* Reindexing (`reindex()`)
* `.reindex()`: Reordering: column selection or 
* Changing column order

### 7.2. Applying Functions
- `.map()` - element-wise Series transformation; Element-wise transformation on a Series.
- `.apply()` - row/column-wise DataFrame operations; Row-wise or column-wise transformation on a DataFrame. More flexible, but slower.
- `.applymap()` - element-wise on entire DataFrame; Element-wise on a whole DataFrame (less common).
* Applying Functions:
    * Element-wise operations: Using NumPy functions or lambda functions with **`.apply()`** on a Series.
    * Row-wise or Column-wise operations: Using **`.apply()`** with `axis=0` or `axis=1`.
* **Vectorized operations** are preferred for performance.
- **Lambda functions** with apply

### Binning & Discretization
- `pd.cut()` - equal-sized bins
- `pd.qcut()` - quantile-based bins

---

## 8. Data Aggregation & Grouping
### Basic/Simple Aggregation: Statistical Methods/Descriptive statistics
- **Single function**: 
  - `describe()`: Summary statistics for numerical columns.?? 
  - `sum()`:
  - Counts: 
    - `.count()`: 
    - `.value_counts()`: For categorical columns.
    - `.nunique()`:
  - Extremes: 
    - `.min()`: 
    - `.max()`:
  - Central tendency:
    - `.mean()`: 
    - `.median()`: 
    - `.mode()`: 
  - Dispersion: 
    - `.std()`: 
    - `.var()`: 
    - `.mad()`:
  - Quantiles: 
    - `.quantile()`: 
    - `.percentile()`: 
- **Multiple functions**: 
  - `.agg(['mean', 'std', 'count'])`
- **Column-specific**: 
  - `.agg({'col1': 'mean', 'col2': ['min', 'max']})`

* Grouping by multiple columns
* Iterating over groups
* Transformations (`transform()`)
* Pivot tables (`pivot_table()`)
* Cross-tabulation (`pd.crosstab()`)

### GroupBy Operations: Grouping Basics
- **Split-Apply-Combine pattern**
  - `.groupby('col')`: Single column grouping
  - `.groupby(['col1', 'col2']`: Multiple columns
  - `.groupby(lambda x: x.year)`: Grouping with functions

1.  **The `groupby` Mechanism**
    * Concept: Split-Apply-Combine.
    * Syntax: `df.groupby('by_column')`
    * Aggregating: `.agg(['mean', 'std'])` or `.agg({'col1':'sum', 'col2':'mean'})`
    * Iterating over groups.
    * Grouping by multiple columns.

- **GroupBy methods**:
  - Aggregation: `.sum()`, `.mean()`, `.size()`
  - Transformation: `.transform()`
  - Filtration: `.filter()`
  - Iteration: `for name, group in df.groupby()`

* **Grouping and Aggregation:**
    * The **Split-Apply-Combine** strategy.
    * Using **`.groupby()`** and common aggregation functions (e.g., `.mean()`, `.sum()`, `.count()`, `.agg()`).

### Advanced Grouping: Pivot Tables & Cross-Tabulation
- `.agg()` with custom functions
- Named aggregation with tuples
- `.pivot_table()` - multi-dimensional analysis
- `.crosstab()` - frequency tables
- `pd.pivot_table()` - `index`, `columns`, `values`, `aggfunc`.
- `pd.crosstab()` - For computing a simple frequency table.

---

## 9. Combining DataFrames/DataSets: Data Manipulation??
### 9.1. Concatinating DataFrames (stacking/side-by-side): `pd.concat()`
- Key parameters: `axis=0/1`, `join='inner'/'outer'`, ignore_index, keys
- Row-wise vs column-wise concatenation
  * `axis=0` (row-wise, stacking), 
  * `axis=1` (column-wise, side-by-side).
* join

### 9.2. Merging DataFrames: `pd.merge()`
- SQL/Database-style joins
- Join types (`how`): inner, outer, left, right, cross
- Key parameters: `on`, `left_on`, `right_on`, `how`, `suffixes`.
- Indicator for merge diagnostics

### 9.3. Joining on indexes/index-based joining: `.join()`




* **Difference between `merge` (general) and `join` (on index)**
  * SQL/Database-style joins vs ____________

- **`.combine_first()`** - filling missing values
* Combining data from multiple sources

---

## 10. Reshaping and Pivoting
* `melt()`: 
* `pivot()`: 
* Stacking and unstacking
* Wide vs long format
* MultiIndex and hierarchical indexing

### **Pivot Tables & Melting**
- `pd.pivot_table()` - multi-dimensional aggregation
- `.pivot()` - reshaping without aggregation
- `.melt()` - wide to long format
- `.stack()` and `.unstack()` - hierarchical indexing

* **Reshaping Data:**
  * Pivoting data: **`.pivot_table()`** (similar to pivot tables in spreadsheets).
  * Melting data: `pd.melt()` (wide to long format).
  * Stacking/Unstacking.

---

## 11. Working with Indexes
* Setting and resetting indexes (`set_index()`, `reset_index()`)
* Hierarchical (multi-level) indexes
* Index sorting and selection
* Reindexing and alignment

---

## 12. (Working with) Time Series and Categorical Data/Time Series Analysis
* **Working with DateTimeIndex/DateTime Handling**
  * `pd.to_datetime()`: Converting to datetime
  * `pd.to_datetime()` - parsing dates
  * Setting a datetime column as the index.
  * `pd.date_range()`: 
  * `pd.date_range()` - generating date sequences
  * Setting a DateTimeIndex.
  * Accessing date/time components (e.g., `.dt.year`, `.dt.day_name()`).
* Date indexing and slicing
* **Time-Based Indexing & Slicing**
  * Partial string indexing: 
    * `df.loc['2020']`, 
    * `df.loc['2020-01']`
  * Slicing: `df.loc['2020-01-01':'2020-01-15']`
  
* Resampling, shifting, and time zone handling.
* **Resampling** (`resample()`)
  * `.resample('M').mean()`: Downsampling (to a lower frequency).
  * `.resample('D').ffill()`: Upsampling  (to a higher frequency).

* Shifting and lagging (
  * `shift()`, 
  * `tshift()`)


### **Resampling & Rolling**
- **Resampling**: `.resample()` (up/down sampling)
  - Downsampling: 'D'→'M', 'H'→'D'
  - Upsampling: 'D'→'H' with filling/interpolation
- **Rolling operations**: 
  - `.rolling()` for moving averages
- **Expanding operations**: 
  - `.expanding()`
- * Rolling and expanding windows (
  * `rolling()`, 
  * `expanding()`)


- DateTimeIndex properties and methods
- Timezone handling with 
  - `tz_convert()`: 
  - `tz_localize()`: 

### **Time-Based Operations**
- `.set_index()`: Setting datetime index
- Time-based indexing: 
  - `df.loc['2023']`, 
  - `df.loc['2023-01':'2023-03']`
- Date properties: 
  - `.dt.year`, 
  - `.dt.month`, 
  - `.dt.day_name()`

* **Categorical Data:**
    * Creating and converting to `category` dtype.
    * Benefits of using categorical data (memory and speed).
    * Getting dummy variables/one-hot encoding: **`pd.get_dummies()`**.
---

## **14. Performance Optimization**
* Memory usage and profiling 
  * (`memory_usage()`: 
  * `info(memory_usage='deep')`)
* Using `categorical` data types
* Vectorization over loops
* Chunked reading of large files
* Using `df.eval()` and `df.query()` for performance
- Method chaining for readability
- Vectorized operations vs apply
- Efficient dtypes and memory usage
- `pd.eval()` for expression evaluation
- Using `.isin()` instead of multiple OR conditions
* Using optimized methods like `.at`, `.iat`, `.loc`, `.iloc` over iterative loops.
* The efficiency of vectorized operations over **`.apply()`** (when possible).
* Understanding **`copy()`** and "SettingWithCopyWarning" to avoid chained assignment issues.

---

## 15. Visualization (with Pandas): Integration with Visualization
* Basic built-in plotting with (`df.plot()`, `plot(kind='bar')`, etc.)
* Line, bar, histogram, box/box plots, scatter, area plots
* Customizing plots: titles, labels, colors, legends
* Subplots and multiple figures
* Integration with Matplotlib and Seaborn (passing the DataFrame as data)

---

## 16. Advanced Topics
* MultiIndex operations
* Working with categorical data
* Handling large datasets (`chunksize`, `Dask`)
* Method chaining (using `pipe()`)
* Pandas options and settings (`pd.set_option()`)
* Style formatting (`df.style`)

### Categorical Data
- `astype('category')` for memory efficiency
- Ordered categories
- Performance benefits with groupby and sorting
* Benefits: Memory efficiency and performance for fixed, repeating values.

### MultiIndex DataFrames
- Creating MultiIndex (from_tuples, from_product)
- Indexing with MultiIndex (.loc with tuples)
- Cross-sections with `.xs()`
- Stacking and unstacking levels

4. **Styling DataFrames**
  * Using `.style` to apply conditional formatting for display in Jupyter notebooks.

2. **Handling Large Data**
  * Specifying `dtype` on import.
  * Using `chunksize` for iterative processing.
  * **Dask** as a parallel-computing alternative.

3. **Method Chaining**
  * Writing clean, readable code by chaining methods.
  * Example: `(df.load_data().query('age > 30').groupby('city')['income'].mean().round(2))`

---

## 17. Integration with Other Libraries
* Pandas + NumPy
* Pandas + Matplotlib / Seaborn
* Pandas + Scikit-learn (`train_test_split`, `get_dummies()`)
* Pandas + SQL / Databases

---

## 18. Real-World Case Studies / Practice
* Exploratory Data Analysis (EDA) workflow
* Cleaning messy datasets (missing values, inconsistent text)
* Combining datasets (merging, reshaping)
* Feature engineering with Pandas
* Time series analysis
* Generating reports or dashboards

## 12. Practical Patterns & Best Practices
### Common Operations
- Handling large datasets with chunksize
- Memory optimization with categoricals and dtypes
- Method chaining patterns
- Pipeline creation

### Troubleshooting & Debugging
- Common errors and solutions
- Performance profiling with `%timeit`
- Memory usage analysis
- Data validation techniques

### Integration with Other Libraries
- Visualization with Matplotlib/Seaborn
- Statistical analysis with SciPy/StatsModels
- Machine learning with Scikit-learn
- Web applications with Streamlit

## 13. Real-world Applications
- Data cleaning pipelines
- Exploratory Data Analysis (EDA) workflow
- Time series forecasting preparation
- Feature engineering examples
- Data validation and quality checks

### Pro-Tips for Your Notes:
* **Code Snippets:** For every topic, include a small, clear code example.
* **Common Pitfalls:** Note down common errors, like using chained assignment (`df[df.age > 25]['salary'] = 1000`), which should be avoided in favor of `.loc`.
* **"Cheat Sheet" Section:** Create a quick-reference page with the most common operations and their syntax.
* **Visuals:** Use diagrams to explain concepts like `groupby` (Split-Apply-Combine) and `merge` operations.