The `EXTRACT` function in SQL is used to **retrieve a specific part of a date or timestamp**, like the year, month, day, hour, etc. Its exact syntax and availability can vary slightly depending on the SQL engine (PostgreSQL, Oracle, MySQL, etc.), but the general idea is the same.

---

## **1. General Syntax**

```sql
EXTRACT(field FROM source)
```

* **field** → the part you want to extract: `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, etc.
* **source** → a date, timestamp, or datetime column.

## **2. Examples**

```sql
SELECT 
    EXTRACT(YEAR FROM date_received) AS year,        -- Extract year
    EXTRACT(MONTH FROM date_received) AS month,      -- Extract month
    EXTRACT(DAY FROM date_received) AS day          -- Extract day
FROM consumer_complaints;
```

### **d) Combine with GROUP BY**

```sql
SELECT 
    EXTRACT(YEAR FROM date_received) AS year,
    EXTRACT(MONTH FROM date_received) AS month,
    COUNT(*) AS complaints
FROM consumer_complaints
GROUP BY year, month
ORDER BY year, month;
```

## **3. Notes by SQL engine**

* **PostgreSQL / Oracle** → supports `EXTRACT` fully.
* **MySQL** → you can use `EXTRACT`, but you can also use `YEAR(date_col)`, `MONTH(date_col)`, etc.
* **SQL Server** → doesn’t support `EXTRACT`; use `DATEPART` instead:

```sql
SELECT DATEPART(YEAR, date_received) AS year,
       DATEPART(MONTH, date_received) AS month
FROM consumer_complaints;
```

---

If you want, I can write a **ready-to-use query to list all months per year as columns** using `EXTRACT` that works for **PostgreSQL**.

Do you want me to do that?
