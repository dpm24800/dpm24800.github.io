---
layout: post
title: SQL Test – 2
description: 
thumbnail: ../../../../../assets/images/sql/sql-test.png
author: Dipak Pulami Magar
date :  2025-12-01 5:12:45 +0545
categories: sql test
status: draft
---


```sql
-- Creating transactions table
CREATE TABLE IF NOT EXISTS transactions(
	customer_id VARCHAR(5),
    purchase_date DATE,
    transaction_id VARCHAR(8)
);
```

```sql
-- Inserting data
INSERT INTO transactions(customer_id, purchase_date, transaction_id) VALUES
('C1', '2024-01-10', 'T001'),
('C1', '2024-01-15', 'T002'),
('C2', '2024-02-01', 'T003'),
('C1', '2024-02-20', 'T004'),
('C2', '2024-03-05', 'T005');
```


**1. Retrieve the first purchase date and the total number of purchases for each customer.**

```sql
-- 1. Retrieve the first purchase date and the total number of purchases for each customer.
SELECT 
    customer_id, 
    MIN(purchase_date) AS first_purchase_date, 
    COUNT(customer_id) AS total_purchases
FROM transactions
GROUP BY customer_id;
```

**Output**:
```
+-------------+---------------------+-----------------+
| customer_id | first_purchase_date | total_purchases |
+-------------+---------------------+-----------------+
| C1          | 2024-01-10          |               3 |
| C2          | 2024-02-01          |               2 |
+-------------+---------------------+-----------------+
```

**Alter the table**
```sql
ALTER TABLE transactions` 
ADD COLUMN `amount` INT NULL AFTER `transaction_id`;

UPDATE transactions SET amount = 100 WHERE transaction_id = 'T001';
UPDATE transactions SET amount = 150 WHERE transaction_id = 'T002';
UPDATE transactions SET amount = 100 WHERE transaction_id = 'T003';
UPDATE transactions SET amount = 100 WHERE transaction_id = 'T004';
UPDATE transactions SET amount = 150 WHERE transaction_id = 'T005';
```

**2.  Find the transaction amount that occurs most frequently**
```sql
-- 2.  Find the transaction amount that occurs most frequently
SELECT amount
FROM transactions
GROUP BY amount
ORDER BY COUNT(amount) DESC
LIMIT 1;
```

<!-- ```sql
-- Rough 
SELECT amount, COUNT(*) AS freq
FROM transactions
GROUP BY amount
ORDER BY freq DESC;
``` -->

**Output**:
```
+--------+
| amount |
+--------+
|    100 |
+--------+
```

---

```sql
CREATE TABLE IF NOT EXISTS employee(
	emp_id INT,
	department VARCHAR(20),
	salary INT
);

INSERT INTO employee (emp_id, department, salary) VALUES ('1', 'HR', '50000');
INSERT INTO employee (emp_id, department, salary) VALUES ('2', 'IT', '80000');
INSERT INTO employee (emp_id, department, salary) VALUES ('3', 'IT', '85000');
INSERT INTO employee (emp_id, department, salary) VALUES ('4', 'Sales', '60000');
INSERT INTO employee (emp_id, department, salary) VALUES ('5', 'Sales', '62000');
INSERT INTO employee (emp_id, department, salary) VALUES ('6', 'Finance', '75000');
```

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employee
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 3;
```

**Output**
```
+------------+------------+
| department | avg_salary |
+------------+------------+
| IT         | 82500.0000 |
| Finance    | 75000.0000 |
| Sales      | 61000.0000 |
+------------+------------+
```

---
```sql
CREATE TABLE IF NOT EXISTS students21(
	student_id INT PRIMARY KEY,
	name VARCHAR(50),
	age INT,
	department VARCHAR(30),
	gpa FLOAT
);

INSERT INTO students21 (student_id, name, age, department, gpa) VALUES ('1', 'Alice', '20', 'ComputerSci', '3.8');
INSERT INTO students21 (student_id, name, age, department, gpa) VALUES ('2', 'Bob', '22', 'Physics', '3.2');
INSERT INTO students21 (student_id, name, age, department, gpa) VALUES ('3', 'Charlie', '21', 'Mathematics', '2.9');
INSERT INTO students21 (student_id, name, age, department, gpa) VALUES ('4', 'Diana', '23', 'ComputerSci', '3.6');
INSERT INTO students21 (student_id, name, age, department, gpa) VALUES ('5', 'Eva', '20', 'Physics', '3.1');
```

