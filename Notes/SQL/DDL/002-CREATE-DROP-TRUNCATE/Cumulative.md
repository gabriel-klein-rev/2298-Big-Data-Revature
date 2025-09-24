
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:

- Describe and understand the difference between `CREATE`, `DROP`, and `TRUNCATE`

</details>
<details><summary>Description</summary>
<br>

`CREATE`
- It is part of the DDL sublanguage
- `CREATE` is a command that creates new database objects, like tables, in the database
- Tables are used to store the data in the database with a unique name and schema
    - tables also require at least one column to be valid
    - Each column requires an associated data type
- Certain RDBMS have transactional DDL language that allows you to rollback creates
    - PostgreSQL, SQL Server and SQLite among various others have transactional DDL
    - MySQL and Oracle Database do not support transactional DDL
- Used to also define schemas, procedures, views, indexes and even databases

`DROP`
- It is part of the DDL sublanguage
- The `DROP` command removes the table from the database.
- It removes all the indexes, privileges, rows and frees the memory space for other objects.
- You can not drop the table referenced by foreign key constraint.
- The objects related to the table like views, procedures needs to be explicitly dropped.
- No DML triggers will be fired.
- We can not roll back the drop table operation.

`TRUNCATE`
- It is part of the DDL sublanguage
- It is used to remove all the rows from the table.
- It does not return number of rows truncated from the table.
- It also deallocates the memory for that object and other object will use that deallocated space.
- `TRUNCATE` operation can not roll back as it does not operate on each row.
- We cannot use condition when it comes to using `TRUNCATE`.



</details>
<details><summary>Real World Application</summary>
<br>

FOR `CREATE` :

Consider a scenario where we want to create a fresh new table of course information, now when we create, we must specify all the information and appropriate data type for each column of information related to the course information. You can also use `CREATE` for schemas, procedures, views, indexes and even databases.

FOR `TRUNCATE` :

Consider a scenario where we want to delete or remove all records from table named student, now if we truncate, then the table structure remains and all the records will be removed.

FOR `DROP` :
 
Consider a scenario where we want to delete the whole table called Department, then we use `DROP`. Here, all the records and the table structure is completely removed.

</details>
<details><summary>Implementation</summary> 
<br>

- Syntax to `DROP` a table from database

``` sql
DROP TABLE table_name;
```

Example:

``` sql
DROP TABLE Movies;
```

- Syntax to `CREATE` a table 

``` sql
CREATE TABLE table_name{
    table_id INT PRIMARY KEY IDENTITY(1,1),
    table_value VARCHAR (50) NOT NULL,
    table_value INT,
    foreign_key INT
    FOREIGN KEY (foreign_id) REFERENCES foreign_table_name (foreign_id)
}
```

Example:

``` sql
CREATE TABLE courses (
    course_id INT PRIMARY KEY IDENTITY (1, 1),
    course_name VARCHAR (50) NOT NULL,
    max_capacity VARCHAR (50) NOT NULL,
    professor_id INT
    FOREIGN KEY (professor_id) REFERENCES professors (professor_id)
);
```

- Syntax to `TRUNCATE` a table from database

``` sql
TRUNCATE TABLE table_name;
```

Example:

``` sql
TRUNCATE TABLE student;
```

</details>
<details><summary>Summary</summary> 
<br>

| `DROP`  | `CREATE` | `TRUNCATE` |
| ------------- | ------------- | ------ |
| It removes a table form the database | It creates a new table with no information, along with views, procedures, schemas, indexes and databases | It is executed using table lock, where whole table is locked while removing the records |
| It maintains the log, so it is slower than `TRUNCATE` | It maintains the log | Least amount of logging needed so it is faster in performace |
| It cannot be rolled back | It cannot be rolled back | It cannot be rolled back |

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
