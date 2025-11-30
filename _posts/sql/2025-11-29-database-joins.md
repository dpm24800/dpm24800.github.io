---
layout: post
title: Database Joins
author: Reshika Garanja Magar
date :  2025-11-29 5:12:45 +0545
categories: sql
status: draft
---

A database join is a fundamental operation in relational database management systems (RDBMS) that combines rows from two or more tables based on a related column between them. This related column is typically a primary key in one table and a foreign key in another, establishing a logical link between the data. 

Joins are essential for retrieving data that is distributed across multiple tables and presenting it as a single, unified result set.

There are several types of SQL joins, each with a distinct behavior:

- **INNER JOIN**: Returns only the rows where there is a match in both tables based on the specified join condition. Rows without a match in either table are excluded.

```sql
    SELECT *
    FROM TableA
    INNER JOIN TableB ON TableA.common_column = TableB.common_column;
```

- **LEFT (OUTER) JOIN**: Returns all rows from the left table and the matching rows from the right table. If there's no match in the right table, `NULL` values are returned for the right table's columns.

```sql
    SELECT *
    FROM TableA
    LEFT JOIN TableB ON TableA.common_column = TableB.common_column;
```

- **RIGHT (OUTER) JOIN**: Returns all rows from the right table and the matching rows from the left table. If there's no match in the left table, `NULL` values are returned for the left table's columns.

```sql
    SELECT *
    FROM TableA
    RIGHT JOIN TableB ON TableA.common_column = TableB.common_column;
```

- **FULL (OUTER) JOIN**: Returns all rows when there is a match in one of the tables. If there's no match in either table, `NULL` values are returned for the non-matching table's columns.

```sql
    SELECT *
    FROM TableA
    FULL JOIN TableB ON TableA.common_column = TableB.common_column;
```

- **CROSS JOIN**: Produces a Cartesian product of the two tables, meaning every row from the first table is combined with every row from the second table. This type of join does not require a join condition.

```sql
    SELECT *
    FROM TableA
    CROSS JOIN TableB;
```

Joins are crucial for tasks such as retrieving customer details along with their orders, combining product information with inventory levels, or generating reports that require data from various related entities within a database.