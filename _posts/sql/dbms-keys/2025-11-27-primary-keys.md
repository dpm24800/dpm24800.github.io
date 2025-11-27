---
layout: post
title:  Primary Keys – SQL
author: Dipak Pulami Magar
date:   2025-11-27 10:12:45 +0545
categories: sql
status: draft
---





## Creating Primary Keys From Multiple Fields

```sql
CREATE TABLE Teacher(
    teacher_id INT NOT NULL,
    subject_id INT NOT NULL,
    dept_id INT NOT NULL,
    PRIMARY KEY (subject_id, dept_id)
);
```