```sql
CREATE TABLE IF NOT EXISTS courses(
	course_id INT PRIMARY KEY,
    course_name VARCHAR(20),
    credits TINYINT
);

INSERT INTO courses (course_id, course_name, credits) VALUES ('101', 'Database', '3');
INSERT INTO courses (course_id, course_name, credits) VALUES ('102', 'Algorithms', '4');
INSERT INTO courses (course_id, course_name, credits) VALUES ('103', 'Physics-I', '3');
INSERT INTO courses (course_id, course_name, credits) VALUES ('104', 'Calculus', '4');
INSERT INTO courses (course_id, course_name, credits) VALUES ('105', 'AI Basics', '3');
```

```sql
CREATE TABLE IF NOT EXISTS enrollments(
	enrollment_id INT PRIMARY KEY,
	student_id INT,
	course_id INT,
	semester VARCHAR(20),
	grade VARCHAR(5)
);

INSERT INTO enrollments (enrollment_id, student_id, course_id, semester, grade) VALUES
(1, 1, 101, 'Fall2024', 'A'),
(2, 1, 102, 'Fall2024', 'B'),
(3, 2, 103, 'Fall2024', 'B+'),
(4, 3, 104, 'Fall2024', 'A-'),
(5, 4, 101, 'Fall2024', 'B'),
(6, 5, 103, 'Fall2024', 'C+'),
(7, 2, 104, 'Spring25', 'A'),
(8, 3, 105, 'Spring25', 'B+');
```

---
**1. Select all students**
```sql
SELECT * FROM students;
```

**2. Display only the names and GPA of students**
```sql
SELECT name, gpa FROM students;
```

**3. Find students who belong to the Physics department**
```sql
SELECT * FROM students
WHERE department = 'Physics';
```

**4. List students whose GPA is greater than 3.5**
```sql
SELECT * FROM students
WHERE gpa > 3.5;
```

**5. Retrieve the course names with credits greater than 3**
```sql
SELECT course_name FROM courses
WHERE credits > 3;
```

**6. Show all enrollments for Fall2024**
```sql
SELECT * FROM enrollments
WHERE semester = 'Fall2024';
```

**7. Get student names in ascending order**
```sql
SELECT name FROM students
ORDER BY name ASC;
```

**8. Count the total number of students**
```sql
SELECT COUNT(*) AS total_students FROM students;
```

**9. Find the average GPA of students in ComputerSci department**
```sql
SELECT AVG(gpa) AS avg_gpa
FROM students
WHERE department = 'ComputerSci';
```

**10. Show distinct department names**
```sql
SELECT DISTINCT department
FROM students;
```

**11. Find students who scored grade A in any course**
```sql
SELECT DISTINCT s.name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
WHERE e.grade = 'A';
```

**12. Retrieve all courses taken by Alice**
```sql
SELECT c.course_name
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
JOIN students s ON s.student_id = e.student_id
WHERE s.name = 'Alice';
```

**13. List student names along with the courses they enrolled in**
```sql
SELECT s.name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;
```

**14. Show students who are enrolled in more than one course**
```sql
SELECT s.name, COUNT(*) AS course_count
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id
HAVING COUNT(*) > 1;
```

**15. Get the highest GPA student from the Physics department**
```sql
SELECT *
FROM students
WHERE department = 'Physics'
ORDER BY gpa DESC
LIMIT 1;
```

**16. Courses that have not been taken by any student**
```sql
SELECT c.*
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
WHERE e.course_id IS NULL;
```

**17. Display the number of students enrolled in each course**
```sql
SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;
```

**18. Student names with their average grade per semester**

(Assuming grade-to-points conversion is needed: A=4, A-=3.7, B=3, B+=3.3, C+=2.3)

#Step 1: Use a CASE mapping

```sql
SELECT s.name, e.semester,
       AVG(
         CASE e.grade
           WHEN 'A'  THEN 4.0
           WHEN 'A-' THEN 3.7
           WHEN 'B+' THEN 3.3
           WHEN 'B'  THEN 3.0
           WHEN 'C+' THEN 2.3
         END
       ) AS avg_grade_points
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.name, e.semester;
```

**19. Update Bob’s GPA to 3.5**
```sql
UPDATE students
SET gpa = 3.5
WHERE name = 'Bob';
```

**20. Delete enrollments where grade is C+**
```sql
DELETE FROM enrollments
WHERE grade = 'C+';
```