## **1. Introduction to Databases & SQL**
* **What is Data?**
* What is a Database?
  * Definition, purpose (persistent storage).
* Types of Databases (Relational vs NoSQL)
* What is a Relational Database Management System (RDBMS)?
* The concept of tables, rows, and columns.
* Popular RDBMS: MySQL, PostgreSQL, Oracle, SQL Server, SQLite

* What is SQL? (Declarative language)
* Structured Query Language - the standard language for communicating with relational databases.
* SQL vs NoSQL
* ACID Properties (Atomicity, Consistency, Isolation, Durability)
* OLTP vs OLAP

## **2. SQL Basics**
* SQL Syntax Rules
* Case Sensitivity
* Statements vs Clauses
* Keywords & Identifiers
* Database Objects (Tables, Views, Indexes, Procedures, Functions)

## **3. Data Types**
* **Numeric**: 
  * `INT`
  * `FLOAT`
  * `DECIMAL(p,s)`
  * `NUMERIC`
* **Character/Strings**: 
  * `CHAR(n)`, 
  * `VARCHAR(n)`, 
  * `TEXT`
* **Date/Time**: 
  * `DATE`, 
  * `TIME`, 
  * `DATETIME`, 
  * `TIMESTAMP`
* Boolean
* Binary types (BLOB): Binary Large Object
* JSON / XML (modern RDBMS support)
* Distinctions between different database vendors' data types (e.g., MySQL vs. PostgreSQL).

## **4. Table Operations**

### **Creating Tables**
* CREATE TABLE syntax
* Column constraints (NOT NULL, UNIQUE, DEFAULT)
* Primary Key
* Composite Primary Key
* Foreign Key
* Check Constraints
* Auto Increment / Identity columns

### **Altering Tables**
* ALTER TABLE ADD / DROP / MODIFY COLUMN
* Adding constraints
* Dropping constraints

### **Deleting Tables**
* DROP TABLE
* TRUNCATE TABLE

## **5. CRUD Operations (Most Used in Real Projects)**

### **INSERT**
* Insert single row
* Insert multiple rows
* Insert using SELECT

### **SELECT**

* SELECT syntax
* Selecting specific columns
* DISTINCT
* WHERE clause
* ORDER BY
* LIMIT / TOP / FETCH
* BETWEEN
* LIKE
* IN / NOT IN
* NULL handling (IS NULL / IS NOT NULL)

### **UPDATE**
* Updating specific rows
* Updating using JOIN

### **DELETE**
* Delete specific rows
* Delete with WHERE
* Delete with JOIN

## **6. SQL Functions**

### **Aggregate Functions**
* COUNT()
* SUM()
* AVG()
* MIN()
* MAX()

### **String Functions**
* CONCAT
* SUBSTRING
* LENGTH
* UPPER / LOWER
* TRIM / LTRIM / RTRIM
* REPLACE

### **Number Functions**
* ROUND
* CEIL / FLOOR
* ABS

### **Date Functions**
* NOW()
* DAY(), MONTH(), YEAR()
* DATE_ADD, DATE_SUB
* DATEDIFF

### **Conditional Functions**
* COALESCE
* NULLIF
* CASE WHEN … THEN …

## **7. Joins (Extremely Important)**
* What is a Join?
* **Types of Joins**
  * INNER JOIN
  * LEFT JOIN
  * RIGHT JOIN
  * FULL OUTER JOIN
  * CROSS JOIN
  * SELF JOIN
* JOIN conditions
* USING vs ON
* Multi-table joins

## **8. Grouping & Aggregation**
* GROUP BY
* HAVING
* Grouping sets
* ROLLUP
* CUBE

## **9. Subqueries**
* Subqueries in SELECT
* Subqueries in WHERE
* Subqueries in FROM (Derived tables)
* EXISTS vs IN vs ANY vs ALL
* Correlated Subqueries

## **10. Set Operations**
* UNION
* UNION ALL
* INTERSECT
* EXCEPT / MINUS

## **11. Indexing**
* What is an Index?
* How indexes work (B-Tree)
* Types of Indexes:
  * Single-column
  * Composite index
  * Unique index
  * Full-text index
  * Bitmap index
* Advantages & disadvantages
* When to use (and avoid) indexes
* Index performance analysis

## **12. Views**
* What is a View?
* CREATE VIEW
* Materialized View
* Read-only vs Updatable Views
* Dropping views

## **13. SQL Constraints (Deep Explanation)**
* NOT NULL
* UNIQUE
* PRIMARY KEY
* FOREIGN KEY
* CHECK
* DEFAULT
* ON DELETE CASCADE
* ON UPDATE CASCADE

## **14. Transactions**
* What is a Transaction?
* COMMIT
* ROLLBACK
* SAVEPOINT
* Autocommit
* Isolation Levels:
  * READ UNCOMMITTED
  * READ COMMITTED
  * REPEATABLE READ
  * SERIALIZABLE
* Problems prevented by isolation:
  * Dirty reads
  * Non-repeatable reads
  * Phantom reads

## **15. Stored Procedures & Functions**
* What is a stored procedure?
* Advantages
* CREATE PROCEDURE
* Parameters (IN / OUT)
* Stored functions (return values)
* Cursors
* Error handling

## **16. Triggers**
* What is a Trigger?
* BEFORE / AFTER triggers
* INSERT, UPDATE, DELETE triggers
* Use cases (audit logs, validations)

## **17. Performance Tuning**
* Query execution order (very important)
* EXPLAIN / EXPLAIN ANALYZE
* Query Plans
* Index selection
* Avoiding SELECT *
* Avoiding unnecessary subqueries
* Using LIMIT / OFFSET efficiently
* Normalization & Denormalization trade-offs

## **18. Normalization**
* Why normalize?
* 1NF, 2NF, 3NF, BCNF
* Functional dependencies
* Denormalization concepts

## **19. Database Design**
* Entities and Attributes
* Entity-Relationship Diagrams (ERD)
* Primary and foreign keys
* Designing tables from requirements
* Handling Many-to-Many relationships (junction table)

## **20. Security in SQL**
* Users and roles
* GRANT
* REVOKE
* Encryption basics
* SQL injection prevention
  * Parameterized queries
  * Escaping
  * Least privilege principle

## **21. Window Functions (Advanced SQL – Must Learn for Data Jobs)**
* OVER() clause
* PARTITION BY
* ORDER BY in window function
* ROW_NUMBER()
* RANK()
* DENSE_RANK()
* LAG() / LEAD()
* MOVING AVERAGES
* Cumulative sums with SUM() OVER()

## **22. Advanced SQL Topics**
* Common Table Expressions (CTE)
  * WITH clause
  * Recursive CTEs
* Pivoting / Unpivoting
* JSON handling
  * JSON_EXTRACT
  * JSON_ARRAYAGG
* Temporary Tables
* Cross Apply, Outer Apply (SQL Server/Oracle)
* MERGE statement (UPSERT)

## **23. SQL for Analytics**
* Data summarization
* Cohort analysis
* Retention calculations
* Funnels
* Time-series queries
* Ranking products / categories / cities
* Window functions for analytics

## **24. SQL in Real Applications**
* SQL in backend applications
* ORM (Django ORM, SQLAlchemy)
* Connecting Python to SQL (pymysql, psycopg2)
* ETL pipelines using SQL
* Data Warehousing SQL