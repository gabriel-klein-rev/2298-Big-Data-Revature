
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:

- You will learn how to `CREATE`, `DROP`, `TRUNCATE` and `ALTER` a table in MySQL database.
- Understand the difference between `TABLE` and `DATABASE`.
- You will learn what a `TUPLE` is.

</details>
<details><summary>Description</summary>
<br>

- In MySQL, a table stores and organizes data in columns and rows as defined during table creation.
- The `CREATE TABLE` command is used to create a new table in a database.
- The `DROP TABLE` command is used to completely remove the table from database.
- The `TRUNCATE TABLE` command is used to remove all the data and not the table itself.
- The `ALTER TABLE` command is used to alter the table.

- The major differences between a database and a table are as follows:

    - Tables are a way to represent the division of information in a database while, database is a collection of tables and records.
    - Tables are used to group the records in relation with each other and create a dataset. This dataset will be used in the database. The data which are stored in the table in any form is a part of the database, but the vice-versa is not true.

- `TUPLE` - A tuple refers to an ordered set of values. The number of values, or elements, in a tuple is fixed and is known as the arity of the tuple (arity - refers to number of columns in a table). Each value in the tuple is often called an attribute or a component.

In the context of databases and relational database management systems (RDBMS), a tuple is equivalent to a row in a table. Each tuple represents a single record, and the values in the tuple correspond to the attributes or columns of that record.

For example, consider a simple table representing employees:

Employee Table

| EmployeeID | FirstName | LastName | Age | Salary |
|------------|-----------|----------|-----|--------|
| 1          | Susie     | Que      | 30  | 50000  |
| 2          | Billy     | Bob      | 25  | 60000  |
| 3          | Bacon     | Hamburger| 35  | 75000  |

In this table, each row is a tuple. For instance, the first tuple (or row) is (1, "Susie", "Que", 30, 50000), where each value corresponds to a specific attribute such as EmployeeID , FirstName, LastName, Age, and Salary.

Tuples are used in various areas of computer science, including databases, programming languages, and mathematical modeling, where the concept of an ordered set of values is fundamental.
</details>
<details><summary>Real World Application</summary>

<br>

- A table is used in all forms of statistical report in today's world. 
- It's a sequence of labeled columns of data. 
- It can be used to both store and display data in a structured format.


</details>
<details><summary>Implementation</summary> 
<br>

The general syntax for creating a table in MySQL is:

``` sql
CREATE TABLE [IF NOT EXISTS] table_name(  
    column_definition1,  
    column_definition2,  
    ........,  
    table_constraints  
);
```
Example:

``` sql
CREATE TABLE movies(m_name VARCHAR(45) NOT NULL,m_genre VARCHAR(20) NOT NULL,m_director VARCHAR(30) NOT NULL,m_year INT NOT NULL,PRIMARY KEY(m_name));
```
Add values to the newly created table.

``` sql
INSERT INTO movies VALUE("Mr.Bean", "comedy", "Mr.ABC", 2019);
INSERT INTO movies VALUE("Fox", "horror", "Mr.XYZ", 2020);
```

### DROP vs TRUNCATE

The general syntax for dropping a table in MySQL is:


``` sql
DROP TABLE table_name;
```

We use `DROP` command to completely remove the table. Example:

``` sql
DROP TABLE movies;
```

The general syntax for truncating a table in MySQL is:


``` sql
TRUNCATE TABLE table_name;
```
The `TRUNCATE` command is used to delete the data inside a table, but not the table itself. Example:

``` sql
TRUNCATE TABLE movies;
```

### Modifying structure


To `ADD` a column:

``` sql
ALTER TABLE table_name
ADD column_name datatype;
```

We use `ALTER TABLE` command to modify a table. Example:

``` sql
ALTER TABLE movies
ADD ticket_price INT;
```

To `DROP` a column:

``` sql
ALTER TABLE table_name
DROP COLUMN column_name;
```
Example:

``` sql
ALTER TABLE movies
DROP COLUMN m_genre;
```

To `MODIFY` a column:

``` sql
ALTER TABLE table_name
MODIFY COLUMN column_name datatype;
```

Example:

``` sql
ALTER TABLE movies
MODIFY COLUMN ticket_price double;
```


</details>
<details><summary>Summary</summary> 
<br>

After reading this module, you will be able to differentiate `TABLE` with `DATABASE`, and describle the following:

- `CREATE` a table.
- `DROP` a table.
- `TRUNCATE` a table.
- `ALTER` a table. 

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
