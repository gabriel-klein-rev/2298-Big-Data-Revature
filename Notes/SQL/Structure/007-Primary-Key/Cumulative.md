
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- To define PRIMARY KEY


</details>
<details><summary>Description</summary>
<br>

- The PRIMARY KEY constraint that is used to uniquely identify each record in a table.
- Primary keys must contain values that are UNIQUE and NOT NULL.
- A table can have only a single primary key.
- Primary keys should not be sensitive information. 
    - For example, although social security numbers are unique, assigning them as primary keys is a security risk.
    
</details>
<details><summary>Real World Application</summary>
<br>

Almost every table has a primary key. A few examples are:

- the employee id in the employee details table is the primary key
- the student id in the student table of a college database is the primary key
- branch id of any company with more than one branch is the primary key

All these are used to uniquely identify the record.
</details>
<details><summary>Implementation</summary> 
<br>

Below is an example of creating a table named `employee` with `employee_id` as primary key

``` sql
 CREATE TABLE employee(
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    emp_role VARCHAR(20)
    );
```
``` sql
DESC employee;
```
The `DESC` or `DESCRIBE` commands describe the table.


result:
| Field       | Type        | Null | Key | Default | Extra |
|-------------|-------------|------|-----|---------|-------|
| employee_id | int         | NO   | PRI | NULL    |       |
| first_name  | varchar(20) | YES  |     | NULL    |       |
| last_name   | varchar(20) | YES  |     | NULL    |       |
| emp_role    | varchar(20) | YES  |     | NULL    |       |


</details>
<details><summary>Summary</summary> 
<br>

- the primary key is used to uniquely identify a record in the table.
- there can be only one primary key for one table
- primary key values should be unique and not null

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
