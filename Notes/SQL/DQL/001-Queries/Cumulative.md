
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:


- Define basic queries in MySQL

</details>
<details><summary>Description</summary>
<br>

Basic queries are important to work in many websites and applications, and are at the core of how data is stored and transferred across the internet. In RDBMS, a query is any command used to retrieve data from a table. Queries are almost always made using the SELECT statement.

In this module, we will discuss the basic syntax of SQL queries. We will also practice some important SQL queries using simple examples.

List of most widely used MySQL queries include:

- `CREATE` database
- `USE` database
- `CREATE` table
- `INSERT` values
- `UPDATE` record
- `DELETE` record
- `SELECT` record
- `TRUNCATE` table
- `DROP` table

</details>
<details><summary>Real World Application</summary>
<br>

The ability to write SQL queries is crucial for various reasons:

- __Data Retrieval__: SQL queries are used to retrieve data from databases. Being able to write SQL queries allows you to extract the information you need from large datasets efficiently and accurately.

- __Data Manipulation__: SQL queries can also be used to manipulate data in databases. With SQL, you can insert, update, or delete records in tables, allowing you to modify the data according to your requirements.

- __Data Analysis__: SQL queries enable data analysis by allowing you to perform calculations, aggregations, and filtering operations on datasets. You can use SQL to summarize data, calculate statistics, and generate reports to gain insights into the underlying data.

- __Database Administration__: SQL queries are essential for database administration tasks such as creating and modifying database schema, managing users and permissions, and optimizing database performance. Database administrators rely on SQL to maintain and manage databases effectively.

In summary, the ability to write SQL queries is essential for developers working with relational databases and it empowers individuals to interact with databases effectively and leverage the full potential of their data assets.
</details>
<details><summary>Implementation</summary> 
<br>

Syntax to create database:

``` sql
CREATE DATABASE WORK;
```

Syntax to select/use database:

``` sql
USE WORK;
```

Syntax to create TABLE:

``` sql
CREATE TABLE EMP
(id INT, NAME VARCHAR(25), AGE INT, PRIMARY KEY(id));
```

Syntax to alter TABLE:

``` sql
ALTER TABLE EMP
ADD SALARY DOUBLE;
```

Syntax to insert values:

``` sql
INSERT INTO EMP VALUES(111, "Ryan", 24, 5000);
```

Syntax to update record:

``` sql
UPDATE EMP SET AGE = 23 WHERE id = 111;
```

Syntax to delete record:

``` sql
DELETE FROM EMP WHERE id = 111;
```

Syntax to select record:

``` sql
SELECT * FROM EMP;
```

Syntax to truncate table:

``` sql
TRUNCATE TABLE EMP;
```

Syntax to drop table:

``` sql
DROP TABLE EMP;
```

</details>
<details><summary>Summary</summary> 
<br>

In this module, we have implemented the following:


- `CREATE` database
- `USE` database
- `CREATE` table
- `INSERT` values
- `UPDATE` record
- `DELETE` record
- `SELECT` record
- `TRUNCATE` table
- `DROP` table


</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
