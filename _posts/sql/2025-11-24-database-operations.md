---
layout: post
title: Database Operations – SQL
author: Dipak Pulami Magar
date :  2025-11-24 10:12:45 +0545
categories: sql
status: draft
---

## 1. Creating a Database
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

## 2. Using a Database
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

## 3. Dropping/Removing a Database
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

Dropping a database is serious matter so confirm whether you're really doing this.