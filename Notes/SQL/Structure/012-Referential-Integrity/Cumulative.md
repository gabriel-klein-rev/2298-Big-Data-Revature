
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- To define Referential integrity

</details>
<details><summary>Description</summary>
<br>

- Referential integrity is the relationship between tables. Each table in a database has a primary key and this primary key can appear in other tables because of its relationship to data within other tables. When a primary key from one table appears in another table, it is called a foreign key.
- Referential integrity does not allow the addition of any record in a table that contains the foreign key unless the reference table contains a corresponding primary key.
- Referential integrity does not allow deletion of a record in a table that contains the foreign key. To delete the record in the parent table, the corresponding record in the child table should be deleted first. To solve this issue ON DELETE CASCADE is used. 
- Other options are to set the foreign key to null or to its default value (only if the default value references an existing value in the primary-key table).

</details>
<details><summary>Real World Application</summary>
 <br>

Consider any database, for example, an Office Database with Employee, Branch, and Client tables. Employee table will have a foreign key called branch_id which is the primary key for the Branch table and the Client table will have a foreign key called employee_id which is a Primary key fro Employee table. Any changes made in the Branch table will affect the Employee table. If a branch is closed (deleted), all the employees in that branch are fired (deleted), and if an employee leaves the company(deleted), all the clients of the employee in the Client table are lost (deleted).

</details>
<details><summary>Implementation</summary> 
<br>

step 1: Create a table named Student.

``` sql
 CREATE TABLE Student(
    student_id INT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    Major VARCHAR(20)
    );

```
Step 2: create a table named InternationalStudent.

``` sql
CREATE TABLE InternationalStudent(
    country_id INT PRIMARY KEY,
    name VARCHAR(20),
    student_id INT,
    FOREIGN KEY(student_id) REFERENCES Student(student_id)
    ON DELETE CASCADE
);
```
Step 3: Insert values into Student table and InternationalStudent table.
``` sql
INSERT INTO Student VALUES(1,"Taylor", "Swift","English Literature");
INSERT INTO Student VALUES(2,"Stephen", "Hawking","Physics");
INSERT INTO InternationalStudent VALUES(1,"USA",1);
INSERT INTO InternationalStudent VALUES(2,"UK",2);
```
``` sql
SELECT * FROM InternationalStudent;
```
Result:
| country_id | name  | student_id |
|------------|-------|------------|
|     1      | USA   |          1 |
|     2      | UK    |          2 |

Step 4: delete a record from Student table
``` sql
DELETE FROM Student WHERE Major="English Literature";
```
Now the record in child table InternationalStudent with student_id as 1 is deleted.

``` sql
SELECT * FROM InternationalStudent;
```
Result:
| country_id | name  | student_id |
|------------|-------|------------|
|     2      | UK    |          2 |





</details>
<details><summary>Summary</summary> 
<br>

- Referential integrity  is used to build and maintain logical relationships between tables to avoid logical corruption of data.

- Referential integrity is made up of the combination of a primary key and a foreign key.

- Normally the table with a Primary key is considered as a parent table and the table with a foreign key is considered a child table.

- Updating and Deletion in primary key table and Insertion and Updating in the foreign key table could
violate the referential integrity.

- To avoid violating Referential Integrity, ON DELETE CASCADE, set the foreign key to NULL, or set foreign key to default are implemented.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
