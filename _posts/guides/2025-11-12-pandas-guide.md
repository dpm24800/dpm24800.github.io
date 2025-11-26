---
layout: post
title:  Pandas Guide
description: 
# thumbnail: ../../../../../assets/Correl.png
author: Dipak Pulami Magar
date:   2025-11-12 10:12:45 +0545
categories: pandas
status: published
---
```py
import pandas as p
pd.__version__ # pandas version

pd.show_versions() 
# all the *version* information of the libraries that are required by the pandas library.

# Creating DataFrame from a dictionary
df = pd.DataFrame[dictonary]
    df = pd.DataFrame[dict1]

# Creating DataFrame from a dictionary with index (from a list: with equal lengtg as the dictionary)
df = pd.DataFrame[dictonary, index=list] 
# list size should match the size of dictionary as index
    df = pd.DataFrame(data, index=labels)
    # DataFrame `df` from this dictionary `data` which has the index `labels`

df.info()
df.describe()

df.head()
df.head(3)
df.tail()
df.tail(4)

# Sellecting multiple columns with all rows
df[['columnX', 'columnY']] # all rows and two columns: columnX and columnY 
    df[['animal', 'age']]

# Selecting specified rows and columns
df.loc[df.index[[index3, index4, index8]], ['columnX', 'columnY']] 
# extract data from index: 3, 4, 8 and columnX and columnY
    df.loc[df.index[[3, 4, 8]], ['animal', 'age']]

# Select the rows based on conditon
df1 = df.loc[df['column'] > 2] 
    df1 = df.loc[df['visits'] > 2]

# select the rows where the columnX is null (NaN)
df1 = df.loc[df['columnX'].isna()] 
    df1 = df.loc[df['age'].isna()]
	
# select the rows based on multiple condition
df1 = df.loc[(df['columnX'] == 'abc') & (df['age'] < 3)] 
    df1 = df.loc[(df['animal'] == 'cat') & (df['age'] < 3)]
    df1 = df.loc[(df['age'] > 2) & (df['age'] < 4)]

# Changing the value of a cell (row*column)
df.loc['index/row', 'column'] = "value" 
    df.loc['f', 'age'] = 1.5

# Finding sum of columnX
df['columnX'].sum()
    df['visits'].sum()

# Group
df1 = df.groupby(['columnA'])['columnX'].mean()
    df1 = df.groupby(["animal"])['age'].mean() 
    # mean age for each different animal

# Adding new index/row
df.loc['index/row'] = [column1, column2, column3, column4] 
    df.loc['k'] = ['rabbit', 4, 2, 'yes']

# Dropping a row or column
df.drop('index/row')
    df = df.drop('k')
    df = df.drop('animal', axis=1)
    df = df.drop('animal', axis=1)

# Counting the number of 'columnx'
df.value_counts('columnX')
    df.value_counts('animal')

# Sorting values
df.sort_values('column', ascending=True/False)
    df2 = df.sort_values('age', ascending=False)
    df3 = df.sort_values('visits') # default: ascending=True

df.sort_values(by=['columnX', 'columnY'], ascending=[False, True])
    df4 = df.sort_values(by=['age', 'visits'], ascending=[False, True])
     # can be more than two columns

# Replacing values
df['columnX'] = df['columnX'].replace({dict})
    df['priority'] = df['priority'].replace({'yes': True, 'no': False})
    # Replace 'yes' with True and 'no' with False

# Replacing values
df['columnX'] = df['columnX'].map({dict})
    df['priority'] = df['priority'].map({'yes': True, 'no': False}) # does the same thing
```