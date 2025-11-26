---
layout: post
title: Database Constraints – SQL
author: Dipak Pulami Magar
date:   2025-11-26 16:12:45 +0545
categories: sql
status: draft
---

## Keys
### Primary Key
- every value is unique
- no null value is present
- if null produces error

## Foreign Key
- primary key of another table

# Database Constraints
Database constraints are rules enforced on data within a database to ensure its accuracy, consistency, reliability and integrity. These rules are fundamental part of database design, helping to prevent invalid data from being entered, maintaining valid relationships between tables/data, and ensuring the data adheres to defined business logic. They are typically defined as part of a table's schema and are automatically enforced by the database management system (DBMS). Constraints can be applied at the column level (affecting a single column) or the table level (affecting the entire table or multiple columns).

## 1. Common Types of Database Constraints
Here are the most widely used constraints in SQL:

**PRIMARY KEY**:  
  Uniquely identifies each row (record) in a table. It is a combination of NOT NULL and UNIQUE constraints. Each table can have only one primary key, which serves as the main identifier for records. It consists of one or more columns and cannot contain NULL values. 

**FOREIGN KEY**:  
  Establishes a link and enforces a relationship between data in two tables. A foreign key in one table (the child table) references the primary key in another table (the parent table), ensuring that a value inserted into the foreign key column must exist in the referenced primary key column. This prevents "orphaned" records and maintains referential integrity.

**UNIQUE**:  
  Ensures that all values in a specified column or set of columns are unique across all rows in the table. Unlike a primary key, a unique constraint can allow one NULL value.

**NOT NULL**:  
  Ensures that a column cannot contain NULL values. - This means a value must always be provided for that column when a record is inserted or updated.

**CHECK**:  
  Enforces domain integrity by limiting the range of values that can be accepted by a column based on a specified condition. - In other words, enforces a specific condition that must be met for data to be inserted or updated in a column. - For example, a  `CHECK` constraint could ensure that an `Age` column always contains a positive value or a salary is within a specific range.

**DEFAULT**:  
  Automatically assigns a default value to a column if no value is explicitly provided/specified during the insertion of a new row. This helps maintain consistency and simplifies data entry.

## 2. Importance of Database Constraints
<!-- Constraints are the primary mechanism for maintaining the integrity, accuracy, and reliability of the data stored in a database. -->

**1. Ensure Data Accuracy**
Constraints act as the first line of defense against incorrect data. For example, restricting age to positive integers ensures that only valid information enters the system.
<!-- Constraints prevent invalid or incorrect data (e.g., negative age, duplicate IDs) from being inserted into the database. -->

**2. Maintain Data Consistency**
Foreign keys and relational rules keep different tables aligned. If an order references a customer, the customer must exist—ensuring logical consistency throughout the database.
<!-- They make sure related data stays synchronized—for example, foreign key constraints ensure that referenced records actually exist. -->

**3. Protect Data Integrity**
By enforcing NOT NULL, UNIQUE, and CHECK rules, constraints make sure that essential fields are always filled in and follow the correct format, guaranteeing long-term reliability of the stored data.
<!-- They make sure related data stays synchronized—for example, foreign key constraints ensure that referenced records actually exist. -->

**4. Reduce Application-Level Validation**
With constraints handling foundational checks, developers don’t need to repeatedly implement the same validation in multiple parts of an application, reducing redundancy and potential errors.
<!-- They make sure related data stays synchronized—for example, foreign key constraints ensure that referenced records actually exist. -->

**5. Prevent Duplicate Records**
Unique constraints ensure that values meant to be exclusive—like email, username, or transaction ID—are never duplicated, which helps maintain clean and trustworthy data.
<!-- Unique constraints ensure that key fields like email or username are not repeated. -->

**6. Enable Reliable Relationships**
Primary keys uniquely identify each row, and foreign keys ensure proper links between tables. This creates structured, interconnected datasets that support complex queries and reporting.
<!-- Primary keys and foreign keys help maintain clear, correct relationships between tables. -->

**7. Improve Data Quality**
CHECK constraints enforce that values fall within a reasonable range or follow a required pattern (e.g., price > 0), ensuring the stored data is meaningful and trustworthy.
<!-- Validation rules like CHECK constraints ensure values fall within valid ranges or formats. -->

**8. Enhance Security**
Constraints prevent accidental or malicious insertion of invalid data, safeguarding the database even when users interact directly via SQL scripts or external tools.
<!-- Constraints stop unauthorized or unintended data changes, even if someone interacts with the database directly. -->

**9. Simplify Maintenance**
Centralizing rules at the database level ensures that when applications evolve or new systems connect to the same data source, they all automatically follow the same validation rules.
<!-- With business rules enforced at the database level, future updates and new applications automatically follow the same rules. -->

**10. Support Better Query Performance**: Constraints tied with indexing—such as PRIMARY KEY and UNIQUE—help speed up search operations, joins, and overall query processing, improving system performance.
<!-- Indexed constraints (like PRIMARY KEY or UNIQUE) can speed up searches and joins. -->

<!-- ---

- **Data Integrity**:  
  Prevents incorrect, duplicate, or inconsistent data from entering the database.
- **Error Prevention**: They prevent common data entry errors, such as duplicate IDs, negative prices, or references to non-existent records, by aborting any action that violates the defined rules. 

- **Data Accuracy**:   
  Ensures that stored data aligns with real-world expectations and business rules.
