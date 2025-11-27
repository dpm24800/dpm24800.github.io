---
layout: post
title: Table Operations – SQL
author: Dipak Pulami Magar
date :  2025-11-24 14:12:45 +0545
categories: sql
status: draft
---

## 1. Creating a Table
To create a new table, `CREATE TABLE` command is used thus:  

**Syntax**:
```sql
-- Attempts to create the table; throws an error if it already exists.
CREATE TABLE table_name(
    field1 datatype (constraint1 constraint2, constraintN),
    field2 datatype,
    .......
    filedN datatype
); 

-- Safely creates the table only if it doesn’t already exist, preventing errors.
CREATE DATABASE IF NOT EXISTS database_name; 
```
**Example**:
```
CREATE DATABASE hotel;
CREATE DATABASE IF NOT EXISTS library;
```

## 2. Updating a table
**Syntax**:
```sql
ALTER TABLE table_name
CHANGE COLUMN column_name (new)column_name DATATYPES CONSTRAINTS;
```

**Examples**:
```sql
ALTER TABLE `test`.`library1` 
CHANGE COLUMN `library_id` `library_id` INT NOT NULL AUTO_INCREMENT;
```

```sql
ALTER TABLE `test`.`customers` 
CHANGE COLUMN `dist` `district` VARCHAR(50) NULL DEFAULT NULL ;
```

## 3. Renaming a Table
To rename a table `RENAME TO` keyword is used along with `ALTER TABLE`, thus:

**Syntax**:
```sql
-- Renaming a table name
ALTER TABLE table_name
RENAME TO new_name;
```

**Example**:
```sql
ALTER TABLE `test`.`students` 
RENAME TO `test`.`customers`;
```

## 4. Dropping/Removing a Table
To drop/remove a existing table, `DROP` keyword is used thus:  
**Syntax**:
```sql
-- Removing a table;
DROP TABLE table_name;
DROP TABLE IF EXISTS table_name;
```
**Example**:
```
DROP DATABASE library;
```

Dropping a database is serious matter so confirm whether you're really doing this.