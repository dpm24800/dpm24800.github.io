## 2. Types of SQL Commands: categories of SQL Command  
(Categorization is Crucial)

### 2.1. DDL (Data Definition Language)
> Creating and Modifying Database Objects

DDL, or Data Definition Language, in SQL refers to a set of commands used to define, modify, and manage the structure of a database. These commands are responsible for creating, altering, and deleting database objects such as tables, views, indexes, and schemas.

The primary DDL commands include:

**CREATE**: Used to create new database objects.
```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    HireDate DATE
);
```
**ALTER**: 
Used to modify the structure of existing database objects. This can include adding or dropping columns, changing data types, or adding/removing constraints.
```sql
  ALTER TABLE Employees
  ADD COLUMN Email VARCHAR(100);
```


**DROP**:  
Used to delete existing database objects. This permanently removes the object and any associated data.
```sql
DROP TABLE Employees;
```

**TRUNCATE**:  
Used to remove all rows from a table, but keeps the table structure intact. This is faster than DELETE for removing all data from a table as it does not log individual row deletions. 

```sql
TRUNCATE TABLE Employees;
```
DDL commands fundamentally change the database schema and are typically executed by database administrators or developers responsible for managing the database structure. Unlike Data Manipulation Language (DML) commands, which deal with data within the objects, DDL focuses on the objects themselves.

---


#### **CREATE** Defining database objects
##### `CREATE DATABASE`: Creating a Database
##### `CREATE TABLE`: Creating a Table
###### Defining columns, data types, and constraints
###### Table Constraints
      * `PRIMARY KEY`
      * `FOREIGN KEY`
      * `UNIQUE`
      * `NOT NULL`
      * `CHECK`
      * `DEFAULT`
    * `CREATE VIEW`
    * `CREATE INDEX`

#### **ALTER** 
`ALTER` command is used to modify the structure of an existing object (e.g., adding/dropping columns, changing data types).

The `ALTER TABLE` statement is used to add, delete, or modify columns in an existing table.

The `ALTER TABLE` statement is also used to add and drop various constraints on an existing table.
`ALTER TABLE`: Altering a Table (add, drop, modify columns).


### Adding a column
Syntx:
```sql
ALTER TABLE table_name
ADD column_name datatype;
```

Example:
```sql
ALTER TABLE customers
ADD email varchar(255);
```

To delete a column in a table, use the following syntax (notice that some database systems don't allow deleting a column):

### **Removing a columns**
Syntax,
```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

Example,
```sql
ALTER TABLE customers
DROP COLUMN email;
```



#### **DROP** 
`DROP` command is used to delete database objects, like, table, _______ or database itself.

**1. Dropping/deleting a table**
`DROP TABLE`: Deleting database objects
```sql
-- Syntax: DROP TABLE table_name;
DROP TABLE tbl_test;
```

**2. Dropping/deleting a database**  
```sql
-- Syntax: DROP DATABASE database_name;
DROP TABLE db_practice;
```

#### **TRUNCATE** 
Quickly removing all rows from a table (DDL because it resets the structure/storage).

**`TRUNCATE TABLE` (vs. `DELETE`)**

#### `RENAME`
