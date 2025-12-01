---
layout: post
title: SQL Query Optimization
description: 
author: Dipak Pulami Magar
date :  2025-11-30 5:12:45 +0545
categories: sql
status: draft
---

SQL query optimization is the process of improving the performance of SQL queries to ensure they run efficiently, consume fewer resources, and retrieve data quickly. 

This is crucial for database systems, especially when dealing with large datasets or high concurrency.

## Key Techniques for SQL Query Optimization:
**1. Indexing:**  
Create appropriate indexes on columns frequently used in `WHERE` clauses, `JOIN` conditions, `ORDER BY`, and `GROUP BY` clauses. Indexes allow the database to quickly locate specific rows without scanning the entire table.

```sql
CREATE TABLE IF NOT EXISTS students(
    student_id INT,
    name VARCHAR(50), 
    gpa FLOAT,
    department VARCHAR(30)
);

INSERT INTO students (student_id, name, gpa, department) VALUES
(1, 'Richard', 2.5, 'CA'),
(2, 'Saurav', 3.1, 'Math'),
(3, 'Cristina', 3.4, 'Phyiscs'),
(4, 'David', 3.4, 'Biology'),
(5, 'Emma', 3.7, 'Chemistry'),
(6, 'Frank', 2.9, 'Math'),
(7, 'Grace', 3.6, 'Physics'),
(8, 'Henry', 3.2, 'CS'),
(9, 'Ivy', 3.8, 'Biology'),
(10, 'Jack', 2.7, 'Math'),
(11, 'Kathy', 3.9, 'Chemistry'),
(12, 'Leo', 3.1, 'Physics'),
(13, 'Mia', 3.5, 'CS'),
(14, 'Noah', 3.0, 'Biology'),
(15, 'Olivia', 3.6, 'Physics'),
(16, 'Paul', 2.8, 'Math'),
(17, 'Queenie', 3.7, 'Chemistry'),
(18, 'Ryan', 3.4, 'CS'),
(19, 'Sophia', 3.9, 'Biology'),
(20, 'Tom', 3.3, 'Physics'),
(21, 'Uma', 3.2, 'Chemistry'),
(22, 'Victor', 3.8, 'Math'),
(23, 'Wendy', 3.1, 'CS'),
(24, 'Xavier', 2.9, 'Biology'),
(25, 'Yara', 3.5, 'Physics'),
(26, 'Zack', 3.0, 'Chemistry'),
(27, 'Aaron', 3.7, 'Math'),
(28, 'Bella', 3.8, 'CS'),
(29, 'Carter', 2.8, 'Physics'),
(30, 'Diana', 3.4, 'Biology'),
(31, 'Ethan', 3.6, 'Chemistry'),
(32, 'Fiona', 3.2, 'Math'),
(33, 'George', 3.9, 'CS'),
(34, 'Hannah', 3.3, 'Physics'),
(35, 'Ian', 2.7, 'Biology'),
(36, 'Julia', 3.8, 'Chemistry'),
(37, 'Kyle', 3.5, 'Math'),
(38, 'Luna', 3.1, 'CS'),
(39, 'Mason', 3.4, 'Physics'),
(40, 'Nina', 3.0, 'Biology'),
(41, 'Owen', 3.7, 'Chemistry'),
(42, 'Piper', 3.6, 'Math'),
(43, 'Quinn', 3.9, 'Physics'),
(44, 'Ruth', 3.3, 'CS'),
(45, 'Sean', 2.9, 'Biology'),
(46, 'Tina', 3.8, 'Chemistry'),
(47, 'Umar', 3.2, 'Math'),
(48, 'Violet', 3.6, 'Physics'),
(49, 'Will', 3.5, 'CS'),
(50, 'Xena', 3.1, 'Biology'),
(51, 'Yusuf', 3.4, 'Chemistry'),
(52, 'Zoe', 3.7, 'Math'),
(53, 'Alex', 3.3, 'Physics'),
(54, 'Brianna', 3.2, 'Biology'),
(55, 'Caleb', 3.8, 'CS'),
(56, 'Daisy', 3.6, 'Chemistry'),
(57, 'Eli', 2.9, 'Math'),
(58, 'Faith', 3.5, 'Physics'),
(59, 'Gavin', 3.1, 'Biology'),
(60, 'Hailey', 3.9, 'CS'),
(61, 'Isaac', 3.4, 'Chemistry'),
(62, 'Jasmine', 3.7, 'Math'),
(63, 'Keegan', 3.3, 'Physics'),
(64, 'Lara', 3.0, 'Biology'),
(65, 'Marcus', 3.8, 'CS'),
(66, 'Nora', 3.6, 'Chemistry'),
(67, 'Omar', 2.8, 'Math'),
(68, 'Paula', 3.5, 'Physics'),
(69, 'Reese', 3.2, 'Biology'),
(70, 'Sam', 3.9, 'CS'),
(71, 'Talia', 3.4, 'Chemistry'),
(72, 'Uriah', 3.8, 'Math'),
(73, 'Vera', 3.1, 'Physics'),
(74, 'Wes', 3.3, 'Biology'),
(75, 'Ximena', 3.7, 'Chemistry'),
(76, 'Yohan', 3.6, 'Math'),
(77, 'Zara', 3.2, 'CS'),
(78, 'Aiden', 3.9, 'Physics'),
(79, 'Brittany', 3.4, 'Biology'),
(80, 'Cody', 3.5, 'Chemistry'),
(81, 'Denise', 3.1, 'Math'),
(82, 'Evan', 3.8, 'CS'),
(83, 'Felix', 3.6, 'Physics'),
(84, 'Gina', 2.9, 'Biology'),
(85, 'Harold', 3.7, 'Chemistry'),
(86, 'Irene', 3.5, 'Math'),
(87, 'Jonas', 3.4, 'CS'),
(88, 'Kara', 3.8, 'Physics'),
(89, 'Liam', 3.2, 'Biology'),
(90, 'Maria', 3.9, 'Chemistry'),
(91, 'Nolan', 3.6, 'Math'),
(92, 'Opal', 3.3, 'CS'),
(93, 'Preston', 2.7, 'Physics'),
(94, 'Riley', 3.1, 'Biology'),
(95, 'Stella', 3.8, 'Chemistry'),
(96, 'Trent', 3.5, 'Math'),
(97, 'Ulma', 3.4, 'CS'),
(98, 'Valerie', 3.9, 'Physics'),
(99, 'Wayne', 3.3, 'Biology'),
(100, 'Xander', 3.6, 'Chemistry'),
(101, 'Yvette', 3.2, 'Math'),
(102, 'Zion', 3.7, 'CS'),
(103, 'Amber', 3.5, 'Biology');
```


