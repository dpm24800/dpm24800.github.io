---
layout: post
title: Inner Join
description: 
author: Dipak Pulami Magar
date :  2025-11-30 5:12:45 +0545
categories: sql
status: draft
---

This is the most common type of join.  
It returns only the rows that have **matching values** in both tables.

**Syntax:**
```sql
SELECT columns
FROM TableA
INNER JOIN TableB ON TableA.key = TableB.key;
```

## Examples

### **1. Orders and Customers**  
*Retrieve orders that have a matching customer.*

```
Table: orders
+----------+------------+-------------+--------+
| order_id | order_date | customer_id | amount |
+----------+------------+-------------+--------+
|      101 | 2024-01-10 |           1 | 250.00 |
|      102 | 2024-01-11 |           2 | 450.50 |
|      103 | 2024-01-12 |           1 | 120.75 |
|      104 | 2024-01-15 |           3 | 999.99 |
|      105 | 2024-02-01 |           4 | 540.00 |
|      106 | 2024-02-10 |           2 | 300.00 |
|      107 | 2024-03-05 |           5 | 220.40 |
|      108 | 2024-03-18 |           3 | 780.00 |
|      109 | 2024-03-22 |           5 | 150.00 |
|      110 | 2024-04-02 |           1 | 500.00 |
+----------+------------+-------------+--------+

Table: customers
+-------------+---------------+---------------------+------------+
| customer_id | customer_name | email               | phone      |
+-------------+---------------+---------------------+------------+
|           1 | Alice Johnson | alice@example.com   | 9876543210 |
|           2 | Bob Smith     | bob@example.com     | 9812314567 |
|           3 | Charlie Brown | charlie@example.com | 9845671234 |
|           4 | Diana Miller  | diana@example.com   | 9823456789 |
|           5 | Edward Wilson | edward@example.com  | 9801234567 |
+-------------+---------------+---------------------+------------+
```

```sql
SELECT o.order_id, o.order_date, c.customer_name
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;
```

Output:
```
+----------+------------+---------------+
| order_id | order_date | customer_name |
+----------+------------+---------------+
|      101 | 2024-01-10 | Alice Johnson |
|      103 | 2024-01-12 | Alice Johnson |
|      110 | 2024-04-02 | Alice Johnson |
|      102 | 2024-01-11 | Bob Smith     |
|      106 | 2024-02-10 | Bob Smith     |
|      104 | 2024-01-15 | Charlie Brown |
|      108 | 2024-03-18 | Charlie Brown |
|      105 | 2024-02-01 | Diana Miller  |
|      107 | 2024-03-05 | Edward Wilson |
|      109 | 2024-03-22 | Edward Wilson |
+----------+------------+---------------+
```

#### **Tabele with data**  
`Table`: customers
```sql
-- Table: customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20)
);

INSERT INTO customers (customer_id, customer_name, email, phone) VALUES
(1, 'Alice Johnson', 'alice@example.com', '9876543210'),
(2, 'Bob Smith', 'bob@example.com', '9812314567'),
(3, 'Charlie Brown', 'charlie@example.com', '9845671234'),
(4, 'Diana Miller', 'diana@example.com', '9823456789'),
(5, 'Edward Wilson', 'edward@example.com', '9801234567');
```

```sql
-- Table: orders
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders (order_id, order_date, customer_id, amount) VALUES
(101, '2024-01-10', 1, 250.00),
(102, '2024-01-11', 2, 450.50),
(103, '2024-01-12', 1, 120.75),
(104, '2024-01-15', 3, 999.99),
(105, '2024-02-01', 4, 540.00),
(106, '2024-02-10', 2, 300.00),
(107, '2024-03-05', 5, 220.40),
(108, '2024-03-18', 3, 780.00),
(109, '2024-03-22', 5, 150.00),
(110, '2024-04-02', 1, 500.00);
```

**Note**: doesn't matter the order of SELECT FROM table_name and INNER JOIN table_name.

---

### **2. Students and Courses**  
*Retrieve students who are enrolled in courses.*

