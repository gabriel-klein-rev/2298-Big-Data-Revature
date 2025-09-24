
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:
- Understand the purpose of aggregate functions in SQL
- Explore different types of aggregate functions and their uses


</details>
<details><summary>Description</summary>
<br>

Aggregate functions in MySQL provide the output as a single value after performing different operations on a set of values.

The 5 most commonly used aggregate functions are given as follows: 


| Aggregate Function  | Descriptions |
| ------------- | ------------- |
| count()  | Returns the number of rows, including rows with NULL values in a group.  |
| sum()  |  Returns the total summed values in a set.  |
| avg()  | Returns the average value of an expression.  |
| min()  | Returns the minimum (lowest) value in a set.  |
| max()  | Returns the maximum (highest) value in a set.  |

</details>
<details><summary>Real World Application</summary>

<br>

Real world applications include:

- Bank Management system: Finding the count of all accounts in a bank.
- Employee management system: finding the average salary of all employees.
- Student report: Finding the minimum and maximum marks scored in a specific course.


</details>
<details><summary>Implementation</summary> 

### Examples

Counting the amount of records in a table:
```SQL
SELECT COUNT(*) FROM EMP;    
```

Counting the values of a particular column:
```SQL
SELECT COUNT(EMP_NAME) FROM EMP;   
```

Finding the sum of all values from a specific field:
```SQL
SELECT SUM(duration) AS "Total duration" FROM EMP;
```

Calculating the average of the values from specified columnL
```SQL
SELECT AVG(salary) FROM EMP;
```

Finding the minimum salary:
```SQL
SELECT MIN(salary) FROM EMP;    
```

Finding the maximum salary:
```SQL
SELECT MAX(salary) FROM EMP; 
```
</details>
<details><summary>Summary</summary> 
<br>

- MySQL aggregate functions retrieve a single value after performing a calculation on a set of values.
- In general, aggregate functions ignore null values.
- Often, aggregate functions are accompanied by the GROUP BY clause of the SELECT statement.


</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
