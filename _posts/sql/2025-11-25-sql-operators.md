---
layout: post
title: SQL Operators – SQL
author: Dipak Pulami Magar
date :  2025-11-25 16:12:45 +0545
categories: sql
status: draft
---

SQL operators are special symbols or keywords *(reserved words or characters)* used to perform operations (such as calculations, comparisons, and logical evaluations) on data within SQL queries. They are essential for tasks such as: filtering, combining, manipulating, and retrieving data from a database.

SQL operators can be broadly categorized into several types:
<!-- Here are the main categories of SQL operators: -->

## 1. Arithmetic Operators: 
  Used to perform mathematical operations on numeric data.
  - `+` (Addition)
  - `-` (Subtraction)
  - `*` (Multiplication)
  - `/` (Division)
  - `%` (Modulus - returns the remainder of a division)

```sql
    SELECT 10 + 5 AS SumResult;
    SELECT Salary * 1.10 AS NewSalary FROM Employees;
```

## Comparison Operators: 
  Used to compare values (one expression with another) and return a boolean result: TRUE, FALSE, or UNKNOWN (if a NULL value is involved).
  - `=` (Equal to)
  - `>` (Greater than)
  - `<` (Less than)
  - `>=` (Greater than or equal to)
  - `<=` (Less than or equal to)
  - `<>` or `!=` (Not equal to)

```sql
    SELECT * FROM Products WHERE Price > 50;
    SELECT * FROM Customers WHERE Country = 'Nepal';
```

## Logical Operators: 
  Used to combine multiple conditions or to negate a condition.
  These operators manipulate the results of conditions, typically combining multiple conditions in a WHERE clause.

  - `AND` (Returns TRUE if all conditions are TRUE)
  - `OR` (Returns TRUE if any condition is TRUE)
  - `NOT` (Negates a condition)

```sql
    -- Returns all orders where the quantity is greater than 
    -- 10 and the order date is after January 1, 2024.
    SELECT * 
    FROM Orders 
    WHERE Quantity > 10 
    AND OrderDate > '2024-01-01';
    
    -- Fetch employees who work in Sales and also earn more than 50,000.
    SELECT *
    FROM employees
    WHERE department = 'Sales'
    AND salary > 50000;

    -- Returns all employees who work either in the Sales 
    -- department or in the Marketing department.
    SELECT * 
    FROM Employees 
    WHERE Department = 'Sales' 
    OR Department = 'Marketing';

    -- Get all products that are either Electronics or Clothing.
    SELECT *
    FROM products
    WHERE category = 'Electronics'
    OR category = 'Clothing';
    
    -- Fetch customers who are not from the USA.
    SELECT *
    FROM customers
    WHERE NOT country = 'India';

    -- Return all employees except those whose job title is "Manager".
    SELECT *
    FROM employees
    WHERE NOT job_title = 'Manager';

    -- Combined
    -- Show orders that are Pending or Processing, and have 
    -- already been shipped (shipped_date not empty).
    SELECT *
    FROM orders
    WHERE (status = 'Pending' OR status = 'Processing')
    AND NOT shipped_date IS NULL;

    -- Show all expensive or premium products that are still available in stock.
    SELECT *
    FROM products
    WHERE (price > 100 OR category = 'Premium')
    AND NOT stock = 0;
    
```

## String Operators: 
  Used for pattern matching and string manipulation.
  - `LIKE` (Used with wildcards for pattern matching, e.g., `%` for any sequence of characters, `_` for any single character)
  - `||` (Concatenation - combines strings, though `+` is often used in some SQL dialects)

```sql
    SELECT * FROM Customers WHERE Name LIKE 'A%';
    SELECT FirstName || ' ' || LastName AS FullName FROM Employees;
```

## Set Operators: 
  Used to combine the result sets of two or more `SELECT` statements.

  - `UNION` (Combines results, removes duplicates)
  - `UNION ALL` (Combines results, includes duplicates)
  - `INTERSECT` (Returns only common rows between result sets)
  - `EXCEPT` or `MINUS` (Returns rows from the first query not present in the second)

```sql
    SELECT City FROM Customers UNION SELECT City FROM Suppliers;
```

## Other Operators:
  - `IN` (Checks if a value is within a list of values)
  - `BETWEEN` (Checks if a value is within a specified range)
  - `IS NULL` / `IS NOT NULL` (Checks for NULL values)
  - `EXISTS` (Checks for the existence of rows in a subquery)

```sql
    SELECT * FROM Products WHERE CategoryID IN (1, 3, 5);
    SELECT * FROM Library WHERE Books NOT IN ('Pandas Basics');
    SELECT * FROM Library WHERE Class BETWEEN 6 AND 12;
    SELECT * FROM Orders WHERE OrderDate BETWEEN '2025-01-01' AND '2025-03-31';
    CREATE DATABASE IF NOT EXISTS Library(...);
```


## References:
- [SQL Operators](https://www.w3schools.com/sql/sql_operators.asp)
- [SQL Operators](https://www.geeksforgeeks.org/sql/sql-operators/)
- [SQL - Operators ](https://www.tutorialspoint.com/sql/sql-operators.htm)