```
Table: students
+------------+---------------+---------------------+
| student_id | student_name  | email               |
+------------+---------------+---------------------+
|          1 | Alice Johnson | alice@example.com   |
|          2 | Bob Smith     | bob@example.com     |
|          3 | Charlie Brown | charlie@example.com |
|          4 | Diana Miller  | diana@example.com   |
|          5 | Edward Wilson | edward@example.com  |
+------------+---------------+---------------------+

Table: courses
+-----------+-------------------+---------+
| course_id | course_name       | credits |
+-----------+-------------------+---------+
|       101 | Database Systems  |       3 |
|       102 | Operating Systems |       4 |
|       103 | Computer Networks |       3 |
|       104 | Machine Learning  |       4 |
|       105 | Data Structures   |       3 |
+-----------+-------------------+---------+

Table: enrollments
+---------------+------------+-----------+------------+
| enrollment_id | student_id | course_id | semester   |
+---------------+------------+-----------+------------+
|             1 |          1 |       101 | Fall2024   |
|             2 |          1 |       104 | Fall2024   |
|             3 |          2 |       105 | Spring2024 |
|             4 |          2 |       103 | Fall2024   |
|             5 |          3 |       102 | Fall2024   |
|             6 |          3 |       105 | Spring2024 |
|             7 |          4 |       101 | Spring2024 |
|             8 |          4 |       103 | Fall2024   |
|             9 |          5 |       104 | Spring2024 |
|            10 |          5 |       102 | Fall2024   |
+---------------+------------+-----------+------------+
```

```sql
SELECT s.student_id, s.student_name, c.course_name
FROM students s
INNER JOIN enrollments e
    ON s.student_id = e.student_id
INNER JOIN courses c
    ON e.course_id = c.course_id;
```

Output:

```
+------------+---------------+-------------------+
| student_id | student_name  | course_name       |
+------------+---------------+-------------------+
|          1 | Alice Johnson | Database Systems  |
|          1 | Alice Johnson | Machine Learning  |
|          2 | Bob Smith     | Data Structures   |
|          2 | Bob Smith     | Computer Networks |
|          3 | Charlie Brown | Operating Systems |
|          3 | Charlie Brown | Data Structures   |
|          4 | Diana Miller  | Database Systems  |
|          4 | Diana Miller  | Computer Networks |
|          5 | Edward Wilson | Machine Learning  |
|          5 | Edward Wilson | Operating Systems |
+------------+---------------+-------------------+
```

```sql
-- Table: students
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO students (student_id, student_name, email) VALUES
(1, 'Alice Johnson', 'alice@example.com'),
(2, 'Bob Smith', 'bob@example.com'),
(3, 'Charlie Brown', 'charlie@example.com'),
(4, 'Diana Miller', 'diana@example.com'),
(5, 'Edward Wilson', 'edward@example.com');
```

```sql
-- Table: courses
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT
);

INSERT INTO courses (course_id, course_name, credits) VALUES
(101, 'Database Systems', 3),
(102, 'Operating Systems', 4),
(103, 'Computer Networks', 3),
(104, 'Machine Learning', 4),
(105, 'Data Structures', 3);
```

```sql
-- -- Table: enrollments
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    semester VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO enrollments (enrollment_id, student_id, course_id, semester) VALUES
(1, 1, 101, 'Fall2024'),
(2, 1, 104, 'Fall2024'),
(3, 2, 105, 'Spring2024'),
(4, 2, 103, 'Fall2024'),
(5, 3, 102, 'Fall2024'),
(6, 3, 105, 'Spring2024'),
(7, 4, 101, 'Spring2024'),
(8, 4, 103, 'Fall2024'),
(9, 5, 104, 'Spring2024'),
(10, 5, 102, 'Fall2024');
```

---

### **3. Employees and Departments**  
*Retrieve employees that belong to a valid department.*

```
fsdfsdf
```


```sql
SELECT e.employee_id, e.employee_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;
```

#### fsdf
```sql
-- Table: departments
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

INSERT INTO departments (department_id, department_name) VALUES
(1, 'Human Resources'),
(2, 'Finance'),
(3, 'Engineering'),
(4, 'Marketing'),
(5, 'Sales');
```

```sql
-- Table: departments
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    email VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO employees (employee_id, employee_name, email, department_id) VALUES
(101, 'Alice Johnson', 'alice@example.com', 1),
(102, 'Bob Smith', 'bob@example.com', 2),
(103, 'Charlie Brown', 'charlie@example.com', 3),
(104, 'Diana Miller', 'diana@example.com', 4),
(105, 'Edward Wilson', 'edward@example.com', 5),
(106, 'Fiona Davis', 'fiona@example.com', 3),
(107, 'George Clark', 'george@example.com', 2),
(108, 'Hannah Lee', 'hannah@example.com', 1),
(109, 'Ian Scott', 'ian@example.com', 4),
(110, 'Jane Adams', 'jane@example.com', 5);
```
---

### **4. Products and Sales**  
*Retrieve products that have at least one sale.*

```sql
SELECT p.product_id, p.product_name, s.sale_date, s.quantity
FROM products p
INNER JOIN sales s ON p.product_id = s.product_id;
```

---

### **5. Blog Posts and Authors**  
*Retrieve posts that have an associated author.*

```sql
SELECT p.post_id, p.title, a.author_name
FROM posts p
INNER JOIN authors a ON p.author_id = a.author_id;
```