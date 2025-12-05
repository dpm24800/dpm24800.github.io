---
layout: post
title: Common Table Expressions (CTE) – SQL
description: Define temporary, named result sets for cleaner queries
thumbnail: ../../../../assets/images/sql/common-table-expressions.png
author: Dipak Pulami Magar
date :  2025-12-05 14:12:45 +0545
categories: sql
status: draft
---

**Common Table Expressions (CTEs)** is a powerful technique for simplifying complex queries, improving readability, and enabling recursive logic. CTEs define a temporary, named result set that exists only for the duration of a single query.

## Syntax
A CTE is always introduced by the `WITH` keyword, followed by the CTE's name, the `AS` keyword, and the defining `SELECT` statement enclosed in parentheses.

### Single CTE Syntax
The most basic structure involves a single CTE followed by the main query that references it:

```sql
WITH cte_name (column1, column2, ...)  -- Column list is optional
AS (
    -- The defining SELECT statement (the temporary result set)
    SELECT col_a, col_b
    FROM source_table
    WHERE condition
)
-- The main query that uses the CTE
SELECT column1, column2
FROM cte_name
WHERE another_condition;
```

### Multiple CTE Syntax
You can chain multiple CTEs together. Subsequent CTEs can refer to previously defined CTEs within the same WITH clause. The CTEs are separated by commas.

```sql
WITH first_cte AS (
    -- Defines the first result set
    SELECT ...
),
second_cte AS (
    -- Defines the second result set, referencing the first_cte
    SELECT *
    FROM first_cte
    WHERE ...
),
third_cte (c3_col1, c3_col2) AS (
    -- Defines the third result set
    SELECT ...
)
-- Main query referencing any of the defined CTEs
SELECT *
FROM second_cte, third_cte
WHERE ...;
```

-----

## Practical Examples

Let's use a sample table called `Employees` for these examples:

| EmployeeID | Name | DepartmentID | Salary | ManagerID |
| :---:       | :---: | :---: | :---: | :---: |
| 101 | Alice | 1 | 70000 | 104 |
| 102 | Bob | 2 | 65000 | 104 |
| 103 | Charlie | 1 | 80000 | 105 |
| 104 | David | 3 | 95000 | NULL |
| 105 | Eve | 2 | 75000 | 104 |
| 106 | Fiona | 3 | 110000 | 105 |

### 1. Simplifying Subqueries with a Single CTE
Instead of using a non-reusable subquery in the FROM clause, a CTE provides a clear name for the logic.

**Goal:** Find all employees whose salary is above the average salary for their respective department.

```sql
WITH DepartmentAverage AS (
    -- CTE to calculate the average salary for each department
    SELECT
        DepartmentID,
        AVG(Salary) AS AvgDepartmentSalary
    FROM
        Employees
    GROUP BY
        DepartmentID
)
SELECT
    e.Name,
    e.Salary,
    d.AvgDepartmentSalary
FROM
    Employees e
JOIN
    DepartmentAverage d ON e.DepartmentID = d.DepartmentID
WHERE
    e.Salary > d.AvgDepartmentSalary;
```

  * **Without CTE:** This would require calculating the `DepartmentAverage` in a subquery and joining to it, or using an expensive correlated subquery in the WHERE clause. The CTE makes the logic easy to follow: first, get the average, then use it to filter the employees.

-----

### 2\. Chaining CTEs for Step-by-Step Logic

CTEs are excellent for multi-step processing where the output of one step is the input for the next.

**Goal:** First, get the list of high-earning managers (salary $\ge$ 90000), and then find all employees who report to those specific high-earning managers.

```sql
WITH HighEarningManagers AS (
    -- Step 1: Identify managers earning $90,000 or more
    SELECT
        EmployeeID AS ManagerID,
        Name AS ManagerName
    FROM
        Employees
    WHERE
        Salary >= 90000
),
EmployeeDetails AS (
    -- Step 2: Join HighEarningManagers with the Employees table
    -- to find their direct reports.
    SELECT
        e.Name AS EmployeeName,
        e.Salary AS EmployeeSalary,
        m.ManagerName
    FROM
        Employees e
    JOIN
        HighEarningManagers m ON e.ManagerID = m.ManagerID
)
-- Final Query: Select the required information
SELECT
    EmployeeName,
    EmployeeSalary,
    ManagerName
FROM
    EmployeeDetails
ORDER BY
    ManagerName, EmployeeSalary DESC;
```

  * **Clarity:** The chained CTEs clearly delineate the two logical steps: finding the managers, then finding their reports.

-----

### 3\. Recursive CTEs for Hierarchical Data

The WITH clause is **mandatory** for **recursive queries** using the WITH RECURSIVE keyword. This is typically used to traverse organizational charts, bill of materials, or network paths.

**Goal:** Trace the full management hierarchy, starting from an employee with EmployeeID = 101 up to the top-level manager (ManagerID is NULL).

