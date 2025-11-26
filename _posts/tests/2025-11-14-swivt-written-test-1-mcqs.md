---
layout: post
title:  Swivt Written Test – 1 (MCQs)
thumbnail: ../../../../../assets/images/swivt-tests/python-pandas-test.png
author: Dipak Pulami Magar
date:   2025-11-14 16:12:45 +0545
categories: test written
status: draft
---

Here is a curated set of **25 Multiple Choice Questions (with answers included)** from the recent Python, NumPy, and Pandas test conducted at our institute, **[Swivt Education](https://swivt.com.np/)**.

These questions cover fundamental concepts, syntax, data structures, and practical operations that every aspiring data professional should know. I encourage you to first attempt all questions on your own—this will help you identify your strengths and the areas that need more revision. After that, you can check the provided answers to evaluate your progress.

Whether you're preparing for interviews, strengthening your basics, or revising key topics, I hope this collection adds value to your learning journey.

Wishing you all the best on your path toward becoming a successful Data Scientist. Thank you!


---
# Questions
## 1. What is the output of this code?
```py
s = "Pytthon"
print(s[0:100][-1:1:-2])
```

a. nhy  
b. nohtyP  
c. nh  
d. nht  

## 2. What is the purpose of the finally block in exception handling?
a. Handle the error  
b. Execute code regardless of exception  
c. Raise a new exception  
d. Exit the program  

## 3. Which method is used to remove all items from a list?
a. delete()  
b. pop()  
c. clear()  
d. removeAll()  

## 4. Which statement is used to exit a loop in Python?
a. exit  
b. stop  
c. break  
d. return  

## 5. What will be the output of the following Python code?
```py
x = 0
while x < 3:
    x += 1
    if x == 2:
        continue
    print(x)
```
a. 
```
1  
2  
3
```  
b. 
```
1  
3
```  
c. 
```
1  
2
```
d. Error

## 6. What is the output of the following nested loop?
```py
numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:
    for y in items:
        print(x, y)
```
a.
```
10 Chair
20 Tables
10 Chair
20 Tables
```
b. 
```
10 Chair
10 Chair
10 Table
10 Table
```
c. 
```
10 Chair
20 Table
10 Chair
20 Table
```
d.
```
10 Chair
10 Table
20 Chair
20 Table
```

## 7. What is the result of this broadcasting operation?
```py
import numpy as np

a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])

print(a + b)
```

a. Error

b.
```
[[11 21 31]
 [12 22 32]
 [13 23 33]]
```
c. [11, 22, 33]  
d. [11 12 13 21 22 23 31 32 33]

## 8. What will be the shape of `np.ones((2, 3)) + np.array([1, 2, 3])`?
a. (2, 3)  
b. (2, 1)  
c. Error  
d. (3, 2)  

## 9. Which list comprehension correctly filters a list numbers to include only evennumbers?
a. `[x for x in numbers if x % 2 == 0]`  
b. `[x if x % 2 == 0 for x in numbers]`  
c. `[x for x in numbers else x % 2 == 0]`  
d. `[x where x % 2 == 0 in numbers]` 

## 10. Given the nested `if-else` structure below, what will be the value of `x`?
```py
x = 0
a = 0
b = -5

if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
    
print(x)
```

a. 2  
b. 0  
c. 3  
d. 4 

## 11. What does `np.arange(1, 10, 2)` return?
a. `[1, 2, 3, ..., 10]`  
b. `[1, 3, 5, 7, 9]`  
c. `[2, 4, 6, 8, 10]`  
d. `[1, 3, 5, 7]`

## 12. What is the difference between a list and a tuple in Python?
## 13. What are the four principles of OOPS?
## 4. What is the output of the below given code?
```py
str1 = "Hello World"

is_present = "Hello" in str1
print(is_present)
```
a. str1  
b. True  
c. False  
d. Error  

## 15. Which returns column names of a DataFrame?
a. `df.column_names()`  
b. `df.columns`  
c. `df.fields()`  
d. `df.header()`

## 16. `df.groupby('dept')['salary'].mean()` computes:
a. Total salary  
b. Count of salary  
c. Average salary per department  
d. Minimum salary  

## 17. What is a lambda function in Python?

## 18. What is the default behavior of `merge()`? 
a. outer join  
b. inner join  
c. left join  
d. full join

## 19. What does `plt.plot(x, y)` create?
a. Bar chart  
b. Scatter plot  
c. Line chart  
d. Histogram  

## 20. How to access the element at column 1, row 2 in a 2D array `a`?
a. a[2][1]  
b. a[1, 2]  
c. a[1][2]  
d. a[2, 1]  

## 21. What is the output of the following code if `filtered_numbers` is printed?
```py
numbers = [1, 2, 3, 4, 5]

filtered_numbers = [x for x in numbers if x % 2 == 0 and x > 2]

print(filtered_numbers)
```
a. [2, 4]  
b. [1, 2, 5]  
c. [4]  
d. Error: Multiple if conditions not allowed in list comprehension

## 22. What is the output of the following?
```py
import numpy as np

a = np.array([[1, 2], [3, 4]])

print(a[1][0])
```
a. 2  
b. 3   
c. 4  
d. Error 

## 23. What will be the shape of the array after the following operation?
```py
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
b = arr.reshape(3, 2)

print(b.shape)
```
a. (2, 3)  
b. (3, 2)  
c. (6,)  
d. Error 

## 24. What is the output of this code?  
```py
import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x[:, 1])
```
a. [1, 2]  
b. [3, 6]  
c. [2 5]  
d. Error 

## 25. Which of these loops will continue forever?
a. for i in range(3):   
b. while True:  
c. while False:  
d. for i in [1,2,3]:  

---

<center>
    <h2>Answers</h2>
</center>

**1**: d. nht  
**2**: b. Execute code regardless of exception    
**3**: c. clear()    
**4**: c. break   
**5**: b. 
```
1  
3
```    
**6**: d.
```
10 Chair
10 Table
20 Chair
20 Table
```   
**7**: b.
```
[[11 21 31]
 [12 22 32]
 [13 23 33]]
```   
**8**: a. (2, 3)   
**9**: a. [x for x in numbers if x % 2 == 0]   
**10**: a. 2  
**11**: b. [1, 3, 5, 7, 9]
**12**: 
```
List: Mutable, Ordered, Allows duplicates
Tuple: Immutable, Ordered, Allows duplicates
```
**13**: 
```
1. Inheritance
2. Polymorphism
3. Encapsulation
4. Abstraction
```
**14**: b. True   
**15**: b. `df.columns`   
**16**: c. Average salary per department  
**17**: A small, anonymous function defined with the lambda keyword, typically used for short, one-line operations.
**18**: b. inner join  
**19**: c. Line chart  
**20**: a. a[2][1] 
**21**: c. [4]
**22**: b. 3  
**23**: b. (3, 2)
**24**: c. [2 5]
**25**: b. while True:

---

<center>***** Thank You.*****</center>