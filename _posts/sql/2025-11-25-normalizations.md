---
layout: post
title: Database Normalizations – SQL
description: Combining Data from Multiple Tables in SQL
# thumbnail: ../../../../assets/images/pandas/encoding-categorical-data.png
author: Dipak Pulami Magar
date:   2025-11-24 02:12:45 +0545
categories: sql
status: published
---

## Introduction
- Database normalization is the process of organizing a database to reduce redundancy and improve data integrity by dividing large tables into smaller, linked tables. 
- It follows a series of rules called normal forms, with the first three (1NF, 2NF, and 3NF) being the most common.
- Normalization helps prevent errors like insertion, update, and deletion anomalies and leads to a more efficient, flexible, and consistent database. 

## Goals of database normalization
- **Reduce data redundancy:** Minimize duplicate data by storing it in a single location.
- **Improve data integrity:** Ensure data is consistent and accurate across the database.
- **Prevent data anomalies:** Avoid issues where, for example, a change in one record unintentionally affects other data.
- **Increase efficiency:** Make the database more flexible and easier to manage. 

## How it works (The normal forms)
Normalization is achieved by following a set of rules, with each level building upon the previous one: 

- **First Normal Form (1NF)**
  - Eliminate repeating groups of data within individual rows.
  - Ensure each column contains atomic (single) values and that all columns have unique names.
  - Every table must have a primary key.
- **Second Normal Form (2NF):**
  - Must be in 1NF first.
  - All non-key attributes must be fully dependent on the primary key.
  - This means creating separate tables for sets of values that apply to multiple records to avoid redundancy.
- **Third Normal Form (3NF):**
  - Must be in 2NF first.
  - Eliminate transitive dependencies, meaning non-key attributes should not be dependent on other non-key attributes.
  - All attributes must be directly dependent on the primary key. 

## Example
Consider a library database with an unnormalized table that lists book details and the borrower's information together. When a member borrows multiple books, their information is repeated. 

- **Unnormalized:** A single table contains book and borrower details, leading to redundant borrower information for each book borrowed.
- **Normalized:** The data is split into three tables: "Books," "Members," and "Borrowed." The "Borrowed" table links the "Books" and "Members" tables using primary and foreign keys, removing the redundancy and saving space.