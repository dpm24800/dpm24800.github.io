---
layout: post
title:  "SQL – note plan"
author: Dipak Pulami Magar
date:   2025-12-20 10:12:45 +0545
categories: sql
status: draft
---



    * their importance for data integrity and relationships. 
#### **Relationships** between tables (
      * One-to-One, 
      * One-to-Many, 
      * Many-to-Many).


## 🔬 Advanced Querying and Functions

These topics move beyond simple data retrieval and manipulation.

* ### **Filtering and Pattern Matching**
    * Using **LIKE** with wildcards (%, \_) for string matching.
    * Using **IN** and **BETWEEN** operators.
    * Handling null values with **IS NULL** / **IS NOT NULL**.
  
### **Aggregate Functions**
  * Functions like **COUNT()**, **SUM()**, **AVG()**, **MIN()**, **MAX()**.
  *
  

* ### **Set Operations**
    * Combining result sets using **UNION** (removes duplicates) and **UNION ALL** (keeps duplicates).
    * **INTERSECT** and **EXCEPT** (or MINUS, depending on the RDBMS).


## 📈 Advanced Features and Optimization
For a complete understanding of real-world database usage, these topics are crucial.


**15. Indexes**
* **What is an index?** 
*   (Like a book index, speeds up data retrieval).
*   **When to use an index?** 
*   On columns frequently used in `WHERE`, `JOIN`, and `ORDER BY`.
*   **Trade-offs:** 
*   Speed vs. storage space and slower `INSERT`/`UPDATE`/`DELETE`.
*   **Types:**
*    Clustered vs. Non-Clustered Indexes.

  * Purpose and types of **Indexes** (Clustered vs. Non-Clustered).
    * How indexes improve query performance and when they should be used.

---

**16. Views**
*   **What is a view?** 
*   A virtual table based on the result of a SQL query.
*   **Creating a view:** 
    * `CREATE VIEW view_name AS ...`
    * Creating and using **VIEWs** (virtual tables) for security and simplification.
*   **Benefits:** Security, simplicity, and logical data abstraction.

* ### **Window Functions (Analytic Functions)**
    * Functions like **ROW\_NUMBER()**, **RANK()**, **DENSE\_RANK()**.
    * Using the **OVER** clause with **PARTITION BY** and **ORDER BY**.
    * Advanced aggregates (e.g., moving averages).
* ### **Stored Procedures and Functions**
    * The difference between Stored Procedures and User-Defined Functions.
    * Benefits (performance, security, reusability).
    * Basic syntax for creation and execution.

### Part 5: Database Design & Administration
### **Normalization**
* Understanding the goal of normalization (reducing data redundancy and improving data integrity).
* **Purpose:** To reduce data redundancy and improve data integrity.
* * Defining the first three normal forms (**1NF, 2NF, 3NF**).
* **1NF (First Normal Form):** Atomic values, no repeating groups.
* **2NF (Second Normal Form):** In 1NF + no partial dependency (all non-key attributes depend on the whole primary key).
* **3NF (Third Normal Form):** In 2NF + no transitive dependency (non-key attributes depend only on the key).
* **Denormalization** (when and why to use it).




### **Query Optimization**
    * Basic tips for writing efficient queries (e.g., avoiding `SELECT *`, optimizing `WHERE` clauses).
    * Understanding the **Query Execution Plan** (conceptual).



### Part 3: Advanced Querying & Optimization
**9. Common Table Expressions (CTEs)**
*   Syntax: `WITH cte_name AS ( ... )`
*   Using CTEs for better readability and organization of complex queries.
*   **Recursive CTEs:** For hierarchical data (e.g., organizational charts).

**10. Set Operations**
*   `UNION` and `UNION ALL` (combines result sets, removes duplicates vs. keeps all).
*   `INTERSECT` (returns common records).
*   `EXCEPT` or `MINUS` (returns records from the first query that are not in the second).

**11. Window Functions**
*   The `OVER()` clause.
*   `PARTITION BY` for dividing the data into windows.
*   `ORDER BY` within the window for ordering.
*   **Common Window Functions:**
    *   Ranking: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`
    *   Analytical: `LAG()`, `LEAD()`, `FIRST_VALUE()`, `LAST_VALUE()`
    *   Aggregate functions used as window functions: `SUM() OVER(...)`
    *   