```sql
WITH RECURSIVE OrganizationHierarchy AS (
    -- Anchor Member (The initial starting point for the recursion)
    SELECT
        EmployeeID,
        Name,
        ManagerID,
        1 AS Level
    FROM
        Employees
    WHERE
        EmployeeID = 101

    UNION ALL

    -- Recursive Member (Iterates by joining the CTE to the Employees table)
    SELECT
        e.EmployeeID,
        e.Name,
        e.ManagerID,
        o.Level + 1 AS Level
    FROM
        Employees e
    JOIN
        OrganizationHierarchy o ON e.EmployeeID = o.ManagerID
)
-- Main query to display the result set
SELECT
    EmployeeID,
    Name,
    ManagerID,
    Level
FROM
    OrganizationHierarchy;
```

  * **Anchor Member:** The first SELECT statement provides the initial row(s) for the result set and is executed once.
  * **`UNION ALL`:** The operator that connects the anchor and recursive members.
  * **Recursive Member:** The second SELECT statement, which references the CTE itself (OrganizationHierarchy), is repeatedly executed until it returns an empty result set (i.e., when ManagerID is NULL).
  * **Note:** The exact syntax for recursive CTEs can vary slightly between database systems (e.g., PostgreSQL, MySQL, SQL Server).

-----

## Key Rules and Considerations
* **Scope**: A CTE is temporary and can **only** be used within the single SELECT, INSERT, UPDATE, DELETE, or MERGE statement immediately following the WITH clause. It cannot be referenced by other, separate queries.
* **No Indexing**: Since a CTE is not physically stored, you cannot create indexes on it.
* **Performance vs. Readability**: While CTEs are highly valuable for readability and complexity management, they **do not necessarily improve query performance** over an equivalent subquery. In most modern SQL systems, the query optimizer treats CTEs and subqueries similarly. If a CTE is referenced multiple times, however, some database systems may re-execute the CTE's defining query for each reference (unless materialized or optimized otherwise), which *could* hurt performance.
* **Data Modification**: You can use a CTE to define the rows to be affected by an INSERT, UPDATE, or DELETE statement, making complex modifications clearer.

<!-- end list -->

```sql
-- Example: Delete employees who report to a specific manager
WITH EmployeesToDelete AS (
    SELECT
        EmployeeID
    FROM
        Employees
    WHERE
        ManagerID = 104
)
DELETE FROM Employees
WHERE EmployeeID IN (SELECT EmployeeID FROM EmployeesToDelete);
```


## Exercises
**1**: 
```
+------------+--------------------------+-------------+---------------------+------------+----------------+------------+
| product_id | product_name             | category_id | parent_category_id  | unit_price | units_in_stock | units_sold |
+------------+--------------------------+-------------+---------------------+------------+----------------+------------+
|        101 | laptop_x1                |           1 | NULL                |    1200.00 |             50 |         20 |
|        102 | gaming_mouse             |           2 |                   1 |      75.00 |            150 |         80 |
|        103 | mechanical_keyboard      |           2 |                   1 |     120.00 |             90 |         45 |
|        104 | 4k_monitor               |           3 | NULL                |     450.00 |             30 |         15 |
|        105 | usb_c_hub                |           4 |                   3 |      40.00 |            200 |        110 |
|        106 | software_license_pro     |           5 | NULL                |     300.00 |              5 |         20 |
|        107 | office_chair_ergonomic   |           6 | NULL                |     350.00 |             40 |         10 |
|        108 | desk_mat_large           |           6 |                 107 |      25.00 |            180 |         50 |
|        109 | webcam_hd                |           2 |                   1 |      55.00 |            110 |         30 |
|        110 | portable_ssd_1tb         |           4 |                   3 |     150.00 |             70 |         35 |
+------------+--------------------------+-------------+---------------------+------------+----------------+------------+
```

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INT,
    parent_category_id INT,
    unit_price DECIMAL(10, 2),
    units_in_stock INT,
    units_sold INT
);

INSERT INTO products (product_id, product_name, category_id, parent_category_id, unit_price, units_in_stock, units_sold) VALUES
(101, 'laptop_x1', 1, NULL, 1200.00, 50, 20),
(102, 'gaming_mouse', 2, 1, 75.00, 150, 80),
(103, 'mechanical_keyboard', 2, 1, 120.00, 90, 45),
(104, '4k_monitor', 3, NULL, 450.00, 30, 15),
(105, 'usb_c_hub', 4, 3, 40.00, 200, 110),
(106, 'software_license_pro', 5, NULL, 300.00, 5, 20),
(107, 'office_chair_ergonomic', 6, NULL, 350.00, 40, 10),
(108, 'desk_mat_large', 6, 107, 25.00, 180, 50),
(109, 'webcam_hd', 2, 1, 55.00, 110, 30),
(110, 'portable_ssd_1tb', 4, 3, 150.00, 70, 35);
```

```sql
-- Find the product_name and unit_price of all products whose price is greater than the overall average unit price of all products.

-- using sub-query
SELECT product_name, unit_price
FROM products
WHERE unit_price > (
    SELECT AVG(unit_price) 
    FROM products
);
-- using CTE
WITH avg_unit_price AS (
    SELECT AVG(unit_price) AS avg_unit_price
    FROM products
)

SELECT p.product_name, p.unit_price
FROM products p
CROSS JOIN avg_unit_price a
WHERE p.unit_price > a.avg_unit_price;

-- by category
WITH avg_unit_price AS(
	SELECT category_id, AVG(unit_price) avg_unit_price
	FROM products
	GROUP BY category_id
)
SELECT p.product_name, p.unit_price, a.avg_unit_price
FROM products p
JOIN avg_unit_price a ON p.category_id = a.category_id
WHERE p.unit_price > a.avg_unit_price;

```