```sql
SELECT COUNT(*)
FROM students
WHERE department = 'Physics';
```

```
+----------+
| COUNT(*) |
+----------+
|       22 |
+----------+
1 row in set (0.140 sec)
```

```sql
CREATE INDEX idx_department ON students(department);

SELECT COUNT(*)
FROM students
WHERE department = 'Physics';
```

```
+----------+
| COUNT(*) |
+----------+
|       22 |
+----------+
1 row in set (0.005 sec)
```

**2. Select Specific Columns:**   
Instead of using `SELECT *`, specify only the columns required. This reduces the amount of data retrieved and transferred, improving performance.

```sql
-- selecting all data (once)
SELECT *
FROM students
```

Output:
```
+------------+---------+------+-------------+------+
| student_id | name    | age  | department  | gpa  |
+------------+---------+------+-------------+------+
|          1 | Alice   |   20 | ComputerSci |  3.8 |
|          2 | Bob     |   22 | Physics     |  3.2 |
|          3 | Charlie |   21 | Mathematics |  2.9 |
|          4 | Diana   |   23 | ComputerSci |  3.6 |
|          5 | Eva     |   20 | Physics     |  3.1 |
+------------+---------+------+-------------+------+
5 rows in set (0.311 sec)
```

```sql
-- Selecting required table fields
SELECT name, age, gpa
FROM students;
```

