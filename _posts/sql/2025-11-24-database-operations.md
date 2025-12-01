---
layout: post
title: Database Operations – SQL
author: Dipak Pulami Magar
thumbnail: ../../../../../assets/images/sql/database-operations.png
date :  2025-11-24 10:12:45 +0545
categories: sql
status: draft
---

## 1. Creating a database
To create a new database, `CREATE DATABASE` command is used thus:  

**Syntax**:
```sql
-- Attempts to create the database; throws an error if it already exists.
CREATE DATABASE database_name; 

-- Safely creates the database only if it doesn’t already exist, preventing errors.
CREATE DATABASE IF NOT EXISTS database_name; 
```
**Example**:
```
CREATE DATABASE hotel;
CREATE DATABASE IF NOT EXISTS library;
```

## 2. Using a database
After creating a database it needs to be selected/used before working on it. For the selection `USE` keyword is used thus:  

**Syntax**:
```sql
-- Using a database
USE database_name;
```

**Example**:
```
USE library;
```

## 3. Renaming a Database
To rename a database in MySQL (since direct renaming isn’t supported in recent versions), you can create a new database, move tables, and drop the old one.

**Syntax**:
```sql
-- Step 1: Create a new database
CREATE DATABASE new_database_name;

-- Step 2: Move tables from old to new database
RENAME TABLE old_database_name.table1 TO new_database_name.table1,
             old_database_name.table2 TO new_database_name.table2;

-- Step 3: Drop the old database
DROP DATABASE old_database_name;
```

Example:

```sql
CREATE DATABASE library_new;

RENAME TABLE library.books TO library_new.books,
             library.members TO library_new.members;

DROP DATABASE library;
```

This method effectively “renames” the database while keeping all data intact.

## 4. Dropping/removing a database
To drop/remove a existing database, `DROP` keyword is used thus:  
**Syntax**:
```sql
-- Removing a database;
DROP DATABASE database_name;
```
**Example**:
```
DROP DATABASE library;
```

Dropping a database is serious business so confirm whether you're really doing this.