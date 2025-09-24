
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:

- Define DQL Clauses
- Understand the purpose of `WHERE` , `ORDERBY` and `GROUPBY`


</details>
<details><summary>Description</summary>
<br>

- `WHERE` clause is used to filter the data from the table based on user needs.
- `GROUP BY` clause is used in MySQL queries to organize records which have same attribute values.
- `ORDER BY` clause is used in MySQL queries to return the records in a sorted manner. By default, it returns in ascending order, which can also be specified as `ASC`. To return in descending order, We mention `DESC` after the expression along with `ORDER BY`.
- The difference between `ORDER BY` and `GROUP BY`

| ORDER BY | GROUP BY |
| ------------- | ------------- |
| It ensures presentation of columns  | It ensures presentation of rows  |
| It is always used after the GROUP BY clause in SELECT statement |  It is always used before the ORDER BY clause in SELECT statement  |
| It is not mandatory to use aggregate functions in the ORDER BY | It is mandatory to use aggregate functions in the GROUP BY  |
| The output is sorted based on the column's attribute values | The grouping of records is done based on the similarity among the row's attribute values |

</details>
<details><summary>Real World Application</summary>
<br>

Consider a scenario where we want to know the employee's salary in a particular department and organize results in descending order based on the department column. In the case, we would need both the group by and order by clause to get the desired result.

</details>
<details><summary>Implementation</summary> 
<br>

- The Syntax to use `WHERE` clause is:

``` sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

Example:

``` sql
SELECT title
FROM movies
WHERE ticket_price=200;
```

- The Syntax to use `ORDER BY` clause is:

``` sql
SELECT expressions    
FROM tables    
[WHERE conditions]    
ORDER BY expression [ ASC | DESC ];    
```

Example:

``` sql
SELECT marks
FROM STUDENTS
WHERE marks>60
ORDER BY marks DESC;
```

- The Syntax to use `GROUP BY` clause is:

``` sql
SELECT column_name, function(column_name)  
FROM table_name   
WHERE condition   
GROUP BY column_name;  
```

Example 1:

``` sql
SELECT Dept, Salary
FROM Employee
WHERE Salary > 15000
GROUP BY employee.salary, employee.dept
ORDER BY Dept DESC;
```
Example 2:

``` sql
SELECT Dept, AVG(Salary) as AvgSalary
FROM Employee
WHERE Salary > 15000
GROUP BY employee.dept
ORDER BY Dept DESC;
```
#### Let's break down the differences:

Column Selection:

- **Example 1:** Selects individual Dept and Salary values.
- **Example 2:** Selects Dept and the average Salary for each department.

GROUP BY clause:
        
- **Example 1:** Groups by both salary and department, which doesn't change the result set.
- **Example 2:** Groups only by department, allowing for aggregation of salaries within each department.

Aggregation:

- **Example 1:** No aggregation is performed.
- **Example 2:** Uses AVG() to calculate the average salary for each department.

#### When to use each approach:

**Example 1:**

- Use when you want to see individual salary records for each employee in departments where at least one employee earns more than $15,000.
- It's essentially equivalent to removing the GROUP BY clause entirely, as it doesn't change the result set.
- This query might be useful for getting a detailed view of high-earning employees across departments.

**Example 2:**

- Use when you want to analyze salary data at the department level.
- It provides a summary view, showing the average salary for each department (considering only salaries above $15,000).
- This is useful for comparing compensation across departments or identifying departments with higher average salaries.

#### The key difference is the level of detail and the type of analysis you're performing:

- The **Example 1** query gives you a granular view of individual salaries.
- The **Example 2** query provides an aggregated view, summarizing salary data by department.

</details>
<details><summary>Summary</summary> 

<br>

- The `WHERE` clause is not only used in `SELECT` statements, it is also used in `UPDATE`, `DELETE` as well
- The `ORDER BY` clause sorts the result and shows it in ascending or descending order
- The `GROUP BY` clause is used to group data based on the exact value in a specific field


</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
