---
layout: post
title: Table & Columns Operations – SQL
thumbnail: ../../../../assets/images/sql/table-operations.png
author: Dipak Pulami Magar
date :  2025-11-24 14:12:45 +0545
categories: sql
status: draft
---

# A. Table Operations
## 1. Creating a table
To create a new table, `CREATE TABLE` command is used thus:  

**Syntax**:
```sql
-- Attempts to create the table; throws an error if it already exists.
CREATE TABLE IF NOT EXISTS table_name(
    column1 datatype (constraint1 constraint2, constraintN),
    column2 datatype,
    .......
    filedN datatype
); 
```

Example:
```sql
-- Safely creates the table only if it doesn’t already exist, preventing errors.
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

<!-- <center>* * *</center> -->

## 2. Renaming a table
To rename a table, `RENAME TO` keyword is used along with `ALTER TABLE`, thus:

**Syntax**:
```sql
-- Renaming a table name
ALTER TABLE table_name
RENAME TO new_name;
```

Example:
```sql
ALTER TABLE student
RENAME TO students;
```
## 3. Truncating/emptying a table
To empty a table, `TRUNCATE` keyword is used thus:

**Syntax**:
```sql
-- Emptying a table
TRUNCATE TABLE table_name;
```

Examples:
```sql
-- Emptying a table
TRUNCATE TABLE orders;
```

## 4. Dropping/deleting a table
To drop/remove a existing table, `DROP` keyword is used thus:  

**Syntax**:
```sql
-- Removing a table
DROP TABLE table_name; -- Raises error if the table doesn't exist
DROP TABLE IF EXISTS table_name;
```
Examples:
```sql
DROP TABLE orders;
DROP TABLE IF EXISTS customers;
```

**Alert**: Truncating or dropping a table is serious business so confirm whether you're really doing.

---

# B. Column Operations
## 1. Adding a new column
To add a new column, `ADD COLUMN` keyword is used thus,

**Syntax**: 
```sql
-- Adding a new column
ALTER TABLE table_name
ADD COLUMN column_name datatype constraints;
```

Examples:
```sql
-- Adding a new column
ALTER TABLE orders
ADD COLUMN amount FLOAT;
```

## 2. Changing data type & constraints of a column
To change datatype and constraint of a column once created, `MODIFY` keyword is used along with `ALTER TABLE` thus,

```sql
-- Changing Data Types & Constraints
ALTER TABLE table_name
MODIFY column_name datatype constraints;
```

Examples:
```sql
-- Changing Data Types & Constraints
ALTER TABLE orders
MODIFY amount FLOAT NOT NULL;
```

## 3. Changing a column: (name, datatypes and constraints)
To change name (rename), datatype and constraints of a column once created, `CHANGE COLUMN` keyword is used along with `ALTER TABLE` thus,

**Syntax**:
```sql
ALTER TABLE table_name
CHANGE COLUMN column_name (new)column_name datatype constraints;
```

Exampless:
```sql
ALTER TABLE library
CHANGE COLUMN library_id library_id INT NOT NULL AUTO_INCREMENT;
```

```sql
ALTER TABLE customers
CHANGE COLUMN dist district VARCHAR(50) NULL DEFAULT NULL; -- name changed here
```

## 4. Removing an existing column
To remove(drop) a column, `DROP COLUMN` keyword is used thus,

**Syntax**:
```sql
-- Removing a column
ALTER TABLE table_name
DROP COLUMN column_name;
```

Example:
```sql
-- Removing a column
ALTER TABLE orders
DROP COLUMN quantity;
```

---

# C. Row Operations
## 1. Inserting a row
To insert data into a row of a table, `INSERT INTO` keyword is used thus,

**Syntax**:
```sql
INSERT INTO table_name(column1, column2, column....) VALUES
(value, value, valueN....),
(value, value, valueN....),
(value, value, valueN....),
(value, value, valueN....);
```

Example:
```sql
INSERT INTO orders (order_id, order_date, customer_id, amount) VALUES
(101, '2024-01-10', 1, 250.00),
(102, '2024-01-11', 2, 450.50),
(103, '2024-01-12', 1, 120.75),
(104, '2024-01-15', 3, 999.99),
(105, '2024-02-01', 4, 540.00),
(106, '2024-02-10', 2, 300.00);
```

## 2. Changing/updating the record
To change/update the table record, `UPDATE`, `SET` and `WHERE` keywords are used thus,

**Syntax**
```sql
UPDATE table_name
SET column_name = value
WHERE (identifying/filtering)column = value;
```

**Note**:
- Safe updates mode normally prevents `UPDATE` or `DELETE` statements without a `WHERE` clause using a key column or a LIMIT. After disabling it, you can run updates/deletes that might otherwise be blocked.
- Temporarily bypass MySQL’s safe update restriction thus,

```sql
SET SQL_SAFE_UPDATES = 0;  -- disables safe updates
```

Examples:
```sql
UPDATE students
SET gpa = 3.5
WHERE name = 'Bob';
```

```sql
-- If you omit the WHERE clause, all rows will be updated, which may not be intended.
-- Use SELECT first to preview which rows will be updated.
UPDATE employees
SET bonus = salary * 0.1
WHERE served_years >= 5;
```

## 3. Deleting a row
To delete a row,` DELETE FROM` keyword is used thus:

**Syntax**
```sql
DELETE FROM table_name
WHERE column conditions;
```

Examples:
```sql
DELETE FROM enrollments
WHERE grade = 'C+';
```

```sql
DELETE FROM users
WHERE status = 'inactive';
```

<center> * * * </center>