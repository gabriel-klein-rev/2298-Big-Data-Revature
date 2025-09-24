
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- Describe the different types of subqueries
- Write subqueries

</details>
<details><summary>Description</summary>
<br>

- A SQL subquery is a query nested inside of a larger query. A subquery can occur in various subsections of a query:

    - SELECT clause (Inner Query)
    - WHERE clause (Nested Query)
    - FROM clause (Inline View)

- Subqueries can be nested in a `SELECT`, `INSERT`, `UPDATE`, `DELETE`, or even inside of another subquery.
- Logical operators can be used to compare the results of the subquery
- Nested queries can return single or multiple rows
- Inline views create temporary tables
- Inner queries create temporary columns on the result set
    - The column created by the inner query has a value equal to the result of the query
- The subquery can also be called `inner query` or `inner select` while the container query is called the `outer query` or `outer select`
- The `inner query` executes before the `outer query`
- Subqueries are convenient, but perform worse than joins.


</details>
<details><summary>Real World Application</summary>
<br>

Subqueries can be a convenient way of gathering information between related tables. However, in many cases the same data can be queried using a join. It is a better practice to prefer a join over a subquery since joins execute faster by replacing multiple queries with a single one.

It isn't often that you will find a subquery being used where a join could perform the same work, faster.

</details>
<details><summary>Implementation</summary> 
<br>

For the following demonstrations, use the below table:

```SQL
CREATE TABLE IF NOT EXISTS students(
    id INT PRIMARY KEY,
    name VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS evals (
    id INT PRIMARY KEY,
    studentId INT NOT NULL,
    evalName VARCHAR(10) NOT NULL,
    mark INT DEFAULT 0,
    FOREIGN KEY(studentId) REFERENCES students(id),
    CONSTRAINT mark_check CHECK(mark >= 0), CHECK(mark <= 100)
);

INSERT INTO students (id, name) VALUES (1, 'Steve'), (2, 'Jane'), (3, 'Casey');
INSERT INTO evals (id, studentId, evalName, mark) VALUES (1, 1, 'quiz 1', 98),
 (2, 2, 'quiz 1', 80), 
 (3, 3, 'quiz 1', 95), 
 (4, 1, 'test 1', 72), 
 (5, 2, 'test 1', 100), 
 (6, 3, 'test 1', 68);
```

## Nested Queries

A nested query is a subquery found in the `WHERE` clause of the `outer query`.

```sql
SELECT col1, ... FROM table_ref WHERE (subquery);
```

Using the students schema lets find all students that scored higher than Jane (2) on quiz 1. The problem is, we don't know what Jane scored on quiz 1. There is a simple solution for this first problem.

```sql
SELECT studentId, evalName, mark  FROM evals WHERE studentId = 2 AND evalName = 'quiz 1';
```


| studentId | evalName | mark |
|-----------|----------|------|
| 2         | quiz 1   | 80   |


Knowing this information we could write a simple query to obtain the other information.

```sql
SELECT studentId, evalName, mark FROM evals WHERE evalName = 'quiz 1' AND mark > 80;
```

| studentId | evalName | mark |
|-----------|----------|------|
|         1 | quiz 1   |   98 |
|         3 | quiz 1   |   95 |


There is a problem with the second query, it isn't reusable. We can write the solution to use a subquery to make it more reusable where only the studentId and eval name would need to be known.

```sql
SELECT a.id, a.name, b.evalName, b.mark FROM students a, evals b WHERE a.id = b.studentId
    AND b.evalName = 'quiz 1'
    AND b.mark > (SELECT mark FROM evals WHERE evalName = 'quiz 1' AND studentId = 2);
```


| id | name  | evalName | mark |
|----|-------|----------|------|
|  1 | Steve | quiz 1   |   98 |
|  3 | Casey | quiz 1   |   95 |



The subquery `(SELECT mark FROM evals WHERE evalName = 'quiz 1' AND studentId = 2)` is used to select a single record from the `evals` table. this value is then compared in the `outer query` which is used to filter the final results. It is important that the `inner query` only return a single record because the outer query uses the > operator.

## Inline View

Inline views are subqueries that occur in the `FROM` clause of the `outer query`.

Let's write an inline view where any mark is greater than 90 on any eval.

```sql
SELECT a.name, b.evalName, b.mark FROM students a, (SELECT studentId, evalName, mark FROM evals WHERE mark > 90) b WHERE a.id = b.studentId;
```


| name  | evalName | mark |
|-------|----------|------|
| Steve | quiz 1   |   98 |
| Casey | quiz 1   |   95 |
| Jane  | test 1   |  100 |


The subquery `(SELECT studentId, evalName, mark FROM evals WHERE mark > 90)` creates a temporary table, called an inline view. That inline view is used in the outer query to select records from.

## Inner query

An Inner query is a subquery found in the `SELECT` clause of the outer query. This creates a temporary column on the result set where the value of that column is provided by the inner query.

Let's write an inner query to get the average score for each student on all exams.

```sql
SELECT a.id, a.name, (SELECT AVG(mark) FROM evals WHERE studentId = a.id GROUP BY studentId) avg FROM students a;
```



| id | name  | avg     |
|----|-------|---------|
|  3 | Casey | 81.5000 |
|  2 | Jane  | 90.0000 |
|  1 | Steve | 85.0000 |


Each of these types of queries have their own advantages, but one of the most observable uses for subqueries is to gather data from related tables. As you can see in the above examples, when the `evals` table was queried in the subquery, the data was bound to the student name from the `students` table making the data more relevant and readable to the end user.


</details>
<details><summary>Summary</summary> 
<br>

Subqueries are queries that are contained in another query. The container query is known as the `outer query` and the subquery is known as the `inner query`. There are 3 types of subqueries

- Nest Query in the `WHERE` clause
- Inline View in the `FROM` clause
- Inner Query in the `SELECT` clause

Important Notes

- Nested queries can return single or multiple rows
- Nested query results can be compared using logical operators
- Inline views create temporary tables
- Inner queries create temporary columns on the result set
- The column created by the inner query has a value equal to the result of the query

Subqueries are convenient, but perform worse than joins.


</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
