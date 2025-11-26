


### Part 2: Working with Multiple Tables and Data
**5. Sorting and Limiting Results**
*   `ORDER BY column [ASC | DESC]` (sorting by one or multiple columns)
*   `LIMIT count` (and `OFFSET` for pagination) - *Note: Syntax varies (e.g., `TOP` in SQL Server, `ROWNUM` in Oracle).*

**6. Aggregating Data**
* **Aggregate Functions:** 
  * `COUNT()`, 
  * `SUM()`, 
  * `AVG()`, 
  * `MIN()`, 
  * `MAX()`
* The `GROUP BY` clause for creating summary rows.
  * Grouping results using **GROUP BY**.
* The `HAVING` clause for filtering groups (vs. `WHERE` which filters rows *before* grouping).
  * Filtering groups using **HAVING** (important distinction from WHERE).

**7. Joins: Combining Data from Multiple Tables**
Joining Tables
* **The Concept of Keys:** Primary Key and Foreign Key
* Understanding the different types of joins:
* **INNER JOIN:** Returns records with matching values in both tables.
* **OUTER JOINs:**
    * `LEFT (OUTER) JOIN`: Returns all records from the left table and matched records from the right.
    * `RIGHT (OUTER) JOIN`: Returns all records from the right table and matched records from the left.
    * `FULL (OUTER) JOIN`: Returns all records when there is a match in either left or right table.
* **CROSS JOIN:** Cartesian product of both tables.
* **SELF JOIN:** Joining a table to itself.
* Writing concise **JOIN** syntax and understanding **ON** clauses.

[Image of the different SQL join types Venn diagram]

**8. Subqueries (Nested Queries)**
*   **Types based on Result:**
    *   **Scalar Subquery:** Returns a single value.
    *   **Row Subquery:** Returns a single row.
    *   **Column Subquery:** Returns a single column.
    *   **Table Subquery:** Returns a result set that can be treated as a table.
*   **Types based on Dependency:**
    *   **Correlated Subquery:** Depends on the outer query for its values.
    *   **Non-Correlated Subquery:** Can run independently of the outer query.
*   Using subqueries in `SELECT`, `FROM`, and `WHERE` clauses (especially with `IN`, `ANY`, `ALL`).

---
    * Using queries within a query (**Nested SELECTs**).
    * Types: Scalar, Multiple-Row, Correlated Subqueries.
    * Using subqueries with **IN**, **EXISTS**, **ANY**, and **ALL**.

### Part 4: Data Definition and Manipulation
**13. Modifying Data (DML)**
*   **Adding Data:** `INSERT INTO table VALUES (...)`
*   **Updating Data:** 
*   **Deleting Data:** 
*   **Upserting Data:** `INSERT ... ON DUPLICATE KEY UPDATE ...` (MySQL) or `MERGE` (SQL Server/Oracle).

### Part 5: Database Design & Administration


**17. Transactions & ACID Properties**
*   **What is a Transaction?** A single unit of work.
*   **ACID Properties:**
    *   **Atomicity:** All or nothing.
    *   **Consistency:** Brings database from one valid state to another.
    *   **Isolation:** Transactions are isolated from each other.
    *   **Durability:** Committed changes are permanent.
*   **Transaction Control:** `BEGIN TRANSACTION`, `COMMIT`, `ROLLBACK`.

**18. Stored Procedures, Functions, and Triggers (Procedural SQL)**
*   **Stored Procedures:** Reusable blocks of SQL code stored in the database.
*   **User-Defined Functions (UDFs):** Routines that return a value.
*   **Triggers:** Code that automatically runs in response to specific events (`INSERT`, `UPDATE`, `DELETE`) on a table.

### How to Structure Your Notes:
*   **Use Headers and Sub-headers** (like this outline).
*   **For each command/syntax:** Write the general syntax.
*   **Provide a clear, simple example** for every concept.
*   **Note the "Gotchas":** Common pitfalls, differences between SQL dialects (e.g., MySQL vs. PostgreSQL vs. SQL Server).
*   **Use Diagrams:** For Joins (Venn diagrams are popular), database schema, and relationships.