- **Business Rules Enforcement**: They ensure that the data adheres to predefined business rules and logical structures, such as ensuring an order is always linked to an existing customer.
- 
- **Referential Integrity:** 
  Maintains the relationships between tables, preventing "orphan" records.

- **Reduced Manual Validation**:  
  Automates data validation at the database level, reducing the need for application-level checks.
  - **Centralized Validation**: Enforcing rules at the database level, rather than in the application code, ensures that the rules are consistently applied regardless of how the data is accessed or modified (e.g., via web interface, mobile app, or direct SQL scripts).
    - By **automating** and **centralizing** data validation at the **database level**, this approach **reduces** the need for **manual**, application-level checks, ensuring rules are **consistently applied** regardless of how the data is **accessed** or **modified**.

- **Improved Performance:** 
  Constraints, especially primary keys and unique constraints, often lead to the creation of indexes, which can improve data retrieval performance. -->



## 3. **Example**
```sql
-- Create the Suppliers table (Parent table)
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY,               -- PRIMARY KEY constraint (NOT NULL and UNIQUE)
    SupplierName VARCHAR(100) NOT NULL,       -- NOT NULL constraint
    ContactEmail VARCHAR(255) UNIQUE,         -- UNIQUE constraint
    Country VARCHAR(50) DEFAULT 'Nepal'         -- DEFAULT constraint
);

-- Create the Products table (Child table)
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,                -- PRIMARY KEY constraint
    ProductName VARCHAR(100) NOT NULL,        -- NOT NULL constraint
    SupplierID INT,                           -- Column to hold the foreign key
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT NOT NULL,
    
    -- CHECK constraint: Ensures the price is positive
    CHECK (Price > 0),
    
    -- CHECK constraint: Ensures stock quantity is not negative
    CHECK (StockQuantity >= 0),
    
    -- FOREIGN KEY constraint: Links to the Suppliers table
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);
```
**Example Data Inserts**  
You can test these constraints by running the following SQL commands:

```sql
-- Insert a valid supplier
INSERT INTO Suppliers (SupplierID, SupplierName, ContactEmail)
VALUES (1, 'Tech Supplies Inc.', 'contact@techsupplies.com');

-- Insert a valid product linked to the supplier
INSERT INTO Products (ProductID, ProductName, SupplierID, Price, StockQuantity)
VALUES (101, 'Laptop', 1, 999.99, 50);

-- This insert will fail because the SupplierID 99 does not exist (FOREIGN KEY violation)
-- INSERT INTO Products (ProductID, ProductName, SupplierID, Price, StockQuantity)
-- VALUES (102, 'Mouse', 99, 19.99, 100);

-- This insert will fail because the price is invalid (CHECK constraint violation)
-- INSERT INTO Products (ProductID, ProductName, SupplierID, Price, StockQuantity)
-- VALUES (103, 'Keyboard', 1, -5.00, 20);
```

<!-- ```sql
-- Constraints
CREATE TABLE IF NOT EXISTS library (
	library_id INT PRIMARY KEY,
	student_id INT,
	books VARCHAR(100) NOT NULL,
	fine FLOAT DEFAULT 0.0,
	age INT UNIQUE,
	CONSTRAINT age_check CHECK (age >= 20),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
``` -->

everything that follows after datatype is constraint.

## Operators
**AND**:
**OR**
**NOT**
**Examples**:
```sql
SELECT * FROM library WHERE fine > 0; -- WHERE clause for setting conditions
SELECT * FROM library WHERE fine > 20 AND fine <50; -- setting multiple conditions with AND
SELECT * FROM library WHERE books = 'Pandas Basics' OR books = 'NumPy Basics';
SELECT * FROM library WHERE books NOT IN ('Pandas Basics');
```

**IN**
**BETWEEN**

**Examples**:
```sql
SELECT * FROM library WHERE books IN ('Pandas Basics', 'NumPy Basics');
SELECT * FROM library WHERE books NOT IN('Pandas Basics', 'NumPy Basics');
SELECT * FROM library WHERE age BETWEEN 25 AND 60;
```


## **Clauses**
WHERE
ORDER BY
LIMIT

CREATE TABLE IF NOT EXISTS library(
	library_id INT PRIMARY KEY,
	student_id INT FOREIGN KEY,
	books VARCHAR(100) NOT NULL,
	fine FLOAT DEFAULT 0.0,
	age INT UNIQUE,
	CONSTRAINT age_check CHECK (age>=20)
);

**Creating a database**

**Creating a table**:
```sql
-- CREATE TABLE IF NOT EXISTS table_name;


```sql
CREATE TABLE IF NOT EXISTS practice;
	col INT,
	col2 VARCHAR(10)
	col3 INT,
	col4 FLOAT,
)
```

**Inserting data into table**:
```sql
INSERT INTO table_name
(field1, field2, field3, field4) VALUES
(value11, 'value12', 'value13', value14),
(value21, 'value22', 'value23, value24),
(value31, 'value32', 'value33', value34);
```

Dropping a database

Dropping a table
```sql
-- DROP TABLE database_name.table_name;
DROP TABLE test.tbl_test;
```

### References:
- [SQL Constraints](https://www.w3schools.com/sql/sql_constraints.asp)
- [SQL  Constraints](https://www.geeksforgeeks.org/sql/sql-constraints/)
- [Constraints on Relational Database Model ](https://www.geeksforgeeks.org/dbms/constraints-on-relational-database-model/)