Output:
```
+---------+------+------+
| name    | age  | gpa  |
+---------+------+------+
| Alice   |   20 |  3.8 |
| Bob     |   22 |  3.2 |
| Charlie |   21 |  2.9 |
| Diana   |   23 |  3.6 |
| Eva     |   20 |  3.1 |
+---------+------+------+
5 rows in set (0.112 sec)
```

**3. Avoid Functions in Predicates:**   
Applying functions to columns in `WHERE` clauses can prevent the use of indexes. For example, instead of `WHERE YEAR(date_column) = 2024`, use `WHERE date_column BETWEEN '2024-01-01' AND '2024-12-31'`.

**Limit Data Retrieval:**   
Use `LIMIT` or `TOP` clauses to restrict the number of rows returned, especially when only a sample or a specific number of results are needed.

```sql
-- inefficient
SELECT *
FROM students;
```

```
+------------+---------+------+-------------+------+
| student_id | name    | age  | department  | gpa  |
+------------+---------+------+-------------+------+
|          1 | Alice   |   20 | ComputerSci |  3.8 |
|          2 | Bob     |   22 | Physics     |  3.2 |
|          3 | Charlie |   21 | Mathematics |  2.9 |
|          4 | Diana   |   23 | ComputerSci |  3.6 |
|          5 | Eva     |   20 | Physics     |  3.1 |
+------------+---------+------+-------------+------+
5 rows in set (0.153 sec)
```

```sql
SELECT *
FROM students21
LIMIT 3;
```

```
+------------+---------+------+-------------+------+
| student_id | name    | age  | department  | gpa  |
+------------+---------+------+-------------+------+
|          1 | Alice   |   20 | ComputerSci |  3.8 |
|          2 | Bob     |   22 | Physics     |  3.2 |
|          3 | Charlie |   21 | Mathematics |  2.9 |
+------------+---------+------+-------------+------+
3 rows in set (0.009 sec)
```

**Use `EXISTS()` instead of `COUNT()` for Existence Checks**:   
When simply checking for the existence of records, `EXISTS()` is generally more efficient than `COUNT()` as it stops scanning once a match is found.

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2)
);

INSERT INTO orders (order_id, customer_id, order_date, amount) VALUES
(1, 101, '2025-01-01', 250.00),
(2, 102, '2025-01-05', 150.00),
(3, 103, '2025-01-10', 300.00),
(4, 101, '2025-02-01', 400.00);
```

```sql
-- Check if customer_id = 101 has orders
SELECT COUNT(*) AS order_count
FROM orders
WHERE customer_id = 101;
```

```
+-------------+
| order_count |
+-------------+
|           2 |
+-------------+
1 row in set (0.115 sec)
```

```sql
-- Check if customer_id = 101 has any orders
SELECT EXISTS(
    SELECT 1
    FROM orders
    WHERE customer_id = 101
) AS customer_exists;
```
Output:

```
+-----------------+
| customer_exists |
+-----------------+
|               1 |
+-----------------+
1 row in set (0.006 sec)
```

**Optimize Joins:**    
  - Choose the correct join types (e.g., `INNER JOIN` when possible, over `OUTER JOIN` if not strictly necessary).
  - Ensure join conditions are indexed.
  - Consider the order of tables in joins, especially in complex queries, as the optimizer might benefit from a specific order.

**Use `WHERE` instead of `HAVING` for Filtering**:   
`WHERE` clauses filter rows before grouping, while `HAVING` filters after grouping. Filtering early with `WHERE` reduces the dataset processed by aggregation functions.

**Avoid Leading Wildcards in `LIKE`**:   
Using `LIKE '%pattern'` prevents index usage, forcing a full table scan. If possible, use `LIKE 'pattern%'`.

**Consider Stored Procedures:**   
For frequently executed and complex logic, encapsulating queries in stored procedures can improve performance through pre-compilation and reduced network traffic.

**Analyze Execution Plans:**   
Use the database's `EXPLAIN` or `ANALYZE` tools to understand how a query is being executed, identify bottlenecks, and refine optimization strategies.

**Use Appropriate Data Types:**   
Choosing the most efficient data types for columns can reduce storage space and improve query performance.

By applying these techniques, developers and database administrators can significantly enhance the efficiency and responsiveness of their SQL queries and overall database system.
