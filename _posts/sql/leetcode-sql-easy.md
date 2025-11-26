```
Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

```sql
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders);
```

```sql
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL;
```


SELECT name, population, area
FROM World;

WHERE
    area >= 3000000 OR
	population >= 25000000;
	
SELECT * 
FROM Customers;


SELECT CustomerName, City 
FROM Customers;

SELECT DISTINCT Country 
FROM Customers;

SELECT DISTINCT CustomerName, City 
FROM Customers;



library_id INT PRIMARY KEY,
books VARCHAR(100) NOT NULL,
fine FLOAT DEFAULT 0.0,
age INT UNIQUE,

FOREIGN KEY (student_id) REFERENCES students(student_id)


constrints
	

keys

WHERE
orderby
limits

OPERATOR
and, or, not, in, between