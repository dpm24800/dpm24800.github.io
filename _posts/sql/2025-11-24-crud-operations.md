---
layout: post
title: CRUD Operations – SQL
description: Create, Read, Update, Delete Operations
author: Dipak Pulami Magar
date :  2025-11-24 20:12:45 +0545
categories: sql
status: draft
---

**CRUD** (short for **C**reate, **R**ead, **U**pdate, and **D**elete) operations are the four fundamental actions performed on data in a relational database using **SQL**.

Here are the standard SQL commands for each operation, assuming you have a table named `Employees` with columns `EmployeeID`, `Name`, and `Department`.

## 1. Inserting Records (C-reate Operation)
The `INSERT INTO` command is used to add new rows (records) to a table.

**Syntax:** 
```sql
INSERT INTO table_name (column1, column2, ...) 
VALUES (value1, value2, ...);
```

**Example**:
```sql
INSERT INTO Employees (EmployeeID, Name, Department)
VALUES (101, 'Alice Smith', 'Sales');
```

## 2. Selecting/Retrieving Records (R-ead Operation)
The `SELECT` command is used to retrieve data from a table or a set of tables. This is the most frequently used command.

**Syntax:** 
```sql
SELECT column1, column2, ... FROM table_name;
SELECT column1, column2, ... FROM table_name WHERE condition;
```
The `WHERE` clause is optional but crucial for filtering results.

**Example**:
```sql
-- Retrieve all columns and all rows
SELECT *
FROM Employees;
```

```sql
-- Retrieve specific columns for employees in the 'Sales' department
SELECT Name, EmployeeID
FROM Employees
WHERE Department = 'Sales';
```

## 3. Updating Records (U-pdate Operation)
The `UPDATE` command is used to modify existing data in one or more rows of a table.  
**Crucial Note:** Always use the **`WHERE` clause** with `UPDATE`. If you omit it, *all* rows in the table will be updated.

**Syntax:** 
```sql
UPDATE table_name 
SET column1 = new_value1, column2 = new_value2, ... 
WHERE condition;
```

**Example**:
```sql
-- Change the department of the employee with `EmployeeID = 101`
UPDATE Employees
SET Department = 'Marketing'
WHERE EmployeeID = 101;
```

## 4. Deleting Records (D-elete Operation)
The `DELETE FROM` command is used to remove one or more rows from a table.  
**Crucial Note:** Similar to `UPDATE`, always use the **`WHERE` clause** with `DELETE FROM`. If you omit it, *all* rows in the table will be deleted.

**Syntax:** 
```sql
DELETE FROM table_name WHERE condition;
```

**Example**:
```sql
-- remove the employee with `EmployeeID = 101`
DELETE FROM Employees
WHERE EmployeeID = 101;
```


