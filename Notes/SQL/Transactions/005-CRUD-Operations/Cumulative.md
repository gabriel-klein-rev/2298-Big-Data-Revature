
<details><summary>Learning Objectives</summary>

<br>

After completing this module, associates should be able to:
- Define all CRUD Operations
- Understand which SQL commands are associated with each operation
- Implement the use of each of these

</details>
<details><summary>Description</summary>

<br>

CRUD operations are the foundation of any computer programming language that is based on the four operations used to implement persistent storage for applications such as a relational database. These operations are not strictly for SQL, but can also be utilized by NoSQL as well. CRUD stands for the following:
- **C**reate: `CREATE` & `INSERT` commands from SQL allow us to facilitate this operation
- **R**ead: `SELECT` command from SQL allow us to facilitate this operation
- **U**pdate: `UPDATE` command from SQL allow us to facilitate this operation
- **D**elete: `DELETE` command from SQL allow us to facilitate this operation


</details>
<details><summary>Real World Application</summary>
<br>

You cannot interact with databases without using CRUD operations are they are essential for anything requiring persistant storage. Even Web Developers wouldn't be able to use REST, a superset of CRUD, to access HTTP requests and responses. CRUD is also crucial for the end-user to perform actions on the site they are visiting, creating bookmarks and interacting with anyone on the internet. CRUD Operation helps businesses faciliate control of security by satisifying various access requirements and simplify design to allow for more scalability and better performance.

</details>
<details><summary>Implementation</summary> 
<br>

- Basic Syntax for **C**reate Operations you've seen previously

```sql
CREATE TABLE TABLE_NAME (
    col_1 INT PRIMARY KEY, 
    col_2 VARCHAR(20), 
    col_N INT
);

INSERT INTO TABLE_NAME (column1, column2, columnN)
VALUES (value1, value2, valueN);
```

- Basic Syntax for **R**ead Operations you've seen previously

```sql
SELECT * FROM TABLE_NAME;

SELECT col_1, col_N
FROM TABLE_NAME
WHERE id = 1;
```

- Basic Syntax for **U**pdate Operations you've seen previously

```sql
UPDATE TABLE_NAME
SET column1 = value1, column2 = value2, columnN = valueN
WHERE [condition]
```

- Basic Syntax for **D**elete Operations you've seen previously

```sql
DELETE FROM TABLE_NAME
WHERE [condition];
```
</details>
<details><summary>Summary</summary> 
<br>

Understanding CRUD operations allow developers to build powerful web applications that can persist and retrieve information rapidly and easily from a database. 

CRUD:
- **C**reate: `CREATE` & `INSERT` commands from SQL allow us to facilitate this operation
- **R**ead: `SELECT` command from SQL allow us to facilitate this operation
- **U**pdate: `UPDATE` command from SQL allow us to facilitate this operation
- **D**elete: `DELETE` command from SQL allow us to facilitate this operation
</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
