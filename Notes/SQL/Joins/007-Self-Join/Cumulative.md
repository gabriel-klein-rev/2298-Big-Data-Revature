
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- Describe the use of `SELF JOIN` in a database
- Make use of `SELF JOIN` in SQL queries


</details>
<details><summary>Description</summary>
<br>

- `SELF JOIN` is an SQL statement which is used to intersect or join a table in the database to itself. We use it when we need to compare data within the same table. 
- This type of joining of data with other data in the same table when a condition is matched is also known as something called a Unary relationship.


![self](images/Self-join.jpg)

**Syntax**:   
SELECT column_name(s)  
FROM table1 T1, table1 T2  
WHERE condition;  

</details>
<details><summary>Real World Application</summary>
<br>

Real world applications include:

- To query the hierarchical data and comparing records of official reports.
- The main application of this join in MySQL is when we have a table reference data rows in itself.


</details>
<details><summary>Implementation</summary> 
<br>

In the following example our database will have one table since a `SELF JOIN` is a type of join wherein the data is coming from a single table.

Table: Employees

|employee_id|employee_name       |manager_id|
-----------|--------------------|----------|
|1|CEO                 |          |
|2|Marketing Manager   |         1|
|3|Sales Manager       |         1|
|4|Marketing Specialist|         2|
|5|Sales Representative|         3|
|6|Marketing Intern    |         2|

Using the records from this table, we would like to retrieve our employees and readable information for each employee’s associated manager in the company.

A `SELF JOIN` query will accomplish this task perfectly:

```sql
SELECT e.employee_name AS employee, m.employee_name AS manager  
FROM employees e  
JOIN employees m ON e.manager_id = m.employee_id  
ORDER BY e.employee_id;
```

Note that we can also execute the same logic by utilizing a query without the `JOIN` keyword:

```sql
SELECT e.employee_name AS employee, m.employee_name AS manager  
FROM employees e, employees m  
WHERE e.manager_id = m.employee_id  
ORDER BY e.employee_id;  
```

OUTPUT:
|employee            |manager          |
|--------------------|-----------------|
|Marketing Manager   |CEO              |
|Sales Manager       |CEO              |
|Marketing Specialist|Marketing Manager|
|Sales Representative|Sales Manager    |
|Marketing Intern    |Marketing Manager|

Both examples utilize a `SELF JOIN`. An important note however is that the CEO record is not returned from the query due to the `NULL` foreign key reference and the behavior of a simple `SELF JOIN` or a where clause. If we require the CEO data in the result set, we can re-structure our `SELF JOIN`.

For instance, if we perform a `LEFT JOIN` we can pull data with null references. As a note and to clarify any confusion this is still a `SELF JOIN` since we are performing a join referencing a single table.

```sql
SELECT e.employee_name AS employee, m.employee_name AS manager
FROM employees e
LEFT JOIN employees m 
ON e.manager_id = m.employee_id
ORDER BY e.employee_id;
```

|employee            |manager          |
|--------------------|-----------------|
|CEO                 |NULL             |
|Marketing Manager   |CEO              |
|Sales Manager       |CEO              |
|Marketing Specialist|Marketing Manager|
|Sales Representative|Sales Manager    |
|Marketing Intern    |Marketing Manager|

To accomplish the same output without the use of the `JOIN` keyword, we’ll need a more complex version of this query:

```sql
-- Without JOIN
SELECT e.employee_name AS employee,
( SELECT employee_name
  FROM employees m
  WHERE m.employee_id = e.manager_id) AS manager
FROM employees e
ORDER BY e.employee_id;
```
|employee            |manager          |
|--------------------|-----------------|
|CEO                 |NULL             |
|Marketing Manager   |CEO              |
|Sales Manager       |CEO              |
|Marketing Specialist|Marketing Manager|
|Sales Representative|Sales Manager    |
|Marketing Intern    |Marketing Manager|

Each example demonstrates how we can use a single table and query data on itself. 
</details>
<details><summary>Summary</summary> 
<br>

- `SELF JOIN` is important to query ordered records by comparing rows in the same table.
- We can make use of `SELF JOIN` considering the table as two using an alias so that the table name is not repeated two times which may lead to an error.
- This type of join is useful for modeling an organized structured data form which also allows comparing the rows and produce the required output.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
