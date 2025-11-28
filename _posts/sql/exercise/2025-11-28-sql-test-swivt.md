---
layout: post
title: SQL Test – Swivt
description: 
# thumbnail: ../../../../assets/images/sql/dbms-keys.png
author: Dipak Pulami Magar
date :  2025-11-28 12:12:45 +0545
categories: sql test
status: draft
---

```
Table: Orders
+---------+-----------+------------+-------------+-------------+
| ord_no  | purch_amt | ord_date   | customer_id | salesman_id |
+---------+-----------+------------+-------------+-------------+
| 70001   | 150.50    | 2012-10-05 | 3005        | 5002        |
| 70009   | 270.65    | 2012-09-10 | 3001        | 5005        |
| 70002   | 65.26     | 2012-10-05 | 3002        | 5001        |
| 70004   | 110.50    | 2012-08-17 | 3009        | 5003        |
| 70007   | 948.50    | 2012-09-10 | 3005        | 5002        |
| 70005   | 2400.60   | 2012-07-27 | 3007        | 5001        |
| 70008   | 5760.00   | 2012-09-10 | 3002        | 5001        |
| 70010   | 1983.43   | 2012-10-10 | 3004        | 5006        |
| 70003   | 2480.40   | 2012-10-10 | 3009        | 5003        |
| 70012   | 250.45    | 2012-06-27 | 3008        | 5002        |
| 70011   | 75.29     | 2012-08-17 | 3003        | 5007        |
| 70013   | 3045.60   | 2012-04-25 | 3002        | 5001        |
| 70014   | 5000.00   | 2012-10-10 | 3004        | 5007        |
+---------+-----------+------------+-------------+-------------+
```

## Questions 
**1. Create a Table: Orders as shown above.**

```sql
 -- 1. Create a Table: Orders as shown above
CREATE TABLE IF NOT EXISTS Orders(
	order_no INT PRIMARY KEY,
	purch_amt FLOAT,
	ord_date DATE,
	customer_id INT,
	salesman_id INT
);

INSERT INTO orders (order_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
(70001, 150.50, '2012-10-05', 3005, 5002),
(70002, 65.26, '2012-10-05', 3002, 5001),
(70003, 2480.40, '2012-10-10', 3009, 5003),
(70004, 110.50, '2012-08-17', 3009, 5003),
(70005, 2400.60, '2012-07-27', 3007, 5001),
(70007, 948.50, '2012-09-10', 3005, 5002),
(70008, 5760.00, '2012-09-10', 3002, 5001),
(70009, 270.65, '2012-09-10', 3001, 5005),
(70010, 1983.43, '2012-10-10', 3004, 5006),
(70011, 75.29,  '2012-08-17', 3003, 5007),
(70012, 250.45, '2012-06-27', 3008, 5002),
(70013, 3045.60,'2012-04-25', 3002, 5001),
(70014, 5000.60,'2012-10-10', 3004, 5007);
```

**2. Calculate Total Purchase Amount of All Orders**

```sql
-- 2. Calculate Total Purchase Amount of All Orders: 17541.180145263672
SELECT SUM(purch_amt) AS `Total Purchase Amount` 
FROM Orders;
```
**3. Calculate Average Purchase Amount of All Orders**

```sql
-- 3. Calculate Average Purchase Amount of All Orders: 1461.765012105306
SELECT AVG(purch_amt) AS `Average Purchase Amount` 
FROM Orders;
```

**4. Count the Number of Unique Salespeople**

```sql
-- 4. Count the Number of Unique Salespeople
SELECT COUNT(DISTINCT salesman_id) AS `Number of Unique Salespeople`
FROM Orders;
```

**5. Find Maximum Purchase Amount**

```sql
-- 5. Find Maximum Purchase Amount: 5760
SELECT MAX(purch_amt) AS `Maximum Purchase Amount`
FROM Orders;
```

**6. Find Minimum Purchase Amount**

```sql
-- 6. Find Minimum Purchase Amount: 65.26
SELECT MIN(purch_amt) AS `Minimum Purchase Amount`
FROM Orders;
```

**7. Find Highest Purchase Amount Ordered by Each Customer**

```sql
-- 7. Find Highest Purchase Amount Ordered by Each Customer
SELECT customer_id, MAX(purch_amt) AS `Highest Purchase Amount`
FROM Orders
GROUP BY customer_id
ORDER BY customer_id;
```

**8. Highest Purchase by Customer on Date**

```sql
-- 8. Highest Purchase by Customer on Date
SELECT ord_date, customer_id, MAX(purch_amt) AS `Higest Purchase Amount`
FROM Orders
GROUP BY ord_date, customer_id
ORDER BY ord_date ASC, customer_id ASC;
```

**9.  Highest Purchase Amount by Salesperson on '2012-08-17'**

```sql
-- 9. Highest Purchase Amount by Salesperson on '2012-08-17'
SELECT ord_date, salesman_id, purch_amt
FROM Orders
WHERE ord_date = '2012-08-17'
ORDER BY salesman_id
LIMIT 1;
```

**10. Purchase Amount >= 2100 by Customer on Specific Date**

```sql
-- 10. Highest Purchase Amount by Customer on Specific Date
SELECT customer_id, ord_date, purch_amt
FROM Orders
WHERE purch_amt >= 2100
ORDER BY ord_date;
```

```sql
-- (Date-wise highest)
SELECT ord_date, MAX(purch_amt) AS highest_purch_amount
FROM Orders
GROUP BY ord_date
ORDER BY ord_date;
```

**11. Max Purchase Amount by Customer and Order Date (2000-6000)**

```sql
SELECT customer_id, ord_date, purch_amt
FROM Orders
WHERE purch_amt >= 2000 AND purch_amt <=6000
ORDER BY ord_date;
```

**12. Count Orders on '2012-08-17'**

```sql
-- 12. Count Orders on '2012-08-17'
SELECT COUNT(order_no)
FROM Orders
WHERE ord_date = '2012-08-17';
```

<center> * * * </center>