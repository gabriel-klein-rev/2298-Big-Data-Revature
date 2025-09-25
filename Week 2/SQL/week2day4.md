# Week 2 Day 4 Notes

### Constraints
Constraint - A rule in schema that defines some limitation about the data. For instance: UNIQUE which tells the database engine that no data can be inserted or modified in this column if it would break the UNIQUE rule, that there can only be one of each value in that column.
 - PRIMARY KEY - Sets the primary index on the table and gurantees that every row can be uniquely identified. Implies INDEXED, UNIQUE, & NOT NULL
 - FOREIGN KEY - Sets a reference and enforces referential integrity. 
 - UNIQUE - Every value in the column must be unique.
 - NOT NULL - The column cannot hold `null` values.
 - DEFAULT - Sets a default value, if a `null` value would be inserted, replace it with the default instead. Works well with NOT NULL, but doesn't work with UNIQUE
 - Data type - we can only insert the proper type of data in a column

### Nested Queries
Queries within queries. You can use the results from an inner query for your outer query. You could go many levels deep in this way, having a query inside a query inside a query and so on. You could use multiple subqueries in sequence as well. There are several ways to use subqueries:

#### Single-Value
```SQL
-- Find employees earning more than the average salary
SELECT name, salary 
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);
```
Here we get one value back from the nested query, and that is used to filter the outer query.

#### Multi-Value
```SQL
-- Find employees in departments located in New York
SELECT name 
FROM employees 
WHERE department_id IN (
    SELECT dept_id 
    FROM departments 
    WHERE city = 'New York'
);
```
Here we use the inner query to produce a list of `dept_id`s found in New York. Simlar to above, that list is then used to filter the outer query.

#### Inline View
```SQL
-- Find cities that start with 'A' from countries that start with 'A'
SELECT city, country
FROM (
    SELECT ci.city, co.country 
    FROM city ci
    JOIN country co ON ci.country_id = co.country_id
    WHERE co.country LIKE 'A%'
) A
WHERE city LIKE 'A%';
```
This basically makes a "view", or a temporary table from a result set. Then we query from that view. In this case we find all countries that start with the letter 'A', and use that result set like a table (a view) to query all cities that start with 'A' from the results of that subquery. 

### Distinct
Distinct - SQL keyword used in a query to only select one of each value from a column, if more of the same values are encountered, they are not included in the seleciotn.

### Delete, Drop, & Truncate
 - Delete - DML - Remove data from a table one row at a time with the potential to filter using WHERE clause.
 - Drop - DDL - Drops the whole table, which necessarioly ejects all data in that table.
 - Truncate - DDL(?!) - This apparently counts as DDL because of the way it ejects data. Removes all data from the table by de-allocating "data pages" (the actual blocks of data). Another reason TRUNCATE is DDL is that it impacts table schema, like resetting auto incrementing sequences. The result is that the data in a table is changed (deleted) but the way this is done is by modifying the underlying structure of the database.


### Alter Table
We can alter anything about the table schema just like when creating the table, but this becomes difficult if the table has data already within, as that data cannot be in violation of new constraints. In that case the alter table command will fail.
 - add or remove columns
 - change the names of columns
 - change the constraints and data types
 - add or remove foreign keys (which are just more constraints)

### ACID - Transaction Properties
 - Atomicity - The transaction is applied atomically, cannot be inturrupted, either occurs fully or not at all.
 - Consistency - All database changes must go from a consistent (obeying the rules and constraints) state to a consistent state. No inturruptions or mistakes can take your database to an inconsistent state.
 - Isolation - Two transactions in parallel (happening at the exact same time) should not interfere with eachother.
 - Durability - Any completed transactions are permenant, and incomplete transactions don't modify the state at all until fully committed, where they become permenant.



### Group By 
GROUP BY groups rows that have the same values in specified columns into summary rows. It's used with aggregate functions to perform calculations on each group separately.
 - Creates one result row per unique combination of grouped columns
 - Any column in SELECT must either be in GROUP BY or be an aggregate function
 - Aggregate functions operate on each group individually
 - GROUP BY comes after WHERE but before ORDER BY

### Having
HAVING filters groups created by GROUP BY, similar to how WHERE filters individual rows. The key difference is HAVING works on grouped data and can use aggregate functions in its conditions. Where filters before the results are aggregated, and Having filters based on aggregate function output.
 - Used only with GROUP BY
 - Filters results based on the output of aggregate functions
 - Executes after GROUP BY but before ORDER BY

### Functions
Function - Take some input, perform some operation, and produce some output

#### Scalar Functions - one input value, one output value.
 - LCASE() - Converts a string to lowercase letters
 - UCASE() - Converts a string to uppercase letters
 - MID() - Extracts a substring from a string starting at a specified position
 - LEN() - Returns the number of characters in a string
 - ROUND() - Rounds a number to a specified number of decimal places

#### Aggregate Functions - many input values, exactly one output value
 - SUM() - Calculates the total of all values in a column
 - AVG() - Calculates the average (mean) of all values in a column
 - MEDIAN() - Returns the middle value when all values are sorted in order
 - COUNT() - Returns the number of rows or non-null values in a column
 - MIN() - Returns the smallest value in a column
 - MAX() - Returns the largest value in a column

What about NOW()? GeeksforGeeks says this is a scalar function. I suppose we can think of aggregate functions as taking in ONE OR MORE inputs, and producing exactly one output. With NOW() taking in no inputs, we're left with scalar. It's really not important, Kyle just thought this was interesting. He would probably say there's no right answer.


