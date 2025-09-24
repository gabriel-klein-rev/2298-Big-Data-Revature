
<details><summary>Learning Objectives</summary>
<br>

After completing this module, associates should be able to:

- To define and implement Composite key

</details>
<details><summary>Description</summary>

## Composite Key

- Composite key is a combination of columns used to uniquely identify a table.
- A composite key can also be a combination of candidate keys.
- A group of all the foreign keys can also be used to uniquely identify a table, even in this scenario is also considered a composite key.


</details>
<details><summary>Real World Application</summary>
<br>

Consider a scenario where there is a `student` table, `mentor` table, and another table named `mentor_mentee`. A student can have multiple mentors, and a mentor can have multiple students. In this type of relationship, the `mentor_mentee` table stores pairings between a student and their mentor. Records in the student table can be uniquely identified by `student id`, records in mentor table can be identified by `mentor id`, but the table `mentor_mentee` needs both `student id` and `mentor id` to uniquely identify a record. Both `student id` and `mentor id` are grouped as a primary key.

</details>
<details><summary>Implementation</summary> 
<br>

Below is an example of using a composite key.

## Step 1: Create the tables called employee, client, and branch.

``` sql
CREATE TABLE employee(
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    manager_id INT,
    FOREIGN KEY(manager_id) REFERENCES employee(employee_id) ON DELETE SET NULL
    );
CREATE TABLE client(
    client_id INT PRIMARY KEY,
    client_name VARCHAR(20),
    branch_id INT,
    FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL

);
CREATE TABLE branch (
  branch_id INT PRIMARY KEY,
  client_name VARCHAR(40),
  manager_id INT,
  FOREIGN KEY(manager_id) REFERENCES employee(employee_id) ON DELETE SET NULL
);
```
## Step 2: Create a table works_with

``` sql
CREATE TABLE works_with (
  employee_id INT,
  client_id INT,
  sales INT,
  PRIMARY KEY(employee_id, client_id),
  FOREIGN KEY(employee_id) REFERENCES Employee(employee_id) ON DELETE CASCADE,
  FOREIGN KEY(client_id) REFERENCES Client(client_id) ON DELETE CASCADE
);
```
In the above table `works_with`, `employee_id` and `client_id` are combined to create a composite key.

</details>
<details><summary>Summary</summary> 
<br>

- Composite key is a combination of columns used to uniquely identify a table.
- A composite key can also be a combination of candidate keys.
- A group of all the foreign keys can also be used to uniquely identify a table, even in this scenario is also considered a composite key.

</details>
<details><summary>Practice Questions</summary>

[Practice Questions](./Quiz.gift)</details>
