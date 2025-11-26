---
layout: post
title: Database Keys – SQL
author: Dipak Pulami Magar
date :  2025-11-26 16:12:45 +0545
categories: sql
status: draft
---

Database keys are fields or groups of fields that uniquely identify each row in a table, establish relationships between tables, and maintain data integrity. Common types include the **primary key**, which uniquely identifies each row, and the **foreign key**, which links tables together by referencing a primary key. Other important keys include the candidate key, super key, unique key, and composite key. 

## Key types and functions
- **Primary Key** A field that uniquely identifies each record in a table. It can be an existing attribute or one generated specifically for the database.
- **Foreign Key** A field in one table that references the primary key of another table. This is used to link tables together and ensure referential integrity.
- **Candidate Key** Any attribute or set of attributes that can be used to uniquely identify a row in a table. A table can have multiple candidate keys.
- **Super Key** A set of attributes that uniquely identifies each row. A super key can have additional attributes that are not necessary for unique identification.
- **Unique Key** A key that ensures all values in a column are unique, similar to a primary key, but can allow for a single NULL value.
- **Composite Key** A key made up of two or more columns that, when combined, uniquely identify a row. Also known as a compound key. 

## Why keys are important
- **Uniqueness:** They ensure each record is uniquely identifiable, preventing duplicate entries.
- **Data integrity:** They enforce rules that keep data accurate, consistent, and reliable.
- **Relationships:** They establish links between different tables, allowing you to connect related information across the database.
- **Efficiency:** They enable faster and more efficient data retrieval and manipulation.
